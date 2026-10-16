---
title: "Determine Normal Direction of Brep Face"
source: "https://developer.rhino3d.com/samples/rhinocommon/determine-normal-direction-of-brep-face/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine the normal direction of a Brep face at a specified point."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [determine, normal, direction, brep, face, Other]
---
Demonstrates how to determine the normal direction of a Brep face at a specified point.

```python
import rhinoscriptsyntax as rs
import Rhino
from Rhino.Commands import Result

def RunCommand():
    # select a surface
    gs = Rhino.Input.Custom.GetObject()
    gs.SetCommandPrompt("select surface")
    gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
    gs.DisablePreSelect()
    gs.SubObjectSelect = False
    gs.Get()
    if gs.CommandResult() != Result.Success:
        return gs.CommandResult()

    # get the selected face
    face = gs.Object(0).Face()
    if face == None:
        return

    # pick a point on the surface.  Constain
    # picking to the face.
    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("select point on surface")
    gp.Constrain(face, False)
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()

    # get the parameters of the point on the
    # surface that is clesest to gp.Point()
    b, u, v = face.ClosestPoint(gp.Point())
    if b:
        dir = face.NormalAt(u, v)
        if face.OrientationIsReversed:
            dir.Reverse()
        print("Surface normal at uv({0:f},{1:f}) = ({2:f},{3:f},{4:f})".format(
            u, v, dir.X, dir.Y, dir.Z))

if __name__ == "__main__":
    RunCommand()
```
