---
title: "Text Justify"
source: "https://developer.rhino3d.com/samples/rhinocommon/text-justify/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to set text justification with a specific font."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [justifying, text, entities, Other]
---
Demonstrates how to set text justification with a specific font.

```python
from scriptcontext import doc
from Rhino.Geometry import *

text_entity = TextEntity()
text_entity.Plane = Plane.WorldXY
text_entity.Text = "Hello Rhino!"
text_entity.Justification = TextJustification.MiddleCenter
text_entity.FontIndex = doc.Fonts.FindOrCreate("Arial", False, False)

doc.Objects.AddText(text_entity)
doc.Views.Redraw()
```
