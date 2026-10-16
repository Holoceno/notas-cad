---
title: "Add Named View"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-named-view/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a named view to a Rhino model from a user-specified view and camera location."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, named, view, Adding Objects, Viewports and Views]
---
Demonstrates how to add a named view to a Rhino model from a user-specified view and camera location.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddNamedView(Rhino.RhinoDoc doc)
  {
    Rhino.Display.RhinoView view;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetView("Select view to adjust", out view);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Geometry.Point3d location;
    rc = Rhino.Input.RhinoGet.GetPoint("Camera Location", false, out location);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
    gp.SetCommandPrompt("Look At Location");
    gp.DrawLineFromPoint(location, false);
    gp.Get();
    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();
    Rhino.Geometry.Point3d lookat = gp.Point();

    string name = view.ActiveViewport.Name;
    rc = Rhino.Input.RhinoGet.GetString("Name", true, ref name);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Display.RhinoViewport vp = view.ActiveViewport;
    // save the current viewport projection
    vp.PushViewProjection();
    vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis;
    vp.SetCameraLocation(location, false);
    vp.SetCameraDirection(lookat - location, true);
    vp.Name = name;

    doc.NamedViews.Add(name, vp.Id);
    view.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
