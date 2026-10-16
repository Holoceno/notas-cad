---
title: "Find Objects by Name"
source: "https://developer.rhino3d.com/samples/rhinocommon/find-objects-by-name/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to find objects by their name or label."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [find, objects, name, Adding Objects]
---
Demonstrates how to find objects by their name or label.

```python
import Rhino
import scriptcontext
import System.Guid

def FindObjectsByName():
    name = "abc"
    settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    settings.NameFilter = name
    ids = [rhobj.Id for rhobj in scriptcontext.doc.Objects.GetObjectList(settings)]
    if not ids:
        print("No objects with the name", name)
        return Rhino.Commands.Result.Failure
    else:
        print("Found", len(ids), "objects")
        for id in ids: print("  ", id)
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    FindObjectsByName()
```
