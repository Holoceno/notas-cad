---
title: "Change Dimension Style"
source: "https://developer.rhino3d.com/samples/rhinocommon/change-dimension-style/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to change the dimension style on all objects in a Rhino document."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [change, dimension, style, Other]
---
Demonstrates how to change the dimension style on all objects in a Rhino document.

```cs
partial class Examples
{
  public static Result ChangeDimensionStyle(RhinoDoc doc)
  {
    foreach (var rhino_object in doc.Objects.GetObjectList(ObjectType.Annotation))
    {
      var annotation_object = rhino_object as AnnotationObjectBase;
      if (annotation_object == null) continue;

      var annotation = annotation_object.Geometry as AnnotationBase;
      if (annotation == null) continue;

      if (annotation.Index == doc.DimStyles.CurrentDimensionStyleIndex) continue;

      annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex;
      annotation_object.CommitChanges();
    }

    doc.Views.Redraw();

    return Result.Success;
  }
}
```
