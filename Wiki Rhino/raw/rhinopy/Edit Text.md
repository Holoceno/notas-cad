---
title: "Edit Text"
source: "https://developer.rhino3d.com/samples/rhinocommon/edit-text/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to edit selected text, replacing it with new text."
tags:
  - "clippings"
---
Demonstrates how to edit selected text, replacing it with new text.

```python
import Rhino

import scriptcontext

 

def EditText():

    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select text", False, Rhino.DocObjects.ObjectType.Annotation)

    if rc!=Rhino.Commands.Result.Success: return

 

    textobj = objref.Object()

    if not textobj: return

 

    str = textobj.Geometry.Text

    rc, str = Rhino.Input.RhinoGet.GetString("New text", False, str)

    if rc!=Rhino.Commands.Result.Success: return

 

    textobj.Geometry.Text = str;

    textobj.CommitChanges();

    scriptcontext.doc.Views.Redraw();

 

if __name__=="__main__":

    EditText()
```