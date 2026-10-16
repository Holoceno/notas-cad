---
tags: [tipo/mapa, geometria/curvas, geometria/nurbs, software/grasshopper, software/rhinocommon, software/cadquery]
---

# Curvas

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Líneas, arcos, polilíneas y curvas NURBS: crearlas, medirlas, dividirlas y modificarlas. Casi todo en diseño paramétrico parte de una curva (contornos para CNC, perfiles para lofts, rieles para sweeps).

## Teoría y código
- [[wiki/concepts/curvas-nurbs]]: grado, puntos de control, pesos y nodos
- [[wiki/concepts/continuidad-geometrica]] · [[wiki/concepts/curvatura]]
- [[wiki/sources/2026-05-04-rhinopy-curvas]]: 22 samples de RhinoCommon en Python
- [[Aprendizaje/CadQuery/CadQuery vs RhinoCommon]] · [[Aprendizaje/Algoritmos/OVERKILL (CADCraft)]] (limpiar líneas superpuestas)

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Dividir en N partes | [[Catálogo - Curve#Divide Curve (Divide)\|Divide Curve]] | `ts = crv.DivideByCount(n, True)` | `[edge.positionAt(i / n) for i in range(n + 1)]` |
| Largo | [[Catálogo - Curve#Length (Len)\|Length]] | `crv.GetLength()` | `edge.Length()` |
| Punto y tangente en t | [[Catálogo - Curve#Evaluate Curve (Eval)\|Evaluate Curve]] | `crv.PointAt(t)`, `crv.TangentAt(t)` | `edge.positionAt(t)`, `edge.tangentAt(t)` (t de 0 a 1) |
| Punto más cercano | [[Catálogo - Curve#Curve Closest Point (Crv CP)\|Curve Closest Point]] | `ok, t = crv.ClosestPoint(pt)` | — |
| Offset en un plano | [[Catálogo - Curve#Offset Curve (Offset)\|Offset Curve]] | `crv.Offset(plano, d, tol, rg.CurveOffsetCornerStyle.Sharp)` | `wire.offset2D(d)` |
| Unir | [[Catálogo - Curve#Join Curves (Join)\|Join Curves]] | `rg.Curve.JoinCurves(curvas)` | `cq.Wire.assembleEdges(edges)` |
| Interpolar puntos | [[Catálogo - Curve#Interpolate (IntCrv)\|Interpolate]] | `rg.Curve.CreateInterpolatedCurve(pts, 3)` | `cq.Workplane().spline(pts)` |
| Partir en parámetros | [[Catálogo - Curve#Shatter\|Shatter]] | `crv.Split(ts)` | — |
| Redondear esquinas | [[Catálogo - Curve#Fillet\|Fillet]] | `rg.Curve.CreateFilletCornersCurve(crv, r, tol, ang_tol)` | `wire.fillet2D(r, vertices)` |

## Para empezar
[[Catálogo - Curve#Divide Curve (Divide)|Divide Curve]] · [[Catálogo - Curve#Evaluate Curve (Eval)|Evaluate Curve]] · [[Catálogo - Curve#Curve Closest Point (Crv CP)|Curve Closest Point]] · [[Catálogo - Curve#Offset Curve (Offset)|Offset Curve]] · [[Catálogo - Curve#Join Curves (Join)|Join Curves]] · [[Catálogo - Curve#Rebuild Curve (ReB)|Rebuild Curve]] · [[Catálogo - Curve#Perp Frames (PFrames)|Perp Frames]] · [[Catálogo - Curve#Polygon|Polygon]] · [[Catálogo - Curve#Rectangle|Rectangle]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (30)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Arrowheads to Curves | [[Add Arrowheads to Curves\|Py]] · [[Add Arrowheads to Curves (cs)\|C#]] | Pone puntas de flecha a una línea con los atributos del objeto | `ObjectAttributes.ObjectDecoration` |
| Add Circle | [[Add Circle\|Py]] · [[Add Circle (cs)\|C#]] | Crea un círculo con centro y radio | `Circle(centro, r) → doc.Objects.AddCircle` |
| Add Line | [[Add Line\|Py]] · [[Add Line (cs)\|C#]] | Crea una línea entre dos puntos pedidos | `GetPoint.DrawLineFromPoint → doc.Objects.AddLine` |
| Add NURBS Circle | [[Add NURBS Circle\|Py]] · [[Add NURBS Circle (cs)\|C#]] | Construye un círculo NURBS a mano: puntos con peso y nodos | `NurbsCurve(3, True, 3, 9), Points.SetPoint(i, x, y, z, w), Knots[i]` |
| Add NURBS Curve | [[Add NURBS Curve\|Py]] · [[Add NURBS Curve (cs)\|C#]] | Crea una curva NURBS desde puntos de control | `NurbsCurve.Create(periodica, grado, puntos)` |
| Brep from Curve Bounding Box | [[Brep from Curve Bounding Box\|Py]] · [[Brep from Curve Bounding Box (cs)\|C#]] | Caja Brep desde la caja contenedora de una curva, alineada al plano de construcción | `Curve.GetBoundingBox(plano) → Brep.CreateFromBox` |
| Calculate Curve Intersections | [[Calculate Curve Intersections\|Py]] · [[Calculate Curve Intersections (cs)\|C#]] | Puntos y tramos superpuestos entre dos curvas | `Intersection.CurveCurve(a, b, tol, tolSolape)` |
| Circle Center | [[Circle Center\|Py]] · [[Circle Center (cs)\|C#]] | Centro de las curvas cerradas que son círculos | `Curve.TryGetCircle(tol)` |
| Create Spiral | [[Create Spiral (cs)\|C#]] | Espiral desde un eje y un punto de radio, o a lo largo de un riel | `NurbsCurve.CreateSpiral(...)` |
| Curve Bounding Box | [[Curve Bounding Box\|Py]] · [[Curve Bounding Box (cs)\|C#]] | Caja contenedora de una curva (en el mundo y en un plano) | `Curve.GetBoundingBox(True / plano)` |
| Curve Deviation | [[Curve Deviation\|Py]] · [[Curve Deviation (cs)\|C#]] | Distancia mínima y máxima entre dos curvas | `rs.CurveDeviation(a, b) → Curve.GetDistancesBetweenCurves` |
| Divide by Length Points | [[Divide by Length Points\|Py]] · [[Divide by Length Points (cs)\|C#]] | Puntos a una distancia fija a lo largo de una curva | `Curve.DivideByLength(largo, incluirExtremos)` |
| Divide Curve by Segments | [[Divide Curve by Segments\|Py]] · [[Divide Curve by Segments (cs)\|C#]] | Divide una curva en N partes iguales | `Curve.DivideByCount(n, True) → PointAt(t)` |
| Divide Curve Straight | [[Divide Curve Straight\|Py]] · [[Divide Curve Straight (cs)\|C#]] | Divide con distancias en línea recta (cuerda) usando esferas | `Intersection.CurveBrep con esferas → Curve.Split` |
| Export Control Points | [[Export Control Points (cs)\|C#]] | Escribe los puntos de control de una curva en un archivo de texto | `ToNurbsCurve().Points → SaveFileDialog → StreamWriter` |
| Extend Curve | [[Extend Curve\|Py]] · [[Extend Curve (cs)\|C#]] | Extiende una curva hasta objetos límite | `Curve.Extend(extremo, CurveExtensionStyle.Line, geometrias)` |
| Extract Isocurve | [[Extract Isocurve\|Py]] · [[Extract Isocurve (cs)\|C#]] | Extrae una isocurva U o V en un punto | `Surface.IsoCurve(direccion, parametro)` |
| Fillet Curves | [[Fillet Curves\|Py]] · [[Fillet Curves (cs)\|C#]] | Empalme entre dos curvas con un radio | `Curve.CreateFilletCurves(c1, p1, c2, p2, r, unir, recortar, extender, tol, tolAng)` |
| Find Curve Parameter At Point | [[Find Curve Parameter At Point\|Py]] · [[Find Curve Parameter At Point (cs)\|C#]] | Parámetro t de un punto sobre la curva | `Curve.ClosestPoint(pt) → t` |
| Find point on curve at distance | [[Find point on curve at distance\|Py]] · [[Find point on curve at distance (cs)\|C#]] | Punto a una distancia medida sobre la curva | `Curve.PointAtLength(d)` |
| Increase NURBS Curve Degree | [[Increase NURBS Curve Degree\|Py]] · [[Increase NURBS Curve Degree (cs)\|C#]] | Sube el grado de una curva NURBS | `ToNurbsCurve().IncreaseDegree(g) → doc.Objects.Replace` |
| Insert Knot | [[Insert Knot\|Py]] · [[Insert Knot (cs)\|C#]] | Inserta un nodo en una curva NURBS | `NurbsCurve.Knots.InsertKnot(t)` |
| Intersect Lines | [[Intersect Lines\|Py]] · [[Intersect Lines (cs)\|C#]] | Intersección (o puntos más cercanos) entre dos líneas | `Intersection.LineLine(a, b) → parámetros a, b` |
| Intersecting Line and Circle | [[Intersecting Line and Circle (cs)\|C#]] | Puntos de intersección entre una línea y un círculo | `Intersection.LineCircle(linea, circulo, ...)` |
| Line Between Curves | [[Line Between Curves (cs)\|C#]] | Línea entre dos curvas (tangente o perpendicular) | `Line.TryCreateBetweenCurves(c0, c1, t0, t1, ...)` |
| Offset Curve | [[Offset Curve\|Py]] · [[Offset Curve (cs)\|C#]] | Copia paralela de una curva hacia un lado (compensación de herramienta) | `Curve.Offset(punto, normal, distancia, tol, esquinas)` |
| Reparameterize Curves | [[Reparameterize Curves\|Py]] · [[Reparameterize Curves (cs)\|C#]] | Cambia el dominio de una curva (por ejemplo de 0 a 1) | `Curve.Domain = Interval(a, b)` |
| Reverse Curve | [[Reverse Curve\|Py]] · [[Reverse Curve (cs)\|C#]] | Invierte la dirección de curvas | `Curve.Reverse() → doc.Objects.Replace` |
| Surface from Edge Curves | [[Surface from Edge Curves\|Py]] · [[Surface from Edge Curves (cs)\|C#]] | Superficie desde 2 a 4 curvas de borde | `Brep.CreateEdgeSurface(curvas)` |
| Tween Curve | [[Tween Curve (cs)\|C#]] | Curvas intermedias entre dos curvas | `Curve.CreateTweenCurves(c0, c1, n)` |

## Componentes de Grasshopper (198)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (5)

- [[Catálogo - Params#Circle (parámetro)|Circle (parámetro)]] — Contiene una colección de círculos
- [[Catálogo - Params#Circular Arc (Arc, parámetro)|Circular Arc (Arc, parámetro)]] — Contiene una colección de arcos circulares
- [[Catálogo - Params#Curve (Crv, parámetro)|Curve (Crv, parámetro)]] — Contiene una colección de curvas genéricas
- [[Catálogo - Params#Line (parámetro)|Line (parámetro)]] — Contiene una colección de segmentos de línea
- [[Catálogo - Params#Rectangle (Rec, parámetro)|Rectangle (Rec, parámetro)]] — Contiene una colección de rectángulos

### Curve › Analysis (32)

- [[Catálogo - Curve#Closed (Cls)|Closed (Cls)]] — Prueba si una curva es cerrada o periódica
- [[Catálogo - Curve#Control Points (CP)|Control Points (CP)]] — Extrae los puntos de control y los nodos NURBS de una curva
- [[Catálogo - Curve#Control Polygon (CPoly)|Control Polygon (CPoly)]] — Extrae el polígono de control NURBS de una curva
- [[Catálogo - Curve#Curvature|Curvature]] — Evalúa la curvatura de una curva en un parámetro dado
- [[Catálogo - Curve#Curvature Graph (CrvGraph)|Curvature Graph (CrvGraph)]] — Dibuja los gráficos de curvatura de Rhino
- [[Catálogo - Curve#Curve Closest Point (Crv CP)|Curve Closest Point (Crv CP)]] — Busca el punto más cercano en una curva
- [[Catálogo - Curve#Curve Domain (CrvDom)|Curve Domain (CrvDom)]] — Mide y define el dominio de la curva
- [[Catálogo - Curve#Curve Frame (Frame)|Curve Frame (Frame)]] — Obtiene el marco de curvatura de una curva en un parámetro dado
- [[Catálogo - Curve#Curve Middle (MidPt)|Curve Middle (MidPt)]] — Obtiene el punto medio de una curva
- [[Catálogo - Curve#Curve Nearest Object (CrvNear)|Curve Nearest Object (CrvNear)]] — Busca el objeto más cercano a una curva
- [[Catálogo - Curve#Curve Proximity (CrvProx)|Curve Proximity (CrvProx)]] — Busca el par de puntos más cercanos entre dos curvas
- [[Catálogo - Curve#Curve Side (Side)|Curve Side (Side)]] — Determina a qué lado de una curva está un punto
- [[Catálogo - Curve#Deconstruct Arc (DArc)|Deconstruct Arc (DArc)]] — Obtiene el plano base, el radio y el dominio angular de un arco
- [[Catálogo - Curve#Deconstruct Rectangle (DRec)|Deconstruct Rectangle (DRec)]] — Obtiene el plano base y los intervalos de los lados de un rectángulo
- [[Catálogo - Curve#Derivatives (CDiv)|Derivatives (CDiv)]] — Evalúa las derivadas de una curva en un parámetro dado
- [[Catálogo - Curve#Discontinuity (Disc)|Discontinuity (Disc)]] — Busca todas las discontinuidades a lo largo de una curva
- [[Catálogo - Curve#End Points (End)|End Points (End)]] — Extrae los puntos extremos de una curva
- [[Catálogo - Curve#Evaluate Curve (Eval)|Evaluate Curve (Eval)]] — Evalúa una curva en el parámetro indicado
- [[Catálogo - Curve#Evaluate Length (Eval)|Evaluate Length (Eval)]] — Evalúa una curva en un factor de su longitud. El factor se puede dar en unidades de la curva o normalizado.…
- [[Catálogo - Curve#Extremes (X-tremez)|Extremes (X-tremez)]] — Busca los extremos (puntos más alto y más bajo) de una curva
- [[Catálogo - Curve#Horizontal Frame (HFrame)|Horizontal Frame (HFrame)]] — Obtiene un marco alineado horizontalmente a lo largo de una curva en un parámetro dado
- [[Catálogo - Curve#Length (Len)|Length (Len)]] — Mide la longitud de una curva
- [[Catálogo - Curve#Length Domain (LenD)|Length Domain (LenD)]] — Mide la longitud de un subdominio de la curva
- [[Catálogo - Curve#Length Parameter (LenP)|Length Parameter (LenP)]] — Mide la longitud de una curva hasta un parámetro y desde él
- [[Catálogo - Curve#Perp Frame (PFrame)|Perp Frame (PFrame)]] — Calcula el marco perpendicular (sin torsión) en un parámetro dado de la curva
- [[Catálogo - Curve#Planar|Planar]] — Prueba si una curva es plana
- [[Catálogo - Curve#Point In Curve (InCurve)|Point In Curve (InCurve)]] — Prueba si un punto está contenido en una curva cerrada
- [[Catálogo - Curve#Point in Curves (InCurves)|Point in Curves (InCurves)]] — Prueba si un punto está contenido en varias curvas cerradas
- [[Catálogo - Curve#Point On Curve (CurvePoint, parámetro)|Point On Curve (CurvePoint, parámetro)]] — Evalúa una curva en una ubicación específica
- [[Catálogo - Curve#Polygon Center (PCen)|Polygon Center (PCen)]] — Busca el punto central (promedio) de una polilínea
- [[Catálogo - Curve#Segment Lengths (LenSeg)|Segment Lengths (LenSeg)]] — Busca los segmentos más corto y más largo de una curva
- [[Catálogo - Curve#Torsion|Torsion]] — Evalúa la torsión de una curva en un parámetro dado

### Curve › Division (10)

- [[Catálogo - Curve#Contour (ex) (Contour)|Contour (ex) (Contour)]] — Crea un conjunto de contornos de una curva
- [[Catálogo - Curve#Curve Contour (Contour)|Curve Contour (Contour)]] — Crea un conjunto de contornos de una curva
- [[Catálogo - Curve#Curve Frames (Frames)|Curve Frames (Frames)]] — Genera una cantidad de marcos de curva equiespaciados
- [[Catálogo - Curve#Dash Pattern (Dash)|Dash Pattern (Dash)]] — Convierte una curva en un patrón de trazos
- [[Catálogo - Curve#Divide Curve (Divide)|Divide Curve (Divide)]] — Divide una curva en segmentos de igual longitud
- [[Catálogo - Curve#Divide Distance (DivDist)|Divide Distance (DivDist)]] — Divide una curva con una distancia predefinida entre puntos
- [[Catálogo - Curve#Divide Length (DivLength)|Divide Length (DivLength)]] — Divide una curva en segmentos de una longitud predefinida
- [[Catálogo - Curve#Horizontal Frames (HFrames)|Horizontal Frames (HFrames)]] — Genera una cantidad de marcos de curva equiespaciados y alineados horizontalmente
- [[Catálogo - Curve#Perp Frames (PFrames)|Perp Frames (PFrames)]] — Genera una cantidad de marcos perpendiculares equiespaciados a lo largo de una curva
- [[Catálogo - Curve#Shatter|Shatter]] — Fragmenta una curva en segmentos

### Curve › Primitive (28)

- [[Catálogo - Curve#Arc|Arc]] — Crea un arco definido por un plano base, un radio y un dominio angular
- [[Catálogo - Curve#Arc 3Pt (Arc)|Arc 3Pt (Arc)]] — Crea un arco que pasa por tres puntos
- [[Catálogo - Curve#Arc SED (Arc)|Arc SED (Arc)]] — Crea un arco definido por un punto inicial, un punto final y un vector tangente
- [[Catálogo - Curve#BiArc|BiArc]] — Crea un biarco a partir de los puntos extremos y sus tangentes
- [[Catálogo - Curve#Circle (Cir)|Circle (Cir)]] — Crea un círculo definido por un plano base y un radio
- [[Catálogo - Curve#Circle 3Pt (Circle)|Circle 3Pt (Circle)]] — Crea un círculo definido por tres puntos
- [[Catálogo - Curve#Circle CNR (Circle)|Circle CNR (Circle)]] — Crea un círculo definido por un centro, una normal y un radio
- [[Catálogo - Curve#Circle Fit (FCircle)|Circle Fit (FCircle)]] — Ajusta un círculo a una colección de puntos
- [[Catálogo - Curve#Circle TanTan (CircleTT)|Circle TanTan (CircleTT)]] — Crea un círculo tangente a dos curvas
- [[Catálogo - Curve#Circle TanTanTan (CircleTTT)|Circle TanTanTan (CircleTTT)]] — Crea un círculo tangente a tres curvas
- [[Catálogo - Curve#Ellipse|Ellipse]] — Crea una elipse definida por un plano base y dos radios
- [[Catálogo - Curve#Fit Line (FLine)|Fit Line (FLine)]] — Ajusta una línea a una colección de puntos
- [[Catálogo - Curve#InCircle|InCircle]] — Crea el círculo inscrito de un triángulo
- [[Catálogo - Curve#InEllipse|InEllipse]] — Crea la elipse inscrita (elipse de Steiner) de un triángulo
- [[Catálogo - Curve#Line (Ln)|Line (Ln)]] — Crea una línea entre dos puntos
- [[Catálogo - Curve#Line 2Plane (Ln2Pl)|Line 2Plane (Ln2Pl)]] — Crea una línea entre dos planos
- [[Catálogo - Curve#Line 4Pt (Ln4Pt)|Line 4Pt (Ln4Pt)]] — Crea una línea a partir de cuatro puntos
- [[Catálogo - Curve#Line SDL (Line)|Line SDL (Line)]] — Crea un segmento de línea definido por un punto inicial, una tangente y una longitud
- [[Catálogo - Curve#Modified Arc (ModArc)|Modified Arc (ModArc)]] — Crea un arco a partir de otro arco
- [[Catálogo - Curve#Polygon|Polygon]] — Crea un polígono, con aristas redondeadas opcionales
- [[Catálogo - Curve#Polygon Edge (PolEdge)|Polygon Edge (PolEdge)]] — Crea un polígono a partir de una sola arista
- [[Catálogo - Curve#Rectangle|Rectangle]] — Crea un rectángulo sobre un plano
- [[Catálogo - Curve#Rectangle 2Pt (Rec 2Pt)|Rectangle 2Pt (Rec 2Pt)]] — Crea un rectángulo a partir de un plano base y dos puntos
- [[Catálogo - Curve#Rectangle 3Pt (Rec 3Pt)|Rectangle 3Pt (Rec 3Pt)]] — Crea un rectángulo a partir de tres puntos
- [[Catálogo - Curve#Tangent Arcs (TArc)|Tangent Arcs (TArc)]] — Crea arcos tangentes entre círculos
- [[Catálogo - Curve#Tangent Lines (Ex) (TanEx)|Tangent Lines (Ex) (TanEx)]] — Crea líneas tangentes exteriores entre círculos
- [[Catálogo - Curve#Tangent Lines (In) (TanIn)|Tangent Lines (In) (TanIn)]] — Crea líneas tangentes interiores entre círculos
- [[Catálogo - Curve#Tangent Lines (Tan)|Tangent Lines (Tan)]] — Crea líneas tangentes entre un punto y un círculo

### Curve › Spline (19)

- [[Catálogo - Curve#Bezier Span (BzSpan)|Bezier Span (BzSpan)]] — Construye un tramo Bézier a partir de los puntos extremos y sus tangentes
- [[Catálogo - Curve#Blend Curve (BlendC)|Blend Curve (BlendC)]] — Crea una curva de mezcla (blend) entre dos curvas
- [[Catálogo - Curve#Blend Curve Pt (BlendCPt)|Blend Curve Pt (BlendCPt)]] — Crea una curva de mezcla (blend) entre dos curvas que pasa por un punto
- [[Catálogo - Curve#Catenary (Cat)|Catenary (Cat)]] — Crea una catenaria (cadena colgante) entre dos puntos
- [[Catálogo - Curve#Connect Curves (Connect)|Connect Curves (Connect)]] — Conecta una secuencia de curvas
- [[Catálogo - Curve#Curve On Surface (CrvSrf)|Curve On Surface (CrvSrf)]] — Crea una curva interpolada que pasa por un conjunto de puntos sobre una superficie
- [[Catálogo - Curve#Geodesic|Geodesic]] — Construye una geodésica sobre una superficie entre dos puntos
- [[Catálogo - Curve#Interpolate (IntCrv)|Interpolate (IntCrv)]] — Crea una curva interpolada que pasa por un conjunto de puntos
- [[Catálogo - Curve#Interpolate (t) (IntCrv(t))|Interpolate (t) (IntCrv(t))]] — Crea una curva interpolada que pasa por un conjunto de puntos, con tangentes
- [[Catálogo - Curve#Iso Curve (Iso)|Iso Curve (Iso)]] — Construye isocurvas {uv} sobre una superficie
- [[Catálogo - Curve#Kinky Curve (KinkCrv)|Kinky Curve (KinkCrv)]] — Construye una curva interpolada que pasa por un conjunto de puntos, con un umbral de ángulo de quiebre (kink)
- [[Catálogo - Curve#Knot Vector (Knots)|Knot Vector (Knots)]] — Construye un vector de nodos para una curva NURBS
- [[Catálogo - Curve#Nurbs Curve (Nurbs)|Nurbs Curve (Nurbs)]] — Construye una curva NURBS a partir de puntos de control
- [[Catálogo - Curve#Nurbs Curve PWK (NurbCrv)|Nurbs Curve PWK (NurbCrv)]] — Construye una curva NURBS a partir de puntos de control, pesos y nodos
- [[Catálogo - Curve#PolyArc (PArc)|PolyArc (PArc)]] — Crea una policurva formada por segmentos de arco y de línea
- [[Catálogo - Curve#PolyLine (PLine)|PolyLine (PLine)]] — Crea una polilínea que conecta varios puntos
- [[Catálogo - Curve#Sub Curve (SubCrv)|Sub Curve (SubCrv)]] — Construye una curva a partir de un subdominio de una curva base
- [[Catálogo - Curve#Tangent Curve (TanCurve)|Tangent Curve (TanCurve)]] — Crea una curva que pasa por un conjunto de puntos, con tangentes
- [[Catálogo - Curve#Tween Curve (TweenCrv)|Tween Curve (TweenCrv)]] — Interpola (tween) entre dos curvas

### Curve › Util (21)

- [[Catálogo - Curve#Curve To Polyline (ToPoly)|Curve To Polyline (ToPoly)]] — Convierte una curva en una polilínea
- [[Catálogo - Curve#Explode|Explode]] — Explota una curva en segmentos más pequeños
- [[Catálogo - Curve#Extend Curve (Ext)|Extend Curve (Ext)]] — Extiende una curva una distancia dada
- [[Catálogo - Curve#Fillet|Fillet]] — Aplica fillet a las esquinas agudas de una curva
- [[Catálogo - Curve#Fillet Distance (Fillet)|Fillet Distance (Fillet)]] — Aplica fillet a las esquinas agudas de una curva según una distancia
- [[Catálogo - Curve#Fillet · 2|Fillet · 2]] — Aplica fillet a una curva en un parámetro
- [[Catálogo - Curve#Fit Curve (Fit)|Fit Curve (Fit)]] — Ajusta una curva a lo largo de otra curva
- [[Catálogo - Curve#Flip Curve (Flip)|Flip Curve (Flip)]] — Invierte el sentido de una curva, usando una curva guía opcional
- [[Catálogo - Curve#Join Curves (Join)|Join Curves (Join)]] — Une la mayor cantidad posible de curvas
- [[Catálogo - Curve#Offset Curve (Offset)|Offset Curve (Offset)]] — Aplica offset a una curva con una distancia dada
- [[Catálogo - Curve#Offset Curve Loose (Offset (L))|Offset Curve Loose (Offset (L))]] — Aplica offset a los puntos de control de una curva con una distancia dada
- [[Catálogo - Curve#Offset on Srf (OffsetS)|Offset on Srf (OffsetS)]] — Aplica offset a una curva sobre una superficie con una distancia dada
- [[Catálogo - Curve#Polyline Collapse (PCol)|Polyline Collapse (PCol)]] — Colapsa los segmentos cortos de una curva polilínea
- [[Catálogo - Curve#Project Curve (Project)|Project Curve (Project)]] — Proyecta una curva sobre un Brep
- [[Catálogo - Curve#Pull Curve (Pull)|Pull Curve (Pull)]] — Lleva (pull) una curva sobre una superficie
- [[Catálogo - Curve#Rebuild Curve (ReB)|Rebuild Curve (ReB)]] — Reconstruye una curva con una cantidad específica de puntos de control
- [[Catálogo - Curve#Reduce (RedPLine)|Reduce (RedPLine)]] — Reduce una polilínea quitando los vértices menos significativos
- [[Catálogo - Curve#Seam|Seam]] — Ajusta la costura de una curva cerrada
- [[Catálogo - Curve#Simplify Curve (Simplify)|Simplify Curve (Simplify)]] — Simplifica una curva
- [[Catálogo - Curve#Smooth Polyline (SmoothPLine)|Smooth Polyline (SmoothPLine)]] — Suaviza los vértices de una curva polilínea
- [[Catálogo - Curve#Vectorize|Vectorize]] — Vectoriza, o calca, un mapa de bits

### Parakeet › Curve (25)

- [[Catálogo - Parakeet#AddOrnament (AddOrn)|AddOrnament (AddOrn)]] — Mapea una curva sobre una línea
- [[Catálogo - Parakeet#Align Curves (AlignCrv)|Align Curves (AlignCrv)]] — Alinea una lista de curvas según una curva guía, ajustando la costura y la dirección de las curvas
- [[Catálogo - Parakeet#Approx. Convex Hull (ConvexH)|Approx. Convex Hull (ConvexH)]] — Este componente calcula una Alpha Shape aproximada de un conjunto de puntos 3D con un método de envolvente…
- [[Catálogo - Parakeet#Complex Transform A (Complex T A)|Complex Transform A (Complex T A)]] — Aplica una transformación compleja a una red de curvas (llamada de forma imprecisa transformación 4D o…
- [[Catálogo - Parakeet#Curve to Arcs and Lines (Curve > Arc/Line)|Curve to Arcs and Lines (Curve > Arc/Line)]] — Convierte una curva en arcos y líneas
- [[Catálogo - Parakeet#Discontinuity With Threshold (Discontinuity+)|Discontinuity With Threshold (Discontinuity+)]] — Busca discontinuidades angulares (quiebres G1) a lo largo de una curva usando un umbral de ángulo dado
- [[Catálogo - Parakeet#Divide Curve Variable (DivideVar)|Divide Curve Variable (DivideVar)]] — Divide una curva según su curvatura, con parámetros variables
- [[Catálogo - Parakeet#Dual Garph (Dual)|Dual Garph (Dual)]] — Genera el grafo dual de una lista de polígonos
- [[Catálogo - Parakeet#Extend on surface (Extend Cr)|Extend on surface (Extend Cr)]] — Extiende una curva sobre una superficie
- [[Catálogo - Parakeet#FontSelector (fonts)|FontSelector (fonts)]] — Lista todas las fuentes instaladas en este equipo. Usa el parámetro Fi para obtener la fuente número 'i' de…
- [[Catálogo - Parakeet#Graph Coloring (GraphC)|Graph Coloring (GraphC)]] — Obtiene un entero por cada punto de la red. La coloración de grafos es un caso especial del etiquetado de…
- [[Catálogo - Parakeet#Join Curves Plus (Join Curves +)|Join Curves Plus (Join Curves +)]] — Une la mayor cantidad posible de curvas que estén a menos de una distancia
- [[Catálogo - Parakeet#Loop Trancate (Trancate)|Loop Trancate (Trancate)]] — Trunca un patrón (red 2D o 3D de líneas/curvas) de forma recursiva
- [[Catálogo - Parakeet#Map Curves (MapCrv2Crv)|Map Curves (MapCrv2Crv)]] — Mapea una colección de polilíneas y curvas de una polilínea a otra. Las polilíneas de origen y destino deben…
- [[Catálogo - Parakeet#MapToLine (MapToLn)|MapToLine (MapToLn)]] — Mapea una curva sobre una línea
- [[Catálogo - Parakeet#Mirrored Subdivide Quad (QuadSubM)|Mirrored Subdivide Quad (QuadSubM)]] — Subdivide un polígono cerrado en celdas cuadrangulares y refleja las piezas de forma alternada (útil para…
- [[Catálogo - Parakeet#Network Regions (Region)|Network Regions (Region)]] — Obtiene regiones (áreas cerradas) de una red de curvas
- [[Catálogo - Parakeet#Network Regions + (Region+)|Network Regions + (Region+)]] — Obtiene regiones (áreas cerradas) de una red de curvas + datos de half-edge
- [[Catálogo - Parakeet#Network Topology|Network Topology]] — Obtiene la topología completa de una red de líneas
- [[Catálogo - Parakeet#ParaText (text)|ParaText (text)]] — Escribe un texto sobre un plano dado y entrega su silueta como una lista de curvas
- [[Catálogo - Parakeet#Polygon by Area (Polygon Area)|Polygon by Area (Polygon Area)]] — Crea un polígono según un área dada
- [[Catálogo - Parakeet#Random Seam|Random Seam]] — Ajusta al azar la costura de las curvas (y polilíneas) dadas
- [[Catálogo - Parakeet#Remove Duplicate Curves+ (RmDupCrv+)|Remove Duplicate Curves+ (RmDupCrv+)]] — Elimina curvas duplicadas usando longitud, dirección y muestreo de puntos con un umbral de tolerancia
- [[Catálogo - Parakeet#Remove Short Segments (RmvShortSgmnt)|Remove Short Segments (RmvShortSgmnt)]] — Quita los segmentos cortos de una curva
- [[Catálogo - Parakeet#SeparateDifferentCurves (SepCrvs)|SeparateDifferentCurves (SepCrvs)]] — Separa distintos tipos de curvas

### Pufferfish › Curve (58)

- [[Catálogo - Pufferfish#Align Curve Seams (AliCrvSeams)|Align Curve Seams (AliCrvSeams)]] — Alinea las costuras de un conjunto de curvas cerradas, de forma iterativa o no, a partir de la primera curva…
- [[Catálogo - Pufferfish#Arc/Circle/Ellipse (ACE)|Arc/Circle/Ellipse (ACE)]] — Obtiene la representación como arco, círculo o elipse de una curva
- [[Catálogo - Pufferfish#Average Curve (AvrCrv)|Average Curve (AvrCrv)]] — Calcula el promedio aritmético de un conjunto de curvas
- [[Catálogo - Pufferfish#Bounding Rectangle (BRec)|Bounding Rectangle (BRec)]] — Crea un rectángulo contenedor orientado a un plano que une toda la geometría, o rectángulos contenedores…
- [[Catálogo - Pufferfish#Close Curve (ClsCrv)|Close Curve (ClsCrv)]] — Cierra una curva abierta de distintas formas; si la curva ya es cerrada o es lineal, sale sin cambios
- [[Catálogo - Pufferfish#Compatibilize Polylines (ComPLines)|Compatibilize Polylines (ComPLines)]] — Hace compatibles (iguales) en cantidad de puntos de control un conjunto de polilíneas, sin cambiar su forma
- [[Catálogo - Pufferfish#Constrained Area Ellipse (ConsAreaEli)|Constrained Area Ellipse (ConsAreaEli)]] — Crea una elipse o círculo del tamaño de un área dada, con factores de proporción {x} e {y}, centrado en un…
- [[Catálogo - Pufferfish#Constrained Area Polygon (ConsAreaPly)|Constrained Area Polygon (ConsAreaPly)]] — Crea un polígono irregular o regular del tamaño de un área dada, con factores de proporción {x} e {y}…
- [[Catálogo - Pufferfish#Constrained Area Rectangle (ConsAreaRec)|Constrained Area Rectangle (ConsAreaRec)]] — Crea un rectángulo o cuadrado del tamaño de un área dada, con factores de proporción {x} e {y}, centrado en…
- [[Catálogo - Pufferfish#Curve Align Curve Seams (CrvAliCrvSeams)|Curve Align Curve Seams (CrvAliCrvSeams)]] — Alinea las costuras de un conjunto de curvas cerradas a lo largo de una curva guía, con la opción de…
- [[Catálogo - Pufferfish#Curve Degree (CrvDeg)|Curve Degree (CrvDeg)]] — Obtiene el valor del grado de una curva
- [[Catálogo - Pufferfish#Curve Length At (CrvLenAt)|Curve Length At (CrvLenAt)]] — Obtiene la longitud a lo largo de una curva desde su inicio hasta un punto de la curva (u opcionalmente hasta…
- [[Catálogo - Pufferfish#Curve Length Between (CrvLenBtwn)|Curve Length Between (CrvLenBtwn)]] — Obtiene las longitudes a lo largo de una curva entre puntos de la curva (u opcionalmente entre parámetros)…
- [[Catálogo - Pufferfish#Curve Spans (CrvSpans)|Curve Spans (CrvSpans)]] — Obtiene el subdominio de cada tramo (span) de una curva e información de los tramos: cantidad, longitud de…
- [[Catálogo - Pufferfish#Curve Statistics (CrvStats)|Curve Statistics (CrvStats)]] — Obtiene estadísticas de una curva: cantidad de puntos de control, de puntos de edición, de quiebres, de…
- [[Catálogo - Pufferfish#Discrete Polyline (DPLine)|Discrete Polyline (DPLine)]] — Crea una polilínea formada por segmentos orientados según vectores objetivo, buscando para cada vector entre…
- [[Catálogo - Pufferfish#Fit Curve Segments (FitCrvSegs)|Fit Curve Segments (FitCrvSegs)]] — Busca en una curva los segmentos de los grados indicados y ajusta nuevos segmentos a través de ellos con un…
- [[Catálogo - Pufferfish#Fit Curve Smooth (FitCrvSmo)|Fit Curve Smooth (FitCrvSmo)]] — Ajusta una nueva curva a una curva existente suavizando los ángulos de quiebre, sin cambiar la forma general
- [[Catálogo - Pufferfish#Is Arc/Circle/Ellipse (IsACE)|Is Arc/Circle/Ellipse (IsACE)]] — Prueba si una curva es un arco, un círculo o una elipse según la definición de Rhino. Una curva puede ser de…
- [[Catálogo - Pufferfish#Is Curve Kinky (CrvKinky)|Is Curve Kinky (CrvKinky)]] — Prueba si una curva tiene quiebres y obtiene información de ellos: cantidad y longitud a lo largo de la curva…
- [[Catálogo - Pufferfish#Is Curve Linear (CrvLinr)|Is Curve Linear (CrvLinr)]] — Prueba si una curva es lineal
- [[Catálogo - Pufferfish#Is Curve Segmented (CrvSegs)|Is Curve Segmented (CrvSegs)]] — Prueba si una curva tiene segmentos y obtiene información de ellos: cantidad, longitud de cada uno y grado de…
- [[Catálogo - Pufferfish#Mesh Loop Edges (MshLoopEdgs)|Mesh Loop Edges (MshLoopEdgs)]] — Extrae las polilíneas de los bucles de aristas (edge loops) de una malla de cuadriláteros en un índice de…
- [[Catálogo - Pufferfish#Mesh Naked Edges (MshNakedEdgs)|Mesh Naked Edges (MshNakedEdgs)]] — Extrae las polilíneas de las aristas desnudas de una malla, si existen
- [[Catálogo - Pufferfish#Mirror Cut Curve (MirCutCrv)|Mirror Cut Curve (MirCutCrv)]] — Corta una curva con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo…
- [[Catálogo - Pufferfish#Net On Surface (NetSrf)|Net On Surface (NetSrf)]] — Crea una red de curvas interpoladas sobre una superficie
- [[Catálogo - Pufferfish#Offset Curve (OffCrv)|Offset Curve (OffCrv)]] — Aplica offset a una curva, con la opción de hacerlo hacia ambos lados a distancias distintas y tapar los…
- [[Catálogo - Pufferfish#Offset Curve From Surface (OffCrvFromSrf)|Offset Curve From Surface (OffCrvFromSrf)]] — Aplica offset a una curva alejándola de una superficie según las direcciones normales de la superficie, con…
- [[Catálogo - Pufferfish#Open Curve (OpnCrv)|Open Curve (OpnCrv)]] — Abre una curva cerrada desde su costura, o acorta una curva abierta desde sus extremos
- [[Catálogo - Pufferfish#Parameter Curve Divide Rectangle (ParamCrvDivRec)|Parameter Curve Divide Rectangle (ParamCrvDivRec)]] — Genera una grilla de curvas sobre un rectángulo dividiendo su dominio con parámetros {x} e {y}, o genera una…
- [[Catálogo - Pufferfish#Parameter Curve Divide Surface (ParamCrvDivSrf)|Parameter Curve Divide Surface (ParamCrvDivSrf)]] — Genera una grilla de curvas sobre una superficie dividiendo su dominio con parámetros {u} y {v}, o genera una…
- [[Catálogo - Pufferfish#Parameter Rectangle Grid (ParamRecGrid)|Parameter Rectangle Grid (ParamRecGrid)]] — Genera una grilla de celdas rectangulares en un rectángulo dividiendo su dominio con parámetros {x} e {y}
- [[Catálogo - Pufferfish#Parameter Rectangle Isocurve (ParamRecIso)|Parameter Rectangle Isocurve (ParamRecIso)]] — Genera una isocurva sobre un rectángulo a partir de un parámetro {x} o {y} que divide su dominio
- [[Catálogo - Pufferfish#Parameter Surface Grid (ParamSrfGrid)|Parameter Surface Grid (ParamSrfGrid)]] — Genera una grilla de celdas rectangulares sobre una superficie dividiendo su dominio con parámetros {u} y {v}
- [[Catálogo - Pufferfish#Parameter Surface Isocurve (ParamSrfIso)|Parameter Surface Isocurve (ParamSrfIso)]] — Genera una isocurva sobre una superficie a partir de un parámetro {u} o {v} que divide su dominio
- [[Catálogo - Pufferfish#Plane Trim Curve (PlnTrimCrv)|Plane Trim Curve (PlnTrimCrv)]] — Recorta (quita) las partes de una curva que están a un lado de un plano
- [[Catálogo - Pufferfish#Point Fit Rectangle (PtFitRec)|Point Fit Rectangle (PtFitRec)]] — Ajusta un rectángulo a un conjunto de puntos
- [[Catálogo - Pufferfish#Points Trim Curve (PtsTrimCrv)|Points Trim Curve (PtsTrimCrv)]] — Recorta una curva con un conjunto de puntos (u opcionalmente de parámetros) como un patrón de trazos; si los…
- [[Catálogo - Pufferfish#Prude Curve (PrudeCrv)|Prude Curve (PrudeCrv)]] — Quita las partes con quiebres de una curva (discontinuidades) mezclando sus segmentos; si la curva no tiene…
- [[Catálogo - Pufferfish#Rebuild Curve (RebCrv)|Rebuild Curve (RebCrv)]] — Reconstruye una curva con una cantidad de puntos, un grado y un dominio dados
- [[Catálogo - Pufferfish#Rebuild Curve Segments (RebCrvSegs)|Rebuild Curve Segments (RebCrvSegs)]] — Busca en una curva los segmentos de los grados indicados y los reconstruye con un grado y una cantidad de…
- [[Catálogo - Pufferfish#Relocate Curve Ends (ReCrvEnds)|Relocate Curve Ends (ReCrvEnds)]] — Reubica los extremos de una curva en nuevos puntos inicial y final sin tener que reconstruir la curva
- [[Catálogo - Pufferfish#Remap Curve Domain (ReCrvDom)|Remap Curve Domain (ReCrvDom)]] — Reasigna el rango del dominio {t} de una curva a un rango de entrada, con la opción de igualar el rango del…
- [[Catálogo - Pufferfish#Reparameterize Curve (ReparamCrv)|Reparameterize Curve (ReparamCrv)]] — Reparametriza una curva para que su dominio (t) vaya de 0 a 1
- [[Catálogo - Pufferfish#Seam To Curve Corner (Seam2CrvCorn)|Seam To Curve Corner (Seam2CrvCorn)]] — Ajusta la costura de una curva cerrada con esquinas para que quede en la esquina más cercana a la costura…
- [[Catálogo - Pufferfish#Slide Curve Along Curve (SlideCrvCrv)|Slide Curve Along Curve (SlideCrvCrv)]] — Desliza una curva a lo largo de una curva guía (u opcionalmente de dos curvas guía)
- [[Catálogo - Pufferfish#Smooth Curve (SmoCrv)|Smooth Curve (SmoCrv)]] — Suaviza una curva de forma recursiva (fairing) sin cambiar su cantidad de puntos de control
- [[Catálogo - Pufferfish#Superimpose Curve (SuperCrv)|Superimpose Curve (SuperCrv)]] — Superpone la cantidad de puntos de control, el grado y el dominio de una curva de referencia sobre una curva…
- [[Catálogo - Pufferfish#Tween Consecutive Curves (TwnConCrvs)|Tween Consecutive Curves (TwnConCrvs)]] — Interpola (tween) consecutivamente entre un conjunto de curvas
- [[Catálogo - Pufferfish#Tween Consecutive Curves Along Curve (TwnConCrvsCrv)|Tween Consecutive Curves Along Curve (TwnConCrvsCrv)]] — Interpola (tween) consecutivamente entre un conjunto de curvas a lo largo de una curva guía (u opcionalmente…
- [[Catálogo - Pufferfish#Tween Consecutive Curves On Surface (TwnConCrvsSrf)|Tween Consecutive Curves On Surface (TwnConCrvsSrf)]] — Interpola (tween) consecutivamente entre un conjunto de curvas sobre una superficie; si las curvas no están…
- [[Catálogo - Pufferfish#Tween Through Curves (TwnThruCrvs)|Tween Through Curves (TwnThruCrvs)]] — Interpola (tween) a través de un conjunto de curvas
- [[Catálogo - Pufferfish#Tween Through Curves Along Curve (TwnThruCrvsCrv)|Tween Through Curves Along Curve (TwnThruCrvsCrv)]] — Interpola (tween) a través de un conjunto de curvas a lo largo de una curva guía (u opcionalmente de dos…
- [[Catálogo - Pufferfish#Tween Through Curves On Surface (TwnThruCrvsSrf)|Tween Through Curves On Surface (TwnThruCrvsSrf)]] — Interpola (tween) a través de un conjunto de curvas sobre una superficie; si las curvas no están sobre la…
- [[Catálogo - Pufferfish#Tween Two Curves (Twn2Crvs)|Tween Two Curves (Twn2Crvs)]] — Interpola (tween) entre dos curvas
- [[Catálogo - Pufferfish#Tween Two Curves Along Curve (Twn2CrvsCrv)|Tween Two Curves Along Curve (Twn2CrvsCrv)]] — Interpola (tween) entre dos curvas a lo largo de una curva guía (u opcionalmente de dos curvas guía)
- [[Catálogo - Pufferfish#Tween Two Curves On Surface (Twn2CrvsSrf)|Tween Two Curves On Surface (Twn2CrvsSrf)]] — Interpola (tween) entre dos curvas sobre una superficie; si las curvas no están sobre la superficie, se…
- [[Catálogo - Pufferfish#Weighted Average Curve (WavCrv)|Weighted Average Curve (WavCrv)]] — Calcula el promedio ponderado aritmético de un conjunto de curvas

<!-- AUTO:fin -->
