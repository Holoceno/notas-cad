---
title: "Divide Curve by Segments"
source: "https://developer.rhino3d.com/samples/rhinocommon/divide-curve-by-segments/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to divide a user-selected curve into length segments."
tags:
  - "clippings"
---
Demonstrates how to divide a user-selected curve into length segments.

```python
from Rhino.DocObjects import *

from Rhino.Input import *

from Rhino.Commands import *

from Rhino.Geometry import *

from Rhino import *

from scriptcontext import doc

 

def RunCommand():

    rc, objref = RhinoGet.GetOneObject("Select curve to divide", False, ObjectType.Curve)

    if rc != Result.Success or objref == None:

        return rc

 

    curve = objref.Curve()

    if curve == None or curve.IsShort(RhinoMath.ZeroTolerance):

        return Result.Failure

 

    segment_count = 2

    rc, segment_count = RhinoGet.GetInteger("Divide curve into how many segments?", False, segment_count)

    if rc != Result.Success:

        return rc

 

    curve_params = curve.DivideByCount(segment_count, True)

    if curve_params == None:

        return Result.Failure

 

    points = [curve.PointAt(t) for t in curve_params]

    for point in points:

        doc.Objects.AddPoint(point)

 

    doc.Views.Redraw()

    return Result.Success

 

if __name__ == "__main__":

    RunCommand()
```