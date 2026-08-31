#!/usr/bin/env python3
"""
Fixes post-conversión:
  1. Home page = contenido de hercules/index.md
  2. Nav: secciones raíz como tabs (SGI, Arquitectura, APIs, …)
  3. Páginas vacías: auto-generar lista de hijos
  4. Links externos confluence.um.es → rutas internas cuando sea posible
"""
import re, unicodedata
from pathlib import Path
from bs4 import BeautifulSoup

DOCS   = Path("docs")
SOURCE = Path("Confluence-space-export-format-html/HERCULES")
SPEC   = Path("/home/lmatarrubia/Descargas/hercules-docs-mv-specs.txt")

# ── cargar spec ───────────────────────────────────────────────────────

spec_list = []
id_to_dest = {}   # raw_id  → dest_path (con .md)
numid_to_dest = {}  # numeric → dest_path

with open(SPEC) as f:
    for line in f:
        parts = line.strip().split(" ", 1)
        if len(parts) == 2:
            raw, dest = parts
            spec_list.append((raw, dest))
            id_to_dest[raw] = dest
            m = re.search(r'(\d+)$', raw)
            if m:
                numid_to_dest[m.group(1)] = dest

def dest_url(dest):
    """Convert spec dest path to URL (strip /index.md and .md)."""
    url = re.sub(r'/index\.md$', '', dest)
    url = re.sub(r'\.md$', '', url)
    return '/' + url

# ── helper ────────────────────────────────────────────────────────────

def file_id(href):
    return re.sub(r'\.html?$', '', Path(href).name)

def page_title_from_html(pid):
    f = SOURCE / f"{pid}.html"
    if not f.exists():
        # try compound names
        matches = list(SOURCE.glob(f"*_{pid}.html"))
        if matches:
            f = matches[0]
        else:
            return pid
    soup = BeautifulSoup(f.read_text(errors='replace'), 'lxml')
    t = soup.find('title')
    return t.text.strip().removeprefix('Hércules : ').strip() if t else pid

# ── FIX 1: home page ─────────────────────────────────────────────────

print("Fix 1: home page…")
hercules_index = DOCS / "hercules" / "index.md"
home = DOCS / "index.md"
if hercules_index.exists():
    home.write_text(hercules_index.read_text(encoding='utf-8'), encoding='utf-8')
    print("  docs/index.md ← copia de hercules/index.md")

# ── FIX 2: generar mkdocs.yml con tabs por sección ───────────────────

print("Fix 2: mkdocs.yml con tabs…")

index_soup = BeautifulSoup((SOURCE / "index.html").read_text(errors='replace'), 'lxml')

def nav_node(li, depth=0):
    a = li.find("a", recursive=False)
    if not a or not a.get("href","").endswith(".html"):
        return None
    pid   = file_id(a["href"])
    dest  = id_to_dest.get(pid)
    if not dest:
        m = re.search(r'(\d+)$', pid)
        if m: dest = numid_to_dest.get(m.group(1))
    if not dest:
        return None
    title = page_title_from_html(pid)
    child_uls = li.find_all("ul", recursive=False)
    if child_uls:
        children = []
        for ul in child_uls:
            for child_li in ul.find_all("li", recursive=False):
                node = nav_node(child_li, depth+1)
                if node:
                    children.append(node)
        if children:
            return {"title": title, "path": dest, "children": children}
        else:
            return {"title": title, "path": dest, "children": []}
    else:
        return {"title": title, "path": dest, "children": []}

root_ul = index_soup.find("ul")
root_nodes = []
for li in root_ul.find_all("li", recursive=False):
    node = nav_node(li)
    if node:
        root_nodes.append(node)

# root_nodes[0] = Hércules; its children become tabs
hercules_node = root_nodes[0]
top_sections  = hercules_node["children"]   # SGI, Arquitectura, APIs, …

def yaml_str(s):
    return '"' + s.replace('\\','\\\\').replace('"','\\"') + '"'

def render_nav(nodes, indent=0):
    lines = []
    pad = "  " * indent
    for n in nodes:
        if n["children"]:
            lines.append(f"{pad}- {yaml_str(n['title'])}:")
            lines.append(f"{pad}  - {n['path']}")
            lines.extend(render_nav(n["children"], indent + 1))
        else:
            lines.append(f"{pad}- {yaml_str(n['title'])}: {n['path']}")
    return lines

nav_lines  = [f'- "Hércules": index.md']
for s in top_sections:
    if s["children"]:
        nav_lines.append(f'- {yaml_str(s["title"])}:')
        nav_lines.append(f'  - {s["path"]}')
        nav_lines.extend(render_nav(s["children"], indent=1))
    else:
        nav_lines.append(f'- {yaml_str(s["title"])}: {s["path"]}')

nav_yaml = "\n".join(nav_lines)

mkdocs = f"""# Generado automáticamente — no editar manualmente
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
Path("mkdocs.yml").write_text(mkdocs, encoding='utf-8')
print(f"  mkdocs.yml generado ({len(nav_lines)} líneas de nav)")

# ── FIX 3: páginas vacías → lista de hijos ───────────────────────────

print("Fix 3: rellenando páginas vacías…")

# Construir mapa dest → lista de hijos directos desde el árbol
children_map = {}  # dest_path → [(child_title, child_dest)]

def collect_children(nodes):
    for n in nodes:
        parent = n["path"]
        if n["children"]:
            children_map[parent] = [(c["title"], c["path"]) for c in n["children"]]
            collect_children(n["children"])

collect_children(root_nodes)

filled = 0
for dest, children in children_map.items():
    md_file = DOCS / dest
    if not md_file.exists():
        continue
    content = md_file.read_text(encoding='utf-8')
    # Solo rellenar si el contenido es muy corto (solo el H1 o casi vacío)
    if len(content.strip()) < 300:
        title_line = content.strip().split('\n')[0] if content.strip() else ''
        child_links = '\n'.join(
            f'- [{t}]({dest_url(d)})' for t, d in children
        )
        new_content = f"{title_line}\n\n{child_links}\n"
        md_file.write_text(new_content, encoding='utf-8')
        filled += 1

print(f"  {filled} páginas rellenadas con lista de hijos")

# ── FIX 4: links externos confluence.um.es → internos ────────────────

print("Fix 4: reescribiendo links externos de Confluence…")

url_pattern = re.compile(
    r'https?://confluence\.um\.es[^\s\)"\'>]*'
)

def resolve_confluence_url(url):
    # Formato pageId=NNNNN
    m = re.search(r'pageId=(\d+)', url)
    if m:
        pid = m.group(1)
        if pid in numid_to_dest:
            base = dest_url(numid_to_dest[pid])
            # Preservar fragmento si existe
            frag = re.search(r'#([^)"\s]+)', url)
            return base + ('#' + frag.group(1) if frag else '')
    # Formato /pages/NNNNN/
    m = re.search(r'/pages/(\d+)/', url)
    if m:
        pid = m.group(1)
        if pid in numid_to_dest:
            return dest_url(numid_to_dest[pid])
    return None  # no resoluble

replaced = 0
files_changed = 0
for md_file in DOCS.rglob("*.md"):
    content = md_file.read_text(encoding='utf-8')
    new_content, n = url_pattern.subn(
        lambda m: resolve_confluence_url(m.group()) or m.group(),
        content
    )
    if new_content != content:
        replaced += sum(
            1 for m in url_pattern.finditer(content)
            if resolve_confluence_url(m.group())
        )
        md_file.write_text(new_content, encoding='utf-8')
        files_changed += 1

print(f"  {replaced} URLs reemplazadas en {files_changed} ficheros")
remaining = sum(
    len(url_pattern.findall(md_file.read_text(errors='replace')))
    for md_file in DOCS.rglob("*.md")
)
print(f"  {remaining} URLs de confluence.um.es sin resolver (externas reales)")

print("¡Listo!")
