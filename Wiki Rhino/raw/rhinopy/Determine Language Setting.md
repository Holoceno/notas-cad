---
title: "Determine Language Setting"
source: "https://developer.rhino3d.com/samples/rhinocommon/determine-language-setting/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine Rhino's language setting."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [determine, rhinos, language, setting, Other]
---
Demonstrates how to determine Rhino's language setting.

```python
import rhinoscriptsyntax as rs
import System

locale_id = rs.LocaleID()
culture = System.Globalization.CultureInfo(locale_id)
print(culture.EnglishName)
```
