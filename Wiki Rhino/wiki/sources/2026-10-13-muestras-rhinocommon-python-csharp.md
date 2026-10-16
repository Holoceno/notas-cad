---
title: "Muestras de RhinoCommon en Python y C# (colección completa)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, lenguaje/csharp]
palabras-clave: [samples, muestras, ejemplos, rhinocommon, python, csharp, c#, developer.rhino3d.com, rhinopy, rhinocs, ironpython]
sources: [raw/rhinopy/, raw/rhinocs/]
created: 2026-10-13
updated: 2026-10-13
---

Son las **158 muestras oficiales de RhinoCommon** que publica McNeel en developer.rhino3d.com, cada una en los dos lenguajes cuando existe: **158 en C#** (`raw/rhinocs/`) y **129 en Python** (`raw/rhinopy/`). Las otras 29 solo existen en C#. Completan las 80 que el usuario había recortado con Web Clipper, que habían quedado casi todas solo en Python porque Web Clipper guarda nada más la pestaña visible. Cada muestra aparece en el mapa de su tema con una descripción en español y el método de RhinoCommon que conviene mirar. Por eso esta colección es el puente entre los mapas de Grasshopper y el código.

## Detalles

### Cómo leer una muestra

Todas siguen el mismo esqueleto de **comando de Rhino** en tres pasos:

| Paso | C# | Python | En un componente de Grasshopper |
|---|---|---|---|
| 1. Pedir datos | `RhinoGet.GetOneObject(...)`, `GetPoint`, `GetNumber` | lo mismo, o `rs.GetObject(...)` | **desaparece**: son las entradas del componente |
| 2. Calcular | métodos de `Rhino.Geometry` (`curve.Offset(...)`) | **idénticos** | idénticos |
| 3. Agregar al documento | `doc.Objects.AddCurve(c)` + `doc.Views.Redraw()` | `scriptcontext.doc.Objects.AddCurve(c)` | **desaparece**: se asigna a una salida (`a = c`) |

La idea clave para reutilizarlas: **el paso 2 es el mismo en todas partes** (script de Rhino, componente de Grasshopper, plugin). Solo cambia de dónde salen los datos y adónde van. La traducción línea a línea entre los dos lenguajes está en [[wiki/concepts/python-csharp-rhinocommon]].

Envoltorios típicos:

- C#: `partial class Examples { public static Result Nombre(RhinoDoc doc) { ... } }`. El `doc` llega como parámetro.
- Python: `def Nombre(): ...` con `if __name__ == "__main__": Nombre()`. El documento es `scriptcontext.doc`.
- 26 muestras de Python usan `print x` sin paréntesis: son **IronPython 2** (de la época de Rhino 5–7). Corren tal cual en el motor Python 2 de Rhino 8; para Python 3 hay que poner `print(x)` y revisar los cambios de [[wiki/sources/2026-10-13-guias-scripting-rhino8|Python 3 en Rhino]].

### Dónde están

Cada mapa tiene, dentro de su parte automática, una tabla **Muestras de RhinoCommon** con columnas *Código* (enlaces `Py` y `C#`), *Qué hace* y *Mirar en RhinoCommon*. Reparto actual (una muestra puede estar en dos mapas):

| Mapa | Muestras | Mapa | Muestras |
|---|---|---|---|
| [[Mapa - Visualización y anotaciones]] | 45 | [[Mapa - Scripts, interfaz y archivos]] | 19 |
| [[Mapa - Curvas]] | 30 | [[Mapa - CAD 2D y planos]] | 14 |
| [[Mapa - Documento de Rhino]] | 30 | [[Mapa - Mallas y SubD]] | 11 |
| [[Mapa - Superficies y NURBS]] | 20 | [[Mapa - Intersecciones y booleanos]] | 11 |
| [[Mapa - Brep y sólidos]] | 19 | [[Mapa - Transformaciones]] | 7 |
| [[Mapa - Fabricación]] | 7 | [[Mapa - Puntos, vectores y planos]] | 6 |
| [[Mapa - Morph y tween]] | 2 | | |

### Las más útiles para mis proyectos (★ = nuevas)

- **CNC y fabricación**: ★ Unroll Surface, ★ Unroll Surface and Mesh, ★ Split BReps with Planes, ★ Tight Bounding Boxes for Breps, Create Contour Curves y Offset Curve (compensación de herramienta). Ver [[Mapa - Fabricación]].
- **Sólidos para muebles**: ★ Box Shell (vaciado), ★ Extrude Brep Face, ★ Planar Surface, ★ Loft Surfaces, ★ Sweep Surfaces with Sweep1, ★ IsBrepBox Test (¿esta pieza es un tablero?).
- **Datos en las piezas**, la base del plugin de muebles: ★ **User Data** (datos propios que viajan dentro del objeto y se guardan en el .3dm), ★ Find Objects by Name, ★ Object Iterator, ★ Add Objects to Group, ★ Add Nested Block, ★ Instance Definition Tree.
- **Planos**: ★ **Add Layout** (lámina A0 con ventana de detalle a escala), ★ Set RhinoPageView Width and Height, Add Linear Dimension2 (ahora también en Python), ★ Text Justify. Ver [[Mapa - CAD 2D y planos]].
- **Para plugins**: ★ Display Conduit (dibujar sin agregar al documento), Custom Undo, ★ Custom Python (un comando C# que corre Python) y ★ Visual Analysis Modes.

### Solo en C# (29)

El sitio dice "No Python sample available" para: Add Layout · Add Mesh Box · Add Nested Block · Add Twisted Cube · Box Shell · Conduit Draw Shaded Mesh · Create Spiral · Custom Python · Display Conduit · Export Control Points · Extract Render Mesh · Extrude Brep Face · Instance Archive File Status · Intersecting Line and Circle · Line Between Curves · Move Grip Objects · Object Color · Pick Points · Read Dimension Text · Replace the Color Picking Dialog · Set RhinoPageView Width and Height · Show Surface Direction · Single Color Back Faces · Space Morph · Sprite Drawing · Tweak Colors · Tween Curve · User Data · Visual Analysis Modes.

**Buen ejercicio**: traducir a Python 3 las que sirven para los proyectos (Box Shell, Extrude Brep Face, Add Layout, User Data) con la tabla de [[wiki/concepts/python-csharp-rhinocommon]], y guardarlas en `Aprendizaje/`.

### Cómo se mantiene

Desde `Wiki Rhino/`:

1. `python herramientas/muestras_rhinocommon.py`: estado (cuántas hay publicadas, cuáles faltan y en qué lenguaje).
2. `python herramientas/muestras_rhinocommon.py completar` o `... traer nombre-corto`: las trae del repositorio público de la documentación.
3. Agregar la muestra nueva a `herramientas/muestras_rhinocommon.json` (mapas, `es`, `clave`).
4. `python herramientas/relacionar_catalogo.py`: actualiza las tablas de los mapas.

### Limitaciones

- La columna *Qué hace* y la columna *Mirar en RhinoCommon* las escribí yo leyendo el código de cada muestra. Algunas muestras de Python usan `rhinoscriptsyntax` (`rs.AddLoftSrf`): en ese caso se anota también el método de RhinoCommon equivalente (`Brep.CreateFromLoft`), que hay que confirmar en la API.
- Cuatro recortes viejos de `raw/rhinopy/` guardaron el código C# en vez del Python (Add Linear Dimension2, Add Radial Dimension, Add Twisted Cube, Tween Curve), y uno está repetido (Find point on curve at distance 1). Se dejan tal cual (raw/ es inmutable). El Python que faltaba quedó como `… (py).md`, y las páginas fuente antiguas enlazan todas las versiones.

## Conexiones

- Mapas: [[Mapa - Programación]] · [[Mapa - Grasshopper]] y los mapas de la tabla de arriba
- [[wiki/concepts/python-csharp-rhinocommon]]: cómo pasar de un lenguaje al otro
- [[wiki/concepts/ecosistema-programacion-rhino]]: dónde se usa cada muestra (script, Grasshopper, plugin)
- [[wiki/entities/rhinocommon]]: el SDK
- Fichas por tema de las 80 originales: [[wiki/sources/2026-05-04-rhinopy-curvas]] · [[wiki/sources/2026-05-04-rhinopy-superficies]] · [[wiki/sources/2026-05-04-rhinopy-primitivas]] · [[wiki/sources/2026-05-04-rhinopy-solidos-brep]] · [[wiki/sources/2026-05-04-rhinopy-mallas]] · [[wiki/sources/2026-05-04-rhinopy-operaciones-espaciales]] · [[wiki/sources/2026-05-04-rhinopy-capas]] · [[wiki/sources/2026-05-04-rhinopy-anotaciones]] · [[wiki/sources/2026-05-04-rhinopy-vista]] · [[wiki/sources/2026-05-04-rhinopy-input-ui]]

## Fuentes

- `raw/rhinopy/` y `raw/rhinocs/`: copiadas del repositorio público de la documentación de McNeel (github.com/mcneel/developer-rhino3d-com, carpeta `content/en/samples/rhinocommon/`), que es lo mismo que publica https://developer.rhino3d.com/samples/.
