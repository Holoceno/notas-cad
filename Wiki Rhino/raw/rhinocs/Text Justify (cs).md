---
title: "Text Justify"
source: "https://developer.rhino3d.com/samples/rhinocommon/text-justify/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to set text justification with a specific font."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [justifying, text, entities, Other]
---
Demonstrates how to set text justification with a specific font.

```cs
partial class Examples
{
  public static Result TextJustify(RhinoDoc doc)
  {
    var text_entity = new TextEntity
    {
      Plane = Plane.WorldXY,
      Text = "Hello Rhino!",
      Justification = TextJustification.MiddleCenter,
      FontIndex = doc.Fonts.FindOrCreate("Arial", false, false)
    };

    doc.Objects.AddText(text_entity);
    doc.Views.Redraw();

    return Result.Success;
  }
}
```
