---
title: "Brep from Curve Bounding Box"
source: "https://developer.rhino3d.com/samples/rhinocommon/brep-from-curve-bounding-box/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a valid Brep from a curve's bounding box."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [brep, curve, bounding, Curves]
---
Demonstrates how to create a valid Brep from a curve's bounding box.

```cs
partial class Examples
{
  public static Result BrepFromCurveBBox(RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = RhinoGet.GetOneObject("Select Curve", false, ObjectType.Curve, out objref);
    if( rc != Result.Success )
      return rc;
    var curve = objref.Curve();

    var view = doc.Views.ActiveView;
    var plane = view.ActiveViewport.ConstructionPlane();
    // Create a construction plane aligned bounding box
    var bbox = curve.GetBoundingBox(plane);

    if (bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0) {
      RhinoApp.WriteLine("the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created.");
      return Result.Failure;
    }
    var brep = Brep.CreateFromBox(bbox);
    doc.Objects.AddBrep(brep);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
