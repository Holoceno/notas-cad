---
title: "Add Torus"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-torus/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to construct a torus from a set of radii and a plane."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, torus, Adding Objects]
---
Demonstrates how to construct a torus from a set of radii and a plane.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddTorus(Rhino.RhinoDoc doc)
  {
    const double major_radius = 4.0;
    const double minor_radius = 2.0;

    Rhino.Geometry.Plane plane = Rhino.Geometry.Plane.WorldXY;
    Rhino.Geometry.Torus torus = new Rhino.Geometry.Torus(plane, major_radius, minor_radius);
    Rhino.Geometry.RevSurface revsrf = torus.ToRevSurface();
    if (doc.Objects.AddSurface(revsrf) != Guid.Empty)
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```
