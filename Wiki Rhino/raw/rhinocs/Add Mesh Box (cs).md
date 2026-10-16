---
title: "Add Mesh Box"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-mesh-box/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to construct a mesh box from a Brep box."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, mesh, Adding Objects]
---
Demonstrates how to construct a mesh box from a Brep box.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddMeshBox(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Box box;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetBox(out box);
    if (rc == Rhino.Commands.Result.Success)
    {
      Rhino.Geometry.Mesh mesh = Rhino.Geometry.Mesh.CreateFromBox(box, 2, 2, 2);
      if (null != mesh)
      {
        doc.Objects.AddMesh(mesh);
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }

    return Rhino.Commands.Result.Failure;
  }
}
```
