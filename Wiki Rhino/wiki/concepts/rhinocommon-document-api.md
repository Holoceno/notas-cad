---
title: "RhinoCommon — Document API y scriptcontext"
type: concept
tags: [tipo/concepto, software/rhinocommon, lenguaje/python, rhino/documento]
palabras-clave: [rhinopython, scriptcontext, documento, api, objects]
sources: [raw/rhinopy — múltiples samples]
created: 2026-05-04
updated: 2026-10-13
---

En scripting Python con RhinoCommon, `scriptcontext.doc` es el punto de entrada al documento activo de Rhino. Equivale a `RhinoDoc` en el SDK .NET completo.

## Patrón base

```python
import Rhino
import scriptcontext
import System.Guid

def AddSomething():
    geom = Rhino.Geometry.Circle(Rhino.Geometry.Point3d(0, 0, 0), 5.0)
    
    id = scriptcontext.doc.Objects.AddCircle(geom)
    
    if id != System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure
```

Todos los métodos `Add*` retornan un `Guid`. `System.Guid.Empty` indica fallo.

## doc.Objects — métodos Add*

| Método | Tipo de geometría |
|--------|------------------|
| `AddPoint(pt)` | `Point3d` |
| `AddLine(pt0, pt1)` | dos `Point3d` |
| `AddCircle(circle)` | `Circle` |
| `AddCurve(curve)` | `Curve` / `NurbsCurve` / etc. |
| `AddSurface(srf)` | `Surface` / `NurbsSurface` |
| `AddBrep(brep)` | `Brep` |
| `AddMesh(mesh)` | `Mesh` |
| `AddSphere(sphere)` | `Sphere` |
| `AddHatch(hatch)` | `Hatch` |
| `AddPolyline(polyline)` | `Polyline` |
| `AddText(str, pt, h, ...)` | texto de anotación |
| `AddLinearDimension(dim)` | `LinearDimension` |
| `AddClippingPlane(plane, ...)` | plano de corte |

## doc.Objects — modificación

| Método | Descripción |
|--------|-------------|
| `Replace(id, geom)` | reemplaza geometría de objeto existente |
| `Transform(id, xform, copy)` | aplica transformación; `copy=True` duplica |
| `Delete(id, quiet)` | elimina objeto |
| `Select(id)` | selecciona objeto |
| `GetObjectList(settings)` | itera sobre objetos del documento |
| `FindByLayer(layer)` | filtra por capa |

## doc — otras colecciones

| Colección | Descripción |
|-----------|-------------|
| `doc.Layers` | `LayerTable` — gestión de capas |
| `doc.Groups` | grupos de objetos |
| `doc.Views` | vistas; `.Redraw()` actualiza pantalla |
| `doc.Views.ActiveView` | vista activa actual |
| `doc.Views.ActiveView.ActiveViewportID` | ID del viewport activo |
| `doc.HatchPatterns` | patrones de hatch disponibles |
| `doc.DimStyles` | estilos de dimensión |
| `doc.InstanceDefinitions` | definiciones de bloque |

## Importación alternativa

```python
from scriptcontext import doc
from Rhino.Geometry import Circle, Point3d

c = Circle(Point3d(0, 0, 0), 5.0)
doc.Objects.AddCircle(c)
doc.Views.Redraw()
```

## Diferencia con rhinoscriptsyntax

`rhinoscriptsyntax` abstrae este patrón: sus funciones `rs.AddCircle()`, `rs.AddLine()`, etc. internamente llaman a `doc.Objects.Add*()`. Para máximo control usar RhinoCommon directamente.

## Conexiones

- Mapas: [[Mapa - Documento de Rhino]] · [[Mapa - Programación]]
- [[wiki/entities/rhinocommon]] — SDK fuente
- [[wiki/entities/rhinoscriptsyntax]] — abstracción de alto nivel
- [[wiki/concepts/tipos-geometria-rhinocommon]] — tipos de geometría disponibles
