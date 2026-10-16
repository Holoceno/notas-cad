---
title: "Single Color Back Faces"
source: "https://developer.rhino3d.com/samples/rhinocommon/single-color-back-faces/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine the curve and object colors of back faces."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [single, color, back, faces, Other]
---
Demonstrates how to determine the curve and object colors of back faces.

```cs
partial class Examples
{
  public static Result SingleColorBackfaces(RhinoDoc doc)
  {
    var display_mode_descs = //DisplayModeDescription.GetDisplayModes();
      from dm in DisplayModeDescription.GetDisplayModes()
      where dm.EnglishName == "Shaded"
      select dm;

    foreach (var dmd in display_mode_descs)
    {
      RhinoApp.WriteLine("CurveColor {0}", dmd.DisplayAttributes.CurveColor.ToKnownColor());
      RhinoApp.WriteLine("ObjectColor {0}", dmd.DisplayAttributes.ObjectColor.ToKnownColor());
    }
    return Result.Success;
  }
}
```
