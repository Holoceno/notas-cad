---
title: "Transform Breps"
source: "https://developer.rhino3d.com/samples/rhinocommon/transform-breps/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to move (or transform) a user-specified Brep object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [transform, brep, Other]
---
Demonstrates how to move (or transform) a user-specified Brep object.

```python
import Rhino
import scriptcontext

def TransformBrep():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select brep", True, Rhino.DocObjects.ObjectType.Brep)
    if rc!=Rhino.Commands.Result.Success: return

    # Simple translation transformation
    xform = Rhino.Geometry.Transform.Translation(18,-18,25)
    scriptcontext.doc.Objects.Transform(objref, xform, True)
    scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    TransformBrep()
```
