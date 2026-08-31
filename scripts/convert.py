#!/usr/bin/env python3
"""
Confluence HTML export → MkDocs Markdown
Pipeline: extract #main-content → markdownify → move per spec → fix links → mkdocs.yml
"""
import re, sys
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

SOURCE = Path("Confluence-space-export-format-html/HERCULES")
DOCS   = Path("docs")
SPEC   = Path("/home/lmatarrubia/Descargas/hercules-docs-mv-specs.txt")

# ── helpers ───────────────────────────────────────────────────────────

def page_title(soup):
    t = soup.find("title")
    if not t:
        return ""
    return t.text.strip().removeprefix("Hércules : ").strip()

def shift_headings(md):
    """H1→H2, H2→H3, … (clamp at H6)."""
    def repl(m):
        level = min(len(m.group(1)) + 1, 6)
        return "#" * level + m.group(2)
    return re.sub(r"^(#{1,6})([ \t].*)$", repl, md, flags=re.MULTILINE)

def file_id(path):
    return re.sub(r"\.html?$", "", path.name)

# ── step 1: load spec ─────────────────────────────────────────────────

spec = []
with open(SPEC) as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(" ", 1)
            if len(parts) == 2:
                spec.append((parts[0], parts[1]))

id_to_dest = {src: dest for src, dest in spec}
print(f"Spec: {len(spec)} entradas")

# ── step 2: HTML → docs/{pageId}.md ──────────────────────────────────

print("Convirtiendo HTML → Markdown …")
html_files = sorted(f for f in SOURCE.glob("*.html") if f.name != "index.html")
total = len(html_files)

for i, html_file in enumerate(html_files, 1):
    soup = BeautifulSoup(html_file.read_text(errors="replace"), "lxml")
    title = page_title(soup)
    mc = soup.find(id="main-content")
    content_html = str(mc) if mc else ""

    md = md_convert(content_html, heading_style="atx", keep_inline_images_in=["body"])
    md = shift_headings(md)
    if title:
        md = f"# {title}\n\n{md.lstrip()}"

    (DOCS / f"{html_file.stem}.md").write_text(md, encoding="utf-8")
    if i % 200 == 0 or i == total:
        print(f"  {i}/{total}")

print("  Conversión completa.")

# ── step 3: mover ficheros a su destino ───────────────────────────────

print("Moviendo ficheros …")
moved = skipped = 0
for src_id, dest_path in spec:
    src  = DOCS / f"{src_id}.md"
    dest = DOCS / dest_path
    if src.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dest)
        moved += 1
    else:
        skipped += 1
        print(f"  WARN src no encontrado: {src_id}.md")

print(f"  Movidos: {moved}  |  No encontrados: {skipped}")

# ── step 4: reescribir enlaces internos ───────────────────────────────

print("Reescribiendo enlaces …")
replacements = {}
for src_id, dest_path in spec:
    url = re.sub(r"/index\.md$", "", dest_path)
    url = re.sub(r"\.md$",        "", url)
    replacements[f"{src_id}.html"] = f"/{url}"

md_files = list(DOCS.rglob("*.md"))
for md_file in md_files:
    content = md_file.read_text(encoding="utf-8")
    changed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True
    if changed:
        md_file.write_text(content, encoding="utf-8")

print(f"  Procesados {len(md_files)} ficheros.")

# ── step 5: rutas de attachments absolutas ────────────────────────────

print("Fijando rutas de attachments …")
for md_file in DOCS.rglob("*.md"):
    content = md_file.read_text(encoding="utf-8")
    if "](attachments" in content:
        md_file.write_text(content.replace("](attachments", "](/attachments"), encoding="utf-8")

# ── step 6: generar mkdocs.yml ────────────────────────────────────────

print("Generando mkdocs.yml …")

# Leer títulos de los HTML
titles = {}
for html_file in SOURCE.glob("*.html"):
    if html_file.name == "index.html":
        continue
    soup = BeautifulSoup(html_file.read_text(errors="replace"), "lxml")
    titles[file_id(html_file)] = page_title(soup)

# Construir árbol de nav desde index.html (orden original de Confluence)
index_soup = BeautifulSoup((SOURCE / "index.html").read_text(errors="replace"), "lxml")

def nav_node(li):
    a = li.find("a", recursive=False)
    if not a or not a.get("href", "").endswith(".html"):
        return None
    pid   = file_id(Path(a["href"]))
    dest  = id_to_dest.get(pid)
    title = titles.get(pid, pid)
    if not dest:
        return None
    child_uls = li.find_all("ul", recursive=False)
    if child_uls:
        children = []
        for ul in child_uls:
            for child_li in ul.find_all("li", recursive=False):
                node = nav_node(child_li)
                if node:
                    children.append(node)
        if children:
            return {title: [dest] + children}
        else:
            return {title: dest}
    else:
        return {title: dest}

root_ul = index_soup.find("ul")
nav = []
for li in root_ul.find_all("li", recursive=False):
    node = nav_node(li)
    if node:
        nav.append(node)

def yaml_str(s):
    """Quote a string for YAML — always use double quotes, escape internals."""
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def nav_to_yaml(nav, indent=0):
    lines = []
    pad = "  " * indent
    for item in nav:
        if isinstance(item, str):
            lines.append(f"{pad}- {item}")
        elif isinstance(item, dict):
            for k, v in item.items():
                if isinstance(v, list):
                    lines.append(f"{pad}- {yaml_str(k)}:")
                    lines.extend(nav_to_yaml(v, indent + 1))
                else:
                    lines.append(f"{pad}- {yaml_str(k)}: {v}")
    return lines

nav_yaml = "\n".join(nav_to_yaml(nav))

mkdocs_content = f"""# Generado automáticamente — no editar manualmente
site_name: Hércules SGI
docs_dir: docs
theme:
  name: material
  features:
    - navigation.indexes
    - navigation.tabs
    - navigation.top
    - search.highlight
  language: es

plugins:
  - search

markdown_extensions:
  - admonition
  - tables
  - attr_list
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.details

nav:
{nav_yaml}
"""

Path("mkdocs.yml").write_text(mkdocs_content, encoding="utf-8")
print("  mkdocs.yml generado.")
print("¡Listo!")
