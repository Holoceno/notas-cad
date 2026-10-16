---
title: "Instance Definition Names"
source: "https://developer.rhino3d.com/samples/rhinocommon/instance-definition-names/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to print the instance definition names."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [instance, definition, names, Other]
---
Demonstrates how to print the instance definition names.

```python
from scriptcontext import doc

def RunCommand():
    instanceDefinitionNames = [instanceDefinition.Name for instanceDefinition in doc.InstanceDefinitions if instanceDefinition != None and not instanceDefinition.IsDeleted]

    for n in instanceDefinitionNames:
        print("instance definition = {0}".format(n))

if __name__ == "__main__":
    RunCommand()
```
