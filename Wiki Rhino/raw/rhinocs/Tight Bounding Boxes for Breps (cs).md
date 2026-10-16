---
title: "Tight Bounding Boxes for Breps"
source: "https://developer.rhino3d.com/samples/rhinocommon/tight-bounding-boxes-for-breps/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to generate tight bounding boxes for Brep objects."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [tight, bounding, boxes, breps, Other]
---
Demonstrates how to generate tight bounding boxes for Brep objects.

```cs
partial class Examples
{
  public static Result TightBoundingBox(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject(
      "Select surface to split", true, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var surface = obj_ref.Surface();
    if (surface == null)
      return Result.Failure;

    obj_ref = null;
    rc = RhinoGet.GetOneObject(
      "Select cutting curve", true, ObjectType.Curve, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var curve = obj_ref.Curve();
    if (curve == null)
      return Result.Failure;

    var brep_face = surface as BrepFace;
    if (brep_face == null)
      return Result.Failure;

    var split-brep = brep_face.Split(
      new List<Curve> {curve}, doc.ModelAbsoluteTolerance);
    if (split-brep == null)
    {
      RhinoApp.WriteLine("Unable to split surface.");
      return Result.Nothing;
    }

    var meshes = Mesh.CreateFromBrep(split-brep);

    foreach (var mesh in meshes)
    {
      var bbox = mesh.GetBoundingBox(true);
      switch (bbox.IsDegenerate(doc.ModelAbsoluteTolerance))
      {
        case 3:
        case 2:
          return Result.Failure;
        case 1:
          // rectangle
          // box with 8 corners flattened to rectangle with 4 corners
          var rectangle_corners = bbox.GetCorners().Distinct().ToList();
          // add 1st point as last to close the loop
          rectangle_corners.Add(rectangle_corners[0]);
          doc.Objects.AddPolyline(rectangle_corners);
          doc.Views.Redraw();
          break;
        case 0:
          // box
          var brep_box = new Box(bbox).ToBrep();
          doc.Objects.AddBrep(brep_box);
          doc.Views.Redraw();
          break;
      }
    }

    return Result.Success;
  }
}
```
