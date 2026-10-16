---
title: "Select Objects in Object Groups"
source: "https://developer.rhino3d.com/samples/rhinocommon/select-objects-in-object-groups/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to select objects that are an object group."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [select, objects, groups, Picking and Selection, Adding Objects]
---
Demonstrates how to select objects that are an object group.

```cs
partial class Examples
{
  public static Result SelectObjectsInObjectGroups(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rs = RhinoGet.GetOneObject(
      "Select object", false, ObjectType.AnyObject, out obj_ref);
    if (rs != Result.Success)
      return rs;
    var rhino_object = obj_ref.Object();
    if (rhino_object == null)
      return Result.Failure;

    var rhino_object_groups = rhino_object.Attributes.GetGroupList().DefaultIfEmpty(-1);

    var selectable_objects= from obj in doc.Objects.GetObjectList(ObjectType.AnyObject)
                            where obj.IsSelectable(true, false, false, false)
                            select obj;

    foreach (var selectable_object in selectable_objects)
    {
      foreach (var group in selectable_object.Attributes.GetGroupList())
      {
        if (rhino_object_groups.Contains(group))
        {
            selectable_object.Select(true);
            continue;
        }
      }
    }
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
