---
title: "Add Circle"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-circle/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-03
description: "Rhinoceros 3D: Demonstrates how to add a circle from a center point and radius."
tags:
  - "clippings"
---
Demonstrates how to add a circle from a center point and radius.

```cs
partial class Examples

{

  public static Rhino.Commands.Result AddCircle(Rhino.RhinoDoc doc)

  {

    Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);

    const double radius = 10.0;

    Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(center, radius);

    if (doc.Objects.AddCircle(c) != Guid.Empty)

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

  Public Shared Function AddCircle(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result

    Dim center As New Rhino.Geometry.Point3d(0, 0, 0)

    Const radius As Double = 10.0

    Dim c As New Rhino.Geometry.Circle(center, radius)

    If doc.Objects.AddCircle(c) <> Guid.Empty Then

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

from System import Guid

 

def AddCircle():

    center = Rhino.Geometry.Point3d(0, 0, 0)

    radius = 10.0

    c = Rhino.Geometry.Circle(center, radius)

    if scriptcontext.doc.Objects.AddCircle(c)!= Guid.Empty:

        scriptcontext.doc.Views.Redraw()

        return Rhino.Commands.Result.Success

    return Rhino.Commands.Result.Failure

 

if __name__=="__main__":

    AddCircle()
```

<iframe src="https://accounts.rhino3d.com/login-status-iframe"></iframe>