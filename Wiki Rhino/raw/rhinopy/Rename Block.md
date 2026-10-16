---
title: "Rename Block"
source: "https://developer.rhino3d.com/samples/rhinocommon/rename-block/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to rename an instance definition (block)."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [rename, instance, definition, block, Blocks]
---
Demonstrates how to rename an instance definition (block).

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc

def Rename():
    blockName = rs.GetString("block to rename")
    instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
    if not instanceDefinition:
        print("{0} block does not exist".format(blockName))
        return

    newName = rs.GetString("new name")
    instanceDefinition = doc.InstanceDefinitions.Find(newName, True)
    if instanceDefinition:
        print("the name '{0}' is already taken by another block".format(newName))
        return

    rs.RenameBlock(blockName, newName)

if __name__ == "__main__":
    Rename()
```
