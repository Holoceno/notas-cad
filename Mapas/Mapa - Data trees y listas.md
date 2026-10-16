---
tags: [tipo/mapa, datos/arboles, datos/listas, datos/texto, software/grasshopper, lenguaje/python]
---

# Data trees y listas

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Cómo se organizan los datos que viajan por los cables: listas, árboles (ramas y rutas) y texto. Es el tema que más errores explica en Grasshopper. **Empezar por [[wiki/concepts/data-trees]].**

## Teoría y código
- [[wiki/concepts/data-trees]]: rutas, acceso item/lista/árbol, data matching, errores típicos, `DataTree` en Python y C#
- [[wiki/entities/opennest]]: Batch = una rama por lote (ejemplo real de por qué importan las ramas)
- [[Ramas paralelas por pieza]]: una pieza = una ruta; Path Mapper, Replace Paths, Construct Path y Unflatten Tree en un caso real

## Equivalencias con Python (listas)

| Tarea | Grasshopper | Python |
|---|---|---|
| Elemento i | [[Catálogo - Sets#List Item (Item)\|List Item]] | `lista[i]` |
| Largo | [[Catálogo - Sets#List Length (Lng)\|List Length]] | `len(lista)` |
| Invertir | [[Catálogo - Sets#Reverse List (Rev)\|Reverse List]] | `lista[::-1]` |
| Desplazar (con vuelta) | [[Catálogo - Sets#Shift List (Shift)\|Shift List]] | `lista[k:] + lista[:k]` |
| Ordenar por clave | [[Catálogo - Sets#Sort List (Sort)\|Sort List]] | `[v for _, v in sorted(zip(claves, valores))]` |
| Filtrar con patrón | [[Catálogo - Sets#Cull Pattern (Cull)\|Cull Pattern]] | `[x for x, ok in zip(lista, itertools.cycle(patron)) if ok]` |
| Repartir en dos | [[Catálogo - Sets#Dispatch\|Dispatch]] | `a = [x for x, ok in zip(l, p) if ok]`, `b = [x for x, ok in zip(l, p) if not ok]` |
| Agrupar de a N | [[Catálogo - Sets#Partition List (Partition)\|Partition List]] | `[l[i:i + n] for i in range(0, len(l), n)]` |
| Serie | [[Catálogo - Sets#Series\|Series]] | `[inicio + i * paso for i in range(n)]` |
| N+1 valores en un rango | [[Catálogo - Sets#Range\|Range]] | `[a + (b - a) * i / n for i in range(n + 1)]` |
| Unir y partir texto | [[Catálogo - Sets#Text Join (Join)\|Text Join]] / [[Catálogo - Sets#Text Split (Split)\|Text Split]] | `sep.join(textos)` / `texto.split(sep)` |
| Formatear texto | [[Catálogo - Sets#Format\|Format]] | `f"Pieza {n:03d}"` |

## Para empezar
[[Catálogo - Sets#Graft Tree (Graft)|Graft Tree]] · [[Catálogo - Sets#Flatten Tree (Flatten)|Flatten Tree]] · [[Catálogo - Sets#Simplify Tree (Simplify)|Simplify Tree]] · [[Catálogo - Sets#Flip Matrix (Flip)|Flip Matrix]] · [[Catálogo - Sets#Partition List (Partition)|Partition List]] · [[Catálogo - Sets#Path Mapper (parámetro)|Path Mapper]] · [[Catálogo - Params#Param Viewer (Viewer, parámetro)|Param Viewer]] · [[Catálogo - Sets#Cull Pattern (Cull)|Cull Pattern]] · [[Catálogo - Sets#Dispatch|Dispatch]]

<!-- AUTO:inicio -->

## Componentes de Grasshopper (136)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Primitive (6)

- [[Catálogo - Params#Boolean (Bool, parámetro)|Boolean (Bool, parámetro)]] — Contiene una colección de valores booleanos
- [[Catálogo - Params#Culture (parámetro)|Culture (parámetro)]] — Contiene una colección de especificadores de cultura (idioma/región)
- [[Catálogo - Params#Data (parámetro)|Data (parámetro)]] — Contiene una colección de datos genéricos
- [[Catálogo - Params#Data Path (Path, parámetro)|Data Path (Path, parámetro)]] — Contiene una colección de rutas de árbol de datos
- [[Catálogo - Params#Guid (ID, parámetro)|Guid (ID, parámetro)]] — Contiene una colección de identificadores únicos globales (GUID)
- [[Catálogo - Params#Text (Txt, parámetro)|Text (Txt, parámetro)]] — Contiene una colección de fragmentos de texto

### Params › Util (2)

- [[Catálogo - Params#Cherry Picker (Item, parámetro)|Cherry Picker (Item, parámetro)]] — Toma un solo elemento de un árbol de datos
- [[Catálogo - Params#Param Viewer (Viewer, parámetro)|Param Viewer (Viewer, parámetro)]] — Un visor de estructuras de datos

### Sets › List (21)

- [[Catálogo - Sets#Combine Data (Combine)|Combine Data (Combine)]] — Combina los elementos no nulos de varias entradas
- [[Catálogo - Sets#Cross Reference (CrossRef)|Cross Reference (CrossRef)]] — Referencia cruzada de datos de varias listas
- [[Catálogo - Sets#Dispatch|Dispatch]] — Reparte (dispatch) los elementos de una lista en dos listas de destino
- [[Catálogo - Sets#Insert Items (Ins)|Insert Items (Ins)]] — Inserta una colección de elementos en una lista
- [[Catálogo - Sets#Item Index (Index)|Item Index (Index)]] — Obtiene el índice de un elemento en una lista
- [[Catálogo - Sets#List Item (Item)|List Item (Item)]] — Obtiene un elemento específico de una lista
- [[Catálogo - Sets#List Length (Lng)|List Length (Lng)]] — Mide el largo de una lista
- [[Catálogo - Sets#Longest List (Long)|Longest List (Long)]] — Alarga una colección de listas hasta el largo de la más larga
- [[Catálogo - Sets#Null Item (Null)|Null Item (Null)]] — Prueba si un dato es nulo o inválido
- [[Catálogo - Sets#Partition List (Partition)|Partition List (Partition)]] — Parte una lista en sublistas
- [[Catálogo - Sets#Pick'n'Choose (P'n'C)|Pick'n'Choose (P'n'C)]] — Elige y selecciona de un conjunto de datos de entrada
- [[Catálogo - Sets#Replace Items (Replace)|Replace Items (Replace)]] — Reemplaza ciertos elementos de una lista
- [[Catálogo - Sets#Replace Nulls (NullRep)|Replace Nulls (NullRep)]] — Reemplaza datos nulos o inválidos por otros datos
- [[Catálogo - Sets#Reverse List (Rev)|Reverse List (Rev)]] — Invierte el orden de una lista
- [[Catálogo - Sets#Shift List (Shift)|Shift List (Shift)]] — Desplaza todos los elementos de una lista
- [[Catálogo - Sets#Shortest List (Short)|Shortest List (Short)]] — Acorta una colección de listas hasta el largo de la más corta
- [[Catálogo - Sets#Sift Pattern (Sift)|Sift Pattern (Sift)]] — Separa (sift) los elementos de una lista usando un patrón de índices que se repite
- [[Catálogo - Sets#Sort List (Sort)|Sort List (Sort)]] — Ordena una lista de claves numéricas
- [[Catálogo - Sets#Split List (Split)|Split List (Split)]] — Divide una lista en partes separadas
- [[Catálogo - Sets#Sub List (SubSet)|Sub List (SubSet)]] — Extrae un subconjunto de una lista
- [[Catálogo - Sets#Weave|Weave]] — Entrelaza (weave) un conjunto de datos de entrada con un patrón personalizado

### Sets › Sequence (14)

- [[Catálogo - Sets#Char Sequence (CharSeq)|Char Sequence (CharSeq)]] — Crea una secuencia de caracteres de texto
- [[Catálogo - Sets#Cull Index (Cull i)|Cull Index (Cull i)]] — Elimina (cull) elementos indexados de una lista
- [[Catálogo - Sets#Cull Nth (CullN)|Cull Nth (CullN)]] — Elimina (cull) cada N-ésimo elemento de una lista
- [[Catálogo - Sets#Cull Pattern (Cull)|Cull Pattern (Cull)]] — Elimina (cull) elementos de una lista usando una máscara de bits que se repite
- [[Catálogo - Sets#Duplicate Data (Dup)|Duplicate Data (Dup)]] — Duplica datos una cantidad predefinida de veces
- [[Catálogo - Sets#Fibonacci (Fib)|Fibonacci (Fib)]] — Crea una sucesión de Fibonacci
- [[Catálogo - Sets#Jitter|Jitter]] — Mezcla al azar una lista de valores
- [[Catálogo - Sets#Random|Random]] — Genera una lista de números pseudoaleatorios
- [[Catálogo - Sets#Random Reduce (Reduce)|Random Reduce (Reduce)]] — Quita al azar N elementos de una lista
- [[Catálogo - Sets#Range|Range]] — Crea un rango de números
- [[Catálogo - Sets#Repeat Data (Repeat)|Repeat Data (Repeat)]] — Repite un patrón hasta alcanzar cierto largo
- [[Catálogo - Sets#Sequence (Seq)|Sequence (Seq)]] — Genera una secuencia de números
- [[Catálogo - Sets#Series|Series]] — Crea una serie de números
- [[Catálogo - Sets#Stack Data (Stack)|Stack Data (Stack)]] — Duplica elementos individuales de una lista de datos

### Sets › Sets (14)

- [[Catálogo - Sets#Carthesian Product (CProd)|Carthesian Product (CProd)]] — Crea el producto cartesiano de dos conjuntos de igual cardinalidad
- [[Catálogo - Sets#Create Set (CSet)|Create Set (CSet)]] — Crea el conjunto válido a partir de una lista de elementos (un conjunto válido solo contiene elementos…
- [[Catálogo - Sets#Delete Consecutive (DCon)|Delete Consecutive (DCon)]] — Elimina miembros similares consecutivos de un conjunto
- [[Catálogo - Sets#Disjoint|Disjoint]] — Prueba si dos conjuntos son disjuntos
- [[Catálogo - Sets#Find similar member (FSim)|Find similar member (FSim)]] — Busca el miembro más parecido en un conjunto
- [[Catálogo - Sets#Key/Value Search (KeySearch)|Key/Value Search (KeySearch)]] — Extrae un elemento de una colección según una coincidencia clave-valor
- [[Catálogo - Sets#Member Index (MIndex)|Member Index (MIndex)]] — Busca las apariciones de un miembro específico en un conjunto
- [[Catálogo - Sets#Replace Members (Replace)|Replace Members (Replace)]] — Reemplaza miembros de un conjunto
- [[Catálogo - Sets#Set Difference (Difference)|Set Difference (Difference)]] — Crea la diferencia de dos conjuntos (los objetos presentes en A pero no en B)
- [[Catálogo - Sets#Set Difference (S) (ExDiff)|Set Difference (S) (ExDiff)]] — Crea la diferencia simétrica de dos conjuntos (los objetos presentes en A o en B, pero no en ambos)
- [[Catálogo - Sets#Set Intersection (Intersection)|Set Intersection (Intersection)]] — Crea la intersección de dos conjuntos (los objetos únicos presentes en ambos conjuntos)
- [[Catálogo - Sets#Set Majority (Majority)|Set Majority (Majority)]] — Determina qué miembros aparecen en la mayoría de tres conjuntos
- [[Catálogo - Sets#Set Union (SUnion)|Set Union (SUnion)]] — Crea la unión de dos conjuntos (los objetos únicos presentes en cualquiera de los dos)
- [[Catálogo - Sets#SubSet|SubSet]] — Prueba la inclusión entre dos conjuntos

### Sets › Text (14)

- [[Catálogo - Sets#Characters (Chars)|Characters (Chars)]] — Separa un texto en caracteres individuales
- [[Catálogo - Sets#Concatenate (Concat)|Concatenate (Concat)]] — Concatena fragmentos de texto
- [[Catálogo - Sets#Format|Format]] — Da formato a datos usando marcadores de posición y etiquetas de formato
- [[Catálogo - Sets#Match Text (TMatch)|Match Text (TMatch)]] — Compara un texto con un patrón
- [[Catálogo - Sets#Replace Text (Rep)|Replace Text (Rep)]] — Reemplaza todas las apariciones de un fragmento de texto por otro
- [[Catálogo - Sets#Sort Text (TSort)|Sort Text (TSort)]] — Ordena una colección de fragmentos de texto
- [[Catálogo - Sets#Text Case (Case)|Text Case (Case)]] — Cambia las MaYúScUlAs de un texto
- [[Catálogo - Sets#Text Distance (TDist)|Text Distance (TDist)]] — Calcula la distancia de Levenshtein entre dos fragmentos de texto
- [[Catálogo - Sets#Text Fragment (Fragment)|Text Fragment (Fragment)]] — Extrae un fragmento (subconjunto) de un texto
- [[Catálogo - Sets#Text Join (Join)|Text Join (Join)]] — Une una colección de fragmentos de texto en uno
- [[Catálogo - Sets#Text Length (Len)|Text Length (Len)]] — Obtiene el largo (cantidad de caracteres) de un texto
- [[Catálogo - Sets#Text On Surface (TextSrf)|Text On Surface (TextSrf)]] — Crea una colección de símbolos de texto alineados sobre una superficie
- [[Catálogo - Sets#Text Split (Split)|Text Split (Split)]] — Divide un texto en fragmentos usando separadores
- [[Catálogo - Sets#Text Trim (Trim)|Text Trim (Trim)]] — Quita los espacios en blanco al inicio y al final de un texto

### Sets › Tree (26)

- [[Catálogo - Sets#Clean Tree (Clean)|Clean Tree (Clean)]] — Quita todos los elementos nulos e inválidos de un árbol de datos
- [[Catálogo - Sets#Construct Path (Path)|Construct Path (Path)]] — Construye una ruta de rama de un árbol de datos
- [[Catálogo - Sets#Deconstruct Path (DPath)|Deconstruct Path (DPath)]] — Descompone una ruta de árbol de datos en enteros individuales
- [[Catálogo - Sets#Entwine|Entwine]] — Aplana y combina una colección de flujos de datos
- [[Catálogo - Sets#Explode Tree (BANG!)|Explode Tree (BANG!)]] — Extrae todas las ramas de un árbol
- [[Catálogo - Sets#Flatten Tree (Flatten)|Flatten Tree (Flatten)]] — Aplana un árbol de datos quitando toda la información de ramas
- [[Catálogo - Sets#Flip Matrix (Flip)|Flip Matrix (Flip)]] — Voltea un árbol de datos tipo matriz intercambiando filas y columnas
- [[Catálogo - Sets#Graft Tree (Graft)|Graft Tree (Graft)]] — Injerta (graft) un árbol de datos agregando una rama extra por cada elemento
- [[Catálogo - Sets#Match Tree (Match)|Match Tree (Match)]] — Hace coincidir un árbol de datos con otro
- [[Catálogo - Sets#Merge|Merge]] — Fusiona varios flujos de datos
- [[Catálogo - Sets#Path Compare (Compare)|Path Compare (Compare)]] — Compara una ruta con un patrón de máscara
- [[Catálogo - Sets#Path Mapper (parámetro)|Path Mapper (parámetro)]] — Realiza operaciones léxicas sobre árboles de datos
- [[Catálogo - Sets#Prune Tree (Prune)|Prune Tree (Prune)]] — Quita las ramas pequeñas de un árbol de datos
- [[Catálogo - Sets#Relative Item (RelItem)|Relative Item (RelItem)]] — Obtiene un par de elementos relativos de un árbol de datos
- [[Catálogo - Sets#Relative Items (RelItem2)|Relative Items (RelItem2)]] — Obtiene un par de elementos relativos de dos árboles de datos
- [[Catálogo - Sets#Replace Paths (Replace)|Replace Paths (Replace)]] — Busca y reemplaza rutas en un árbol de datos
- [[Catálogo - Sets#Shift Paths (PShift)|Shift Paths (PShift)]] — Desplaza los índices de todas las rutas de un árbol de datos
- [[Catálogo - Sets#Simplify Tree (Simplify)|Simplify Tree (Simplify)]] — Simplifica un árbol de datos quitando la parte de la ruta que comparten todas las ramas
- [[Catálogo - Sets#Split Tree (Split)|Split Tree (Split)]] — Divide un árbol de datos en dos partes usando máscaras de ruta
- [[Catálogo - Sets#Stream Filter (Filter)|Stream Filter (Filter)]] — Filtra una colección de flujos de entrada
- [[Catálogo - Sets#Stream Gate (Gate)|Stream Gate (Gate)]] — Redirige un flujo hacia salidas específicas
- [[Catálogo - Sets#Tree Branch (Branch)|Tree Branch (Branch)]] — Obtiene una rama específica de un árbol de datos
- [[Catálogo - Sets#Tree Item (Item)|Tree Item (Item)]] — Obtiene un elemento específico de un árbol de datos
- [[Catálogo - Sets#Tree Statistics (TStat)|Tree Statistics (TStat)]] — Obtiene estadísticas de un árbol de datos
- [[Catálogo - Sets#Trim Tree (Trim)|Trim Tree (Trim)]] — Reduce la complejidad de un árbol fusionando las ramas más externas
- [[Catálogo - Sets#Unflatten Tree (Unflatten)|Unflatten Tree (Unflatten)]] — Desaplana un árbol de datos devolviendo los elementos a sus ramas

### eleFront › 07 Trees (9)

- [[Catálogo - eleFront#Clean Parallel (CleanP)|Clean Parallel (CleanP)]] — Limpia el árbol de datos principal y entrega todos los objetos secundarios respectivos por elemento
- [[Catálogo - eleFront#Create Tree (Tree)|Create Tree (Tree)]] — Crea un árbol indicando una ruta de rama para cada elemento
- [[Catálogo - eleFront#Duplicate Data Match (Dup)|Duplicate Data Match (Dup)]] — Duplica datos según un árbol de datos de origen
- [[Catálogo - eleFront#Get Matching Branches (GetBrn)|Get Matching Branches (GetBrn)]] — Toma las ramas de un árbol paralelo con las mismas rutas. Puede quitar las vacías
- [[Catálogo - eleFront#Graft By Index (GraftI)|Graft By Index (GraftI)]] — Injerta (graft) elementos en ramas nuevas usando un índice para la rama de destino. Cada elemento del árbol…
- [[Catálogo - eleFront#Graft Match (GraftM)|Graft Match (GraftM)]] — Hace coincidir árboles secundarios con un árbol guía por prefijo de ruta. Una rama secundaria coincide cuando…
- [[Catálogo - eleFront#Graft Parallel (GraftP)|Graft Parallel (GraftP)]] — Injerta (graft) el árbol de datos principal y entrega todos los objetos secundarios respectivos por elemento
- [[Catálogo - eleFront#Shift To Depth (ShfDep)|Shift To Depth (ShfDep)]] — Desplaza un árbol de datos a una profundidad indicada
- [[Catálogo - eleFront#ShiftMatch (ShiftM)|ShiftMatch (ShiftM)]] — Desplaza un árbol de datos para que coincida con la estructura de un árbol guía

### Human › Misc (3)

- [[Catálogo - Human#Dispatch Multiple (MDispatch)|Dispatch Multiple (MDispatch)]] — Reparte (dispatch) varias listas a la vez. Solo obtiene los valores True; usa invertir para obtener los otros
- [[Catálogo - Human#Filter By Item (IFilter)|Filter By Item (IFilter)]] — Filtra una o varias listas según una lista guía y un subconjunto de esa lista guía
- [[Catálogo - Human#Item Selector (List, parámetro)|Item Selector (List, parámetro)]] — Permite seleccionar uno o varios elementos de una lista de entrada

### LunchBox › Util (19)

- [[Catálogo - LunchBox#Arc Divide (ArcDivide)|Arc Divide (ArcDivide)]] — Divide una curva spline en segmentos de arco tangentes
- [[Catálogo - LunchBox#Brep Join Progression (BrepJoin)|Brep Join Progression (BrepJoin)]] — Une progresivamente caras de Brep con un valor de tolerancia. Las caras se unen progresivamente en el orden…
- [[Catálogo - LunchBox#Brep Join with Tolerance (BrepJoin)|Brep Join with Tolerance (BrepJoin)]] — Une caras de Brep con un valor de tolerancia
- [[Catálogo - LunchBox#Create RTree (RTree)|Create RTree (RTree)]] — Crea un RTree en el que se puede buscar
- [[Catálogo - LunchBox#Deconstruct Wireframe (DeWire)|Deconstruct Wireframe (DeWire)]] — Organiza una estructura de curvas en alambre en nodos y ejes
- [[Catálogo - LunchBox#Flatness Check (Flat)|Flatness Check (Flat)]] — Revisa la planitud de un panel cuadrangular
- [[Catálogo - LunchBox#Patch Surface (Patch)|Patch Surface (Patch)]] — Devuelve una superficie de parche (patch) a partir de una lista de curvas de borde. (Solo Rhino 5)
- [[Catálogo - LunchBox#Random Split List (RandomSplit)|Random Split List (RandomSplit)]] — Divide al azar una lista en dos listas
- [[Catálogo - LunchBox#Rebuild Surface (RebuildSrf)|Rebuild Surface (RebuildSrf)]] — Reconstruye una superficie sin recortar usando parámetros U y V
- [[Catálogo - LunchBox#Relative Coordinates (Relative)|Relative Coordinates (Relative)]] — Devuelve las coordenadas de un punto respecto de un plano
- [[Catálogo - LunchBox#Reverse Surface Direction (RevSrf)|Reverse Surface Direction (RevSrf)]] — Invierte las direcciones UV de una superficie
- [[Catálogo - LunchBox#Shell Brep (Shell)|Shell Brep (Shell)]] — Crea un cascarón hueco a partir de un Brep sólido
- [[Catálogo - LunchBox#Shortest Walk (Walk)|Shortest Walk (Walk)]] — Busca el "camino más corto" (Shortest Walk) dentro de una red de curvas. Este nodo usa código actualizado…
- [[Catálogo - LunchBox#Sort Adjacent Brep Faces (Adjacent)|Sort Adjacent Brep Faces (Adjacent)]] — Devuelve una estructura ordenada de caras de Brep adyacentes a otras caras
- [[Catálogo - LunchBox#Sort Duplicate Breps (Sort Brep)|Sort Duplicate Breps (Sort Brep)]] — Ordena una lista de Breps según sus duplicados
- [[Catálogo - LunchBox#Sort Duplicate Curves (Sort Crv)|Sort Duplicate Curves (Sort Crv)]] — Ordena una lista de curvas según sus duplicados, usando las tolerancias del documento
- [[Catálogo - LunchBox#Sort Duplicate Points (Sort Pts)|Sort Duplicate Points (Sort Pts)]] — Ordena una lista de puntos según sus duplicados
- [[Catálogo - LunchBox#Sort Duplicate Values (Sort Val)|Sort Duplicate Values (Sort Val)]] — Ordena una lista de números o textos según sus duplicados
- [[Catálogo - LunchBox#String Distance (Str Dist)|String Distance (Str Dist)]] — Evalúa la "distancia" (diferencia) entre dos textos con el algoritmo de Levenshtein. Una distancia de 0…

### Pufferfish › List (8)

- [[Catálogo - Pufferfish#Dispatch Indices (DispDexs)|Dispatch Indices (DispDexs)]] — Reparte (dispatch) una lista de elementos en dos listas según un conjunto de índices: los que están en esos…
- [[Catálogo - Pufferfish#Last Index (LastDex)|Last Index (LastDex)]] — Obtiene el último índice de una lista (largo de la lista - 1)
- [[Catálogo - Pufferfish#List Indices (ListDexs)|List Indices (ListDexs)]] — Obtiene la lista de índices de una lista de elementos
- [[Catálogo - Pufferfish#Mirror Combine Items (MirComItems)|Mirror Combine Items (MirComItems)]] — Refleja un conjunto de elementos de lista desde su final o su inicio y lo combina con el conjunto original
- [[Catálogo - Pufferfish#Mirror Cut Items (MirCutItems)|Mirror Cut Items (MirCutItems)]] — Corta un conjunto de elementos de lista en un índice, refleja el lado conservado del corte respecto de ese…
- [[Catálogo - Pufferfish#Null Placeholder (Null)|Null Placeholder (Null)]] — Entrega un elemento nulo que se puede usar como marcador de posición en listas
- [[Catálogo - Pufferfish#Point Sort Items (PtSortItems)|Point Sort Items (PtSortItems)]] — Ordena un conjunto de elementos de lista de forma sincronizada, según el orden por punto más cercano…
- [[Catálogo - Pufferfish#Sift Indices (SiftDexs)|Sift Indices (SiftDexs)]] — Separa (sift) una lista de elementos en dos listas según un conjunto de índices: los que están en esos…

<!-- AUTO:fin -->
