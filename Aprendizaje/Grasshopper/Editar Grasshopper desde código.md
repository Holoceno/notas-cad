---
tags: [tipo/apunte, software/grasshopper, software/rhinocommon, lenguaje/python, programacion/scripts, rhino/anotaciones]
palabras-clave: [GH SDK, EmitObject, AddSource, DataMapping, Python 3 Script, SetSource, TypeHints, SetConverterOrGoo, goo, bake, MCP]
---

# Editar Grasshopper desde código

Notas de cómo modifiqué una definición de Grasshopper abierta usando Python dentro de Rhino (MCP de Rhino). Sirve para repetirlo y para entender qué hay "debajo" del canvas.

## Lo básico del SDK
```python
import Grasshopper, System
doc = Grasshopper.Instances.ActiveCanvas.Document
comp = Grasshopper.Instances.ComponentServer.EmitObject(System.Guid(guid_componente))
comp.CreateAttributes(); comp.NickName = "Mi componente"
comp.Attributes.Pivot = System.Drawing.PointF(x, y)
doc.AddObject(comp, False)
comp.Params.Input[0].AddSource(otro.Params.Output[0])   # conectar un cable
doc.NewSolution(False)
```
- **Graft / Flatten** de una entrada: `p.DataMapping = System.Enum.ToObject(GH_DataMapping, 2)` (1 = Flatten, 2 = Graft). `None` es palabra reservada en Python, por eso se usa el número.
- Un **Path Mapper** es un parámetro, no un componente: `AddSource` directo sobre él, y sus reglas son `GH_LexerCombo` (en `Grasshopper.Kernel.Data`).
- Componentes con entradas variables (Merge, Text Entity): `CreateParameter` + `RegisterInputParam` + `VariableParameterMaintenance()`.
- Buscar el GUID de un componente por nombre: `ComponentServer.ObjectProxies`, filtrando los obsoletos.

## Componente Python 3 (Rhino 8) creado por código
- GUID `719467e6-7cf5-4848-99b0-c5dd57e5442c`. Código: `comp.SetSource(texto)`.
- Las entradas se crean a mano y se les pone acceso (`item`, `list`, `tree`) y **sugerencia de tipo**: `p.TypeHints.Select("Curve")`.
- Para recibir el **goo** de Grasshopper sin convertir (textos con estilo, bloques): la sugerencia "No Type Hint" se aplica con el método interno `SetConverterOrGoo` (por reflexión). Igual llega convertido; lo seguro es leer `ghenv.Component.Params.Input[i].VolatileData` dentro del script.

## Hornear sin perder estilo ni bloque
- Un *Text Entity* de Grasshopper con estilo de cota **se ve de altura 1** en la vista previa, pero al hornear toma el estilo (estilo de cota del archivo). Probar horneando uno antes de "arreglar" lo que no está roto.
- Si un script transforma una `InstanceReferenceGeometry` cruda, al hornear crea un bloque `*Grasshopper::Default`. Transformando el **goo** (`goo.DuplicateGeometry().Transform(t)`) se conserva el bloque real (*Flock doble*).

## Rhino y el MCP
- Si Rhino se cae y se reabre desde un **autoguardado**, el documento abierto es el `RhinoAutosave` (carpeta `AutoSave`), no el original: hay que **Guardar como** sobre el archivo real. El puerto del MCP también puede cambiar (10500 → 10501).
- Guardar un `.3dm` grande en una unidad de red puede pasar los 5 minutos del MCP: el pedido "falla" por tiempo, pero Rhino sigue guardando. Revisar la fecha del archivo antes de repetir.
- `Objects.Replace(id, geometría)` conserva el ID: las referencias de Grasshopper siguen funcionando.

## Conexiones
- Mapas: [[Mapa - Programación]] · [[Mapa - Scripts, interfaz y archivos]] · [[Mapa - Visualización y anotaciones]]
- [[wiki/concepts/ecosistema-programacion-rhino]] · [[wiki/concepts/data-trees]]
