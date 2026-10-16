---
title: "Add Objects to Group"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-objects-to-group/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to group objects from a user-specified selection set of objects."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [add, objects, group, Adding Objects]
---
Demonstrates how to group objects from a user-specified selection set of objects.

```python
import Rhino
import scriptcontext

def AddObjectsToGroup():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select objects to group")
    go.GroupSelect = True
    go.GetMultiple(1, 0)
    if go.CommandResult()!=Rhino.Commands.Result.Success:
        return go.CommandResult()

    ids = [go.Object(i).ObjectId for i in range(go.ObjectCount)]
    index = scriptcontext.doc.Groups.Add(ids)
    scriptcontext.doc.Views.Redraw()
    if index>=0: return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__ == "__main__":
    AddObjectsToGroup()
```
