---
title: "Object Selection with Options"
source: "https://developer.rhino3d.com/guides/rhinocommon/object-selection-options/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-03
description: "Rhinoceros 3D: This guide covers how to pick some objects, select command options, return to picking more objects, all while keeping your current selection set."
tags:
  - "clippings"
---
## GetObject

RhinoCommon’s [GetObject class](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Input_Custom_GetObject.htm) has a few properties and methods that you need to use, including:

- [GetObject.EnableClearObjectsOnEntry](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_Input_Custom_GetObject_EnableClearObjectsOnEntry.htm)
- [GetObject.EnableUnselectObjectsOnExit](https://developer.rhino3d.com/api/RhinoCommon/html/M_Rhino_Input_Custom_GetObject_EnableUnselectObjectsOnExit.htm)
- [GetObject.DeselectAllBeforePostSelect](https://developer.rhino3d.com/api/RhinoCommon/html/P_Rhino_Input_Custom_GetObject_DeselectAllBeforePostSelect.htm)

Also, after clicking a command line option, turn off pre-selection, using `GetObject.EnablePreSelect`. Otherwise, `GetObject.GetMultiple` will return with a `GetResult.Object` return code.

For example:

```cs
using System;

using Rhino;

using Rhino.Commands;

using Rhino.DocObjects;

using Rhino.Input;

using Rhino.Input.Custom;

 

...

 

protected override Result RunCommand(RhinoDoc doc, RunMode mode)

{

  const ObjectType geometryFilter = ObjectType.Surface | ObjectType.PolysrfFilter | ObjectType.Mesh;

  int integer1 = 300;

  int integer2 = 300;

 

  OptionInteger optionInteger1 = new OptionInteger(integer1, 200, 900);

  OptionInteger optionInteger2 = new OptionInteger(integer2, 200, 900);

 

  GetObject go = new GetObject();

  go.SetCommandPrompt("Select surfaces, polysurfaces, or meshes");

  go.GeometryFilter = geometryFilter;

  go.AddOptionInteger("Option1", ref optionInteger1);

  go.AddOptionInteger("Option2", ref optionInteger2);

  go.GroupSelect = true;

  go.SubObjectSelect = false;

  go.EnableClearObjectsOnEntry(false);

  go.EnableUnselectObjectsOnExit(false);

  go.DeselectAllBeforePostSelect = false;

 

  bool bHavePreselectedObjects = false;

 

  for (;;)

  {

    GetResult res = go.GetMultiple(1, 0);

 

    if (res == GetResult.Option)

    {

      go.EnablePreSelect(false, true);

      continue;

    }

 

    else if (res != GetResult.Object)

      return Result.Cancel;

 

    if (go.ObjectsWerePreselected)

    {

      bHavePreselectedObjects = true;

      go.EnablePreSelect(false, true);

      continue;

    }

 

    break;

  }

 

  if (bHavePreselectedObjects)

  {

    // Normally, pre-selected objects will remain selected, when a

    // command finishes, and post-selected objects will be unselected.

    // This this way of picking, it is possible to have a combination

    // of pre-selected and post-selected. So, to make sure everything

    // "looks the same", lets unselect everything before finishing

    // the command.

    for (int i = 0; i < go.ObjectCount; i++)

    {

      RhinoObject rhinoObject = go.Object(i).Object();

      if (null != rhinoObject)

        rhinoObject.Select(false);

    }

    doc.Views.Redraw();

  }

 

  int objectCount = go.ObjectCount;

  integer1 = optionInteger1.CurrentValue;

  integer2 = optionInteger2.CurrentValue;

 

  RhinoApp.WriteLine(string.Format("Select object count = {0}", objectCount));

  RhinoApp.WriteLine(string.Format("Value of integer1 = {0}", integer1));

  RhinoApp.WriteLine(string.Format("Value of integer2 = {0}", integer2));

 

  return Result.Success;

}
```