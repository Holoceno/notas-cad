---
title: "Add Arrowheads to Curves"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-arrowheads-to-curves/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-03
description: "Rhinoceros 3D: Demonstrates how to decorate curves in a Rhino model with arrowheads."
tags:
  - "clippings"
---
Demonstrates how to decorate curves in a Rhino model with arrowheads.

```python
import Rhino

import scriptcontext

 

def ObjectDecoration():

    # Define a line

    line = Rhino.Geometry.Line(Rhino.Geometry.Point3d(0, 0, 0), Rhino.Geometry.Point3d(10, 0, 0))

 

    # Make a copy of Rhino's default object attributes

    attribs = scriptcontext.doc.CreateDefaultAttributes()

 

    # Modify the object decoration style

    attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead

 

    # Create a new curve object with our attributes

    scriptcontext.doc.Objects.AddLine(line, attribs)

    scriptcontext.doc.Views.Redraw()

 

if __name__ == "__main__":

    ObjectDecoration()
```