---
title: "Determine Language Setting"
source: "https://developer.rhino3d.com/samples/rhinocommon/determine-language-setting/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to determine Rhino's language setting."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [determine, rhinos, language, setting, Other]
---
Demonstrates how to determine Rhino's language setting.

```cs
partial class Examples
{
  public static Result DetermineCurrentLanguage(RhinoDoc doc)
  {
    var language_id = Rhino.ApplicationSettings.AppearanceSettings.LanguageIdentifier;
    var culture = new System.Globalization.CultureInfo(language_id);
    RhinoApp.WriteLine("The current language is {0}", culture.EnglishName);
    return Result.Success;
  }
}
```
