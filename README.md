# Hércules SGI — Documentación

Documentación completa del proyecto **Hércules SGI** (Sistema de Gestión de Investigación), generada a partir del espacio Confluence del proyecto y publicada como sitio estático con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Contenido

La documentación cubre las siguientes secciones principales:

- **SGI — Sistema de Gestión de Investigación**: requisitos funcionales, diseño, desarrollo, manual de usuario, integraciones y guía de implantación (más de 1.500 páginas)
- **Arquitectura**: arquitectura técnica de los proyectos Hércules (ED, MA, RPA)
- **APIs de Integración**: servicios propios y de terceros expuestos y consumidos por el SGI
- **Portal Nacional Avanzado de Investigación** (Hércules MA — Métodos de Análisis)
- **Herramienta de CV** (Hércules ED — Enriquecimiento de Datos)
- **RPA**: módulo de automatización y gestión

## Estructura del repositorio

```
hercules-docs/
├── docs/                        # Fuentes Markdown
│   ├── index.md                 # Página de inicio
│   ├── assets/                  # Logo e imágenes globales
│   ├── attachments/             # Imágenes y adjuntos exportados de Confluence
│   └── hercules/                # Árbol de documentación (1.771 páginas)
├── site/                        # Sitio estático generado (no editar)
├── mkdocs.yml                   # Configuración de MkDocs
└── scripts/                     # Scripts de conversión Confluence → MkDocs
    ├── convert.py               # Convierte HTML export → Markdown
    ├── fix_site.py              # Ajustes de navegación y enlaces internos
    └── fetch_external.py        # Resolución de enlaces externos
```

## Visualizar la documentación localmente

### Requisitos

```bash
pip install mkdocs-material
```

### Construir y servir

```bash
# Construir el sitio estático
mkdocs build

# Servir el sitio ya construido (más rápido, ~1.771 páginas)
python3 -m http.server 8001 --directory site/
```

Abre `http://localhost:8001` en el navegador.

> **Nota**: `mkdocs serve` también funciona pero tarda ~90 segundos en cargar por el gran número de páginas.

## Regenerar la documentación desde el export de Confluence

Si se dispone de un nuevo export HTML del espacio Confluence:

```bash
# 1. Colocar el export en Confluence-space-export-format-html/HERCULES/
# 2. Ejecutar la conversión
python3 scripts/convert.py

# 3. Aplicar ajustes de navegación y enlaces
python3 scripts/fix_site.py

# 4. Resolver enlaces externos y logo
python3 scripts/fetch_external.py

# 5. Reconstruir el sitio
mkdocs build
```

## Origen de los datos

La documentación se generó a partir del export HTML del espacio **HERCULES** del Confluence de la Universidad de Murcia (`confluence.um.es`). La conversión preserva:

- Estructura jerárquica de navegación original
- Imágenes y adjuntos exportados
- Tablas (formato GFM)
- Enlaces internos entre páginas

Los enlaces a páginas de otros espacios Confluence o a páginas nunca creadas se han conservado como texto plano.
