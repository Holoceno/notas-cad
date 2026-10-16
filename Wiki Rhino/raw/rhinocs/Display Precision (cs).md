---
title: "Display Precision"
source: "https://developer.rhino3d.com/samples/rhinocommon/display-precision/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to change the display precision in a Rhino model."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [changing, display, precision, Other]
---
Demonstrates how to change the display precision in a Rhino model.

```cs
partial class Examples
{
  public static Result DisplayPrecision(RhinoDoc doc)
  {
    var gi = new GetInteger();
    gi.SetCommandPrompt("New display precision");
    gi.SetDefaultInteger(doc.ModelDistanceDisplayPrecision);
    gi.SetLowerLimit(0, false);
    gi.SetUpperLimit(7, false);
    gi.Get();
    if (gi.CommandResult() != Result.Success)
      return gi.CommandResult();
    var distance_display-precision = gi.Number();

    if (distance_display-precision != doc.ModelDistanceDisplayPrecision)
      doc.ModelDistanceDisplayPrecision = distance_display-precision;

    return Result.Success;
  }
}
```
