---
title: "Intersecting Line and Circle"
source: "https://developer.rhino3d.com/samples/rhinocommon/intersect-line-and-circle/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to find the intersection point(s) of a circle and a line."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [intersecting, line, with, circle, Other]
---
Demonstrates how to find the intersection point(s) of a circle and a line.

```cs
partial class Examples
{
  public static Result IntersectLineCircle(RhinoDoc doc)
  {
    Circle circle;
    var rc = RhinoGet.GetCircle(out circle);
    if (rc != Result.Success)
      return rc;
    doc.Objects.AddCircle(circle);
    doc.Views.Redraw();

    Line line;
    rc = RhinoGet.GetLine(out line);
    if (rc != Result.Success)
      return rc;
    doc.Objects.AddLine(line);
    doc.Views.Redraw();

    double t1, t2;
    Point3d point1, point2;
    var line_circle_intersect = Intersection.LineCircle(line, circle, out t1, out point1, out t2, out point2);
    string msg = "";
    switch (line_circle_intersect) {
      case LineCircleIntersection.None:
        msg = "line does not intersect circle";
        break;
      case LineCircleIntersection.Single:
        msg = string.Format("line intersects circle at point ({0})", point1);
        doc.Objects.AddPoint(point1);
        break;
      case LineCircleIntersection.Multiple:
        msg = string.Format("line intersects circle at points ({0}) and ({1})",
          point1, point2);
        doc.Objects.AddPoint(point1);
        doc.Objects.AddPoint(point2);
        break;
    }
    RhinoApp.WriteLine(msg);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
