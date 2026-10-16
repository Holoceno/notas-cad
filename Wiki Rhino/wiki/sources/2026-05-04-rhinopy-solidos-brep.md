---
title: "RhinoCommon Samples — Sólidos y Brep (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, geometria/brep, geometria/intersecciones]
palabras-clave: [rhinopython, brep, solidos, booleanas, topologia]
sources: [raw/rhinopy/Add Brep Box.md, raw/rhinopy/Add Twisted Cube.md, raw/rhinopy/Brep from Curve Bounding Box.md, raw/rhinopy/Boolean Difference.md]
created: 2026-05-04
updated: 2026-10-13
---

4 samples de RhinoCommon sobre construcción de Brep (desde caja y manual) y operaciones booleanas.

## Add Brep Box

```python
pt_min = Rhino.Geometry.Point3d(0, 0, 0)
pt_max = Rhino.Geometry.Point3d(10, 10, 10)
bbox = Rhino.Geometry.BoundingBox(pt_min, pt_max)
brep = bbox.ToBrep()
scriptcontext.doc.Objects.AddBrep(brep)
```

## Add Twisted Cube — construcción manual de Brep

El ejemplo más completo de la colección: construye un Brep desde cero exponiendo toda la estructura geometría+topología:

```
# Capa de geometría:
brep.Vertices.Add(point, tolerance)     — 8 vértices
brep.Curves3D.Add(lineCurve)           — 12 curvas de arista 3D
brep.AddSurface(nurbsSurface)          — 6 superficies (una por cara)

# Capa de topología:
brep.Edges.Add(v_start, v_end, c3d_index, tolerance)   — 12 edges
face = brep.Faces.Add(surface_index)                    — 6 faces
loop = brep.Loops.Add(BrepLoopType.Outer, face)         — 1 loop por face
trim = brep.Trims.Add(edge, reverse, loop, c2d_index)  — 4 trims por face
trim.IsoStatus = IsoStatus.South/East/North/West
trim.TrimType = BrepTrimType.Mated
trim.SetTolerances(0, 0)
```

Cada `Face` necesita curvas de trim 2D (`Curves2D`) en el espacio de parámetros de la superficie. La orientación del loop es CCW (anti-horaria) cuando se ve desde el exterior.

## Brep from Curve Bounding Box

```python
curve = obj_ref.Curve()
bbox = curve.GetBoundingBox(accurate=True)
if not bbox.IsDegenerate(tolerance):
    brep = Rhino.Geometry.Brep.CreateFromBox(bbox)
    scriptcontext.doc.Objects.AddBrep(brep)
```

## Boolean Difference

```python
breps_a = [ref.Brep() for ref in set_a]
breps_b = [ref.Brep() for ref in set_b]
result = Rhino.Geometry.Brep.CreateBooleanDifference(breps_a, breps_b, tolerance)
for b in result:
    scriptcontext.doc.Objects.AddBrep(b)
```

## Conexiones

- Mapas: [[Mapa - Brep y sólidos]] · [[Mapa - Intersecciones y booleanos]] · [[Mapa - Programación]]
- [[wiki/concepts/brep-polisuperficies]] — estructura de datos del Brep (geometría + topología)
- [[wiki/concepts/rhinocommon-document-api]] — doc.Objects.AddBrep
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Brep Box: [[Add Brep Box|Python]] · [[Add Brep Box (cs)|C#]]
- Add Twisted Cube: [[Add Twisted Cube (cs)|C#]] · [[Add Twisted Cube|recorte original]]
- Brep from Curve Bounding Box: [[Brep from Curve Bounding Box|Python]] · [[Brep from Curve Bounding Box (cs)|C#]]
- Boolean Difference: [[Boolean Difference|Python]] · [[Boolean Difference (cs)|C#]]
