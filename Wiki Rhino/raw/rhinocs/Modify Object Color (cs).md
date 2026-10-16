---
title: "Modify Object Color"
source: "https://developer.rhino3d.com/samples/rhinocommon/modify-object-color/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to modify the color of a user-specified object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [modify, objects, color, Adding Objects]
---
Demonstrates how to modify the color of a user-specified object.

```cs
partial class Examples
{
  public static Result ModifyObjectColor(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object", false, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();
    var color = rhino_object.Attributes.ObjectColor;
    bool b = Rhino.UI.Dialogs.ShowColorDialog(ref color);
    if (!b) return Result.Cancel;

    rhino_object.Attributes.ObjectColor = color;
    rhino_object.Attributes.ColorSource = ObjectColorSource.ColorFromObject;
    rhino_object.CommitChanges();

    // an object's color attributes can also be specified
    // when the object is added to Rhino
    var sphere = new Sphere(Point3d.Origin, 5.0);
    var attributes = new ObjectAttributes();
    attributes.ObjectColor = Color.CadetBlue;
    attributes.ColorSource = ObjectColorSource.ColorFromObject;
    doc.Objects.AddSphere(sphere, attributes);

    doc.Views.Redraw();
    return Result.Success;
  }
}
```
