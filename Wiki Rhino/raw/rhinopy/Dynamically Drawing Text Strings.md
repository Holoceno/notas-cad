---
title: "Dynamically Drawing Text Strings"
source: "https://developer.rhino3d.com/samples/rhinocommon/dynamically-drawing-text-strings/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to dynamically draw text strings relative to a given screen to world transform."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [dynamically, drawing, text, strings, Other]
---
Demonstrates how to dynamically draw text strings relative to a given screen to world transform.

```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Commands import *
from Rhino.Input.Custom import *
from System.Drawing import Color

def RunCommand():
    gp = GetDrawStringPoint()
    gp.SetCommandPrompt("Point")
    gp.Get()
    return gp.CommandResult()

class GetDrawStringPoint(GetPoint):
    def OnDynamicDraw(self, e):
        xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen)

        current_point = e.CurrentPoint
        current_point.Transform(xform)
        screen_point = Point2d(current_point.X, current_point.Y)

        msg = "screen {0}, {1}".format(screen_point.X, screen_point.Y)
        e.Display.Draw2dText(msg, Color.Blue, screen_point, False)

if __name__ == "__main__":
    RunCommand()
```
