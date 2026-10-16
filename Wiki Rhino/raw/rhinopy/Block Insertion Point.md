---
title: "Block Insertion Point"
source: "https://developer.rhino3d.com/samples/rhinocommon/block-insertion-point/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to set (or reset) the block insertion point of a block instance."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [obtain, insertion, point, block, Blocks]
---
Demonstrates how to set (or reset) the block insertion point of a block instance.

```python
import Rhino
import scriptcontext

def BlockInsertionPoint():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select instance", True, Rhino.DocObjects.ObjectType.InstanceReference)
    if rc!=Rhino.Commands.Result.Success: return rc;
    instance = objref.Object()
    if instance:
        pt = instance.InsertionPoint
        scriptcontext.doc.Objects.AddPoint(pt)
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__=="__main__":
    BlockInsertionPoint()
```
