---
title: "rhino3dm"
type: entity
tags: [tipo/entidad, software/rhino3dm, lenguaje/python, software/cadquery]
palabras-clave: [rhino3dm, openNURBS, 3dm, File3dm, pip, uv, sin Rhino, Rhino.Compute, javascript, wasm]
sources: [raw/developer-rhino3d/opennurbs/What is Rhino3dm.md]
created: 2026-10-13
updated: 2026-10-13
---

Librería de código abierto de McNeel, basada en **openNURBS**, para crear, leer y escribir geometría y archivos `.3dm` **sin tener Rhino**, desde Python, JavaScript o .NET. Es el puente natural entre el Python "normal" de el usuario (`cad-python` con uv, en Linux) y los archivos de Rhino. No sirve para hacer plugins.

## Detalles

- **Qué trae**: todos los tipos de geometría de Rhino (puntos, nubes de puntos, curvas y superficies NURBS, Brep, mallas, anotaciones, extrusiones, SubD) y lo que no es geometría (capas, atributos de objeto, transformaciones, vistas). Lee y escribe todo eso en `.3dm`.
- **Qué no trae**: los algoritmos de modelado de Rhino (booleanas, offsets, intersecciones). Para eso hay que usar Rhino, o llamar a **Rhino.Compute** como servidor.
- **Tres versiones**: `rhino3dm` en PyPI (Python), `rhino3dm` en npm (JavaScript + WebAssembly, corre en el navegador) y `Rhino3dm` en NuGet (.NET).
- **Instalar en cad-python**: `uv add rhino3dm`. La versión 8.35.0 tiene ruedas para Python 3.9–3.14 en Linux, Windows y Mac. La guía oficial todavía dice 3.7–3.11, pero está desactualizada.

Uso típico (sin probar):

```python
import rhino3dm

modelo = rhino3dm.File3dm()
capa = rhino3dm.Layer()
capa.Name = "CORTE"
indice = modelo.Layers.Add(capa)

atributos = rhino3dm.ObjectAttributes()
atributos.LayerIndex = indice
puntos = [rhino3dm.Point3d(0, 0, 0), rhino3dm.Point3d(100, 0, 0), rhino3dm.Point3d(100, 50, 0), rhino3dm.Point3d(0, 0, 0)]
modelo.Objects.AddPolyline(puntos, atributos)
modelo.Write("contornos.3dm", 8)
```

Sirve, por ejemplo, para que un script de CadQuery entregue contornos de corte en un `.3dm` con las capas que espera la oficina, en vez de un DXF sin capas.

## Conexiones

- Mapas: [[Mapa - Programación]] · [[Mapa - CAD 2D y planos]]
- [[wiki/concepts/ecosistema-programacion-rhino]]: dónde encaja (fuera de Rhino, junto a CadQuery)
- [[wiki/sources/2026-10-13-guias-plugins-rhino]]

## Fuentes

- [[What is Rhino3dm]]; versiones y ruedas en https://pypi.org/project/rhino3dm/ (revisado el 2026-10-13).
- El ejemplo de código es propio a partir de la API de rhino3dm. **No se ha probado**: confirmar los nombres (`Layers.Add`, `AddPolyline`, `Write`) con la documentación de Python del repositorio `mcneel/rhino3dm` antes de usarlo.
