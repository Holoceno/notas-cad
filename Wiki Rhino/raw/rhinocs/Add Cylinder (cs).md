---
title: "Add Cylinder"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-cylinder/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to construct a cylinder using a center-point, height and axis."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, cylinder, rhino, Adding Objects]
---
Demonstrates how to construct a cylinder using a center-point, height and axis.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddCylinder(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d center_point = new Rhino.Geometry.Point3d(0, 0, 0);
    Rhino.Geometry.Point3d height_point = new Rhino.Geometry.Point3d(0, 0, 10);
    Rhino.Geometry.Vector3d zaxis = height_point - center_point;
    Rhino.Geometry.Plane plane = new Rhino.Geometry.Plane(center_point, zaxis);
    const double radius = 5;
    Rhino.Geometry.Circle circle = new Rhino.Geometry.Circle(plane, radius);
    Rhino.Geometry.Cylinder cylinder = new Rhino.Geometry.Cylinder(circle, zaxis.Length);
    Rhino.Geometry.Brep brep = cylinder.ToBrep(true, true);
    if (brep != null)
    {
      doc.Objects.AddBrep(brep);
      doc.Views.Redraw();
    }
    return Rhino.Commands.Result.Success;
  }
}
```
