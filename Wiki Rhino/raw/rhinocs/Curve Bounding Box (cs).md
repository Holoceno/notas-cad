---
title: "Curve Bounding Box"
source: "https://developer.rhino3d.com/samples/rhinocommon/curve-bounding-box/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a curve bounding box (world and plane oriented)."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [curve, bounding, world, plane, oriented, Curves]
---
Demonstrates how to create a curve bounding box (world and plane oriented).

```cs
partial class Examples
{
  public static Rhino.Commands.Result CurveBoundingBox(Rhino.RhinoDoc doc)
  {
    // Select a curve object
    Rhino.DocObjects.ObjRef rhObject;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", false, Rhino.DocObjects.ObjectType.Curve, out rhObject);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    // Validate selection
    var curve = rhObject.Curve();
    if (curve == null)
      return Rhino.Commands.Result.Failure;

    // Get the active view's construction plane
    var view = doc.Views.ActiveView;
    if (view == null)
      return Rhino.Commands.Result.Failure;
    var plane = view.ActiveViewport.ConstructionPlane();

    // Compute the tight bounding box of the curve in world coordinates
    var bbox = curve.GetBoundingBox(true);
    if (!bbox.IsValid)
      return Rhino.Commands.Result.Failure;

    // Print the min and max box coordinates in world coordinates
    Rhino.RhinoApp.WriteLine("World min: {0}", bbox.Min);
    Rhino.RhinoApp.WriteLine("World max: {0}", bbox.Max);

    // Compute the tight bounding box of the curve based on the
    // active view's construction plane
    bbox = curve.GetBoundingBox(plane);

    // Print the min and max box coordinates in cplane coordinates
    Rhino.RhinoApp.WriteLine("CPlane min: {0}", bbox.Min);
    Rhino.RhinoApp.WriteLine("CPlane max: {0}", bbox.Max);
    return Rhino.Commands.Result.Success;
  }
}
```
