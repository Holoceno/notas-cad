---
title: "RhinoCommon Samples — Curvas (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, geometria/curvas]
palabras-clave: [rhinopython, curvas, nurbs, operaciones]
sources: [raw/rhinopy/Add Circle.md, raw/rhinopy/Add Line.md, raw/rhinopy/Add NURBS Curve.md, raw/rhinopy/Add NURBS Circle.md, raw/rhinopy/Add Arrowheads to Curves.md, raw/rhinopy/Circle Center.md, raw/rhinopy/Curve Bounding Box.md, raw/rhinopy/Curve Deviation.md, raw/rhinopy/Divide Curve by Segments.md, raw/rhinopy/Divide Curve Straight.md, raw/rhinopy/Extend Curve.md, raw/rhinopy/Fillet Curves.md, raw/rhinopy/Find Curve Parameter At Point.md, raw/rhinopy/Find point on curve at distance.md, raw/rhinopy/Find point on curve at distance 1.md, raw/rhinopy/Hatch Curve.md, raw/rhinopy/Increase NURBS Curve Degree.md, raw/rhinopy/Offset Curve.md, raw/rhinopy/Reparameterize Curves.md, raw/rhinopy/Reverse Curve.md, raw/rhinopy/Tween Curve.md, raw/rhinopy/Create Contour Curves.md, raw/rhinopy/Surface from Edge Curves.md]
created: 2026-05-04
updated: 2026-10-13
---

22 samples de RhinoCommon sobre creación, consulta y modificación de curvas en Python. Usan `Rhino.Geometry` directamente con el patrón `scriptcontext.doc.Objects.Add*()`.

## Creación de curvas

| Sample | Método clave | Notas |
|--------|-------------|-------|
| Add Circle | `Circle(center, radius)` → `doc.Objects.AddCircle(c)` | — |
| Add Line | `Point3d` + `GetPoint` + `doc.Objects.AddLine` | Valida con `Line.IsTiny` |
| Add NURBS Curve | `NurbsCurve.Create(isPeriodic, degree, points)` | `Point3dList`, `AddCurve` |
| Add NURBS Circle | `NurbsCurve(3, False, 9)`, `Points.SetPoint(i,x,y,z,w)`, knots manuales | NURBS desde cero con pesos |
| Add Arrowheads to Curves | `ObjectDecoration` en `ObjectAttributes` | Decorador sobre línea existente |
| Hatch Curve | `Hatch.Create(curve, patternIndex, rotation, scale)`, `doc.Objects.AddHatch` | Curva cerrada y plana |
| Tween Curve | `Curve.CreateTweenCurves(c1, c2, numCurves)` | Interpola entre dos curvas |
| Surface from Edge Curves | `Brep.CreateEdgeSurface(curves)`, `doc.Objects.AddBrep` | Genera Brep desde bordes |

## Consulta y análisis

| Sample | Método clave |
|--------|-------------|
| Circle Center | `Curve.TryGetCircle(out c)` → `c.Center` |
| Curve Bounding Box | `Curve.GetBoundingBox(plane)` — versión orientada al plano |
| Curve Deviation | `rs.CurveDeviation(id1, id2)` → tupla con min/max/avg |
| Find Curve Parameter At Point | `Curve.ClosestPoint(pt, out t)` → t del punto más cercano |
| Find point on curve at distance | `Curve.GetLength()`, `Curve.PointAtLength(d)` |
| Divide Curve by Segments | `Curve.DivideByCount(n, includeEnds)` → params t → `PointAt(t)` |

## Modificación de curvas

| Sample | Método clave |
|--------|-------------|
| Extend Curve | `Curve.Extend(CurveEnd, CurveExtensionStyle, objects)` |
| Fillet Curves | `Curve.CreateFilletCurves(c1, p1, c2, p2, radius, ...)` |
| Increase NURBS Degree | `Curve.ToNurbsCurve()` → `nc.IncreaseDegree(d)` → `Objects.Replace` |
| Offset Curve | `Curve.Offset(plane, dist, tol, CurveOffsetCornerStyle)` |
| Reparameterize | `curve.Domain = Interval(a, b)` → `Objects.Replace` |
| Reverse Curve | `nc.Reverse()` → `Objects.Replace` |
| Divide Curve Straight | `Intersection.CurveBrep` con esfera → `Curve.Split` |
| Create Contour Curves | `Brep.CreateContourCurves(brep, pt, normal, interval)` |

## Conexiones

- Mapas: [[Mapa - Curvas]] · [[Mapa - Programación]]
- [[wiki/concepts/rhinocommon-document-api]] — patrón scriptcontext/doc.Objects
- [[wiki/concepts/curvas-nurbs]] — teoría NURBS
- [[wiki/concepts/rhinocommon-interseccion-api]] — Intersection.CurveBrep
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Circle: [[Add Circle|Python]] · [[Add Circle (cs)|C#]]
- Add Line: [[Add Line|Python]] · [[Add Line (cs)|C#]]
- Add NURBS Curve: [[Add NURBS Curve|Python]] · [[Add NURBS Curve (cs)|C#]]
- Add NURBS Circle: [[Add NURBS Circle|Python]] · [[Add NURBS Circle (cs)|C#]]
- Add Arrowheads to Curves: [[Add Arrowheads to Curves|Python]] · [[Add Arrowheads to Curves (cs)|C#]]
- Circle Center: [[Circle Center|Python]] · [[Circle Center (cs)|C#]]
- Curve Bounding Box: [[Curve Bounding Box|Python]] · [[Curve Bounding Box (cs)|C#]]
- Curve Deviation: [[Curve Deviation|Python]] · [[Curve Deviation (cs)|C#]]
- Divide Curve by Segments: [[Divide Curve by Segments|Python]] · [[Divide Curve by Segments (cs)|C#]]
- Divide Curve Straight: [[Divide Curve Straight|Python]] · [[Divide Curve Straight (cs)|C#]]
- Extend Curve: [[Extend Curve|Python]] · [[Extend Curve (cs)|C#]]
- Fillet Curves: [[Fillet Curves|Python]] · [[Fillet Curves (cs)|C#]]
- Find Curve Parameter At Point: [[Find Curve Parameter At Point|Python]] · [[Find Curve Parameter At Point (cs)|C#]]
- Find point on curve at distance: [[Find point on curve at distance|Python]] · [[Find point on curve at distance (cs)|C#]]
- Find point on curve at distance: [[Find point on curve at distance|Python]] · [[Find point on curve at distance (cs)|C#]] · [[Find point on curve at distance 1|copia repetida del recorte]]
- Hatch Curve: [[Hatch Curve|Python]] · [[Hatch Curve (cs)|C#]]
- Increase NURBS Curve Degree: [[Increase NURBS Curve Degree|Python]] · [[Increase NURBS Curve Degree (cs)|C#]]
- Offset Curve: [[Offset Curve|Python]] · [[Offset Curve (cs)|C#]]
- Reparameterize Curves: [[Reparameterize Curves|Python]] · [[Reparameterize Curves (cs)|C#]]
- Reverse Curve: [[Reverse Curve|Python]] · [[Reverse Curve (cs)|C#]]
- Tween Curve: [[Tween Curve (cs)|C#]] · [[Tween Curve|recorte original]]
- Create Contour Curves: [[Create Contour Curves|Python]] · [[Create Contour Curves (cs)|C#]]
- Surface from Edge Curves: [[Surface from Edge Curves|Python]] · [[Surface from Edge Curves (cs)|C#]]
