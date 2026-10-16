---
title: "Tipos de Geometría en RhinoCommon"
type: concept
tags: [tipo/concepto, software/rhinocommon, lenguaje/csharp, software/grasshopper]
palabras-clave: [estructuras, clases, jerarquia, geometria]
sources: [raw/rhinocommon/Chapter 3 RhinoCommon Geometry.md]
created: 2026-05-03
updated: 2026-10-13
---

RhinoCommon organiza los tipos de geometría en dos grandes categorías: **estructuras** (value types, livianas) y **clases** (reference types, con jerarquía de herencia). Entender esta distinción es clave para trabajar con la API de Rhino.

## Estructuras — Geometría liviana (Lightweight)

Se pasan por copia (valor). Representaciones matemáticas directas. Se pueden convertir a NURBS con `.ToNurbsCurve()` o `.ToNurbsSurface()`.

**Puntos y vectores:**
| Tipo | Descripción |
|------|-------------|
| `Point2d` | Punto en espacio de parámetros (u,v) |
| `Point3d` | Punto en espacio 3D — el más usado |
| `Point4d` | Punto de control con peso (x,y,z,w) |
| `Vector2d` | Vector en 2D |
| `Vector3d` | Vector en 3D |

**Curvas livianas:**
`Line`, `Arc`, `Circle`, `Ellipse`, `Polyline`

**Superficies livianas:**
`Sphere`, `Cylinder`, `Cone`, `Torus`

**Otras estructuras:**
`Plane`, `Interval`, `BoundingBox`, `Box`, `Transform` (matriz 4×4), `Rectangle3d`

## Clases — Geometría completa (Full)

Se pasan por referencia. Tienen herencia. La raíz es `GeometryBase` (abstracta).

```
GeometryBase
 ├── Curve (abstracta)
 │    ├── NurbsCurve       ← curva NURBS completa
 │    ├── ArcCurve         ← arco/círculo como curva
 │    ├── LineCurve        ← línea como curva
 │    ├── PolylineCurve    ← polilínea como curva
 │    └── PolyCurve        ← segmentos unidos
 ├── Surface (abstracta)
 │    ├── NurbsSurface     ← superficie NURBS completa
 │    ├── PlaneSurface     ← superficie plana
 │    ├── RevSurface       ← superficie de revolución
 │    └── Extrusion        ← extrusión (más ligera que NurbsSurface)
 ├── Mesh                  ← malla poligonal
 └── Brep                  ← polisuperficie / sólido
```

**Clases abstractas** (`Curve`, `Surface`, `GeometryBase`): no se pueden instanciar directamente. Definen funcionalidad común para todas las derivadas.

## Formas de crear instancias

1. **Constructor con `new`**: `new NurbsCurve(...)`, `new LineCurve(p0, p1)`
2. **Método estático `Create`** de la clase: `NurbsCurve.Create(isPeriodic, degree, points)`
3. **Método estático de la clase padre**: `Curve.CreateInterpolatedCurve(points, degree)`
4. **Valor de retorno de otro método**: `srf.IsoCurve(0, t)`, `crv.Offset(...)`

## Transformaciones en GeometryBase

Todos los objetos derivados de `GeometryBase` heredan:
- `.Scale(factor)`
- `.Rotate(angle, axis, center)`
- `.Translate(vector)`
- `.Transform(xform)` — acepta cualquier `Transform` (matriz 4×4)

## Mesh: estructura especial

El `Mesh` no es NURBS. Sus datos son:
- `Vertices`: lista de `Point3f` (precisión simple)
- `Faces`: lista de `MeshFace` (triángulos o cuadriláteros)
- `Normals`, `FaceNormals`
- Topología: `TopologyEdges` para navegación de conectividad

## Connections

- Mapas: [[Mapa - Programación]] · [[Mapa - Grasshopper]]
- [[wiki/concepts/brep-polisuperficies]] — `Brep` como clase de geometría completa
- [[wiki/concepts/transformaciones-geometricas]] — `Transform` estructura implementa matrices 4×4
- [[wiki/concepts/curvas-nurbs]] — `NurbsCurve` como implementación de las curvas NURBS
- [[wiki/entities/rhinocommon]] — SDK fuente
- [[wiki/sources/2026-05-03-rhinocommon-geometry-cap3]] — fuente primaria
