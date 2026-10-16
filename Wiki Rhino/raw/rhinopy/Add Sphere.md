---
title: "Add Sphere"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-sphere/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to create a sphere from a center point and radius."
tags:
  - "clippings"
---
Demonstrates how to create a sphere from a center point and radius.

```cs
partial class Examples

{

  public static Rhino.Commands.Result AddSphere(Rhino.RhinoDoc doc)

  {

    Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);

    const double radius = 5.0;

    Rhino.Geometry.Sphere sphere = new Rhino.Geometry.Sphere(center, radius);

    if( doc.Objects.AddSphere(sphere) != Guid.Empty )

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

  Public Shared Function AddSphere(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result

    Dim center As New Rhino.Geometry.Point3d(0, 0, 0)

    Const radius As Double = 5.0

    Dim sphere As New Rhino.Geometry.Sphere(center, radius)

    If doc.Objects.AddSphere(sphere) <> Guid.Empty Then

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

 

def AddSphere():

    center = Rhino.Geometry.Point3d(0, 0, 0)

    radius = 5.0

    sphere = Rhino.Geometry.Sphere(center, radius)

    if scriptcontext.doc.Objects.AddSphere(sphere)!=System.Guid.Empty:

        scriptcontext.doc.Views.Redraw()

        return Rhino.Commands.Result.Success

    return Rhino.Commands.Result.Failure

 

 

if __name__ == "__main__":

    AddSphere()
```

<iframe src="https://accounts.rhino3d.com/login-status-iframe"></iframe>