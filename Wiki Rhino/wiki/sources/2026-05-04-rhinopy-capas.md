---
title: "RhinoCommon Samples — Capas (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, rhino/capas]
palabras-clave: [rhinopython, capas, layers, documento]
sources: [raw/rhinopy/Add Layer.md, raw/rhinopy/Add Child Layer.md, raw/rhinopy/Determine Object Layer.md, raw/rhinopy/Move Objects to Current Layer.md, raw/rhinopy/Rename Layer.md, raw/rhinopy/Select Objects on Layer.md]
created: 2026-05-04
updated: 2026-10-13
---

6 samples de RhinoCommon para gestión completa de capas en el documento.

## Add Layer — con validación

```python
import Rhino, scriptcontext, System.Drawing.Color

# Sugerir nombre sin usar
unused_name = scriptcontext.doc.Layers.GetUnusedLayerName(False)

# Validar nombre
if not Rhino.DocObjects.Layer.IsValidName(layer_name): return Cancel

# Verificar que no exista
if scriptcontext.doc.Layers.Find(layer_name, True) >= 0: return Cancel

# Crear
idx = scriptcontext.doc.Layers.Add(layer_name, System.Drawing.Color.Black)
```

## Add Child Layer

```python
parent_idx = doc.Layers.FindByFullPath("Parent", True)
child = Rhino.DocObjects.Layer()
child.ParentLayerId = doc.Layers[parent_idx].Id
child.Name = "Child"
doc.Layers.Add(child)
```

## Determine Object Layer

```python
obj_ref = GetOneObject("Select object")
layer_index = obj_ref.Object().Attributes.LayerIndex
layer_name = doc.Layers[layer_index].Name
```

## Move Objects to Current Layer

```python
settings = Rhino.DocObjects.ObjectEnumeratorSettings()
current_index = doc.Layers.CurrentLayerIndex
for obj in doc.Objects.GetObjectList(settings):
    obj.Attributes.LayerIndex = current_index
    obj.CommitChanges()
```

## Rename Layer

```python
idx = doc.Layers.FindByFullPath(old_name, True)
doc.Layers[idx].Name = new_name
doc.Layers[idx].CommitChanges()
```

## Select Objects on Layer

```python
layer_idx = doc.Layers.FindByFullPath(layer_name, True)
objects = doc.Objects.FindByLayer(doc.Layers[layer_idx])
for obj in objects:
    obj.Select(True)
```

## Conexiones

- Mapas: [[Mapa - Documento de Rhino]] · [[Mapa - Programación]]
- [[wiki/concepts/rhinocommon-capas-api]] — API de capas detallada
- [[wiki/concepts/rhinocommon-document-api]] — doc y scriptcontext
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Layer: [[Add Layer|Python]] · [[Add Layer (cs)|C#]]
- Add Child Layer: [[Add Child Layer|Python]] · [[Add Child Layer (cs)|C#]]
- Determine Object Layer: [[Determine Object Layer|Python]] · [[Determine Object Layer (cs)|C#]]
- Move Objects to Current Layer: [[Move Objects to Current Layer|Python]] · [[Move Objects to Current Layer (cs)|C#]]
- Rename Layer: [[Rename Layer|Python]] · [[Rename Layer (cs)|C#]]
- Select Objects on Layer: [[Select Objects on Layer|Python]] · [[Select Objects on Layer (cs)|C#]]
