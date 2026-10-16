# -*- coding: utf-8 -*-
"""
Traduce al español las descripciones del catálogo de Grasshopper
=================================================================
Usa el diccionario `traducciones_es.json` (inglés -> español), que está en esta carpeta.
Solo cambia DESCRIPCIONES: los nombres, abreviaturas y tipos de las entradas y salidas
quedan en inglés, como se ven en Grasshopper.

Uso (desde la carpeta Wiki Rhino/herramientas, con cualquier Python 3):
  python traducir_catalogo.py estado                  -> cuántas descripciones están traducidas
  python traducir_catalogo.py aplicar                 -> traduce el catálogo con el diccionario
  python traducir_catalogo.py pendientes FALTAN.tsv   -> lista los textos sin traducir
  python traducir_catalogo.py importar FALTAN.tsv TRADUCIDAS.tsv
                                                      -> agrega traducciones al diccionario
Formato de los .tsv: una línea por texto, "id<TAB>texto" (pendientes agrega la pestaña al medio).

Flujo después de exportar el catálogo de nuevo:  aplicar -> pendientes -> (traducir) -> importar -> aplicar
"""
import json
import pathlib
import re
import sys

AQUI = pathlib.Path(__file__).resolve().parent
CATALOGO = AQUI.parent / "raw" / "grasshopper" / "catalogo"
DICCIONARIO = AQUI / "traducciones_es.json"
INDICE = "_Índice del catálogo.md"
AVISO = ("> Descripciones traducidas al español (diccionario `herramientas/traducciones_es.json`). "
         "Nombres, abreviaturas y tipos en inglés, como en Grasshopper.")
CELDA = re.compile(r"(?<!\\)\|")


def cargar():
    if DICCIONARIO.exists():
        return json.loads(DICCIONARIO.read_text(encoding="utf-8"))
    return {}


def guardar(d):
    texto = json.dumps(dict(sorted(d.items())), ensure_ascii=False, indent=0)
    DICCIONARIO.write_text(texto + "\n", encoding="utf-8")


def _seguro(s):
    """Una sola línea y sin '|' sin escapar (rompería la tabla)."""
    s = re.sub(r"\s+", " ", s.replace("\t", " ")).strip()
    return CELDA.sub(r"\\|", s)


def _archivos():
    return sorted(CATALOGO.glob("Catálogo - *.md"))


def recorrer(lineas):
    """(índice de línea, 'comp' | 'param', texto, partes de la fila) de cada descripción."""
    for i, l in enumerate(lineas):
        if l.startswith("### "):
            j = i + 1
            while j < len(lineas) and not lineas[j].strip():
                j += 1
            if j < len(lineas) and lineas[j] and not lineas[j].startswith(("|", ">", "#", "Tipo de dato:")):
                yield j, "comp", lineas[j], None
        elif l.startswith("| ") and not l.startswith(("| Entrada", "| Salida", "|---")):
            partes = CELDA.split(l)
            if len(partes) == 7 and partes[5].strip():
                yield i, "param", partes[5].strip(), partes


def estado(d):
    valores = set(d.values())
    total = hechas = 0
    for p in _archivos():
        for _, _, texto, _ in recorrer(p.read_text(encoding="utf-8").split("\n")):
            total += 1
            hechas += texto in valores
    return total, hechas


def aplicar(d):
    cambiadas = 0
    for p in _archivos():
        lineas = p.read_text(encoding="utf-8").split("\n")
        n = 0
        for i, tipo, texto, partes in list(recorrer(lineas)):
            es = d.get(texto)
            if es is None or es == texto:
                continue
            es = _seguro(es)
            if tipo == "comp":
                lineas[i] = es
            else:
                partes[5] = " " + es + " "
                lineas[i] = "|".join(partes)
            n += 1
        if n:
            p.write_text("\n".join(lineas), encoding="utf-8")
            cambiadas += n
    indice = CATALOGO / INDICE
    if indice.exists():
        t = indice.read_text(encoding="utf-8")
        if AVISO not in t:
            t = t.replace("# Catálogo de Grasshopper (exportado)\n", "# Catálogo de Grasshopper (exportado)\n\n" + AVISO + "\n", 1)
            indice.write_text(t, encoding="utf-8")
    return cambiadas


def pendientes(d, salida):
    valores = set(d.values())
    vistos = {}
    for p in _archivos():
        pestana = p.stem.replace("Catálogo - ", "")
        for _, _, texto, _ in recorrer(p.read_text(encoding="utf-8").split("\n")):
            if texto not in d and texto not in valores and texto not in vistos:
                vistos[texto] = pestana
    with open(salida, "w", encoding="utf-8") as f:
        for n, (texto, pestana) in enumerate(vistos.items(), 1):
            f.write("{}\t{}\t{}\n".format(n, pestana, texto))
    return len(vistos)


def importar(d, faltan, traducidas):
    originales = {}
    for linea in open(faltan, encoding="utf-8"):
        partes = linea.rstrip("\n").split("\t")
        if len(partes) == 3:
            originales[partes[0]] = partes[2]
    nuevas = 0
    for linea in open(traducidas, encoding="utf-8"):
        partes = linea.rstrip("\n").split("\t", 1)
        if len(partes) == 2 and partes[0] in originales and partes[1].strip():
            d[originales[partes[0]]] = partes[1].strip()
            nuevas += 1
    return nuevas, len(originales)


if __name__ == "__main__":
    accion = sys.argv[1] if len(sys.argv) > 1 else "estado"
    d = cargar()
    if accion == "aplicar":
        print("Descripciones traducidas en esta pasada:", aplicar(d))
    elif accion == "pendientes":
        print("Textos sin traducir:", pendientes(d, sys.argv[2]))
    elif accion == "importar":
        nuevas, total = importar(d, sys.argv[2], sys.argv[3])
        guardar(d)
        print("Importadas {} de {} (diccionario: {} entradas)".format(nuevas, total, len(d)))
    if accion in ("estado", "aplicar"):
        total, hechas = estado(cargar())
        print("Catálogo: {} de {} descripciones en español ({:.0%})".format(hechas, total, hechas / total if total else 0))
