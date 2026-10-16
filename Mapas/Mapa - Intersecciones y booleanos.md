---
tags: [tipo/mapa, geometria/intersecciones, geometria/brep, software/grasshopper, software/rhinocommon]
---

# Intersecciones y booleanos

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Dónde se cruzan dos geometrías (puntos, curvas de corte), booleanos de sólidos y de regiones planas, cortes y contornos (secciones para láser o router) y detección de choques.

## Teoría y código
- [[wiki/concepts/rhinocommon-interseccion-api]]: la clase `Intersection` y el RTree
- [[wiki/sources/2026-05-04-rhinopy-operaciones-espaciales]] · [[wiki/concepts/brep-polisuperficies]]

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Curva con curva | [[Catálogo - Intersect#Curve – Curve (CCX)\|Curve – Curve]] | `rg.Intersect.Intersection.CurveCurve(a, b, tol, tol)` | — |
| Curva con plano | [[Catálogo - Intersect#Curve – Plane (PCX)\|Curve – Plane]] | `rg.Intersect.Intersection.CurvePlane(crv, plano, tol)` | — |
| Brep con Brep | [[Catálogo - Intersect#Brep – Brep (BBX)\|Brep – Brep]] | `ok, curvas, puntos = rg.Intersect.Intersection.BrepBrep(a, b, tol)` | — |
| Contornos (secciones) | [[Catálogo - Intersect#Contour\|Contour]] | `rg.Brep.CreateContourCurves(brep, p0, p1, intervalo)` | `.section(altura)` |
| Unión de regiones 2D | [[Catálogo - Intersect#Region Union (RUnion)\|Region Union]] | `rg.Curve.CreateBooleanUnion(curvas, tol)` | — |
| Diferencia de regiones 2D | [[Catálogo - Intersect#Region Difference (RDiff)\|Region Difference]] | `rg.Curve.CreateBooleanDifference(a, b, tol)` | — |
| Booleanos de sólidos | [[Catálogo - Intersect#Solid Difference (SDiff)\|Solid Difference]] | ver [[Mapa - Brep y sólidos]] | `.cut()`, `.union()` |
| Partir un Brep | [[Catálogo - Intersect#Split Brep (Split)\|Split Brep]] | `brep.Split(cortador, tol)` | — |

## Para empezar
[[Catálogo - Intersect#Curve – Curve (CCX)|Curve – Curve]] · [[Catálogo - Intersect#Brep – Plane (Sec)|Brep – Plane]] · [[Catálogo - Intersect#Contour|Contour]] · [[Catálogo - Intersect#Region Union (RUnion)|Region Union]] · [[Catálogo - Intersect#Trim with Region (Trim)|Trim with Region]] · [[Catálogo - Intersect#Collision Many–Many (ColMM)|Collision Many–Many]] · [[Catálogo - Intersect#Region Slits (RSlits)|Region Slits]] (o la versión corregida de [[Catálogo - Params#Region Slits (RSlits)|OpenNest]])

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (11)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Boolean Difference | [[Boolean Difference\|Py]] · [[Boolean Difference (cs)\|C#]] | Diferencia booleana entre dos grupos de polisuperficies | `Brep.CreateBooleanDifference(a, b, tol)` |
| Calculate Curve Intersections | [[Calculate Curve Intersections\|Py]] · [[Calculate Curve Intersections (cs)\|C#]] | Puntos y tramos superpuestos entre dos curvas | `Intersection.CurveCurve(a, b, tol, tolSolape)` |
| Create Contour Curves | [[Create Contour Curves\|Py]] · [[Create Contour Curves (cs)\|C#]] | Curvas de contorno (cortes paralelos) de Breps y mallas | `Brep.CreateContourCurves / Mesh.CreateContourCurves` |
| Curve Surface Intersection | [[Curve Surface Intersection\|Py]] · [[Curve Surface Intersection (cs)\|C#]] | Intersección curva–superficie: puntos y tramos superpuestos | `rs.CurveBrepIntersect → Intersection.CurveBrep` |
| Divide Curve Straight | [[Divide Curve Straight\|Py]] · [[Divide Curve Straight (cs)\|C#]] | Divide con distancias en línea recta (cuerda) usando esferas | `Intersection.CurveBrep con esferas → Curve.Split` |
| Furthest Z on Surface given X Y | [[Furthest Z on Surface given X Y\|Py]] · [[Furthest Z on Surface given X Y (cs)\|C#]] | Z más alta de una superficie en una posición X, Y | `Intersection.ProjectPointsToBreps(breps, pts, dir, tol)` |
| Intersect Lines | [[Intersect Lines\|Py]] · [[Intersect Lines (cs)\|C#]] | Intersección (o puntos más cercanos) entre dos líneas | `Intersection.LineLine(a, b) → parámetros a, b` |
| Intersecting Line and Circle | [[Intersecting Line and Circle (cs)\|C#]] | Puntos de intersección entre una línea y un círculo | `Intersection.LineCircle(linea, circulo, ...)` |
| Project Points to Breps | [[Project Points to Breps\|Py]] · [[Project Points to Breps (cs)\|C#]] | Proyecta puntos sobre Breps en una dirección | `Intersection.ProjectPointsToBreps` |
| Project Points to Mesh | [[Project Points to Mesh\|Py]] · [[Project Points to Mesh (cs)\|C#]] | Proyecta puntos sobre una malla | `Intersection.ProjectPointsToMeshesEx` |
| Split BReps with Planes | [[Split BReps with Planes\|Py]] · [[Split BReps with Planes (cs)\|C#]] | Corta Breps con un plano | `PlaneSurface.CreateThroughBox → Brep.Split(cortador, tol)` |

## Componentes de Grasshopper (52)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Intersect › Mathematical (18)

- [[Catálogo - Intersect#Brep – Line (BLX)|Brep – Line (BLX)]] — Calcula las intersecciones entre un Brep y una línea
- [[Catálogo - Intersect#Brep – Plane (Sec)|Brep – Plane (Sec)]] — Calcula las intersecciones entre un Brep y un plano (lo que también se conoce como sección)
- [[Catálogo - Intersect#Contour|Contour]] — Crea un conjunto de contornos de un Brep o una malla
- [[Catálogo - Intersect#Contour (ex) (Contour)|Contour (ex) (Contour)]] — Crea un conjunto de contornos de un Brep o una malla
- [[Catálogo - Intersect#Curve – Line (CLX)|Curve – Line (CLX)]] — Calcula las intersecciones entre una curva y una línea
- [[Catálogo - Intersect#Curve – Plane (PCX)|Curve – Plane (PCX)]] — Calcula las intersecciones entre una curva y un plano
- [[Catálogo - Intersect#IsoVist (IVist)|IsoVist (IVist)]] — Calcula un muestreo de isovista en una ubicación
- [[Catálogo - Intersect#IsoVist Ray (IVRay)|IsoVist Ray (IVRay)]] — Calcula una sola muestra de isovista en una ubicación
- [[Catálogo - Intersect#Line – Line (LLX)|Line – Line (LLX)]] — Calcula las intersecciones entre dos líneas
- [[Catálogo - Intersect#Line – Plane (PLX)|Line – Plane (PLX)]] — Calcula la intersección entre una línea y un plano
- [[Catálogo - Intersect#Mesh – Plane (Sec)|Mesh – Plane (Sec)]] — Calcula las intersecciones entre una malla y un plano (lo que también se conoce como sección)
- [[Catálogo - Intersect#Mesh – Ray (MeshRay)|Mesh – Ray (MeshRay)]] — Intersecta una malla con un rayo semi-infinito
- [[Catálogo - Intersect#Plane Region (PlReg)|Plane Region (PlReg)]] — Crea una región acotada a partir de planos que se intersectan
- [[Catálogo - Intersect#Plane – Plane (PPX)|Plane – Plane (PPX)]] — Calcula la intersección de dos planos
- [[Catálogo - Intersect#Plane – Plane – Plane (3PX)|Plane – Plane – Plane (3PX)]] — Calcula las intersecciones de tres planos
- [[Catálogo - Intersect#Point Cloud Contour (PC Contour)|Point Cloud Contour (PC Contour)]] — Crea una serie de curvas planas intersectando planos con una nube de puntos
- [[Catálogo - Intersect#Point Cloud Section (PC Section)|Point Cloud Section (PC Section)]] — Crea una sección plana intersectando un plano con una nube de puntos
- [[Catálogo - Intersect#Surface – Line (SLX)|Surface – Line (SLX)]] — Calcula las intersecciones entre una superficie y una línea

### Intersect › Physical (12)

- [[Catálogo - Intersect#Brep – Brep (BBX)|Brep – Brep (BBX)]] — Calcula las intersecciones entre dos Breps
- [[Catálogo - Intersect#Brep – Curve (BCX)|Brep – Curve (BCX)]] — Calcula las intersecciones entre un Brep y una curva
- [[Catálogo - Intersect#Clash|Clash]] — Realiza un análisis de colisiones (clash) en un conjunto de formas
- [[Catálogo - Intersect#Collision Many–Many (ColMM)|Collision Many–Many (ColMM)]] — Prueba colisiones muchos-con-muchos entre objetos
- [[Catálogo - Intersect#Collision One–Many (ColOM)|Collision One–Many (ColOM)]] — Prueba colisiones uno-con-muchos entre objetos
- [[Catálogo - Intersect#Curve – Curve (CCX)|Curve – Curve (CCX)]] — Calcula las intersecciones entre dos curvas
- [[Catálogo - Intersect#Curve – Self (CX)|Curve – Self (CX)]] — Calcula todas las autointersecciones de una curva
- [[Catálogo - Intersect#Mesh – Curve (MCX)|Mesh – Curve (MCX)]] — Intersección malla-curva
- [[Catálogo - Intersect#Mesh – Mesh (MMX)|Mesh – Mesh (MMX)]] — Intersección malla-malla
- [[Catálogo - Intersect#Multiple Curves (MCX)|Multiple Curves (MCX)]] — Calcula las intersecciones entre varias curvas
- [[Catálogo - Intersect#Surface Split (SrfSplit)|Surface Split (SrfSplit)]] — Divide una superficie con un grupo de curvas
- [[Catálogo - Intersect#Surface – Curve (SCX)|Surface – Curve (SCX)]] — Calcula las intersecciones entre una superficie y una curva

### Intersect › Region (6)

- [[Catálogo - Intersect#Split with Brep (Split)|Split with Brep (Split)]] — Divide una curva con un Brep
- [[Catálogo - Intersect#Split with Breps (Split)|Split with Breps (Split)]] — Divide una curva con varios Breps
- [[Catálogo - Intersect#Trim with Brep (Trim)|Trim with Brep (Trim)]] — Recorta una curva con un Brep
- [[Catálogo - Intersect#Trim with Breps (Trim)|Trim with Breps (Trim)]] — Recorta una curva con varios Breps
- [[Catálogo - Intersect#Trim with Region (Trim)|Trim with Region (Trim)]] — Recorta una curva con una región
- [[Catálogo - Intersect#Trim with Regions (Trim)|Trim with Regions (Trim)]] — Recorta una curva con varias regiones

### Intersect › Shape (16)

- [[Catálogo - Intersect#Boundary Volume (BVol)|Boundary Volume (BVol)]] — Crea una polisuperficie cerrada a partir de superficies de contorno
- [[Catálogo - Intersect#Box Slits (Slits)|Box Slits (Slits)]] — Agrega ranuras (slits) a una colección de cajas que se intersectan
- [[Catálogo - Intersect#Mesh Difference (MDif)|Mesh Difference (MDif)]] — Realiza una diferencia sólida entre dos conjuntos de mallas
- [[Catálogo - Intersect#Mesh Intersection (MInt)|Mesh Intersection (MInt)]] — Realiza una intersección sólida de un conjunto de mallas
- [[Catálogo - Intersect#Mesh Split (MSplit)|Mesh Split (MSplit)]] — División malla-malla
- [[Catálogo - Intersect#Mesh Union (MUnion)|Mesh Union (MUnion)]] — Realiza una unión sólida de un conjunto de mallas
- [[Catálogo - Intersect#Region Difference (RDiff)|Region Difference (RDiff)]] — Diferencia entre dos conjuntos de curvas planas cerradas (regiones)
- [[Catálogo - Intersect#Region Intersection (RInt)|Region Intersection (RInt)]] — Intersección entre dos conjuntos de curvas planas cerradas (regiones)
- [[Catálogo - Intersect#Region Slits (RSlits)|Region Slits (RSlits)]] — Agrega ranuras (slits) a una colección de regiones planas que se intersectan
- [[Catálogo - Intersect#Region Union (RUnion)|Region Union (RUnion)]] — Unión de un conjunto de curvas planas cerradas (regiones)
- [[Catálogo - Intersect#Solid Difference (SDiff)|Solid Difference (SDiff)]] — Realiza una diferencia sólida entre dos conjuntos de Breps
- [[Catálogo - Intersect#Solid Intersection (SInt)|Solid Intersection (SInt)]] — Realiza una intersección sólida entre dos conjuntos de Breps
- [[Catálogo - Intersect#Solid Union (SUnion)|Solid Union (SUnion)]] — Realiza una unión sólida de un conjunto de Breps
- [[Catálogo - Intersect#Split Brep (Split)|Split Brep (Split)]] — Divide un brep con otro
- [[Catálogo - Intersect#Split Brep Multiple (SplitMul)|Split Brep Multiple (SplitMul)]] — Divide un brep con un grupo de otros breps
- [[Catálogo - Intersect#Trim Solid (Trim)|Trim Solid (Trim)]] — Abre perforaciones en una forma con un conjunto de cortadores sólidos

<!-- AUTO:fin -->
