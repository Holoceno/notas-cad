---
title: "IsBrepBox Test"
source: "https://developer.rhino3d.com/samples/rhinocommon/isbrepbox-test/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine whether a given Brep is a box."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [isbrepbox, test, Other]
---
Demonstrates how to determine whether a given Brep is a box.

```cs
partial class Examples
{
  private static bool IsBrepBox(Rhino.Geometry.Brep brep)
  {
    const double zero_tolerance = 1.0e-6; // or whatever
    bool rc = brep.IsSolid;
    if( rc )
      rc = brep.Faces.Count == 6;

    var N = new Rhino.Geometry.Vector3d[6];
    for (int i = 0; rc && i < 6; i++)
    {
      Rhino.Geometry.Plane plane;
      rc = brep.Faces[i].TryGetPlane(out plane, zero_tolerance);
      if( rc )
      {
        N[i] = plane.ZAxis;
        N[i].Unitize();
      }
    }

    for (int i = 0; rc && i < 6; i++)
    {
      int count = 0;
      for (int j = 0; rc && j < 6; j++)
      {
        double dot = Math.Abs(N[i] * N[j]);
        if (dot <= zero_tolerance)
          continue;
        if (Math.Abs(dot - 1.0) <= zero_tolerance)
          count++;
        else
          rc = false;
      }

      if (rc)
      {
        if (2 != count)
          rc = false;
      }
    }
    return rc;
  }

  public static Rhino.Commands.Result IsBrepBox(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef obj_ref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select Brep", true, Rhino.DocObjects.ObjectType.Brep, out obj_ref);
    if (rc == Rhino.Commands.Result.Success)
    {
      var brep = obj_ref.Brep();
      if (brep != null)
      {
        Rhino.RhinoApp.WriteLine(IsBrepBox(brep) ? "Yes it is a box" : "No it is not a box");
      }
    }
    return rc;
  }
}
```
