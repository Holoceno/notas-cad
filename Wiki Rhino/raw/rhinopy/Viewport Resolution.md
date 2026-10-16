---
title: "Viewport Resolution"
source: "https://developer.rhino3d.com/samples/rhinocommon/viewport-resolution/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Print Active Viewport Resolution"
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [print, active, viewport, resolution, Viewports and Views]
---
Print Active Viewport Resolution

```python
from scriptcontext import doc

activeViewport = doc.Views.ActiveView.ActiveViewport
print("Name = {0}: Width = {1}, Height = {2}".format(
    activeViewport.Name, activeViewport.Size.Width, activeViewport.Size.Height))
```
