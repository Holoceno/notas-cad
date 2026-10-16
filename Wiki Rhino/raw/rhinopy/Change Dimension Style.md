---
title: "Change Dimension Style"
source: "https://developer.rhino3d.com/samples/rhinocommon/change-dimension-style/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to change the dimension style on all objects in a Rhino document."
tags:
  - "clippings"
---
Demonstrates how to change the dimension style on all objects in a Rhino document.

```python
from Rhino import *

from Rhino.DocObjects import *

from Rhino.Commands import *

from Rhino.Geometry import *

from scriptcontext import doc

 

def RunCommand():

    for annotation_object in doc.Objects.GetObjectList(ObjectType.Annotation):

        if not isinstance (annotation_object, AnnotationObjectBase):

            continue

 

        annotation = annotation_object.Geometry

 

        if annotation.Index == doc.DimStyles.CurrentDimensionStyleIndex:

            continue

 

        annotation.Index = doc.DimStyles.CurrentDimensionStyleIndex

        annotation_object.CommitChanges()

 

    doc.Views.Redraw()

    return Result.Success

 

if __name__ == "__main__":

    RunCommand()
```