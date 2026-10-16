---
title: "Create Mesh from Brep"
source: "https://developer.rhino3d.com/samples/rhinocommon/create-mesh-from-brep/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a mesh from a selected surface or polysurface."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [create, meshes, brep, Other]
---
Demonstrates how to create a mesh from a selected surface or polysurface.

```cs
partial class Examples
{
  public static Result CreateMeshFromBrep(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select surface or polysurface to mesh", true, ObjectType.Surface | ObjectType.PolysrfFilter, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var brep = obj_ref.Brep();
    if (null == brep)
      return Result.Failure;

    // you could choose anyone of these for example
    var jagged_and_faster = MeshingParameters.Coarse;
    var smooth_and_slower = MeshingParameters.Smooth;
    var default_mesh_params = MeshingParameters.Default;
    var minimal = MeshingParameters.Minimal;

    var meshes = Mesh.CreateFromBrep(brep, smooth_and_slower);
    if (meshes == null || meshes.Length == 0)
      return Result.Failure;

    var brep_mesh = new Mesh();
    foreach (var mesh in meshes)
      brep_mesh.Append(mesh);
    doc.Objects.AddMesh(brep_mesh);
    doc.Views.Redraw();

    return Result.Success;
  }
}
```
