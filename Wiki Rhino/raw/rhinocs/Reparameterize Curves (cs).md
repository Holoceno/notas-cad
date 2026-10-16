---
title: "Reparameterize Curves"
source: "https://developer.rhino3d.com/samples/rhinocommon/reparameterize-curves/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to reparameterize - or change the domain of - user-specified curves."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [reparamemterize, curve, Curves]
---
Demonstrates how to reparameterize - or change the domain of - user-specified curves.

```cs
partial class Examples
{
  public static Result ReparameterizeCurve(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select curve to reparameterize", false, ObjectType.Curve, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var curve = obj_ref.Curve();
    if (curve == null)
      return Result.Failure;

    double domain_start = 0;
    rc = RhinoGet.GetNumber("Domain start", false, ref domain_start);
    if (rc != Result.Success)
      return rc;

    double domain_end = 0;
    rc = RhinoGet.GetNumber("Domain end", false, ref domain_end);
    if (rc != Result.Success)
      return rc;

    if (Math.Abs(curve.Domain.T0 - domain_start) < RhinoMath.ZeroTolerance &&
        Math.Abs(curve.Domain.T1 - domain_end) < RhinoMath.ZeroTolerance)
      return Result.Nothing;

    var curve_copy = curve.DuplicateCurve();
    curve_copy.Domain = new Interval(domain_start, domain_end);
    if (!doc.Objects.Replace(obj_ref, curve_copy))
      return Result.Failure;
    else
    {
      doc.Views.Redraw();
      return Result.Success;
    }
  }
}
```
