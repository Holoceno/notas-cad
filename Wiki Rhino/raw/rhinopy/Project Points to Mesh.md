---
title: "Project Points to Mesh"
source: "https://developer.rhino3d.com/samples/rhinocommon/project-points-to-mesh/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to project points to a mesh."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [project, points, mesh, Other]
---
Demonstrates how to project points to a mesh.

```python
from System.Collections.Generic import *
from Rhino import *
from Rhino.Commands import *
from Rhino.Geometry import *
from Rhino.Geometry.Intersect import *
from Rhino.Input import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("mesh", False, ObjectType.Mesh)
    if rc != Result.Success: return rc
    mesh = obj_ref.Mesh()

    rc, obj_ref_pts = RhinoGet.GetMultipleObjects("points", False, ObjectType.Point)
    if rc != Result.Success: return rc
    points = []
    for obj_ref_pt in obj_ref_pts:
        pt = obj_ref_pt.Point().Location
        points.append(pt)

    prj_points, indices = Intersection.ProjectPointsToMeshesEx({mesh}, points, Vector3d(0, 1, 0), 0)
    for prj_pt in prj_points:
        doc.Objects.AddPoint(prj_pt)
    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```
