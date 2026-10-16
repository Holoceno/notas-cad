---
title: "Isocurve Density"
source: "https://developer.rhino3d.com/samples/rhinocommon/isocurve-density/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to adjust the the isocurve density of a user-specified surface."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [adjusting, surface, isocurve, density, Other]
---
Demonstrates how to adjust the the isocurve density of a user-specified surface.

```cs
partial class Examples
{
  public static Rhino.Commands.Result IsocurveDensity(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select surface", false, Rhino.DocObjects.ObjectType.Surface, out objref);
    if( rc!= Rhino.Commands.Result.Success )
      return rc;

    var brep_obj = objref.Object() as Rhino.DocObjects.BrepObject;
    if( brep_obj!=null )
    {
      brep_obj.Attributes.WireDensity = 3;
      brep_obj.CommitChanges();
      doc.Views.Redraw();
    }
    return Rhino.Commands.Result.Success;
  }
}
```
