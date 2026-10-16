---
title: "RhinoCommon Samples — Input y UI Interactivo (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, rhino/seleccion, programacion/interfaz, rhino/vista]
palabras-clave: [rhinopython, input, ui, getpoint, commandline, options, display, conduit]
sources: [raw/rhinopy/Add Command Line Options.md, raw/rhinopy/Dynamically Draw Geometry when Picking Points.md, raw/rhinopy/Get Angle.md, raw/rhinopy/Pick Point.md, raw/rhinopy/Custom Geometry Filter.md, raw/rhinopy/Get Multiple With Options.md]
created: 2026-05-04
updated: 2026-10-13
---

6 samples de RhinoCommon sobre interacción con el usuario: opciones de línea de comandos, selección de puntos y geometría, filtros personalizados y dibujado dinámico.

## Command Line Options

```python
import Rhino, scriptcontext

gp = Rhino.Input.Custom.GetPoint()
gp.SetCommandPrompt("GetPoint with options")

int_opt  = Rhino.Input.Custom.OptionInteger(1, 1, 99)
dbl_opt  = Rhino.Input.Custom.OptionDouble(2.2, 0, 99.9)
bool_opt = Rhino.Input.Custom.OptionToggle(True, "Off", "On")
list_vals = ("Item0", "Item1", "Item2", "Item3")

gp.AddOptionInteger("Integer", int_opt)
gp.AddOptionDouble("Double", dbl_opt)
gp.AddOptionToggle("Boolean", bool_opt)
list_idx = gp.AddOptionList("List", list_vals, 0)

while True:
    rc = gp.Get()
    if gp.CommandResult() != Rhino.Commands.Result.Success:
        return
    if rc == Rhino.Input.GetResult.Point:
        point = gp.Point()
        scriptcontext.doc.Objects.AddPoint(point)
        scriptcontext.doc.Views.Redraw()
        break
    elif rc == Rhino.Input.GetResult.Option:
        if gp.OptionIndex() == list_idx:
            current = gp.Option().CurrentListOptionIndex
        continue
```

Tipos de opción disponibles: `OptionInteger`, `OptionDouble`, `OptionToggle` (on/off), `AddOptionList` (lista de strings).

## Get Multiple Objects with Options

```python
go = Rhino.Input.Custom.GetObject()
go.SetCommandPrompt("Select objects")
count_opt = Rhino.Input.Custom.OptionInteger(1, 1, 100)
go.AddOptionInteger("Count", count_opt)
go.EnablePreSelect(True, True)
go.GetMultiple(1, 0)  # mínimo 1, máximo 0 = ilimitado
if go.ObjectsWerePreselected:
    pass  # manejar pre-selección
```

## Get Angle

```python
rc, angle_rad = Rhino.Input.RhinoGet.GetAngle(
    "Start angle", base_pt, ref_pt1, ref_pt2, 0)
angle_deg = Rhino.RhinoMath.ToDegrees(angle_rad)
```

## Dibujado dinámico durante selección de puntos

```python
gp = Rhino.Input.Custom.GetPoint()
gp.DynamicDraw += on_dynamic_draw

def on_dynamic_draw(sender, e):
    center = e.CurrentPoint
    circle = Rhino.Geometry.Circle(construction_plane, center, radius)
    e.Display.DrawCircle(circle, System.Drawing.Color.Red)
```
El evento `DynamicDraw` se dispara en cada movimiento del cursor, permitiendo preview en tiempo real.

## Filtros de geometría personalizados

```python
go = Rhino.Input.Custom.GetObject()
go.SetCommandPrompt("Select a circle")
go.SetCustomGeometryFilter(circle_filter)
go.Get()

def circle_filter(rhino_object, geometry, component_index):
    if hasattr(geometry, 'TryGetCircle'):
        result, circle = geometry.TryGetCircle()
        return result
    return False
```

## Conexiones

- Mapas: [[Mapa - Visualización y anotaciones]] · [[Mapa - Documento de Rhino]] · [[Mapa - Scripts, interfaz y archivos]] · [[Mapa - Programación]]
- [[wiki/concepts/interactive-object-selection]] — patrón GetObject base
- [[wiki/concepts/rhinocommon-document-api]] — doc.Objects.AddPoint
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Command Line Options: [[Add Command Line Options|Python]] · [[Add Command Line Options (cs)|C#]]
- Dynamically Draw Geometry when Picking Points: [[Dynamically Draw Geometry when Picking Points|Python]] · [[Dynamically Draw Geometry when Picking Points (cs)|C#]]
- Get Angle: [[Get Angle|Python]] · [[Get Angle (cs)|C#]]
- Pick Point: [[Pick Point|Python]] · [[Pick Point (cs)|C#]]
- Custom Geometry Filter: [[Custom Geometry Filter|Python]] · [[Custom Geometry Filter (cs)|C#]]
- Get Multiple With Options: [[Get Multiple With Options|Python]] · [[Get Multiple With Options (cs)|C#]]
