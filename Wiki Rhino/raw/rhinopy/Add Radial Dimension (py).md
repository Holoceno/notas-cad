---
title: "Add Radial Dimension"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-radial-dimension/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add radial dimensions to a selected curve."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [create, radial, dimensions, Other]
---
Demonstrates how to add radial dimensions to a selected curve.

```python
from Rhino import RhinoMath
from Rhino.DocObjects import ObjectType
from Rhino.Commands import Result
from Rhino.Geometry import RadialDimension, AnnotationType
from Rhino.Input import RhinoGet
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select curve for radius dimension", True, ObjectType.Curve)
    if rc != Result.Success:
        return rc
    curve, curve_parameter = obj_ref.CurveParameter()
    if curve == None:
        return Result.Failure

    if curve.IsLinear() or curve.IsPolyline():
        print("Curve must be non-linear.")
        return Result.Nothing

    # in this example just deal with planar curves
    if not curve.IsPlanar():
        print("Curve must be planar.")
        return Result.Nothing

    point_on_curve = curve.PointAt(curve_parameter)
    curvature_vector = curve.CurvatureAt(curve_parameter)
    len = curvature_vector.Length
    if len < RhinoMath.SqrtEpsilon:
        print("Curve is almost linear and therefore has no curvature.")
        return Result.Nothing

    center = point_on_curve + (curvature_vector/(len*len))
    _, plane = curve.TryGetPlane()
    indicator_point = point_on_curve + (point_on_curve - center) * 0.5
    radial_dimension = RadialDimension(AnnotationType.Radius, plane, center, point_on_curve, indicator_point)
    doc.Objects.AddRadialDimension(radial_dimension)
    doc.Views.Redraw()
    return Result.Success

if __name__=="__main__":
    RunCommand()
```
