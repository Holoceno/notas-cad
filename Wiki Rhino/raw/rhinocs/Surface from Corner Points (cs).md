---
title: "Surface from Corner Points"
source: "https://developer.rhino3d.com/samples/rhinocommon/surface-from-corner-points/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a surface from a set of corner points."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [surface, corner, points, Other]
---
Demonstrates how to create a surface from a set of corner points.

```cs
partial class Examples
{
  public static Result SurfaceFromCorners(RhinoDoc doc)
  {
    var surface = NurbsSurface.CreateFromCorners(
      new Point3d(5, 0, 0),
      new Point3d(5, 5, 5),
      new Point3d(0, 5, 0),
      new Point3d(0, 0, 0));

    doc.Objects.AddSurface(surface);
    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```
