---
title: "Add Named View"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-named-view/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a named view to a Rhino model from a user-specified view and camera location."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [add, named, view, Adding Objects, Viewports and Views]
---
Demonstrates how to add a named view to a Rhino model from a user-specified view and camera location.

```python
import Rhino
import scriptcontext
import System.Guid

def AddNamedView():
    rc, view = Rhino.Input.RhinoGet.GetView("Select view to adjust")
    if rc!=Rhino.Commands.Result.Success: return rc

    rc, location = Rhino.Input.RhinoGet.GetPoint("Camera Location", False)
    if rc!=Rhino.Commands.Result.Success: return rc

    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Look At Location")
    gp.DrawLineFromPoint(location, False)
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()
    lookat = gp.Point()

    name = view.ActiveViewport.Name
    rc, name = Rhino.Input.RhinoGet.GetString("Name", True, name)
    if rc!=Rhino.Commands.Result.Success: return rc

    vp = view.ActiveViewport
    # save the current viewport projection
    vp.PushViewProjection()
    vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis
    vp.SetCameraLocation(location, False)
    vp.SetCameraDirection(lookat - location, True)
    vp.Name = name

    scriptcontext.doc.NamedViews.Add(name, vp.Id)
    view.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    AddNamedView()
```
