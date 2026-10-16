---
title: "Duplicate Object"
source: "https://developer.rhino3d.com/samples/rhinocommon/duplicate-object/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to clone (or copy, or duplicate) a Rhino object."
tags:
  - "clippings"
---
Demonstrates how to clone (or copy, or duplicate) a Rhino object.

```python
from System import *

from Rhino import *

from Rhino.Commands import *

from Rhino.DocObjects import *

from Rhino.Input import *

from scriptcontext import doc

 

def RunCommand():

 

    rc, obj_ref = RhinoGet.GetOneObject("Select object to duplicate", False, ObjectType.AnyObject)

    if rc != Result.Success:

        return rc

    rhino_object = obj_ref.Object()

 

    geometry_base = rhino_object.DuplicateGeometry()

    if geometry_base != None:

        if doc.Objects.Add(geometry_base) != Guid.Empty:

            doc.Views.Redraw()

 

    return Result.Success

 

if __name__ == "__main__":

    RunCommand()
```