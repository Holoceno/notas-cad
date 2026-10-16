---
title: "RhinoCommon — API de Capas"
type: concept
tags: [tipo/concepto, software/rhinocommon, lenguaje/python, rhino/capas, rhino/documento]
palabras-clave: [rhinopython, capas, layers, layertable, documento]
sources: [raw/rhinopy/Add Layer.md, raw/rhinopy/Add Child Layer.md, raw/rhinopy/Determine Object Layer.md, raw/rhinopy/Move Objects to Current Layer.md, raw/rhinopy/Rename Layer.md, raw/rhinopy/Select Objects on Layer.md]
created: 2026-05-04
updated: 2026-10-13
---

RhinoCommon gestiona capas via `doc.Layers` (tipo `LayerTable`). Cada capa es un `Rhino.DocObjects.Layer` con nombre, GUID e índice propio.

## Crear capas

```python
import Rhino, scriptcontext, System.Drawing.Color

# Nombre sugerido sin colisiones
unused = scriptcontext.doc.Layers.GetUnusedLayerName(False)

# Validaciones previas
if not Rhino.DocObjects.Layer.IsValidName(name): return
if scriptcontext.doc.Layers.Find(name, True) >= 0: return  # ya existe

# Crear con color
idx = scriptcontext.doc.Layers.Add(name, System.Drawing.Color.Red)
```

## Crear capa hija (sub-capa)

```python
parent_idx = doc.Layers.FindByFullPath("Padre", True)
child = Rhino.DocObjects.Layer()
child.ParentLayerId = doc.Layers[parent_idx].Id
child.Name = "Hijo"
child_idx = doc.Layers.Add(child)
```

## Consultar y modificar objetos por capa

```python
# Determinar la capa de un objeto
layer_index = obj.Attributes.LayerIndex
layer_name = doc.Layers[layer_index].Name

# Mover objeto a otra capa
obj.Attributes.LayerIndex = target_index
obj.CommitChanges()

# Seleccionar todos los objetos de una capa
objects = doc.Objects.FindByLayer(doc.Layers[layer_idx])
for obj in objects:
    obj.Select(True)
```

## Renombrar capa

```python
idx = doc.Layers.FindByFullPath("OldName", True)
doc.Layers[idx].Name = "NewName"
doc.Layers[idx].CommitChanges()
```

## Propiedades de Layer

| Propiedad | Descripción |
|-----------|-------------|
| `layer.Name` | nombre corto |
| `layer.FullPath` | ruta completa (incluye padres) |
| `layer.Id` | GUID único de la capa |
| `layer.ParentLayerId` | GUID del padre (`Guid.Empty` si es raíz) |
| `layer.Color` | `System.Drawing.Color` |
| `layer.IsVisible` | visible/oculta |
| `layer.IsLocked` | bloqueada |

## Métodos de LayerTable

| Método | Descripción |
|--------|-------------|
| `doc.Layers.GetUnusedLayerName(persistHint)` | nombre único disponible |
| `doc.Layers.Find(name, ignoreDeleted)` | índice, o -1 si no existe |
| `doc.Layers.FindByFullPath(path, ignoreDeleted)` | busca por ruta completa |
| `doc.Layers.Add(name, color)` | añade y retorna índice |
| `doc.Layers.Add(layer)` | añade objeto Layer preconfigurado |
| `doc.Layers.CurrentLayerIndex` | capa activa actual |

## Conexiones

- Mapas: [[Mapa - Documento de Rhino]] · [[Mapa - Programación]]
- [[wiki/sources/2026-05-04-rhinopy-capas]] — todos los samples de capas
- [[wiki/concepts/rhinocommon-document-api]] — doc y scriptcontext
- [[wiki/entities/rhinocommon]] — SDK fuente
