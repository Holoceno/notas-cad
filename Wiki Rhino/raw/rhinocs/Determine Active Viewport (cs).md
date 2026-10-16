---
title: "Determine Active Viewport"
source: "https://developer.rhino3d.com/samples/rhinocommon/determine-active-viewport/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine the active viewport name, even in a layout or a detail view."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [determine, active, viewport, Viewports and Views]
---
Demonstrates how to determine the active viewport name, even in a layout or a detail view.

```cs
partial class Examples
{
  public static Rhino.Commands.Result ActiveViewport(Rhino.RhinoDoc doc)
  {
    Rhino.Display.RhinoView view = doc.Views.ActiveView;
    if (view == null)
      return Rhino.Commands.Result.Failure;

    Rhino.Display.RhinoPageView pageview = view as Rhino.Display.RhinoPageView;
    if (pageview != null)
    {
      string layout_name = pageview.PageName;
      if (pageview.PageIsActive)
      {
        Rhino.RhinoApp.WriteLine("The layout {0} is active", layout_name);
      }
      else
      {
        string detail_name = pageview.ActiveViewport.Name;
        Rhino.RhinoApp.WriteLine("The detail {0} on layout {1} is active", detail_name, layout_name);
      }
    }
    else
    {
      string viewport_name = view.MainViewport.Name;
      Rhino.RhinoApp.WriteLine("The viewport {0} is active", viewport_name);
    }
    return Rhino.Commands.Result.Success;
  }
}
```
