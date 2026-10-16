---
title: "Add Annotation Text"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-annotation-text/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add annotation text to a Rhino model at a specific location."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, annotation, text, Adding Objects]
---
Demonstrates how to add annotation text to a Rhino model at a specific location.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddAnnotationText(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d pt = new Rhino.Geometry.Point3d(10, 0, 0);
    const string text = "Hello RhinoCommon";
    const double height = 2.0;
    const string font = "Arial";
    Rhino.Geometry.Plane plane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane();
    plane.Origin = pt;
    Guid id = doc.Objects.AddText(text, plane, height, font, false, false);
    if( id != Guid.Empty )
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```
