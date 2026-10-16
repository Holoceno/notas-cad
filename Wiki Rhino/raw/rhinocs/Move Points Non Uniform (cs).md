---
title: "Move Points Non Uniform"
source: "https://developer.rhino3d.com/samples/rhinocommon/move-points-non-uniform/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to move points in a non-uniform manner."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [move, points, uniform, Other]
---
Demonstrates how to move points in a non-uniform manner.

```cs
partial class Examples
{
  public static Result MovePointObjectsNonUniform(RhinoDoc doc)
  {
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select points to move", false, ObjectType.Point, out obj_refs);
    if (rc != Result.Success || obj_refs == null)
      return rc;

    foreach (var obj_ref in obj_refs)
    {
      var point3d = obj_ref.Point().Location;
      // modify the point coordinates in some way ...
      point3d.X++;
      point3d.Y++;
      point3d.Z++;

      doc.Objects.Replace(obj_ref, point3d);
    }

    doc.Views.Redraw();
    return Result.Success;
  }
}
```
