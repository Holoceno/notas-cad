---
title: "Move Objects to Current Layer"
source: "https://developer.rhino3d.com/samples/rhinocommon/move-objects-to-current-layer/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to move object to the currently active layer."
tags:
  - "clippings"
---
Demonstrates how to move object to the currently active layer.

```python
from Rhino import *

from Rhino.Commands import *

from Rhino.DocObjects import *

from scriptcontext import doc

 

def RunCommand():

    # all non-light objects that are selected

    object_enumerator_settings = ObjectEnumeratorSettings()

    object_enumerator_settings.IncludeLights = False

    object_enumerator_settings.IncludeGrips = True

    object_enumerator_settings.NormalObjects = True

    object_enumerator_settings.LockedObjects = True

    object_enumerator_settings.HiddenObjects = True

    object_enumerator_settings.ReferenceObjects = True

    object_enumerator_settings.SelectedObjectsFilter = True

    selected_objects = doc.Objects.GetObjectList(object_enumerator_settings)

 

    current_layer_index = doc.Layers.CurrentLayerIndex

    for selected_object in selected_objects:

        selected_object.Attributes.LayerIndex = current_layer_index

        selected_object.CommitChanges()

 

    doc.Views.Redraw()

    return Result.Success

 

if __name__ == "__main__":

    RunCommand()
```