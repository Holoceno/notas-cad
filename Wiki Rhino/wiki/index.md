---
tags: [tipo/indice]
---

# Índice de la Wiki — Rhino

> Catálogo de todas las páginas. Actualizado automáticamente en cada ingesta.
> Última actualización: 2026-10-13 · Entrada por tema: [[Mapa - Grasshopper]], [[Mapa - Programación]], [[Mapa - Fabricación]] · Cómo se relaciona todo: [[wiki/concepts/ecosistema-programacion-rhino]]

---

## Resumen

| Categoría | Páginas |
|-----------|---------|
| Fuentes | 20 |
| Conceptos | 19 |
| Entidades | 6 |
| Síntesis | 0 |
| **Total** | **45** |

---

## Fuentes (`wiki/sources/`)

### Grasshopper
- [Catálogo de Grasshopper exportado](sources/2026-10-12-catalogo-grasshopper.md) — 2.214 componentes en 23 pestañas (nativo + 13 plugins), descripciones en español, pipeline exportar → traducir → relacionar

### RhinoCommon SDK (Essential Mathematics + geometría C#)
- [Object Selection with Options](sources/2026-05-03-object-selection-with-options.md) — GetObject API pattern: mixed pre/post selection and command-line options
- [Essential Mathematics Ch.1 — Matemáticas Vectoriales](sources/2026-05-03-matematicas-vectoriales.md) — Vectores, producto escalar/vectorial, ecuaciones de línea y plano; tutoriales GH/C#/Python
- [Essential Mathematics Ch.2 — Matrices y Transformaciones](sources/2026-05-03-matrices-y-transformaciones.md) — Matrices 4×4, traslación, rotación, escala, sesgado, reflejo, proyección
- [Essential Mathematics Ch.3 — Curvas y Superficies Paramétricas](sources/2026-05-03-curvas-superficies-parametricas.md) — NURBS completo: grado, CPs, nodos, pesos, continuidad, curvatura, Brep
- [C# Essentials Ch.3 — RhinoCommon Geometry](sources/2026-05-03-rhinocommon-geometry-cap3.md) — Tipos de geometría en C#: estructuras, jerarquía de clases, Mesh, Brep, transformaciones

### Guías oficiales y muestras completas (developer.rhino3d.com, 2026-10-13)
- [Muestras de RhinoCommon en Python y C#](sources/2026-10-13-muestras-rhinocommon-python-csharp.md) — Las 158 muestras oficiales (158 en C#, 129 en Python), cómo leerlas, cuáles sirven para CNC, muebles y planos; repartidas en los mapas
- [Scripting en Rhino 8](sources/2026-10-13-guias-scripting-rhino8.md) — ScriptEditor, Python 3 vs 2, paquetes, componente Script (Script-Mode / SDK-Mode), out/ref y sobrecargas desde Python
- [RhinoCommon, plugins y rhino3dm](sources/2026-10-13-guias-plugins-rhino.md) — Ensamblados y tipos de plugin, primer plugin (Windows/Mac), script plugins (.rhproj → .rhp/.gha/.yak), rhino3dm
- [Data trees](sources/2026-10-13-guias-data-trees.md) — Por qué existen (1:N, consistencia), DataTree/GH_Path y treehelpers en Python

### RhinoCommon Samples Python (rhinopy — las 80 recortadas, por tema)
- [Samples — Curvas (22)](sources/2026-05-04-rhinopy-curvas.md) — Creación, consulta y modificación de curvas: NURBS, Circle, Line, offset, fillet, tween, contorno
- [Samples — Superficies (6)](sources/2026-05-04-rhinopy-superficies.md) — NurbsSurface desde cero, isocurvas, curvatura, borde, extensión, proyección
- [Samples — Mallas (4)](sources/2026-05-04-rhinopy-mallas.md) — Construcción Mesh, Create from Brep, Display Conduit, bordes desnudos
- [Samples — Sólidos y Brep (4)](sources/2026-05-04-rhinopy-solidos-brep.md) — BrepBox, Twisted Cube (manual), Boolean Difference, Brep from BBox
- [Samples — Primitivas Geométricas (8)](sources/2026-05-04-rhinopy-primitivas.md) — Esfera, Cono, Cilindro, Toro, TCone; bloques, grupos, undo
- [Samples — Capas (6)](sources/2026-05-04-rhinopy-capas.md) — Crear, validar, renombrar, buscar, mover objetos a capa, selección por capa
- [Samples — Anotaciones (9)](sources/2026-05-04-rhinopy-anotaciones.md) — Texto, dimensiones lineales/radiales, leader, hatch, estilos
- [Samples — Input y UI (6)](sources/2026-05-04-rhinopy-input-ui.md) — Command-line options, DynamicDraw, filtros geométricos, GetAngle
- [Samples — Vista y Entorno (5)](sources/2026-05-04-rhinopy-vista.md) — Background bitmap, clipping plane, textura, display settings, viewport
- [Samples — Operaciones Espaciales (8)](sources/2026-05-04-rhinopy-operaciones-espaciales.md) — Copias, transformaciones, intersecciones curva/línea/brep, RTree

---

## Conceptos (`wiki/concepts/`)

### Matemáticas y geometría
- [Vector Mathematics](concepts/vector-mathematics.md) — Representación vectorial, operaciones, producto escalar/vectorial, línea y plano
- [Transformaciones Geométricas (Matrices 4×4)](concepts/transformaciones-geometricas.md) — Traslación, rotación, escala, sesgado, reflejo, proyección; coordenadas homogéneas
- [Curvas NURBS](concepts/curvas-nurbs.md) — Grado, puntos de control, pesos, nodos, anclada vs periódica, De Casteljau, De Boor
- [Continuidad Geométrica](concepts/continuidad-geometrica.md) — G0/G1/G2 para curvas y superficies; cómo lograrla en NURBS
- [Curvatura](concepts/curvatura.md) — Curvatura de curvas; curvatura principal, gaussiana y media de superficies
- [Superficies NURBS y Polisuperficies](concepts/superficies-nurbs.md) — Dominio u-v, recortadas, singularidades, Brep como polisuperficie
- [Brep y Polisuperficies — Estructura de Datos](concepts/brep-polisuperficies.md) — Geometría + topología: faces, edges, vertices, trims, loops

### Programar Rhino (relación entre entornos)
- [Ecosistema de programación de Rhino](concepts/ecosistema-programacion-rhino.md) — Grasshopper, scripts, rhinoscriptsyntax, plugins, rhino3dm y CadQuery: la pila, cuándo usar cada uno y la misma tarea en siete lugares
- [Traducir entre Python y C#](concepts/python-csharp-rhinocommon.md) — Tabla de sintaxis, out → tupla, enums NONE, sobrecargas; Offset Curve lado a lado; componentes Script
- [Plugins de Rhino y Grasshopper](concepts/plugins-rhino-grasshopper.md) — Script plugins (sin C#) y plugins en C#; archivos .rhp/.gha/.yak; aplicación a OVERKILL y muebles CNC

### Grasshopper
- [Data trees (árboles de datos)](concepts/data-trees.md) — Rutas, ramas, acceso item/lista/árbol, data matching, Graft/Flatten/Simplify, DataTree en Python y C# (contrastado con las guías oficiales)

### RhinoCommon API
- [Tipos de Geometría en RhinoCommon](concepts/tipos-geometria-rhinocommon.md) — Estructuras livianas vs clases completas; jerarquía GeometryBase; Mesh
- [Interactive Object Selection](concepts/interactive-object-selection.md) — Workflow de selección con command-line options en Rhino
- [RhinoCommon — Document API y scriptcontext](concepts/rhinocommon-document-api.md) — doc.Objects.Add*, doc.Layers, doc.Views, patrón base Python
- [RhinoCommon — API de Capas](concepts/rhinocommon-capas-api.md) — LayerTable, crear/buscar/renombrar capas, mover objetos por capa
- [RhinoCommon — API de Anotaciones](concepts/rhinocommon-anotaciones-api.md) — Texto, dimensiones lineales/radiales, leaders, hatches, estilos
- [RhinoCommon — API de Mallas](concepts/rhinocommon-mesh-api.md) — Construcción Mesh, CreateFromBrep, Display Conduit, GetNakedEdges
- [GetObject: bucle de selección](concepts/getobject-loop-pattern.md) — (pendiente) patrón GetObject con opciones
- [RhinoCommon — API de Intersección](concepts/rhinocommon-interseccion-api.md) — CurveCurve, LineLine, CurveBrep, ProjectPoints, RTree

---

## Entidades (`wiki/entities/`)

- [Grasshopper](entities/grasshopper.md) — Programa, pestañas nativas y los 13 plugins instalados con versiones
- [OpenNest 2](entities/opennest.md) — Nesting sobre planchas para CNC: flujo, opciones, Batch por rama, herramientas de fabricación
- [rhinoscriptsyntax](entities/rhinoscriptsyntax.md) — Funciones simples de Python escritas sobre RhinoCommon; tabla rs ↔ RhinoCommon
- [rhino3dm](entities/rhino3dm.md) — Geometría y archivos .3dm sin Rhino (Python, JS, .NET); puente con CadQuery
- [RhinoCommon](entities/rhinocommon.md) — SDK .NET para Rhino 3D; namespaces con su mapa, ensamblados, tipos de plugin, jerarquía de tipos
- [Essential Mathematics for Computational Design](entities/essential-mathematics-computational-design.md) — Libro de referencia McNeel; fundamentos matemáticos para diseño computacional

---

## Síntesis (`wiki/synthesis/`)

_Sin síntesis archivadas aún._
