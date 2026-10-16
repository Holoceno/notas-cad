---
title: "RhinoCommon — API de Anotaciones y Dimensiones"
type: concept
tags: [tipo/concepto, software/rhinocommon, lenguaje/python, rhino/anotaciones, fabricacion/planos]
palabras-clave: [rhinopython, anotaciones, dimensiones, texto, hatch, leader, annotation]
sources: [raw/rhinopy/Add Annotation Text.md, raw/rhinopy/Add Leader.md, raw/rhinopy/Add Linear Dimension.md, raw/rhinopy/Add Linear Dimension2.md, raw/rhinopy/Add Radial Dimension.md, raw/rhinopy/Change Dimension Style.md, raw/rhinopy/Edit Text.md, raw/rhinopy/Explode Hatch.md, raw/rhinopy/Hatch Curve.md]
created: 2026-05-04
updated: 2026-10-13
---

RhinoCommon expone anotaciones via `doc.Objects.Add*` con tipos en `Rhino.Geometry` y `Rhino.DocObjects`.

## Texto

```python
# Añadir texto
text_id = doc.Objects.AddText(
    text="Hola",
    plane_or_point=location,  # Point3d o Plane
    height=1.0,
    fontName="Arial",
    bold=False,
    italic=False
)

# Editar texto existente
obj = GetOneObject(filter=ObjectType.Annotation)
annotation = obj.Geometry  # TextEntity
annotation.PlainText = "Nuevo texto"
obj.CommitChanges()
```

## Dimensiones lineales

```python
import Rhino.Geometry as g

plane = g.Plane.WorldXY

# Proyectar puntos 3D al plano 2D de anotación
b0, u0, v0 = plane.ClosestParameter(pt3d_a)
b1, u1, v1 = plane.ClosestParameter(pt3d_b)

pt0 = g.Point2d(u0, v0)
pt1 = g.Point2d(u1, v1)
offset = g.Point2d((u0+u1)/2, v0 + 3.0)

dim = g.LinearDimension(plane, pt0, pt1, offset)
doc.Objects.AddLinearDimension(dim)
```

## Leader (línea guía)

```python
plane = Rhino.Geometry.Plane.WorldXY
points_2d = [
    Rhino.Geometry.Point2d(0, 0),
    Rhino.Geometry.Point2d(5, 3),
    Rhino.Geometry.Point2d(10, 3)
]
doc.Objects.AddLeader("Texto de la guía", plane, points_2d)
```

## Hatches

```python
# Prerequisitos: curva cerrada y plana
if not curve.IsClosed or not curve.IsPlanar(): return

pattern_index = doc.HatchPatterns.CurrentHatchPatternIndex
hatches = Rhino.Geometry.Hatch.Create(
    curve, pattern_index,
    rotation=0.0,
    scale=1.0
)
for h in hatches:
    doc.Objects.AddHatch(h)
```

`Hatch.Explode()` descompone el hatch en partes constitutivas; cada pieza se identifica por su `ObjectType` (Point, Curve, Brep).

## Cambiar estilo de dimensión a todos los objetos

```python
style_id = doc.DimStyles.CurrentDimensionStyle.Id
settings = Rhino.DocObjects.ObjectEnumeratorSettings()
for obj in doc.Objects.GetObjectList(settings):
    if isinstance(obj, Rhino.DocObjects.AnnotationObjectBase):
        obj.AnnotationGeometry.DimensionStyleId = style_id
        obj.CommitChanges()
```

## Jerarquía de tipos

```
AnnotationObjectBase
 ├── TextObject         (AddText)
 ├── LinearDimensionObject  (AddLinearDimension)
 ├── RadialDimensionObject  (AddRadialDimension)
 └── LeaderObject       (AddLeader)
```

## Conexiones

- Mapas: [[Mapa - Visualización y anotaciones]] · [[Mapa - CAD 2D y planos]] · [[Mapa - Programación]]
- [[wiki/sources/2026-05-04-rhinopy-anotaciones]] — todos los samples de anotaciones
- [[wiki/concepts/rhinocommon-document-api]] — doc.Objects.Add*
- [[wiki/entities/rhinocommon]] — SDK fuente
