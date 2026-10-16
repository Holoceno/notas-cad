---
title: "Delete Block Instance Definition"
source: "https://developer.rhino3d.com/samples/rhinocommon/delete-block-instance-definition/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to delete a block instance definition given the name of the block."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [delete, instance, definition, block, Blocks]
---
Demonstrates how to delete a block instance definition given the name of the block.

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc

def Delete():
    blockName = rs.GetString("block to delete")
    instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
    if not instanceDefinition:
        print("{0} block does not exist".format(blockName))
        return

    rs.DeleteBlock(blockName)

if __name__ == "__main__":
    Delete()
```
