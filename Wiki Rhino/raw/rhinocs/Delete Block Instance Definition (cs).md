---
title: "Delete Block Instance Definition"
source: "https://developer.rhino3d.com/samples/rhinocommon/delete-block-instance-definition/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to delete a block instance definition given the name of the block."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [delete, instance, definition, block, Blocks]
---
Demonstrates how to delete a block instance definition given the name of the block.

```cs
partial class Examples
{
  public static Result DeleteBlock(RhinoDoc doc)
  {
    // Get the name of the instance definition to rename
    string instance_definition_name = "";
    var rc = RhinoGet.GetString("Name of block to delete", true, ref instance_definition_name);
    if (rc != Result.Success)
      return rc;
    if (string.IsNullOrWhiteSpace(instance_definition_name))
      return Result.Nothing;

    // Verify instance definition exists
    var instance_definition = doc.InstanceDefinitions.Find(instance_definition_name, true);
    if (instance_definition == null) {
      RhinoApp.WriteLine("Block \"{0}\" not found.", instance_definition_name);
      return Result.Nothing;
    }

    // Verify instance definition can be deleted
    if (instance_definition.IsReference) {
      RhinoApp.WriteLine("Unable to delete block \"{0}\".", instance_definition_name);
      return Result.Nothing;
    }

    // delete block and all references
    if (!doc.InstanceDefinitions.Delete(instance_definition.Index, true, true)) {
      RhinoApp.WriteLine("Could not delete {0} block", instance_definition.Name);
      return Result.Failure;
    }

    return Result.Success;
  }
}
```
