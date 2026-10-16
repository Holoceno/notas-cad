---
tags: [tipo/apunte, software/cadquery, software/rhinocommon, lenguaje/python]
---

# CadQuery vs RhinoCommon

| Idea | RhinoCommon / Grasshopper | CadQuery |
|---|---|---|
| Plano de trabajo | `Plane` | `cq.Workplane` (se encadena; offset y rotate son **relativos**) |
| Geometría | NURBS (Rhino kernel) | B-rep de OpenCascade |
| Loft / Sweep | `Brep.CreateFromLoft`, `Sweep1` | `.loft()`, `.sweep()` |
| Booleanos | `Brep.CreateBooleanDifference` | `.cut()`, `.union()`, `.intersect()` |
| Seleccionar caras | por índice o a mano | selectores de texto: `">Z"`, `"|Z"`, `"<X"` |
| Vista en vivo | lienzo de Grasshopper | OCP CAD Viewer en Cursor (`show(...)`) |

## Lo que aprendí con los ejemplos
- Booleanos con muchas piezas: juntar todo en un `Compound` y cortar **una vez**.
- Los fillets fallan con facilidad: hazlos **antes** de los cortes complicados.
- Limitaciones: sin SubD, sin Kangaroo, superficies libres más difíciles. Para lattices/gyroides → Blender Geometry Nodes.

## En la Wiki Rhino
- [[tipos-geometria-rhinocommon|Tipos de geometría en RhinoCommon]]: el equivalente a los `Shape` / `Workplane` de CadQuery
- [[brep-polisuperficies|Brep y polisuperficies]]: CadQuery también trabaja con B-rep (OpenCascade), misma idea de caras, aristas y vértices
- [[curvas-nurbs|Curvas NURBS]] · [[superficies-nurbs|Superficies NURBS]]: lo que hay detrás de `spline`, `loft` y `sweep`
- [[transformaciones-geometricas|Transformaciones (matrices 4×4)]]: lo que hace `transformed(rotate=...)` por dentro


## Rendimiento: 2D antes que 3D (2026-10-12)
Panel con 1.500 agujeros: cortando sólidos uno a uno → se colgaba. Dibujando **una cara 2D** con todos los huecos (`cq.Face.makeFromWires(borde, huecos)`) y extruyendo una vez → 1,5 s.
Regla: si el patrón es plano, resuélvelo en 2D y extruye al final. (En Grasshopper es lo mismo: Boundary Surfaces con curvas internas + Extrude, en vez de Solid Difference.)
