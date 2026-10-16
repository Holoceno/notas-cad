---
title: "Add Leader"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-leader/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to add a leaders to your Rhino model from an array of points."
tags:
  - "clippings"
---
Demonstrates how to add a leaders to your Rhino model from an array of points.

```cs
partial class Examples

{

  public static Result Leader(RhinoDoc doc)

  {

    var points = new Point3d[]

    {

      new Point3d(1, 1, 0),

      new Point3d(5, 1, 0),

      new Point3d(5, 5, 0),

      new Point3d(9, 5, 0)

    };

 

    var xy_plane = Plane.WorldXY;

 

    var points2d = new List<Point2d>();

    foreach (var point3d in points)

    {

      double x, y;

      if (xy_plane.ClosestParameter(point3d, out x, out y))

      {

        var point2d = new Point2d(x, y);

        if (points2d.Count < 1 || point2d.DistanceTo(points2d.Last<Point2d>()) > RhinoMath.SqrtEpsilon)

          points2d.Add(point2d);

      }

    }

 

    doc.Objects.AddLeader(xy_plane, points2d);

    doc.Views.Redraw();

    return Result.Success;

  }

}
```

```vbnet
Partial Friend Class Examples

  Public Shared Function Leader(ByVal doc As RhinoDoc) As Result

    Dim points = New Point3d() {

        New Point3d(1, 1, 0),

        New Point3d(5, 1, 0),

        New Point3d(5, 5, 0),

        New Point3d(9, 5, 0)

    }

 

    Dim xy_plane = Plane.WorldXY

 

    Dim points2d = New List(Of Point2d)()

    For Each point3d In points

      Dim x As Double = Nothing, y As Double = Nothing

      If xy_plane.ClosestParameter(point3d, x, y) Then

        Dim point2d = New Point2d(x, y)

        If points2d.Count < 1 OrElse point2d.DistanceTo(points2d.Last()) > RhinoMath.SqrtEpsilon Then

          points2d.Add(point2d)

        End If

      End If

    Next point3d

 

    doc.Objects.AddLeader(xy_plane, points2d)

    doc.Views.Redraw()

    Return Result.Success

  End Function

End Class
```

```python
import rhinoscriptsyntax as rs

 

def RunCommand():

    points = [(1,1,0), (5,1,0), (5,5,0), (9,5,0)]

    rs.AddLeader(points)

 

if __name__ == "__main__":

    RunCommand()
```

<iframe src="https://accounts.rhino3d.com/login-status-iframe"></iframe>