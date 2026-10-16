---
title: "Rename Object"
source: "https://developer.rhino3d.com/samples/rhinocommon/rename-object/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to rename a user-specified object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [rename, object, Adding Objects]
---
Demonstrates how to rename a user-specified object.

```cs
partial class Examples
{
  public static Result RenameObject(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object to change name", true, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();

    var new_object_name = "";
    rc = RhinoGet.GetString("New object name", true, ref new_object_name);
    if (rc != Result.Success)
      return rc;
    if (string.IsNullOrWhiteSpace(new_object_name))
      return Result.Nothing;

    if (rhino_object.Name != new_object_name)
    {
      rhino_object.Attributes.Name = new_object_name;
      rhino_object.CommitChanges();
    }

    return Result.Success;
  }
}
```
