# -*- coding: utf-8 -*-
"""
Guías de developer.rhino3d.com como fuentes en raw/
===================================================
Trae una guía de la documentación oficial de McNeel (repositorio público
github.com/mcneel/developer-rhino3d-com) y la guarda como fuente en bruto:

    raw/developer-rhino3d/<sección>/<Título>.md

Uso (desde la carpeta Wiki Rhino/), con la parte de la dirección web que va después de /guides/:

    python herramientas/guias_mcneel.py scripting/scripting-csharp rhinopython/python-overloads

Por ejemplo https://developer.rhino3d.com/guides/scripting/scripting-csharp/ -> scripting/scripting-csharp.
Las imágenes quedan enlazadas al sitio (se ven con conexión a internet). Los avisos del sitio
pasan a callouts de Obsidian (> [!note]). Después se ingesta como cualquier fuente (ver CLAUDE.md).

Nunca sobreescribe un archivo que ya existe (raw/ es inmutable). Solo biblioteca estándar.
"""
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1]
DESTINO = WIKI / "raw" / "developer-rhino3d"
SITIO = "https://developer.rhino3d.com"
CRUDO = "https://raw.githubusercontent.com/mcneel/developer-rhino3d-com/main/content/en/guides/{}/index.md"

ETIQUETAS = {  # sección -> etiquetas del vocabulario (Mapas/Etiquetas y navegación.md)
    "scripting": ["software/rhino", "programacion/scripts"],
    "rhinocommon": ["software/rhinocommon", "programacion/plugins"],
    "rhinopython": ["software/rhinocommon", "lenguaje/python"],
    "grasshopper": ["software/grasshopper", "programacion/plugins"],
    "opennurbs": ["software/rhino3dm"],
    "yak": ["programacion/plugins"],
    "compute": ["software/rhino", "programacion/plugins"],
}


def bajar(url):
    pedido = urllib.request.Request(url, headers={"User-Agent": "notas-wiki-rhino"})
    with urllib.request.urlopen(pedido, timeout=30) as r:
        return r.read().decode("utf-8")


def _callout(m):
    tipo, titulo, cuerpo = m.group(1), m.group(2) or "", m.group(3).strip("\n")
    return "\n".join(["> [!{}] {}".format(tipo, titulo).rstrip()] + ["> " + l if l else ">" for l in cuerpo.split("\n")])


def _enlaces(texto, base):
    """Enlaces e imágenes relativos -> direcciones completas del sitio (solo fuera del código)."""
    texto = re.sub(r"\]\((/[^)\s]*)", lambda m: "](" + SITIO + m.group(1), texto)                   # páginas del sitio
    texto = re.sub(r"\]\((?!https?:|#|mailto:)([^)\s]+)", lambda m: "](" + base + m.group(1), texto)  # imágenes
    texto = re.sub(r'(href=")(/[^"]*)', lambda m: m.group(1) + SITIO + m.group(2), texto)
    return re.sub(r'(<img[^>]*src=")(?!https?:)/?([^"]+)', lambda m: m.group(1) + base + m.group(2), texto)


def convertir(texto, ruta):
    """Markdown de Hugo -> Markdown de Obsidian (enlaces absolutos, avisos como callouts)."""
    base = "{}/guides/{}/".format(SITIO, ruta)
    texto = re.sub(r"<(style|script)>.*?</\1>\s*", "", texto, flags=re.S)
    texto = re.sub(r'<svg[^>]*aria-label="([^"]*)"[^>]*>.*?</svg>', r"*(Gráfico del sitio: \1)*", texto, flags=re.S)
    texto = re.sub(r'\{\{<\s*call-out\s+"?(\w+)"?\s*(?:"([^"]*)")?\s*>\}\}(.*?)\{\{<\s*/call-out\s*>\}\}',
                   _callout, texto, flags=re.S)
    texto = re.sub(r'\{\{<\s*relref\s+"(#[^"]*)"\s*>\}\}', r"\1", texto)
    texto = re.sub(r'\{\{<\s*relref\s+"(/[^"]*)"\s*>\}\}', lambda m: SITIO + m.group(1).rstrip("/") + "/", texto)
    texto = re.sub(r'\{\{<\s*vimeo\s+id="(\d+)"[^>]*>\}\}', r"[Video](https://vimeo.com/\1)", texto)
    partes = re.split(r"(```.*?```|`[^`\n]*`)", texto, flags=re.S)  # impares = código: no se toca
    texto = "".join(p if i % 2 else _enlaces(p, base) for i, p in enumerate(partes))
    return re.sub(r"\n{3,}", "\n\n", texto).strip() + "\n"


def nombre_archivo(titulo):
    titulo = titulo.replace(": ", " - ").replace("#", "♯")  # mismo criterio que el catálogo (C♯)
    titulo = re.sub(r'[?*"<>|^\[\]]', "", titulo)
    return re.sub(r"[\\/:]", "-", titulo).strip(" .")


def traer(ruta):
    ruta = ruta.strip("/")
    if ruta.startswith(("http://", "https://")):
        ruta = ruta.split("/guides/", 1)[1].strip("/")
    texto = bajar(CRUDO.format(ruta))
    partes = texto.split("+++")
    cabecera, cuerpo = (partes[1], "+++".join(partes[2:])) if texto.startswith("+++") else ("", texto)
    campo = {}
    for clave in ("title", "description"):
        h = re.search(r'^{} = "(.*)"\s*$'.format(clave), cabecera, re.M)
        campo[clave] = h.group(1).replace('\\"', "'") if h else ruta
    seccion = ruta.split("/")[0]
    tags = ["tipo/documentacion"] + ETIQUETAS.get(seccion, [])
    if "C#" in campo["title"] or "csharp" in ruta:
        tags.append("lenguaje/csharp")
    if "Python" in campo["title"] or "python" in ruta:
        tags.append("lenguaje/python")
    if "tree" in ruta:
        tags.append("datos/arboles")
    tags = list(dict.fromkeys(tags))
    carpeta = DESTINO / seccion
    carpeta.mkdir(parents=True, exist_ok=True)
    path = carpeta / (nombre_archivo(campo["title"]) + ".md")
    if path.exists():
        print("  = ya existe:", path.relative_to(WIKI))
        return
    lineas = [
        "---",
        'title: "{}"'.format(campo["title"]),
        'source: "{}/guides/{}/"'.format(SITIO, ruta),
        "author:",
        '  - "[[Robert McNeel & Associates]]"',
        "created: {}".format(date.today().isoformat()),
        'description: "{}"'.format(campo["description"].replace('"', "'")),
        "tags: [{}]".format(", ".join(tags)),
        "---",
        convertir(cuerpo, ruta),
    ]
    path.write_text("\n".join(lineas), encoding="utf-8")
    print("  +", path.relative_to(WIKI))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for r in sys.argv[1:]:
        traer(r)
