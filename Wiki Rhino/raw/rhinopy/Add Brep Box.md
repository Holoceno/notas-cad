---
title: "Add Brep Box"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-brep-box/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-03
description: "Rhinoceros 3D: Demonstrates how to add a Brep Box to a Rhino model by specifying two points."
tags:
  - "clippings"
---
Demonstrates how to add a Brep Box to a Rhino model by specifying two points.

```python
import Rhino

import scriptcontext

import System.Guid

 

def AddBrepBox():

    pt0 = Rhino.Geometry.Point3d(0, 0, 0)

    pt1 = Rhino.Geometry.Point3d(10, 10, 10)

    box = Rhino.Geometry.BoundingBox(pt0, pt1)

    brep = box.ToBrep()

    rc = Rhino.Commands.Result.Failure

    if( scriptcontext.doc.Objects.AddBrep(brep) != System.Guid.Empty ):

        rc = Rhino.Commands.Result.Success

        scriptcontext.doc.Views.Redraw()

    return rc

 

if( __name__ == "__main__" ):

    AddBrepBox()
```