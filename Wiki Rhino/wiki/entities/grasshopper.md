---
title: "Grasshopper"
type: entity
tags: [tipo/entidad, software/grasshopper, software/rhino]
palabras-clave: [grasshopper, programación visual, componentes, plugins, pestañas, food4rhino, package manager, script components]
sources: [raw/grasshopper/catalogo/_Índice del catálogo.md]
created: 2026-10-13
updated: 2026-10-13
---

Grasshopper es el entorno de **programación visual** de Rhino (McNeel): se conectan componentes con cables y cada cable lleva un [[wiki/concepts/data-trees|árbol de datos]]. Viene incluido en Rhino desde la versión 6. Debajo, cada componente llama a [[wiki/entities/rhinocommon|RhinoCommon]], así que lo que se hace con componentes también se puede escribir en Python o C#. La instalación de el usuario (Rhino 8.35, Grasshopper 1.0.0008) tiene **2.214 objetos en 23 pestañas** documentados en el [[wiki/sources/2026-10-12-catalogo-grasshopper|catálogo exportado]].

## Detalles

### Pestañas nativas

Params, Maths, Sets, Vector, Curve, Surface, Mesh, Intersect, Transform, Display y Rhino (la pestaña Rhino, nueva en Rhino 8, lee y escribe el documento: capas, bloques, anotaciones y materiales).

Los componentes de script están en **Maths › Script**: [[Catálogo - Maths#Python 3 Script (Py3)|Python 3 Script]], [[Catálogo - Maths#C♯ Script (C♯)|C# Script]] e [[Catálogo - Maths#IronPython 2 Script (IPy2)|IronPython 2]] (este último para compatibilidad con Rhino 7). Usan el mismo editor que el `ScriptEditor` de Rhino (con depurador) y se pueden escribir en modo simple o en *SDK-Mode*, casi igual que un componente de plugin. Una definición con componentes Script se puede publicar como plugin `.gha` desde el Script Editor. Ver [[wiki/sources/2026-10-13-guias-scripting-rhino8]] y [[wiki/concepts/plugins-rhino-grasshopper]].

### Plugins instalados

| Plugin | Versión | Para qué sirve | Catálogo |
|---|---|---|---|
| Anemone (Mateusz Zwierzycki) | Classic | Bucles con retroalimentación (Loop Start / Loop End) | [[Catálogo - Anemone\|Anemone]] |
| Biber | 1.4.0.3 (+ Endoframe 1.2) | Estructuras de placas planas con uniones de carpintería (finger, dovetail, lap...) y materiales | [[Catálogo - Biber\|Biber]] |
| eleFront | 5.4.1 | Referenciar y hornear con atributos (capas, nombres, user text), bloques y archivos | [[Catálogo - eleFront\|eleFront]] |
| Human | 1.3.1 | Crear y modificar objetos del documento, capas, display e imágenes | [[Catálogo - Human\|Human]] |
| Human UI (Andrew Heumann) | 0.8.10 | Ventanas propias con sliders, botones y gráficos | [[Catálogo - Human UI\|Human UI]] |
| Kangaroo2 (Daniel Piker) | 2.5.3 | Simulación física y form-finding con *goals* | [[Catálogo - Kangaroo2\|Kangaroo2]] |
| LunchBox | 2025.5.5 | Paneles, superficies matemáticas, estructuras, Excel/CSV/JSON | [[Catálogo - LunchBox\|LunchBox]] |
| LunchBoxML | 2024.2.11 | Machine learning (Accord.NET): regresión, clasificación, clustering | [[Catálogo - LunchBoxML\|LunchBoxML]] |
| NGon | 1.0 (RH8) | Mallas con caras poligonales: planarizar, adyacencia, uniones | [[Catálogo - NGon\|NGon]] |
| [[wiki/entities/opennest\|OpenNest 2]] | 2.12 | Nesting de piezas sobre planchas (CNC/láser) | [[Catálogo - Params#OpenNest2\|Params › OpenNest2]] |
| Parakeet (Mottaghi & Khalilbeigi) | 1.2.0 | Patrones y teselados (incluye teselados de Escher y Wang tiles) | [[Catálogo - Parakeet\|Parakeet]] |
| Pufferfish (Michael Pryor) | 3.0 | Tweens, twisted boxes, morph y utilidades de geometría | [[Catálogo - Pufferfish\|Pufferfish]] |
| Weaverbird (Piacentino) | 0.9.0.1 | Subdivisión y transformación de mallas | [[Catálogo - Wb\|Wb]] |
| Galapagos | 1.0 (nativo) | Optimización evolutiva de un valor | [[Catálogo - Params#Galapagos (objeto especial)\|Params › Util]] |

Plugins que se mencionaron pero **no** están en esta exportación: Cocoon, Crystallon. Quedan pendientes si se instalan.

### Cómo navegar

- **Por tema**: [[Mapa - Grasshopper]] → mapas de curvas, mallas, data trees, fabricación, etc. Cada mapa lista sus componentes con un enlace directo a la ficha.
- **Por pestaña**: [[_Índice del catálogo]].
- **Por nombre**: buscar (Ctrl+Shift+F) el nombre o la abreviatura, por ejemplo `Divide Curve` o `(Divide)`.

## Conexiones

- [[wiki/concepts/data-trees]]: cómo viajan los datos entre componentes
- [[wiki/entities/opennest]]: nesting para CNC
- [[wiki/entities/rhinocommon]]: la API que hay debajo de cada componente
- [[wiki/concepts/tipos-geometria-rhinocommon]]: tipos que circulan por los cables
- [[wiki/concepts/ecosistema-programacion-rhino]]: Grasshopper frente a scripts, plugins y CadQuery
- [[Mapa - Grasshopper]]

## Fuentes

- [[wiki/sources/2026-10-12-catalogo-grasshopper|Catálogo exportado]] (versiones, autores y cantidad de componentes).
- La columna "Para qué sirve" es un resumen propio a partir de los componentes de cada pestaña y del conocimiento general de cada plugin.
