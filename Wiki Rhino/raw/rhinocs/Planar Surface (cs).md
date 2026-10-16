---
title: "Planar Surface"
source: "https://developer.rhino3d.com/samples/rhinocommon/planar-surface/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a planar surface from a rectangle."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [create, plane, surface, Other]
---
Demonstrates how to create a planar surface from a rectangle.

```cs
partial class Examples
{
  public static Result PlanarSurface(RhinoDoc doc)
  {
    Point3d[] corners;
    var rc = Rhino.Input.RhinoGet.GetRectangle(out corners);
    if (rc != Result.Success)
      return rc;

    var plane = new Plane(corners[0], corners[1], corners[2]);

    var plane_surface = new PlaneSurface(plane,
      new Interval(0, corners[0].DistanceTo(corners[1])),
      new Interval(0, corners[1].DistanceTo(corners[2])));

    doc.Objects.Add(plane_surface);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
