---
title: "Reverse Curve"
source: "https://developer.rhino3d.com/samples/rhinocommon/reverse-curve/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to reverse the direction of user-specified curves."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [reverse, curve, Curves]
---
Demonstrates how to reverse the direction of user-specified curves.

```cs
partial class Examples
{
  public static Result ReverseCurve(RhinoDoc doc)
  {
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select curves to reverse", true, ObjectType.Curve, out obj_refs);
    if (rc != Result.Success)
      return rc;

    foreach (var obj_ref in obj_refs)
    {
      var curve_copy = obj_ref.Curve().DuplicateCurve();
      if (curve_copy != null)
      {
        curve_copy.Reverse();
        doc.Objects.Replace(obj_ref, curve_copy);
      }
    }
    return Result.Success;
  }
}
```
