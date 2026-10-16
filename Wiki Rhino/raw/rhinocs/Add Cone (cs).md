---
title: "Add Cone"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-cone/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to construct a cone using a plane, height, and radius."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, cone, Adding Objects]
---
Demonstrates how to construct a cone using a plane, height, and radius.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddCone(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Plane plane = Rhino.Geometry.Plane.WorldXY;
    const double height = 10;
    const double radius = 5;
    Rhino.Geometry.Cone cone = new Rhino.Geometry.Cone(plane, height, radius);
    if (cone.IsValid)
    {
      const bool cap_bottom = true;
      Rhino.Geometry.Brep cone_brep = cone.ToBrep(cap_bottom);
      if (cone_brep!=null)
      {
        doc.Objects.AddBrep(cone_brep);
        doc.Views.Redraw();
      }
    }
    return Rhino.Commands.Result.Success;
  }
}
```
