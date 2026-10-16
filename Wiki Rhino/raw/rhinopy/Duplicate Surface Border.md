---
title: "Duplicate Surface Border"
source: "https://developer.rhino3d.com/samples/rhinocommon/duplicate-surface-border/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to duplicate the borders of a user-specified surface or polysurface."
tags:
  - "clippings"
---
Demonstrates how to duplicate the borders of a user-specified surface or polysurface.

```python
import Rhino

import scriptcontext

 

def DupBorder():

    filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter

    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, filter)

    if rc != Rhino.Commands.Result.Success: return rc

 

    rhobj = objref.Object()

    brep = objref.Brep()

    if not rhobj or not brep: return Rhino.Commands.Result.Failure

    rhobj.Select(False)

    curves = brep.DuplicateEdgeCurves(True)

    tol = scriptcontext.doc.ModelAbsoluteTolerance * 2.1

    curves = Rhino.Geometry.Curve.JoinCurves(curves, tol)

    for curve in curves:

        id = scriptcontext.doc.Objects.AddCurve(curve)

        scriptcontext.doc.Objects.Select(id)

    scriptcontext.doc.Views.Redraw()

    return Rhino.Commands.Result.Success

 

if __name__=="__main__":

    DupBorder()
```