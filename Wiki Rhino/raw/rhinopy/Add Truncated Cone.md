---
title: "Add Truncated Cone"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-truncated-cone/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to construct a truncated cone (TCone) from two circles."
tags:
  - "clippings"
---
Demonstrates how to construct a truncated cone (TCone) from two circles.

```python
import Rhino

import scriptcontext

import System.Guid

 

def AddTruncatedCone():

    bottom_pt = Rhino.Geometry.Point3d(0,0,0)

    bottom_radius = 2

    bottom_circle = Rhino.Geometry.Circle(bottom_pt, bottom_radius)

 

    top_pt = Rhino.Geometry.Point3d(0,0,10)

    top_radius = 6

    top_circle = Rhino.Geometry.Circle(top_pt, top_radius)

 

    shapeCurve = Rhino.Geometry.LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0))

    axis = Rhino.Geometry.Line(bottom_circle.Center, top_circle.Center)

    revsrf = Rhino.Geometry.RevSurface.Create(shapeCurve, axis)

    tcone_brep = Rhino.Geometry.Brep.CreateFromRevSurface(revsrf, True, True)

 

    if scriptcontext.doc.Objects.AddBrep(tcone_brep)!=System.Guid.Empty:

        scriptcontext.doc.Views.Redraw()

        return Rhino.Commands.Result.Success

    return Rhino.Commands.Result.Failure

 

 

if __name__=="__main__":

    AddTruncatedCone()
```