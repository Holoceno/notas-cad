---
title: "Add Material"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-material/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a material to the document and apply it to a sphere object."
tags: [tipo/muestra, software/rhinocommon, lenguaje/python]
palabras-clave: [add, basic, material, Adding Objects]
---
Demonstrates how to add a material to the document and apply it to a sphere object.

```python
import Rhino
import scriptcontext
import System.Drawing

def AddMaterial():

    # Create a Rhino material.
    rhino_material = Rhino.DocObjects.Material();
    rhino_material.Name = "Chocolate";
    rhino_material.DiffuseColor = System.Drawing.Color.Chocolate;
    rhino_material.SpecularColor = System.Drawing.Color.CadetBlue;
    
    texture = Rhino.DocObjects.Texture()
    texture.FileName = "my_image.jpg"
    rhino_material.SetTexture(texture, Rhino.DocObjects.TextureType.Bitmap)

    # Use the Rhino material to create a Render material.
    render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, scriptcontext.doc)
    scriptcontext.doc.RenderMaterials.Add(render_material);

    # Create a sphere.
    sphere = Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 5);

    # Add the sphere to the document with a material.
    id = scriptcontext.doc.Objects.AddSphere(sphere);
    obj = scriptcontext.doc.Objects.FindId(id);
    if obj is not None:
      # Assign the render material to the sphere object.
      obj.RenderMaterial = render_material;
      obj.CommitChanges();

    scriptcontext.doc.Views.Redraw();

    return Rhino.Commands.Result.Success;

if __name__=="__main__":
    AddMaterial()
```
