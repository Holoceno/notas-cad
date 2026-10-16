---
title: "rhinoscriptsyntax"
type: entity
tags: [tipo/entidad, software/rhinoscriptsyntax, software/rhinocommon, lenguaje/python]
palabras-clave: [rhinoscriptsyntax, rs, RhinoScript, coerce, coercecurve, Guid, ghdoc, scriptcontext]
sources: [raw/developer-rhino3d/rhinopython/Using RhinoCommon from Python.md, raw/developer-rhino3d/scripting/Grasshopper Scripting - Python.md]
created: 2026-10-13
updated: 2026-10-13
---

Librería de Python de McNeel (`import rhinoscriptsyntax as rs`) con funciones simples al estilo del antiguo RhinoScript: `rs.AddLine`, `rs.GetObject`, `rs.DivideCurve`. Por dentro **son scripts de Python que llaman a RhinoCommon**, así que no es otra API: es un atajo. Trabaja con **identificadores (Guid)** de objetos del documento, mientras que RhinoCommon trabaja con la geometría misma. Es más fácil para empezar; RhinoCommon da más control, más velocidad y funciona igual en C#.

## Detalles

### rs ↔ RhinoCommon

Equivalencias tomadas de las muestras oficiales que usan `rs` ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp]]):

| rhinoscriptsyntax | RhinoCommon | Muestra |
|---|---|---|
| `rs.GetObject("…", rs.filter.curve)` | `RhinoGet.GetOneObject("…", False, ObjectType.Curve)` | [[Offset Curve]] |
| `rs.coercecurve(id)` | `ObjRef.Curve()` o `doc.Objects.FindId(id).Geometry` | [[Reverse Curve]] |
| `rs.DivideCurve(id, n)` | `crv.DivideByCount(n, True)` + `crv.PointAt(t)` | [[Divide Curve by Segments]] |
| `rs.CurveDeviation(a, b)` | `Curve.GetDistancesBetweenCurves(...)` | [[Curve Deviation]] |
| `rs.SurfaceCurvature(id, (u, v))` | `Surface.CurvatureAt(u, v)` | [[Calculate Surface Curvature]] |
| `rs.AddLoftSrf(ids)` | `Brep.CreateFromLoft(...)` | [[Loft Surfaces]] |
| `rs.AddPlaneSurface(plano, u, v)` | `PlaneSurface(plano, intervaloU, intervaloV)` | [[Planar Surface]] |
| `rs.ObjectName(id, nombre)` | `obj.Attributes.Name = nombre` + `CommitChanges()` | [[Rename Object]] |

Las funciones `coerce…` (`coercecurve`, `coercebrep`, `coercemesh`) son el puente: convierten un Guid de `rs` en geometría de RhinoCommon, y permiten **mezclar** los dos estilos en un mismo script, como hacen varias muestras.

### En Grasshopper

En el componente de Python, las salidas convierten los Guid que devuelve `rs` en geometría. Las entradas con hint *ghdoc Object* hacen lo inverso. Mientras corre el script, `scriptcontext.doc` apunta a un documento interno de Grasshopper, no al de Rhino ([[wiki/sources/2026-10-13-guias-scripting-rhino8]]).

### ¿rs o RhinoCommon?

- `rs` para scripts cortos de Rhino y para aprender: menos líneas.
- RhinoCommon cuando se necesita algo que `rs` no tiene, velocidad (miles de objetos), o se va a pasar a C# o a un plugin. En C# **no existe** `rs`.

## Conexiones

- Mapas: [[Mapa - Programación]] · [[Mapa - Scripts, interfaz y archivos]]
- [[wiki/entities/rhinocommon]] · [[wiki/concepts/ecosistema-programacion-rhino]] · [[wiki/concepts/python-csharp-rhinocommon]]

## Fuentes

- [[Using RhinoCommon from Python]]: "las funciones de rhinoscriptsyntax son scripts de Python que usan RhinoCommon".
- [[Grasshopper Scripting - Python]]: conversión de Guid en el componente de Grasshopper.
- Tabla de equivalencias: armada por mí a partir de las muestras enlazadas. Los métodos de RhinoCommon de las filas *CurveDeviation*, *SurfaceCurvature* y *AddLoftSrf* no aparecen en esas muestras: confirmarlos en la API.
