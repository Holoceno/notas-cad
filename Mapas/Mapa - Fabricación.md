---
tags: [tipo/mapa, fabricacion, fabricacion/cnc, fabricacion/nesting, fabricacion/uniones, fabricacion/impresion-3d, fabricacion/cam, software/grasshopper, plugin/opennest, plugin/biber]
---

# Fabricación

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

De la geometría a la máquina: **CNC** (router y láser), **nesting** (aprovechar planchas), **uniones** de carpintería digital, **impresión 3D** y, más adelante, **CAM** (trayectorias de herramienta). Es el puente con el plugin de muebles CNC y con los posibles negocios.

## CNC, nesting y uniones
- [[wiki/entities/opennest]]: nesting sobre planchas, separación, veta (rotaciones por pieza), Batch por mueble
- [[wiki/concepts/data-trees]]: cada pieza y sus atributos en ramas paralelas
- [[Nesting por franjas]]: piezas de alto constante → nesting 1D con cota inferior (más simple y demostrable que OpenNest)
- [[Recortar piezas con un contorno]]: quedarse con lo de adentro y fillet solo en las esquinas cortadas
- [[Ramas paralelas por pieza]]: contorno, rótulo, pliegue y flocks con la misma ruta, por color y por placa
- Uniones: Biber ([[Catálogo - Biber#Finger Joint (FJ)|Finger Joint]], [[Catálogo - Biber#Dovetail Joint (DVTJ)|Dovetail Joint]], [[Catálogo - Biber#Half-lap Joint (HLJ)|Half-lap Joint]], [[Catálogo - Biber#Tongue & Groove Joint (TAGJ)|Tongue & Groove Joint]]), NGon ([[Catálogo - NGon#Finger|Finger]]) y ranuras encastrables ([[Catálogo - Params#Region Slits (RSlits)|Region Slits]]).
- Contornos y offsets de herramienta: [[Catálogo - Intersect#Contour|Contour]], [[Catálogo - Curve#Offset Curve (Offset)|Offset Curve]], [[Catálogo - Params#Simplify|Simplify]]
- Grabado de nombres: [[Catálogo - Params#Text|Text]] (OpenNest) · desenrollar: [[Catálogo - Params#Unroll|Unroll]]
- Por código (Python y C#): desarrollar (**Unroll Surface**), cortar con planos (**Split BReps with Planes**), medir piezas (**Tight Bounding Boxes for Breps**): tabla *Muestras de RhinoCommon*, más abajo

## Impresión 3D
- Llenar la cama con varias piezas: [[Catálogo - Params#OpenNest3D|OpenNest3D]]

## CAM (pendiente)
Trayectorias, postprocesadores y simulación de mecanizado: todavía sin notas. Cuando empiece, crear aquí la primera nota y etiquetarla `#fabricacion/cam`.

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Secciones cada N mm | [[Catálogo - Intersect#Contour\|Contour]] | `rg.Brep.CreateContourCurves(brep, p0, p1, n)` | `.section(altura)` |
| Offset de herramienta | [[Catálogo - Curve#Offset Curve (Offset)\|Offset Curve]] | `crv.Offset(plano, d, tol, rg.CurveOffsetCornerStyle.Sharp)` | `wire.offset2D(d)` |
| Desenrollar | [[Catálogo - Params#Unroll\|Unroll]] | `rg.Unroller(brep).PerformUnroll()` | — |
| Exportar para cortar o imprimir | — | `doc.ExportSelected(ruta)` | `cq.exporters.export(pieza, "pieza.dxf")` / `"pieza.stl"` |

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (7)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Create Contour Curves | [[Create Contour Curves\|Py]] · [[Create Contour Curves (cs)\|C#]] | Curvas de contorno (cortes paralelos) de Breps y mallas | `Brep.CreateContourCurves / Mesh.CreateContourCurves` |
| Mesh Volume | [[Mesh Volume\|Py]] · [[Mesh Volume (cs)\|C#]] | Volumen de mallas cerradas (material de una impresión 3D) | `VolumeMassProperties.Compute(malla).Volume` |
| Offset Curve | [[Offset Curve\|Py]] · [[Offset Curve (cs)\|C#]] | Copia paralela de una curva hacia un lado (compensación de herramienta) | `Curve.Offset(punto, normal, distancia, tol, esquinas)` |
| Split BReps with Planes | [[Split BReps with Planes\|Py]] · [[Split BReps with Planes (cs)\|C#]] | Corta Breps con un plano | `PlaneSurface.CreateThroughBox → Brep.Split(cortador, tol)` |
| Tight Bounding Boxes for Breps | [[Tight Bounding Boxes for Breps\|Py]] · [[Tight Bounding Boxes for Breps (cs)\|C#]] | Cajas contenedoras ajustadas de las partes de una superficie cortada | `BrepFace.Split → Mesh.CreateFromBrep → GetBoundingBox` |
| Unroll Surface | [[Unroll Surface\|Py]] · [[Unroll Surface (cs)\|C#]] | Desarrolla una superficie desarrollable junto con curvas y puntos asociados | `Unroller(brep).PerformUnroll()` |
| Unroll Surface and Mesh | [[Unroll Surface and Mesh\|Py]] · [[Unroll Surface and Mesh (cs)\|C#]] | Desarrolla una superficie y lleva su malla al plano | `Unroller.AddFollowingGeometry(puntos) → PerformUnroll` |

## Componentes de Grasshopper (149)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › OpenNest2 (23)

- [[Catálogo - Params#Bounding Box Edges (BBoxEdges)|Bounding Box Edges (BBoxEdges)]] — Devuelve las dos aristas base de la caja contenedora orientada de un objeto y sus longitudes
- [[Catálogo - Params#Box Packing (PackBox)|Box Packing (PackBox)]] — Empaqueta cajas 3D dentro de un contenedor
- [[Catálogo - Params#Geometry|Geometry]] — Prepara piezas para el anidado (nesting): separa los contornos (con agujeros) de los atributos adjuntos…
- [[Catálogo - Params#Geometry (Rhino) (Geometry Rhino)|Geometry (Rhino) (Geometry Rhino)]] — Construye piezas para anidar a partir de objetos de Rhino referenciados, separando los contornos de los…
- [[Catálogo - Params#Geometry (Surfaces) (Geometry Srf)|Geometry (Surfaces) (Geometry Srf)]] — Construye piezas para anidar a partir de superficies planas en vez de curvas; los agujeros se leen de los…
- [[Catálogo - Params#Inscribed Circle (InscribeCircle)|Inscribed Circle (InscribeCircle)]] — Busca el círculo más grande que cabe dentro de cada polilínea cerrada
- [[Catálogo - Params#Merge|Merge]] — Combina dos flujos de geometría de OpenNest en uno
- [[Catálogo - Params#NestOptions|NestOptions]] — Construye los textos de opciones para un solver de anidado. Solver = -1 (Auto, por defecto) sigue al solver…
- [[Catálogo - Params#OpenNest1|OpenNest1]] — Anida curvas/superficies SIN PROCESAR sobre planchas con el solver de no-fit-polygon (sin componente Geometry…
- [[Catálogo - Params#OpenNest2|OpenNest2]] — Anida piezas sobre planchas con el solver genético de no-fit-polygon, conservando los atributos de cada…
- [[Catálogo - Params#OpenNest3D|OpenNest3D]] — Anidado 3D malla-malla (empaquetado espectral / FFT). Empaqueta mallas dentro de una caja contenedora
- [[Catálogo - Params#OpenNestCollision|OpenNestCollision]] — Anida piezas sobre planchas con el solver de colisión física: empaqueta de forma apretada y puede rellenar…
- [[Catálogo - Params#Pack Objects (Pack)|Pack Objects (Pack)]] — Dispone objetos en una fila, orientando cada uno de 3D a 2D con la separación elegida
- [[Catálogo - Params#Principal Component Analysis (PCA)|Principal Component Analysis (PCA)]] — Caja contenedora orientada, alineada con las aristas de la pieza: un rectángulo de área mínima para conjuntos…
- [[Catálogo - Params#Project to Plane (Project)|Project to Plane (Project)]] — Proyecta una polilínea sobre su plano de mejor ajuste y devuelve ese plano
- [[Catálogo - Params#Region Slits (RSlits)|Region Slits (RSlits)]] — Corta ranuras de encaje donde se encuentran regiones planas (una versión corregida del componente nativo)
- [[Catálogo - Params#Rhino Objects (RhinoObjects)|Rhino Objects (RhinoObjects)]] — Lee objetos de Rhino referenciados, con atributos como texto, y los convierte en Breps planos para el anidado
- [[Catálogo - Params#Sheets|Sheets]] — Define las planchas sobre las que anidar (con agujeros opcionales) a partir de polilíneas cerradas; admite…
- [[Catálogo - Params#Sheets (Surfaces) (Sheets Srf)|Sheets (Surfaces) (Sheets Srf)]] — Define las planchas sobre las que anidar a partir de superficies planas en vez de polilíneas; los agujeros…
- [[Catálogo - Params#Simplify|Simplify]] — Reduce la cantidad de vértices de una curva cerrada, aplicando automáticamente hacia afuera el offset justo…
- [[Catálogo - Params#Text|Text]] — Construye contornos de texto como curvas para corte láser o fresado
- [[Catálogo - Params#Transform Object (TGuid)|Transform Object (TGuid)]] — Transforma un objeto de Rhino referenciado en su lugar, conservando todas sus propiedades
- [[Catálogo - Params#Unroll|Unroll]] — Desenrolla un Brep o malla desarrollable a plano, llevando consigo sus curvas, puntos y textos

### Biber › Assemble Tools (11)

- [[Catálogo - Biber#Assemble (DM)|Assemble (DM)]] — Toma una polisuperficie poligonal de entrada y crea un ensamble a partir de sus polígonos planos. Las caras y…
- [[Catálogo - Biber#Breps to PPS (BTPPS)|Breps to PPS (BTPPS)]] — Convierte un conjunto de breps planos que se intersectan en una PPS (Planar Poly-Surface) que se puede usar…
- [[Catálogo - Biber#Disassemble (D)|Disassemble (D)]] — Explota un ensamble en sus componentes (Shells, Joints y Node). Cada uno de estos subcomponentes puede tener…
- [[Catálogo - Biber#Disassemble Joint (Joint)|Disassemble Joint (Joint)]] — Obtiene la información de los elementos Shell, como objetos sólidos, superficies, etc
- [[Catálogo - Biber#Disassemble Node (Node)|Disassemble Node (Node)]] — Obtiene la información de los elementos Node, como objetos sólidos, superficies, índices, etc
- [[Catálogo - Biber#Disassemble Shell (Shell)|Disassemble Shell (Shell)]] — Obtiene la información de los elementos Shell: índice del shell e índices de aristas y nodos
- [[Catálogo - Biber#Fillet Shell Edges (FSE)|Fillet Shell Edges (FSE)]] — Aplica fillet a las aristas del shell según su tipo. Las aristas convexas/cóncavas y de superficie se pueden…
- [[Catálogo - Biber#Merge PPS (M.P.P.S)|Merge PPS (M.P.P.S)]] — Fusiona varias PPS (Planar Poly-Surface) en una sola PPS
- [[Catálogo - Biber#Mesh to PPS (MTPPS)|Mesh to PPS (MTPPS)]] — Convierte una malla en una PPS (Planar Poly-Surface) que se puede usar para crear un ensamble
- [[Catálogo - Biber#Shell Geometry (SG)|Shell Geometry (SG)]] — Construye la geometría del shell y algunos objetos auxiliares para el proceso de fresado
- [[Catálogo - Biber#Sub-PPS (SPPS)|Sub-PPS (SPPS)]] — Crea una PPS (Planar Poly-Surface) parcial a partir de los componentes de otra PPS

### Biber › Joints (27)

- [[Catálogo - Biber#Add feature (A.F.)|Add feature (A.F.)]] — Agrega una serie de elementos (features) en la pieza objetivo a lo largo del joint, transformando la…
- [[Catálogo - Biber#Add feature (A.F.) · 2|Add feature (A.F.) · 2]] — Agrega elementos (features) al joint. Un elemento puede ser una cavidad, una adición o un accesorio
- [[Catálogo - Biber#Barefaced Housing Joint (BHJ)|Barefaced Housing Joint (BHJ)]] — Crea un joint de alojamiento a cara vista (barefaced housing) a lo largo de la arista, en aristas manifold y…
- [[Catálogo - Biber#Blind Finger Joint (BFJ)|Blind Finger Joint (BFJ)]] — Crea una unión de dedos ciega (blind finger joint)
- [[Catálogo - Biber#Butt Joint (BJ)|Butt Joint (BJ)]] — Crea una unión a tope (butt joint) a lo largo de la arista, en aristas manifold y no manifold. La unión a…
- [[Catálogo - Biber#Butt Rub Joint (BRJ)|Butt Rub Joint (BRJ)]] — Crea una unión a tope con refuerzo (butt rub joint) a lo largo de la arista, en aristas manifold y no…
- [[Catálogo - Biber#Custom Profile Joint (CPJ)|Custom Profile Joint (CPJ)]] — Ofrece opciones para crear un perfil personalizado a lo largo de las aristas manifold
- [[Catálogo - Biber#Dovetail Joint (DVTJ)|Dovetail Joint (DVTJ)]] — Crea una unión de cola de milano (dovetail) a lo largo de la arista. Este joint solo se puede usar en aristas…
- [[Catálogo - Biber#Dovetail Joint Settings (DTS)|Dovetail Joint Settings (DTS)]] — Entrega todos los ajustes de la unión de cola de milano
- [[Catálogo - Biber#Dowel Butt Joint (DBJ)|Dowel Butt Joint (DBJ)]] — La unión con tarugos se arma igual que una unión atornillada, solo que en vez de tornillos se pegan trozos de…
- [[Catálogo - Biber#Feature (F.)|Feature (F.)]] — Define un elemento (feature) de un joint. Un elemento puede ser aditivo, sustractivo o un accesorio. Un joint…
- [[Catálogo - Biber#Finger Joint (FJ)|Finger Joint (FJ)]] — Crea una unión de dedos (finger joint)
- [[Catálogo - Biber#Half-lap Joint (HLJ)|Half-lap Joint (HLJ)]] — Crea una unión a media madera (half-lap) a lo largo de la arista, en aristas manifold y no manifold
- [[Catálogo - Biber#Keyed Mitered Joint (KMJ)|Keyed Mitered Joint (KMJ)]] — Crea una unión a inglete con llave (keyed miter) a lo largo de la arista. Este joint solo se puede usar en…
- [[Catálogo - Biber#Lap Joint (LJ)|Lap Joint (LJ)]] — Crea una unión a solape (lap joint) a lo largo de la arista, en aristas manifold y no manifold
- [[Catálogo - Biber#Lap Mitered Joint (LMJ)|Lap Mitered Joint (LMJ)]] — Crea una unión a solape con inglete (lap-mitered) a lo largo de la arista. Este joint solo se puede usar en…
- [[Catálogo - Biber#Lock Mitered Joint (LMJ)|Lock Mitered Joint (LMJ)]] — Crea una unión a inglete con traba (lock miter) a lo largo de la arista. Este joint solo se puede usar en…
- [[Catálogo - Biber#Mitered Joint (MJ)|Mitered Joint (MJ)]] — Unión a inglete
- [[Catálogo - Biber#Mitered Lap Joint (MLJ)|Mitered Lap Joint (MLJ)]] — Crea una unión a inglete con solape (mitered lap) a lo largo de la arista. Este joint solo se puede usar en…
- [[Catálogo - Biber#Null Shape (Nseg)|Null Shape (Nseg)]] — Crea una forma nula
- [[Catálogo - Biber#Open Joint (OJ)|Open Joint (OJ)]] — Alinea la cara de las aristas abiertas con el plano de entrada
- [[Catálogo - Biber#Simplified Mitered Joint (default) (SMJ)|Simplified Mitered Joint (default) (SMJ)]] — Una versión simple de la unión a inglete, sin variaciones. Todos los shells se encuentran en el centro de la…
- [[Catálogo - Biber#Splined Miter Joint (SMJ)|Splined Miter Joint (SMJ)]] — Unión a inglete con lengüeta (splined miter)
- [[Catálogo - Biber#Tongue & Groove Joint (TAGJ)|Tongue & Groove Joint (TAGJ)]] — Crea una unión machihembrada (tongue & groove) a lo largo de la arista, en aristas manifold y no manifold
- [[Catálogo - Biber#U Shape (Useg)|U Shape (Useg)]] — Crea una forma de U con esquinas redondeadas
- [[Catálogo - Biber#User defined profile segment (UDPS)|User defined profile segment (UDPS)]] — Un segmento de perfil personalizado definido por una curva plana en el plano XY. La curva de entrada debe…
- [[Catálogo - Biber#Waffle Joint (WJ)|Waffle Joint (WJ)]] — Crea una unión tipo waffle entre shells coplanares que se intersectan

### Biber › Material Library (5)

- [[Catálogo - Biber#Birch Multiplex|Birch Multiplex]]
- [[Catálogo - Biber#Blockboard light-core|Blockboard light-core]] — Bla bla bla
- [[Catálogo - Biber#Maritime Pine Plywood|Maritime Pine Plywood]] — Bla bla bla
- [[Catálogo - Biber#Poplar Plywood|Poplar Plywood]] — Bla bla bla
- [[Catálogo - Biber#Tischlerplatte Pappel|Tischlerplatte Pappel]]

### Biber › Nodes (5)

- [[Catálogo - Biber#Coarse Node (CN)|Coarse Node (CN)]] — Resuelve la intersección de los elementos shell recortando cada pieza con la opuesta. Esto puede dejar…
- [[Catálogo - Biber#Multi-trims Node (MTN)|Multi-trims Node (MTN)]] — Resuelve la intersección de los elementos shell con varias operaciones de recorte entre cada par de shells…
- [[Catálogo - Biber#Null Node (default) (NN)|Null Node (default) (NN)]] — Un nodo nulo no hace nada y deja el vértice sin tratar. Usa este componente en los vértices con menos de 3…
- [[Catálogo - Biber#Overlap Killer Node (O.K.N.)|Overlap Killer Node (O.K.N.)]] — Solo resuelve las esquinas superpuestas cuando una de las piezas tiene un ángulo llano o reflejo en la esquina
- [[Catálogo - Biber#Single-trim Node (STN)|Single-trim Node (STN)]] — Resuelve la intersección de los elementos shell con una sola operación de recorte en cada shell que se…

### Biber › Optimization (7)

- [[Catálogo - Biber#Check Size (CS)|Check Size (CS)]] — Revisa el tamaño de los shells de un ensamble e informa si algún shell no se puede obtener de la plancha de…
- [[Catálogo - Biber#Fixed Constrain (FC)|Fixed Constrain (FC)]] — Fija los vértices de la malla en su lugar durante la optimización de planaridad
- [[Catálogo - Biber#Linear Constrain (LC)|Linear Constrain (LC)]] — Fija los vértices de la malla sobre una línea durante la optimización de planaridad
- [[Catálogo - Biber#Optimize for Planarity (Solver)|Optimize for Planarity (Solver)]] — Mueve los vértices de la malla para que todas las celdas queden planas
- [[Catálogo - Biber#Plane Constrain (PC)|Plane Constrain (PC)]] — Fija los vértices de la malla sobre un plano durante la optimización de planaridad
- [[Catálogo - Biber#Simplify Mesh (SM)|Simplify Mesh (SM)]] — Toma una malla de entrada y la simplifica soldando sus vértices, fusionando las caras coplanares y eliminando…
- [[Catálogo - Biber#Split Polygon by Angle (SPA)|Split Polygon by Angle (SPA)]] — Divide los polígonos en los vértices con un ángulo mayor que el umbral de entrada. El polígono se divide…

### Biber › Parameters (10)

- [[Catálogo - Biber#Assembly (parámetro)|Assembly (parámetro)]] — Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de…
- [[Catálogo - Biber#Joint (J, parámetro)|Joint (J, parámetro)]] — Un joint contiene la geometría creada a lo largo de las aristas de las piezas (si existe), además de…
- [[Catálogo - Biber#Joint type (jt, parámetro)|Joint type (jt, parámetro)]] — Define cómo se tratan varias piezas a lo largo de una arista común
- [[Catálogo - Biber#Material (M, parámetro)|Material (M, parámetro)]] — Un conjunto de propiedades que definen el material de una pieza
- [[Catálogo - Biber#Mesh Constrain (Constrain, parámetro)|Mesh Constrain (Constrain, parámetro)]] — Una restricción usada en la optimización de mallas. Con restricciones puedes fijar vértices en su lugar…
- [[Catálogo - Biber#Node (N, parámetro)|Node (N, parámetro)]] — Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para…
- [[Catálogo - Biber#Node type (Nt, parámetro)|Node type (Nt, parámetro)]] — Define cómo se tratan varias piezas alrededor de un nodo común
- [[Catálogo - Biber#Part (P, parámetro)|Part (P, parámetro)]] — Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional…
- [[Catálogo - Biber#Planar Polysurface (PPS, parámetro)|Planar Polysurface (PPS, parámetro)]] — Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica…
- [[Catálogo - Biber#Shell type (St, parámetro)|Shell type (St, parámetro)]] — Define cómo se crea una pieza a partir de una superficie plana. Una pieza puede ubicarse arriba, al medio o…

### Biber › PPS Tools (31)

- [[Catálogo - Biber#Edge Labeling (EL)|Edge Labeling (EL)]] — Etiqueta las aristas de una malla poligonal
- [[Catálogo - Biber#Edge Selection (ES)|Edge Selection (ES)]] — Selecciona aristas de una PPS desde la vista previa de Grasshopper
- [[Catálogo - Biber#Filter Edge by Number of Connected Polgons (FEBNP)|Filter Edge by Number of Connected Polgons (FEBNP)]] — Devuelve los números de las aristas de la malla poligonal donde la cantidad de polígonos conectados está…
- [[Catálogo - Biber#Filter Edges by Angle (FEBA)|Filter Edges by Angle (FEBA)]] — Devuelve los números de las aristas de la malla donde el ángulo entre las dos caras conectadas está dentro…
- [[Catálogo - Biber#Filter Edges by Attributes (FEBA)|Filter Edges by Attributes (FEBA)]] — Busca las aristas usando el par clave-valor definido en los atributos de usuario de los objetos brep
- [[Catálogo - Biber#Filter Edges by Box (F.E.Box.)|Filter Edges by Box (F.E.Box.)]] — Entrega los índices de las aristas que están dentro de la caja contenedora
- [[Catálogo - Biber#Filter Edges by Length (FEBL)|Filter Edges by Length (FEBL)]] — Devuelve los números de las aristas de la PPS cuya longitud está dentro del rango indicado
- [[Catálogo - Biber#Filter Edges by Polygons (FEBP)|Filter Edges by Polygons (FEBP)]] — Devuelve los números de las aristas de la malla poligonal que se comparten con alguno de los polígonos…
- [[Catálogo - Biber#Filter Edges by Vertex (FEBV)|Filter Edges by Vertex (FEBV)]] — Devuelve los números de las aristas de la malla poligonal que se comparten con alguno de los vértices…
- [[Catálogo - Biber#Filter Edges within a Plane (FEBP)|Filter Edges within a Plane (FEBP)]] — Filtra las aristas que están dentro de un plano dado. Se usa la tolerancia de proximidad de la PPS para…
- [[Catálogo - Biber#Filter Manifold Edges (FME)|Filter Manifold Edges (FME)]] — Filtra las aristas con dos caras conectadas en que ambas caras están orientadas en la misma dirección
- [[Catálogo - Biber#Filter Open Edges (FOE)|Filter Open Edges (FOE)]] — Filtra las aristas que tienen una sola cara
- [[Catálogo - Biber#Filter Planar Polygons (FPP)|Filter Planar Polygons (FPP)]] — Busca los polígonos coplanares con los polígonos indicados
- [[Catálogo - Biber#Filter Polygons by Area (FPBA)|Filter Polygons by Area (FPBA)]] — Filtra los Ngons planos cuya área está dentro del rango indicado
- [[Catálogo - Biber#Filter Polygons by Attributes (FPBA)|Filter Polygons by Attributes (FPBA)]] — Busca los polígonos usando el par clave-valor definido en los atributos de usuario
- [[Catálogo - Biber#Filter Polygons by Box (F.P.Box.)|Filter Polygons by Box (F.P.Box.)]] — Filtra los polígonos que están dentro de la caja contenedora indicada
- [[Catálogo - Biber#Filter Polygons by Edge (FPBE)|Filter Polygons by Edge (FPBE)]] — Busca los polígonos que contienen al menos una de las aristas indicadas
- [[Catálogo - Biber#Filter Polygons by Plane (FPBP)|Filter Polygons by Plane (FPBP)]] — Calcula los ángulos entre el plano del polígono de la malla y un plano dado. El filtro deja pasar el índice…
- [[Catálogo - Biber#Filter Polygons by Vertices (FPBV)|Filter Polygons by Vertices (FPBV)]] — Busca los polígonos que contienen al menos un vértice de la lista de vértices de entrada
- [[Catálogo - Biber#Filter Vertices by Box (F.V.Box.)|Filter Vertices by Box (F.V.Box.)]] — Filtra los vértices que están dentro de una caja contenedora dada
- [[Catálogo - Biber#Filter Vertices by Edges (FVBE)|Filter Vertices by Edges (FVBE)]] — Filtra los vértices de la arista indicada
- [[Catálogo - Biber#Filter Vertices by Polygon (FVBP)|Filter Vertices by Polygon (FVBP)]] — Filtra los vértices de los polígonos indicados
- [[Catálogo - Biber#Filter Vertices by Proximity (FVP)|Filter Vertices by Proximity (FVP)]] — Filtra los vértices que están dentro de una tolerancia dada respecto de un conjunto de puntos
- [[Catálogo - Biber#Invert Filter (INV)|Invert Filter (INV)]] — Invierte los elementos filtrados
- [[Catálogo - Biber#Polygon Labeling (PL)|Polygon Labeling (PL)]] — Etiqueta los polígonos planos de una malla poligonal
- [[Catálogo - Biber#Polygon Selection (PS)|Polygon Selection (PS)]] — Selecciona polígonos de una PPS desde la vista previa de Grasshopper
- [[Catálogo - Biber#PPS Edge (E)|PPS Edge (E)]] — Extrae información de las aristas de una polisuperficie plana
- [[Catálogo - Biber#PPS Polygon (V)|PPS Polygon (V)]] — Extrae información de los polígonos de una polisuperficie plana
- [[Catálogo - Biber#PPS Vertex (V)|PPS Vertex (V)]] — Extrae información de los vértices de una polisuperficie plana
- [[Catálogo - Biber#Vertex Labeling (VL)|Vertex Labeling (VL)]] — Etiqueta los vértices de una malla poligonal
- [[Catálogo - Biber#Vertex Selection (VS)|Vertex Selection (VS)]] — Selecciona vértices de una PPS desde la vista previa de Grasshopper

### Biber › Shells (3)

- [[Catálogo - Biber#Negative Shell (default) (NS)|Negative Shell (default) (NS)]] — Todo el shell se crea en el lado negativo de la cara (polígono). El lado negativo de la cara es el opuesto a…
- [[Catálogo - Biber#Positive Shell (PS)|Positive Shell (PS)]] — Todo el shell se crea en el lado positivo de la cara (polígono). El lado positivo de la cara es hacia donde…
- [[Catálogo - Biber#Symmetric Shell (SS)|Symmetric Shell (SS)]] — El shell se crea de forma simétrica a ambos lados de la cara de la malla (polígono)

### Biber › Simulation (2)

- [[Catálogo - Biber#Assembly Sequence Generator (ASG)|Assembly Sequence Generator (ASG)]] — Entrega la primera secuencia posible, a partir del índice de shell indicado, en la que se puede armar el…
- [[Catálogo - Biber#Assembly Simulation (AS)|Assembly Simulation (AS)]] — Muestra la secuencia de un ensamble colocando cada pieza en su posición en el orden y la dirección correctos

### Biber › Sub-Structure (12)

- [[Catálogo - Biber#Construct (Type 4) 3D Connector (3DC)|Construct (Type 4) 3D Connector (3DC)]] — Este conector crea una geometría guía a lo largo de las aristas para ayudar a colocar los marcos a ambos…
- [[Catálogo - Biber#Construct 2D Connector (2DC)|Construct 2D Connector (2DC)]] — Construye un conector 2D: una geometría guía en cada esquina de la pieza que conecta dos marcos adyacentes.…
- [[Catálogo - Biber#Construct Edge Support (CES)|Construct Edge Support (CES)]] — Define los ajustes de un soporte en forma de "V" perpendicular a la arista del ensamble, que sostiene los…
- [[Catálogo - Biber#Construct Frame (F)|Construct Frame (F)]] — Un marco que sostiene los shells a lo largo de las aristas
- [[Catálogo - Biber#Deconstruct 2D Connector (2DC)|Deconstruct 2D Connector (2DC)]] — Conecta dos shells adyacentes cerca de la ubicación del nodo
- [[Catálogo - Biber#Deconstruct 3D Connector (3DC)|Deconstruct 3D Connector (3DC)]] — Conecta dos shells adyacentes cerca de la ubicación del nodo
- [[Catálogo - Biber#Deconstruct Edge Support (DCES)|Deconstruct Edge Support (DCES)]] — Descompone los soportes de arista generados por el Edge Support System en sus subcomponentes (geometría…
- [[Catálogo - Biber#Deconstruct Frame (F)|Deconstruct Frame (F)]] — Un marco que sostiene los shells a lo largo de las aristas
- [[Catálogo - Biber#Edge Support System (ESS)|Edge Support System (ESS)]] — Da soporte a las piezas a lo largo de las aristas del ensamble
- [[Catálogo - Biber#Nodal Support Structure (NSS)|Nodal Support Structure (NSS)]] — Da soporte a los shells en los elementos joint
- [[Catálogo - Biber#Tongue And Groove System (TGS)|Tongue And Groove System (TGS)]] — Crea una serie de soportes machihembrados a lo largo de los conjuntos de planos dados. Normalmente se usa…
- [[Catálogo - Biber#Waffle Grid 1 (WG1)|Waffle Grid 1 (WG1)]] — Crea una estructura tipo waffle a partir de un conjunto de superficies planas que se intersectan

### Biber › Utilities (5)

- [[Catálogo - Biber#Add Shape (AS)|Add Shape (AS)]] — Extrae la porción de la forma plana que queda dentro de la superficie superior del shell
- [[Catálogo - Biber#Edge marker (E.M.)|Edge marker (E.M.)]] — Marca las aristas en su punto medio para que las piezas se puedan alinear al ensamblarlas
- [[Catálogo - Biber#Furring Strips in Rectangle (FSR)|Furring Strips in Rectangle (FSR)]] — Genera listones paralelos (furring strips) dentro del rectángulo indicado
- [[Catálogo - Biber#Futting Strips in Boundary (FSB)|Futting Strips in Boundary (FSB)]] — Genera listones paralelos (furring strips) dentro de una curva plana cerrada dada
- [[Catálogo - Biber#Slicer|Slicer]] — Genera un conjunto de planos paralelos copiando un plano de referencia a lo largo de una polisuperficie plana…

### Kangaroo2 › Mesh (1)

- [[Catálogo - Kangaroo2#Unroller|Unroller]] — Desenrolla una franja de cuadriláteros

### LunchBox › Util (1)

- [[Catálogo - LunchBox#Unroll Brep (Unroll)|Unroll Brep (Unroll)]] — Desenrolla un brep o una superficie

### NGon › Joint (4)

- [[Catálogo - NGon#Finger|Finger]] — Dedo en el plano
- [[Catálogo - NGon#JointsVDA|JointsVDA]] — JointsVDA
- [[Catálogo - NGon#MeshCollision (MC)|MeshCollision (MC)]] — MeshCollision
- [[Catálogo - NGon#MeshFlap|MeshFlap]] — MeshFlap

### Parakeet › Util (1)

- [[Catálogo - Parakeet#Pack Curves (PackCrv)|Pack Curves (PackCrv)]] — Empaqueta curvas sobre el plano XY (nesting simple)

### Pufferfish › Surface (1)

- [[Catálogo - Pufferfish#Unroll Polysurface (UnrollPsrf)|Unroll Polysurface (UnrollPsrf)]] — Desenrolla una polisuperficie (Brep) para que sus caras queden planas sobre un plano, con la opción de…

<!-- AUTO:fin -->
