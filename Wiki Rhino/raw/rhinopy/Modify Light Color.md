---
title: "Modify Light Color"
source: "https://developer.rhino3d.com/samples/rhinocommon/modify-light-color/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to change the color of a user-specified light."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [modify, lights, color, Other]
---
Demonstrates how to change the color of a user-specified light.

```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Input import *
from Rhino.UI import *
from Rhino.Commands import Result
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select light to change color", True, ObjectType.Light)
    if rc != Result.Success:
        return rc
    light = obj_ref.Light()
    if light == None:
        return Result.Failure

    b, color = Dialogs.ShowColorDialog(light.Diffuse)
    if b:
        light.Diffuse = color

    doc.Lights.Modify(obj_ref.ObjectId, light)
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```
