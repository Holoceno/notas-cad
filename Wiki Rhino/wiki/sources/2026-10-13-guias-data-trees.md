---
title: "Guías oficiales: data trees (por qué existen y cómo usarlos en Python)"
type: source
tags: [tipo/fuente, software/grasshopper, datos/arboles, lenguaje/python]
palabras-clave: [data tree, GH_Path, DataTree, rama, ruta, treehelpers, list_to_tree, tree_to_list, David Rutten, 1:N]
sources: [raw/developer-rhino3d/grasshopper/The Why and How of Data Trees.md, raw/developer-rhino3d/rhinopython/Grasshopper data trees and Python.md]
created: 2026-10-13
updated: 2026-10-13
---

Dos guías de developer.rhino3d.com sobre los árboles de datos de Grasshopper. *The Why and How of Data Trees* explica **por qué** Grasshopper guarda los datos así. *Grasshopper data trees and Python* explica **cómo** leerlos y crearlos desde un script. Con ellas se contrasta lo que [[wiki/concepts/data-trees]] decía de memoria.

## Detalles

### Por qué existen

- Los componentes transforman datos de distintas formas: `1:1` (Subtraction), `1:N` (Range, Divide Curve), `N:1` (Polyline, Loft), `N:N` (Sort) y los que entregan **varias listas** (Divide Surface, Square Grid).
- Al encadenar componentes `1:N`, la complejidad crece rápido. Por ejemplo: 3 sólidos → caras → isocurvas → puntos. Hace falta poder elegir cualquier subconjunto lógico ("los puntos de la cara 2 del cilindro"), así que el dato debe guardar **su historia**.
- La solución es el **data tree**: una *colección ordenada de listas*, cada una identificada por una **ruta** (path) de enteros no negativos, como `{0;2;1}`. Dos listas del mismo árbol no pueden tener la misma ruta.
- **Por qué aparecen tantos ceros** (`{0;0;0;0;3}`): todo componente de tipo `1:N` agrega **siempre** un nivel a la ruta, aunque esta vez haya producido una sola lista, porque Grasshopper prefiere la **consistencia** a la economía. Para limpiarlas está *Simplify*.

### En Python

- Un `DataTree` se comporta como un diccionario **ordenado** de `GH_Path` → lista (rama). Las rutas pueden ser **dispersas** (no hace falta que existan todas); dentro de una rama puede haber nulos, pero no huecos.
- Recorrer: `x.BranchCount`, `x.Branch(i)`, `x.Path(i)`.
- Lo más cómodo es convertir a **listas anidadas** con `ghpythonlib.treehelpers`: `th.tree_to_list(x)` y `th.list_to_tree(lista, source=[0,0])`. La opción `source` fija el prefijo de las rutas.
- Límite: una lista de listas no puede representar un árbol con ramas de **distinta profundidad** (un dato en `{0;1}` y otro en `{0}`). Si el árbol viene de una lógica normal de Grasshopper, no pasa.

## Conexiones

- Mapas: [[Mapa - Data trees y listas]] · [[Mapa - Programación]]
- [[wiki/concepts/data-trees]]: el concepto completo, ahora con estas fuentes
- [[wiki/sources/2026-10-13-guias-scripting-rhino8]]: acceso Item / List / Tree en los componentes de script

## Fuentes

- [[The Why and How of Data Trees]] (David Rutten)
- [[Grasshopper data trees and Python]] (ejemplo completo: `datatree_examples.gh` en el sitio)
- Las dos en `raw/developer-rhino3d/`, traídas con `herramientas/guias_mcneel.py` (2026-10-13).
