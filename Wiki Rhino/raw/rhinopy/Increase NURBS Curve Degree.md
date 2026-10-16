---
title: "Increase NURBS Curve Degree"
source: "https://developer.rhino3d.com/samples/rhinocommon/increase-nurbs-curve-degree/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to increase the degree of a NURBS curve."
tags:
  - "clippings"
---
Demonstrates how to increase the degree of a NURBS curve.

```python
from Rhino import *

from Rhino.Commands import *

from Rhino.Input import *

from Rhino.DocObjects import *

from scriptcontext import doc

 

def RunCommand():

    rc, obj_ref = RhinoGet.GetOneObject("Select curve", False, ObjectType.Curve)

    if rc != Result.Success: return rc

    if obj_ref == None: return Result.Failure

    curve = obj_ref.Curve()

    if curve == None: return Result.Failure

    nurbs_curve = curve.ToNurbsCurve()

 

    new_degree = -1

    rc, new_degree = RhinoGet.GetInteger("New degree <{0}...11>".format(nurbs_curve.Degree), True, new_degree, nurbs_curve.Degree, 11)

    if rc != Result.Success: return rc

 

    rc = Result.Failure

    if nurbs_curve.IncreaseDegree(new_degree):

        if doc.Objects.Replace(obj_ref.ObjectId, nurbs_curve):

            rc = Result.Success

 

    print "Result: {0}".format(rc)

    doc.Views.Redraw()

    return rc

 

if __name__ == "__main__":

    RunCommand()
```