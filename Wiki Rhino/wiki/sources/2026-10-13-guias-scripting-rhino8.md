---
title: "Guías oficiales: scripting en Rhino 8 (Python 3, Python 2 y C#)"
type: source
tags: [tipo/fuente, software/rhino, software/grasshopper, software/rhinocommon, programacion/scripts, lenguaje/python, lenguaje/csharp]
palabras-clave: [ScriptEditor, script editor, Python 3, CPython, IronPython, Python.NET, C# script, Script component, SDK-Mode, Script-Mode, RunScript, type hints, marshalling, overloads, out, ref, clr.Reference, paquetes, pip, nuget]
sources: [raw/developer-rhino3d/scripting/Scripting - Python.md, raw/developer-rhino3d/scripting/Scripting - C♯.md, raw/developer-rhino3d/scripting/Grasshopper Scripting - Python.md, raw/developer-rhino3d/scripting/Grasshopper Scripting - C♯.md, raw/developer-rhino3d/rhinopython/Python 3 in Rhino.md, raw/developer-rhino3d/rhinopython/Using RhinoCommon from Python.md, raw/developer-rhino3d/rhinopython/Calling Overloaded Methods from Python.md, raw/developer-rhino3d/rhinopython/Providing Arguments for By-Reference Parameters.md, raw/developer-rhino3d/grasshopper/Chapter 1 - Grasshopper C♯ Component.md]
created: 2026-10-13
updated: 2026-10-13
---

Nueve guías de developer.rhino3d.com sobre cómo se programa **dentro** de Rhino 8: el editor de scripts (`ScriptEditor`), los tres lenguajes que trae (Python 3, Python 2/IronPython y C#), el componente de script de Grasshopper y los detalles de llamar a RhinoCommon desde Python. Son la base de [[wiki/concepts/python-csharp-rhinocommon]] y del primer peldaño de [[wiki/concepts/ecosistema-programacion-rhino]].

## Detalles

### 1. Un editor, tres lenguajes

- `ScriptEditor` es el editor nuevo de Rhino 8. Escribe y corre scripts en **Python 3**, **Python 2** y **C#**, con depurador (puntos de quiebre, variables, pila de llamadas). `EditPythonScript` sigue existiendo pero está obsoleto.
- El **mismo editor** se abre dentro de los componentes de script de Grasshopper, así que también se puede depurar un componente paso a paso.
- Un script se corre desde un botón, un alias o una macro: `_-ScriptEditor _R "ruta/script.py"`.

### 2. Python 3 y Python 2 conviven

| | Python 3 | Python 2 |
|---|---|---|
| Qué es | CPython; llega a RhinoCommon por **Python.NET** | IronPython; corre sobre .NET directamente |
| Ventaja | paquetes de PyPI (`#r: numpy`), sintaxis moderna | llamadas puras a RhinoCommon más rápidas, hilos .NET |
| Versión | Rhino 8 trae Python 3.9.10 | 2.7 |

La guía recomienda Python 3 para casi todo. Tres cambios atrapan a los scripts de Rhino al pasar de Python 2 a 3:

1. Los miembros de enum llamados `None` pasan a `NONE` (`Mesh.MeshType.NONE`).
2. Un método .NET que devuelve `IEnumerable` da un iterador: `list(metodo())` para indexar o medir.
3. Una clase que hereda de un tipo .NET (un `DisplayConduit`, por ejemplo) debe llamar `super().__init__()`.

`rhinocompat` (`PY3`, `RANGE`, `ENUM_NONE`) sirve para escribir scripts que corran en los dos.

### 3. Paquetes y código compartido

Las referencias van en el propio script, así viajan con él:

| Directiva | Qué trae |
|---|---|
| `#r: numpy` o `#r "pip: numpy"` | paquete de PyPI (Python 3) |
| `#r "nuget: RestSharp, 110.2.0"` | paquete NuGet (C# y Python) |
| `#r "yak: LunchBox, 2025.5.5"` | paquete del gestor de Rhino |
| `#r "ruta/archivo.dll"` | ensamblado en disco |
| `#load "helpers.cs"` | otro archivo C# (código compartido) |

En Python, el código compartido va en módulos dentro de las **rutas de búsqueda** del editor (Options › Module Search Paths o archivos `.pth`).

### 4. El componente de script en Grasshopper

- **Entradas**: tienen *Type Hint* (convierte el dato al tipo pedido) y *Access* **Item / List / Tree** (ver [[wiki/concepts/data-trees]]). Desde Rhino 8.14 se pueden marcar como *Required*.
- **Salidas**: en C# siempre son `object`; el Type Hint solo convierte. `out` recoge lo que se imprime.
- **Dos modos de escribir** (C# y Python):
  - **Script-Mode**: código suelto; las entradas ya existen como variables y basta asignar las salidas (`a = x + y`).
  - **SDK-Mode**: una clase `Script_Instance` (hereda de `GH_ScriptInstance`) con `RunScript(...)`, más `BeforeRunScript` / `AfterRunScript` (una vez por solución) y `DrawViewportWires` / `DrawViewportMeshes` (vista previa propia). Es casi lo mismo que un componente de plugin, de ahí el nombre.
- En C#, `RunScript` recibe las salidas como `ref object a`. Un tipo por valor (`double`, `Point3d`) sin conectar vale su **valor por defecto** (0), no `null`.
- **Python 3 y la conversión de datos (*marshalling*)**: en Script-Mode, una `List<int>` de .NET llega como `list` de Python y la salida `list` se devuelve como `List<object>`. Se puede desactivar entre componentes Python 3 para ganar velocidad. Con `rhinoscriptsyntax`, las salidas convierten los Guid en geometría, y las entradas con hint *ghdoc Object* hacen lo inverso.
- Un componente se puede **publicar** dentro de un plugin: la descripción (*Tooltip*) y los nombres de las entradas pasan al componente publicado (ver [[wiki/concepts/plugins-rhino-grasshopper]]).

### 5. RhinoCommon desde Python: tres trampas

- `rhinoscriptsyntax` **son scripts de Python que usan RhinoCommon**. Todo lo que hace `rs.` también se puede hacer directo con RhinoCommon, y más.
- **Parámetros `out`/`ref`** (C#): en Python **no se pasan**; el método devuelve una **tupla** con el resultado y los valores de salida (`ok, t = crv.ClosestPoint(pt)`). Alternativa: `clr.Reference[tipo]()`.
- **Sobrecargas**: si Python no sabe cuál versión del método usar ("Multiple targets could match"), se elige a mano: `brep.Split.Overloads[IEnumerable[Brep], System.Double](cortadores, tol)`.

*(Las dos últimas guías están escritas para IronPython; en Python 3 la regla de la tupla se mantiene, pero `clr.Reference` y `.Overloads` son propias de IronPython. Pendiente confirmar en Rhino 8 con Python 3.)*

## Conexiones

- Mapas: [[Mapa - Programación]] · [[Mapa - Scripts, interfaz y archivos]]
- [[wiki/concepts/python-csharp-rhinocommon]]: la traducción entre lenguajes, con ejemplos
- [[wiki/concepts/ecosistema-programacion-rhino]]: dónde encaja cada forma de programar
- [[wiki/concepts/plugins-rhino-grasshopper]]: de script a plugin
- [[wiki/concepts/data-trees]]: acceso Item / List / Tree
- [[wiki/entities/rhinoscriptsyntax]] · [[wiki/entities/rhinocommon]] · [[wiki/entities/grasshopper]]

## Fuentes

- [[Scripting - Python]] · [[Scripting - C♯]]
- [[Grasshopper Scripting - Python]] · [[Grasshopper Scripting - C♯]]
- [[Python 3 in Rhino]] · [[Using RhinoCommon from Python]]
- [[Calling Overloaded Methods from Python]] · [[Providing Arguments for By-Reference Parameters]]
- [[Chapter 1 - Grasshopper C♯ Component]] (Essential C# Scripting for Grasshopper, Rajaa Issa: interfaz del componente y acceso a datos; el capítulo 3 ya estaba en [[wiki/sources/2026-05-03-rhinocommon-geometry-cap3]])
- Todas en `raw/developer-rhino3d/`, traídas con `herramientas/guias_mcneel.py` desde el repositorio público de la documentación (2026-10-13).
