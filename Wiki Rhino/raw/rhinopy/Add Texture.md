---
title: "Add Texture"
source: "https://developer.rhino3d.com/samples/rhinocommon/add-texture/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-04
description: "Rhinoceros 3D: Demonstrates how to add a texture to an object from a user-specified bitmap file."
tags:
  - "clippings"
---
Demonstrates how to add a texture to an object from a user-specified bitmap file.

```python
import Rhino

import scriptcontext

import System.Guid

import System.Windows.Forms.DialogResult

import System.IO.File

 

def AddTexture():

    # Select object to add texture to.

    filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter | Rhino.DocObjects.ObjectType.Mesh

    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select object to add texture", False, filter)

    if rc != Rhino.Commands.Result.Success:

        return rc

 

    rhino_object = objref.Object()

    if rhino_object is None:

        return Rhino.Commands.Result.Failure

 

    # Choose a texture file.

    fd = Rhino.UI.OpenFileDialog()

    fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"

    if not fd.ShowDialog():

        return Rhino.Commands.Result.Cancel

 

    # Verify that the file exists.

    bitmap_filename = fd.FileName

    if not System.IO.File.Exists(bitmap_filename):

        return Rhino.Commands.Result.Nothing

 

    # Make sure the object has a render material assigned.

    if rhino_object.RenderMaterial is None:

      

      # Create a Rhino material.

      rhino_material = Rhino.DocObjects.Material()

      rhino_material.DiffuseColor = System.Drawing.Color.White

 

      # Create a basic Render material from the Rhino material.

      render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, scriptcontext.doc);

 

      # Create a Rhino texture for the filename.

      tex = Rhino.DocObjects.Texture()

      tex.FileName = bitmap_filename

 

      # Create a bitmap texture from the Rhino texture.

      sim = Rhino.Render.SimulatedTexture(scriptcontext.doc, tex);

      render_texture = Rhino.Render.RenderTexture.NewBitmapTexture(sim, scriptcontext.doc);

 

      # Set the texture as a child of the material in the bump slot.

      child_slot_name = "bump-texture";

      render_material.SetChild(render_texture, child_slot_name);

      render_material.SetChildSlotOn(child_slot_name, True, Rhino.Render.RenderContent.ChangeContexts.Program);

      render_material.SetChildSlotAmount(child_slot_name, 100.0, Rhino.Render.RenderContent.ChangeContexts.Program);

 

      # Add the basic Render material to the document.

      scriptcontext.doc.RenderMaterials.Add(render_material);

 

      # Assign the render material to the object.

      rhino_object.RenderMaterial = render_material;

 

      # Don't forget to update the object, if necessary.

      rhino_object.CommitChanges();

 

    scriptcontext.doc.Views.Redraw();

 

    return Rhino.Commands.Result.Success;

 

if __name__=="__main__":

    AddTexture()
```