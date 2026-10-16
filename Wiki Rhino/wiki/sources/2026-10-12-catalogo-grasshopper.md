---
title: "Catálogo de Grasshopper exportado (Rhino 8.35)"
type: source
tags: [tipo/fuente, software/grasshopper, tipo/catalogo]
palabras-clave: [catálogo, componentes, entradas, salidas, plugins, exportador, traducción, mapas]
sources: [raw/grasshopper/catalogo/_Índice del catálogo.md]
created: 2026-10-13
updated: 2026-10-13
---

Ficha de **todos los componentes instalados** en mi Grasshopper, exportada con `herramientas/exportar_catalogo_gh.py` desde Rhino 8.35 (Grasshopper 1.0.0008). Son 2.214 objetos en 23 pestañas, con nombre, abreviatura, descripción y tablas de entradas y salidas (tipo y acceso). Las descripciones están traducidas al español; nombres, abreviaturas y tipos quedan en inglés, igual que en el programa. Se usa para consultar ("¿qué hace X?"); los conceptos se explican en páginas wiki aparte.

## Detalles

### Qué contiene

- Una nota por pestaña: `raw/grasshopper/catalogo/Catálogo - <Pestaña>.md`, ordenada por subcategoría (`##`) y componente (`###`).
- Índice: [[_Índice del catálogo]].
- Cada componente tiene un encabezado enlazable `### Nombre (Abrev)`, por ejemplo [[Catálogo - Curve#Divide Curve (Divide)]]. Los parámetros llevan `(…, parámetro)`.
- Se omitieron 524 objetos obsoletos y 152 ocultos (los que Grasshopper no muestra en la cinta).

### Cómo se mantiene (pipeline)

Desde la carpeta `Wiki Rhino/`, después de instalar o actualizar plugins:

1. **Exportar** en Rhino: componente Python 3 con `herramientas/exportar_catalogo_gh.py` → botón.
2. **Traducir**: `python herramientas/traducir_catalogo.py aplicar` (y `pendientes` para los textos nuevos; ver `CLAUDE.md`).
3. **Relacionar**: `python herramientas/relacionar_catalogo.py` → actualiza los [[Mapa - Grasshopper|mapas temáticos]] y las etiquetas.

### Limitaciones

- Las descripciones son las del autor de cada plugin: algunas son escuetas y otras traen consejos de uso valiosos (OpenNest, por ejemplo).
- La clasificación por mapas es automática (pestaña + subcategoría + tipos de entrada y salida). Puede haber componentes en un mapa discutible: se corrige en `REGLAS` del script.
- No incluye ejemplos ni la teoría: eso va en `wiki/concepts/`.

## Conexiones

- [[wiki/entities/grasshopper]]: plugins, versiones y cómo navegar
- [[wiki/concepts/data-trees]]: concepto base para leer la columna *Acceso*
- [[wiki/entities/opennest]]: primer plugin documentado a fondo desde el catálogo
- [[Mapa - Grasshopper]]: entrada por tema

## Fuentes

- `raw/grasshopper/catalogo/` (generado; ver la excepción de inmutabilidad en `CLAUDE.md`).
