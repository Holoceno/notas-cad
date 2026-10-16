---
title: "Data trees (árboles de datos) en Grasshopper"
type: concept
tags: [tipo/concepto, software/grasshopper, datos/arboles, datos/listas, lenguaje/python, lenguaje/csharp]
palabras-clave: [data tree, GH_Path, DataTree, rama, ruta, path, graft, flatten, simplify, flip matrix, path mapper, data matching, longest list, treehelpers]
sources: [raw/grasshopper/catalogo/Catálogo - Sets.md, raw/grasshopper/catalogo/Catálogo - eleFront.md, raw/grasshopper/catalogo/Catálogo - Pufferfish.md, raw/developer-rhino3d/grasshopper/The Why and How of Data Trees.md, raw/developer-rhino3d/rhinopython/Grasshopper data trees and Python.md]
created: 2026-10-13
updated: 2026-10-13
---

Un **data tree** es la estructura en la que Grasshopper guarda todo lo que viaja por un cable: un conjunto de **ramas** (listas), cada una identificada por una **ruta** como `{0;2}`. Dentro de cada rama los elementos tienen un **índice**, así que la dirección completa de un dato es `{0;2}(5)`. Cada componente decide cómo combinar sus entradas según esa estructura. Por eso entender los árboles es lo que separa una definición que funciona por casualidad de una que escala de 1 a 1.000 piezas.

## Detalles

### Anatomía

| Término | Qué es | Ejemplo |
|---|---|---|
| Ruta (path) | Secuencia de enteros, un entero por nivel | `{0;3}` |
| Rama (branch) | La lista guardada en una ruta (puede estar vacía o tener nulos) | `{0;3}` → 12 puntos |
| Índice | Posición dentro de la rama | `(5)` |
| Lista plana | Un árbol con una sola rama | todo en `{0}` |

Para **ver** la estructura: [[Catálogo - Params#Panel (parámetro)|Panel]] (muestra rutas y elementos), [[Catálogo - Params#Param Viewer (Viewer, parámetro)|Param Viewer]] (doble clic: vista gráfica del árbol) y [[Catálogo - Sets#Tree Statistics (TStat)|Tree Statistics]].

### Cómo nace la estructura

Cuando un componente produce **varios resultados por cada elemento de entrada**, agrega un nivel a la ruta. Ejemplo: 3 curvas en `{0}` → [[Catálogo - Curve#Divide Curve (Divide)|Divide Curve]] → 3 ramas `{0;0}`, `{0;1}`, `{0;2}`, cada una con los puntos de su curva. Así Grasshopper mantiene la relación "estos puntos son de esta curva" sin que nadie lo programe.

McNeel clasifica los componentes según cómo transforman los datos: `1:1` (Subtraction), `1:N` (Range, Divide Curve), `N:1` (Polyline, Loft), `N:N` (Sort) y los que entregan varias listas (Divide Surface). Todo componente `1:N` agrega **siempre** un nivel, aunque esta vez haya producido una sola lista: Grasshopper prefiere la consistencia a la economía. De ahí vienen las rutas llenas de ceros como `{0;0;0;0;3}`, que *Simplify* limpia ([[wiki/sources/2026-10-13-guias-data-trees|guía oficial]]).

### Acceso: item, lista o árbol

Cada entrada de un componente declara su **acceso**. El catálogo lo muestra en la columna *Acceso* de cada tabla:

- **item**: el componente se ejecuta una vez por elemento (ej. `Move`).
- **lista**: una vez por **rama**, y recibe la rama completa (ej. `PolyLine`, `Sort List`, `List Item`).
- **árbol**: recibe el árbol entero de una vez (ej. `Flatten Tree`, `Path Mapper`, las entradas `Sheets` y `Geometry` de [[wiki/entities/opennest|OpenNest]]).

Consecuencia práctica: un componente con acceso *lista* respeta los grupos. Si cada rama es una pieza, cada pieza se procesa por separado.

### Cómo se combinan dos entradas (data matching)

- **Dentro de una rama**, Grasshopper usa por defecto *longest list*: si una entrada tiene menos elementos, repite el último.
- **Entre árboles**, empareja las ramas **por orden** (la rama 0 con la rama 0, la 1 con la 1...). Si un árbol tiene menos ramas, repite su última rama. Un valor suelto (un slider) se reutiliza en todas.
- Para controlar el emparejamiento a mano: [[Catálogo - Sets#Longest List (Long)|Longest List]], [[Catálogo - Sets#Shortest List (Short)|Shortest List]] y [[Catálogo - Sets#Cross Reference (CrossRef)|Cross Reference]] (todas las combinaciones).
- Regla mental: **Graft** convierte "cada uno contra todos" en "uno con uno".

### Operaciones esenciales

Graft, Flatten, Simplify y Reverse también existen como **modificadores**: clic derecho sobre cualquier entrada o salida, sin agregar un componente.

| Operación | Componente | Qué hace | Cuándo usarlo |
|---|---|---|---|
| Injertar | [[Catálogo - Sets#Graft Tree (Graft)\|Graft Tree]] | Cada elemento a su propia rama | Emparejar uno a uno con otra lista |
| Aplanar | [[Catálogo - Sets#Flatten Tree (Flatten)\|Flatten Tree]] | Todo a una sola rama `{0}` | Cuando la agrupación ya no importa (¡pierde la relación pieza-dato!) |
| Simplificar | [[Catálogo - Sets#Simplify Tree (Simplify)\|Simplify Tree]] | Quita la parte de la ruta que comparten todas las ramas | Rutas largas tipo `{0;0;0;3}` |
| Transponer | [[Catálogo - Sets#Flip Matrix (Flip)\|Flip Matrix]] | Rama *i* elemento *j* → rama *j* elemento *i* | Grillas: curvas en la otra dirección |
| Subir de nivel | [[Catálogo - Sets#Shift Paths (PShift)\|Shift Paths]] / [[Catálogo - Sets#Trim Tree (Trim)\|Trim Tree]] | Quita índices de la ruta y fusiona ramas | Agrupar puntos por curva → por superficie |
| Agrupar de a N | [[Catálogo - Sets#Partition List (Partition)\|Partition List]] | Parte una lista en ramas de tamaño N | Lotes de OpenNest, filas de una grilla |
| Reescribir rutas | [[Catálogo - Sets#Path Mapper (parámetro)\|Path Mapper]] | Regla léxica `{A;B}(i) → {B}(i)` | Reorganizar a medida (potente, frágil si cambia la entrada) |
| Separar ramas | [[Catálogo - Sets#Explode Tree (BANG!)\|Explode Tree]] | Una salida por rama | Pocos grupos fijos |
| Juntar flujos | [[Catálogo - Sets#Entwine\|Entwine]] / [[Catálogo - Sets#Merge\|Merge]] | Entwine: cada entrada a su rama · Merge: une ramas con la misma ruta | Combinar resultados de varias partes |
| Extraer | [[Catálogo - Sets#Tree Branch (Branch)\|Tree Branch]] / [[Catálogo - Sets#Tree Item (Item)\|Tree Item]] | Una rama o un elemento por ruta | Inspeccionar o tomar un caso |
| Limpiar | [[Catálogo - Sets#Clean Tree (Clean)\|Clean Tree]] / [[Catálogo - Sets#Prune Tree (Prune)\|Prune Tree]] | Quita nulos y ramas vacías o pequeñas | Después de Cull, Dispatch o intersecciones |
| Recuperar forma | [[Catálogo - Sets#Unflatten Tree (Unflatten)\|Unflatten Tree]] / [[Catálogo - Sets#Match Tree (Match)\|Match Tree]] | Devuelve los elementos a la estructura de un árbol guía | Después de un proceso que exigió aplanar |
| Vecinos | [[Catálogo - Sets#Relative Item (RelItem)\|Relative Item]] | Pares de elementos con un desfase de rama e índice | Diagonales en grillas, paneles |

**eleFront** agrega herramientas útiles para mantener datos "en paralelo" (geometría + atributos): [[Catálogo - eleFront#Graft Parallel (GraftP)|Graft Parallel]], [[Catálogo - eleFront#Clean Parallel (CleanP)|Clean Parallel]], [[Catálogo - eleFront#Get Matching Branches (GetBrn)|Get Matching Branches]], [[Catálogo - eleFront#Shift To Depth (ShfDep)|Shift To Depth]] y [[Catálogo - eleFront#Graft By Index (GraftI)|Graft By Index]]. **Pufferfish** suma utilidades de listas (`Dispatch Indices`, `Sift Indices`, `Point Sort Items`). La lista completa está en [[Mapa - Data trees y listas]].

### En código (Python 3 y C# en Rhino 8)

Lo más simple es **no manejar árboles**: poner la entrada del script en *List Access*. Grasshopper ejecuta el script una vez por rama y la salida conserva la ruta. Así se pensó OVERKILL para Grasshopper: una rama por capa o por grupo, y el script nunca mezcla ramas.

Si hace falta construir un árbol a mano:

```python
# Python 3 Script (Rhino 8) — puntos de cada curva en su propia rama
from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path

arbol = DataTree[object]()
for i, crv in enumerate(curvas):            # curvas: List Access
    for t in crv.DivideByCount(10, True):
        arbol.Add(crv.PointAt(t), GH_Path(i))
a = arbol

# Leer un árbol (entrada con Tree Access)
for i in range(x.BranchCount):
    ruta, rama = x.Path(i), x.Branch(i)

# Atajo: listas anidadas <-> árbol
import ghpythonlib.treehelpers as th
anidada = th.tree_to_list(x)
a = th.list_to_tree(anidada)
```

```csharp
// C# Script — lo mismo
var arbol = new DataTree<Point3d>();
for (int i = 0; i < curvas.Count; i++)
    foreach (double t in curvas[i].DivideByCount(10, true))
        arbol.Add(curvas[i].PointAt(t), new GH_Path(i));
a = arbol;
```

### Errores típicos

| Síntoma | Causa probable | Arreglo |
|---|---|---|
| Funciona con 1 curva y falla con varias | Falta *Graft* o sobra *Flatten* | Revisar el Panel antes y después |
| Combinaciones cruzadas o repetidas | Dos árboles con distinta cantidad de ramas (se repite la última) | Igualar estructuras: Graft, Simplify, Match Tree |
| Rutas que crecen sin control `{0;0;0;0;3}` | Cada componente agrega un nivel | *Simplify* en la salida, Trim Tree o Shift Paths |
| Atributos que se separan de su pieza | Se aplanó un lado y el otro no | Mantener las dos cosas con la misma estructura (eleFront *Parallel*) |
| Ramas vacías y nulos tras filtrar | Cull, Dispatch o intersecciones sin resultado | Clean Tree |

### Aplicación en mis proyectos

- **OpenNest:** con la opción *Batch* activada, **cada rama de Geometry es un lote** que va junto en su plancha. Partition List o una ruta por mueble controlan qué piezas viajan juntas. Ver [[wiki/entities/opennest]].
- **Mueble CNC:** estructura sugerida `{mueble;pieza}`, con contorno, perforaciones, nombre, material y veta en árboles paralelos con las mismas rutas.

## Conexiones

- Mapas: [[Mapa - Data trees y listas]] (todos los componentes de listas, árboles y texto) · [[Mapa - Programación]]
- [[wiki/entities/opennest]]: Batch por rama, entradas con acceso árbol
- [[wiki/entities/grasshopper]]: el programa y sus plugins
- [[wiki/concepts/tipos-geometria-rhinocommon]]: qué tipos viajan dentro de las ramas
- [[wiki/concepts/python-csharp-rhinocommon]]: `DataTree` en los componentes de script de Python y C#

## Fuentes

- Descripciones de componentes: [[wiki/sources/2026-10-12-catalogo-grasshopper|catálogo exportado]] (pestañas Sets, eleFront y Pufferfish; Rhino 8.35).
- Rutas, por qué existen los árboles, `DataTree`/`GH_Path` y `treehelpers`: **contrastado** con [[wiki/sources/2026-10-13-guias-data-trees|las guías oficiales]] (2026-10-13). Acceso Item / List / Tree en scripts: [[wiki/sources/2026-10-13-guias-scripting-rhino8]].
- Reglas de *data matching* (longest list, emparejar ramas por orden): síntesis propia con conocimiento general de Grasshopper, **pendiente de contrastar** con *Essential Algorithms and Data Structures for Computational Design* (McNeel) y el *Grasshopper Primer* cuando se ingesten.
