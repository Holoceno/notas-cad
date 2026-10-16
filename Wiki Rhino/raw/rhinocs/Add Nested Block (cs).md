---
title: "Add Nested Block"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-nested-block/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a nested block to an instance definition."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, nested, block, Adding Objects, Blocks]
---
Demonstrates how to add a nested block to an instance definition.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddNestedBlock(RhinoDoc doc)
  {
    var circle = new Circle(Point3d.Origin, 5);
    Curve[] curveList = { new ArcCurve(circle) };
    var circleIndex = doc.InstanceDefinitions.Add("Circle", "Circle with radius of 5", Point3d.Origin, curveList);
    var transform = Transform.Identity;
    var irefId = doc.InstanceDefinitions[circleIndex].Id;
    var iref = new InstanceReferenceGeometry(irefId, transform);
    circle.Radius = circle.Radius * 2.0;
    GeometryBase[] blockList = { iref, new ArcCurve(circle) };
    var circle2Index = doc.InstanceDefinitions.Add("TwoCircles", "Nested block test", Point3d.Origin, blockList);
    doc.Objects.AddInstanceObject(circle2Index, transform);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
