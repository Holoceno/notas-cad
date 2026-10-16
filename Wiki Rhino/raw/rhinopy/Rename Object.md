---
title: "Rename Object"
source: "https://developer.rhino3d.com/samples/rhinocommon/rename-object/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to rename a user-specified object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [rename, object, Adding Objects]
---
Demonstrates how to rename a user-specified object.

```python
import rhinoscriptsyntax as rs

obj_id = rs.GetObject("Select object to change name")
object_new_name = rs.GetString("New object name")

rs.ObjectName(obj_id, object_new_name)
```
