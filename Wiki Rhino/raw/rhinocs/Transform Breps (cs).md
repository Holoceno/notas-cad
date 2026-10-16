---
title: "Transform Breps"
source: "https://developer.rhino3d.com/samples/rhinocommon/transform-breps/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to move (or transform) a user-specified Brep object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [transform, brep, Other]
---
Demonstrates how to move (or transform) a user-specified Brep object.

```cs
partial class Examples
{
  public static Rhino.Commands.Result TransformBrep(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef rhobj;
    var rc = RhinoGet.GetOneObject("Select brep", true, Rhino.DocObjects.ObjectType.Brep, out rhobj);
    if(rc!= Rhino.Commands.Result.Success)
      return rc;

    // Simple translation transformation
    var xform = Rhino.Geometry.Transform.Translation(18,-18,25);
    doc.Objects.Transform(rhobj, xform, true);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
