---
title: "Instance Definition Names"
source: "https://developer.rhino3d.com/samples/rhinocommon/instance-definition-names/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to print the instance definition names."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [instance, definition, names, Other]
---
Demonstrates how to print the instance definition names.

```cs
partial class Examples
{
  public static Result InstanceDefinitionNames(RhinoDoc doc)
  {
    var instance-definition-names = (from instance_definition in doc.InstanceDefinitions
                                     where instance_definition != null && !instance_definition.IsDeleted
                                     select instance_definition.Name);

    foreach (var n in instance-definition-names)
      RhinoApp.WriteLine("Instance definition = {0}", n);

    return Result.Success;
  }
}
```
