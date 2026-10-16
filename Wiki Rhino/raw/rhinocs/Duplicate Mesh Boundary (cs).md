---
title: "Duplicate Mesh Boundary"
source: "https://developer.rhino3d.com/samples/rhinocommon/duplicated-mesh-boundary/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a bounding polyline from naked edges of an open mesh."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [bounding, polyline, naked, edges, open, mesh, Other]
---
Demonstrates how to create a bounding polyline from naked edges of an open mesh.

```cs
partial class Examples
{
  public static Result DupMeshBoundary(RhinoDoc doc)
  {
    var gm = new GetObject();
    gm.SetCommandPrompt("Select open mesh");
    gm.GeometryFilter = ObjectType.Mesh;
    gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh;
    gm.Get();
    if (gm.CommandResult() != Result.Success)
      return gm.CommandResult();
    var mesh = gm.Object(0).Mesh();
    if (mesh == null)
      return Result.Failure;

    var polylines = mesh.GetNakedEdges();
    foreach (var polyline in polylines)
    {
      doc.Objects.AddPolyline(polyline);
    }

    return Result.Success;
  }
}
```
