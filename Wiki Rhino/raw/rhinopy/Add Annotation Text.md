---
title: "Add Annotation Text"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-annotation-text/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-03
description: "Rhinoceros 3D: Demonstrates how to add annotation text to a Rhino model at a specific location."
tags:
  - "clippings"
---
Demonstrates how to add annotation text to a Rhino model at a specific location.

```python
import Rhino

import scriptcontext

import System.Guid

 

def AddAnnotationText():

    pt = Rhino.Geometry.Point3d(10, 0, 0)

    text = "Hello RhinoCommon"

    height = 2.0

    font = "Arial"

    plane = scriptcontext.doc.Views.ActiveView.ActiveViewport.ConstructionPlane()

    plane.Origin = pt

    id = scriptcontext.doc.Objects.AddText(text, plane, height, font, False, False)

    if id!=System.Guid.Empty:

        scriptcontext.doc.Views.Redraw()

        return Rhino.Commands.Result.Success

    return Rhino.Commands.Result.Failure

 

 

if __name__=="__main__":

    AddAnnotationText()
```