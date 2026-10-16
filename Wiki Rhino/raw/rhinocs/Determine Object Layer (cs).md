---
title: "Determine Object Layer"
source: "https://developer.rhino3d.com/samples/rhinocommon/determine-object-layer/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine which layer a user-specified object is on and print the name."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [determine, objects, layer, Adding Objects, Layers]
---
Demonstrates how to determine which layer a user-specified object is on and print the name.

```cs
partial class Examples
{
  public static Rhino.Commands.Result DetermineObjectLayer(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef obref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select object", true, Rhino.DocObjects.ObjectType.AnyObject, out obref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    Rhino.DocObjects.RhinoObject rhobj = obref.Object();
    if (rhobj == null)
      return Rhino.Commands.Result.Failure;
    int index = rhobj.Attributes.LayerIndex;
    string name = doc.Layers[index].Name;
    Rhino.RhinoApp.WriteLine("The selected object's layer is '{0}'", name);
    return Rhino.Commands.Result.Success;
  }
}
```
