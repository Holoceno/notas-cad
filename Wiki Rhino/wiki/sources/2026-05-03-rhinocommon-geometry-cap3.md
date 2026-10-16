---
title: "C# Essentials for Grasshopper Ch.3 — RhinoCommon Geometry"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/csharp, geometria/brep, geometria/mallas, geometria/nurbs]
palabras-clave: [geometria, nurbs, brep, mesh]
sources: [raw/rhinocommon/Chapter 3 RhinoCommon Geometry.md]
created: 2026-05-03
updated: 2026-10-13
---

Capítulo 3 de *Essential C# Scripting for Grasshopper* (McNeel). Cubre cómo se representan y manipulan los tipos de geometría de Rhino en el SDK de RhinoCommon usando C#.

**URL original:** https://developer.rhino3d.com/guides/grasshopper/csharp-essentials/3-rhinocommon-geometry/

## Temas cubiertos

**Estructuras de geometría** (value types — pasan por copia):
- `Point3d`, `Vector3d`, `Point2d`, `Point4d`
- `Line`, `Arc`, `Circle`, `Ellipse`, `Plane`, `Interval`
- `Sphere`, `Cylinder`, `Cone`, `Torus`
- `BoundingBox`, `Box`, `Transform` (matriz 4×4)
- Curvas ligeras: `Line`, `Arc`, `Circle`, `Polyline` → conversión a `NurbsCurve` con `.ToNurbsCurve()`
- Superficies ligeras: `Sphere`, `Cylinder`, `Cone`, `Torus` → conversión con `.ToNurbsSurface()`

**Jerarquía de clases de geometría** (reference types — se pasan por referencia):
- `GeometryBase` → `Curve` (abstracta) → `NurbsCurve`, `ArcCurve`, `LineCurve`, `PolylineCurve`
- `GeometryBase` → `Surface` (abstracta) → `NurbsSurface`, `PlaneSurface`, `RevSurface`, `Extrusion`
- `GeometryBase` → `Mesh`
- `GeometryBase` → `Brep`

**Mesh:** vértices (`Point3f`), caras (`MeshFace`), normales; topología de aristas; `GetNakedEdges()`, `IsPointInside()`

**Brep:** geometría (superficies 3D, curvas 3D de aristas, curvas 2D de recortes) + topología (faces, edges, vertices, trims, loops); navegación completa del grafo de conectividad

**Transformaciones:** `.Rotate()`, `.Scale()`, `.Translate()`, `.Transform(xform)` disponibles en todos los objetos derivados de `GeometryBase`

**Make2D:** `HiddenLineDrawing` para generar dibujos 2D desde geometría 3D

## Connections

- Mapas: [[Mapa - Superficies y NURBS]] · [[Mapa - Brep y sólidos]] · [[Mapa - Mallas y SubD]] · [[Mapa - Programación]]
- [[wiki/concepts/tipos-geometria-rhinocommon]] — jerarquía de tipos y estructuras
- [[wiki/concepts/brep-polisuperficies]] — data structure del Brep
- [[wiki/concepts/curvas-nurbs]] — curvas NURBS desde perspectiva de API
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

- Archivo original: [[Chapter 3 RhinoCommon Geometry]]
