---
title: "Set Viewport Name"
source: "https://developer.rhino3d.com/samples/rhinocommon/set-viewport-name/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to set a viewport's name or title."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [setting, viewports, title, Viewports and Views]
---
Demonstrates how to set a viewport's name or title.

```cs
partial class Examples
{
  public static Result SetViewName(RhinoDoc doc)
  {
    var view = doc.Views.ActiveView;
    if (view == null)
      return Result.Failure;

    view.MainViewport.Name = "Facade";
    return Result.Success;
  }
}
```
