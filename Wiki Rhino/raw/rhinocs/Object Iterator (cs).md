---
title: "Object Iterator"
source: "https://developer.rhino3d.com/samples/rhinocommon/object-iterator/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to iterate (or enumerate) through Rhino's geometry table."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [iterate, through, rhinos, geometry, table, Other]
---
Demonstrates how to iterate (or enumerate) through Rhino's geometry table.

```cs
partial class Examples
{
  public static Result ObjectIterator(RhinoDoc doc)
  {
    var object_enumerator_settings = new ObjectEnumeratorSettings();
    object_enumerator_settings.IncludeLights = true;
    object_enumerator_settings.IncludeGrips = false;
    var rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings);

    int count = 0;
    foreach (var rhino_object in rhino_objects)
    {
      if (rhino_object.IsSelectable() && rhino_object.IsSelected(false) == 0)
      {
        rhino_object.Select(true);
        count++;
      }
    }
    if (count > 0)
    {
      doc.Views.Redraw();
      RhinoApp.WriteLine("{0} object{1} selected", count,
        count == 1 ? "" : "s");
    }
    return Result.Success;
  }
}
```
