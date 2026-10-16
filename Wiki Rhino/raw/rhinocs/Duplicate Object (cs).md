---
title: "Duplicate Object"
source: "https://developer.rhino3d.com/samples/rhinocommon/duplicate-object/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to clone (or copy, or duplicate) a Rhino object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [clone, copy, duplicate, rhino, object, Adding Objects]
---
Demonstrates how to clone (or copy, or duplicate) a Rhino object.

```cs
partial class Examples
{
  public static Result DuplicateObject(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object to duplicate", false, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();

    var geometry_base = rhino_object.DuplicateGeometry();
    if (geometry_base != null)
      if (doc.Objects.Add(geometry_base) != Guid.Empty)
        doc.Views.Redraw();

    return Result.Success;
  }
}
```
