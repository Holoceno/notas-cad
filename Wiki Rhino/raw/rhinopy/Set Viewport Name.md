---
title: "Set Viewport Name"
source: "https://developer.rhino3d.com/samples/rhinocommon/set-viewport-name/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to set a viewport's name or title."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [setting, viewports, title, Viewports and Views]
---
Demonstrates how to set a viewport's name or title.

```python
from Rhino.Commands import *
import rhinoscriptsyntax as rs
from scriptcontext import doc

def RunCommand():
    view = doc.Views.ActiveView
    if view == None:
        return Result.Failure

    view.MainViewport.Name = "Facade"
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```
