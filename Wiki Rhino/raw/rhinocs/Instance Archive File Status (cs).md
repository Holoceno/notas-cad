---
title: "Instance Archive File Status"
source: "https://developer.rhino3d.com/samples/rhinocommon/instance-archive-file-status/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to find the status of a file that contains an instance (block) definition."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [instance, archive, file, status, Other]
---
Demonstrates how to find the status of a file that contains an instance (block) definition.

```cs
partial class Examples
{
  public static Rhino.Commands.Result InstanceArchiveFileStatus(Rhino.RhinoDoc doc)
  {
    for (int i = 0; i < doc.InstanceDefinitions.Count; i++)
    {
      Rhino.DocObjects.InstanceDefinition iDef = doc.InstanceDefinitions[i];
      Rhino.DocObjects.InstanceDefinitionArchiveFileStatus iDefStatus = iDef.ArchiveFileStatus;

      string status = "Unknown";
      switch (iDefStatus)
      {
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.NotALinkedInstanceDefinition:
          status = "not a linked instance definition.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotReadable:
          status = "archive file is not readable.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotFound:
          status = "archive file cannot be found.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsUpToDate:
          status = "archive file is up-to-date.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsNewer:
          status = "archive file is newer.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsOlder:
          status = "archive file is older.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsDifferent:
          status = "archive file is different.";
          break;
      }

      Rhino.RhinoApp.WriteLine("{0} - {1}", iDef.Name, status);
    }

    return Rhino.Commands.Result.Success;
  }
}
```
