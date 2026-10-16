---
title: "RhinoCommon — API de Intersección"
type: concept
tags: [tipo/concepto, software/rhinocommon, lenguaje/python, geometria/intersecciones]
palabras-clave: [rhinopython, interseccion, curvas, superficies, lineas, rtree, espacial]
sources: [raw/rhinopy/Calculate Curve Intersections.md, raw/rhinopy/Intersect Lines.md, raw/rhinopy/Curve Surface Intersection.md, raw/rhinopy/Closest Point Calculation with RTree.md, raw/rhinopy/Divide Curve Straight.md, raw/rhinopy/Furthest Z on Surface given X Y.md]
created: 2026-05-04
updated: 2026-10-13
---

`Rhino.Geometry.Intersection` es el namespace estático de RhinoCommon para cálculos de intersección entre tipos de geometría.

## Intersección curva-curva

```python
events = Rhino.Geometry.Intersection.CurveCurve(c1, c2, tolerance, overlapTol)
for e in events:
    if e.IsPoint:
        # intersección puntual
        scriptcontext.doc.Objects.AddPoint(e.PointA)
    elif e.IsOverlap:
        # solapamiento (segmento)
        scriptcontext.doc.Objects.AddLine(e.PointA, e.PointB)
```

Cada `IntersectionEvent` tiene `ParameterA` / `ParameterB` (params t en cada curva), `PointA` / `PointB` (puntos 3D).

## Intersección línea-línea

```python
if line1.Direction.IsParallelTo(line2.Direction) != 0:
    return  # paralelas, sin intersección

rc, t1, t2 = Rhino.Geometry.Intersection.LineLine(line1, line2)
if rc:
    pt_on_L1 = line1.PointAt(t1)
    pt_on_L2 = line2.PointAt(t2)
    # Si pt_on_L1 ≈ pt_on_L2 → intersecan; si no → líneas cruzadas en 3D
```

## Intersección curva-Brep

```python
# Versión rhinoscriptsyntax
ok, crv_params, brep_pts = rs.CurveBrepIntersect(crv_id, brep_id)
for pt in brep_pts:
    scriptcontext.doc.Objects.AddPoint(pt)

# Versión RhinoCommon directa
events = Rhino.Geometry.Intersection.CurveBrep(curve, brep, tolerance)
for e in events:
    scriptcontext.doc.Objects.AddCurve(e.OverlapCurve)  # solapamiento
```

## Proyección de puntos a Brep

```python
direction = Rhino.Geometry.Vector3d(0, 0, -1)  # proyectar hacia -Z
projected = Rhino.Geometry.Intersection.ProjectPointsToBreps(
    [brep],        # lista de Breps
    [query_pt],    # lista de puntos a proyectar
    direction,     # dirección de proyección
    tolerance
)
max_z = max(p.Z for p in projected)
```

## Intersección curva-esfera (para división)

```python
# Patrón "Divide Curve Straight": divide una curva en segmentos de longitud igual
sphere_brep = Rhino.Geometry.Sphere(current_pt, arc_length).ToBrep()
events = Rhino.Geometry.Intersection.CurveBrep(remaining_curve, sphere_brep, tol)
# El parámetro t del evento se usa para Split
t_params = [e.ParameterA for e in events if e.IsPoint]
segments = remaining_curve.Split(t_params)
```

## Búsqueda de punto más cercano con RTree

`RTree` es una estructura de datos espacial (R-Tree) que acelera búsquedas de vecino más cercano de O(n) a O(log n).

```python
# Construir el árbol (una vez)
tree = Rhino.Geometry.RTree()
for i, vertex in enumerate(mesh.Vertices):
    tree.Insert(vertex, i)

class SearchData:
    def __init__(self, mesh, point):
        self.Mesh = mesh
        self.Point = point
        self.Index = -1
        self.Distance = 0.0

def callback(sender, e):
    data = e.Tag
    dist = data.Point.DistanceTo(data.Mesh.Vertices[e.Id])
    if data.Index == -1 or dist < data.Distance:
        e.SearchSphere = Rhino.Geometry.Sphere(data.Point, dist)  # contrae la esfera
        data.Index = e.Id
        data.Distance = dist

# Búsqueda
data = SearchData(mesh, query_pt)
initial_r = query_pt.DistanceTo(mesh.Vertices[0]) * 1.1
tree.Search(Rhino.Geometry.Sphere(query_pt, initial_r), callback, data)
# data.Index = índice del vértice más cercano
```

La esfera de búsqueda se contrae en cada hit encontrado, podando eficientemente las ramas del árbol.

## Conexiones

- Mapas: [[Mapa - Intersecciones y booleanos]] · [[Mapa - Programación]]
- [[wiki/sources/2026-05-04-rhinopy-operaciones-espaciales]] — samples que usan Intersection
- [[wiki/sources/2026-05-04-rhinopy-curvas]] — Divide Curve Straight usa CurveBrep
- [[wiki/concepts/curvas-nurbs]] — parámetros t de curva
- [[wiki/concepts/rhinocommon-mesh-api]] — RTree opera sobre vértices de Mesh
- [[wiki/entities/rhinocommon]] — SDK fuente
