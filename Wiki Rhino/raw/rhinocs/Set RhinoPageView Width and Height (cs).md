---
title: "Set RhinoPageView Width and Height"
source: "https://developer.rhino3d.com/samples/rhinocommon/set-rhinopageview-width-and-height/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to set the RhinoPageView width and height dimensions."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [rhinopageview, width, height, Other]
---
Demonstrates how to set the RhinoPageView width and height dimensions.

```cs
partial class Examples
{
  public static Result SetRhinoPageViewWidthAndHeight(RhinoDoc doc)
  {
    var width = 1189;
    var height = 841;
    var page_views = doc.Views.GetPageViews();
    int page_number = (page_views==null) ? 1 : page_views.Length + 1;
    var pageview = doc.Views.AddPageView(string.Format("A0_{0}",page_number), width, height);

    int new_width = width;
    var rc = RhinoGet.GetInteger("new width", false, ref new_width);
    if (rc != Result.Success || new_width <= 0) return rc;

    int new_height = height;
    rc = RhinoGet.GetInteger("new height", false, ref new_height);
    if (rc != Result.Success || new_height <= 0) return rc;

    pageview.PageWidth = new_width;
    pageview.PageHeight = new_height;
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
