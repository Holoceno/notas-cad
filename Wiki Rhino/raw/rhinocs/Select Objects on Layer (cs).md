---
title: "Select Objects on Layer"
source: "https://developer.rhino3d.com/samples/rhinocommon/select-objects-on-layer/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to select all the objects on a user-specified layer."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [select, objects, layer, Picking and Selection, Adding Objects, Layers]
---
Demonstrates how to select all the objects on a user-specified layer.

```cs
partial class Examples
{
  public static Rhino.Commands.Result SelLayer(Rhino.RhinoDoc doc)
  {
    // Prompt for a layer name
    string layername = doc.Layers.CurrentLayer.Name;
    Result rc = Rhino.Input.RhinoGet.GetString("Name of layer to select objects", true, ref layername);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    // Get all of the objects on the layer. If layername is bogus, you will
    // just get an empty list back
    Rhino.DocObjects.RhinoObject[] rhobjs = doc.Objects.FindByLayer(layername);
    if (rhobjs == null || rhobjs.Length < 1)
      return Rhino.Commands.Result.Cancel;

    for (int i = 0; i < rhobjs.Length; i++)
      rhobjs[i].Select(true);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
