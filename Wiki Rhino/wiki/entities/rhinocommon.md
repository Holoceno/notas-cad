---
title: "RhinoCommon"
type: entity
tags: [tipo/entidad, software/rhinocommon, lenguaje/csharp, lenguaje/python, programacion/plugins]
palabras-clave: [rhino3d, sdk, mcneel, api, .net, nuget, namespaces, plugin, eto]
sources: [raw/rhinocommon/Object Selection with Options.md, raw/rhinocommon/Chapter 3 RhinoCommon Geometry.md, raw/developer-rhino3d/rhinocommon/What is RhinoCommon.md]
created: 2026-05-03
updated: 2026-10-13
---

RhinoCommon es el SDK .NET **multiplataforma** (Windows y Mac) de Rhino, hecho por Robert McNeel & Associates. Lo usan los plugins en C#, los scripts de Python (2 y 3), `rhinoscriptsyntax` y el propio Grasshopper. Expone la geometría de Rhino, el documento y la interacción con el usuario. Es gratuito y se instala como paquete NuGet `RhinoCommon`. Cómo se relaciona con todo lo demás: [[wiki/concepts/ecosistema-programacion-rhino]].

**API Reference:** https://developer.rhino3d.com/api/RhinoCommon/
**Developer Docs:** https://developer.rhino3d.com/

## Namespaces principales y su mapa

Cada namespace corresponde a uno o más mapas temáticos. Ahí están los componentes de Grasshopper equivalentes y las muestras de código en Python y C#.

| Namespace | Contenido | Mapa |
|-----------|-----------|------|
| `Rhino.Geometry` | Tipos y operaciones: `Point3d`, `Curve`, `NurbsSurface`, `Brep`, `Mesh`, `Transform`... | [[Mapa - Curvas]] · [[Mapa - Superficies y NURBS]] · [[Mapa - Brep y sólidos]] · [[Mapa - Mallas y SubD]] · [[Mapa - Puntos, vectores y planos]] · [[Mapa - Transformaciones]] |
| `Rhino.Geometry.Intersect` | `Intersection.CurveCurve`, `CurveBrep`, `ProjectPointsToBreps` | [[Mapa - Intersecciones y booleanos]] |
| `Rhino.Geometry.Morphs` | `TwistSpaceMorph`, `BendSpaceMorph`, `FlowSpaceMorph` | [[Mapa - Morph y tween]] |
| `Rhino.DocObjects` | Objetos del documento: `RhinoObject`, `ObjRef`, `ObjectAttributes`, `Layer`, `InstanceDefinition` | [[Mapa - Documento de Rhino]] |
| `Rhino.Input`, `Rhino.Input.Custom` | Pedir datos: `RhinoGet`, `GetObject`, `GetPoint`, `OptionInteger` | [[Mapa - Scripts, interfaz y archivos]] |
| `Rhino.Display` | Dibujo en pantalla: `DisplayConduit`, `DisplayPipeline`, modos de visualización | [[Mapa - Visualización y anotaciones]] |
| `Rhino.Commands`, `Rhino.PlugIns` | Plugins: `Command`, `Result`, `RunMode`, `PlugIn` | [[wiki/concepts/plugins-rhino-grasshopper]] |
| `Rhino.FileIO`, `Rhino.UI` | Archivos (`File3dm`, `TextLog`) y diálogos | [[Mapa - Scripts, interfaz y archivos]] |

## Ensamblados y tipos de plugin

- `RhinoCommon.dll` (el núcleo), `Eto.dll` (interfaz que funciona igual en Windows y Mac) y `Rhino.UI.dll` (interfaz propia de Rhino).
- Cinco tipos de plugin: utilidad general (comandos), importar, exportar, render y digitalizador 3D. Todos pueden tener comandos. Ver [[wiki/concepts/plugins-rhino-grasshopper]].

## Tipos de geometría

### Estructuras (value types — livianas)
`Point3d`, `Vector3d`, `Line`, `Arc`, `Circle`, `Plane`, `Sphere`, `Cylinder`, `Transform` (4×4), etc.

### Jerarquía de clases (reference types)
```
GeometryBase → Curve → NurbsCurve / ArcCurve / LineCurve
             → Surface → NurbsSurface / PlaneSurface / RevSurface
             → Mesh
             → Brep
```

## Relación con Essential Mathematics

| Concepto matemático | Implementación en SDK |
|---------------------|----------------------|
| Vector 3D | `Vector3d` — operaciones `+`, `-`, `*` (dot), `CrossProduct` |
| Matriz 4×4 | `Transform` — métodos `Translation`, `Rotation`, `Scale`, `Shear` |
| Curva NURBS | `NurbsCurve` — acceso a `Points`, `Knots`, `Degree` |
| Superficie NURBS | `NurbsSurface` — mismos atributos en u y v |
| Polisuperficie / Brep | `Brep` — `Faces`, `Edges`, `Vertices`, `Trims`, `Loops` |

## Cómo aprenderlo

1. Leer una muestra en los dos lenguajes: cada mapa tiene la tabla **Muestras de RhinoCommon** ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp]]).
2. Traducir entre lenguajes con [[wiki/concepts/python-csharp-rhinocommon]].
3. Probar en el `ScriptEditor` de Rhino 8 o en un componente Script de Grasshopper ([[wiki/sources/2026-10-13-guias-scripting-rhino8]]).

## Conexiones

- Mapas: [[Mapa - Programación]]
- [[wiki/concepts/ecosistema-programacion-rhino]]: Grasshopper, Python, C#, plugins y CadQuery
- [[wiki/concepts/python-csharp-rhinocommon]] · [[wiki/concepts/plugins-rhino-grasshopper]]
- [[wiki/concepts/interactive-object-selection]] — patrón de selección con GetObject
- [[wiki/concepts/getobject-loop-pattern]] — loop for(;;) con GetResult (ver vault C)
- [[wiki/concepts/tipos-geometria-rhinocommon]] — jerarquía completa de tipos
- [[wiki/concepts/brep-polisuperficies]] — data structure del Brep
- [[wiki/entities/rhinoscriptsyntax]] — funciones simples escritas sobre RhinoCommon
- [[wiki/entities/rhino3dm]] — la geometría de Rhino fuera de Rhino
- [[wiki/entities/essential-mathematics-computational-design]] — fundamentos matemáticos
- [[wiki/sources/2026-05-03-object-selection-with-options]] — selección interactiva
- [[wiki/sources/2026-05-03-rhinocommon-geometry-cap3]] — tipos de geometría C#

## Fuentes

- [[What is RhinoCommon]] (ensamblados, tipos de plugin, NuGet) · [[wiki/sources/2026-10-13-guias-plugins-rhino]].
- [[wiki/sources/2026-05-03-rhinocommon-geometry-cap3]] · [[wiki/sources/2026-05-03-object-selection-with-options]].
- La columna *Mapa* de la tabla de namespaces la armé yo para relacionar la API con los mapas.
