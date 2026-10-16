---
title: "Add Texture"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-texture/"
author:
  - "[[Robert McNeel & Associates]]"
created: 2026-10-13
description: "Demonstrates how to add a texture to an object from a user-specified bitmap file."
tags: [tipo/muestra, software/rhinocommon, lenguaje/csharp]
palabras-clave: [add, texture, Adding Objects]
---
Demonstrates how to add a texture to an object from a user-specified bitmap file.

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddTexture(Rhino.RhinoDoc doc)
  {
    // Select object to add texture to.
    const ObjectType filter = Rhino.DocObjects.ObjectType.Surface |
                              Rhino.DocObjects.ObjectType.PolysrfFilter |
                              Rhino.DocObjects.ObjectType.Mesh;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", false, filter, out ObjRef objref);
    if (rc != Rhino.Commands.Result.Success)
    return rc;

    var rhino_object = objref.Object();
    if (rhino_object == null)
      return Rhino.Commands.Result.Failure;

    // Choose a texture file.
    var fd = new Rhino.UI.OpenFileDialog
    {
      Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
    };
    if (!fd.ShowOpenDialog())
      return Rhino.Commands.Result.Cancel;

    // Verify that the file exists.
    string bitmap_filename = fd.FileName;
    if (string.IsNullOrEmpty(bitmap_filename) || !System.IO.File.Exists(bitmap_filename))
      return Rhino.Commands.Result.Nothing;

    // Make sure the object has a render material assigned.
    if (rhino_object.RenderMaterial == null)
    {
      // Create a Rhino material.
      var rhino_material = new Rhino.DocObjects.Material()
      {
        DiffuseColor = System.Drawing.Color.White
      };

      // Create a basic Render material from the Rhino material.
      var render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, doc);

      // Create a Rhino texture for the filename.
      var tex = new Rhino.DocObjects.Texture
      {
        FileName = bitmap_filename
      };

      // Create a bitmap texture from the Rhino texture.
      var sim = new Rhino.Render.SimulatedTexture(doc, tex);
      var render_texture = Rhino.Render.RenderTexture.NewBitmapTexture(sim, doc);

      // Set the texture as a child of the material in the bump slot.
      var child_slot_name = "bump-texture";
      render_material.SetChild(render_texture, child_slot_name);
      render_material.SetChildSlotOn(child_slot_name, true, Rhino.Render.RenderContent.ChangeContexts.Program);
      render_material.SetChildSlotAmount(child_slot_name, 100.0, Rhino.Render.RenderContent.ChangeContexts.Program);

      // Add the basic Render material to the document.
      doc.RenderMaterials.Add(render_material);

      // Assign the render material to the object.
      rhino_object.RenderMaterial = render_material;

      // Don't forget to update the object, if necessary.
      rhino_object.CommitChanges();
    }

    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```
