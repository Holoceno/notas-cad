---
title: "Display Precision"
source: "https://developer.rhino3d.com/samples/rhinocommon/display-precision/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to change the display precision in a Rhino model."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [changing, display, precision, Other]
---
Demonstrates how to change the display precision in a Rhino model.

```python
from Rhino.Commands import Result
from scriptcontext import doc
import rhinoscriptsyntax as rs

def RunCommand():
    distance_display_precision = rs.GetInteger("Display precision",
        doc.ModelDistanceDisplayPrecision, 0, 7)
    if distance_display_precision == None: return Result.Nothing

    if distance_display_precision != doc.ModelDistanceDisplayPrecision:
        doc.ModelDistanceDisplayPrecision = distance_display_precision

    return Result.Success

if __name__ ==  "__main__":
    RunCommand()
```
