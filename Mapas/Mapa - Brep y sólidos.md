---
tags: [tipo/mapa, geometria/brep, software/grasshopper, software/rhinocommon, software/cadquery]
---

# Brep y sólidos

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Un **Brep** (boundary representation) es geometría + topología: caras, aristas, vértices y bucles de recorte. Es lo que Rhino llama polisuperficie y lo que CadQuery (OpenCascade) usa para todo. Aquí van los sólidos, los booleanos y la descomposición en caras y aristas.

## Teoría y código
- [[wiki/concepts/brep-polisuperficies]]: faces, edges, trims, loops
- [[wiki/concepts/superficies-nurbs]] · [[wiki/concepts/tipos-geometria-rhinocommon]]
- [[wiki/sources/2026-05-04-rhinopy-solidos-brep]] · [[wiki/sources/2026-05-04-rhinopy-primitivas]]
- [[Aprendizaje/CadQuery/CadQuery vs RhinoCommon]]: el mismo modelo B-rep visto desde CadQuery

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Caja | [[Catálogo - Surface#Center Box (Box)\|Center Box]] | `rg.Box(plano, ix, iy, iz).ToBrep()` | `cq.Workplane().box(x, y, z)` |
| Unión | [[Catálogo - Intersect#Solid Union (SUnion)\|Solid Union]] | `rg.Brep.CreateBooleanUnion(breps, tol)` | `.union(otro)` |
| Diferencia | [[Catálogo - Intersect#Solid Difference (SDiff)\|Solid Difference]] | `rg.Brep.CreateBooleanDifference(a, b, tol)` | `.cut(otro)` |
| Intersección | [[Catálogo - Intersect#Solid Intersection (SInt)\|Solid Intersection]] | `rg.Brep.CreateBooleanIntersection(a, b, tol)` | `.intersect(otro)` |
| Unir polisuperficies | [[Catálogo - Surface#Brep Join (Join)\|Brep Join]] | `rg.Brep.JoinBreps(breps, tol)` | — |
| Tapar agujeros planos | [[Catálogo - Surface#Cap Holes (Cap)\|Cap Holes]] | `brep.CapPlanarHoles(tol)` | — |
| Caras, aristas, vértices | [[Catálogo - Surface#Deconstruct Brep (DeBrep)\|Deconstruct Brep]] | `brep.Faces`, `brep.Edges`, `brep.Vertices` | `.faces()`, `.edges()`, `.vertices()` |
| Volumen | [[Catálogo - Surface#Volume\|Volume]] | `rg.VolumeMassProperties.Compute(brep).Volume` | `solido.Volume()` |
| Redondear aristas | [[Catálogo - Surface#Fillet Edge (FilEdge)\|Fillet Edge]] | `rg.Brep.CreateFilletEdges(...)` | `.edges(selector).fillet(r)` |

`tol` = `doc.ModelAbsoluteTolerance` (en Grasshopper: `Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance`).

## Para empezar
[[Catálogo - Surface#Deconstruct Brep (DeBrep)|Deconstruct Brep]] · [[Catálogo - Surface#Brep Join (Join)|Brep Join]] · [[Catálogo - Surface#Cap Holes (Cap)|Cap Holes]] · [[Catálogo - Intersect#Solid Difference (SDiff)|Solid Difference]] · [[Catálogo - Intersect#Split Brep (Split)|Split Brep]] · [[Catálogo - Surface#Brep Closest Point (Brep CP)|Brep Closest Point]] · [[Catálogo - Surface#Point In Brep (BrepInc)|Point In Brep]] · [[Catálogo - Surface#Bounding Box (BBox)|Bounding Box]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (19)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Brep Box | [[Add Brep Box\|Py]] · [[Add Brep Box (cs)\|C#]] | Crea una caja Brep desde dos esquinas | `BoundingBox(p0, p1).ToBrep()` |
| Add Cone | [[Add Cone\|Py]] · [[Add Cone (cs)\|C#]] | Crea un cono desde plano, altura y radio | `Cone(plano, h, r).ToBrep(tapa)` |
| Add Cylinder | [[Add Cylinder\|Py]] · [[Add Cylinder (cs)\|C#]] | Crea un cilindro desde un círculo y una altura | `Cylinder(circulo, h).ToBrep(True, True)` |
| Add Sphere | [[Add Sphere\|Py]] · [[Add Sphere (cs)\|C#]] | Crea una esfera con centro y radio | `Sphere(centro, r) → doc.Objects.AddSphere` |
| Add Torus | [[Add Torus\|Py]] · [[Add Torus (cs)\|C#]] | Crea un toro desde un plano y dos radios | `Torus(plano, R, r).ToRevSurface()` |
| Add Truncated Cone | [[Add Truncated Cone\|Py]] · [[Add Truncated Cone (cs)\|C#]] | Cono truncado por revolución entre dos círculos | `RevSurface.Create(perfil, eje) → Brep.CreateFromRevSurface` |
| Add Twisted Cube | [[Add Twisted Cube (cs)\|C#]] | Arma un Brep pieza por pieza: vértices, aristas, caras, loops y trims | `Brep.Vertices / Curves3D / Edges / Faces / Loops / Trims` |
| Boolean Difference | [[Boolean Difference\|Py]] · [[Boolean Difference (cs)\|C#]] | Diferencia booleana entre dos grupos de polisuperficies | `Brep.CreateBooleanDifference(a, b, tol)` |
| Box Shell | [[Box Shell (cs)\|C#]] | Da espesor a una caja quitando una cara (vaciado) | `Brep.CreateShell(brep, carasAQuitar, espesor, tol)` |
| Brep from Curve Bounding Box | [[Brep from Curve Bounding Box\|Py]] · [[Brep from Curve Bounding Box (cs)\|C#]] | Caja Brep desde la caja contenedora de una curva, alineada al plano de construcción | `Curve.GetBoundingBox(plano) → Brep.CreateFromBox` |
| Create Mesh from Brep | [[Create Mesh from Brep\|Py]] · [[Create Mesh from Brep (cs)\|C#]] | Convierte un Brep en malla con parámetros de mallado | `Mesh.CreateFromBrep(brep, MeshingParameters.Smooth)` |
| Determine Normal Direction of Brep Face | [[Determine Normal Direction of Brep Face\|Py]] · [[Determine Normal Direction of Brep Face (cs)\|C#]] | Normal de una cara en un punto, considerando si está invertida | `BrepFace.ClosestPoint → NormalAt(u, v), OrientationIsReversed` |
| Duplicate Surface Border | [[Duplicate Surface Border\|Py]] · [[Duplicate Surface Border (cs)\|C#]] | Borde de una superficie o polisuperficie como curvas | `Brep.DuplicateEdgeCurves(True) → Curve.JoinCurves` |
| Extrude Brep Face | [[Extrude Brep Face (cs)\|C#]] | Extruye una cara a lo largo de una curva | `BrepFace.CreateExtrusion(curva, tapar)` |
| IsBrepBox Test | [[IsBrepBox Test\|Py]] · [[IsBrepBox Test (cs)\|C#]] | Comprueba si un Brep es una caja: 6 caras planas a escuadra | `Brep.IsSolid, BrepFace.TryGetPlane, producto punto` |
| Project Points to Breps | [[Project Points to Breps\|Py]] · [[Project Points to Breps (cs)\|C#]] | Proyecta puntos sobre Breps en una dirección | `Intersection.ProjectPointsToBreps` |
| Split BReps with Planes | [[Split BReps with Planes\|Py]] · [[Split BReps with Planes (cs)\|C#]] | Corta Breps con un plano | `PlaneSurface.CreateThroughBox → Brep.Split(cortador, tol)` |
| Tight Bounding Boxes for Breps | [[Tight Bounding Boxes for Breps\|Py]] · [[Tight Bounding Boxes for Breps (cs)\|C#]] | Cajas contenedoras ajustadas de las partes de una superficie cortada | `BrepFace.Split → Mesh.CreateFromBrep → GetBoundingBox` |
| Transform Breps | [[Transform Breps\|Py]] · [[Transform Breps (cs)\|C#]] | Mueve un Brep con una transformación | `Transform.Translation(x, y, z) → doc.Objects.Transform` |

## Componentes de Grasshopper (114)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (3)

- [[Catálogo - Params#Box (parámetro)|Box (parámetro)]] — Contiene una colección de cajas
- [[Catálogo - Params#Brep (parámetro)|Brep (parámetro)]] — Contiene una colección de Breps (Boundary REPresentations)
- [[Catálogo - Params#Extrusion (parámetro)|Extrusion (parámetro)]] — Contiene una colección de extrusiones

### Params › Input (1)

- [[Catálogo - Params#Import SHP (SHP)|Import SHP (SHP)]] — Importa datos de archivos GIS *.shp

### Params › OpenNest2 (4)

- [[Catálogo - Params#Geometry (Surfaces) (Geometry Srf)|Geometry (Surfaces) (Geometry Srf)]] — Construye piezas para anidar a partir de superficies planas en vez de curvas; los agujeros se leen de los…
- [[Catálogo - Params#Rhino Objects (RhinoObjects)|Rhino Objects (RhinoObjects)]] — Lee objetos de Rhino referenciados, con atributos como texto, y los convierte en Breps planos para el anidado
- [[Catálogo - Params#Sheets (Surfaces) (Sheets Srf)|Sheets (Surfaces) (Sheets Srf)]] — Define las planchas sobre las que anidar a partir de superficies planas en vez de polilíneas; los agujeros…
- [[Catálogo - Params#Unroll|Unroll]] — Desenrolla un Brep o malla desarrollable a plano, llevando consigo sus curvas, puntos y textos

### Sets › Text (1)

- [[Catálogo - Sets#Text On Surface (TextSrf)|Text On Surface (TextSrf)]] — Crea una colección de símbolos de texto alineados sobre una superficie

### Curve › Util (1)

- [[Catálogo - Curve#Project Curve (Project)|Project Curve (Project)]] — Proyecta una curva sobre un Brep

### Surface › Analysis (8)

- [[Catálogo - Surface#Brep Closest Point (Brep CP)|Brep Closest Point (Brep CP)]] — Busca el punto más cercano en un brep
- [[Catálogo - Surface#Brep Edges (Edges)|Brep Edges (Edges)]] — Extrae las curvas de arista de un brep
- [[Catálogo - Surface#Brep Topology (Topology)|Brep Topology (Topology)]] — Obtiene y muestra la topología de un brep
- [[Catálogo - Surface#Brep Wireframe (Wires)|Brep Wireframe (Wires)]] — Extrae las curvas de alambre (wireframe) de un brep
- [[Catálogo - Surface#Deconstruct Brep (DeBrep)|Deconstruct Brep (DeBrep)]] — Descompone un brep en sus partes
- [[Catálogo - Surface#Point In Brep (BrepInc)|Point In Brep (BrepInc)]] — Prueba si un punto está dentro de un brep cerrado
- [[Catálogo - Surface#Point In Breps (BrepsInc)|Point In Breps (BrepsInc)]] — Prueba si un punto está dentro de una colección de breps cerrados
- [[Catálogo - Surface#Shape In Brep (ShapeIn)|Shape In Brep (ShapeIn)]] — Prueba si una forma está dentro de un brep

### Surface › Freeform (13)

- [[Catálogo - Surface#Edge Surface (EdgeSrf)|Edge Surface (EdgeSrf)]] — Crea una superficie a partir de dos, tres o cuatro curvas de borde
- [[Catálogo - Surface#Extrude Along (ExtrCrv)|Extrude Along (ExtrCrv)]] — Extruye curvas y superficies a lo largo de una curva
- [[Catálogo - Surface#Extrude Linear (Extrude)|Extrude Linear (Extrude)]] — Extruye curvas y superficies a lo largo de un camino recto
- [[Catálogo - Surface#Extrude Point (Extr)|Extrude Point (Extr)]] — Extruye curvas y superficies hasta un punto
- [[Catálogo - Surface#Fragment Patch (FPatch)|Fragment Patch (FPatch)]] — Crea un parche fragmentado a partir de un borde de polilínea
- [[Catálogo - Surface#Loft|Loft]] — Crea una superficie con loft a través de un conjunto de curvas de sección
- [[Catálogo - Surface#Pipe|Pipe]] — Crea una superficie de tubería alrededor de una curva de riel
- [[Catálogo - Surface#Pipe Variable (VPipe)|Pipe Variable (VPipe)]] — Crea una superficie de tubería con radios variables alrededor de una curva de riel
- [[Catálogo - Surface#Rail Revolution (RailRev)|Rail Revolution (RailRev)]] — Crea una superficie de revolución usando un riel de barrido
- [[Catálogo - Surface#Revolution (RevSrf)|Revolution (RevSrf)]] — Crea una superficie de revolución
- [[Catálogo - Surface#Sum Surface (SumSrf)|Sum Surface (SumSrf)]] — Crea una superficie de suma a partir de dos curvas de borde
- [[Catálogo - Surface#Sweep1 (Swp1)|Sweep1 (Swp1)]] — Crea una superficie de barrido (sweep) con una curva de riel
- [[Catálogo - Surface#Sweep2 (Swp2)|Sweep2 (Swp2)]] — Crea una superficie de barrido (sweep) con dos curvas de riel

### Surface › Primitive (1)

- [[Catálogo - Surface#Quad Sphere (QSph)|Quad Sphere (QSph)]] — Crea un brep esférico formado por parches NURBS cuadrangulares

### Surface › SubD (1)

- [[Catálogo - Surface#SubD To Brep (ToBrep)|SubD To Brep (ToBrep)]] — Convierte una superficie de subdivisión en una polisuperficie equivalente formada por caras NURBS

### Surface › Util (11)

- [[Catálogo - Surface#Brep Join (Join)|Brep Join (Join)]] — Une varios Breps
- [[Catálogo - Surface#Cap Holes (Cap)|Cap Holes (Cap)]] — Tapa todos los agujeros planos de un Brep
- [[Catálogo - Surface#Cap Holes Ex (CapEx)|Cap Holes Ex (CapEx)]] — Tapa la mayor cantidad posible de agujeros de un Brep
- [[Catálogo - Surface#Convex Edges (EdgesCvx)|Convex Edges (EdgesCvx)]] — Selecciona las aristas cóncavas o convexas de un brep
- [[Catálogo - Surface#Edges from Directions (EdgesDir)|Edges from Directions (EdgesDir)]] — Selecciona aristas de un brep según su dirección
- [[Catálogo - Surface#Edges from Faces (EdgesFaces)|Edges from Faces (EdgesFaces)]] — Selecciona todas las aristas del brep que delimitan ciertas caras
- [[Catálogo - Surface#Edges from Length (EdgesLen)|Edges from Length (EdgesLen)]] — Selecciona aristas de un brep según su longitud
- [[Catálogo - Surface#Edges from Linearity (EdgesLin)|Edges from Linearity (EdgesLin)]] — Selecciona aristas de un brep según su linealidad
- [[Catálogo - Surface#Edges from Points (EdgesPt)|Edges from Points (EdgesPt)]] — Selecciona aristas de un brep según su coincidencia con puntos
- [[Catálogo - Surface#Fillet Edge (FilEdge)|Fillet Edge (FilEdge)]] — Aplica fillet a algunas aristas de un brep
- [[Catálogo - Surface#Merge Faces (FMerge)|Merge Faces (FMerge)]] — Fusiona todas las caras coplanares adyacentes de un brep

### Mesh › Triangulation (2)

- [[Catálogo - Mesh#Voronoi 3D (Voronoi³)|Voronoi 3D (Voronoi³)]] — Diagrama de Voronoi volumétrico de una colección de puntos
- [[Catálogo - Mesh#Voronoi Cell (VCell)|Voronoi Cell (VCell)]] — Calcula una sola celda de Voronoi 3D

### Mesh › Util (2)

- [[Catálogo - Mesh#Mesh Brep (Mesh)|Mesh Brep (Mesh)]] — Crea una malla que aproxima la geometría de un Brep
- [[Catálogo - Mesh#Simple Mesh (SMesh)|Simple Mesh (SMesh)]] — Crea una malla que representa un Brep de la forma más simple posible

### Intersect › Mathematical (2)

- [[Catálogo - Intersect#Brep – Line (BLX)|Brep – Line (BLX)]] — Calcula las intersecciones entre un Brep y una línea
- [[Catálogo - Intersect#Brep – Plane (Sec)|Brep – Plane (Sec)]] — Calcula las intersecciones entre un Brep y un plano (lo que también se conoce como sección)

### Intersect › Physical (2)

- [[Catálogo - Intersect#Brep – Brep (BBX)|Brep – Brep (BBX)]] — Calcula las intersecciones entre dos Breps
- [[Catálogo - Intersect#Brep – Curve (BCX)|Brep – Curve (BCX)]] — Calcula las intersecciones entre un Brep y una curva

### Intersect › Region (4)

- [[Catálogo - Intersect#Split with Brep (Split)|Split with Brep (Split)]] — Divide una curva con un Brep
- [[Catálogo - Intersect#Split with Breps (Split)|Split with Breps (Split)]] — Divide una curva con varios Breps
- [[Catálogo - Intersect#Trim with Brep (Trim)|Trim with Brep (Trim)]] — Recorta una curva con un Brep
- [[Catálogo - Intersect#Trim with Breps (Trim)|Trim with Breps (Trim)]] — Recorta una curva con varios Breps

### Intersect › Shape (8)

- [[Catálogo - Intersect#Boundary Volume (BVol)|Boundary Volume (BVol)]] — Crea una polisuperficie cerrada a partir de superficies de contorno
- [[Catálogo - Intersect#Box Slits (Slits)|Box Slits (Slits)]] — Agrega ranuras (slits) a una colección de cajas que se intersectan
- [[Catálogo - Intersect#Solid Difference (SDiff)|Solid Difference (SDiff)]] — Realiza una diferencia sólida entre dos conjuntos de Breps
- [[Catálogo - Intersect#Solid Intersection (SInt)|Solid Intersection (SInt)]] — Realiza una intersección sólida entre dos conjuntos de Breps
- [[Catálogo - Intersect#Solid Union (SUnion)|Solid Union (SUnion)]] — Realiza una unión sólida de un conjunto de Breps
- [[Catálogo - Intersect#Split Brep (Split)|Split Brep (Split)]] — Divide un brep con otro
- [[Catálogo - Intersect#Split Brep Multiple (SplitMul)|Split Brep Multiple (SplitMul)]] — Divide un brep con un grupo de otros breps
- [[Catálogo - Intersect#Trim Solid (Trim)|Trim Solid (Trim)]] — Abre perforaciones en una forma con un conjunto de cortadores sólidos

### Biber › Assemble Tools (4)

- [[Catálogo - Biber#Disassemble Joint (Joint)|Disassemble Joint (Joint)]] — Obtiene la información de los elementos Shell, como objetos sólidos, superficies, etc
- [[Catálogo - Biber#Disassemble Node (Node)|Disassemble Node (Node)]] — Obtiene la información de los elementos Node, como objetos sólidos, superficies, índices, etc
- [[Catálogo - Biber#Fillet Shell Edges (FSE)|Fillet Shell Edges (FSE)]] — Aplica fillet a las aristas del shell según su tipo. Las aristas convexas/cóncavas y de superficie se pueden…
- [[Catálogo - Biber#Shell Geometry (SG)|Shell Geometry (SG)]] — Construye la geometría del shell y algunos objetos auxiliares para el proceso de fresado

### Biber › Optimization (1)

- [[Catálogo - Biber#Split Polygon by Angle (SPA)|Split Polygon by Angle (SPA)]] — Divide los polígonos en los vértices con un ángulo mayor que el umbral de entrada. El polígono se divide…

### Biber › PPS Tools (1)

- [[Catálogo - Biber#PPS Polygon (V)|PPS Polygon (V)]] — Extrae información de los polígonos de una polisuperficie plana

### Biber › Simulation (1)

- [[Catálogo - Biber#Assembly Simulation (AS)|Assembly Simulation (AS)]] — Muestra la secuencia de un ensamble colocando cada pieza en su posición en el orden y la dirección correctos

### Biber › Sub-Structure (5)

- [[Catálogo - Biber#Deconstruct 2D Connector (2DC)|Deconstruct 2D Connector (2DC)]] — Conecta dos shells adyacentes cerca de la ubicación del nodo
- [[Catálogo - Biber#Deconstruct 3D Connector (3DC)|Deconstruct 3D Connector (3DC)]] — Conecta dos shells adyacentes cerca de la ubicación del nodo
- [[Catálogo - Biber#Deconstruct Edge Support (DCES)|Deconstruct Edge Support (DCES)]] — Descompone los soportes de arista generados por el Edge Support System en sus subcomponentes (geometría…
- [[Catálogo - Biber#Deconstruct Frame (F)|Deconstruct Frame (F)]] — Un marco que sostiene los shells a lo largo de las aristas
- [[Catálogo - Biber#Tongue And Groove System (TGS)|Tongue And Groove System (TGS)]] — Crea una serie de soportes machihembrados a lo largo de los conjuntos de planos dados. Normalmente se usa…

### Biber › Utilities (3)

- [[Catálogo - Biber#Furring Strips in Rectangle (FSR)|Furring Strips in Rectangle (FSR)]] — Genera listones paralelos (furring strips) dentro del rectángulo indicado
- [[Catálogo - Biber#Futting Strips in Boundary (FSB)|Futting Strips in Boundary (FSB)]] — Genera listones paralelos (furring strips) dentro de una curva plana cerrada dada
- [[Catálogo - Biber#Slicer|Slicer]] — Genera un conjunto de planos paralelos copiando un plano de referencia a lo largo de una polisuperficie plana…

### Human › Reference (1)

- [[Catálogo - Human#Sort Objects By Type (SortByType)|Sort Objects By Type (SortByType)]] — Ordena un conjunto de objetos de Rhino por tipo y extrae la geometría de los tipos que ya existen en…

### Human › Texture Mapping (2)

- [[Catálogo - Human#CylinderMapping (CylinderMap)|CylinderMapping (CylinderMap)]] — Aplica un mapeo de textura cilíndrico a una malla
- [[Catálogo - Human#SphericalMapping (SphericalMap)|SphericalMapping (SphericalMap)]] — Aplica un mapeo de textura esférico a una malla

### LunchBox › Mass (4)

- [[Catálogo - LunchBox#Building Mass (Area Constrained) (Mass by Area)|Building Mass (Area Constrained) (Mass by Area)]] — Crea una masa de edificio rectangular restringida por un valor de área total
- [[Catálogo - LunchBox#Building Mass (Boundary and Area) (Mass Boundary Area)|Building Mass (Boundary and Area) (Mass Boundary Area)]] — Crea una masa de edificio a partir de una forma de contorno, restringida por el área total
- [[Catálogo - LunchBox#Building Mass (Boundary and Floors) (Mass Boundary Floors)|Building Mass (Boundary and Floors) (Mass Boundary Floors)]] — Crea una masa de edificio a partir de una forma de contorno, restringida por la cantidad de pisos
- [[Catálogo - LunchBox#Building Mass (Floor Count) (Mass by Floor)|Building Mass (Floor Count) (Mass by Floor)]] — Crea una masa de edificio rectangular a partir de la cantidad de pisos

### NGon › Subdivide (1)

- [[Catálogo - NGon#SortBrep|SortBrep]] — Ordena las caras del Brep si es posible

### NGon › Utilities Mesh (1)

- [[Catálogo - NGon#LoftCircles|LoftCircles]] — LoftCircles

### Parakeet › Surface (7)

- [[Catálogo - Parakeet#BooleanSplit|BooleanSplit]] — Divide un Brep con otro(s) Brep(s) [división Brep\|Brep]
- [[Catálogo - Parakeet#Brep join plus (Brep join +)|Brep join plus (Brep join +)]] — Une varios Breps que estén a menos de una distancia
- [[Catálogo - Parakeet#Brep Remove Holes (BrepRemoveHoles)|Brep Remove Holes (BrepRemoveHoles)]] — Quita los agujeros de un B-rep (funciona con superficies NURBS recortadas y sin recortar)
- [[Catálogo - Parakeet#Brep Topology|Brep Topology]] — Obtiene la topología completa de un Brep
- [[Catálogo - Parakeet#CreateSolid|CreateSolid]] — Crea un sólido (Brep cerrado) encerrado por superficies y polisuperficies que se intersectan
- [[Catálogo - Parakeet#Offset Brep (BrepOffset)|Offset Brep (BrepOffset)]] — Aplica offset a un Brep con parámetros variables
- [[Catálogo - Parakeet#Unjoin Brep Faces (Unjoin Brep)|Unjoin Brep Faces (Unjoin Brep)]] — Explota un Brep desde algunas aristas específicas

### Pufferfish › Surface (19)

- [[Catálogo - Pufferfish#Append Polysurfaces (AppPsrfs)|Append Polysurfaces (AppPsrfs)]] — Agrega un conjunto de polisuperficies (Breps) desconectadas para formar una sola polisuperficie (Brep)…
- [[Catálogo - Pufferfish#Automatic Edge Surface (AutoEdgSrf)|Automatic Edge Surface (AutoEdgSrf)]] — Crea una superficie entre 2, 3 o 4 curvas de borde ordenadas automáticamente
- [[Catálogo - Pufferfish#Extrude Tapered Polysurface (ExtrTaper)|Extrude Tapered Polysurface (ExtrTaper)]] — Extruye un perfil con conicidad según un ángulo de desmoldeo
- [[Catálogo - Pufferfish#Fit Surface (FitSrf)|Fit Surface (FitSrf)]] — Ajusta una nueva superficie a una superficie existente cuando es posible, sin cambiar la forma general…
- [[Catálogo - Pufferfish#Flip Polysurface (FlipPsrf)|Flip Polysurface (FlipPsrf)]] — Invierte las normales de una polisuperficie (Brep); las polisuperficies cerradas no se pueden invertir y…
- [[Catálogo - Pufferfish#Mesh To Polysurface (Msh2Psrf)|Mesh To Polysurface (Msh2Psrf)]] — Convierte una malla en una polisuperficie NURBS (Brep)
- [[Catálogo - Pufferfish#Mirror Cut Polysurface (MirCutPsrf)|Mirror Cut Polysurface (MirCutPsrf)]] — Corta una polisuperficie (Brep) con un plano, refleja el lado conservado del corte respecto de un plano de…
- [[Catálogo - Pufferfish#Mirror Cut Surface (MirCutSrf)|Mirror Cut Surface (MirCutSrf)]] — Corta una superficie con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo…
- [[Catálogo - Pufferfish#Offset Surface (OffSrf)|Offset Surface (OffSrf)]] — Aplica offset a una superficie, con la opción de hacerlo hacia ambos lados a distancias distintas y crear un…
- [[Catálogo - Pufferfish#Plane Trim Surface (PlnTrimSrf)|Plane Trim Surface (PlnTrimSrf)]] — Recorta (quita) las partes de una superficie que están a un lado de un plano; también funciona con…
- [[Catálogo - Pufferfish#Rebuild Surface (RebSrf)|Rebuild Surface (RebSrf)]] — Reconstruye una superficie con una cantidad de puntos, un grado y un dominio dados en las direcciones {u} y…
- [[Catálogo - Pufferfish#Remap Surface Domain² (ReSrfDom²)|Remap Surface Domain² (ReSrfDom²)]] — Reasigna el rango del dominio² {uv} de una superficie a un rango de entrada, con la opción de igualar el…
- [[Catálogo - Pufferfish#Reparameterize Surface (ReparamSrf)|Reparameterize Surface (ReparamSrf)]] — Reparametriza una superficie para que su dominio² (uv) vaya de 0 a 1; también funciona con superficies…
- [[Catálogo - Pufferfish#Shell Polysurface (ShellPsrf)|Shell Polysurface (ShellPsrf)]] — Crea un cascarón hueco con espesor a partir de una polisuperficie cerrada (Brep)
- [[Catálogo - Pufferfish#Shrink Trimmed Surface (ShrinkTrimSrf)|Shrink Trimmed Surface (ShrinkTrimSrf)]] — Encoge la superficie sin recortar subyacente de una superficie recortada para que quede lo más cerca posible…
- [[Catálogo - Pufferfish#Split Kinky Surface (SplitKinkySrf)|Split Kinky Surface (SplitKinkySrf)]] — Divide en una polisuperficie (Brep) la superficie de salida de un componente de superficie sin dividir, si…
- [[Catálogo - Pufferfish#Superimpose Surface (SuperSrf)|Superimpose Surface (SuperSrf)]] — Superpone la cantidad de puntos de control {uv}, el grado {uv}, el dominio {uv} y los recortes de una…
- [[Catálogo - Pufferfish#Swap Surface Directions (SwapSrfDir)|Swap Surface Directions (SwapSrfDir)]] — Intercambia o invierte las direcciones {u} y {v} de una superficie; también funciona con superficies…
- [[Catálogo - Pufferfish#Unroll Polysurface (UnrollPsrf)|Unroll Polysurface (UnrollPsrf)]] — Desenrolla una polisuperficie (Brep) para que sus caras queden planas sobre un plano, con la opción de…

<!-- AUTO:fin -->
