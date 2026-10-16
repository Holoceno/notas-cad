---
title: "Is Planar Surface in Plane"
source: "https://developer.rhino3d.com/samples/rhinocommon/is-planar-surface-in-plane/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine if a user-selected surface is in plane."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [planar, surface, plane, Other]
---
Demonstrates how to determine if a user-selected surface is in plane.

```python
import Rhino
from Rhino.Geometry import Plane
import rhinoscriptsyntax as rs
from scriptcontext import doc
import math

def RunCommand():
    surface_id = rs.GetSurfaceObject()[0]
    if surface_id == None:
        return
    surface = rs.coercesurface(surface_id)

    corners = rs.GetRectangle()
    if corners == None:
        return

    plane = Plane(corners[0], corners[1], corners[2])

    is_or_isnt = "" if IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance) else " not "
    print("Surface is{0} in plane.".format(is_or_isnt))

def IsSurfaceInPlane(surface, plane, tolerance):
    if not surface.IsPlanar(tolerance):
        return False

    bbox = surface.GetBoundingBox(True)
    rc = True
    for corner in bbox.GetCorners():
        if math.fabs(plane.DistanceTo(corner)) > tolerance:
            rc = False
            break

    return rc

if __name__ == "__main__":
    RunCommand()
```
