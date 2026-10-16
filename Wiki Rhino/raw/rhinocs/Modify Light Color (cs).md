---
title: "Modify Light Color"
source: "https://developer.rhino3d.com/samples/rhinocommon/modify-light-color/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to change the color of a user-specified light."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [modify, lights, color, Other]
---
Demonstrates how to change the color of a user-specified light.

```cs
partial class Examples
{
  public static Result ModifyLightColor(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select light to change color", true,
      ObjectType.Light, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var light = obj_ref.Light();
    if (light == null)
      return Result.Failure;

    var diffuse_color = light.Diffuse;
    if (Dialogs.ShowColorDialog(ref diffuse_color))
    {
      light.Diffuse = diffuse_color;
    }

    doc.Lights.Modify(obj_ref.ObjectId, light);
    return Result.Success;
  }
}
```
