---
tags: [tipo/mapa, geometria/mallas, geometria/subd, software/grasshopper, software/rhinocommon, fabricacion/impresion-3d]
---

# Mallas y SubD

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Mallas (vértices + caras) para análisis, visualización, impresión 3D (STL) y form-finding; SubD para modelado orgánico. Es el mapa más grande porque varios plugins trabajan con mallas: Weaverbird (subdivisión), NGon (caras poligonales), Kangaroo (simulación) y Pufferfish.

## Teoría y código
- [[wiki/concepts/rhinocommon-mesh-api]]: construcción, CreateFromBrep, Display Conduit, bordes desnudos
- [[wiki/sources/2026-05-04-rhinopy-mallas]] · [[wiki/concepts/tipos-geometria-rhinocommon]]
- Impresión 3D: Ender 3 V3 KE · [[Mapa - Fabricación]]

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Malla desde Brep | [[Catálogo - Mesh#Mesh Brep (Mesh)\|Mesh Brep]] | `rg.Mesh.CreateFromBrep(brep, rg.MeshingParameters.Default)` | `forma.tessellate(tol)` |
| Construir a mano | [[Catálogo - Mesh#Construct Mesh (ConMesh)\|Construct Mesh]] | `m = rg.Mesh(); m.Vertices.Add(x, y, z); m.Faces.AddFace(0, 1, 2)` | — |
| Unir | [[Catálogo - Mesh#Mesh Join (MJoin)\|Mesh Join]] | `m.Append(otra)` | — |
| Soldar | [[Catálogo - Mesh#Weld Mesh (Weld)\|Weld Mesh]] | `m.Weld(math.radians(22.5))` | — |
| Normales de caras | [[Catálogo - Mesh#Face Normals (FaceN)\|Face Normals]] | `m.FaceNormals.ComputeFaceNormals()` | — |
| Bordes abiertos | [[Catálogo - Mesh#Mesh Edges (MEdges)\|Mesh Edges]] | `m.GetNakedEdges()` | — |
| SubD desde malla | [[Catálogo - Surface#SubD from Mesh (SubDMesh)\|SubD from Mesh]] | `rg.SubD.CreateFromMesh(m)` | — |
| Exportar STL | — | — | `cq.exporters.export(pieza, "pieza.stl")` |

## Para empezar
[[Catálogo - Mesh#Mesh Brep (Mesh)|Mesh Brep]] · [[Catálogo - Mesh#Deconstruct Mesh (DeMesh)|Deconstruct Mesh]] · [[Catálogo - Mesh#Weld Mesh (Weld)|Weld Mesh]] · [[Catálogo - Mesh#Quad Remesh (QRMesh)|Quad Remesh]] · [[Catálogo - Mesh#Voronoi|Voronoi]] · [[Catálogo - Mesh#Delaunay Mesh (Del)|Delaunay Mesh]] · [[Catálogo - Wb#Weaverbird's Catmull-Clark Subdivision (wbCatmullClark)|Catmull-Clark (Weaverbird)]] · [[Catálogo - Wb#Weaverbird's Mesh Thicken (wbThicken)|Mesh Thicken (Weaverbird)]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (11)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Mesh | [[Add Mesh\|Py]] · [[Add Mesh (cs)\|C#]] | Crea una malla desde vértices y caras | `Mesh.Vertices.Add, Mesh.Faces.AddFace, Normals.ComputeNormals` |
| Add Mesh Box | [[Add Mesh Box (cs)\|C#]] | Crea una malla en forma de caja | `Mesh.CreateFromBox(caja, 2, 2, 2)` |
| Closest Point Calculation with RTree | [[Closest Point Calculation with RTree\|Py]] · [[Closest Point Calculation with RTree (cs)\|C#]] | Vértice más cercano de una malla con un RTree (búsqueda rápida) | `RTree.Insert, RTree.Search(esfera, callback)` |
| Conduit Draw Shaded Mesh | [[Conduit Draw Shaded Mesh (cs)\|C#]] | Dibuja una malla sombreada con un display conduit, sin agregarla al documento | `DisplayConduit.PostDrawObjects → DrawMeshShaded` |
| Create Mesh from Brep | [[Create Mesh from Brep\|Py]] · [[Create Mesh from Brep (cs)\|C#]] | Convierte un Brep en malla con parámetros de mallado | `Mesh.CreateFromBrep(brep, MeshingParameters.Smooth)` |
| Draw Mesh | [[Draw Mesh\|Py]] · [[Draw Mesh (cs)\|C#]] | Malla desde una esfera, dibujada en azul con un conduit | `Mesh.CreateFromSphere → DisplayConduit (DrawMeshShaded)` |
| Duplicate Mesh Boundary | [[Duplicate Mesh Boundary\|Py]] · [[Duplicate Mesh Boundary (cs)\|C#]] | Borde abierto de una malla como polilíneas | `Mesh.GetNakedEdges()` |
| Extract Render Mesh | [[Extract Render Mesh (cs)\|C#]] | Saca la malla de render de un Brep | `RhinoObject.GetRenderMeshes(objetos, ...)` |
| Mesh Volume | [[Mesh Volume\|Py]] · [[Mesh Volume (cs)\|C#]] | Volumen de mallas cerradas (material de una impresión 3D) | `VolumeMassProperties.Compute(malla).Volume` |
| Project Points to Mesh | [[Project Points to Mesh\|Py]] · [[Project Points to Mesh (cs)\|C#]] | Proyecta puntos sobre una malla | `Intersection.ProjectPointsToMeshesEx` |
| Unroll Surface and Mesh | [[Unroll Surface and Mesh\|Py]] · [[Unroll Surface and Mesh (cs)\|C#]] | Desarrolla una superficie y lleva su malla al plano | `Unroller.AddFollowingGeometry(puntos) → PerformUnroll` |

## Componentes de Grasshopper (307)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (3)

- [[Catálogo - Params#Mesh (parámetro)|Mesh (parámetro)]] — Contiene una colección de mallas poligonales
- [[Catálogo - Params#Mesh Face (Face, parámetro)|Mesh Face (Face, parámetro)]] — Contiene una colección de caras de malla triangulares o cuadrangulares
- [[Catálogo - Params#SubD (parámetro)|SubD (parámetro)]] — Contiene una colección de SubDs

### Surface › SubD (10)

- [[Catálogo - Surface#Mesh from SubD (MeshSubD)|Mesh from SubD (MeshSubD)]] — Obtiene la malla de aproximación de una SubD
- [[Catálogo - Surface#MultiPipe (MP)|MultiPipe (MP)]] — Crea una tubería ramificada alrededor de una red de líneas/curvas
- [[Catálogo - Surface#SubD Control Polygon (SubDPoly)|SubD Control Polygon (SubDPoly)]] — Extrae el polígono de control de una SubD
- [[Catálogo - Surface#SubD Edge Tags (SubDTags)|SubD Edge Tags (SubDTags)]] — Define las etiquetas de arista de una forma SubD
- [[Catálogo - Surface#SubD Edges (SubDEdges)|SubD Edges (SubDEdges)]] — Extrae todos los datos de aristas de una SubD
- [[Catálogo - Surface#SubD from Mesh (SubDMesh)|SubD from Mesh (SubDMesh)]] — Crea una SubD a partir de una malla de control
- [[Catálogo - Surface#SubD Fuse (Fuse)|SubD Fuse (Fuse)]] — Combina 2 objetos SubD
- [[Catálogo - Surface#SubD To Brep (ToBrep)|SubD To Brep (ToBrep)]] — Convierte una superficie de subdivisión en una polisuperficie equivalente formada por caras NURBS
- [[Catálogo - Surface#SubD Vertex Tags (SubDVTags)|SubD Vertex Tags (SubDVTags)]] — Define las etiquetas de vértice de una forma SubD
- [[Catálogo - Surface#SubD Vertices (SubDVerts)|SubD Vertices (SubDVerts)]] — Extrae todos los datos de vértices de una SubD

### Mesh › Analysis (9)

- [[Catálogo - Mesh#Deconstruct Face (DeFace)|Deconstruct Face (DeFace)]] — Descompone una cara de malla en sus cuatro índices de esquina
- [[Catálogo - Mesh#Deconstruct Mesh (DeMesh)|Deconstruct Mesh (DeMesh)]] — Descompone una malla en sus partes
- [[Catálogo - Mesh#Face Boundaries (FaceB)|Face Boundaries (FaceB)]] — Convierte todas las caras de la malla en polilíneas
- [[Catálogo - Mesh#Face Circles (FaceC)|Face Circles (FaceC)]] — Calcula los círculos circunscritos de todas las caras de la malla
- [[Catálogo - Mesh#Face Normals (FaceN)|Face Normals (FaceN)]] — Extrae las normales y los puntos centrales de todas las caras de una malla
- [[Catálogo - Mesh#Mesh Closest Point (MeshCP)|Mesh Closest Point (MeshCP)]] — Busca el punto más cercano en una malla
- [[Catálogo - Mesh#Mesh Edges (MEdges)|Mesh Edges (MEdges)]] — Obtiene todas las aristas de una malla
- [[Catálogo - Mesh#Mesh Eval (MEval)|Mesh Eval (MEval)]] — Evalúa una malla en un parámetro dado
- [[Catálogo - Mesh#Mesh Inclusion (MInc)|Mesh Inclusion (MInc)]] — Prueba si un punto está contenido en una malla

### Mesh › Primitive (9)

- [[Catálogo - Mesh#Construct Mesh (ConMesh)|Construct Mesh (ConMesh)]] — Construye una malla a partir de vértices, caras y colores opcionales
- [[Catálogo - Mesh#Mesh Box (MBox)|Mesh Box (MBox)]] — Crea una caja de malla
- [[Catálogo - Mesh#Mesh Colours (MCol)|Mesh Colours (MCol)]] — Asigna un patrón de color repetitivo a un objeto malla
- [[Catálogo - Mesh#Mesh Plane (MPlane)|Mesh Plane (MPlane)]] — Crea un plano de malla
- [[Catálogo - Mesh#Mesh Quad (Quad)|Mesh Quad (Quad)]] — Crea un cuadrilátero de malla
- [[Catálogo - Mesh#Mesh Sphere (MSphere)|Mesh Sphere (MSphere)]] — Crea una esfera de malla
- [[Catálogo - Mesh#Mesh Sphere Ex (MSphereEx)|Mesh Sphere Ex (MSphereEx)]] — Crea una esfera de malla a partir de parches cuadrados
- [[Catálogo - Mesh#Mesh Spray (MSpray)|Mesh Spray (MSpray)]] — Asigna colores a una malla según puntos de rociado
- [[Catálogo - Mesh#Mesh Triangle (Triangle)|Mesh Triangle (Triangle)]] — Crea un triángulo de malla

### Mesh › Triangulation (21)

- [[Catálogo - Mesh#Convex Hull (Hull2D)|Convex Hull (Hull2D)]] — Calcula la envolvente convexa plana de una colección de puntos
- [[Catálogo - Mesh#Convex Hull 3D (Hull3D)|Convex Hull 3D (Hull3D)]] — Calcula la envolvente convexa no plana (3D) de una colección de puntos
- [[Catálogo - Mesh#Delaunay Edges (Con)|Delaunay Edges (Con)]] — Conectividad de Delaunay
- [[Catálogo - Mesh#Delaunay Mesh (Del)|Delaunay Mesh (Del)]] — Triangulación de Delaunay
- [[Catálogo - Mesh#Facet Dome (Facet)|Facet Dome (Facet)]] — Crea una cúpula facetada
- [[Catálogo - Mesh#MetaBall|MetaBall]] — Isocurva metaball 2D que pasa por un punto
- [[Catálogo - Mesh#MetaBall(t)|MetaBall(t)]] — Isosuperficie metaball 2D por umbral
- [[Catálogo - Mesh#MetaBall(t) Custom (MetaBall(t))|MetaBall(t) Custom (MetaBall(t))]] — Isosuperficie metaball 2D por umbral y valores de carga personalizados
- [[Catálogo - Mesh#OcTree (OcT)|OcTree (OcT)]] — Una estructura oc-tree tridimensional
- [[Catálogo - Mesh#Proximity 2D (Prox)|Proximity 2D (Prox)]] — Busca proximidad bidimensional dentro de una lista de puntos
- [[Catálogo - Mesh#Proximity 3D (Prox)|Proximity 3D (Prox)]] — Busca proximidad tridimensional dentro de una lista de puntos
- [[Catálogo - Mesh#Quad Remesh (QRMesh)|Quad Remesh (QRMesh)]] — Rehace la malla de una forma con cuadriláteros (quad remesh)
- [[Catálogo - Mesh#Quad Remesh Settings (QRSettings)|Quad Remesh Settings (QRSettings)]] — Crea ajustes para el remallado con cuadriláteros
- [[Catálogo - Mesh#QuadTree (QT)|QuadTree (QT)]] — Una estructura quadtree bidimensional
- [[Catálogo - Mesh#ShrinkWrap (Wrap)|ShrinkWrap (Wrap)]] — Envuelve (ShrinkWrap) una malla o una nube de puntos
- [[Catálogo - Mesh#Substrate|Substrate]] — Algoritmo Substrate inspirado en Jared Tarbell (Complexification.net)
- [[Catálogo - Mesh#TriRemesh|TriRemesh]] — Convierte un Brep o una malla en una malla de triángulos casi equiláteros
- [[Catálogo - Mesh#Voronoi|Voronoi]] — Diagrama de Voronoi plano de una colección de puntos
- [[Catálogo - Mesh#Voronoi 3D (Voronoi³)|Voronoi 3D (Voronoi³)]] — Diagrama de Voronoi volumétrico de una colección de puntos
- [[Catálogo - Mesh#Voronoi Cell (VCell)|Voronoi Cell (VCell)]] — Calcula una sola celda de Voronoi 3D
- [[Catálogo - Mesh#Voronoi Groups (VorGroup)|Voronoi Groups (VorGroup)]] — Calcula un conjunto personalizado de diagramas de Voronoi anidados

### Mesh › Util (25)

- [[Catálogo - Mesh#Align Vertices (AlignVert)|Align Vertices (AlignVert)]] — Alinea los vértices cercanos de una malla
- [[Catálogo - Mesh#Blur Mesh (MBlur)|Blur Mesh (MBlur)]] — Difumina los colores de una malla
- [[Catálogo - Mesh#Cull Faces (CullF)|Cull Faces (CullF)]] — Elimina (cull) caras de una malla
- [[Catálogo - Mesh#Cull Vertices (CullV)|Cull Vertices (CullV)]] — Elimina (cull) vértices de una malla
- [[Catálogo - Mesh#Delete Faces (DeleteF)|Delete Faces (DeleteF)]] — Borra caras de una malla
- [[Catálogo - Mesh#Delete Vertices (DeleteV)|Delete Vertices (DeleteV)]] — Borra vértices de una malla
- [[Catálogo - Mesh#Disjoint Mesh (Disjoint)|Disjoint Mesh (Disjoint)]] — Separa una malla en piezas desconectadas
- [[Catálogo - Mesh#Exposure|Exposure]] — Calcula la exposición de una malla a una colección de rayos de energía y obstáculos
- [[Catálogo - Mesh#Flip Mesh (FlipM)|Flip Mesh (FlipM)]] — Invierte los vectores normales de una malla
- [[Catálogo - Mesh#Mesh Brep (Mesh)|Mesh Brep (Mesh)]] — Crea una malla que aproxima la geometría de un Brep
- [[Catálogo - Mesh#Mesh Join (MJoin)|Mesh Join (MJoin)]] — Une un conjunto de mallas en una sola malla
- [[Catálogo - Mesh#Mesh Shadow (MShadow)|Mesh Shadow (MShadow)]] — Calcula el contorno de la sombra de un objeto malla
- [[Catálogo - Mesh#Mesh Split Plane (MSplit)|Mesh Split Plane (MSplit)]] — Divide una malla con un plano infinito
- [[Catálogo - Mesh#Mesh Surface (Mesh UV)|Mesh Surface (Mesh UV)]] — Crea una malla UV de superficie
- [[Catálogo - Mesh#Occlusion (Occ)|Occlusion (Occ)]] — Calcula la oclusión para una colección de rayos de visión y obstáculos
- [[Catálogo - Mesh#Quadrangulate (Quad)|Quadrangulate (Quad)]] — Convierte en cuadriláteros la mayor cantidad posible de triángulos de una malla
- [[Catálogo - Mesh#Settings (Custom) (Custom Mesh Settings)|Settings (Custom) (Custom Mesh Settings)]] — Representa ajustes de malla personalizados
- [[Catálogo - Mesh#Settings (Quality) (Smooth)|Settings (Quality) (Smooth)]] — Representa los ajustes de malla "suave y más lenta"
- [[Catálogo - Mesh#Settings (Speed) (Jagged)|Settings (Speed) (Jagged)]] — Representa los ajustes de malla "irregular y más rápida"
- [[Catálogo - Mesh#Simple Mesh (SMesh)|Simple Mesh (SMesh)]] — Crea una malla que representa un Brep de la forma más simple posible
- [[Catálogo - Mesh#Smooth Mesh (MSmooth)|Smooth Mesh (MSmooth)]] — Suaviza los vértices de una malla
- [[Catálogo - Mesh#Triangulate (Tri)|Triangulate (Tri)]] — Triangula todos los cuadriláteros de una malla
- [[Catálogo - Mesh#Unify Mesh (UniM)|Unify Mesh (UniM)]] — Unifica las normales de una malla
- [[Catálogo - Mesh#Unweld Mesh (Unweld)|Unweld Mesh (Unweld)]] — Separa (desuelda) los pliegues de una malla
- [[Catálogo - Mesh#Weld Mesh (Weld)|Weld Mesh (Weld)]] — Suelda (fusiona) los pliegues de una malla

### Kangaroo2 › Mesh (22)

- [[Catálogo - Kangaroo2#Bipartite|Bipartite]] — Intenta asignar un booleano a cada vértice de una malla de modo que ningún par de vértices conectados tenga…
- [[Catálogo - Kangaroo2#ByParent|ByParent]] — Refina una malla, separando las salidas por cara de origen
- [[Catálogo - Kangaroo2#Checkerboard|Checkerboard]] — Intenta asignar un booleano a cada cara de una malla de modo que ningún par de caras adyacentes tenga el…
- [[Catálogo - Kangaroo2#Combine&Clean (Clean)|Combine&Clean (Clean)]] — Combina y limpia una lista de mallas, quitando vértices no usados y duplicados
- [[Catálogo - Kangaroo2#Diagonalize (Diag)|Diagonalize (Diag)]] — Reemplaza cada arista por una cara nueva
- [[Catálogo - Kangaroo2#FaceFaceOffset (FaceFace)|FaceFaceOffset (FaceFace)]] — Aplica offset a una malla cónica de modo que las caras correspondientes queden a distancia constante
- [[Catálogo - Kangaroo2#FoldAngle|FoldAngle]] — Mide el ángulo actual entre dos triángulos alrededor de su arista común
- [[Catálogo - Kangaroo2#HingePoints|HingePoints]] — Obtiene los 4 puntos de cada arista interior para usar en una fuerza Hinge
- [[Catálogo - Kangaroo2#MeshCorners (MC)|MeshCorners (MC)]] — Extrae las esquinas más agudas que cierto ángulo
- [[Catálogo - Kangaroo2#MeshDirection (MD)|MeshDirection (MD)]] — Ordena las direcciones de las caras de una malla
- [[Catálogo - Kangaroo2#MeshMap|MeshMap]] — Mapea puntos de una malla a otra
- [[Catálogo - Kangaroo2#MeshTurn (Turn)|MeshTurn (Turn)]] — Rota el orden de los vértices de cada cara
- [[Catálogo - Kangaroo2#NakedVertices (NV)|NakedVertices (NV)]] — Ordena los vértices de una malla en 2 listas según estén o no rodeados por caras
- [[Catálogo - Kangaroo2#PlanarityAnalysis (PA)|PlanarityAnalysis (PA)]] — Muestra la planaridad de las caras como una malla coloreada
- [[Catálogo - Kangaroo2#Refine|Refine]] — Divide cada cuadrilátero en 4 cuadriláteros y cada triángulo en 4 triángulos
- [[Catálogo - Kangaroo2#RefineStrips (Strips)|RefineStrips (Strips)]] — Subdivisión direccional: refina los cuadriláteros en una sola dirección
- [[Catálogo - Kangaroo2#RemeshByColour|RemeshByColour]] — Rehace la malla con longitudes de arista que dependen de los colores de los vértices de la malla de entrada
- [[Catálogo - Kangaroo2#Stripper|Stripper]] — Divide una malla en franjas
- [[Catálogo - Kangaroo2#TangentCircles (TC)|TangentCircles (TC)]] — Genera círculos inscritos en las caras, un empaquetado de círculos centrado en los vértices, o el dual por…
- [[Catálogo - Kangaroo2#Unroller|Unroller]] — Desenrolla una franja de cuadriláteros
- [[Catálogo - Kangaroo2#VertexNeighbours (VN)|VertexNeighbours (VN)]] — Devuelve las posiciones de los vértices conectados por una arista al vértice dado
- [[Catálogo - Kangaroo2#WarpWeft|WarpWeft]] — Separa las aristas de una malla en 2 listas según la dirección de urdimbre y trama

### LunchBox › Mesh (7)

- [[Catálogo - LunchBox#Mesh Edges (with Tolerance) (MshEdge)|Mesh Edges (with Tolerance) (MshEdge)]] — Busca las aristas desnudas de una malla y las aristas entre caras con un ángulo mayor que el indicado
- [[Catálogo - LunchBox#Mesh Extrude (MshExtrude)|Mesh Extrude (MshExtrude)]] — Extruye un objeto malla a lo largo de un vector dado
- [[Catálogo - LunchBox#Mesh Offset (MshOffset)|Mesh Offset (MshOffset)]] — Aplica offset a un objeto malla usando las normales de los vértices de la malla de origen
- [[Catálogo - LunchBox#Mesh Reduce (MshReduce)|Mesh Reduce (MshReduce)]] — Reduce los polígonos de una malla para simplificarla
- [[Catálogo - LunchBox#Mesh to Nurbs (MeshNurbs)|Mesh to Nurbs (MeshNurbs)]] — Convierte las caras de una malla en superficies NURBS
- [[Catálogo - LunchBox#Quad Remesh (Remesh)|Quad Remesh (Remesh)]] — Rehace la malla de un Brep o malla usando la función Quad Remesh de Rhino
- [[Catálogo - LunchBox#Quad Remesh Parameters (Parameters)|Quad Remesh Parameters (Parameters)]] — Parámetros para controlar la salida del componente Quad Remesh

### NGon › Adjacency (16)

- [[Catálogo - NGon#Mesh Edges (MeshEdges)|Mesh Edges (MeshEdges)]] — Obtiene toda la malla
- [[Catálogo - NGon#Naked Vertices (Naked)|Naked Vertices (Naked)]] — Vértices desnudos de la malla
- [[Catálogo - NGon#NGon Centers (NGonCenters)|NGon Centers (NGonCenters)]] — GetNGonCenter
- [[Catálogo - NGon#NGon Edges (Edges)|NGon Edges (Edges)]] — Obtiene los ids y las líneas de todas las aristas de los ngons
- [[Catálogo - NGon#NGon Face Edges (Face Edges)|NGon Face Edges (Face Edges)]] — Obtiene los ids y las líneas de las aristas de las caras de los ngons
- [[Catálogo - NGon#NGon Face Edges by NGon Pairs (EdgeByFP)|NGon Face Edges by NGon Pairs (EdgeByFP)]] — Obtiene las aristas de las caras de los NGons por pares de NGons
- [[Catálogo - NGon#NGon Face Edges Points (Face Edges Points)|NGon Face Edges Points (Face Edges Points)]] — Obtiene los ids y las líneas de las aristas de las caras de los ngons
- [[Catálogo - NGon#NGon Face Vertices (NGFaceVertices)|NGon Face Vertices (NGFaceVertices)]] — Obtiene los vértices de los ngons y los vértices topológicos
- [[Catálogo - NGon#NGon Faces (NGonFaces)|NGon Faces (NGonFaces)]] — Obtiene las caras de la malla en los NGons
- [[Catálogo - NGon#NGon To NGons (NGonToNgons)|NGon To NGons (NGonToNgons)]] — Obtiene los NGons adyacentes al NGon actual
- [[Catálogo - NGon#NGon Vertices (Vertices)|NGon Vertices (Vertices)]] — Obtiene todos los vértices de los ngons y sus vértices conectados en los ngons
- [[Catálogo - NGon#NGon Vertices (Vertices) · 2|NGon Vertices (Vertices) · 2]] — Obtiene todos los vértices de los ngons y los vértices topológicos
- [[Catálogo - NGon#NGons Around Vertices (Vertex Ngons)|NGons Around Vertices (Vertex Ngons)]] — Obtiene los ngons que rodean los vértices topológicos de la malla
- [[Catálogo - NGon#NGons Connected To NGon Edge (EdgeNGon)|NGons Connected To NGon Edge (EdgeNGon)]] — Obtiene los ngons conectados a las aristas de los ngons; se agrega -1 al inicio de la lista si la arista es…
- [[Catálogo - NGon#NGons Edges Around Vertices (VEdge Ngons)|NGons Edges Around Vertices (VEdge Ngons)]] — Obtiene los ngons que rodean los vértices topológicos de la malla
- [[Catálogo - NGon#Scale NGon Face Edges by NGon Pairs (SEdge)|Scale NGon Face Edges by NGon Pairs (SEdge)]] — Escala de Get NGon Face Edges by NGon Pairs

### NGon › Graph (8)

- [[Catálogo - NGon#BFS|BFS]] — Búsqueda en anchura (BFS) desde la malla
- [[Catálogo - NGon#Coloring|Coloring]] — Colorea las aristas con n colores
- [[Catálogo - NGon#ConvexHull|ConvexHull]] — Envolvente convexa a partir de puntos
- [[Catálogo - NGon#KMeans|KMeans]] — KMeans
- [[Catálogo - NGon#LineGraph|LineGraph]] — Grafo de líneas
- [[Catálogo - NGon#MeshCurve|MeshCurve]] — MeshCurve
- [[Catálogo - NGon#MeshSkeleton|MeshSkeleton]] — MeshSkeleton
- [[Catálogo - NGon#Walker|Walker]] — Walker

### NGon › Joint (4)

- [[Catálogo - NGon#Finger|Finger]] — Dedo en el plano
- [[Catálogo - NGon#JointsVDA|JointsVDA]] — JointsVDA
- [[Catálogo - NGon#MeshCollision (MC)|MeshCollision (MC)]] — MeshCollision
- [[Catálogo - NGon#MeshFlap|MeshFlap]] — MeshFlap

### NGon › NGons (9)

- [[Catálogo - NGon#AddNGons|AddNGons]] — Agrega NGons a las caras triangulares planas
- [[Catálogo - NGon#Clear|Clear]] — Borrar los ngons
- [[Catálogo - NGon#From Brep|From Brep]] — Crea una malla a partir de un brep poligonal
- [[Catálogo - NGon#From Mesh|From Mesh]] — Toma una malla y agrega ngons con el contorno de las aristas desnudas y la colección de todas las caras de la…
- [[Catálogo - NGon#From Polylines (FromP)|From Polylines (FromP)]] — Crea una malla a partir de polilíneas y agrega propiedades de NGons
- [[Catálogo - NGon#Get Polylines (ToP)|Get Polylines (ToP)]] — Revisa si hay ngons en una malla y los extrae
- [[Catálogo - NGon#MeshStatistics|MeshStatistics]] — MeshStatistics
- [[Catálogo - NGon#NgonH|NgonH]] — Ngon con agujeros, Delaunay con agujeros
- [[Catálogo - NGon#NGonPreview|NGonPreview]] — NGonPreview

### NGon › Planarize (5)

- [[Catálogo - NGon#Planar Faces (Planar)|Planar Faces (Planar)]] — Planariza los NGons de las caras vecinas
- [[Catálogo - NGon#Planarize|Planarize]] — Planarize
- [[Catálogo - NGon#Planarize2|Planarize2]] — Planarize2
- [[Catálogo - NGon#Project NGons (Project)|Project NGons (Project)]] — Proyecta los ngons a sus planos promedio
- [[Catálogo - NGon#ProjectPairs|ProjectPairs]] — ProjectPairs

### NGon › Polygon (24)

- [[Catálogo - NGon#Boolean|Boolean]] — Booleano de polilíneas
- [[Catálogo - NGon#Chamfer|Chamfer]] — Corta una curva abierta con una curva cerrada
- [[Catálogo - NGon#ClosestCurveComponent (CPCurve)|ClosestCurveComponent (CPCurve)]] — Busca las curvas más cercanas según una tolerancia
- [[Catálogo - NGon#CurveCP|CurveCP]] — Si el punto está cerca de una curva dada
- [[Catálogo - NGon#CurveCut|CurveCut]] — Corta una curva abierta con una curva cerrada
- [[Catálogo - NGon#CurveEnds|CurveEnds]] — Corrige los extremos de la curva
- [[Catálogo - NGon#CurveLoft|CurveLoft]] — Hace loft de curvas a una malla de cuadriláteros. Si no se entrega el parámetro V, la división por defecto en…
- [[Catálogo - NGon#CurveMatch|CurveMatch]] — CurveMatch
- [[Catálogo - NGon#CurvePreview (Display)|CurvePreview (Display)]] — CurvePreview
- [[Catálogo - NGon#CurveShatter|CurveShatter]] — Fragmenta curvas con puntos
- [[Catálogo - NGon#CurveSort|CurveSort]] — Ordena una lista de curvas según otras curvas
- [[Catálogo - NGon#GetTwo|GetTwo]] — Obtiene los dos contornos más grandes
- [[Catálogo - NGon#Intersection|Intersection]] — Intersección de polilíneas
- [[Catálogo - NGon#LineExtrude|LineExtrude]] — LineExtrude
- [[Catálogo - NGon#MapCrv|MapCrv]] — Mapea una lista de curvas de una polilínea a otra
- [[Catálogo - NGon#MapMesh|MapMesh]] — Mapeo de polilínea a malla
- [[Catálogo - NGon#MapSrf|MapSrf]] — Mapeo de polilínea a superficie
- [[Catálogo - NGon#PlaneDisplay (PD)|PlaneDisplay (PD)]] — PlaneDisplay
- [[Catálogo - NGon#Polyline Difference (Difference)|Polyline Difference (Difference)]] — Diferencia de polilíneas
- [[Catálogo - NGon#Polyline Move (PolylineMove)|Polyline Move (PolylineMove)]] — Mueve una curva cerrada en Z
- [[Catálogo - NGon#Polyline Offset (Offset)|Polyline Offset (Offset)]] — Offset de polilínea
- [[Catálogo - NGon#PolylineCenter (PCenter)|PolylineCenter (PCenter)]] — Obtiene el centro, la normal y el plano de las polilíneas
- [[Catálogo - NGon#Simplify|Simplify]] — Simplifica una polilínea
- [[Catálogo - NGon#Text|Text]] — Texto para corte láser o fresado

### NGon › Reciprocal (8)

- [[Catálogo - NGon#MeshProp|MeshProp]] — MeshProp
- [[Catálogo - NGon#ReciMove|ReciMove]] — Traslación de aristas que forma una nexorada
- [[Catálogo - NGon#ReciMoveVol|ReciMoveVol]] — Agrega elementos volumétricos a la traslación recíproca
- [[Catálogo - NGon#RecipricalEdges|RecipricalEdges]] — Rota la arista de la malla según la normal promedio
- [[Catálogo - NGon#RecipricalExtend|RecipricalExtend]] — Rota la arista de la malla y la extiende hasta la siguiente línea
- [[Catálogo - NGon#RecipricalThickness|RecipricalThickness]] — Rota la arista de la malla según la normal promedio y le da espesor
- [[Catálogo - NGon#RecipricalVolume|RecipricalVolume]] — Elementos volumétricos
- [[Catálogo - NGon#ReciRaw|ReciRaw]] — ReciRaw

### NGon › Subdivide (7)

- [[Catálogo - NGon#Chebyshev|Chebyshev]] — Redes de Chebyshev https://github.com/pearswj/buckminster
- [[Catálogo - NGon#DiamondDivide|DiamondDivide]] — Divide una superficie NURBS en formas de diamante
- [[Catálogo - NGon#HexDivide|HexDivide]] — Divide una superficie NURBS en hexágonos
- [[Catálogo - NGon#Platonic|Platonic]] — Obtiene un objeto platónico, por ejemplo icosaedro, toro, cubo o tetraedro
- [[Catálogo - NGon#QuadDivide|QuadDivide]] — Divide una NurbsSurface en cuadriláteros
- [[Catálogo - NGon#SortBrep|SortBrep]] — Ordena las caras del Brep si es posible
- [[Catálogo - NGon#TriangleSubdivision (Tesselate)|TriangleSubdivision (Tesselate)]] — Teselar

### NGon › Transform (19)

- [[Catálogo - NGon#AdjustMeshVertices (MatchMesh)|AdjustMeshVertices (MatchMesh)]] — Toma los vértices de una malla y ajusta los vértices de otra malla según las posiciones de la primera
- [[Catálogo - NGon#Corners|Corners]] — Esquinas
- [[Catálogo - NGon#CutMesh|CutMesh]] — CutMesh
- [[Catálogo - NGon#Dual|Dual]] — Dual
- [[Catálogo - NGon#Extrude Edges|Extrude Edges]] — Extruye las aristas de los NGons según las normales
- [[Catálogo - NGon#Flip|Flip]] — Invertir
- [[Catálogo - NGon#JointsVDA · 2|JointsVDA · 2]] — JointsVDA
- [[Catálogo - NGon#LatticeFromTwoMeshes (MatchMesh)|LatticeFromTwoMeshes (MatchMesh)]] — Toma los vértices de una malla y ajusta los vértices de otra malla según las posiciones de la primera
- [[Catálogo - NGon#Loft Polylines (Loft)|Loft Polylines (Loft)]] — Hace loft de dos polilíneas; deben tener la misma cantidad de puntos
- [[Catálogo - NGon#Loft Polylines (Loft) · 2|Loft Polylines (Loft) · 2]] — Hace loft de dos polilíneas; deben tener la misma cantidad de puntos
- [[Catálogo - NGon#NGonFrame|NGonFrame]] — NGonFrame
- [[Catálogo - NGon#Offset Projected|Offset Projected]] — Aplica offset a una malla usando el offset de malla o intersecciones con planos
- [[Catálogo - NGon#OffsetMesh|OffsetMesh]] — Malla con offset
- [[Catálogo - NGon#OffsetPlanar|OffsetPlanar]] — Offset de malla plana. Planar Offset funciona solo con mallas cerradas de valencia 3; para valencia n > 3 es…
- [[Catálogo - NGon#OffsetTriangleMesh|OffsetTriangleMesh]] — Malla OffsetTriangleMesh
- [[Catálogo - NGon#Simplify · 2|Simplify · 2]] — Quita los puntos con valencia menor que 3 o fijos
- [[Catálogo - NGon#Split3|Split3]] — Divide los ngons en 3 polilíneas si su cantidad de puntos es mayor que la definida; primero se dividen los…
- [[Catálogo - NGon#Stellate|Stellate]] — Crea pirámides y las corta con un plano
- [[Catálogo - NGon#UnifyWindings (Unify)|UnifyWindings (Unify)]] — UnifyWindings

### NGon › Utilities Mesh (22)

- [[Catálogo - NGon#BoundaryFirstFlatenning|BoundaryFirstFlatenning]] — BoundaryFirstFlatenning
- [[Catálogo - NGon#BrepEdges|BrepEdges]] — Obtiene las aristas del BRep que no pertenecen a la misma superficie
- [[Catálogo - NGon#ColorMesh|ColorMesh]] — ColorMesh
- [[Catálogo - NGon#DiagonalMesh (Diagonal)|DiagonalMesh (Diagonal)]] — DiagonalMesh
- [[Catálogo - NGon#DivideBox|DivideBox]] — DivideBox
- [[Catálogo - NGon#ExplodeMesh|ExplodeMesh]] — Explota la malla y asigna el color promedio a cada vértice de una cara
- [[Catálogo - NGon#FacesInCurves|FacesInCurves]] — FacesInCurves
- [[Catálogo - NGon#IsoSurface|IsoSurface]] — Isosuperficie
- [[Catálogo - NGon#LoftCircles|LoftCircles]] — LoftCircles
- [[Catálogo - NGon#Mesh Curvature|Mesh Curvature]] — Curvatura de la malla
- [[Catálogo - NGon#MeshCP|MeshCP]] — Si el punto está cerca de una malla o dentro de ella
- [[Catálogo - NGon#MeshCurve (MeshCrv)|MeshCurve (MeshCrv)]] — Si las curvas están dentro de la malla
- [[Catálogo - NGon#MeshPipe|MeshPipe]] — Crea una tubería de malla a partir de curvas
- [[Catálogo - NGon#Morph|Morph]] — Deformar (morph)
- [[Catálogo - NGon#PreviewEdges|PreviewEdges]] — Busca las aristas que están dentro de cierto ángulo respecto de las normales de las caras adyacentes de la…
- [[Catálogo - NGon#ProjectNakedEdgeToCurves (ProjectNaked)|ProjectNakedEdgeToCurves (ProjectNaked)]] — Proyecta la arista desnuda sobre las curvas
- [[Catálogo - NGon#Remesh|Remesh]] — Remallar
- [[Catálogo - NGon#Smooth|Smooth]] — Smooth
- [[Catálogo - NGon#Tri-Periodic Surfaces|Tri-Periodic Surfaces]] — Superficies triplemente periódicas
- [[Catálogo - NGon#Triangulate|Triangulate]] — Triangula según curvas
- [[Catálogo - NGon#Voxels|Voxels]] — Malla de vóxeles a partir de puntos
- [[Catálogo - NGon#WeldMesh (Weld)|WeldMesh (Weld)]] — Descripción

### Parakeet › Mesh (6)

- [[Catálogo - Parakeet#Angle Split Mesh (AngSplitMesh)|Angle Split Mesh (AngSplitMesh)]] — Divide una malla en piezas separadas desoldando las aristas que superan un umbral de ángulo dado
- [[Catálogo - Parakeet#Mesh Centroid (MeshCentroid)|Mesh Centroid (MeshCentroid)]] — Devuelve el centroide de una malla. Opcionalmente lo proyecta sobre la superficie de la malla
- [[Catálogo - Parakeet#Mesh Surface Variable (MeshSrfVar)|Mesh Surface Variable (MeshSrfVar)]] — Crea una malla según la curvatura de la superficie base (caras más grandes en zonas planas)
- [[Catálogo - Parakeet#Mesh Topology|Mesh Topology]] — Obtiene la topología completa de una malla
- [[Catálogo - Parakeet#MeshCap|MeshCap]] — Tapa todos los agujeros cubriendo las aristas desnudas
- [[Catálogo - Parakeet#Polyline To Mesh (Poly2Mesh)|Polyline To Mesh (Poly2Mesh)]] — Convierte polilíneas cerradas en mallas. Opcionalmente las extruye con un espesor

### Pufferfish › Mesh (27)

- [[Catálogo - Pufferfish#Angle Split Mesh (AngSplitMsh)|Angle Split Mesh (AngSplitMsh)]] — Divide una malla en mallas separadas midiendo una tolerancia angular entre las normales de caras adyacentes…
- [[Catálogo - Pufferfish#Average Mesh (AvrMsh)|Average Mesh (AvrMsh)]] — Calcula el promedio aritmético de un conjunto de mallas; las mallas deben tener la misma topología. También…
- [[Catálogo - Pufferfish#Blend Consecutive Meshes (BlndConMshs)|Blend Consecutive Meshes (BlndConMshs)]] — Mezcla (blend) consecutivamente entre un conjunto de mallas a través de sus vértices, con un conjunto de…
- [[Catálogo - Pufferfish#Blend Through Meshes (BlndThruMshs)|Blend Through Meshes (BlndThruMshs)]] — Mezcla (blend) a través de un conjunto de mallas por sus vértices, con un conjunto de factores donde cada uno…
- [[Catálogo - Pufferfish#Blend Two Meshes (Blnd2Mshs)|Blend Two Meshes (Blnd2Mshs)]] — Mezcla (blend) entre dos mallas por sus vértices, con un conjunto de factores donde cada uno controla la…
- [[Catálogo - Pufferfish#Close Mesh (ClsMsh)|Close Mesh (ClsMsh)]] — Cierra una malla abierta rellenando sus aberturas con caras nuevas; si la malla ya es cerrada, sale sin…
- [[Catálogo - Pufferfish#Displace Mesh (DisMsh)|Displace Mesh (DisMsh)]] — Desplaza una malla por sus vértices con un conjunto de distancias, donde cada distancia controla cuánto se…
- [[Catálogo - Pufferfish#Is Mesh Closed (MshClsd)|Is Mesh Closed (MshClsd)]] — Prueba si una malla es cerrada
- [[Catálogo - Pufferfish#Is Mesh Disjoint (MshDisjn)|Is Mesh Disjoint (MshDisjn)]] — Prueba si una malla tiene piezas desconectadas
- [[Catálogo - Pufferfish#Mesh Statistics (MshStats)|Mesh Statistics (MshStats)]] — Obtiene estadísticas de una malla: cantidad de vértices, de caras, de caras cuadrangulares, de caras…
- [[Catálogo - Pufferfish#Mirror Cut Mesh (MirCutMsh)|Mirror Cut Mesh (MirCutMsh)]] — Corta una malla con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo…
- [[Catálogo - Pufferfish#Offset Mesh (OffMsh)|Offset Mesh (OffMsh)]] — Aplica offset a una malla, con la opción de hacerlo hacia ambos lados a distancias distintas y crear un sólido
- [[Catálogo - Pufferfish#Parameter Extrude Mesh (ParamExtrMsh)|Parameter Extrude Mesh (ParamExtrMsh)]] — Crea una malla extruida a partir de una curva de perfil a lo largo de un vector, una curva o hacia un punto…
- [[Catálogo - Pufferfish#Parameter Loft Mesh (ParamLoftMsh)|Parameter Loft Mesh (ParamLoftMsh)]] — Crea una malla con loft a través de un conjunto de curvas de sección, dividiendo el dominio con parámetros…
- [[Catálogo - Pufferfish#Parameter Pipe Mesh (ParamPipeMsh)|Parameter Pipe Mesh (ParamPipeMsh)]] — Crea una malla tubular a lo largo de una curva, dividiendo el dominio con parámetros {u} y {v}, por…
- [[Catálogo - Pufferfish#Parameter Plane Mesh (ParamPlnMsh)|Parameter Plane Mesh (ParamPlnMsh)]] — Genera una malla plana en un rectángulo dividiendo su dominio con parámetros {x} e {y}
- [[Catálogo - Pufferfish#Parameter Surface Mesh (ParamSrfMsh)|Parameter Surface Mesh (ParamSrfMsh)]] — Genera una malla sobre una superficie dividiendo su dominio con parámetros {u} y {v}
- [[Catálogo - Pufferfish#Plane Trim Mesh (PlnTrimMsh)|Plane Trim Mesh (PlnTrimMsh)]] — Recorta (quita) las partes de una malla que están a un lado de un plano
- [[Catálogo - Pufferfish#Polyline To Mesh (PLine2Msh)|Polyline To Mesh (PLine2Msh)]] — Crea una malla a partir de un contorno de polilínea cerrado o abierto
- [[Catálogo - Pufferfish#Rebuild Mesh (RebMsh)|Rebuild Mesh (RebMsh)]] — Reconstruye una malla con opciones para recalcular normales, quitar caras y vértices no usados, combinar…
- [[Catálogo - Pufferfish#Recursive Morph Mesh (ReMorphMsh)|Recursive Morph Mesh (ReMorphMsh)]] — Deforma (morph) de forma recursiva geometrías de malla sobre las caras de una malla, empezando por una malla…
- [[Catálogo - Pufferfish#Reduce Mesh (ReduMsh)|Reduce Mesh (ReduMsh)]] — Reduce la cantidad de caras de una malla hasta un objetivo (mira la línea de comandos de Rhino para ver el %…
- [[Catálogo - Pufferfish#Tween Consecutive Meshes (TwnConMshs)|Tween Consecutive Meshes (TwnConMshs)]] — Interpola (tween) consecutivamente entre un conjunto de mallas; las mallas deben tener la misma topología.…
- [[Catálogo - Pufferfish#Tween Through Meshes (TwnThruMshs)|Tween Through Meshes (TwnThruMshs)]] — Interpola (tween) a través de un conjunto de mallas; las mallas deben tener la misma topología. También puede…
- [[Catálogo - Pufferfish#Tween Two Meshes (Twn2Mshs)|Tween Two Meshes (Twn2Mshs)]] — Interpola (tween) entre dos mallas; las mallas deben tener la misma topología. También puede interpolar los…
- [[Catálogo - Pufferfish#Voxel Mesh (VoxMsh)|Voxel Mesh (VoxMsh)]] — Crea una voxelización orientada a un plano de un conjunto de puntos, como malla sin caras interiores…
- [[Catálogo - Pufferfish#Weighted Average Mesh (WavMsh)|Weighted Average Mesh (WavMsh)]] — Calcula el promedio aritmético ponderado de un conjunto de mallas; las mallas deben tener la misma topología.…

### Pufferfish › SubD (10)

- [[Catálogo - Pufferfish#Average SubD (AvrSubD, user object)|Average SubD (AvrSubD, user object)]] — Calcula el promedio aritmético de un conjunto de SubDs; las SubDs deben tener la misma topología. (*Solo…
- [[Catálogo - Pufferfish#Mirror Cut SubD (MirCutSubD, user object)|Mirror Cut SubD (MirCutSubD, user object)]] — Corta una SubD con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo…
- [[Catálogo - Pufferfish#Tween Consecutive SubDs (TwnConSubDs, user object)|Tween Consecutive SubDs (TwnConSubDs, user object)]] — Interpola (tween) consecutivamente entre un conjunto de SubDs; las SubDs deben tener la misma topología.…
- [[Catálogo - Pufferfish#Tween Through SubDs (TwnThruSubDs, user object)|Tween Through SubDs (TwnThruSubDs, user object)]] — Interpola (tween) a través de un conjunto de SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)
- [[Catálogo - Pufferfish#Tween Two SubDs (Twn2SubDs, user object)|Tween Two SubDs (Twn2SubDs, user object)]] — Interpola (tween) entre dos SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)
- [[Catálogo - Pufferfish#Twisted Box Consecutive SubDs (TBoxConSubDs, user object)|Twisted Box Consecutive SubDs (TBoxConSubDs, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre un conjunto de SubDs a partir…
- [[Catálogo - Pufferfish#Twisted Box SubD (TBoxSubD, user object)|Twisted Box SubD (TBoxSubD, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas sobre una SubD, a partir de sus caras y un espesor…
- [[Catálogo - Pufferfish#Twisted Box Through SubDs (TBoxThruSubDs, user object)|Twisted Box Through SubDs (TBoxThruSubDs, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de SubDs a partir de sus caras…
- [[Catálogo - Pufferfish#Twisted Box Two SubDs (TBox2SubDs, user object)|Twisted Box Two SubDs (TBox2SubDs, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas entre dos SubDs a partir de sus caras; las SubDs deben…
- [[Catálogo - Pufferfish#Weighted Average SubD (WavSubD, user object)|Weighted Average SubD (WavSubD, user object)]] — Calcula el promedio aritmético ponderado de un conjunto de SubDs; las SubDs deben tener la misma topología.…

### Wb › Create (2)

- [[Catálogo - Wb#Weaverbird's Mesh From Lines (Weave Back) (wbWeave)|Weaverbird's Mesh From Lines (Weave Back) (wbWeave)]] — Transforma una lista de líneas en una malla. (Componente experimental que permite probar funciones futuras.)…
- [[Catálogo - Wb#Weaverbird's Tile (wbTile)|Weaverbird's Tile (wbTile)]] — Tesela algunas caras de una malla según sus propiedades laterales y una regla elegida. (Componente…

### Wb › Define (6)

- [[Catálogo - Wb#Weaverbird's Mesh Antiprism (wbAntiprism)|Weaverbird's Mesh Antiprism (wbAntiprism)]] — Construye una forma sólida (antiprisma). Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Mesh Dipyramid (wbDipyramid)|Weaverbird's Mesh Dipyramid (wbDipyramid)]] — Construye una forma sólida (bipirámide). Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Mesh Mesh Icosahedron (wbIcosahedron)|Weaverbird's Mesh Mesh Icosahedron (wbIcosahedron)]] — Construye una malla (icosaedro de malla). Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Mesh Prism (wbPrism)|Weaverbird's Mesh Prism (wbPrism)]] — Construye una forma sólida (prisma). Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Mesh Pyramid (wbPyramid)|Weaverbird's Mesh Pyramid (wbPyramid)]] — Construye una forma sólida (pirámide). Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Polylines Dodecahedron (wbDodecahedron)|Weaverbird's Polylines Dodecahedron (wbDodecahedron)]] — Construye una malla (dodecaedro de polilíneas). Provisto por Weaverbird 0.9.0.1

### Wb › Extract (9)

- [[Catálogo - Wb#Weaverbird's Dual graph (wbDual)|Weaverbird's Dual graph (wbDual)]] — Este componente calcula el dual débil de la malla. Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Face Polylines (wbFacePolys)|Weaverbird's Face Polylines (wbFacePolys)]] — Devuelve la representación poligonal de una malla, como si cada cara fuera un circuito cerrado de polilínea.…
- [[Catálogo - Wb#Weaverbird's Join Meshes and Weld (wbJoin)|Weaverbird's Join Meshes and Weld (wbJoin)]] — Devuelve un único objeto malla formado a partir de una lista de mallas. La malla nueva es más liviana: ocupa…
- [[Catálogo - Wb#Weaverbird's Mesh Edges (wbEdges)|Weaverbird's Mesh Edges (wbEdges)]] — Devuelve la representación en alambre (wireframe) de una malla. Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Naked boundary (wbNaked)|Weaverbird's Naked boundary (wbNaked)]] — Busca la policurva desnuda (cubierta por una sola cara) como la unión de varias aristas desnudas. Provisto…
- [[Catálogo - Wb#Weaverbird's Reroute Faces (wbReroute)|Weaverbird's Reroute Faces (wbReroute)]] — Devuelve una malla nueva formada por una sublista de caras. Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Reroute Faces by Pattern (wbReroutePattern)|Weaverbird's Reroute Faces by Pattern (wbReroutePattern)]] — Devuelve una malla nueva formada por una sublista de caras: las caras 'True' van a una salida y las 'False' a…
- [[Catálogo - Wb#Weaverbird's Unify face windings (wbUnify)|Weaverbird's Unify face windings (wbUnify)]] — Se asegura de que el sentido de giro de las caras sea uno solo, cuando es posible. Provisto por Weaverbird…
- [[Catálogo - Wb#Weaverbird's Vertices Component (wbVertices)|Weaverbird's Vertices Component (wbVertices)]] — Devuelve la representación en puntos de una malla. Provisto por Weaverbird 0.9.0.1

### Wb › Smoothen (3)

- [[Catálogo - Wb#Weaverbird's Blur Mesh (wbBlur)|Weaverbird's Blur Mesh (wbBlur)]] — Calcula una representación suavizada de una malla original, pero solo en cuanto a colores y coordenadas de…
- [[Catálogo - Wb#Weaverbird's Laplacian Smoothing (wbLaplace)|Weaverbird's Laplacian Smoothing (wbLaplace)]] — Calcula una representación suavizada de una malla original. No aumenta la cantidad de caras. Provisto por…
- [[Catálogo - Wb#Weaverbird's LaplacianHC Smoothing (wbLaplaceHC)|Weaverbird's LaplacianHC Smoothing (wbLaplaceHC)]] — Calcula una representación suavizada de una malla original. No aumenta la cantidad de caras. Permite indicar…

### Wb › SubD (8)

- [[Catálogo - Wb#Weaverbird's Catmull-Clark Subdivision (wbCatmullClark)|Weaverbird's Catmull-Clark Subdivision (wbCatmullClark)]] — Calcula la subdivisión recursiva de mallas descrita por Edwin Catmull y Jim Clark, en su paper de 1978. La…
- [[Catálogo - Wb#Weaverbird's Constant Quads Split Subdivision (wbSplitQuads)|Weaverbird's Constant Quads Split Subdivision (wbSplitQuads)]] — Calcula una malla de solo cuadriláteros y de aspecto similar, que se obtiene agregando una cara por cada…
- [[Catálogo - Wb#Weaverbird's Inner Polygons Subdivision (wbInnerPolygons)|Weaverbird's Inner Polygons Subdivision (wbInnerPolygons)]] — Coloca una cara nueva que parte del punto medio de cada arista de cada cara original. Provisto por Weaverbird…
- [[Catálogo - Wb#Weaverbird's Loop Subdivision (wbLoop)|Weaverbird's Loop Subdivision (wbLoop)]] — Calcula la subdivisión recursiva de mallas descrita por Charles Loop en su tesis de matemáticas de 1987.…
- [[Catálogo - Wb#Weaverbird's Midedge Subdivision (wbMidedge)|Weaverbird's Midedge Subdivision (wbMidedge)]] — Calcula la subdivisión recursiva de mallas que se obtiene dividiendo las aristas en su punto medio. Provisto…
- [[Catálogo - Wb#Weaverbird's Sierpinski Triangles Subdivision (wbSierpinski)|Weaverbird's Sierpinski Triangles Subdivision (wbSierpinski)]] — Coloca un triángulo en cada esquina de una cara de la malla. La malla tendrá un agujero más por cara.…
- [[Catálogo - Wb#Weaverbird's Split Polygons Subdivision (wbSplitPolygons)|Weaverbird's Split Polygons Subdivision (wbSplitPolygons)]] — Coloca una cara nueva que parte del punto medio de cada arista de cada cara original y tapa el agujero con…
- [[Catálogo - Wb#Weaverbird's Split Triangles Subdivision (wbTriangles)|Weaverbird's Split Triangles Subdivision (wbTriangles)]] — Coloca varios triángulos en cada cara. Provisto por Weaverbird 0.9.0.1

### Wb › Transform (8)

- [[Catálogo - Wb#Weaverbird's Bevel Edges (wbBevelEdges)|Weaverbird's Bevel Edges (wbBevelEdges)]] — Reemplaza cada arista de la malla original por una cara nueva que conecta los dos vértices y, por el lado…
- [[Catálogo - Wb#Weaverbird's Bevel Vertices (wbBevelVertices)|Weaverbird's Bevel Vertices (wbBevelVertices)]] — Reemplaza cada vértice de la malla original por una cara nueva que conecta todas las aristas. Provisto por…
- [[Catálogo - Wb#Weaverbird's Mesh Thicken (wbThicken)|Weaverbird's Mesh Thicken (wbThicken)]] — Calcula una malla nueva que es un sólido cerrado, siempre que a la malla original se le pueda aplicar offset…
- [[Catálogo - Wb#Weaverbird's Mesh Window (wbWindow)|Weaverbird's Mesh Window (wbWindow)]] — Reemplaza cada cara de la malla original por una nueva, reconstruida hacia adentro. Cada cara tiene la misma…
- [[Catálogo - Wb#Weaverbird's Offset Mesh (wbOffset)|Weaverbird's Offset Mesh (wbOffset)]] — Calcula un offset de mallas. El resultado es abierto si la entrada es abierta. Provisto por Weaverbird 0.9.0.1
- [[Catálogo - Wb#Weaverbird's Picture Frame (wbFrame)|Weaverbird's Picture Frame (wbFrame)]] — Calcula una malla nueva de género mayor, donde cada cara tiene un agujero nuevo al centro y parece un marco…
- [[Catálogo - Wb#Weaverbird's Sierpinski Carpet (wbCarpet)|Weaverbird's Sierpinski Carpet (wbCarpet)]] — Calcula una malla nueva de género mayor, donde cada cara tiene un agujero nuevo al centro. La malla…
- [[Catálogo - Wb#Weaverbird's Stellate/Cumulation (wbStellate)|Weaverbird's Stellate/Cumulation (wbStellate)]] — Agrega una pirámide sobre cada cara (a veces llamado kis). (Componente experimental que permite probar…

<!-- AUTO:fin -->
