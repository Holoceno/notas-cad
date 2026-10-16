---
tags: [tipo/mapa, geometria/puntos-vectores, matematicas/vectores, software/grasshopper, software/rhinocommon, software/cadquery]
---

# Puntos, vectores y planos

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Lo más básico de la geometría computacional: puntos (posiciones), vectores (direcciones con largo) y planos (origen + ejes, el "sistema de coordenadas local" de casi todo). También grillas, campos vectoriales y búsquedas de cercanía.

## Teoría y código
- [[wiki/concepts/vector-mathematics]]: suma, producto escalar y vectorial, línea y plano
- [[wiki/concepts/transformaciones-geometricas]] · [[wiki/sources/2026-05-03-matematicas-vectoriales]]
- [[wiki/sources/2026-05-04-rhinopy-operaciones-espaciales]]: RTree para buscar puntos cercanos rápido

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Punto | [[Catálogo - Vector#Construct Point (Pt)\|Construct Point]] | `rg.Point3d(x, y, z)` | `cq.Vector(x, y, z)` |
| Vector entre dos puntos | [[Catálogo - Vector#Vector 2Pt (Vec2Pt)\|Vector 2Pt]] | `b - a` | `b - a` |
| Vector unitario | [[Catálogo - Vector#Unit Vector (Unit)\|Unit Vector]] | `v.Unitize()` (modifica `v`) | `v.normalized()` |
| Producto escalar / vectorial | [[Catálogo - Vector#Dot Product (DProd)\|Dot]] / [[Catálogo - Vector#Cross Product (XProd)\|Cross]] | `a * b` / `rg.Vector3d.CrossProduct(a, b)` | `a.dot(b)` / `a.cross(b)` |
| Distancia | [[Catálogo - Vector#Distance (Dist)\|Distance]] | `a.DistanceTo(b)` | `(a - b).Length` |
| Plano por origen y ejes | [[Catálogo - Vector#Construct Plane (Pl)\|Construct Plane]] | `rg.Plane(origen, eje_x, eje_y)` | `cq.Plane(origen, xDir, normal)` |
| Plano por 3 puntos | [[Catálogo - Vector#Plane 3Pt (Pl 3Pt)\|Plane 3Pt]] | `rg.Plane(a, b, c)` | — |
| Punto más cercano de una nube | [[Catálogo - Vector#Closest Point (CP)\|Closest Point]] | `rg.RTree.Point3dClosestPoints(...)` | — |

## Para empezar
[[Catálogo - Vector#Construct Point (Pt)|Construct Point]] · [[Catálogo - Vector#Deconstruct (pDecon)|Deconstruct]] · [[Catálogo - Vector#Vector 2Pt (Vec2Pt)|Vector 2Pt]] · [[Catálogo - Vector#Amplitude (Amp)|Amplitude]] · [[Catálogo - Vector#Construct Plane (Pl)|Construct Plane]] · [[Catálogo - Vector#Deconstruct Plane (DePlane)|Deconstruct Plane]] · [[Catálogo - Vector#Closest Point (CP)|Closest Point]] · [[Catálogo - Vector#Populate 2D (Pop2D)|Populate 2D]] · [[Catálogo - Vector#Hexagonal (HexGrid)|Hexagonal]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (6)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Array Points on Surface | [[Array Points on Surface\|Py]] | Grilla de puntos sobre una superficie (filas × columnas) | `rs.SurfaceDomain, rs.EvaluateSurface` |
| Closest Point Calculation with RTree | [[Closest Point Calculation with RTree\|Py]] · [[Closest Point Calculation with RTree (cs)\|C#]] | Vértice más cercano de una malla con un RTree (búsqueda rápida) | `RTree.Insert, RTree.Search(esfera, callback)` |
| Move CPlane | [[Move CPlane\|Py]] · [[Move CPlane (cs)\|C#]] | Mueve el plano de construcción con vista previa | `Viewport.GetConstructionPlane / SetConstructionPlane` |
| Move Points | [[Move Points\|Py]] · [[Move Points (cs)\|C#]] | Mueve puntos de un lugar a otro | `Transform.Translation → doc.Objects.Transform` |
| Move Points Non Uniform | [[Move Points Non Uniform\|Py]] · [[Move Points Non Uniform (cs)\|C#]] | Mueve puntos sumando a cada coordenada | `doc.Objects.Replace(objRef, punto)` |
| Pick Point | [[Pick Point\|Py]] · [[Pick Point (cs)\|C#]] | Pide un punto o selecciona objetos punto | `GetPoint / GetObject con ObjectType.Point` |

## Componentes de Grasshopper (139)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (5)

- [[Catálogo - Params#Field (parámetro)|Field (parámetro)]] — Contiene una colección de campos vectoriales
- [[Catálogo - Params#Plane (Pln, parámetro)|Plane (Pln, parámetro)]] — Contiene una colección de sistemas de ejes tridimensionales
- [[Catálogo - Params#Point (Pt, parámetro)|Point (Pt, parámetro)]] — Contiene una colección de puntos tridimensionales
- [[Catálogo - Params#Point Cloud (PCloud, parámetro)|Point Cloud (PCloud, parámetro)]] — Contiene una colección de nubes de puntos
- [[Catálogo - Params#Vector (Vec, parámetro)|Vector (Vec, parámetro)]] — Contiene una colección de vectores tridimensionales

### Vector › Field (12)

- [[Catálogo - Vector#Break Field (BreakF)|Break Field (BreakF)]] — Separa un campo en sus elementos individuales
- [[Catálogo - Vector#Direction Display (FDir)|Direction Display (FDir)]] — Muestra las direcciones de fuerza de una sección de un campo
- [[Catálogo - Vector#Evaluate Field (EvF)|Evaluate Field (EvF)]] — Evalúa un campo en un punto
- [[Catálogo - Vector#Field Line (FLine)|Field Line (FLine)]] — Calcula la línea de campo que pasa por cierto punto
- [[Catálogo - Vector#Line Charge (LCharge)|Line Charge (LCharge)]] — Crea un campo generado por una carga lineal
- [[Catálogo - Vector#Merge Fields (MergeF)|Merge Fields (MergeF)]] — Fusiona una colección de campos en uno
- [[Catálogo - Vector#Perpendicular Display (FPerp)|Perpendicular Display (FPerp)]] — Muestra la perpendicularidad de un campo a través de una sección
- [[Catálogo - Vector#Point Charge (PCharge)|Point Charge (PCharge)]] — Crea un campo generado por una carga puntual
- [[Catálogo - Vector#Scalar Display (FScalar)|Scalar Display (FScalar)]] — Muestra los valores escalares de una sección de un campo
- [[Catálogo - Vector#Spin Force (FSpin)|Spin Force (FSpin)]] — Crea un campo generado por una fuerza de giro
- [[Catálogo - Vector#Tensor Display (FTensor)|Tensor Display (FTensor)]] — Muestra los vectores tensores de una sección de un campo
- [[Catálogo - Vector#Vector Force (FVector)|Vector Force (FVector)]] — Crea un campo generado por una fuerza vectorial

### Vector › Grid (8)

- [[Catálogo - Vector#Hexagonal (HexGrid)|Hexagonal (HexGrid)]] — Grilla 2D con celdas hexagonales
- [[Catálogo - Vector#Populate 2D (Pop2D)|Populate 2D (Pop2D)]] — Puebla una región bidimensional con puntos
- [[Catálogo - Vector#Populate 3D (Pop3D)|Populate 3D (Pop3D)]] — Puebla una región tridimensional con puntos
- [[Catálogo - Vector#Populate Geometry (PopGeo)|Populate Geometry (PopGeo)]] — Puebla geometría genérica con puntos
- [[Catálogo - Vector#Radial (RadGrid)|Radial (RadGrid)]] — Grilla radial 2D
- [[Catálogo - Vector#Rectangular (RecGrid)|Rectangular (RecGrid)]] — Grilla 2D con celdas rectangulares
- [[Catálogo - Vector#Square (SqGrid)|Square (SqGrid)]] — Grilla 2D con celdas cuadradas
- [[Catálogo - Vector#Triangular (TriGrid)|Triangular (TriGrid)]] — Grilla 2D con celdas triangulares

### Vector › Plane (19)

- [[Catálogo - Vector#Adjust Plane (PAdjust)|Adjust Plane (PAdjust)]] — Ajusta un plano a una nueva dirección normal
- [[Catálogo - Vector#Align Plane (Align)|Align Plane (Align)]] — Aplica la rotación mínima para alinear un plano con un vector guía
- [[Catálogo - Vector#Align Planes (Align)|Align Planes (Align)]] — Alinea planos minimizando su rotación en serie
- [[Catálogo - Vector#Construct Plane (Pl)|Construct Plane (Pl)]] — Construye un plano a partir de un punto de origen y los ejes {x}, {y}
- [[Catálogo - Vector#Deconstruct Plane (DePlane)|Deconstruct Plane (DePlane)]] — Descompone un plano en sus partes
- [[Catálogo - Vector#Flip Plane (PFlip)|Flip Plane (PFlip)]] — Invierte o intercambia los ejes de un plano
- [[Catálogo - Vector#Line + Line (LnLn)|Line + Line (LnLn)]] — Crea un plano a partir de dos segmentos de línea
- [[Catálogo - Vector#Line + Pt (LnPt)|Line + Pt (LnPt)]] — Crea un plano a partir de una línea y un punto
- [[Catálogo - Vector#Plane 3Pt (Pl 3Pt)|Plane 3Pt (Pl 3Pt)]] — Crea un plano que pasa por tres puntos
- [[Catálogo - Vector#Plane Closest Point (CP)|Plane Closest Point (CP)]] — Busca el punto más cercano en un plano
- [[Catálogo - Vector#Plane Coordinates (PlCoord)|Plane Coordinates (PlCoord)]] — Obtiene las coordenadas de un punto en el sistema de ejes de un plano
- [[Catálogo - Vector#Plane Fit (PlFit)|Plane Fit (PlFit)]] — Ajusta un plano a un conjunto de puntos
- [[Catálogo - Vector#Plane Normal (Pl)|Plane Normal (Pl)]] — Crea un plano perpendicular a un vector
- [[Catálogo - Vector#Plane Offset (Pl Offset)|Plane Offset (Pl Offset)]] — Desplaza (offset) un plano
- [[Catálogo - Vector#Plane Origin (Pl Origin)|Plane Origin (Pl Origin)]] — Cambia el punto de origen de un plano
- [[Catálogo - Vector#Rotate Plane (PRot)|Rotate Plane (PRot)]] — Rota un plano alrededor de su eje z
- [[Catálogo - Vector#XY Plane (XY)|XY Plane (XY)]] — Plano XY del mundo
- [[Catálogo - Vector#XZ Plane (XZ)|XZ Plane (XZ)]] — Plano XZ del mundo
- [[Catálogo - Vector#YZ Plane (YZ)|YZ Plane (YZ)]] — Plano YZ del mundo

### Vector › Point (21)

- [[Catálogo - Vector#Barycentric (BCentric)|Barycentric (BCentric)]] — Crea un punto a partir de coordenadas baricéntricas {u,v,w}
- [[Catálogo - Vector#Closest Point (CP)|Closest Point (CP)]] — Busca el punto más cercano en una colección de puntos
- [[Catálogo - Vector#Closest Points (CPs)|Closest Points (CPs)]] — Busca los puntos más cercanos en una colección de puntos
- [[Catálogo - Vector#Construct Point (Pt)|Construct Point (Pt)]] — Construye un punto a partir de coordenadas {xyz}
- [[Catálogo - Vector#Cull Duplicates (CullPt)|Cull Duplicates (CullPt)]] — Elimina (cull) los puntos que coinciden dentro de una tolerancia
- [[Catálogo - Vector#Deconstruct (pDecon)|Deconstruct (pDecon)]] — Descompone un punto en sus partes
- [[Catálogo - Vector#Distance (Dist)|Distance (Dist)]] — Calcula la distancia euclidiana entre dos puntos
- [[Catálogo - Vector#Numbers to Points (Num2Pt)|Numbers to Points (Num2Pt)]] — Convierte una lista de números en una lista de puntos
- [[Catálogo - Vector#Point Cloud Attributes (Point Cloud)|Point Cloud Attributes (Point Cloud)]] — Atributos de la nube de puntos
- [[Catálogo - Vector#Point Cloud Closest Point (Point Cloud CP)|Point Cloud Closest Point (Point Cloud CP)]] — Busca el punto más cercano en una nube de puntos
- [[Catálogo - Vector#Point Cylindrical (Pt)|Point Cylindrical (Pt)]] — Crea un punto a partir de coordenadas cilíndricas {ángulo, radio, elevación}
- [[Catálogo - Vector#Point Groups (PGroups)|Point Groups (PGroups)]] — Crea grupos de puntos cercanos
- [[Catálogo - Vector#Point Oriented (Pt)|Point Oriented (Pt)]] — Crea un punto a partir de coordenadas {u,v,w} de un plano
- [[Catálogo - Vector#Point Polar (Pt)|Point Polar (Pt)]] — Crea un punto a partir de coordenadas polares {phi, theta, desfase}
- [[Catálogo - Vector#Points to Numbers (Pt2Num)|Points to Numbers (Pt2Num)]] — Convierte una lista de puntos en una lista de números
- [[Catálogo - Vector#Project Point (Project)|Project Point (Project)]] — Proyecta un punto sobre una colección de formas
- [[Catálogo - Vector#Pull Point (Pull)|Pull Point (Pull)]] — Lleva (pull) un punto hacia distintos tipos de geometría
- [[Catálogo - Vector#Reduce Point Cloud (Reduce)|Reduce Point Cloud (Reduce)]] — Reduce la cantidad de puntos de una nube de puntos
- [[Catálogo - Vector#Sort Along Curve (AlongCrv)|Sort Along Curve (AlongCrv)]] — Ordena puntos a lo largo de una curva
- [[Catálogo - Vector#Sort Points (Sort Pt)|Sort Points (Sort Pt)]] — Ordena puntos por coordenadas euclidianas (primero x, luego y, luego z)
- [[Catálogo - Vector#To Polar (Polar)|To Polar (Polar)]] — Convierte un punto 3D a coordenadas polares de un plano

### Vector › Vector (14)

- [[Catálogo - Vector#Amplitude (Amp)|Amplitude (Amp)]] — Define la amplitud (longitud) de un vector
- [[Catálogo - Vector#Angle|Angle]] — Calcula el ángulo entre dos vectores
- [[Catálogo - Vector#Cross Product (XProd)|Cross Product (XProd)]] — Calcula el producto cruz de vectores
- [[Catálogo - Vector#Deconstruct Vector (DeVec)|Deconstruct Vector (DeVec)]] — Descompone un vector en sus partes
- [[Catálogo - Vector#Dot Product (DProd)|Dot Product (DProd)]] — Calcula el producto punto de vectores
- [[Catálogo - Vector#Reverse (Rev)|Reverse (Rev)]] — Invierte un vector (lo multiplica por -1)
- [[Catálogo - Vector#Rotate (VRot)|Rotate (VRot)]] — Rota un vector alrededor de un eje
- [[Catálogo - Vector#Unit Vector (Unit)|Unit Vector (Unit)]] — Unitiza un vector
- [[Catálogo - Vector#Unit X (X)|Unit X (X)]] — Vector unitario paralelo al eje {x} del mundo
- [[Catálogo - Vector#Unit Y (Y)|Unit Y (Y)]] — Vector unitario paralelo al eje {y} del mundo
- [[Catálogo - Vector#Unit Z (Z)|Unit Z (Z)]] — Vector unitario paralelo al eje {z} del mundo
- [[Catálogo - Vector#Vector 2Pt (Vec2Pt)|Vector 2Pt (Vec2Pt)]] — Crea un vector entre dos puntos
- [[Catálogo - Vector#Vector Length (VLen)|Vector Length (VLen)]] — Calcula la longitud (amplitud) de un vector
- [[Catálogo - Vector#Vector XYZ (Vec)|Vector XYZ (Vec)]] — Crea un vector a partir de sus componentes {xyz}

### LunchBox › Util (2)

- [[Catálogo - LunchBox#RTree Closest Point (RTree CP)|RTree Closest Point (RTree CP)]] — Busca el punto más cercano en un RTree a partir de puntos de búsqueda
- [[Catálogo - LunchBox#RTree Points in Range (RTree Range)|RTree Points in Range (RTree Range)]] — Busca los puntos de un RTree que están dentro de un rango de los puntos de búsqueda

### Pufferfish › Plane (19)

- [[Catálogo - Pufferfish#Average Plane (AvrPln)|Average Plane (AvrPln)]] — Calcula el promedio aritmético de un conjunto de planos
- [[Catálogo - Pufferfish#Closest Plane Orientation (CPlnOri)|Closest Plane Orientation (CPlnOri)]] — Busca el plano objetivo más cercano a un plano de referencia según la orientación de uno o varios ejes
- [[Catálogo - Pufferfish#Flip Plane (FlipPln)|Flip Plane (FlipPln)]] — Invierte un plano en los ejes indicados, con la opción de usar un plano guía
- [[Catálogo - Pufferfish#Mirror Cut Planes (MirCutPlns)|Mirror Cut Planes (MirCutPlns)]] — Corta un conjunto de planos con un plano, refleja el lado conservado del corte respecto de un plano de…
- [[Catálogo - Pufferfish#Offset Plane (OffPln)|Offset Plane (OffPln)]] — Desplaza (offset) un plano según los ejes indicados, con la opción de hacerlo hacia ambos lados a distancias…
- [[Catálogo - Pufferfish#Parameter Plane Divide Surface (ParamPlnDivSrf)|Parameter Plane Divide Surface (ParamPlnDivSrf)]] — Genera una grilla de planos orientados según la normal de una superficie, dividiendo su dominio con…
- [[Catálogo - Pufferfish#Parameter Plane In Rectangle (ParamPlnInRec)|Parameter Plane In Rectangle (ParamPlnInRec)]] — Ubica un plano orientado según la normal de un rectángulo, dentro del rectángulo, a partir de parámetros {x}…
- [[Catálogo - Pufferfish#Parameter Plane On Surface (ParamPlnOnSrf)|Parameter Plane On Surface (ParamPlnOnSrf)]] — Ubica un plano orientado según la normal de una superficie, sobre la superficie, a partir de parámetros {u} y…
- [[Catálogo - Pufferfish#Plane Trim Planes (PlnTrimPlns)|Plane Trim Planes (PlnTrimPlns)]] — Recorta (quita) las partes de un conjunto de planos que están a un lado de un plano
- [[Catálogo - Pufferfish#Tween Consecutive Planes (TwnConPlns)|Tween Consecutive Planes (TwnConPlns)]] — Interpola (tween) consecutivamente entre un conjunto de planos
- [[Catálogo - Pufferfish#Tween Consecutive Planes On Curve (TwnConPlnsCrv)|Tween Consecutive Planes On Curve (TwnConPlnsCrv)]] — Interpola (tween) consecutivamente entre un conjunto de planos sobre una curva; si los orígenes de los planos…
- [[Catálogo - Pufferfish#Tween Consecutive Planes On Surface (TwnConPlnsSrf)|Tween Consecutive Planes On Surface (TwnConPlnsSrf)]] — Interpola (tween) consecutivamente entre un conjunto de planos sobre una superficie; si los orígenes de los…
- [[Catálogo - Pufferfish#Tween Through Planes (TwnThruPlns)|Tween Through Planes (TwnThruPlns)]] — Interpola (tween) a través de un conjunto de planos
- [[Catálogo - Pufferfish#Tween Through Planes On Curve (TwnThruPlnsCrv)|Tween Through Planes On Curve (TwnThruPlnsCrv)]] — Interpola (tween) a través de un conjunto de planos sobre una curva; si los orígenes de los planos no están…
- [[Catálogo - Pufferfish#Tween Through Planes On Surface (TwnThruPlnsSrf)|Tween Through Planes On Surface (TwnThruPlnsSrf)]] — Interpola (tween) a través de un conjunto de planos sobre una superficie; si los orígenes de los planos no…
- [[Catálogo - Pufferfish#Tween Two Planes (Twn2Plns)|Tween Two Planes (Twn2Plns)]] — Interpola (tween) entre dos planos
- [[Catálogo - Pufferfish#Tween Two Planes On Curve (Twn2PlnsCrv)|Tween Two Planes On Curve (Twn2PlnsCrv)]] — Interpola (tween) entre dos planos sobre una curva; si los orígenes de los planos no están sobre la curva, se…
- [[Catálogo - Pufferfish#Tween Two Planes On Surface (Twn2PlnsSrf)|Tween Two Planes On Surface (Twn2PlnsSrf)]] — Interpola (tween) entre dos planos sobre una superficie; si los orígenes de los planos no están sobre la…
- [[Catálogo - Pufferfish#Weighted Average Plane (WavPln)|Weighted Average Plane (WavPln)]] — Calcula el promedio aritmético ponderado de un conjunto de planos

### Pufferfish › Point (30)

- [[Catálogo - Pufferfish#Are Points Collinear (PtsCoLinr)|Are Points Collinear (PtsCoLinr)]] — Prueba si un conjunto de puntos es colineal
- [[Catálogo - Pufferfish#Are Points Coplanar (PtsCoPlnr)|Are Points Coplanar (PtsCoPlnr)]] — Prueba si un conjunto de puntos es coplanar
- [[Catálogo - Pufferfish#Curve Coil Points (CrvCoilPts)|Curve Coil Points (CrvCoilPts)]] — Crea una serie de puntos que se enrollan en espiral a lo largo de una curva
- [[Catálogo - Pufferfish#Curve Edit Points (CrvEditPts)|Curve Edit Points (CrvEditPts)]] — Extrae los puntos de edición de una curva en los promedios de nodos: los puntos por los que pasa una curva…
- [[Catálogo - Pufferfish#Curve Middle Point (CrvMidPt)|Curve Middle Point (CrvMidPt)]] — Obtiene el punto en la mitad de la longitud o del dominio de una curva
- [[Catálogo - Pufferfish#Curve Wave Points (CrvWavePts)|Curve Wave Points (CrvWavePts)]] — Crea una serie de puntos que ondulan a lo largo de una curva
- [[Catálogo - Pufferfish#Map Point To Surface (MapPt2Srf)|Map Point To Surface (MapPt2Srf)]] — Mapea un punto al espacio de una superficie objetivo según su ubicación relativa al espacio de una superficie…
- [[Catálogo - Pufferfish#Mirror Cut Points (MirCutPts)|Mirror Cut Points (MirCutPts)]] — Corta un conjunto de puntos con un plano, refleja el lado conservado del corte respecto de un plano de…
- [[Catálogo - Pufferfish#Parameter Point Divide Surface (ParamPtDivSrf)|Parameter Point Divide Surface (ParamPtDivSrf)]] — Genera una grilla de puntos sobre una superficie dividiendo su dominio con parámetros {u} y {v}
- [[Catálogo - Pufferfish#Parameter Point In Rectangle (ParamPtInRec)|Parameter Point In Rectangle (ParamPtInRec)]] — Ubica un punto en un rectángulo a partir de parámetros {x} e {y} que dividen su dominio
- [[Catálogo - Pufferfish#Parameter Point On Surface (ParamPtOnSrf)|Parameter Point On Surface (ParamPtOnSrf)]] — Ubica un punto sobre una superficie a partir de parámetros {u} y {v} que dividen su dominio
- [[Catálogo - Pufferfish#Pinch'n'Spread Points (P'n'S)|Pinch'n'Spread Points (P'n'S)]] — Pellizca y expande (pinch & spread) un conjunto de puntos según valores de radio, intensidad y atenuación en…
- [[Catálogo - Pufferfish#Plane Trim Points (PlnTrimPts)|Plane Trim Points (PlnTrimPts)]] — Recorta (quita) las partes de un conjunto de puntos que están a un lado de un plano
- [[Catálogo - Pufferfish#Point Divide Curve Segments (PtDivCrvSegs)|Point Divide Curve Segments (PtDivCrvSegs)]] — Divide cada segmento de una curva en partes de igual longitud
- [[Catálogo - Pufferfish#Point Divide Curve Target Length (PtDivCrvTarg)|Point Divide Curve Target Length (PtDivCrvTarg)]] — Divide una curva en partes de igual longitud, lo más cercanas posible a una longitud objetivo
- [[Catálogo - Pufferfish#Point Mesh Side (PtMshSide)|Point Mesh Side (PtMshSide)]] — Determina a qué lado de una malla está un punto
- [[Catálogo - Pufferfish#Point Plane Side (PtPlnSide)|Point Plane Side (PtPlnSide)]] — Determina a qué lado de un plano está un punto
- [[Catálogo - Pufferfish#Point Surface Edge (PtSrfEdge)|Point Surface Edge (PtSrfEdge)]] — Busca la arista de una superficie más cercana a un punto
- [[Catálogo - Pufferfish#Point Surface Side (PtSrfSide)|Point Surface Side (PtSrfSide)]] — Determina a qué lado de una superficie está un punto
- [[Catálogo - Pufferfish#Reparameterize Points (ReparamPts)|Reparameterize Points (ReparamPts)]] — Reparametriza un conjunto de puntos para que sus coordenadas {x}, {y}, {z} vayan de 0 a 1, o de forma…
- [[Catálogo - Pufferfish#Surface Edit Points (SrfEditPts)|Surface Edit Points (SrfEditPts)]] — Extrae los puntos de edición de una superficie en los promedios de nodos: los puntos por los que pasa una…
- [[Catálogo - Pufferfish#Tween Consecutive Points (TwnConPts)|Tween Consecutive Points (TwnConPts)]] — Interpola (tween) consecutivamente entre un conjunto de puntos
- [[Catálogo - Pufferfish#Tween Consecutive Points On Curve (TwnConPtsCrv)|Tween Consecutive Points On Curve (TwnConPtsCrv)]] — Interpola (tween) consecutivamente entre un conjunto de puntos sobre una curva; si los puntos no están sobre…
- [[Catálogo - Pufferfish#Tween Consecutive Points On Surface (TwnConPtsSrf)|Tween Consecutive Points On Surface (TwnConPtsSrf)]] — Interpola (tween) consecutivamente entre un conjunto de puntos sobre una superficie; si los puntos no están…
- [[Catálogo - Pufferfish#Tween Through Points (TwnThruPts)|Tween Through Points (TwnThruPts)]] — Interpola (tween) a través de un conjunto de puntos
- [[Catálogo - Pufferfish#Tween Through Points On Curve (TwnThruPtsCrv)|Tween Through Points On Curve (TwnThruPtsCrv)]] — Interpola (tween) a través de un conjunto de puntos sobre una curva; si los puntos no están sobre la curva…
- [[Catálogo - Pufferfish#Tween Through Points On Surface (TwnThruPtsSrf)|Tween Through Points On Surface (TwnThruPtsSrf)]] — Interpola (tween) a través de un conjunto de puntos sobre una superficie; si los puntos no están sobre la…
- [[Catálogo - Pufferfish#Tween Two Points (Twn2Pts)|Tween Two Points (Twn2Pts)]] — Interpola (tween) entre dos puntos
- [[Catálogo - Pufferfish#Tween Two Points On Curve (Twn2PtsCrv)|Tween Two Points On Curve (Twn2PtsCrv)]] — Interpola (tween) entre dos puntos sobre una curva; si los puntos no están sobre la curva, se llevan hacia…
- [[Catálogo - Pufferfish#Tween Two Points On Surface (Twn2PtsSrf)|Tween Two Points On Surface (Twn2PtsSrf)]] — Interpola (tween) entre dos puntos sobre una superficie; si los puntos no están sobre la superficie, se…

### Pufferfish › Vector (9)

- [[Catálogo - Pufferfish#Closest Vector (CVec)|Closest Vector (CVec)]] — Busca el vector objetivo más cercano en ángulo a un vector de referencia
- [[Catálogo - Pufferfish#Mirror Combine Vectors (MirComVecs)|Mirror Combine Vectors (MirComVecs)]] — Refleja un conjunto de vectores desde su final o su inicio y lo combina con el conjunto original
- [[Catálogo - Pufferfish#Mirror Cut Vectors (MirCutVecs)|Mirror Cut Vectors (MirCutVecs)]] — Corta un conjunto de vectores en un índice, refleja el lado conservado del corte respecto de ese índice y lo…
- [[Catálogo - Pufferfish#Reparameterize Vectors (ReparamVecs)|Reparameterize Vectors (ReparamVecs)]] — Reparametriza un conjunto de vectores para que su longitud (amplitud) vaya de 0 a 1, o de forma invertida de…
- [[Catálogo - Pufferfish#Tween Consecutive Vectors (TwnConVecs)|Tween Consecutive Vectors (TwnConVecs)]] — Interpola (tween) consecutivamente entre un conjunto de vectores
- [[Catálogo - Pufferfish#Tween Through Vectors (TwnThruVecs)|Tween Through Vectors (TwnThruVecs)]] — Interpola (tween) a través de un conjunto de vectores
- [[Catálogo - Pufferfish#Tween Two Vectors (Twn2Vecs)|Tween Two Vectors (Twn2Vecs)]] — Interpola (tween) entre dos vectores
- [[Catálogo - Pufferfish#Vector Star (VecStar)|Vector Star (VecStar)]] — Crea una subdivisión espacial recursiva de vectores, orientada a un plano, que sale desde el origen de un…
- [[Catálogo - Pufferfish#Vector World (VecWorld)|Vector World (VecWorld)]] — Crea vectores alineados con los ejes de un plano que salen desde el origen de un plano base

<!-- AUTO:fin -->
