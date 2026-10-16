---
title: "Tight Bounding Boxes for Breps"
source: "https://developer.rhino3d.com/samples/rhinocommon/tight-bounding-boxes-for-breps/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to generate tight bounding boxes for Brep objects."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [tight, bounding, boxes, breps, Other]
---
Demonstrates how to generate tight bounding boxes for Brep objects.

```python
from scriptcontext import doc
import rhinoscriptsyntax as rs
from Rhino import RhinoApp
from Rhino.Geometry import Curve, Mesh, Box
from Rhino.Input import RhinoGet
from Rhino.DocObjects import ObjectType
from Rhino.Commands import Result
from System.Collections.Generic import List

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select surface to split", True, ObjectType.Surface)
    if rc != Result.Success:
        return rc
    brep_face = obj_ref.Surface()
    if brep_face == None:
        return Result.Failure

    rc, obj_ref = RhinoGet.GetOneObject("Select cutting curve", True, ObjectType.Curve)
    if rc != Result.Success:
        return rc
    curve = obj_ref.Curve()
    if curve == None:
        return Result.Failure

    curves = List[Curve]([curve])
    split_brep = brep_face.Split(curves, doc.ModelAbsoluteTolerance)

    if split_brep == None:
        RhinoApp.WriteLine("Unable to split surface.")
        return Result.Nothing

    meshes = Mesh.CreateFromBrep(split_brep)
    print(type(meshes))
    for mesh in meshes:
        bbox = mesh.GetBoundingBox(True)
        bbox_type = bbox.IsDegenerate(doc.ModelAbsoluteTolerance)
        if bbox_type == 1: # rectangle
            # box with 8 corners flattened to rectangle with 4 corners
            box_corners = bbox.GetCorners()
            rectangle_corners = []
            for corner_point in box_corners:
                if corner_point not in rectangle_corners:
                    rectangle_corners.append(corner_point)
            # add 1st point as last to close the loop
            rectangle_corners.append(rectangle_corners[0])
            doc.Objects.AddPolyline(rectangle_corners)
            doc.Views.Redraw()
        elif bbox_type == 0: # box
            brep_box = Box(bbox).ToBrep()
            doc.Objects.AddBrep(brep_box)
            doc.Views.Redraw()
        else: # bbox invalid, point, or line
            return Result.Failure

    return Result.Success

if __name__ == "__main__":
    RunCommand()
```
