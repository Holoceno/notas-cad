---
title: "Insert Knot"
source: "https://developer.rhino3d.com/samples/rhinocommon/insert-knot/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to insert a knot into a user-selected NURBS curve."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [insert, knot, Other]
---
Demonstrates how to insert a knot into a user-selected NURBS curve.

```python
import Rhino
import scriptcontext

def InsertKnot():
    filter = Rhino.DocObjects.ObjectType.Curve
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve for knot insertion", False, filter)
    if rc != Rhino.Commands.Result.Success: return rc

    curve = objref.Curve()
    if not curve: return Rhino.Commands.Result.Failure
    nurb = curve.ToNurbsCurve()
    if not nurb: return Rhino.Commands.Result.Failure

    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Point on curve to add knot")
    gp.Constrain(nurb, False)
    gp.Get()
    if gp.CommandResult() == Rhino.Commands.Result.Success:
        crv, t = gp.PointOnCurve()
        if crv and nurb.Knots.InsertKnot(t):
            scriptcontext.doc.Objects.Replace(objref, nurb)
            scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    InsertKnot()
```
