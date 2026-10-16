---
title: "Explode Hatch"
source: "https://developer.rhino3d.com/samples/rhinocommon/explode-hatch/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to explode a user-specified hatch object into its constituent parts (curves, points, etc.)"
tags:
  - "clippings"
---
Demonstrates how to explode a user-specified hatch object into its constituent parts (curves, points, etc.)

```python
import Rhino

import scriptcontext

 

def ExplodeHatch():

    filter = Rhino.DocObjects.ObjectType.Hatch

    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select hatch to explode", False, filter)

    if rc != Rhino.Commands.Result.Success: return

 

    hatch = objref.Geometry()

    if not hatch: return

 

    hatch_geom = hatch.Explode()

    if hatch_geom:

        for geom in hatch_geom:

            if geom.ObjectType == Rhino.DocObjects.ObjectType.Point:

                scriptcontext.doc.Objects.AddPoint(geom)

            elif geom.ObjectType == Rhino.DocObjects.ObjectType.Curve:

                scriptcontext.doc.Objects.AddCurve(geom)

            elif geom.ObjectType == Rhino.DocObjects.ObjectType.Brep:

                scriptcontext.doc.Objects.AddBrep(geom)

        scriptcontext.doc.Views.Redraw()

 

if __name__=="__main__":

    ExplodeHatch()
```