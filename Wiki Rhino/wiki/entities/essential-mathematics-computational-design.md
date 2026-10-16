---
title: "Essential Mathematics for Computational Design"
type: entity
tags: [tipo/entidad, matematicas, software/rhinocommon, software/grasshopper]
palabras-clave: [mcneel, referencia, libro]
sources: [raw/rhinocommon/1 Matemáticas vectoriales.md, raw/rhinocommon/2 Matrices y transformaciones.md, raw/rhinocommon/3 Curvas y superficies paramétricas.md]
created: 2026-05-03
updated: 2026-10-13
---

Publicación de referencia de Robert McNeel & Associates que cubre las matemáticas que fundamentan el diseño computacional en Rhino y Grasshopper. Disponible gratuitamente en el sitio de desarrolladores de Rhino. Los tutoriales incluyen implementaciones en VB, Python y C# para componentes de Grasshopper.

**Descarga:** https://www.rhino3d.com/download/rhino/6/essentialmathematics/
**Online (ES):** https://developer.rhino3d.com/guides/general/essential-mathematics/

## Estructura del libro (capítulos ingestados)

| Capítulo | Tema | Estado wiki |
|----------|------|-------------|
| Ch. 1 | Matemáticas vectoriales | ✓ ingestado |
| Ch. 2 | Matrices y transformaciones | ✓ ingestado |
| Ch. 3 | Curvas y superficies paramétricas | ✓ ingestado |

## Conexión con RhinoCommon

Cada concepto del libro tiene una implementación directa en la API:
- Vectores → `Vector3d`, `Point3d`
- Matrices 4×4 → `Transform`
- Curvas NURBS → `NurbsCurve`
- Superficies NURBS → `NurbsSurface`
- Brep → `Brep`

## Connections

- Mapas: [[Mapa - Matemáticas]] · [[Mapa - Programación]] · [[Mapa - Grasshopper]]
- [[wiki/concepts/vector-mathematics]] — Ch. 1
- [[wiki/concepts/transformaciones-geometricas]] — Ch. 2
- [[wiki/concepts/curvas-nurbs]] — Ch. 3
- [[wiki/concepts/superficies-nurbs]] — Ch. 3
- [[wiki/entities/rhinocommon]] — SDK que implementa estos conceptos
