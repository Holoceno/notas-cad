---
title: "Divide by Length Points"
source: "https://developer.rhino3d.com/samples/rhinocommon/divide-by-length-points/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to divide a user-selected curve into a set of spaced points along the curve."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [divide, length, points, Other]
---
Demonstrates how to divide a user-selected curve into a set of spaced points along the curve.

```python
import Rhino
import scriptcontext

def DivideByLengthPoints():
    filter = Rhino.DocObjects.ObjectType.Curve
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve to divide", False, filter)
    if not objref or rc!=Rhino.Commands.Result.Success: return rc

    crv = objref.Curve()
    if not crv or crv.IsShort(Rhino.RhinoMath.ZeroTolerance):
        return Rhino.Commands.Result.Failure

    crv_length = crv.GetLength()
    s = "Curve length is {0:.3f}. Segment length".format(crv_length)
    seg_length = crv_length / 2.0
    rc, length = Rhino.Input.RhinoGet.GetNumber(s, False, seg_length, 0, crv_length)
    if rc!=Rhino.Commands.Result.Success: return rc
    t_vals = crv.DivideByLength(length, True)
    if not t_vals:
        return Rhino.Commands.Result.Failure

    [scriptcontext.doc.Objects.AddPoint(crv.PointAt(t)) for t in t_vals]
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    DivideByLengthPoints()
```
