---
title: "Reverse Curve"
source: "https://developer.rhino3d.com/samples/rhinocommon/reverse-curve/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to reverse the direction of user-specified curves."
tags:
  - "clippings"
---
Demonstrates how to reverse the direction of user-specified curves.

```python
import rhinoscriptsyntax as rs

from scriptcontext import *

import Rhino

 

def ReverseCurves():

    crvs = rs.GetObjects("Select curves to reverse", rs.filter.curve)

    if not crvs: return

 

    for crvid in crvs:

        crv = rs.coercecurve(crvid)

        if not crv: continue

        dup = crv.DuplicateCurve()

        if dup:

            dup.Reverse()

        doc.Objects.Replace(crvid, dup)

 

if __name__ == "__main__":

    ReverseCurves()
```