---
title: "Replace the Color Picking Dialog"
source: "https://developer.rhino3d.com/samples/rhinocommon/replace-the-color-picking-dialog/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to replace Rhino's color picking dialog."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [replace, rhinos, color, picking, dialog, Picking and Selection]
---
Demonstrates how to replace Rhino's color picking dialog.

```cs
partial class Examples
{
  private static ColorDialog m_dlg = null;

  public static Result ReplaceColorDialog(RhinoDoc doc)
  {
    Dialogs.SetCustomColorDialog(OnSetCustomColorDialog);
    return Result.Success;
  }

  static void OnSetCustomColorDialog(object sender, GetColorEventArgs e)
  {
    m_dlg = new ColorDialog();
    if (m_dlg.ShowDialog(null) == DialogResult.Ok)
    {
      var c = m_dlg.Color;
      e.SelectedColor = System.Drawing.Color.FromArgb (c.Ab, c.Rb, c.Gb, c.Bb);
    }
  }
}
```
