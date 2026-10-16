---
title: "RhinoCommon Samples — Operaciones Espaciales (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, geometria/transformaciones, geometria/intersecciones]
palabras-clave: [rhinopython, transformaciones, interseccion, rtree, array, grupos]
sources: [raw/rhinopy/Copy Groups.md, raw/rhinopy/Duplicate Object.md, raw/rhinopy/Calculate Curve Intersections.md, raw/rhinopy/Constrained Copy.md, raw/rhinopy/Intersect Lines.md, raw/rhinopy/Array By Distance.md, raw/rhinopy/Closest Point Calculation with RTree.md, raw/rhinopy/Curve Surface Intersection.md]
created: 2026-05-04
updated: 2026-10-13
---

8 samples de RhinoCommon sobre copias, transformaciones, intersecciones y búsqueda espacial.

## Copias y transformaciones

### Duplicate Object
```python
obj = GetOneObject("Select object")
geom = obj.DuplicateGeometry()
scriptcontext.doc.Objects.Add(geom)
```

### Constrained Copy
```python
go = GetObject("Select curve")
gp = GetPoint("Destination")
gp.Constrain(line)  # restringe el movimiento a una línea o plano
gp.Get()
xform = Rhino.Geometry.Transform.Translation(gp.Point() - start)
scriptcontext.doc.Objects.Transform(obj_id, xform, copy=True)
```

### Copy Groups — copia preservando grupos
```python
obj = GetOneObject()
groups = obj.Attributes.GetGroupList()
copy_id = ... # duplicar geometría
for gi in groups:
    new_group = doc.Groups.Add()
    doc.Objects.AddToGroup(copy_id, new_group)
```

### Array By Distance
Combina `GetPoint` con `DynamicDraw` + `OptionDouble` para distancia de separación; aplica `Transform.Translation` iterativo hasta que el usuario confirme.

## Intersecciones

### Calculate Curve Intersections
```python
events = Rhino.Geometry.Intersection.CurveCurve(c1, c2, tolerance, overlapTol)
for e in events:
    if e.IsPoint:
        scriptcontext.doc.Objects.AddPoint(e.PointA)
    elif e.IsOverlap:
        scriptcontext.doc.Objects.AddLine(e.PointA, e.PointB)
```

### Intersect Lines
```python
if line1.Direction.IsParallelTo(line2.Direction) != 0:
    return  # paralelas
rc, t1, t2 = Rhino.Geometry.Intersection.LineLine(line1, line2)
if rc:
    pt = line1.PointAt(t1)
    scriptcontext.doc.Objects.AddPoint(pt)
```

### Curve Surface Intersection
```python
# Usando rhinoscriptsyntax
ok, crv_params, brep_pts = rs.CurveBrepIntersect(crv_id, brep_id)
for pt in brep_pts:
    scriptcontext.doc.Objects.AddPoint(pt)
```

## Búsqueda espacial — RTree

Estructura de datos que acelera búsquedas de punto más cercano en conjuntos grandes:

```python
tree = Rhino.Geometry.RTree()
for i, vertex in enumerate(mesh.Vertices):
    tree.Insert(vertex, i)

def callback(sender, e):
    data = e.Tag
    dist = data.Point.DistanceTo(data.Mesh.Vertices[e.Id])
    if data.Index == -1 or dist < data.Distance:
        e.SearchSphere = Rhino.Geometry.Sphere(data.Point, dist)  # contrae la esfera
        data.Index = e.Id
        data.Distance = dist

sphere = Rhino.Geometry.Sphere(query_point, initial_radius)
tree.Search(sphere, callback, search_data)
# search_data.Index = índice del vértice más cercano
```

La esfera se contrae en cada hit, podando ramas del árbol espacial. Complejidad O(log n) vs O(n) de búsqueda lineal.

## Conexiones

- Mapas: [[Mapa - Transformaciones]] · [[Mapa - Intersecciones y booleanos]] · [[Mapa - Programación]]
- [[wiki/concepts/rhinocommon-interseccion-api]] — Intersection.CurveCurve, LineLine, CurveBrep
- [[wiki/concepts/rhinocommon-document-api]] — doc.Objects.Transform, Add
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Copy Groups: [[Copy Groups|Python]] · [[Copy Groups (cs)|C#]]
- Duplicate Object: [[Duplicate Object|Python]] · [[Duplicate Object (cs)|C#]]
- Calculate Curve Intersections: [[Calculate Curve Intersections|Python]] · [[Calculate Curve Intersections (cs)|C#]]
- Constrained Copy: [[Constrained Copy|Python]] · [[Constrained Copy (cs)|C#]]
- Intersect Lines: [[Intersect Lines|Python]] · [[Intersect Lines (cs)|C#]]
- Array By Distance: [[Array By Distance|Python]] · [[Array By Distance (cs)|C#]]
- Closest Point Calculation with RTree: [[Closest Point Calculation with RTree|Python]] · [[Closest Point Calculation with RTree (cs)|C#]]
- Curve Surface Intersection: [[Curve Surface Intersection|Python]] · [[Curve Surface Intersection (cs)|C#]]
