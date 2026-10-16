---
title: "Add Sphere"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-sphere/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a sphere from a center point and radius."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, sphere, Adding Objects]
---
Demonstrates how to create a sphere from a center point and radius.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddSphere(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);
    const double radius = 5.0;
    Rhino.Geometry.Sphere sphere = new Rhino.Geometry.Sphere(center, radius);
    if( doc.Objects.AddSphere(sphere) != Guid.Empty )
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```
