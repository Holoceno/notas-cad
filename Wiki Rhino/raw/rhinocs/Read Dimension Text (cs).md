---
title: "Read Dimension Text"
source: "https://developer.rhino3d.com/samples/rhinocommon/read-dimension-text/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to read dimension text from an annotation object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [read, dimension, text, Other]
---
Demonstrates how to read dimension text from an annotation object.

```cs
partial class Examples
{
  public static Result ReadDimensionText(RhinoDoc doc)
  {
    var go = new GetObject();
    go.SetCommandPrompt("Select annotation");
    go.GeometryFilter = ObjectType.Annotation;
    go.Get();
    if (go.CommandResult() != Result.Success)
      return Result.Failure;
    var annotation = go.Object(0).Object() as AnnotationObjectBase;
    if (annotation == null)
      return Result.Failure;

    RhinoApp.WriteLine("Annotation text = {0}", annotation.DisplayText);

    return Result.Success;
  }
}
```
