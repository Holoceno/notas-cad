---
title: "Add Circle"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-circle/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a circle from a center point and radius."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, circle, Adding Objects]
---
Demonstrates how to add a circle from a center point and radius.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddCircle(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);
    const double radius = 10.0;
    Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(center, radius);
    if (doc.Objects.AddCircle(c) != Guid.Empty)
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```
