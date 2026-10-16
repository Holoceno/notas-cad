---
title: "Surface from Edge Curves"
source: "https://developer.rhino3d.com/samples/rhinocommon/surface-from-edge-curves/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Create a Surface from Edge Curves"
tags:
  - "clippings"
---
Create a Surface from Edge Curves

```python
from Rhino import *

from Rhino.Commands import *

from Rhino.DocObjects import *

from Rhino.Geometry import *

from Rhino.Input.Custom import *

from scriptcontext import doc

 

def RunCommand():

    go = GetObject()

    go.SetCommandPrompt("Select 2, 3, or 4 open curves")

    go.GeometryFilter = ObjectType.Curve

    go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve

    go.GetMultiple(2, 4)

    if go.CommandResult() != Result.Success:

        return go.CommandResult()

 

    curves = [o.Curve() for o in go.Objects()]

 

    brep = Brep.CreateEdgeSurface(curves)

 

    if brep != None:

        doc.Objects.AddBrep(brep)

        doc.Views.Redraw()

 

    return Result.Success

 

if __name__ == "__main__":

    RunCommand()
```