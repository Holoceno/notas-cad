---
title: "Overlay Text Display Conduit"
source: "https://developer.rhino3d.com/samples/rhinocommon/overlay-text-display-conduit/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to use a display conduit to draw overlay text."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [display, conduit, draw, overlay, text, Draw]
---
Demonstrates how to use a display conduit to draw overlay text.

```cs
class CustomConduit : Rhino.Display.DisplayConduit
{
  protected override void DrawForeground(Rhino.Display.DrawEventArgs e)
  {
    var bounds = e.Viewport.Bounds;
    var pt = new Rhino.Geometry.Point2d(bounds.Right - 100, bounds.Bottom - 30);
    e.Display.Draw2dText("Hello", System.Drawing.Color.Red, pt, false);
  }
}

partial class Examples
{
  readonly static CustomConduit m_customconduit = new CustomConduit();
  public static Rhino.Commands.Result DrawOverlay(RhinoDoc doc)
  {
    // toggle conduit on/off
    m_customconduit.Enabled = !m_conduit.Enabled;

    RhinoApp.WriteLine("Custom conduit enabled = {0}", m_customconduit.Enabled);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
