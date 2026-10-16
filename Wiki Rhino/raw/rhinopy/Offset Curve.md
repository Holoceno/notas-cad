---
title: "Offset Curve"
source: "https://developer.rhino3d.com/samples/rhinocommon/offset-curve/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to offset curves to one side or another by a distance."
tags:
  - "clippings"
---
Demonstrates how to offset curves to one side or another by a distance.

```python
from Rhino import *

from Rhino.DocObjects import *

from Rhino.Geometry import *

from Rhino.Input import *

from Rhino.Commands import *

from scriptcontext import doc

import rhinoscriptsyntax as rs

 

def RunCommand():

    rc, obj_ref = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve)

    if rc != Result.Success:

        return rc

    curve = obj_ref.Curve()

    if curve == None:

        return Result.Nothing

 

    rc, point = RhinoGet.GetPoint("Select Side", False)

    if rc != Result.Success:

        return rc

    if point == Point3d.Unset:

        return Result.Nothing

 

    curves = curve.Offset(point, Vector3d.ZAxis, 1.0, doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None)

 

    for offset_curve in curves:

        doc.Objects.AddCurve(offset_curve)

 

    doc.Views.Redraw()

    return Result.Success

 

if __name__ == "__main__":

    RunCommand()
```