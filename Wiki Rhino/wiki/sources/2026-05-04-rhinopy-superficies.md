---
title: "RhinoCommon Samples — Superficies (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, geometria/superficies, geometria/curvatura]
palabras-clave: [rhinopython, superficies, nurbs, isocurva, curvatura]
sources: [raw/rhinopy/Calculate Surface Curvature.md, raw/rhinopy/Create Surface From Points and Knots.md, raw/rhinopy/Duplicate Surface Border.md, raw/rhinopy/Extend Surface.md, raw/rhinopy/Extract Isocurve.md, raw/rhinopy/Furthest Z on Surface given X Y.md]
created: 2026-05-04
updated: 2026-10-13
---

6 samples de RhinoCommon sobre consulta, creación y modificación de superficies NURBS.

## Create Surface From Points and Knots

Construcción directa de `NurbsSurface` especificando puntos de control y vectores de nodos:

```python
from Rhino.Geometry import Point3d, NurbsSurface, ControlPoint
from scriptcontext import doc

nurbs_surface = NurbsSurface.Create(
    dim,             # dimensión (3 = 3D)
    isRational,      # False para no racional
    u_degree + 1,    # orden U (grado + 1)
    v_degree + 1,    # orden V
    u_cv_count,      # nº puntos de control U
    v_cv_count       # nº puntos de control V
)

# Knots
for i in range(nurbs_surface.KnotsU.Count):
    nurbs_surface.KnotsU[i] = u_knot[i]
for j in range(nurbs_surface.KnotsV.Count):
    nurbs_surface.KnotsV[j] = v_knot[j]

# Control points
for i in range(nurbs_surface.Points.CountU):
    for j in range(nurbs_surface.Points.CountV):
        nurbs_surface.Points.SetControlPoint(i, j, ControlPoint(pts[i][j]))

if nurbs_surface.IsValid:
    doc.Objects.AddSurface(nurbs_surface)
```

## Extract Isocurve

Extrae curva isoparamétrica en dirección U o V con UI interactiva:

```python
b, u, v = surface.ClosestPoint(point)
direction = 1 if toggle.CurrentValue else 0  # 0=U, 1=V
iso_curve = surface.IsoCurve(direction, u if direction == 1 else v)
doc.Objects.AddCurve(iso_curve)
```
Usa `GetPoint.Constrain(surface, False)` + `OptionToggle` para elegir dirección.

## Calculate Surface Curvature

```python
surface_curvature = rs.SurfaceCurvature(surface_id, (u, v))
point, normal, kappa_u, dir_u, kappa_v, dir_v, gaussian, mean = surface_curvature
```
Retorna curvatura principal máxima y mínima (κu, κv), gaussiana (κu×κv) y media ((κu+κv)/2).

## Otros samples

| Sample | API clave |
|--------|-----------|
| Duplicate Surface Border | `Brep.DuplicateEdgeCurves()` → `Curve.JoinCurves()` |
| Extend Surface | `Surface.Extend(IsoStatus, length, smooth)` → `Surface.CreateFromSurface(srf)` |
| Furthest Z on Surface given X Y | `Intersection.ProjectPointsToBreps(breps, pts, dir, tol)` → máx Z |

## Conexiones

- Mapas: [[Mapa - Superficies y NURBS]] · [[Mapa - Programación]]
- [[wiki/concepts/superficies-nurbs]] — teoría de superficies NURBS
- [[wiki/concepts/curvatura]] — curvatura gaussiana, media y principal
- [[wiki/concepts/rhinocommon-document-api]] — doc.Objects.AddSurface
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Calculate Surface Curvature: [[Calculate Surface Curvature|Python]] · [[Calculate Surface Curvature (cs)|C#]]
- Create Surface From Points and Knots: [[Create Surface From Points and Knots|Python]] · [[Create Surface From Points and Knots (cs)|C#]]
- Duplicate Surface Border: [[Duplicate Surface Border|Python]] · [[Duplicate Surface Border (cs)|C#]]
- Extend Surface: [[Extend Surface|Python]] · [[Extend Surface (cs)|C#]]
- Extract Isocurve: [[Extract Isocurve|Python]] · [[Extract Isocurve (cs)|C#]]
- Furthest Z on Surface given X Y: [[Furthest Z on Surface given X Y|Python]] · [[Furthest Z on Surface given X Y (cs)|C#]]
