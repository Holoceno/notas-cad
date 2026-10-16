---
title: "Find point on curve at distance"
source: "https://developer.rhino3d.com/samples/rhinocommon/find-point-on-curve-at-distance/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how find a point on a curve given a specified length from the start of the curve."
tags:
  - "clippings"
---
Demonstrates how find a point on a curve given a specified length from the start of the curve.

```python
import Rhino

import scriptcontext

 

def ArcLengthPoint():

    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve", True, Rhino.DocObjects.ObjectType.Curve)

    if rc!=Rhino.Commands.Result.Success: return rc

    crv = objref.Curve()

    if not crv: return Rhino.Commands.Result.Failure

    crv_length = crv.GetLength()

    length = 0

    rc, length = Rhino.Input.RhinoGet.GetNumber("Length from start", True, length, 0, crv_length)

    if rc!=Rhino.Commands.Result.Success: return rc

    pt = crv.PointAtLength(length)

    if pt.IsValid:

        scriptcontext.doc.Objects.AddPoint(pt)

        scriptcontext.doc.Views.Redraw()

    return Rhino.Commands.Result.Success

 

if __name__=="__main__":

    ArcLengthPoint()
```