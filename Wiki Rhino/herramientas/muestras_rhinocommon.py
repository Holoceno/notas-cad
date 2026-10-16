# -*- coding: utf-8 -*-
"""
Muestras de RhinoCommon (developer.rhino3d.com) en Python y en C#
=================================================================
Cada muestra oficial de McNeel trae el mismo ejemplo en C#, en Python y a veces en VB.
Web Clipper guarda solo la pestaña que está a la vista, por eso `raw/rhinopy/` quedó casi
todo en Python. Este script las trae del repositorio público de la documentación
(github.com/mcneel/developer-rhino3d-com) y guarda cada lenguaje en su carpeta:

    raw/rhinopy/<Título>.md        -> versión Python (igual que las del Web Clipper)
    raw/rhinocs/<Título> (cs).md   -> versión C#

Uso (desde la carpeta Wiki Rhino/):

    python herramientas/muestras_rhinocommon.py              -> estado: cuáles tienes y cuáles faltan
    python herramientas/muestras_rhinocommon.py completar    -> trae el lenguaje que falta de las que ya tienes
    python herramientas/muestras_rhinocommon.py traer unroll-surface split-breps-with-planes
                                                             -> trae muestras nuevas (Python y C#)

El nombre corto (unroll-surface) es el final de la dirección web de la muestra; `estado` los lista.
Después: agregar la muestra a `muestras_rhinocommon.json` (mapa, descripción y método clave) y
correr `python herramientas/relacionar_catalogo.py`, que la pone en los mapas.

Algunas muestras solo existen en C# (el sitio dice "No Python sample available"): esas quedan
solo en raw/rhinocs/. Si un recorte viejo de raw/rhinopy/ guardó el C# en vez del Python,
el Python se guarda aparte como `<Título> (py).md`.

Nunca sobreescribe un archivo que ya existe (raw/ es inmutable). Solo biblioteca estándar.
"""
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1]
CARPETA = {"py": WIKI / "raw" / "rhinopy", "cs": WIKI / "raw" / "rhinocs"}
SUFIJO = {"py": "", "cs": " (cs)"}
CERCO = {"py": "python", "cs": "cs"}
ETIQUETA = {"py": "lenguaje/python", "cs": "lenguaje/csharp"}

REPO = "mcneel/developer-rhino3d-com"
ARBOL = "https://api.github.com/repos/{}/git/trees/main?recursive=1".format(REPO)
CRUDO = "https://raw.githubusercontent.com/{}/main/content/en/samples/rhinocommon/{{}}/index.md".format(REPO)
WEB = "https://developer.rhino3d.com/samples/rhinocommon/{}/"
FUENTE = re.compile(r'^source: "?https://developer\.rhino3d\.com/samples/rhinocommon/([^/"]+)/?"?\s*$', re.M)
VACIO = re.compile(r"^(#|//|')\s*No .*sample available\s*$", re.I)  # pestaña sin código en ese lenguaje


def bajar(url):
    pedido = urllib.request.Request(url, headers={"User-Agent": "notas-wiki-rhino"})
    with urllib.request.urlopen(pedido, timeout=30) as r:
        return r.read().decode("utf-8")


def nombres_remotos():
    """Nombres cortos de todas las muestras de RhinoCommon publicadas."""
    pre, fin = "content/en/samples/rhinocommon/", "/index.md"
    arbol = json.loads(bajar(ARBOL))["tree"]
    return sorted(t["path"][len(pre):-len(fin)] for t in arbol
                  if t["path"].startswith(pre) and t["path"].endswith(fin))


def leer_remota(nombre):
    """Título, descripción, palabras clave, categorías y código por lenguaje ('cs', 'py', 'vb')."""
    texto = bajar(CRUDO.format(nombre))
    cabecera = texto.split("+++")[1] if texto.startswith("+++") else ""
    m = {"nombre": nombre}
    for clave in ("title", "description"):
        h = re.search(r'^{} = "(.*)"\s*$'.format(clave), cabecera, re.M)
        m[clave] = h.group(1).replace('\\"', "'").strip() if h else nombre
    for clave in ("keywords", "categories"):
        h = re.search(r"^{} = \[(.*)\]\s*$".format(clave), cabecera, re.M)
        m[clave] = re.findall(r'"([^"]*)"', h.group(1)) if h else []
    bloques = re.findall(r'<div class="codetab-content" id="(\w+)">\s*```\w*\n(.*?)\n```', texto, re.S)
    m["codigo"] = {lang: codigo for lang, codigo in bloques if not VACIO.match(codigo.strip())}
    return m


def leer_todas(nombres):
    with ThreadPoolExecutor(8) as hilos:
        return list(hilos.map(leer_remota, nombres))


def locales():
    """nombre corto -> {'py': [...], 'cs': [...], 'otros': [...]}, según el campo source: de cada nota.
    Cuenta como Python o C# solo si la nota tiene un bloque de código de ese lenguaje."""
    inv = {}
    for lang, carpeta in CARPETA.items():
        for p in sorted(carpeta.glob("*.md")):
            texto = p.read_text(encoding="utf-8")
            h = FUENTE.search(texto)
            if h:
                tipo = lang if "```" + CERCO[lang] + "\n" in texto else "otros"
                inv.setdefault(h.group(1), {"py": [], "cs": [], "otros": []})[tipo].append(p)
    return inv


def nombre_archivo(titulo):
    """Sin los caracteres que rompen un enlace de Obsidian o un nombre de archivo."""
    return re.sub(r'[\\/:*?"<>|#^\[\]]', "-", titulo).strip()


def escribir(m, lang):
    """Crea la nota de un lenguaje. Devuelve la ruta, o None si ya existía o no hay código."""
    if lang not in m["codigo"]:
        return None
    CARPETA[lang].mkdir(parents=True, exist_ok=True)
    path = CARPETA[lang] / (nombre_archivo(m["title"]) + SUFIJO[lang] + ".md")
    if path.exists() and lang == "py" and "```python\n" not in path.read_text(encoding="utf-8"):
        path = path.with_name(path.stem + " (py).md")  # recorte viejo con C# en la carpeta de Python
    if path.exists():
        return None
    descripcion = m["description"].replace('"', "'")
    lineas = [
        "---",
        'title: "{}"'.format(m["title"]),
        'source: "{}"'.format(WEB.format(m["nombre"])),
        "author:",
        '  - "[[Robert McNeel & Associates]]"',
        "created: {}".format(date.today().isoformat()),
        'description: "{}"'.format(descripcion),
        "tags: [tipo/muestra, software/rhinocommon, {}]".format(ETIQUETA[lang]),
        "palabras-clave: [{}]".format(", ".join(m["keywords"] + m["categories"])),
        "---",
        m["description"],
        "",
        "```" + CERCO[lang],
        m["codigo"][lang].rstrip(),
        "```",
        "",
    ]
    path.write_text("\n".join(lineas), encoding="utf-8")
    return path


def estado():
    inv = locales()
    print("Buscando las muestras publicadas en GitHub...")
    todas = leer_todas(nombres_remotos())
    con_py = [m for m in todas if inv.get(m["nombre"], {}).get("py")]
    con_cs = [m for m in todas if inv.get(m["nombre"], {}).get("cs")]
    faltan = [(m, lang) for m in todas if m["nombre"] in inv
              for lang in ("py", "cs") if lang in m["codigo"] and not inv[m["nombre"]][lang]]
    solo_cs = [m for m in todas if "py" not in m["codigo"]]
    print("Publicadas: {} ({} solo en C#) · tienes en Python: {} · tienes en C#: {}".format(
        len(todas), len(solo_cs), len(con_py), len(con_cs)))
    for m, lang in faltan:
        print("  falta {} de: {}".format({"py": "Python", "cs": "C#"}[lang], m["title"]))
    if faltan:
        print("  -> python herramientas/muestras_rhinocommon.py completar")
    nuevas = [m for m in todas if m["nombre"] not in inv]
    print("\nMuestras que no tienes ({}), por categoría de McNeel:".format(len(nuevas)))
    por_cat = {}
    for m in nuevas:
        por_cat.setdefault((m["categories"] or ["Other"])[0], []).append(m)
    for cat in sorted(por_cat):
        print("\n  {}".format(cat))
        for m in sorted(por_cat[cat], key=lambda x: x["title"].lower()):
            langs = "/".join(k for k in ("cs", "py") if k in m["codigo"])
            print("    {:<45} {:<6} {}".format(m["nombre"], langs, m["description"][:70]))


def traer(nombres, langs=("py", "cs")):
    nuevas = []
    for m in leer_todas(nombres):
        for lang in langs:
            path = escribir(m, lang)
            if path:
                nuevas.append(path)
    for p in nuevas:
        print("  +", p.relative_to(WIKI))
    print("Notas nuevas: {}".format(len(nuevas)))


if __name__ == "__main__":
    orden = sys.argv[1] if len(sys.argv) > 1 else "estado"
    if orden == "estado":
        estado()
    elif orden == "completar":
        traer(sorted(n for n, v in locales().items() if not (v["py"] and v["cs"])))
    elif orden == "traer" and len(sys.argv) > 2:
        traer(sys.argv[2:])
    else:
        sys.exit(__doc__)
