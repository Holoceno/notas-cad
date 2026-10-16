# -*- coding: utf-8 -*-
"""
Exportador del catálogo de Grasshopper -> Markdown (Wiki Rhino)
===============================================================
Recorre TODOS los componentes instalados (Grasshopper + plugins) y escribe una nota
por pestaña con: nombre, abreviatura, descripción, entradas y salidas de cada componente.

Uso (Rhino 8, componente "Python 3 Script" de Grasshopper):
  1. Crear un componente Python 3 Script y pegar este código (o abrir este archivo).
  2. Entradas (zoom al componente -> "+" para agregar, clic derecho -> renombrar):
       ejecutar  (bool) <- conectar un Button
       pestanas  (str)  <- opcional: "Pufferfish, Kangaroo2" = solo esas pestañas
       excluir   (str)  <- opcional: pestañas a saltar, separadas por coma
       carpeta   (str)  <- opcional: dónde escribir
                           (por defecto: ~/notas-cad/Wiki Rhino/raw/grasshopper/catalogo)
     Salida:
       info      (str)  <- resumen de lo que hizo (conectar un Panel)
  3. Presionar el botón con "pestanas" vacío -> exporta TODO de una vez: Grasshopper nativo
     (Params, Maths, Sets, Vector, Curve, Surface, Mesh, ...) + todos los plugins instalados.
     Tarda 1 o 2 minutos. Solo "ejecutar" e "info" son necesarias; las demás entradas son opcionales.
  4. (Opcional) Para probar o actualizar una sola pestaña: pestanas = "Pufferfish".
  5. En una terminal, desde la carpeta "Wiki Rhino":
       python herramientas/traducir_catalogo.py aplicar      (descripciones al español)
       python herramientas/relacionar_catalogo.py            (mapas temáticos y etiquetas)
  6. Obsidian sube los archivos solo (o Ctrl+P -> commit-and-sync).

Notas:
  - No toca el documento de Rhino ni el de Grasshopper: solo lee y escribe archivos .md.
  - Para leer entradas y salidas crea cada componente en memoria (sin ponerlo en el lienzo).
    Si algún plugin muestra una ventana (licencia, bienvenida), ciérrala; si se queda pegado,
    agrega su pestaña en "excluir".
  - Se puede volver a ejecutar cuando instales o actualices plugins: sobrescribe el catálogo.
"""
from __future__ import print_function

import datetime
import io
import os
import re
import time
import traceback

try:
    import Grasshopper as GH
    import Rhino
    from Grasshopper.Kernel import GH_Exposure, GH_ObjectType, GH_ParamAccess

    EN_GH = True
except ImportError:  # fuera de Rhino (pruebas): solo se usa la parte que escribe Markdown
    EN_GH = False

CARPETA_DEFECTO = os.path.join(os.path.expanduser("~"), "notas-cad", "Wiki Rhino", "raw", "grasshopper", "catalogo")
PREFIJO = "Catálogo - "


# ----- Utilidades de texto -----------------------------------------------------------

def _txt(s):
    """Texto en una sola línea, seguro dentro de una tabla Markdown."""
    if s is None:
        return ""
    s = str(s).replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    return re.sub(r"\s+", " ", s).strip()


def _yaml(s):
    return '"' + _txt(s).replace('"', "'") + '"'


def _nombre_archivo(s):
    s = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", s or "").strip(" .")
    return s or "Sin pestaña"


def _limpio(s):
    """Quita lo que rompe un enlace [[nota#encabezado]] en Obsidian: | # ^ [ ] ` \\ y :"""
    s = _txt(s).replace("\\|", "–").replace("\\", "∖").replace("#", "♯").replace(":", " -")
    return re.sub(r"\s+", " ", re.sub(r"[\[\]^`]", "", s)).strip()


def _titulo(c):
    """'Divide Curve (Divide)' o 'Cherry Picker (Item, parámetro)'. Igual que relacionar_catalogo.py."""
    n, a = _limpio(c["nombre"]), _limpio(c["abrev"])
    extra = [a] if a and a != n else []
    if c["tipo"] != "componente":
        extra.append(c["tipo"])
    return n + (" ({})".format(", ".join(extra)) if extra else "")


def _lista(texto):
    if not texto:
        return set()
    return {t.strip().lower() for t in str(texto).split(",") if t.strip()}


# ----- Lectura desde Grasshopper -----------------------------------------------------

def _param(p, acceso):
    return {
        "nombre": p.Name,
        "abrev": p.NickName,
        "tipo": p.TypeName,
        "acceso": acceso.get(p.Access, str(p.Access)),
        "opcional": bool(getattr(p, "Optional", False)),
        "desc": p.Description,
    }


def leer_componentes(solo=frozenset(), excluir=frozenset()):
    """Devuelve (registros, omitidos, errores) de todos los objetos instalados."""
    acceso = {GH_ParamAccess.item: "item", GH_ParamAccess.list: "lista", GH_ParamAccess.tree: "árbol"}
    server = GH.Instances.ComponentServer
    registros, errores = [], []
    omitidos = {"obsoletos": 0, "ocultos": 0, "filtrados": 0}

    for proxy in server.ObjectProxies:
        nombre = "?"
        try:
            d = proxy.Desc
            nombre = d.Name
            tab = d.Category or "(sin pestaña)"
            if (solo and tab.lower() not in solo) or tab.lower() in excluir:
                omitidos["filtrados"] += 1
                continue
            if proxy.Obsolete:
                omitidos["obsoletos"] += 1
                continue
            if proxy.Exposure == GH_Exposure.hidden:
                omitidos["ocultos"] += 1
                continue

            reg = {
                "tab": tab, "sub": d.SubCategory or "", "nombre": d.Name, "abrev": d.NickName,
                "desc": d.Description, "guid": str(proxy.Guid), "tipo": "componente",
                "libreria": "", "autor": "", "dato": "", "entradas": [], "salidas": [], "error": None,
            }
            if proxy.Kind == GH_ObjectType.UserObject:
                reg["tipo"] = "user object"
            try:
                lib = server.FindAssemblyByObject(proxy.Guid)
                if lib is not None:
                    reg["libreria"] = "{} {}".format(lib.Name, lib.Version or "").strip()
                    reg["autor"] = lib.AuthorName or ""
            except Exception:
                pass

            try:
                obj = proxy.CreateInstance()
                params = getattr(obj, "Params", None)
                if params is not None and hasattr(params, "Input"):
                    reg["entradas"] = [_param(p, acceso) for p in params.Input]
                    reg["salidas"] = [_param(p, acceso) for p in params.Output]
                elif obj is not None and hasattr(obj, "TypeName"):
                    if reg["tipo"] == "componente":
                        reg["tipo"] = "parámetro"
                    reg["dato"] = obj.TypeName
                else:
                    reg["tipo"] = "objeto especial"
            except Exception as e:
                reg["error"] = _txt(e)[:200]
                errores.append((tab, nombre, reg["error"]))
            registros.append(reg)
        except Exception as e:
            errores.append(("?", nombre, _txt(e)[:200]))
    return registros, omitidos, errores


# ----- Escritura del catálogo en Markdown (no necesita Rhino) ------------------------

def _tabla(params, es_entrada):
    if not params:
        return []
    if es_entrada:
        filas = ["| Entrada | Abrev. | Tipo | Acceso | Descripción |", "|---|---|---|---|---|"]
        for p in params:
            nombre = _txt(p["nombre"]) + (" *(opcional)*" if p["opcional"] else "")
            filas.append("| {} | `{}` | {} | {} | {} |".format(
                nombre, _txt(p["abrev"]), _txt(p["tipo"]), _txt(p["acceso"]), _txt(p["desc"])))
    else:
        filas = ["| Salida | Abrev. | Tipo | Acceso | Descripción |", "|---|---|---|---|---|"]
        for p in params:
            filas.append("| {} | `{}` | {} | {} | {} |".format(
                _txt(p["nombre"]), _txt(p["abrev"]), _txt(p["tipo"]), _txt(p["acceso"]), _txt(p["desc"])))
    return filas + [""]


def _nota_pestana(tab, comps, meta):
    libs = sorted({c["libreria"] for c in comps if c["libreria"]})
    autores = sorted({c["autor"] for c in comps if c["autor"]})
    l = [
        "---",
        "title: " + _yaml("Catálogo Grasshopper — " + tab),
        'source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"',
        "type: catalogo",
        "tab: " + _yaml(tab),
        "libraries: [" + ", ".join(_yaml(x) for x in libs) + "]",
        "components: {}".format(len(comps)),
        "rhino: " + _yaml(meta.get("rhino", "")),
        "grasshopper: " + _yaml(meta.get("grasshopper", "")),
        "generated: " + meta.get("fecha", ""),
        "tags: [tipo/catalogo, software/grasshopper]",
        "---",
        "",
        "# " + tab,
        "",
        "{} objetos · librería: {}{}".format(
            len(comps), ", ".join(libs) or "—", (" · autor: " + ", ".join(autores)) if autores else ""),
        "",
    ]
    sub_actual = None
    vistos = {}
    for c in comps:
        if c["sub"] != sub_actual:
            sub_actual = c["sub"]
            l += ["## " + (_txt(sub_actual) or "(sin subcategoría)"), ""]
        titulo = _titulo(c)
        vistos[titulo] = vistos.get(titulo, 0) + 1
        if vistos[titulo] > 1:  # dos objetos con el mismo nombre en la pestaña
            titulo += " · {}".format(vistos[titulo])
        l += ["### " + titulo, ""]
        if c["desc"]:
            l += [_txt(c["desc"]), ""]
        if c["dato"]:
            l += ["Tipo de dato: **{}**".format(_txt(c["dato"])), ""]
        l += _tabla(c["entradas"], True)
        l += _tabla(c["salidas"], False)
        if c["error"]:
            l += ["> No se pudieron leer entradas/salidas: " + c["error"], ""]
    return "\n".join(l).rstrip() + "\n"


def escribir_catalogo(registros, carpeta, meta, omitidos=None, errores=(), parcial=False):
    """Escribe una nota por pestaña + un índice. Devuelve [(pestaña, n, librerías, archivo)]."""
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    por_tab = {}
    for r in registros:
        por_tab.setdefault(r["tab"], []).append(r)

    resumen = []
    for tab in sorted(por_tab, key=lambda t: t.lower()):
        comps = sorted(por_tab[tab], key=lambda r: (r["sub"].lower(), r["nombre"].lower()))
        archivo = PREFIJO + _nombre_archivo(tab) + ".md"
        with io.open(os.path.join(carpeta, archivo), "w", encoding="utf-8", newline="\n") as f:
            f.write(_nota_pestana(tab, comps, meta))
        libs = sorted({c["libreria"] for c in comps if c["libreria"]})
        resumen.append((tab, len(comps), libs, archivo))

    omitidos = omitidos or {}
    total = sum(n for _, n, _, _ in resumen)
    l = [
        "# Catálogo de Grasshopper (exportado)",
        "",
        "Generado el {} desde Rhino {} · Grasshopper {}.".format(
            meta.get("fecha", ""), meta.get("rhino", "?"), meta.get("grasshopper", "?")),
        "",
        "**{} objetos en {} pestañas.** Omitidos: {} obsoletos, {} ocultos, {} filtrados.".format(
            total, len(resumen), omitidos.get("obsoletos", 0), omitidos.get("ocultos", 0), omitidos.get("filtrados", 0)),
        "",
    ]
    if parcial:
        l += ["> Exportación **parcial** (se usó `pestanas` o `excluir`). Ejecutar sin filtros para el catálogo completo.", ""]
    l += ["| Pestaña | Objetos | Librería(s) |", "|---|---|---|"]
    for tab, n, libs, archivo in resumen:
        l.append("| [[{}\\|{}]] | {} | {} |".format(archivo[:-3], _txt(tab), n, _txt(", ".join(libs)) or "—"))
    l.append("")
    if errores:
        l += ["## Objetos con errores ({})".format(len(errores)), "",
              "| Pestaña | Objeto | Error |", "|---|---|---|"]
        l += ["| {} | {} | {} |".format(_txt(t), _txt(n), _txt(e)) for t, n, e in errores]
        l.append("")
    with io.open(os.path.join(carpeta, "_Índice del catálogo.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(l))
    return resumen


# ----- Orquestación --------------------------------------------------------------------

def exportar(pestanas=None, excluir=None, carpeta=None):
    if not carpeta:
        notas = os.path.join(os.path.expanduser("~"), "notas")
        if not os.path.isdir(notas):
            return ("No encontré la bóveda en {}.\nConecta la entrada 'carpeta' con la ruta de "
                    "'Wiki Rhino/raw/grasshopper/catalogo' dentro de tu bóveda.".format(notas))
        carpeta = CARPETA_DEFECTO
    inicio = time.time()
    registros, omitidos, errores = leer_componentes(_lista(pestanas), _lista(excluir))
    meta = {"fecha": datetime.date.today().isoformat()}
    try:
        meta["rhino"] = str(Rhino.RhinoApp.Version)
    except Exception:
        pass
    try:
        meta["grasshopper"] = str(GH.Versioning.Version)
    except Exception:
        pass
    resumen = escribir_catalogo(registros, carpeta, meta, omitidos, errores, parcial=bool(pestanas or excluir))
    lineas = ["Listo en {:.0f} s: {} objetos en {} pestañas.".format(
        time.time() - inicio, len(registros), len(resumen)), "Carpeta: " + carpeta, ""]
    lineas += ["{:>5}  {}".format(n, tab) for tab, n, _, _ in resumen]
    if errores:
        lineas += ["", "{} objetos con errores (ver el índice).".format(len(errores))]
    return "\n".join(lineas)


if EN_GH:
    _g = globals().get
    if _g("ejecutar"):
        try:
            info = exportar(_g("pestanas"), _g("excluir"), _g("carpeta"))
        except Exception:
            info = "ERROR:\n" + traceback.format_exc()
    else:
        info = "Listo para exportar: presiona el botón conectado a 'ejecutar'.\nDestino: " + (
            _g("carpeta") or CARPETA_DEFECTO)
