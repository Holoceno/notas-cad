---
title: "Surface from Edge Curves"
source: "https://developer.rhino3d.com/samples/rhinocommon/surface-from-edge-curves/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Create a Surface from Edge Curves"
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [create, surface, edge, curves, Curves]
---
Create a Surface from Edge Curves

```cs
partial class Examples
{
  public static Result EdgeSrf(RhinoDoc doc)
  {
    var go = new GetObject();
    go.SetCommandPrompt("Select 2, 3, or 4 open curves");
    go.GeometryFilter = ObjectType.Curve;
    go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve;
    go.GetMultiple(2, 4);
    if (go.CommandResult() != Result.Success)
      return go.CommandResult();

    var curves = go.Objects().Select(o => o.Curve());

    var brep = Brep.CreateEdgeSurface(curves);

    if (brep != null)
    {
      doc.Objects.AddBrep(brep);
      doc.Views.Redraw();
    }

    return Result.Success;
  }
}
```
