---
title: "Get Object UUID"
source: "https://developer.rhino3d.com/samples/rhinocommon/get-object-uuid/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to get the UUID (sometimes called GUID) of a Rhino object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [objects, uuid, Adding Objects]
---
Demonstrates how to get the UUID (sometimes called GUID) of a Rhino object.

```cs
partial class Examples
{
  public static Result GetUUID(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object", false, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    if (obj_ref == null)
      return Result.Nothing;

    var uuid = obj_ref.ObjectId;
    RhinoApp.WriteLine("The object's unique id is {0}", uuid.ToString());
    return Result.Success;
  }
}
```
