#!/usr/bin/env python3
"""
Fetch external Confluence pages + logo integration + resolve display/HERCULES/Title links.
"""
import re, time, unicodedata, shutil
from pathlib import Path
from urllib.parse import unquote_plus, unquote
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

DOCS   = Path("docs")
SPEC   = Path("/home/lmatarrubia/Descargas/hercules-docs-mv-specs.txt")
LOGO   = Path("/home/lmatarrubia/Descargas/HÉRCULES_logo.png")
EXTERN = DOCS / "hercules" / "referencias-externas"
BASE   = "https://confluence.um.es/confluence"

# ── helpers ───────────────────────────────────────────────────────────

def slugify(s):
    s = s.lower()
    s = unicodedata.normalize("NFD", s)
    s = re.sub(r"[̀-ͯ]", "", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = s.strip()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s

def page_title_from_soup(soup):
    t = soup.find("title")
    if not t: return ""
    return re.sub(r"\s*[-|].*Confluence.*$", "", t.text.strip()).strip()

def shift_headings(md):
    def repl(m):
        level = min(len(m.group(1)) + 1, 6)
        return "#" * level + m.group(2)
    return re.sub(r"^(#{1,6})([ \t].*)$", repl, md, flags=re.MULTILINE)

def dest_url(path_str):
    url = re.sub(r'/index\.md$', '', path_str)
    url = re.sub(r'\.md$', '', url)
    return '/' + url

# ── cargar spec ───────────────────────────────────────────────────────

numid_to_dest = {}
slug_to_dest  = {}

with open(SPEC) as f:
    for line in f:
        parts = line.strip().split(" ", 1)
        if len(parts) != 2: continue
        raw, dest = parts
        m = re.search(r'(\d+)$', raw)
        if m: numid_to_dest[m.group(1)] = dest
        # Build slug from dest path for title matching
        basename = re.sub(r'(/index)?\.md$', '', dest).split('/')[-1]
        slug_to_dest[basename] = dest

# ── FIX A: logo ───────────────────────────────────────────────────────

print("Logo: copiando…")
assets = DOCS / "assets"
assets.mkdir(exist_ok=True)
shutil.copy(LOGO, assets / "logo.png")
print(f"  → docs/assets/logo.png")

# Update mkdocs.yml
yml = Path("mkdocs.yml").read_text()
if "logo:" not in yml:
    yml = yml.replace(
        "  language: es",
        "  language: es\n  logo: assets/logo.png\n  favicon: assets/logo.png"
    )
    Path("mkdocs.yml").write_text(yml)
    print("  mkdocs.yml actualizado con logo y favicon")

# ── FIX B: resolver display/HERCULES/Title con slug matching ──────────

print("\nResolviendo links display/HERCULES/Title por slug…")

display_pattern = re.compile(
    r'https?://confluence\.um\.es/confluence/display/HERCULES/([^#\s\)"\'>]+)(#[^\s\)"\'>]*)?'
)

def resolve_display(title_encoded, fragment=""):
    title = unquote_plus(title_encoded).strip()
    slug  = slugify(title)
    dest  = slug_to_dest.get(slug)
    if dest:
        url = dest_url(dest)
        return url + (fragment or "")
    return None

resolved_display = 0
files_changed = 0

for md_file in DOCS.rglob("*.md"):
    content = md_file.read_text(encoding="utf-8")
    def replace_display(m):
        global resolved_display
        new = resolve_display(m.group(1), m.group(2) or "")
        if new:
            resolved_display += 1
            return new
        return m.group(0)
    new_content = display_pattern.sub(replace_display, content)
    if new_content != content:
        md_file.write_text(new_content, encoding="utf-8")
        files_changed += 1

print(f"  {resolved_display} links display/HERCULES/Title resueltos en {files_changed} ficheros")

# ── FIX C: fetch páginas externas por pageId ─────────────────────────

print("\nFetcheando páginas externas de Confluence…")

# Collect all remaining unresolved page IDs
id_pattern = re.compile(
    r'https?://confluence\.um\.es/confluence/pages/viewpage\.action\?pageId=(\d+)'
)
remaining_ids = set()
for md_file in DOCS.rglob("*.md"):
    for pid in id_pattern.findall(md_file.read_text(errors="replace")):
        if pid not in numid_to_dest:
            remaining_ids.add(pid)

print(f"  IDs sin resolver: {len(remaining_ids)}")

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (compatible; HerculesDocsBot/1.0)"
EXTERN.mkdir(parents=True, exist_ok=True)

fetched_map = {}   # pid → local_dest_path (e.g. hercules/referencias-externas/slug.md)
failed = []

for i, pid in enumerate(sorted(remaining_ids), 1):
    url = f"{BASE}/pages/viewpage.action?pageId={pid}"
    try:
        resp = session.get(url, timeout=15, allow_redirects=True)
        if resp.status_code != 200:
            failed.append((pid, resp.status_code))
            continue

        soup = BeautifulSoup(resp.text, "lxml")

        # Check if login wall
        if soup.find("form", {"id": "loginform"}) or "login" in resp.url:
            failed.append((pid, "login-required"))
            continue

        title = page_title_from_soup(soup)
        mc = soup.find(id="main-content")
        if not mc:
            failed.append((pid, "no-main-content"))
            continue

        # Extract content
        content_html = str(mc)
        md = md_convert(content_html, heading_style="atx", keep_inline_images_in=["body"])
        md = shift_headings(md)
        if title:
            md = f"# {title}\n\n{md.lstrip()}"

        slug = slugify(title) if title else f"pagina-{pid}"
        dest = EXTERN / f"{slug}.md"
        # Avoid collisions
        if dest.exists():
            dest = EXTERN / f"{slug}-{pid}.md"
        dest.write_text(md, encoding="utf-8")

        rel_path = str(dest.relative_to(DOCS))
        fetched_map[pid] = rel_path
        numid_to_dest[pid] = rel_path   # add to map for link replacement

        if i % 20 == 0 or i == len(remaining_ids):
            print(f"  {i}/{len(remaining_ids)} — último: {title[:50] if title else pid}")

        time.sleep(0.4)

    except Exception as e:
        failed.append((pid, str(e)[:60]))

print(f"  Páginas obtenidas: {len(fetched_map)}")
print(f"  Fallidas/inaccesibles: {len(failed)}")
if failed[:5]:
    print(f"  Ejemplos de fallos: {failed[:5]}")

# ── FIX D: reemplazar pageId URLs con las nuevas rutas locales ────────

if fetched_map:
    print("\nActualizando enlaces a páginas recién obtenidas…")
    viewpage_pattern = re.compile(
        r'https?://confluence\.um\.es/confluence/pages/viewpage\.action\?pageId=(\d+)(#[^\s\)"\'>]*)?'
    )
    updated = 0
    for md_file in DOCS.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        def replace_viewpage(m):
            pid = m.group(1)
            frag = m.group(2) or ""
            if pid in numid_to_dest:
                return dest_url(numid_to_dest[pid]) + frag
            return m.group(0)
        new_content = viewpage_pattern.sub(replace_viewpage, content)
        if new_content != content:
            md_file.write_text(new_content, encoding="utf-8")
            updated += 1
    print(f"  {updated} ficheros actualizados")

# ── resumen final ─────────────────────────────────────────────────────

remaining = sum(
    len(re.findall(r'confluence\.um\.es', md_file.read_text(errors="replace")))
    for md_file in DOCS.rglob("*.md")
)
print(f"\nURLs confluence.um.es pendientes: {remaining} (externas a otro space o sin acceso)")
print("¡Listo!")
