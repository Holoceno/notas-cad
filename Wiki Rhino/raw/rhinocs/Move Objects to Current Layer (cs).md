---
title: "Move Objects to Current Layer"
source: "https://developer.rhino3d.com/samples/rhinocommon/move-objects-to-current-layer/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to move object to the currently active layer."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [move, selected, objects, current, layer, Adding Objects, Layers]
---
Demonstrates how to move object to the currently active layer.

```cs
partial class Examples
{
  public static Result MoveObjectsToCurrentLayer(RhinoDoc doc)
  {
    // all non-light objects that are selected
    var object_enumerator_settings = new ObjectEnumeratorSettings();
    object_enumerator_settings.IncludeLights = false;
    object_enumerator_settings.IncludeGrips = true;
    object_enumerator_settings.NormalObjects = true;
    object_enumerator_settings.LockedObjects = true;
    object_enumerator_settings.HiddenObjects = true;
    object_enumerator_settings.ReferenceObjects = true;
    object_enumerator_settings.SelectedObjectsFilter = true;
    var selected_objects = doc.Objects.GetObjectList(object_enumerator_settings);

    var current_layer_index = doc.Layers.CurrentLayerIndex;
    foreach (var selected_object in selected_objects)
    {
      selected_object.Attributes.LayerIndex = current_layer_index;
      selected_object.CommitChanges();
    }
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
