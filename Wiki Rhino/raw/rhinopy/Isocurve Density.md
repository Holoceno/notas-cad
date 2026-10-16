---
title: "Isocurve Density"
source: "https://developer.rhino3d.com/samples/rhinocommon/isocurve-density/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to adjust the the isocurve density of a user-specified surface."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [adjusting, surface, isocurve, density, Other]
---
Demonstrates how to adjust the the isocurve density of a user-specified surface.

```python
import Rhino
import scriptcontext

def IsocurveDensity():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface", False, Rhino.DocObjects.ObjectType.Surface)
    if rc!= Rhino.Commands.Result.Success: return

    brep_obj = objref.Object()
    if brep_obj:
        brep_obj.Attributes.WireDensity = 3
        brep_obj.CommitChanges()
        scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    IsocurveDensity()
```
