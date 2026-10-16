---
title: "Get Angle"
source: "https://developer.rhino3d.com/samples/rhinocommon/get-angle/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to interactively pick an angle given a base point and two reference points."
tags:
  - "clippings"
---
Demonstrates how to interactively pick an angle given a base point and two reference points.

```python
from Rhino import *

from Rhino.Commands import *

from Rhino.Input import *

from Rhino.Input.Custom import *

 

def RunCommand():

    gp = GetPoint()

    gp.SetCommandPrompt("Base point")

    gp.Get()

    if gp.CommandResult() != Result.Success:

        return gp.CommandResult()

    base_point = gp.Point()

 

    gp.SetCommandPrompt("First reference point")

    gp.DrawLineFromPoint(base_point, True)

    gp.Get()

    if gp.CommandResult() != Result.Success:

        return gp.CommandResult()

    first_point = gp.Point()

 

 

    rc, angle_radians = RhinoGet.GetAngle("Second reference point", base_point, first_point, 0)

    if rc == Result.Success:

        print "Angle = {0} degrees".format(RhinoMath.ToDegrees(angle_radians))

    return rc

 

if __name__ == "__main__":

    RunCommand()
```