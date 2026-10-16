---
title: "Loft Surfaces"
source: "https://developer.rhino3d.com/samples/rhinocommon/loft-surfaces/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to create a lofted surface from a set of user-specified curves."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [loft, surfaces, Other]
---
Demonstrates how to create a lofted surface from a set of user-specified curves.

```python
import rhinoscriptsyntax as rs

def RunCommand():
    crvids = rs.GetObjects(message="select curves to loft", filter=rs.filter.curve, minimum_count=2)
    if not crvids: return

    rs.AddLoftSrf(object_ids=crvids, loft_type = 3) #3 = tight

if __name__ == "__main__":
    RunCommand()
```
