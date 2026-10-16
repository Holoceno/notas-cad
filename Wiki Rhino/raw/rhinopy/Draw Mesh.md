---
title: "Draw Mesh"
source: "https://developer.rhino3d.com/samples/rhinocommon/draw-mesh/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to create a mesh from an existing surface and draw it in a display conduit."
tags:
  - "clippings"
---
Demonstrates how to create a mesh from an existing surface and draw it in a display conduit.

```python
#! python 3

import Rhino

import System

import scriptcontext as sc

 

def RunCommand():

    gs = Rhino.Input.Custom.GetObject()

    gs.SetCommandPrompt("Select sphere")

    gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface

    gs.SubObjectSelect = False

    gs.Get()

    if gs.CommandResult() != Rhino.Commands.Result.Success:

        return gs.CommandResult()

 

    rc, sphere = gs.Object(0).Surface().TryGetSphere()

    if not rc or not sphere.IsValid:

        return Rhino.Commands.Result.Cancel

 

    mesh = Rhino.Geometry.Mesh.CreateFromSphere(sphere, 10, 10)

    if not mesh:

        return Rhino.Commands.Result.Failure

 

    conduit = DrawBlueMeshConduit(mesh)

    conduit.Enabled = True

    sc.doc.Views.Redraw()

 

    out_str = ""

    rc = Rhino.Input.RhinoGet.GetString("Press <Enter> to continue", True, out_str);

 

    conduit.Enabled = False

    sc.doc.Views.Redraw()

    

    return Rhino.Commands.Result.Success

 

class DrawBlueMeshConduit(Rhino.Display.DisplayConduit):

    def __init__(self, mesh):

        super().__init__()

        self.mesh = mesh

        self.color = System.Drawing.Color.Blue

        self.material = Rhino.Display.DisplayMaterial()

        self.material.Diffuse = self.color

        if mesh != None and mesh.IsValid:

            self.bbox = mesh.GetBoundingBox(True)

 

    def CalculateBoundingBox(self, args):

        args.BoundingBox.Union(self.bbox)

 

    def PreDrawObjects(self, drawEventArgs):

        gvp = drawEventArgs.Display.Viewport

        if gvp.DisplayMode.Id != Rhino.Display.DisplayModeDescription.WireframeId:

            drawEventArgs.Display.DrawMeshShaded(self.mesh, self.material)

        drawEventArgs.Display.DrawMeshWires(self.mesh, self.color)

 

if __name__ == "__main__":

    RunCommand()
```