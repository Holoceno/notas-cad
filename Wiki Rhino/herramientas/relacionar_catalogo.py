# -*- coding: utf-8 -*-
"""
Relaciona el catálogo de Grasshopper con los mapas temáticos (MOC) de la bóveda
================================================================================
Se ejecuta DESPUÉS de exportar y traducir el catálogo (se puede repetir sin miedo):

    python herramientas/relacionar_catalogo.py            -> aplica los cambios
    python herramientas/relacionar_catalogo.py revisar    -> solo muestra estadísticas

Qué hace:
  1. Encabezados enlazables en `raw/grasshopper/catalogo/`:
       "### Divide Curve · `Divide`"  ->  "### Divide Curve (Divide)"
     Obsidian no puede enlazar encabezados con |, #, ^, [ ] o comillas invertidas.
     Así funciona [[Catálogo - Curve#Divide Curve (Divide)]].
  2. Clasifica cada componente en uno o más mapas (pestaña + subcategoría, más reglas
     por nombre y por tipo de entradas/salidas; ver REGLAS abajo).
  3. Reescribe la sección automática de cada mapa en `notas/Mapas/`, entre
     <!-- AUTO:inicio --> y <!-- AUTO:fin -->. Lo que está fuera de esas marcas
     (introducción, equivalencias, notas propias) NO se toca.
  4. Etiquetas en el frontmatter de cada nota del catálogo + una línea "Mapas: ..."
     bajo el título de la pestaña.
  5. Muestras de RhinoCommon (`raw/rhinopy/` y `raw/rhinocs/`): cada mapa recibe, dentro de
     la misma sección automática, una tabla con sus muestras y enlaces a la versión Python y
     a la C#. El mapa, la descripción en español y el método clave de cada muestra están en
     `herramientas/muestras_rhinocommon.json` (si una muestra cae mal, se corrige ahí).

Solo usa la biblioteca estándar de Python (no necesita Rhino ni uv).
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1]
BOVEDA = WIKI.parent
CATALOGO = WIKI / "raw" / "grasshopper" / "catalogo"
MAPAS = BOVEDA / "Mapas"
PREFIJO = "Catálogo - "
INDICE = "_Índice del catálogo.md"
INICIO, FIN = "<!-- AUTO:inicio -->", "<!-- AUTO:fin -->"
MUESTRAS_JSON = WIKI / "herramientas" / "muestras_rhinocommon.json"
MUESTRAS = {"py": WIKI / "raw" / "rhinopy", "cs": WIKI / "raw" / "rhinocs"}
FICHA_MUESTRAS = "wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp"
CELDA = re.compile(r"(?<!\\)\|")
ANTIGUO = re.compile(r"^### (.*) · `([^`]*)`(?: · \*([^*]+)\*)?\s*$")

# ----- Mapas: clave -> (archivo, etiquetas). La primera etiqueta va al catálogo. -------------
MAPA = {
    "CUR": ("Mapa - Curvas", ["geometria/curvas"]),
    "SUP": ("Mapa - Superficies y NURBS", ["geometria/superficies", "geometria/nurbs"]),
    "BREP": ("Mapa - Brep y sólidos", ["geometria/brep"]),
    "MALLA": ("Mapa - Mallas y SubD", ["geometria/mallas", "geometria/subd"]),
    "PVP": ("Mapa - Puntos, vectores y planos", ["geometria/puntos-vectores", "matematicas/vectores"]),
    "TRANS": ("Mapa - Transformaciones", ["geometria/transformaciones", "matematicas/matrices"]),
    "MORPH": ("Mapa - Morph y tween", ["geometria/morph"]),
    "INTER": ("Mapa - Intersecciones y booleanos", ["geometria/intersecciones"]),
    "DATOS": ("Mapa - Data trees y listas", ["datos/arboles", "datos/listas", "datos/texto"]),
    "MATE": ("Mapa - Matemáticas", ["matematicas"]),
    "VIS": ("Mapa - Visualización y anotaciones", ["rhino/vista", "rhino/anotaciones"]),
    "DOC": ("Mapa - Documento de Rhino", ["rhino/documento", "rhino/capas"]),
    "SIM": ("Mapa - Simulación, optimización y ML", ["simulacion"]),
    "FAB": ("Mapa - Fabricación", ["fabricacion"]),
    "PATRON": ("Mapa - Patrones y teselados", ["geometria/patrones"]),
    "SCRIPT": ("Mapa - Scripts, interfaz y archivos", ["programacion/scripts", "programacion/interfaz", "programacion/archivos"]),
    "CAD2D": ("Mapa - CAD 2D y planos", ["fabricacion/planos", "rhino/anotaciones"]),  # solo muestras
}

# ----- Reglas por (pestaña, subcategoría). None = toda la pestaña. -------------------------
REGLAS = {
    ("Anemone", None): ["SCRIPT"],
    ("Biber", None): ["FAB"],
    ("Biber", "Optimization"): ["FAB", "SIM"],
    ("Curve", None): ["CUR"],
    ("Display", None): ["VIS"],
    ("Human UI", None): ["SCRIPT"],
    ("Human", None): ["DOC"],
    ("Human", "Display"): ["VIS"],
    ("Human", "Image"): ["VIS"],
    ("Human", "Texture Mapping"): ["VIS"],
    ("Intersect", None): ["INTER"],
    ("Kangaroo2", None): ["SIM"],
    ("Kangaroo2", "Mesh"): ["SIM", "MALLA"],
    ("LunchBox", "Data"): ["SCRIPT"],
    ("LunchBox", "Form"): ["SUP"],
    ("LunchBox", "Generate"): ["PATRON"],
    ("LunchBox", "Mass"): ["BREP"],
    ("LunchBox", "Mesh"): ["MALLA"],
    ("LunchBox", "Panels"): ["PATRON"],
    ("LunchBox", "Serialization"): ["SCRIPT"],
    ("LunchBox", "Structure"): ["PATRON"],
    ("LunchBox", "Workflow"): ["DOC", "SCRIPT"],
    ("LunchBoxML", None): ["SIM"],
    ("Maths", None): ["MATE"],
    ("Maths", "Script"): ["SCRIPT"],
    ("Mesh", None): ["MALLA"],
    ("NGon", None): ["MALLA"],
    ("NGon", "Joint"): ["MALLA", "FAB"],
    ("Parakeet", None): ["PATRON"],
    ("Parakeet", "Curve"): ["PATRON", "CUR"],
    ("Parakeet", "Mesh"): ["PATRON", "MALLA"],
    ("Parakeet", "Primitive"): ["SUP"],
    ("Parakeet", "Surface"): ["PATRON", "SUP"],
    ("Parakeet", "Util"): ["SCRIPT"],
    ("Params", "Input"): ["SCRIPT"],
    ("Params", "OpenNest2"): ["FAB"],
    ("Params", "Rhino"): ["DOC"],
    ("Params", "Util"): ["SCRIPT"],
    ("Pufferfish", "Color"): ["VIS"],
    ("Pufferfish", "Curve"): ["CUR"],
    ("Pufferfish", "Domain"): ["MATE"],
    ("Pufferfish", "List"): ["DATOS"],
    ("Pufferfish", "Mesh"): ["MALLA"],
    ("Pufferfish", "Number"): ["MATE"],
    ("Pufferfish", "Plane"): ["PVP"],
    ("Pufferfish", "Point"): ["PVP"],
    ("Pufferfish", "SubD"): ["MALLA"],
    ("Pufferfish", "Surface"): ["SUP"],
    ("Pufferfish", "Transform"): ["TRANS"],
    ("Pufferfish", "Twisted Box"): ["MORPH"],
    ("Pufferfish", "Vector"): ["PVP"],
    ("Rhino", None): ["DOC"],
    ("Rhino", "Annotations"): ["VIS"],
    ("Rhino", "Drafting"): ["VIS"],
    ("Rhino", "Render"): ["VIS"],
    ("Rhino", "Viewports"): ["VIS"],
    ("Sets", None): ["DATOS"],
    ("Sets", "Sequence"): ["DATOS", "MATE"],
    ("Surface", None): ["SUP"],
    ("Surface", "SubD"): ["MALLA"],
    ("Transform", None): ["TRANS"],
    ("Transform", "Morph"): ["MORPH"],
    ("Vector", None): ["PVP"],
    ("Vector", "Grid"): ["PVP", "PATRON"],
    ("Wb", None): ["MALLA"],
    ("Wb", "Transform"): ["MALLA", "PATRON"],
    ("eleFront", None): ["DOC"],
    ("eleFront", "04 Annotations"): ["DOC", "VIS"],
    ("eleFront", "07 Trees"): ["DATOS"],
    ("eleFront", "09 Files"): ["DOC", "SCRIPT"],
}

# Parámetros de Params > Geometry y Params > Primitive: se reparten por nombre.
PARAMS_POR_NOMBRE = {
    "CUR": {"Circle", "Circular Arc", "Curve", "Line", "Rectangle"},
    "SUP": {"Surface"},
    "BREP": {"Box", "Brep", "Extrusion"},
    "MALLA": {"Mesh", "Mesh Face", "SubD"},
    "PVP": {"Field", "Plane", "Point", "Point Cloud", "Vector"},
    "TRANS": {"Transform"},
    "MORPH": {"Twisted Box"},
    "VIS": {"Colour", "Font", "Shader", "Angular Dimension", "Annotation Dot", "Centermark", "Hatch", "Leader", "Linear Dimension",
            "Ordinate Dimension", "Radial Dimension", "Text Entity"},
    "DOC": {"Block Instance", "Geometry", "Geometry Cache", "Geometry Pipeline", "Group", "Light", "View",
            "Earth Anchor Point"},
    "DATOS": {"Boolean", "Culture", "Data", "Data Path", "Guid", "Text"},
    "MATE": {"Complex", "Domain", "Domain²", "Integer", "Matrix", "Number", "Time", "Unit System"},
    "SCRIPT": {"File Path"},
}

# Reglas por nombre (se suman a las anteriores).
POR_NOMBRE = [
    (re.compile(r"\bTween"), "MORPH"),
    (re.compile(r"\bUnroll"), "FAB"),
    (re.compile(r"^Pack Curves$"), "FAB"),
    (re.compile(r"^(Galapagos|Fitness Landscape|Gene Pool)$"), "SIM"),
    (re.compile(r"^(Param Viewer|Cherry Picker|Item Selector|Filter By Item|Dispatch Multiple)$"), "DATOS"),
    (re.compile(r"^RTree"), "PVP"),
    (re.compile(r"^(Sort Duplicate|Random Split List)"), "DATOS"),
]

# Si no hubo ninguna regla: se decide por el tipo de las salidas (y luego de las entradas).
POR_TIPO = [
    ({"Curve", "Line", "Circle", "Arc", "Polyline", "Rectangle", "Polyline Curve"}, "CUR"),
    ({"Surface"}, "SUP"),
    ({"Brep", "Box"}, "BREP"),
    ({"Mesh", "SubD", "Mesh Face"}, "MALLA"),
    ({"Point", "Vector", "Plane"}, "PVP"),
    ({"Transform"}, "TRANS"),
    ({"Number", "Integer", "Domain"}, "MATE"),
    ({"Colour"}, "VIS"),
    ({"Text", "Generic Data", "Boolean"}, "DATOS"),
]

NATIVAS = ["Params", "Maths", "Sets", "Vector", "Curve", "Surface", "Mesh", "Intersect", "Transform",
           "Display", "Rhino"]

PLUGINS = [  # (prefijo de la librería en minúsculas, etiqueta)
    ("anemone", "plugin/anemone"), ("biber", "plugin/biber"), ("endoframe", "plugin/biber"),
    ("elefront", "plugin/elefront"), ("human ui", "plugin/human-ui"), ("human", "plugin/human"),
    ("kangaroo2", "plugin/kangaroo"), ("lunchboxml", "plugin/lunchboxml"), ("lunchbox", "plugin/lunchbox"),
    ("ngon", "plugin/ngon"), ("opennest", "plugin/opennest"), ("parakeet", "plugin/parakeet"),
    ("wang tile", "plugin/parakeet"), ("pufferfish", "plugin/pufferfish"), ("weaverbird", "plugin/weaverbird"),
]


# ----- Lectura del catálogo -------------------------------------------------------------------

def limpio(s):
    """Quita lo que rompe un enlace [[nota#encabezado]] en Obsidian: | # ^ [ ] ` \\ y :"""
    s = (s or "").replace("\\|", "–").replace("|", "–").replace("\\", "∖").replace("#", "♯").replace(":", " -")
    return re.sub(r"\s+", " ", re.sub(r"[\[\]^`]", "", s)).strip()


def titulo(nombre, abrev, tipo="componente"):
    """Encabezado enlazable: 'Nombre (Abrev)' o 'Nombre (Abrev, tipo)'. Igual que en el exportador."""
    n, a = limpio(nombre), limpio(abrev)
    extra = [a] if a and a != n else []
    if tipo and tipo != "componente":
        extra.append(tipo)
    return n + (" ({})".format(", ".join(extra)) if extra else "")


def leer(path):
    """Normaliza encabezados en las líneas y devuelve (líneas, componentes)."""
    lineas = path.read_text(encoding="utf-8").split("\n")
    tab = path.stem[len(PREFIJO):]
    comps, sub, actual, vistos = [], "", None, Counter()
    for i, l in enumerate(lineas):
        if l.startswith("## "):
            sub = l[3:].strip()
        elif l.startswith("### "):
            m = ANTIGUO.match(l)
            if m:
                nombre = m.group(1)
                t = titulo(nombre, m.group(2), m.group(3))
                vistos[t] += 1
                if vistos[t] > 1:
                    t += " · {}".format(vistos[t])
                lineas[i] = "### " + t
            else:
                t = limpio(l[4:])
                lineas[i] = "### " + t
                nombre = re.sub(r" \([^()]*\)( · \d+)?$", "", t)
            actual = {"tab": tab, "sub": sub, "nombre": nombre.replace("\\|", "–"), "titulo": lineas[i][4:],
                      "desc": "", "entradas": set(), "salidas": set(), "en_salidas": False}
            comps.append(actual)
        elif actual is not None:
            if l.startswith("| Salida"):
                actual["en_salidas"] = True
            elif l.startswith("| ") and not l.startswith(("| Entrada", "|---")):
                partes = CELDA.split(l)
                if len(partes) == 7:
                    actual["salidas" if actual["en_salidas"] else "entradas"].add(partes[3].strip())
            elif l.strip() and not actual["desc"] and not l.startswith(("|", ">", "#", "Tipo de dato:")):
                actual["desc"] = l.strip()
    return lineas, comps


def clasificar(c):
    claves = []
    regla = REGLAS.get((c["tab"], c["sub"]), REGLAS.get((c["tab"], None)))
    if c["tab"] == "Params" and c["sub"] in ("Geometry", "Primitive"):
        regla = [k for k, nombres in PARAMS_POR_NOMBRE.items() if c["nombre"] in nombres]
    claves += regla or []
    for patron, clave in POR_NOMBRE:
        if patron.search(c["nombre"]):
            claves.append(clave)
    tipos = c["entradas"] | c["salidas"]
    if "Brep" in c["salidas"] or ("Brep" in c["entradas"] and c["tab"] in NATIVAS):
        claves.append("BREP")
    if "Twisted Box" in tipos:
        claves.append("MORPH")
    if "SubD" in c["salidas"]:
        claves.append("MALLA")
    if not claves:
        for grupo in (c["salidas"], c["entradas"]):
            for tipos_regla, clave in POR_TIPO:
                if grupo & tipos_regla:
                    claves.append(clave)
                    break
            if claves:
                break
    return list(dict.fromkeys(claves))  # sin repetir, en orden


def leer_muestras():
    """Muestras de RhinoCommon: título -> {py, cs, mapas, es, clave}. py/cs = nombre de la nota."""
    datos = json.loads(MUESTRAS_JSON.read_text(encoding="utf-8")) if MUESTRAS_JSON.exists() else {}
    muestras = {}
    cerco = {"py": "```python\n", "cs": "```cs\n"}
    for lang, carpeta in MUESTRAS.items():
        for p in sorted(carpeta.glob("*.md"), key=lambda p: (len(p.stem), p.stem)):
            texto = p.read_text(encoding="utf-8")
            h = re.search(r'^title: "(.*)"\s*$', texto, re.M)
            titulo_m = h.group(1) if h else p.stem
            m = muestras.setdefault(titulo_m, {"titulo": titulo_m, "py": None, "cs": None})
            if cerco[lang] in texto:  # un recorte viejo puede tener C# en la carpeta de Python
                m[lang] = m[lang] or p.stem  # si hay copias, gana el nombre más corto
    for m in muestras.values():
        d = datos.get(m["titulo"], {})
        m.update(mapas=[k for k in d.get("mapas", []) if k in MAPA], es=d.get("es", ""), clave=d.get("clave", ""))
    return sorted(muestras.values(), key=lambda m: m["titulo"].lower())


# ----- Escritura --------------------------------------------------------------------------------

def _corto(s, n=110):
    s = s.strip().rstrip(".")
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def _orden_tab(tab):
    return (0, NATIVAS.index(tab)) if tab in NATIVAS else (1, tab.lower())


def tabla_muestras(muestras):
    l = ["## Muestras de RhinoCommon ({})".format(len(muestras)), "",
         "> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea "
         "([[{}|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` "
         "desde `muestras_rhinocommon.json`.".format(FICHA_MUESTRAS), "",
         "| Muestra | Código | Qué hace | Mirar en RhinoCommon |", "|---|---|---|---|"]
    for m in muestras:
        codigo = " · ".join("[[{}\\|{}]]".format(m[lang], nombre) for lang, nombre in (("py", "Py"), ("cs", "C#")) if m[lang])
        clave = "`{}`".format(m["clave"]) if m["clave"] else ""
        l.append("| {} | {} | {} | {} |".format(m["titulo"], codigo, m["es"], clave))
    return l + [""]


def seccion_auto(comps, muestras=()):
    l = [INICIO, ""]
    if muestras:
        l += tabla_muestras(muestras)
    if not comps:
        return l + [FIN]
    l += ["## Componentes de Grasshopper ({})".format(len(comps)), "",
          "> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. "
          "No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.", ""]
    grupos = defaultdict(list)
    for c in comps:
        grupos[(c["tab"], c["sub"])].append(c)
    for tab, sub in sorted(grupos, key=lambda k: (_orden_tab(k[0]), k[1].lower())):
        cs = sorted(grupos[(tab, sub)], key=lambda c: c["titulo"].lower())
        l += ["### {} › {} ({})".format(tab, sub or "—", len(cs)), ""]
        for c in cs:
            enlace = "[[{}{}#{}|{}]]".format(PREFIJO, tab, c["titulo"], c["titulo"])
            l.append("- " + enlace + (" — " + _corto(c["desc"]) if c["desc"] else ""))
        l.append("")
    return l + [FIN]


def escribir_mapa(clave, comps, muestras=()):
    archivo, etiquetas = MAPA[clave]
    path = MAPAS / (archivo + ".md")
    auto = seccion_auto(comps, muestras)
    if path.exists():
        t = path.read_text(encoding="utf-8")
        if INICIO in t and FIN in t:
            antes, resto = t.split(INICIO, 1)
            despues = resto.split(FIN, 1)[1]
            nuevo = antes + "\n".join(auto) + despues
        else:
            nuevo = t.rstrip() + "\n\n" + "\n".join(auto) + "\n"
    else:
        nombre = archivo[len("Mapa - "):]
        nuevo = "\n".join([
            "---", "tags: [tipo/mapa, {}]".format(", ".join(etiquetas)), "---", "",
            "# " + nombre, "", "> Mapa temático (MOC). Escribir aquí la introducción y las equivalencias.", "",
        ] + auto) + "\n"
    if not path.exists() or path.read_text(encoding="utf-8") != nuevo:
        path.write_text(nuevo, encoding="utf-8")
        return True
    return False


def etiquetas_catalogo(lineas, tab, comps_tab, por_mapa_tab):
    """Frontmatter 'tags:' + línea 'Mapas:' bajo el título de la pestaña."""
    libs = []
    for l in lineas:
        if l.startswith("libraries:"):
            libs = re.findall(r'"([^"]*)"', l)
            break
    tags = ["tipo/catalogo", "software/grasshopper"]
    for lib in libs:
        for prefijo, tag in PLUGINS:
            if lib.lower().startswith(prefijo):
                tags.append(tag)
                break
    umbral = max(3, len(comps_tab) // 10)
    mapas = sorted(por_mapa_tab.items(), key=lambda kv: -kv[1])
    tags += [MAPA[k][1][0] for k, n in mapas if n >= umbral]
    tags = list(dict.fromkeys(tags))
    for i, l in enumerate(lineas):
        if l.startswith("tags:"):
            lineas[i] = "tags: [" + ", ".join(tags) + "]"
            break
    linea_mapas = "Mapas: " + " · ".join("[[{}]] ({})".format(MAPA[k][0], n) for k, n in mapas)
    lineas[:] = [l for l in lineas if not l.startswith("Mapas: [[")]
    titulo_i = lineas.index("# " + tab)
    j = titulo_i + 1
    while j < len(lineas) and not lineas[j].strip():
        j += 1
    # después de la línea "N objetos · librería ..."
    lineas[j + 1:j + 1] = ["", linea_mapas]
    # quitar líneas en blanco dobles que pudieran quedar
    texto = re.sub(r"\n{3,}", "\n\n", "\n".join(lineas))
    return texto


def marcar_indice():
    path = CATALOGO / INDICE
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8")
    nuevo = t
    if not t.startswith("---"):
        nuevo = "---\ntags: [tipo/catalogo, software/grasshopper]\n---\n\n" + nuevo
    aviso = "> Navegar por tema: [[Mapa - Grasshopper]] (mapas de curvas, mallas, data trees, fabricación...)."
    if aviso not in nuevo:
        nuevo = nuevo.replace("# Catálogo de Grasshopper (exportado)\n", "# Catálogo de Grasshopper (exportado)\n\n" + aviso + "\n", 1)
    if nuevo != t:
        path.write_text(nuevo, encoding="utf-8")


def main(aplicar=True):
    archivos = sorted(CATALOGO.glob(PREFIJO + "*.md"))
    if not archivos:
        sys.exit("No hay catálogo en " + str(CATALOGO))
    todos, por_archivo = [], {}
    for p in archivos:
        lineas, comps = leer(p)
        por_archivo[p] = (lineas, comps)
        todos += comps

    por_mapa = defaultdict(list)
    sin_mapa = []
    for c in todos:
        c["mapas"] = clasificar(c)
        for k in c["mapas"]:
            por_mapa[k].append(c)
        if not c["mapas"]:
            sin_mapa.append(c)

    muestras = leer_muestras()
    muestras_por_mapa = defaultdict(list)
    for m in muestras:
        for k in m["mapas"]:
            muestras_por_mapa[k].append(m)

    print("Componentes: {} · con mapa: {} · sin mapa: {}".format(len(todos), len(todos) - len(sin_mapa), len(sin_mapa)))
    print("Muestras de RhinoCommon: {} · con Python: {} · con C#: {}".format(
        len(muestras), sum(1 for m in muestras if m["py"]), sum(1 for m in muestras if m["cs"])))
    print("  {:<45} {:>11} {:>8}".format("", "componentes", "muestras"))
    for k in MAPA:
        print("  {:<45} {:>11} {:>8}".format(MAPA[k][0], len(por_mapa[k]), len(muestras_por_mapa[k])))
    for c in sin_mapa:
        print("  SIN MAPA: {} › {} › {}".format(c["tab"], c["sub"], c["titulo"]))
    for m in muestras:
        if not m["mapas"]:
            print("  MUESTRA SIN MAPA (agregarla a muestras_rhinocommon.json): " + m["titulo"])
    if not aplicar:
        return

    MAPAS.mkdir(exist_ok=True)
    cambiados = 0
    for p, (lineas, comps) in por_archivo.items():
        tab = p.stem[len(PREFIJO):]
        cuenta = Counter(k for c in comps for k in c["mapas"])
        texto = etiquetas_catalogo(lineas, tab, comps, cuenta)
        if texto != p.read_text(encoding="utf-8"):
            p.write_text(texto, encoding="utf-8")
            cambiados += 1
    marcar_indice()
    mapas = sum(escribir_mapa(k, por_mapa[k], muestras_por_mapa[k]) for k in MAPA)
    print("Notas del catálogo actualizadas: {} · mapas actualizados: {}".format(cambiados, mapas))


if __name__ == "__main__":
    main(aplicar=not (len(sys.argv) > 1 and sys.argv[1] == "revisar"))
