---
title: "Add Torus"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-torus/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to construct a torus from a set of radii and a plane."
tags:
  - "clippings"
---
Demonstrates how to construct a torus from a set of radii and a plane.

```cs
partial class Examples

{

  public static Rhino.Commands.Result AddTorus(Rhino.RhinoDoc doc)

  {

    const double major_radius = 4.0;

    const double minor_radius = 2.0;

 

    Rhino.Geometry.Plane plane = Rhino.Geometry.Plane.WorldXY;

    Rhino.Geometry.Torus torus = new Rhino.Geometry.Torus(plane, major_radius, minor_radius);

    Rhino.Geometry.RevSurface revsrf = torus.ToRevSurface();

    if (doc.Objects.AddSurface(revsrf) != Guid.Empty)

    {

      doc.Views.Redraw();

      return Rhino.Commands.Result.Success;

    }

    return Rhino.Commands.Result.Failure;

  }

}
```

```vbnet
Partial Friend Class Examples

  Public Shared Function AddTorus(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result

    Const major_radius As Double = 4.0

    Const minor_radius As Double = 2.0

 

    Dim plane As Rhino.Geometry.Plane = Rhino.Geometry.Plane.WorldXY

    Dim torus As New Rhino.Geometry.Torus(plane, major_radius, minor_radius)

    Dim revsrf As Rhino.Geometry.RevSurface = torus.ToRevSurface()

    If doc.Objects.AddSurface(revsrf) <> Guid.Empty Then

      doc.Views.Redraw()

      Return Rhino.Commands.Result.Success

    End If

    Return Rhino.Commands.Result.Failure

  End Function

End Class
```

```python
import Rhino

import scriptcontext

import System.Guid

 

def AddTorus():

    major_radius = 4.0

    minor_radius = 2.0

 

    plane = Rhino.Geometry.Plane.WorldXY

    torus = Rhino.Geometry.Torus(plane, major_radius, minor_radius)

    revsrf = torus.ToRevSurface()

 

    if scriptcontext.doc.Objects.AddSurface(revsrf)!=System.Guid.Empty:

        scriptcontext.doc.Views.Redraw()

        return Rhino.Commands.Result.Success

    return Rhino.Commands.Result.Failure

 

 

if __name__=="__main__":

    AddTorus()
```

<iframe src="https://accounts.rhino3d.com/login-status-iframe"></iframe>