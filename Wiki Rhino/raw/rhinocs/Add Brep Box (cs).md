---
title: "Add Brep Box"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-brep-box/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a Brep Box to a Rhino model by specifying two points."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, brep, Adding Objects]
---
Demonstrates how to add a Brep Box to a Rhino model by specifying two points.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddBrepBox(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d pt0 = new Rhino.Geometry.Point3d(0, 0, 0);
    Rhino.Geometry.Point3d pt1 = new Rhino.Geometry.Point3d(10, 10, 10);
    Rhino.Geometry.BoundingBox box = new Rhino.Geometry.BoundingBox(pt0, pt1);
    Rhino.Geometry.Brep brep = box.ToBrep();
    Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
    if( doc.Objects.AddBrep(brep) != System.Guid.Empty )
    {
      rc = Rhino.Commands.Result.Success;
      doc.Views.Redraw();
    }
    return rc;
  }
}
```
