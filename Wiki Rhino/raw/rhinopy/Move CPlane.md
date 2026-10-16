---
title: "Move CPlane"
source: "https://developer.rhino3d.com/samples/rhinocommon/move-cplane/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to move a CPlane in the active viewport."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [move, cplane, Other]
---
Demonstrates how to move a CPlane in the active viewport.

```python
import Rhino
import scriptcontext

class MoveCPlanePoint(Rhino.Input.Custom.GetPoint):
    def __init__(self, cplane):
        self.m_cplane = cplane
    def OnMouseMove(self, e):
        pl = self.m_cplane.Plane
        pl.Origin = e.Point
        self.m_cplane.Plane = pl
    def OnDynamicDraw(self, e):
        e.Display.DrawConstructionPlane(self.m_cplane);

def MoveCPlane():
    view = scriptcontext.doc.Views.ActiveView
    if not view: return Rhino.Commands.Result.Failure

    cplane = view.ActiveViewport.GetConstructionPlane()
    origin = cplane.Plane.Origin
    gp = MoveCPlanePoint(cplane)
    gp.SetCommandPrompt("CPlane origin")
    gp.SetBasePoint(origin, True)
    gp.DrawLineFromPoint(origin, True)
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()

    point = gp.Point()
    v = origin - point
    if v.IsTiny(): return Rhino.Commands.Result.Nothing
    pl = cplane.Plane
    pl.Origin = point
    cplane.Plane = pl
    view.ActiveViewport.SetConstructionPlane(cplane)
    view.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    MoveCPlane()
```
