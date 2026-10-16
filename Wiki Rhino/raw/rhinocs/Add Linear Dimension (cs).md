---
title: "Add Linear Dimension"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-linear-dimension/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a linear dimension to a Rhino model."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, linear, dimension, Adding Objects]
---
Demonstrates how to add a linear dimension to a Rhino model.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddLinearDimension(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.LinearDimension dimension;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetLinearDimension(out dimension);
    if (rc == Rhino.Commands.Result.Success && dimension != null)
    {
      if (doc.Objects.AddLinearDimension(dimension) == Guid.Empty)
        rc = Rhino.Commands.Result.Failure;
      else
        doc.Views.Redraw();
    }
    return rc;
  }
}
```
