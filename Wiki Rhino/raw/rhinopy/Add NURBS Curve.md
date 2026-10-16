---
title: "Add NURBS Curve"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-nurbs-curve/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to create a NURBS curve from a list of points."
tags:
  - "clippings"
---
Demonstrates how to create a NURBS curve from a list of points.

```python
import Rhino

import scriptcontext

import System.Guid

 

def AddNurbsCurve():

    points = Rhino.Collections.Point3dList(5)

    points.Add(0, 0, 0)

    points.Add(0, 2, 0)

    points.Add(2, 3, 0)

    points.Add(4, 2, 0)

    points.Add(4, 0, 0)

 

    nc = Rhino.Geometry.NurbsCurve.Create(False, 3, points)

    rc = Rhino.Commands.Result.Failure

    if nc and nc.IsValid:

        if scriptcontext.doc.Objects.AddCurve(nc)!=System.Guid.Empty:

            scriptcontext.doc.Views.Redraw()

            rc = Rhino.Commands.Result.Success

    return rc

 

if __name__=="__main__":

    AddNurbsCurve()
```