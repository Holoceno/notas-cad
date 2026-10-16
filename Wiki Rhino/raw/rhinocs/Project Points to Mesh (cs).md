---
title: "Project Points to Mesh"
source: "https://developer.rhino3d.com/samples/rhinocommon/project-points-to-mesh/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to project points to a mesh."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [project, points, mesh, Other]
---
Demonstrates how to project points to a mesh.

```cs
partial class Examples
{
  public static Result ProjectPointsToMeshesEx(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("mesh", false, ObjectType.Mesh, out obj_ref);
    if (rc != Result.Success) return rc;
    var mesh = obj_ref.Mesh();

    ObjRef[] obj_ref_pts;
    rc = RhinoGet.GetMultipleObjects("points", false, ObjectType.Point, out obj_ref_pts);
    if (rc != Result.Success) return rc;
    var points = new List<Point3d>();
    foreach (var obj_ref_pt in obj_ref_pts)
    {
      var pt = obj_ref_pt.Point().Location;
      points.Add(pt);
    }

    int[] indices;
    var prj_points = Intersection.ProjectPointsToMeshesEx(new[] {mesh}, points, new Vector3d(0, 1, 0), 0, out indices);
    foreach (var prj_pt in prj_points) doc.Objects.AddPoint(prj_pt);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
