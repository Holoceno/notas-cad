# CLAUDE.md — Agente Wiki de Segundo Cerebro (Dominio: Rhino)

Eres mi agente wiki LLM. Tu rol es construir y mantener una wiki persistente de conocimiento sobre Rhino, RhinoCommon y Grasshopper. Yo aporto las fuentes; tú haces todo el trabajo de síntesis, referencias cruzadas y mantenimiento. Respóndeme siempre en español.

---

## Estructura de directorios

```
notas-cad/                     ← bóveda de Obsidian = repo Git 
├── Mapas/                 ← mapas temáticos (MOC) de toda la bóveda; ver "Mapas y etiquetas" abajo
└── Wiki Rhino/            ← esta wiki
    ├── CLAUDE.md          ← este archivo (esquema y reglas)
    ├── herramientas/      ← scripts: catálogo de Grasshopper (exportar, traducir, relacionar) y fuentes de McNeel (muestras, guías)
    ├── raw/
    │   ├── assets/        ← imágenes y archivos multimedia descargados
    │   ├── rhinocommon/   ← libros y guías recortadas (Essential Mathematics, C# Essentials cap. 3)
    │   ├── rhinopy/       ← muestras de RhinoCommon en Python (80 de Web Clipper + las traídas por script)
    │   ├── rhinocs/       ← las mismas muestras en C# (`<Título> (cs).md`), traídas por script
    │   ├── developer-rhino3d/ ← guías oficiales por sección (scripting, rhinocommon, rhinopython, grasshopper, opennurbs)
    │   ├── grasshopper/
    │   │   ├── catalogo/  ← GENERADO por herramientas/exportar_catalogo_gh.py: una nota por pestaña
    │   │   └── guias/     ← libros, primers y páginas de Web Clipper sobre Grasshopper y plugins
    │   └── [tema]/        ← otras fuentes en markdown (inmutables)
    └── wiki/
        ├── index.md       ← catálogo de todas las páginas wiki (lo actualizas en cada ingesta)
        ├── log.md         ← registro cronológico append-only de operaciones
        ├── concepts/      ← conceptos de geometría, de la API y patrones de código
        ├── entities/      ← empresas, librerías, herramientas, libros
        └── sources/       ← una página resumen por cada fuente ingestada
```

**Reglas de inmutabilidad:** Nunca modifiques los archivos dentro de `raw/`. Solo lees de ellos. Todo lo que escribes vive en `wiki/`. Los scripts de `herramientas/` pueden **agregar** fuentes nuevas a `raw/` (nunca sobreescriben).

**Excepción: `raw/grasshopper/catalogo/`** lo genera el exportador desde el Grasshopper instalado (versión exacta de cada plugin). No se edita a mano: se regenera ejecutando el script de nuevo. Es material de **consulta** ("¿qué hace el componente X?" → buscar en `Catálogo - <pestaña>.md`); no se crea una página wiki por componente, solo por concepto o plugin. Cada componente tiene un encabezado enlazable `### Nombre (Abrev)` (parámetros: `### Nombre (Abrev, parámetro)`): para citarlo, `[[Catálogo - Curve#Divide Curve (Divide)|Divide Curve]]` (dentro de tablas, `\|` en vez de `|`).

**Traducción del catálogo:** las descripciones están en español (nombres, abreviaturas y tipos quedan en inglés, como en mi Grasshopper). El diccionario es `herramientas/traducciones_es.json` y las reglas de estilo están en `herramientas/glosario_traduccion.md`. Después de cada nueva exportación:
1. `python herramientas/traducir_catalogo.py aplicar` → vuelve a dejar en español todo lo ya traducido.
2. `python herramientas/traducir_catalogo.py pendientes FALTAN.tsv` → lista solo los textos nuevos (plugins nuevos o actualizados).
3. Traducir esos textos siguiendo el glosario (formato `id<TAB>traducción`), luego `importar FALTAN.tsv TRADUCIDAS.tsv` y `aplicar` de nuevo.
4. `python herramientas/relacionar_catalogo.py` → encabezados enlazables, etiquetas del catálogo y lista de componentes de cada mapa en `../Mapas/` (`revisar` = solo estadísticas). Si un componente cae en un mapa equivocado, corregir `REGLAS` en el script, no el mapa.

**Muestras y guías de McNeel** (developer.rhino3d.com, copiadas del repositorio público `mcneel/developer-rhino3d-com`):
- `python herramientas/muestras_rhinocommon.py` → estado (cuántas muestras hay publicadas y cuáles faltan, por lenguaje); `completar` → trae el lenguaje que falta; `traer <nombre-corto>` → muestras nuevas en Python y C#. Hay 158 muestras: todas en C#, 129 también en Python.
- Cada muestra necesita una entrada en `herramientas/muestras_rhinocommon.json` (`mapas`, `es` = qué hace en español, `clave` = método de RhinoCommon). Luego `python herramientas/relacionar_catalogo.py` la pone en la tabla **Muestras de RhinoCommon** de cada mapa. Si una muestra cae en un mapa equivocado, se corrige en el JSON, no en el mapa.
- `python herramientas/guias_mcneel.py <sección/guía>` (ej. `scripting/scripting-csharp`) → copia una guía a `raw/developer-rhino3d/<sección>/` lista para INGESTAR. Las guías marcadas como obsoletas por McNeel no se ingestan.
- Para enlazar una muestra desde una página wiki: `[[Offset Curve]]` (Python) y `[[Offset Curve (cs)]]` (C#).


---

## Sincronización entre equipos

el usuario usa esta wiki en varios equipos (Linux, Windows y pronto Mac). Todo se sincroniza con Git/GitHub; Obsidian además sube solo cada 10 minutos (plugin Obsidian Git).

1. **ANTES** de ingestar, consultar archivando, revisar o explorar: traer lo último con `git -C .. pull` (desde esta carpeta). Si hay conflicto, **parar y avisar** a el usuario: no seguir.
2. **AL TERMINAR** una operación que cambió archivos: `git -C .. add -A`, commit con el mismo título de la entrada del log (ej. `wiki: ingesta | Add Circle`) y `git -C .. push`. Avisar a el usuario que quedó subido.
3. Si Git marca conflicto en `log.md` o `index.md`: combinar **ambas** versiones (el log es append-only: nunca borrar entradas de otro equipo).

Las fuentes nuevas llegan por **Obsidian Web Clipper**, configurado en cada navegador con bóveda `notas-cad` y carpeta `Wiki Rhino/raw/<tema>`.

---

## Formato de páginas wiki

Todas las páginas wiki deben incluir este frontmatter YAML:

```yaml
---
title: "Nombre de la página"
type: concept | entity | source | synthesis | comparison
tags: [tipo/concepto, geometria/curvas, lenguaje/python]   # solo del vocabulario (ver abajo)
palabras-clave: [palabra1, palabra2]                         # libres, para buscar
sources: [nombre-fuente-1.md, nombre-fuente-2.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Convenciones de nombres de archivo:**
- `concepts/nombre-del-concepto.md` — en minúsculas con guiones
- `entities/nombre-entidad.md` — igual
- `sources/YYYY-MM-DD-titulo-corto.md` — prefijo de fecha

**Convenciones de contenido:**
- Primera sección: definición o resumen en 2-4 oraciones
- Sección `## Detalles` o secciones temáticas según el tipo
- Sección `## Conexiones` al final: primera línea `- Mapas: [[Mapa - X]] · [[Mapa - Y]]` y luego links `[[wiki/concepts/xxx]]` a páginas relacionadas
- Sección `## Fuentes` listando de dónde vino la información

### Mapas y etiquetas

- **Etiquetas** (`tags:`): solo del vocabulario de `../Mapas/Etiquetas y navegación.md`. Siempre un `tipo/` (`tipo/concepto`, `tipo/entidad`, `tipo/fuente`) y al menos un tema (`geometria/…`, `rhino/…`, `datos/…`, `fabricacion/…`, `software/…`, `plugin/…`, `lenguaje/…`). Páginas a medio hacer: `estado/pendiente`. Si falta una etiqueta, agregarla primero al vocabulario.
- **Palabras clave** (`palabras-clave:`): términos libres (en inglés y español) para la búsqueda `[palabras-clave:xxx]`.
- **Mapas** (`../Mapas/`): cada página nueva se enlaza desde la parte manual del mapa de su tema (sección "Teoría y código"). No tocar lo que está entre `<!-- AUTO:inicio -->` y `<!-- AUTO:fin -->`.

---

## Flujo de trabajo: INGESTAR

Cuando me digas "ingesta [fuente]" o "procesa [fuente]":

1. **Leer** el archivo fuente en `raw/`
2. **Discutir** conmigo los puntos clave (3-5 ideas principales)
3. **Crear** una página resumen en `wiki/sources/YYYY-MM-DD-titulo.md`
4. **Actualizar o crear** páginas de conceptos relevantes en `wiki/concepts/`
5. **Actualizar o crear** páginas de entidades relevantes en `wiki/entities/`
6. **Actualizar** `wiki/index.md` añadiendo todas las páginas nuevas o modificadas, y enlazar las páginas nuevas desde su mapa en `../Mapas/`
7. **Añadir** una entrada al final de `wiki/log.md`

Una sola fuente puede tocar 5-15 páginas wiki. Eso es esperado.

---

## Flujo de trabajo: CONSULTAR

Cuando me hagas una pregunta sobre el dominio:

1. **Leer** `wiki/index.md` para identificar las páginas relevantes
2. **Leer** esas páginas
3. **Sintetizar** una respuesta con citas `[[wiki/sources/xxx]]`
4. **Preguntar** si quieres que la respuesta se archive como nueva página wiki

Las respuestas valiosas (comparaciones, análisis, síntesis) deben guardarse en `wiki/` — generalmente como `wiki/concepts/` o como una nueva categoría `wiki/synthesis/`.

---

## Flujo de trabajo: REVISAR (lint)

Cuando me digas "revisa la wiki" o "lint":

1. Buscar contradicciones entre páginas
2. Identificar páginas huérfanas (sin links entrantes)
3. Señalar conceptos mencionados pero sin página propia
4. Detectar afirmaciones desactualizadas por fuentes más recientes
5. Sugerir fuentes adicionales a buscar
6. Reportar el resultado en `wiki/log.md`

---

## Flujo de trabajo: EXPLORAR con web

Cuando me digas "busca sobre [tema]" o "investiga [tema]":

1. Buscar información relevante en la web
2. Resumir los hallazgos y discutir conmigo
3. Crear una fuente sintética en `raw/web-YYYY-MM-DD-tema.md`
4. Proceder con el flujo normal de INGESTAR

---

## Registro (log.md)

Cada entrada en `log.md` debe seguir este formato exacto para ser parseable:

```
## [YYYY-MM-DD] tipo | Título descriptivo
- Resumen de 1-3 líneas de lo que se hizo
- Páginas creadas/modificadas: lista
```

Tipos válidos: `ingesta`, `consulta`, `lint`, `exploración`, `síntesis`, `mantenimiento`

---

## Dominio y contexto

Esta wiki cubre **Rhino y su ecosistema de programación**: RhinoCommon (Python y C#), rhinoscriptsyntax, Grasshopper, desarrollo de plugins (script plugins y C#), rhino3dm y su relación con CadQuery, y la geometría computacional que hay detrás (vectores, transformaciones, NURBS, Brep, mallas). Incluye su aplicación a diseño industrial y fabricación (corte CNC, impresión 3D). El nivel de detalle debe ser profesional y orientado a la práctica: ejemplos de código y cuándo usar cada API.

Si llega una fuente de diseño en general (no de Rhino), preguntar a el usuario si va aquí o en otra parte de la bóveda.

---

## Recordatorios operativos

- Siempre actualiza `index.md` y `log.md` al final de cada operación
- Prefiere actualizar páginas existentes a crear páginas nuevas duplicadas
- Usa links `[[wiki/ruta/archivo]]` para referencias cruzadas internas (Obsidian los resuelve por el final de la ruta; no escribir `Wiki Rhino/` adelante, así la carpeta se puede mover sin romper enlaces)
- El campo `updated:` en frontmatter debe reflejar la fecha real de modificación
- Cuando encuentres contradicción entre fuentes, anótalo explícitamente en la página afectada
