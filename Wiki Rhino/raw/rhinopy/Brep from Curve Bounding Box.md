---
title: "Brep from Curve Bounding Box"
source: "https://developer.rhino3d.com/samples/rhinocommon/brep-from-curve-bounding-box/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to create a valid Brep from a curve's bounding box."
tags:
  - "clippings"
---
Demonstrates how to create a valid Brep from a curve's bounding box.

```python
import Rhino

from Rhino.Geometry import *

from Rhino.Commands import Result

from Rhino.Input import RhinoGet

from Rhino.DocObjects import ObjectType

import rhinoscriptsyntax as rs

from scriptcontext import doc

 

def RunCommand():

    rc, objRef = RhinoGet.GetOneObject("Select curve", False, ObjectType.Curve)

    if rc != Result.Success:

        return rc

    curve = objRef.Curve()

    if None == curve:

        return Result.Failure

 

    view = doc.Views.ActiveView

    plane = view.ActiveViewport.ConstructionPlane()

    # Create a construction plane aligned bounding box

    bbox = curve.GetBoundingBox(plane)

 

    if bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0:

        print "the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created."

        return Result.Failure

 

    brep = Brep.CreateFromBox(bbox)

    doc.Objects.AddBrep(brep)

    doc.Views.Redraw()

 

    return Result.Success

 

if __name__ == "__main__":

    print RunCommand()
```