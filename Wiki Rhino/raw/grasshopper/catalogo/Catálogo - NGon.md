---
title: "Catálogo Grasshopper — NGon"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "NGon"
libraries: ["NGon_RH8 1.0.0.0"]
components: 122
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/ngon, geometria/mallas]
---

# NGon

122 objetos · librería: NGon_RH8 1.0.0.0

Mapas: [[Mapa - Mallas y SubD]] (122) · [[Mapa - Fabricación]] (4) · [[Mapa - Brep y sólidos]] (2)

## Adjacency

### Mesh Edges (MeshEdges)

Obtiene toda la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| AllE | `AE` | Line | árbol | Todas las aristas de la malla |
| NakedE | `NE` | Line | árbol | Aristas desnudas de la malla |

### Naked Vertices (Naked)

Vértices desnudos de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Vértices desnudos |
| Status | `S` | Boolean | lista | Estado desnudo |

### NGon Centers (NGonCenters)

GetNGonCenter

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centers | `C` | Point | lista | Centros de los NGons |
| Normals | `N` | Vector | lista | Normal promedio en el centro del ngon |
| Planes | `P` | Plane | lista | Planos promedio en el centro del ngon |

### NGon Edges (Edges)

Obtiene los ids y las líneas de todas las aristas de los ngons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Line | árbol | Obtiene las aristas de la malla en todos los ngons |
| ID | `I` | Integer | árbol | Obtiene las aristas de la malla (como líneas) en todos los ngons |
| NakedID | `NID` | Boolean | árbol | Aristas desnudas |
| Normal | `NN` | Vector | árbol | Normal de la arista como promedio de los vértices adyacentes |
| Naked | `N` | Line | árbol | Aristas desnudas como líneas |
| AllE | `AE` | Line | árbol | Todas las aristas de la malla |

### NGon Face Edges (Face Edges)

Obtiene los ids y las líneas de las aristas de las caras de los ngons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| TextSize *(opcional)* | `T` | Number | item | Tamaño del texto mostrado |
| Edge Scale *(opcional)* | `S` | Number | item | Escala de las aristas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Line | árbol | Obtiene las aristas de la malla en las caras de los ngons |
| ID | `I` | Integer | árbol | Obtiene las aristas de la malla (como líneas) en las caras de los ngons |
| FID | `F` | Integer | árbol | Caras vecinas |

### NGon Face Edges by NGon Pairs (EdgeByFP)

Obtiene las aristas de las caras de los NGons por pares de NGons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| NGon Face Pair | `P` | Integer | árbol | Pares de caras de NGon (árbol de datos) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Line | lista | Obtiene las aristas (como líneas) de los pares de ngons en las caras de los ngons |
| ID | `I` | Integer | lista | Obtiene las aristas de los ngons |
| Flag | `F` | Boolean | lista | Pertenece al par |

### NGon Face Edges Points (Face Edges Points)

Obtiene los ids y las líneas de las aristas de las caras de los ngons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| Dist | `D` | Number | item | Distancia de división |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P | `P` | Point | árbol | Puntos de arista |

### NGon Face Vertices (NGFaceVertices)

Obtiene los vértices de los ngons y los vértices topológicos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | árbol | Obtiene los vértices de la malla en los ngons |
| ID | `I` | Integer | árbol | Obtiene los vértices de la malla en los ngons |
| TopoID | `IT` | Integer | árbol | Obtiene los vértices topológicos de la malla en los ngons |

### NGon Faces (NGonFaces)

Obtiene las caras de la malla en los NGons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Faces | `F` | Curve | árbol | Obtiene las caras de la malla en los ngons |
| Faces | `I` | Integer | árbol | Obtiene las caras de la malla en los ngons |

### NGon To NGons (NGonToNgons)

Obtiene los NGons adyacentes al NGon actual

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| AdjNgons | `A` | Integer | árbol | Obtiene los NGons adyacentes al NGon actual |
| V | `V` | Integer | árbol | V |
| E0 | `E0` | Integer | árbol | E0 |
| E1 | `E1` | Integer | árbol | E1 |

### NGon Vertices (Vertices)

Obtiene todos los vértices de los ngons y sus vértices conectados en los ngons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | árbol | Obtiene los vértices de la malla en los ngons (HashSet) |
| Vertices | `N` | Point | árbol | Vértices conectados a los vértices de la malla en los ngons (HashSet) |
| ID | `I` | Integer | árbol | Obtiene los vértices de la malla en los ngons (HashSet) |
| NID | `I` | Integer | árbol | Ids de los vértices conectados a los vértices de la malla en los ngons (HashSet) |

### NGon Vertices (Vertices) · 2

Obtiene todos los vértices de los ngons y los vértices topológicos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | árbol | Obtiene los vértices de la malla en los ngons (HashSet) |
| ID | `I` | Integer | árbol | Obtiene los vértices de la malla en los ngons (HashSet) |
| Naked | `N` | Boolean | árbol | Vértices desnudos |
| V | `V` | Integer | árbol | V |
| E0 | `E0` | Integer | árbol | E0 |
| E1 | `E1` | Integer | árbol | E1 |

### NGons Around Vertices (Vertex Ngons)

Obtiene los ngons que rodean los vértices topológicos de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| Naked *(opcional)* | `N` | Boolean | item | Eliminar los desnudos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Index | `I` | Integer | árbol | Índice del NGon |
| Naked | `N` | Boolean | lista | Estado desnudo de los vértices topológicos del NGon (ojo: la cantidad y el orden de los vértices topológicos de los ngons difiere del orden de la lista de vértices topológicos de la malla) |

### NGons Connected To NGon Edge (EdgeNGon)

Obtiene los ngons conectados a las aristas de los ngons; se agrega -1 al inicio de la lista si la arista es desnuda (propiedad izquierda/derecha en mallas limpias)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| Naked *(opcional)* | `N` | Boolean | item | Agregar -1 en aristas desnudas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| EF | `EF` | Integer | árbol | Conectividad arista-cara |
| EFPair | `EF` | Integer | árbol | Conectividad arista-cara (solo dos caras) |
| DihedralAngle | `A` | Number | árbol | Ángulo diedro |
| DihedralAngleLocation | `AL` | Line | árbol | Ubicación de la arista del ángulo diedro |

### NGons Edges Around Vertices (VEdge Ngons)

Obtiene los ngons que rodean los vértices topológicos de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Curve | árbol | Líneas conectadas a los vértices de los ngons |
| Index | `I` | Integer | árbol | Índice de la arista |

### Scale NGon Face Edges by NGon Pairs (SEdge)

Escala de Get NGon Face Edges by NGon Pairs

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| NGon Face Pair | `P` | Integer | árbol | Pares de caras de NGon (árbol de datos) |
| Scale | `S` | Number | item | Escala las aristas de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Line | lista | Obtiene las aristas (como líneas) de los pares de ngons en las caras de los ngons |
| ID | `I` | Integer | lista | Obtiene las aristas de los ngons |
| Flag | `F` | Boolean | lista | Pertenece al par |
| Edges | `E` | Line | árbol | Obtiene las aristas (como líneas) de los pares de ngons en las caras de los ngons |
| Polylines | `P` | Curve | lista | Conexiones |

## Graph

### BFS

Búsqueda en anchura (BFS) desde la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Start *(opcional)* | `V` | Text | item | Vértice inicial |
| Sequence *(opcional)* | `Sequence` | Integer | lista | Secuencia |
| SequenceCrv *(opcional)* | `SequenceCrv` | Curve | item | Curva de la secuencia |
| CustomVectors *(opcional)* | `CustomVectors` | Line | lista | Vectores personalizados |
| Angle *(opcional)* | `Angle` | Number | item | Ángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Integer | árbol | Ids de las caras de la malla |
| Edges | `E` | Integer | árbol | Ids de los pares de caras de la malla |
| EdgeVec | `EV` | Vector | árbol | Vectores de arista |
| Bad | `Bad` | Line | árbol | Aristas defectuosas |
| Mesh | `M` | Mesh | item | Malla |
| FaceVec | `FV` | Vector | lista | Vectores de cara |

### Coloring

Colorea las aristas con n colores

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| n | `n` | Integer | item | n |
| EF | `EF` | Boolean | item | Color de aristas o caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `Edges` | Curve | árbol | Aristas |
| ID | `ID` | Integer | lista | ID |

### ConvexHull

Envolvente convexa a partir de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Polyline | `C` | Curve | item | Polilínea |
| Points | `P` | Point | lista | Puntos |
| Index | `I` | Integer | lista | IDs de los puntos |

### KMeans

KMeans

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Clusters | `N` | Integer | item | Cantidad de clústeres |
| W *(opcional)* | `W` | Number | lista | W |
| D | `D` | Number | lista | D |
| D | `D` | Number | lista | D |
| D | `D` | Number | lista | D |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Index | `I` | Integer | lista | Índices de los clústeres |
| DataTree | `T` | Integer | árbol | Usar el elemento de la lista |

### LineGraph

Grafo de líneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | lista | Lista de líneas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Topology Points | `TP` | Generic Data | lista | Puntos topológicos |
| Nodes | `N` | Generic Data | lista | Nodos |
| Topology Edges U | `U` | Generic Data | lista | Aristas topológicas U |
| Topology Edges V | `V` | Generic Data | lista | Aristas topológicas V |
| Weights | `W` | Generic Data | lista | Pesos |
| Adj | `Adj` | Generic Data | árbol | Adyacencia |

### MeshCurve

MeshCurve

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Lista de polilíneas |
| Radius *(opcional)* | `r` | Number | lista | Radio de cada nodo |
| Circles *(opcional)* | `C` | Circle | lista | Círculos para la escala |
| U *(opcional)* | `U` | Integer | item | División en una dirección |
| V *(opcional)* | `V` | Integer | item | División en la segunda dirección |
| VDist *(opcional)* | `VD` | Number | item | División de la arista por longitud |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Anchors0 | `P0` | Point | árbol | Puntos en el extremo de cada línea |
| Anchors1 | `P1` | Point | árbol | Puntos en el extremo de cada línea y sobre el arco |
| Outlines | `C` | Curve | árbol | Contornos de cada cuadrilátero |
| Nodes | `N` | Curve | lista | Nodos del grafo en los que mostrar el radio |

### MeshSkeleton

MeshSkeleton

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Points *(opcional)* | `P` | Point | lista | Debe haber la misma cantidad de puntos que de caras de la malla; si no, se ignoran |
| Smooth *(opcional)* | `I` | Integer | item | Iteraciones de suavizado |
| Prune *(opcional)* | `N` | Integer | item | Podar ramas desnudas (iteraciones) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Skeleton | `S` | Curve | lista | Líneas del esqueleto |
| 3ValenceLines | `3L` | Curve | árbol | Líneas dibujadas desde el punto de la cara hasta sus vértices |
| Naked Points | `P` | Point | árbol | Puntos extremos del esqueleto |
| All End Points | `P` | Point | lista | Todos los puntos extremos |

### Walker

Walker

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `Polylines` | Curve | lista | Polilíneas |
| Flip | `Flip` | Boolean | item | Invertir |
| Inflate | `Inflate` | Number | item | Inflar |
| RotX | `RotX` | Number | item | RotX |
| RotY | `RotY` | Number | item | RotY |
| MaxLength | `MaxLength` | Integer | item | Longitud máxima |
| Commbine | `Commbine` | Boolean | item | Combinar recorridos impares |
| MaxIterations | `Loops` | Integer | item | Iteraciones máximas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dijkstra | `Dijkstra` | Generic Data | árbol | Dijkstra |
| Line | `Line` | Line | item | Línea |
| OddWalks | `OddWalks` | Integer | item | Recorridos impares |

## Joint

### Finger

Dedo en el plano

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Dist *(opcional)* | `A` | Number | item | Distancia de offset |
| Dist *(opcional)* | `B` | Number | item | Distancia de offset |
| Scale *(opcional)* | `S` | Number | item | Escalar desde las esquinas |
| Plines *(opcional)* | `P` | Curve | árbol | Polilíneas adicionales |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla |
| Curves | `C` | Curve | árbol | Curvas |
| AddPolylines | `A` | Curve | árbol | Polilíneas adicionales usadas para crear un contorno tipo placa con offset |

### JointsVDA

JointsVDA

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `Mesh` | Mesh | item | Malla necesaria para la topología |
| InsertionVec *(opcional)* | `InsertionVec` | Vector | árbol | Vectores de inserción |
| Panels *(opcional)* | `Panels` | Curve | árbol | Contornos de los paneles como polilíneas |
| TwoJoints *(opcional)* | `TwoJoints` | Point | lista | Marcadores de dos puntos de unión |
| ExtendedJoints *(opcional)* | `ExtendedJoints` | Line | lista | Unión extendida como marcadores de líneas |
| DeeperCutsJoints *(opcional)* | `DeeperCutsJoints` | Line | lista | Cortes más profundos de unión como marcadores de líneas |
| Center *(opcional)* | `Center` | Boolean | item | Orientar la unión hacia el centro |
| Finger *(opcional)* | `Finger` | Boolean | item | Crea una unión de dedos (finger joint) |
| Iterations *(opcional)* | `Iterations` | Integer | item | Iteraciones |
| Sequence *(opcional)* | `Sequence` | Integer | lista | Secuencia |
| TextScale *(opcional)* | `TextScale` | Number | lista | 0 - tamaño del panel, 1 - tamaño de la unión, 2 - tamaño adyacente, 3 - posición adyacente, 4 - centro de escala adyacente, 5 - posición de la unión, 6 - últimos elementos, 7 - extender |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Curve | árbol | Polilíneas de los paneles |
| Joints | `Joints` | Curve | árbol | Polilíneas de las uniones |
| PanelsMid | `PanelsMid` | Curve | árbol | Polilíneas de los paneles |
| JointsMid | `JointsMid` | Curve | árbol | Polilíneas de las uniones |
| PanelsP | `PanelsP` | Plane | árbol | Planos de los paneles |
| JointsP | `JointsP` | Plane | árbol | Planos de las uniones |
| PanelsTxt | `PanelsTxt` | Curve | árbol | Texto de numeración de los paneles |
| JointsTxt | `JointsTxt` | Curve | árbol | Texto de numeración de las uniones |
| PanelsLast | `PanelsLast` | Curve | árbol | Polilíneas de los paneles |
| JointsLast | `JointsLast` | Curve | árbol | Polilíneas de las uniones |
| PanelsMidLast | `PanelsMidLast` | Curve | árbol | Polilíneas de los paneles |
| JointsMidLast | `JointsMidLast` | Curve | árbol | Polilíneas de las uniones |
| PanelsPLast | `PanelsPLast` | Plane | árbol | Planos de los paneles |
| JointsPLast | `JointsPLast` | Plane | árbol | Planos de las uniones |
| PanelsTxtLast | `PanelsTxtLast` | Curve | árbol | Texto de numeración de los paneles |
| JointsTxtLast | `JointsTxtLast` | Curve | árbol | Texto de numeración de las uniones |

### MeshCollision (MC)

MeshCollision

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | lista | M |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| I | `I` | Integer | lista | I |

### MeshFlap

MeshFlap

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Dist *(opcional)* | `D` | Number | item | Distancia de offset |
| Flip *(opcional)* | `F` | Boolean | item | Invertir |
| Normals *(opcional)* | `N` | Boolean | item | Offset según las normales de las caras |
| Chamfer *(opcional)* | `C` | Boolean | item | Arista con chaflán |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla |
| Curves | `C` | Curve | árbol | Curvas |

## NGons

### AddNGons

Agrega NGons a las caras triangulares planas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Pair *(opcional)* | `P` | Integer | item | Buscar un par: 0 - todos los polígonos planos, 1 - par, 2 - par ordenado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | árbol | Polilíneas de las aristas desnudas |
| Polylines | `P` | Curve | árbol | Polilíneas de las aristas desnudas |
| Mesh | `M` | Mesh | item | Malla |

### Clear

Borrar los ngons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Generic Data | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Generic Data | item | Malla |

### From Brep

Crea una malla a partir de un brep poligonal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep poligonal |
| Weld *(opcional)* | `W` | Number | item | Soldar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Polylines | `P` | Curve | lista | Contornos de las caras del brep |

### From Mesh

Toma una malla y agrega ngons con el contorno de las aristas desnudas y la colección de todas las caras de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| ID *(opcional)* | `I` | Integer | item | Elige qué contorno |
| It *(opcional)* | `I` | Integer | item | Iteraciones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| VertexID | `V` | Integer | árbol | Id de los vértices de las aristas desnudas |
| Polylines | `P` | Curve | árbol | Polilíneas de las aristas desnudas |

### From Polylines (FromP)

Crea una malla a partir de polilíneas y agrega propiedades de NGons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Polilíneas o curvas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Get Polylines (ToP)

Revisa si hay ngons en una malla y los extrae

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | lista | Polilíneas |

### MeshStatistics

MeshStatistics

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| NGons | `F` | Integer | item | Cantidad de NGons o caras |
| Edges | `E` | Integer | item | Cantidad de NGons o aristas |
| Vertices | `V` | Integer | item | Cantidad de NGons o vértices |

### NgonH

Ngon con agujeros, Delaunay con agujeros

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | lista | Polilíneas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### NGonPreview

NGonPreview

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | árbol | Malla |
| Front *(opcional)* | `F` | Colour | item | Color de la cara frontal |
| Back *(opcional)* | `B` | Colour | item | Color de la cara posterior |
| LineColor *(opcional)* | `C` | Colour | item | Color de las líneas |

## Planarize

### Planar Faces (Planar)

Planariza los NGons de las caras vecinas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | lista | Polilíneas para la malla |
| Lines | `L` | Curve | árbol | Líneas de la intersección con planos, para depuración |

### Planarize

Planarize

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Tolerance | `T` | Number | item | Tolerancia de planaridad |
| Iterations | `I` | Integer | item | Iteraciones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| P | `P` | Plane | lista | P |
| P | `P` | Point | lista | P |

### Planarize2

Planarize2

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Malla |
| Tangential *(opcional)* | `Tangential` | Number | item | Tangencial |
| Iterations *(opcional)* | `Iterations` | Integer | item | Iteraciones |
| StaticSolver *(opcional)* | `StaticSolver` | Boolean | item | StaticSolver |
| Run *(opcional)* | `Run` | Boolean | item | Ejecutar |
| Reset *(opcional)* | `Reset` | Boolean | item | Reiniciar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Malla |

### Project NGons (Project)

Proyecta los ngons a sus planos promedio

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| Offset | `O` | Number | item | Offset del ngon: las normales de los vértices del ngon se intersectan con el plano de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | lista | Proyecta polilíneas a sus planos promedio |

### ProjectPairs

ProjectPairs

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Scale | `S` | Number | item | Para animaciones: agrega un slider de 0.00 a 1.00 para interpolar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla |
| Plines | `P` | Curve | árbol | Polilíneas |

## Polygon

### Boolean

Booleano de polilíneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Curve | lista | La primera polilínea |
| B *(opcional)* | `B` | Curve | lista | La primera polilínea |
| BooleanType | `BT` | Integer | item | Tipo: (0: intersección, 1: unión, 2: diferencia, 3: xor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado simple |

### Chamfer

Corta una curva abierta con una curva cerrada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Poly | `P` | Curve | item | Polilínea |
| Chamfer *(opcional)* | `C` | Number | item | Valores de chaflán: un número positivo es un valor escalar; uno negativo, una distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | item | Curvas |

### ClosestCurveComponent (CPCurve)

Busca las curvas más cercanas según una tolerancia

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Busca las curvas más cercanas |
| Tolerance *(opcional)* | `T` | Number | item | Distancia de búsqueda |
| Eccent *(opcional)* | `E` | Number | item | Desviación respecto del valor dado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| C0 | `C0` | Curve | lista | Curva más cercana A |
| C1 | `C1` | Curve | lista | Curva más cercana B |
| I0 | `I0` | Integer | lista | ID de la curva más cercana A; un valor negativo indica que la curva toca por un extremo |
| I1 | `I1` | Integer | lista | ID de la curva más cercana B; un valor negativo indica que la curva toca por un extremo |
| T0 | `T0` | Number | lista | Parámetro de la curva más cercana A |
| T1 | `T1` | Number | lista | Parámetro de la curva más cercana B |
| D | `D` | Generic Data | item | Datos de los parámetros más cercanos |

### CurveCP

Si el punto está cerca de una curva dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos |
| Curve | `C` | Curve | item | Curva en la que buscar un punto cercano |
| Tol *(opcional)* | `T` | Number | item | Distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos |
| ID | `I` | Integer | lista | Índices de los puntos más cercanos |

### CurveCut

Corta una curva abierta con una curva cerrada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ClosedCurve | `Closed` | Curve | item | Curvas |
| Curves | `C` | Curve | lista | Curvas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas |
| Type | `T` | Integer | lista | -1 - la curva está fuera, 0 - coincidente, 1 - dentro |

### CurveEnds

Corrige los extremos de la curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas |
| Points *(opcional)* | `P` | Point | lista | Puntos a los que ajustar |
| Tolerance *(opcional)* | `D` | Number | item | Distancia a la que los puntos afectan la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas |

### CurveLoft

Hace loft de curvas a una malla de cuadriláteros. Si no se entrega el parámetro V, la división por defecto en la dirección V se basa en la entrada C0: puntos extremos para una curva / puntos de control para una polilínea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CurveFirst *(opcional)* | `C0` | Curve | item | Curvas |
| Curves | `C` | Curve | lista | Curvas |
| DivisionsU *(opcional)* | `U` | Integer | item | Divisiones en la primera dirección |
| DivisionsV *(opcional)* | `V` | Integer | item | Divisiones en la segunda dirección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla |
| D | `D` | Integer | item | D |

### CurveMatch

CurveMatch

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas |
| Type | `T` | Number | item | Tipo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | item | Curvas |
| Curves | `C` | Curve | item | Curvas |

### CurvePreview (Display)

CurvePreview

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | árbol | Curva |
| Width *(opcional)* | `W` | Integer | árbol | Ancho |
| Colour *(opcional)* | `S` | Colour | árbol | Color |

### CurveShatter

Fragmenta curvas con puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva |
| Points | `P` | Point | lista | Puntos a los que ajustar |
| Tolerance *(opcional)* | `D` | Number | item | Distancia a la que los puntos afectan la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas |

### CurveSort

Ordena una lista de curvas según otras curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CurvesGuide | `CurvesGuide` | Curve | lista | Curvas |
| CurvesToSort | `CurvesToSort` | Curve | lista | Curvas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | árbol | Curvas |

### GetTwo

Obtiene los dos contornos más grandes

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep |
| Type | `T` | Integer | item | 0 - dos curvas, otro valor - todas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas |

### Intersection

Intersección de polilíneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve0 | `C0` | Curve | lista | Una lista de curvas a cortar |
| Curve1 | `C1` | Curve | lista | Una lista de curvas de corte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| InnerCurves | `I` | Curve | lista | Una lista de curvas interiores |
| CutCurves | `C` | Curve | lista | Una lista de curvas cortadas |
| EdgeCurves | `E` | Curve | lista | Una lista de curvas de borde |

### LineExtrude

LineExtrude

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea |
| Vector *(opcional)* | `V` | Vector | item | Vector |
| Dist *(opcional)* | `D` | Number | item | Distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea |

### MapCrv

Mapea una lista de curvas de una polilínea a otra

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Una lista de curvas |
| Source0 | `S0` | Curve | item | Polilínea de origen 0 |
| Target0 | `T0` | Curve | item | Polilínea de destino 0 |
| Source1 *(opcional)* | `S1` | Curve | item | Polilínea de origen 1 |
| Target1 *(opcional)* | `T1` | Curve | item | Polilínea de destino 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Una lista de curvas |

### MapMesh

Mapeo de polilínea a malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curva a mapear |
| Mesh0 | `M0` | Generic Data | item | Malla de origen |
| Mesh1 | `M1` | Generic Data | item | Malla de destino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Una lista de curvas |

### MapSrf

Mapeo de polilínea a superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curva a mapear |
| Srf0 | `S0` | Surface | item | Malla de origen |
| Srf1 | `S1` | Surface | item | Malla de destino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Una lista de curvas |

### PlaneDisplay (PD)

PlaneDisplay

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `P` | Plane | árbol | Planos |

### Polyline Difference (Difference)

Diferencia de polilíneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve0 | `C0` | Curve | lista | Una lista de curvas a cortar |
| Curve1 | `C1` | Curve | lista | Una lista de curvas de corte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| C | `C` | Curve | lista | Una lista de curvas cortadas |

### Polyline Move (PolylineMove)

Mueve una curva cerrada en Z

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curvas |
| Distance *(opcional)* | `D` | Number | item | Distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Curve | item | Una lista de curvas cortadas |
| B | `B` | Curve | item | Una lista de curvas cortadas |

### Polyline Offset (Offset)

Offset de polilínea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curvas |
| Distance *(opcional)* | `D` | Number | item | Distancia |
| Divisions *(opcional)* | `T` | Number | item | Divisiones de las curvas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| C | `C` | Curve | lista | Una lista de curvas cortadas |
| H | `H` | Curve | lista | Una lista de curvas cortadas |

### PolylineCenter (PCenter)

Obtiene el centro, la normal y el plano de las polilíneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centers | `C` | Point | lista | Centros de los NGons |
| Normals | `N` | Vector | lista | Normal promedio en el centro del ngon |
| Planes | `P` | Plane | lista | Planos promedio en el centro del ngon |

### Simplify

Simplifica una polilínea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea |

### Text

Texto para corte láser o fresado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `L` | Plane | item | Ubicación y orientación del texto |
| Text | `T` | Text | item | Texto a mostrar |
| Size | `S` | Number | item | Tamaño del texto |
| Bold | `B` | Boolean | item | True para fuente en negrita |
| Horizontal alignment | `H` | Integer | item | 0=centro, 1=izquierda, 2=derecha |
| Vertical alignment | `V` | Integer | item | 0=centro, 1=arriba, 2=abajo, 3=línea base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Texto como curvas |

## Reciprocal

### MeshProp

MeshProp

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Offset *(opcional)* | `O` | Number | item | Offset de malla plana |
| Flip | `F` | Boolean | item | Invertir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh Properties | `Prop` | Generic Data | item | Propiedades de la malla como planos de caras y aristas e indexación |
| FacePlanes | `FPl` | Plane | árbol | Planos de las caras de los ngons |
| FaceEdgePlanes | `FEPL` | Plane | árbol | Planos de las caras de los ngons orientados según las aristas del ngon |
| EdgePlanes | `EPL` | Plane | árbol | Los planos de arista son el promedio de los FaceEdgePlanes adyacentes |
| Mesh | `M` | Mesh | item | Malla |

### ReciMove

Traslación de aristas que forma una nexorada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MeshProp | `Prop` | Generic Data | item | Propiedades de la malla |
| Dist | `Dist` | Number | lista | Distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | árbol | Línea |
| Ecc | `E` | Line | árbol | Excentricidades de las líneas |
| Nexors | `Nexors` | Generic Data | item | Nexors |
| MeshProp | `Prop` | Generic Data | item | Propiedades de la malla |
| LinesN | `LNaked` | Line | árbol | Línea |
| Plines | `Plines` | Curve | árbol | Polilíneas |
| Planes | `Planes` | Plane | árbol | Planos |

### ReciMoveVol

Agrega elementos volumétricos a la traslación recíproca

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Nexors0 | `Nexors0` | Generic Data | item | Nexors0 |
| MeshProp0 | `Prop0` | Generic Data | item | Propiedades de la malla 0 |
| Nexors1 *(opcional)* | `Nexors1` | Generic Data | item | Nexors1 |
| MeshProp1 *(opcional)* | `Prop1` | Generic Data | item | Propiedades de la malla 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Beams0 | `Beams0` | Curve | árbol | Vigas 0 |
| Panels0 | `Panels0` | Curve | árbol | Paneles 0 |
| RoundBeams0M | `RoundBeams0M` | Generic Data | árbol | RoundBeams0M |
| RoundBeams0C | `RoundBeams0C` | Curve | árbol | RoundBeams0C |
| RoundBeams0C | `RoundBeams0C` | Curve | árbol | RoundBeams0C |
| Beams1 | `Beams1` | Curve | árbol | Vigas 1 |
| Panels1 | `Panels1` | Curve | árbol | Paneles 1 |
| RoundBeams1M | `RoundBeams1M` | Generic Data | árbol | RoundBeams1M |
| RoundBeams1C | `RoundBeams1C` | Curve | árbol | RoundBeams1C |
| RoundBeams1C | `RoundBeams1C` | Curve | árbol | RoundBeams1C |
| Dowels0 | `Dowels0` | Line | árbol | Tarugos 0 |
| Dowels1 | `Dowels1` | Line | árbol | Tarugos 1 |

### RecipricalEdges

Rota la arista de la malla según la normal promedio

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Angle *(opcional)* | `A` | Number | item | Ángulo |
| Scale *(opcional)* | `S` | Number | item | Escala |
| NormalType | `T` | Boolean | item | 0 - la normal es la del plano promedio del ngon, 1 - normal de la cara triangular adyacente |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curva |
| ID0 | `I0` | Integer | lista | Primera línea para la colisión |
| ID1 | `I1` | Integer | lista | Segunda línea para la colisión |
| Vectors | `V` | Vector | lista | Vectores de rotación |

### RecipricalExtend

Rota la arista de la malla y la extiende hasta la siguiente línea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Angle *(opcional)* | `A` | Number | item | Ángulo |
| Scale *(opcional)* | `S` | Number | item | Escala |
| NormalType *(opcional)* | `T` | Boolean | item | 0 - la normal es la del plano promedio del ngon, 1 - normal de la cara triangular adyacente |
| Height | `H` | Number | item | Alto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `CM` | Curve | lista | Curva |
| Curve | `C0` | Curve | lista | Curva |
| Curve | `C1` | Curve | lista | Curva |
| Plane | `P` | Plane | lista | Plano |
| EndPlanes | `EP` | Plane | lista | Planos de los extremos |

### RecipricalThickness

Rota la arista de la malla según la normal promedio y le da espesor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Angle *(opcional)* | `A` | Number | item | Ángulo |
| Distance *(opcional)* | `D` | Number | item | Distancia |
| Width *(opcional)* | `W` | Number | item | Ancho |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | árbol | Polilíneas |

### RecipricalVolume

Elementos volumétricos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Malla |
| Angle *(opcional)* | `Angle` | Number | item | Ángulo |
| Scale *(opcional)* | `Scale` | Number | item | Escala |
| NormalType *(opcional)* | `NormalType` | Boolean | item | 0 - la normal es la del plano promedio del ngon, 1 - normal de la cara triangular adyacente |
| Height *(opcional)* | `Height` | Number | item | Alto |
| Offset *(opcional)* | `Offset` | Number | item | Offset entre capas |
| Thickness | `Thickness` | Number | item | Espesor del papel |
| RoofSurface | `RoofSurface` | Surface | item | RoofSurface |
| JointMale *(opcional)* | `JointMale` | Curve | lista | JointMale |
| JointFemale *(opcional)* | `JointFemale` | Curve | lista | JointFemale |
| W1 | `W1` | Number | item | W1 |
| W2 | `W2` | Number | item | W2 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `CM` | Curve | lista | Curva |
| Curve | `C0` | Curve | lista | Curva |
| Curve | `C1` | Curve | lista | Curva |
| Plane | `P` | Plane | lista | Plano |
| EndPlanes | `EP` | Plane | lista | Planos de los extremos |
| ID0 | `I0` | Integer | lista | Primera línea para la colisión |
| FacePlanes | `FP` | Curve | lista | Planos de las caras |
| CutLines | `CL` | Curve | lista | Líneas de corte de las caras |
| Structure | `Structure` | Curve | árbol | Líneas de corte de las caras |

### ReciRaw

ReciRaw

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MeshProp | `Prop` | Generic Data | item | Propiedades de la malla |
| Dist *(opcional)* | `Dist` | Number | lista | Distancia |
| Offset | `Offset` | Number | lista | Offset |
| Cut *(opcional)* | `Cut` | Plane | lista | Cortar |
| Extend *(opcional)* | `Extend` | Number | item | Extender |
| Box *(opcional)* | `Box` | Box | item | Caja |
| BoxT *(opcional)* | `BoxT` | Number | item | BoxT |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | árbol | Línea |
| Ecc | `Ecc` | Line | árbol | Excentricidades de las líneas |
| LinesN | `LNaked` | Line | árbol | Línea |
| Plines | `Plines` | Curve | árbol | Polilíneas |
| Profiles | `Profiles` | Curve | árbol | Perfiles |
| Membrane | `Membrane` | Curve | árbol | Membrana |
| Planes | `Planes` | Plane | árbol | Planos |
| VerticalLines | `VerticalLines` | Line | árbol | Líneas verticales |

## Subdivide

### Chebyshev

Redes de Chebyshev https://github.com/pearswj/buckminster

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface *(opcional)* | `S` | Surface | item | Superficie de entrada |
| Point *(opcional)* | `P` | Point | item | Punto inicial (opcional: si no se entrega, se elige un punto al medio del espacio de parámetros). |
| Length | `L` | Number | item | Longitud de las aristas de la malla |
| Rotation | `R` | Number | item | Ángulo de rotación de la grilla (en grados) |
| Steps | `B` | Integer | item | Cantidad máxima de pasos a recorrer desde el punto inicial |
| Extend | `E` | Boolean | item | Extiende la superficie más allá de sus bordes originales |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de cuadriláteros (red de Chebyshev) |
| Points | `A` | Point | árbol | Puntos de dirección |

### DiamondDivide

Divide una superficie NURBS en formas de diamante

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie a dividir |
| U *(opcional)* | `U` | Number | item | División en la primera dirección |
| V *(opcional)* | `V` | Integer | item | División en la segunda dirección |
| Boundary *(opcional)* | `B` | Integer | item | Ngons de borde |
| Swap *(opcional)* | `S` | Boolean | item | Intercambia la dirección de la superficie de UV a VU (Transpose de RhinoCommon) |
| Flip *(opcional)* | `F` | Boolean | item | Invierte la triangulación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### HexDivide

Divide una superficie NURBS en hexágonos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie a dividir |
| U *(opcional)* | `U` | Number | item | División en la primera dirección |
| V *(opcional)* | `V` | Integer | item | División en la segunda dirección |
| Parameter *(opcional)* | `T` | Number | item | Escala del hexágono |
| Boundary *(opcional)* | `B` | Integer | item | Ngons de borde |
| Swap *(opcional)* | `S` | Boolean | item | Intercambia la dirección de la superficie de UV a VU (Transpose de RhinoCommon) |
| Rebuild *(opcional)* | `R` | Integer | item | Reconstruir la superficie |
| Quadrangulate *(opcional)* | `Q` | Boolean | item | Divide los hexágonos en dos cuadriláteros |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| DistA | `A` | Number | lista | Longitud vertical |
| DistB | `B` | Number | lista | Longitud horizontal |

### Platonic

Obtiene un objeto platónico, por ejemplo icosaedro, toro, cubo o tetraedro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| I *(opcional)* | `I` | Integer | item | Id del objeto: 0 - icosaedro, 1 - toro, 2 - cubo, 3 - tetraedro |
| R *(opcional)* | `R` | Number | lista | Radio |
| P *(opcional)* | `P` | Plane | item | Plano |
| S *(opcional)* | `S` | Integer | lista | Nivel de subdivisión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### QuadDivide

Divide una NurbsSurface en cuadriláteros

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie a dividir |
| U *(opcional)* | `U` | Number | item | División en la primera dirección |
| V *(opcional)* | `V` | Integer | item | División en la segunda dirección |
| Rebuild *(opcional)* | `R` | Integer | item | Reconstruir la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### SortBrep

Ordena las caras del Brep si es posible

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep orientado si es posible |

### TriangleSubdivision (Tesselate)

Teselar

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| N | `N` | Integer | item | Cantidad de subdivisiones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

## Transform

### AdjustMeshVertices (MatchMesh)

Toma los vértices de una malla y ajusta los vértices de otra malla según las posiciones de la primera

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MeshA | `MA` | Mesh | item | Malla a ajustar |
| MeshB | `MB` | Mesh | item | Malla a seguir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MeshA | `MA` | Mesh | item | Malla a ajustar |

### Corners

Esquinas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Angle *(opcional)* | `A` | Number | item | Ángulo en grados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corners | `C` | Point | lista | Vértices cuyos dos vecinos están conectados a más de un ngon |
| ID | `I` | Integer | lista | Id del vértice de la malla |

### CutMesh

CutMesh

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | Malla |
| P *(opcional)* | `P` | Plane | lista | Plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P | `P` | Curve | lista | Polilíneas |

### Dual

Dual

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Type *(opcional)* | `T` | Integer | item | Tipo |
| P *(opcional)* | `P` | Point | lista | Puntos personalizados en vez del centro; la cantidad de puntos debe ser igual a la cantidad de caras o ngons |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Extrude Edges

Extruye las aristas de los NGons según las normales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a extruir |
| Dist *(opcional)* | `D` | Number | item | Distancia de extrusión |
| Cap *(opcional)* | `C` | Boolean | item | Tapar los agujeros |
| Merge *(opcional)* | `M` | Boolean | item | Extruye todas las aristas en vez de ngons individuales |
| BothSides *(opcional)* | `B` | Boolean | item | Extruir hacia ambos lados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla a extruir |

### Flip

Invertir

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla con los ngons invertidos |
| Mesh | `M` | Mesh | item | Malla con las normales invertidas |

### JointsVDA · 2

JointsVDA

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Malla necesaria para la topología |
| Panels | `Panels` | Curve | árbol | Contornos de los paneles como polilíneas |
| EdgeVectors *(opcional)* | `EdgeVectors` | Vector | árbol | Se usan los EdgeVectors como dirección de la unión |
| JointDiv *(opcional)* | `JointDiv` | Integer | item | Cantidad de uniones en cada arista |
| JointLen *(opcional)* | `JointLen` | Number | item | Si el número es negativo, la arista se escala; si es positivo, se usa la longitud exacta |
| JointHei *(opcional)* | `JointHei` | Number | item | Altura de la unión |
| JointThi *(opcional)* | `JointThi` | Number | item | El espesor de la unión debe ser igual al parámetro W del offset de la malla |
| Center *(opcional)* | `Center` | Boolean | item | Orientar la unión hacia el centro |
| Finger *(opcional)* | `Finger` | Boolean | item | Crea una unión de dedos (finger joint) |
| Custom *(opcional)* | `Custom` | Number | item | Crea media unión si existen dos capas |
| PanelsChamfer *(opcional)* | `PanelsChamfer` | Curve | árbol | Polilíneas adicionales por si el offset no funciona bien |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Curve | árbol | Polilíneas de los paneles |
| Joints | `Joints` | Curve | árbol | Polilíneas de las uniones |

### LatticeFromTwoMeshes (MatchMesh)

Toma los vértices de una malla y ajusta los vértices de otra malla según las posiciones de la primera

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MeshA | `MA` | Mesh | item | Malla a ajustar |
| MeshB | `MB` | Mesh | item | Malla a seguir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lattice | `La` | Mesh | item | Malla de retícula (lattice) |
| Joined | `JM` | Mesh | item | Malla unida |

### Loft Polylines (Loft)

Hace loft de dos polilíneas; deben tener la misma cantidad de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | lista | Polilíneas para el loft: árbol de datos con dos polilíneas |
| Polylines *(opcional)* | `P` | Curve | lista | Polilíneas para el loft: árbol de datos con dos polilíneas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Loft Polylines (Loft) · 2

Hace loft de dos polilíneas; deben tener la misma cantidad de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve0 | `C0` | Curve | árbol | Curva para el loft: árbol de datos con dos polilíneas |
| Curve1 *(opcional)* | `C1` | Curve | árbol | Curva para el loft: árbol de datos con dos polilíneas |
| Fast | `F` | Boolean | item | Rápido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | árbol | Malla |

### NGonFrame

NGonFrame

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| Dist | `D` | Number | item | Distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | árbol | Polilíneas |
| Polylines | `P` | Curve | lista | Polilíneas |
| Polylines | `P` | Curve | lista | Polilíneas |

### Offset Projected

Aplica offset a una malla usando el offset de malla o intersecciones con planos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar offset |
| Offset *(opcional)* | `O` | Number | item | Distancia de offset |
| Type | `T` | Integer | item | Tipo de offset: 0 - intersección de planos, 1 - offset de malla y proyección |
| Dist2 | `W` | Number | item | El espesor de placa solo funciona con el tipo 0 |
| Tol | `T` | Number | item | Tolerancia angular |
| Custom *(opcional)* | `C` | Integer | lista | Personalizado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla a la que aplicar offset |
| ProjectedPolylines | `C` | Curve | árbol | Malla a la que aplicar offset |
| Thickness | `C` | Curve | árbol | Malla a la que aplicar offset |
| EdgePlanes | `P` | Plane | árbol | Malla a la que aplicar offset |

### OffsetMesh

Malla con offset

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar offset |
| Dist *(opcional)* | `D` | Number | item | Distancia de offset |
| Solid | `S` | Boolean | item | Sólido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar offset |

### OffsetPlanar

Offset de malla plana. Planar Offset funciona solo con mallas cerradas de valencia 3; para valencia n > 3 es un componente experimental

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar offset |
| Dist *(opcional)* | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | árbol | Contornos |

### OffsetTriangleMesh

Malla OffsetTriangleMesh

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar offset |
| Dist *(opcional)* | `D` | Number | item | Distancia de offset |
| Chamfer *(opcional)* | `C` | Number | item | Distancia de chaflán |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P0` | Curve | lista | Contornos |
| Polylines | `P1` | Curve | lista | Contornos |
| Planes | `S` | Plane | lista | Planos de las aristas |
| Planes | `P` | Plane | lista | Planos P0 |

### Simplify · 2

Quita los puntos con valencia menor que 3 o fijos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Fixed *(opcional)* | `P` | Point | lista | Puntos fijos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Split3

Divide los ngons en 3 polilíneas si su cantidad de puntos es mayor que la definida; primero se dividen los polígonos de mayor longitud

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Size *(opcional)* | `S` | Integer | item | Tamaño máximo |
| Iteration *(opcional)* | `I` | Integer | item | Iteraciones máximas |
| Smooth *(opcional)* | `S` | Integer | item | Iteraciones de suavizado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plines | `P` | Curve | lista | Polilíneas |

### Stellate

Crea pirámides y las corta con un plano

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | Malla |
| D | `D` | Number | lista | Altura de la pirámide |
| T | `T` | Number | lista | Plano en el dominio de la línea vertical de la pirámide |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| S | `S` | Curve | árbol | Lados |
| C | `C` | Curve | árbol | Centros |

### UnifyWindings (Unify)

UnifyWindings

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

## Utilities Mesh

### BoundaryFirstFlatenning

BoundaryFirstFlatenning

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Generic Data | item | Malla |
| Path *(opcional)* | `P` | Text | item | Ruta de la carpeta de ngon; solo hace falta si el componente da un mensaje de error |
| MapToSphere | `S` | Boolean | item | Mapear a esfera = True |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh3D | `M3D` | Generic Data | item | Malla 3D |
| Mesh2D | `M2D` | Generic Data | item | Malla 2D |

### BrepEdges

Obtiene las aristas del BRep que no pertenecen a la misma superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | árbol | Brep |
| Weight *(opcional)* | `W` | Integer | item | Grosor de la curva |
| Color *(opcional)* | `C` | Colour | item | Color |
| RefShTra *(opcional)* | `P` | Number | lista | Parámetros del material como lista: reflexión - brillo - transparencia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | árbol | Curvas |

### ColorMesh

ColorMesh

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Generic Data | item | Malla |
| Color *(opcional)* | `C` | Colour | lista | Cambia los colores de la malla asignando colores a los vértices |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Generic Data | item | Malla |

### DiagonalMesh (Diagonal)

DiagonalMesh

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### DivideBox

DivideBox

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box *(opcional)* | `B` | Box | item | Caja |
| X *(opcional)* | `X` | Integer | item | X |
| Y *(opcional)* | `Y` | Integer | item | Y |
| Z *(opcional)* | `Z` | Integer | item | Z |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P | `P` | Point | lista | P |

### ExplodeMesh

Explota la malla y asigna el color promedio a cada vértice de una cara

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Generic Data | item | Malla |
| Explode *(opcional)* | `E` | Boolean | item | Explota la malla por caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Generic Data | lista | Malla |

### FacesInCurves

FacesInCurves

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Curves *(opcional)* | `C` | Curve | lista | Curvas que influyen en la triangulación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### IsoSurface

Isosuperficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja |
| Values | `V` | Number | lista | Valores |
| X resolution | `X` | Integer | item | Resolución en X |
| Y resolution | `Y` | Integer | item | Resolución en Y |
| Z resolution | `Z` | Integer | item | Resolución en Z |
| IsoValue | `I` | Number | item | Isovalor |
| Merge Vertices | `M` | Boolean | item | Fusionar vértices |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### LoftCircles

LoftCircles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep |
| Radii | `R` | Number | lista | Radios de los círculos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circles | `C` | Curve | lista | Círculos |
| Loft | `B` | Brep | item | Círculos con loft |

### Mesh Curvature

Curvatura de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `Mesh` | Mesh | item | Malla |
| CurvatureType | `CurvatureType` | Integer | item | 0 = mínima, 1 = máxima, 2 = gaussiana, 3 = media, 4 = absoluta, 5 = diferencia, 6 = RMS |
| Radius | `Radius` | Number | item | Radio |
| Method | `Method` | Integer | item | 0 = ajuste cuadrático con 3 coeficientes, 1 = ajuste cuadrático con 4 coeficientes, 2 = ajuste cuadrático con 6 coeficientes, 3 = ajuste cúbico con 7 coeficientes |
| Interval *(opcional)* | `Interval` | Domain | item | Intervalo |
| 3Colors *(opcional)* | `3Colors` | Colour | lista | 3 colores |
| On *(opcional)* | `On` | Boolean | item | Activado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Curvature Values | `V` | Number | lista | Valores de curvatura |

### MeshCP

Si el punto está cerca de una malla o dentro de ella

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos |
| Mesh | `M` | Mesh | item | Malla en la que buscar un punto cercano |
| Tol *(opcional)* | `T` | Number | item | Distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos |
| ID | `I` | Integer | lista | Índices de los puntos más cercanos |

### MeshCurve (MeshCrv)

Si las curvas están dentro de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curva |
| Mesh | `M` | Mesh | item | Malla en la que buscar un punto cercano |
| Flag *(opcional)* | `F` | Boolean | item | Si es True, usa el centro; si es False, revisa la inclusión de los puntos de las esquinas |
| Tol *(opcional)* | `T` | Number | item | Distancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curva |
| ID | `I` | Integer | lista | Índices de los puntos más cercanos |

### MeshPipe

Crea una tubería de malla a partir de curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve *(opcional)* | `C` | Curve | item | Curva |
| Radius | `R` | Number | item | Radio de la tubería |
| Sides | `S` | Integer | item | Cantidad de lados |
| Tolerance | `T` | Integer | item | Tolerancia |
| Ending | `E` | Integer | item | 0-ninguno, 1-caja, 2-cúpula, 3-plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla |

### Morph

Deformar (morph)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Pt` | Point | lista | Puntos |
| Polylines *(opcional)* | `Plines` | Curve | lista | Polilíneas |
| SquarePair0 | `SP0` | Curve | lista | SP0 |
| SquarePair1 | `SP1` | Curve | lista | SP1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `Pt` | Point | lista | Puntos |
| Polylines | `Plines` | Curve | lista | Polilíneas |

### PreviewEdges

Busca las aristas que están dentro de cierto ángulo respecto de las normales de las caras adyacentes de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla |
| tolerance | `t` | Number | item | Tolerancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | lista | Líneas |

### ProjectNakedEdgeToCurves (ProjectNaked)

Proyecta la arista desnuda sobre las curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Curves *(opcional)* | `C` | Curve | lista | Curvas |
| Iteration *(opcional)* | `I` | Integer | item | Iteraciones máximas |
| Tolerance *(opcional)* | `T` | Number | item | Distancia máxima a la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Remesh

Remallar

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | lista | Malla |
| FixEdges *(opcional)* | `FixEdges` | Boolean | item | FixEdges |
| EdgeLength *(opcional)* | `EdgeLength` | Number | item | Longitud de arista |
| Iterations *(opcional)* | `Iterations` | Integer | item | Iteraciones |
| FixPt *(opcional)* | `FixPt` | Point | lista | FixPt |
| Project *(opcional)* | `Project` | Boolean | item | Proyectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Smooth

Smooth

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Value *(opcional)* | `V` | Number | item | Valor de suavizado |
| Iterations *(opcional)* | `I` | Integer | item | Cantidad de iteraciones de suavizado |
| Fixed *(opcional)* | `F` | Boolean | item | Bordes fijos |
| FixedPt, *(opcional)* | `P` | Point | lista | Puntos fijos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Tri-Periodic Surfaces

Superficies triplemente periódicas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `P` | Point | lista | Puntos |
| Type *(opcional)* | `N` | Integer | item | 0 = HybridPW, 1 = Diamond, 2 = Neovius, 3 = IWP, 4 = HybridPW |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `V` | Number | lista | Valor de las fórmulas matemáticas |

### Triangulate

Triangula según curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Curves *(opcional)* | `C` | Curve | lista | Curvas que influyen en la triangulación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Voxels

Malla de vóxeles a partir de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `Pt` | Point | lista | Puntos |
| Scale *(opcional)* | `S` | Number | item | S |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Points | `Pt` | Point | lista | Puntos |

### WeldMesh (Weld)

Descripción

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Generic Data | lista | Malla a soldar |
| Radius | `R` | Number | item | Radio de soldadura |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Generic Data | lista | Malla a soldar |
