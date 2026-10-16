---
title: "Get Object UUID"
source: "https://developer.rhino3d.com/samples/rhinocommon/get-object-uuid/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to get the UUID (sometimes called GUID) of a Rhino object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [objects, uuid, Adding Objects]
---
Demonstrates how to get the UUID (sometimes called GUID) of a Rhino object.

```python
import rhinoscriptsyntax as rs

obj_id = rs.GetObject("Select object")
if obj_id != None:
    print("The object's unique id is {0}".format(obj_id))
```
