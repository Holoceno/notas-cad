---
title: "Determine Active Viewport"
source: "https://developer.rhino3d.com/samples/rhinocommon/determine-active-viewport/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to determine the active viewport name, even in a layout or a detail view."
tags:
  - "clippings"
---
Demonstrates how to determine the active viewport name, even in a layout or a detail view.

```python
import Rhino

import scriptcontext

 

def ActiveViewport():

    view = scriptcontext.doc.Views.ActiveView

    if view is None: return

    if isinstance(view, Rhino.Display.RhinoPageView):

        if view.PageIsActive:

            print "The layout", view.PageName, "is active"

        else:

            detail_name = view.ActiveViewport.Name

            print "The detail", detail_name, "on layout", view.PageName, "is active"

    else:

        print "The viewport", view.MainViewport.Name, "is active"

 

 

if __name__ == "__main__":

    ActiveViewport()
```