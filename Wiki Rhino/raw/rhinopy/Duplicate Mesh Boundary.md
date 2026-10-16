---
title: "Duplicate Mesh Boundary"
source: "https://developer.rhino3d.com/samples/rhinocommon/duplicated-mesh-boundary/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to create a bounding polyline from naked edges of an open mesh."
tags:
  - "clippings"
---
Demonstrates how to create a bounding polyline from naked edges of an open mesh.

```python
from Rhino.Commands import *

from Rhino.Input.Custom import *

from Rhino.DocObjects import *

from scriptcontext import doc

 

def RunCommand():

    gm = GetObject()

    gm.SetCommandPrompt("Select open mesh")

    gm.GeometryFilter = ObjectType.Mesh

    gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh

    gm.Get()

    if gm.CommandResult() != Result.Success:

        return gm.CommandResult()

    mesh = gm.Object(0).Mesh()

    if mesh == None:

        return Result.Failure

 

    polylines = mesh.GetNakedEdges()

    for polyline in polylines:

        doc.Objects.AddPolyline(polyline)

    doc.Views.Redraw()

    return Result.Success

 

if __name__ == "__main__":

    RunCommand()
```