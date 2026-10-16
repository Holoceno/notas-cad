---
title: "Instance Definition Objects"
source: "https://developer.rhino3d.com/samples/rhinocommon/instance-definition-objects/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to print (or list) the objects that make up a block definition."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [list, block, definition, geometry, Blocks]
---
Demonstrates how to print (or list) the objects that make up a block definition.

```python
import Rhino
import scriptcontext

def InstanceDefinitionObjects():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select instance", False, Rhino.DocObjects.ObjectType.InstanceReference)
    if rc != Rhino.Commands.Result.Success: return

    iref = objref.Object()
    if iref:
        idef = iref.InstanceDefinition
        if idef:
            rhino_objects = idef.GetObjects()
            for i, rhobj in enumerate(rhino_objects):
                print("Object", i, "=", rhobj.Id)

if __name__=="__main__":
    InstanceDefinitionObjects()
```
