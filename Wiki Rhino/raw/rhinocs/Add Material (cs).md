---
title: "Add Material"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-material/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a material to the document and apply it to a sphere object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, basic, material, Adding Objects]
---
Demonstrates how to add a material to the document and apply it to a sphere object.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddMaterial(Rhino.RhinoDoc doc)
  {
    // Create a Rhino material with a texture.
    var rhino_material = new Material
    {
      Name = "Chocolate",
      DiffuseColor = System.Drawing.Color.Chocolate,
      SpecularColor = System.Drawing.Color.CadetBlue
    };

    var texture = new Texture
    {
      FileName = "my_image.jpg"
    };
    rhino_material.SetTexture(texture, TextureType.Bitmap);

    // Use the Rhino material to create a Render material.
    var render_material = RenderMaterial.CreateBasicMaterial(rhino_material, doc);
    doc.RenderMaterials.Add(render_material);

    // Create a sphere.
    var sphere = new Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5);

    // Add the sphere to the document.
    var id = doc.Objects.AddSphere(sphere);
    var obj = doc.Objects.FindId(id);
    if (obj != null)
    {
      // Assign the render material to the sphere object.
      obj.RenderMaterial = render_material;
      obj.CommitChanges();
    }

    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```
