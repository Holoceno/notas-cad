---
tags: [tipo/guia, software/obsidian]
---

# Etiquetas y navegación

↑ [[Inicio]] · [[Mapa - Grasshopper]]

La bóveda se navega de tres maneras que se complementan:

1. **Mapas (MOC)**: notas índice por tema en `Mapas/`. Son la puerta de entrada: [[Mapa - Grasshopper]], [[Mapa - Programación]], [[Mapa - Fabricación]], [[Mapa - CAD 2D y planos]] y [[Mapa - Entorno y herramientas]].
2. **Enlaces** `[[ ]]`: conectan una idea con otra. Son lo que dibuja el grafo.
3. **Etiquetas** `#tema/subtema`: agrupan notas del mismo tipo o tema aunque no estén enlazadas. Van en el frontmatter (`tags:`), no en el texto.

## Vocabulario de etiquetas

Usar **solo estas** (si falta una, agregarla aquí primero). Las palabras sueltas para buscar van en `palabras-clave:`, no en `tags:`.

| Familia | Etiquetas | Ejemplo |
|---|---|---|
| `tipo/` | concepto, entidad, fuente, catalogo, muestra, documentacion, mapa, indice, guia, apunte, proyecto, diario, recomendacion, idea, plantilla | `tipo/concepto` |
| `software/` | rhino, grasshopper, rhinocommon, rhinoscriptsyntax, rhino3dm, cadquery, cadcraft, obsidian, git, uv, cursor, orcaslicer | `software/cadquery` |
| `plugin/` | opennest, kangaroo, pufferfish, weaverbird, lunchbox, lunchboxml, elefront, human, human-ui, parakeet, ngon, biber, anemone | `plugin/opennest` |
| `lenguaje/` | python, csharp | `lenguaje/python` |
| `geometria/` | curvas, superficies, nurbs, brep, mallas, subd, puntos-vectores, transformaciones, morph, intersecciones, patrones, continuidad, curvatura | `geometria/mallas` |
| `matematicas/` | vectores, matrices, numeros | `matematicas/vectores` |
| `datos/` | arboles, listas, texto | `datos/arboles` |
| `rhino/` | documento, capas, anotaciones, seleccion, vista | `rhino/capas` |
| `programacion/` | algoritmos, scripts, interfaz, archivos, pruebas, plugins, entorno, sincronizacion | `programacion/algoritmos` |
| `fabricacion/` | cnc, nesting, uniones, cam, impresion-3d, planos | `fabricacion/cnc` |
| `simulacion/` | fisica, optimizacion, ml | `simulacion/fisica` |
| `estado/` | pendiente, borrador | `estado/pendiente` |

Una etiqueta padre incluye a sus hijas: buscar `tag:#fabricacion` encuentra también `#fabricacion/cnc` y `#fabricacion/nesting`.

`tipo/muestra` = ejemplo de código oficial (`raw/rhinopy/`, `raw/rhinocs/`); `tipo/documentacion` = guía oficial copiada a `raw/developer-rhino3d/`. Las muestras recortadas antes con Web Clipper conservan su etiqueta `clippings` (raw/ no se edita).

## Cómo usarlas en Obsidian

- **Panel de etiquetas**: barra lateral derecha → ícono `#` (o Ctrl+P → "Tags view: Show tags"). Clic en una etiqueta = búsqueda de esa etiqueta.
- **Búsqueda** (Ctrl+Shift+F), ejemplos:
  - `tag:#fabricacion/cnc`: todo lo de CNC
  - `tag:#geometria/mallas tag:#lenguaje/python`: mallas **y** Python
  - `tag:#tipo/concepto -path:raw`: solo conceptos de la wiki
  - `[palabras-clave:nesting]`: por palabra clave
  - `path:rhinocs Offset`: la versión C# de una muestra · `path:rhinopy Offset`: la versión Python
  - `"Divide Curve"`: un componente por nombre (o por abreviatura: `"(Divide)"`)
- **Grafo** (Ctrl+G) → ⚙️ Filtros:
  - `-path:raw` oculta las fuentes en bruto (muestras de código, guías de McNeel y el catálogo) y deja ver la estructura.
  - `tag:#tipo/mapa OR tag:#tipo/concepto OR tag:#tipo/entidad` muestra el esqueleto de la wiki.
  - Los colores ya están configurados por tipo: **naranja** = mapas, **azul** = conceptos, **verde** = entidades, **morado** = fuentes, **gris** = catálogo, **turquesa** = muestras de código (Python y C#), **rosado** = guías oficiales de McNeel, **amarillo** = mis notas.
- **Grafo local** (Ctrl+P → "Graph view: Open local graph") sobre un mapa muestra solo sus vecinos. Es la mejor forma de explorar un tema.

## Reglas para notas nuevas
1. Toda nota lleva `tags:` con al menos un `tipo/` y un tema.
2. Toda nota nueva se enlaza desde **un mapa** (o desde [[Inicio]]); si no, queda huérfana.
3. Los componentes del catálogo no se etiquetan uno por uno: los mapas los agrupan solos (`Wiki Rhino/herramientas/relacionar_catalogo.py`).
