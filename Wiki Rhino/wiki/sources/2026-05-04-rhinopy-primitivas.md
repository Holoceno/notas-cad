---
title: "RhinoCommon Samples — Primitivas Geométricas (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, geometria/brep, rhino/documento]
palabras-clave: [rhinopython, primitivas, esfera, cono, cilindro, toro, bloques]
sources: [raw/rhinopy/Add Sphere.md, raw/rhinopy/Add Cone.md, raw/rhinopy/Add Cylinder.md, raw/rhinopy/Add Torus.md, raw/rhinopy/Add Truncated Cone.md, raw/rhinopy/Create Block Definition.md, raw/rhinopy/Custom Undo.md, raw/rhinopy/Select Objects in Object Groups.md]
created: 2026-05-04
updated: 2026-10-13
---

Samples de RhinoCommon sobre primitivas sólidas y gestión de objetos del documento.

## Primitivas — patrón estructura → Brep/Surface → doc

Las primitivas en RhinoCommon son **estructuras** (value types). Para añadirlas al documento se convierten a `Brep` o `Surface`:

| Sample | Estructura | Conversión | Adición |
|--------|-----------|-----------|---------|
| Add Sphere | `Sphere(center, radius)` | — | `doc.Objects.AddSphere(sphere)` |
| Add Cone | `Cone(plane, height, radius)` | `.ToBrep(cap)` | `doc.Objects.AddBrep(b)` |
| Add Cylinder | `Circle(center, r)` → `Cylinder(c, h)` | `.ToBrep(cap, cap)` | `doc.Objects.AddBrep(b)` |
| Add Torus | `Torus(plane, majorR, minorR)` | `.ToRevSurface()` | `doc.Objects.AddSurface(srf)` |
| Add Truncated Cone | `Circle` × 2 → `RevSurface.Create(lineCurve, axis)` | `.CreateFromRevSurface(srf)` | `doc.Objects.AddBrep(b)` |

`Sphere` es la excepción: tiene su propio método `AddSphere`. El resto se convierte primero.

## Bloques (Block Definitions)

```python
obj_refs = GetObjects("Select objects for block")
base_point = GetPoint("Base point")
block_name = GetString("Block name")

# Verificar si ya existe
if doc.InstanceDefinitions.Find(block_name) is not None:
    return Cancel

index = doc.InstanceDefinitions.Add(block_name, description, base_point, obj_refs)
```

## Custom Undo

```python
doc.AddCustomUndoEvent("EventName", undo_handler, state)
# El handler recibe el estado al ejecutar Deshacer/Rehacer
```

## Selección por grupo

```python
obj = GetOneObject("Select object in group")
groups = obj.Attributes.GetGroupList()  # índices de grupos
for gi in groups:
    # iterar objetos del documento y filtrar por grupo
    settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    for member in doc.Objects.GetObjectList(settings):
        if gi in member.Attributes.GetGroupList():
            member.Select(True)
```

## Conexiones

- Mapas: [[Mapa - Brep y sólidos]] · [[Mapa - Documento de Rhino]] · [[Mapa - Programación]]
- [[wiki/concepts/rhinocommon-document-api]] — patrón doc.Objects.Add*
- [[wiki/concepts/tipos-geometria-rhinocommon]] — estructuras livianas vs clases
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Sphere: [[Add Sphere|Python]] · [[Add Sphere (cs)|C#]]
- Add Cone: [[Add Cone|Python]] · [[Add Cone (cs)|C#]]
- Add Cylinder: [[Add Cylinder|Python]] · [[Add Cylinder (cs)|C#]]
- Add Torus: [[Add Torus|Python]] · [[Add Torus (cs)|C#]]
- Add Truncated Cone: [[Add Truncated Cone|Python]] · [[Add Truncated Cone (cs)|C#]]
- Create Block Definition: [[Create Block Definition|Python]] · [[Create Block Definition (cs)|C#]]
- Custom Undo: [[Custom Undo|Python]] · [[Custom Undo (cs)|C#]]
- Select Objects in Object Groups: [[Select Objects in Object Groups|Python]] · [[Select Objects in Object Groups (cs)|C#]]
