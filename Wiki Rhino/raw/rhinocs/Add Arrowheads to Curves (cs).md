---
title: "Add Arrowheads to Curves"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-arrowheads-to-curves/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to decorate curves in a Rhino model with arrowheads."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [adding, arrowheads, curves, Adding Objects, Curves]
---
Demonstrates how to decorate curves in a Rhino model with arrowheads.

```cs
partial class Examples
{
  public static Rhino.Commands.Result ObjectDecoration(Rhino.RhinoDoc doc)
  {
    // Define a line
    var line = new Rhino.Geometry.Line(new Rhino.Geometry.Point3d(0, 0, 0), new Rhino.Geometry.Point3d(10, 0, 0));

    // Make a copy of Rhino's default object attributes
    var attribs = doc.CreateDefaultAttributes();

    // Modify the object decoration style
    attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead;

    // Create a new curve object with our attributes
    doc.Objects.AddLine(line, attribs);
    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```
