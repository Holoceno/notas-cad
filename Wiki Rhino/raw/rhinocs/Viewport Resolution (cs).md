---
title: "Viewport Resolution"
source: "https://developer.rhino3d.com/samples/rhinocommon/viewport-resolution/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Print Active Viewport Resolution"
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [print, active, viewport, resolution, Viewports and Views]
---
Print Active Viewport Resolution

```cs
partial class Examples
{
  public static Result ViewportResolution(RhinoDoc doc)
  {
    var active_viewport = doc.Views.ActiveView.ActiveViewport;
    RhinoApp.WriteLine("Name = {0}: Width = {1}, Height = {2}",
      active_viewport.Name, active_viewport.Size.Width, active_viewport.Size.Height);
    return Result.Success;
  }
}
```
