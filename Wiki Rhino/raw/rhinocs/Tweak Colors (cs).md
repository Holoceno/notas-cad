---
title: "Tweak Colors"
source: "https://developer.rhino3d.com/samples/rhinocommon/tweak-colors/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to set the default paint colors in Rhino."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [tweak, colors, Other]
---
Demonstrates how to set the default paint colors in Rhino.

```cs
partial class Examples
{
  public static Rhino.Commands.Result TweakColors(Rhino.RhinoDoc doc)
  {
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalStart, System.Drawing.Color.AliceBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalEnd, System.Drawing.Color.AliceBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalBorder, System.Drawing.Color.LightBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotStart, System.Drawing.Color.LightBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotEnd, System.Drawing.Color.LightBlue, true);
    return Rhino.Commands.Result.Success;
  }
}
```
