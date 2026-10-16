---
title: "RhinoCommon Samples — Anotaciones (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, rhino/anotaciones]
palabras-clave: [rhinopython, anotaciones, dimensiones, texto, hatch, leader]
sources: [raw/rhinopy/Add Annotation Text.md, raw/rhinopy/Add Leader.md, raw/rhinopy/Add Linear Dimension.md, raw/rhinopy/Add Linear Dimension2.md, raw/rhinopy/Add Radial Dimension.md, raw/rhinopy/Change Dimension Style.md, raw/rhinopy/Edit Text.md, raw/rhinopy/Explode Hatch.md, raw/rhinopy/Hatch Curve.md]
created: 2026-05-04
updated: 2026-10-13
---

9 samples de RhinoCommon sobre creación y edición de anotaciones: texto, dimensiones lineales y radiales, líderes, hatches.

## Texto

### Add Annotation Text
```python
text_id = doc.Objects.AddText(
    "Hello Rhino!",   # string
    location,         # Point3d
    height,           # float
    fontName,         # string
    bold, italic      # bool
)
```

### Edit Text
```python
obj = GetOneObject(filter=ObjectType.Annotation)
annotation = obj.Geometry  # TextEntity
annotation.PlainText = "Nuevo texto"
obj.CommitChanges()
```

## Dimensiones lineales

### Add Linear Dimension (interactivo)
```python
# Usando helper GetLinearDimension para captura interactiva
result, dim = GetLinearDimension(...)
doc.Objects.AddLinearDimension(dim)
```

### Add Linear Dimension2 (desde puntos 3D)
```python
plane = Rhino.Geometry.Plane.WorldXY
# Proyectar puntos 3D al plano 2D de anotación
b0, u0, v0 = plane.ClosestParameter(pt_3d_a)
b1, u1, v1 = plane.ClosestParameter(pt_3d_b)
pt0_2d = Rhino.Geometry.Point2d(u0, v0)
pt1_2d = Rhino.Geometry.Point2d(u1, v1)
offset_2d = Rhino.Geometry.Point2d(u0, v0 + 3)
dim = Rhino.Geometry.LinearDimension(plane, pt0_2d, pt1_2d, offset_2d)
doc.Objects.AddLinearDimension(dim)
```

### Add Radial Dimension
Obtiene la curva seleccionada → `TryGetCircle` → curvatura → `AddRadialDimension`.

## Leader

```python
plane = Rhino.Geometry.Plane.WorldXY
points_2d = [Rhino.Geometry.Point2d(0,0), Rhino.Geometry.Point2d(5,3)]
doc.Objects.AddLeader("texto", plane, points_2d)
```

## Hatches

```python
# Requiere curva cerrada y plana
if not curve.IsClosed or not curve.IsPlanar(): return
pattern_index = doc.HatchPatterns.CurrentHatchPatternIndex
hatches = Rhino.Geometry.Hatch.Create(curve, pattern_index, rotation=0, scale=1.0)
for h in hatches:
    doc.Objects.AddHatch(h)
```

`Hatch.Explode()` descompone en geometrías constitutivas (puntos, curvas, Breps) según el tipo de cada pieza.

## Estilos de dimensión

```python
current_style_id = doc.DimStyles.CurrentDimensionStyle.Id
settings = Rhino.DocObjects.ObjectEnumeratorSettings()
for obj in doc.Objects.GetObjectList(settings):
    if isinstance(obj, Rhino.DocObjects.AnnotationObjectBase):
        obj.AnnotationGeometry.DimensionStyleId = current_style_id
        obj.CommitChanges()
```

## Conexiones

- Mapas: [[Mapa - Visualización y anotaciones]] · [[Mapa - Programación]]
- [[wiki/concepts/rhinocommon-anotaciones-api]] — API de anotaciones detallada
- [[wiki/concepts/rhinocommon-document-api]] — doc.Objects.Add*
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Annotation Text: [[Add Annotation Text|Python]] · [[Add Annotation Text (cs)|C#]]
- Add Leader: [[Add Leader|Python]] · [[Add Leader (cs)|C#]]
- Add Linear Dimension: [[Add Linear Dimension|Python]] · [[Add Linear Dimension (cs)|C#]]
- Add Linear Dimension2: [[Add Linear Dimension2 (py)|Python]] · [[Add Linear Dimension2 (cs)|C#]] · [[Add Linear Dimension2|recorte original]]
- Add Radial Dimension: [[Add Radial Dimension (py)|Python]] · [[Add Radial Dimension (cs)|C#]] · [[Add Radial Dimension|recorte original]]
- Change Dimension Style: [[Change Dimension Style|Python]] · [[Change Dimension Style (cs)|C#]]
- Edit Text: [[Edit Text|Python]] · [[Edit Text (cs)|C#]]
- Explode Hatch: [[Explode Hatch|Python]] · [[Explode Hatch (cs)|C#]]
- Hatch Curve: [[Hatch Curve|Python]] · [[Hatch Curve (cs)|C#]]
