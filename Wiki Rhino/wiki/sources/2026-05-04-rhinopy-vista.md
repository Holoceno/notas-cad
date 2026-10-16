---
title: "RhinoCommon Samples — Vista y Entorno (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, rhino/vista]
palabras-clave: [rhinopython, vista, viewport, display, textura, bitmap, clipping]
sources: [raw/rhinopy/Add Background Bitmap.md, raw/rhinopy/Add Clipping Plane.md, raw/rhinopy/Add Texture.md, raw/rhinopy/Advanced Display Settings.md, raw/rhinopy/Determine Active Viewport.md]
created: 2026-05-04
updated: 2026-10-13
---

5 samples de RhinoCommon sobre configuración de viewport, materiales, texturas y ajustes de display.

## Determine Active Viewport

Distingue entre viewport normal y detalle activo en una page view:

```python
view = scriptcontext.doc.Views.ActiveView
if isinstance(view, Rhino.Display.RhinoPageView):
    viewport_name = view.ActiveViewport.Name
    page_name = view.PageName
else:
    viewport_name = view.ActiveViewport.Name
```

## Add Clipping Plane

```python
rc, points = Rhino.Input.RhinoGet.GetRectangle(...)
# points = [SW, SE, NE, NW]
plane = Rhino.Geometry.Plane(points[0], points[1], points[3])
viewport_id = scriptcontext.doc.Views.ActiveView.ActiveViewportID
scriptcontext.doc.Objects.AddClippingPlane(plane, 1.0, 1.0, viewport_id)
```

## Add Background Bitmap

```python
point = GetPoint("Bitmap location")
bitmap_path = OpenFileDialog(...)
# viewport usa SetTraceImage para imágenes de referencia
view.ActiveViewport.SetTraceImage(bitmap_path, plane, width, height, grayscale, hidden)
```

## Add Texture a objeto

```python
obj = GetOneObject(...)
material = Rhino.Render.RenderMaterial.CreateBasicMaterial(Rhino.DocObjects.Material(), doc)
texture = Rhino.DocObjects.Texture()
texture.FileName = bitmap_path
render_mat = ... # crear con SimulatedTexture y SetChild
obj.RenderMaterial = render_mat
obj.CommitChanges()
doc.Views.Redraw()
```

## Advanced Display Settings

Modifica propiedades de modos de display (ej: grosor de malla):

```python
modes = Rhino.Display.DisplayModeDescription.GetDisplayModes()
# GetOption para elegir modo
mode = modes[selected_index]
mode.DisplayAttributes.MeshWireThickness = new_value
Rhino.Display.DisplayModeDescription.UpdateDisplayMode(mode)
```

## Conexiones

- Mapas: [[Mapa - Visualización y anotaciones]] · [[Mapa - Programación]]
- [[wiki/concepts/rhinocommon-document-api]] — doc.Views.ActiveView, doc.Objects
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Background Bitmap: [[Add Background Bitmap|Python]] · [[Add Background Bitmap (cs)|C#]]
- Add Clipping Plane: [[Add Clipping Plane|Python]] · [[Add Clipping Plane (cs)|C#]]
- Add Texture: [[Add Texture|Python]] · [[Add Texture (cs)|C#]]
- Advanced Display Settings: [[Advanced Display Settings|Python]] · [[Advanced Display Settings (cs)|C#]]
- Determine Active Viewport: [[Determine Active Viewport|Python]] · [[Determine Active Viewport (cs)|C#]]
