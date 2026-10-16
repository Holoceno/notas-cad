---
title: "Is Planar Surface in Plane"
source: "https://developer.rhino3d.com/samples/rhinocommon/is-planar-surface-in-plane/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine if a user-selected surface is in plane."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [planar, surface, plane, Other]
---
Demonstrates how to determine if a user-selected surface is in plane.

```cs
partial class Examples
{
  public static Result IsPlanarSurfaceInPlane(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("select surface", true, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var surface = obj_ref.Surface();

    Point3d[] corners;
    rc = RhinoGet.GetRectangle(out corners);
    if (rc != Result.Success)
      return rc;

    var plane = new Plane(corners[0], corners[1], corners[2]);

    var is_or_isnt = " not ";
    if (IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance))
      is_or_isnt = "";

    RhinoApp.WriteLine("Surface is{0} in plane.", is_or_isnt);
    return Result.Success;
  }

  private static bool IsSurfaceInPlane(Surface surface, Plane plane, double tolerance)
  {
    if (!surface.IsPlanar(tolerance))
      return false;

    var bbox = surface.GetBoundingBox(true);
    return bbox.GetCorners().All(c => System.Math.Abs(plane.DistanceTo(c)) <= tolerance);
  }
}
```
