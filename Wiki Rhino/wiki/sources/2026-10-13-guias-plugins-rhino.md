---
title: "Guías oficiales: RhinoCommon, plugins y rhino3dm"
type: source
tags: [tipo/fuente, software/rhinocommon, software/grasshopper, software/rhino3dm, programacion/plugins, lenguaje/csharp]
palabras-clave: [plugin, rhp, gha, yak, rhproj, script plugin, Visual Studio, VS Code, dotnet, Rhino.Templates, Eto, NuGet, rhino3dm, openNURBS, Grasshopper.dll, GH_IO]
sources: [raw/developer-rhino3d/rhinocommon/What is RhinoCommon.md, raw/developer-rhino3d/rhinocommon/Your First Plugin (Windows).md, raw/developer-rhino3d/rhinocommon/Your First Plugin (Mac).md, raw/developer-rhino3d/grasshopper/What is a Grasshopper Component.md, raw/developer-rhino3d/scripting/Creating Rhino-Grasshopper Script Plugins.md, raw/developer-rhino3d/scripting/Publishing Rhino-Grasshopper Script Plugins.md, raw/developer-rhino3d/opennurbs/What is Rhino3dm.md]
created: 2026-10-13
updated: 2026-10-13
---

Siete guías de developer.rhino3d.com sobre cómo **empaquetar** código para Rhino: qué es RhinoCommon por dentro, cómo nace un plugin en C# (Windows y Mac), qué es un componente de Grasshopper para .NET, cómo el Script Editor convierte scripts en plugins sin escribir C#, y rhino3dm, la librería para leer y escribir `.3dm` **fuera** de Rhino. Alimentan [[wiki/concepts/plugins-rhino-grasshopper]] y la parte "fuera de Rhino" de [[wiki/concepts/ecosistema-programacion-rhino]].

## Detalles

### RhinoCommon por dentro

- SDK .NET **multiplataforma** (Windows y Mac) que usan los plugins, Python y Grasshopper. Se instala como paquete NuGet `RhinoCommon`.
- Tres ensamblados: `RhinoCommon.dll` (todo el núcleo), `Eto.dll` (interfaz multiplataforma) y `Rhino.UI.dll` (interfaz propia de Rhino).
- Cinco tipos de plugin: utilidad general (comandos), importar, exportar, render y digitalizador 3D. Todos pueden tener comandos.

### Plugin en C#: el primero

| | Windows | Mac |
|---|---|---|
| Herramienta | Visual Studio + plantilla *RhinoCommon Plugin for Rhino 3D (C#)* | Visual Studio Code + `dotnet new install Rhino.Templates` y luego `dotnet new rhino --version 8 -sample` |
| Resultado | proyecto `.csproj` con un `PlugIn` y un `Command` | lo mismo |
| Probar | F5 abre Rhino con el plugin cargado | *Run and Debug* abre Rhino |

Anatomía: una clase que hereda de `Rhino.PlugIns.PlugIn` (una sola instancia) y uno o más comandos que heredan de `Rhino.Commands.Command`, cada uno con `EnglishName` y `RunCommand(RhinoDoc doc, RunMode mode)`. **Es el mismo esqueleto de las muestras** ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp]]). La plantilla de Windows trae opciones para crear el paquete Yak y los archivos de VS Code.

### Componente de Grasshopper (.NET)

Grasshopper es a su vez un plugin de Rhino (`GrasshopperPlugin.rhp` carga `Grasshopper.dll`). Un plugin de componentes (`.gha`) es una *Class Library* que referencia `RhinoCommon.dll`, `Grasshopper.dll` y `GH_IO.dll`. La guía es antigua (época de Rhino 5–6) y sirve como contexto. El paso a paso actual está en *Your First Component*, que todavía no está en `raw/`.

### Script plugins: de script a plugin sin Visual Studio (Rhino 8)

- En `ScriptEditor` › **Create Project** se crea un proyecto `.rhproj`.
- **Commands/**: cada script (Python, C# o incluso una **definición de Grasshopper** con entradas contextuales) se vuelve un **comando de Rhino**.
- **Components/**: de una definición `.gh` sale un componente por cada componente *Script* que contiene; si la definición tiene entradas/salidas **contextuales**, sale **un componente que corre la definición completa**.
- **Libraries/** (código compartido Python o C#) y **Shared/** (archivos de datos, por ejemplo un JSON de materiales) viajan con el plugin.
- **Publish Project** genera `<nombre>.rhp`, `<nombre>.Components.gha`, una barra de herramientas `.rui` y un paquete **Yak** listo para el Package Manager. También se puede compilar desde la terminal con `rhinocode project build`.
- Además genera una **solución de Visual Studio** (`.sln` y `.csproj`) con el código fuente de los dos plugins. Es la puerta para pasar después a un plugin en C# hecho a mano.
- Versiones: si cambian las entradas de un componente publicado, se duplica y el viejo se marca *Legacy* para no romper definiciones existentes.

### rhino3dm: Rhino sin Rhino

- Librerías basadas en openNURBS para **.NET, Python y JavaScript** que crean, leen y escriben geometría y archivos `.3dm` (curvas, superficies, Brep, mallas, SubD, capas, atributos) **sin tener Rhino abierto**. También pueden llamar a Rhino.Compute.
- **No es para plugins**: solo para programas externos.
- En Python: `pip install rhino3dm` (o `uv add rhino3dm`).
- **Contradicción**: la guía dice que soporta CPython 3.7–3.11. En PyPI, la versión 8.35.0 (revisada el 2026-10-13) publica ruedas para Python **3.9 a 3.14** en Linux, Windows y Mac. Por lo tanto sirve con el Python 3.12 de `cad-python`; la guía está desactualizada.

## Conexiones

- Mapas: [[Mapa - Programación]] · [[Mapa - Entorno y herramientas]]
- [[wiki/concepts/plugins-rhino-grasshopper]]: la escalera completa, aplicada a OVERKILL y al plugin de muebles
- [[wiki/concepts/ecosistema-programacion-rhino]]: dónde encaja cada pieza
- [[wiki/entities/rhinocommon]] · [[wiki/entities/rhino3dm]] · [[wiki/entities/grasshopper]]

## Fuentes

- [[What is RhinoCommon]] · [[Your First Plugin (Windows)]] · [[Your First Plugin (Mac)]]
- [[What is a Grasshopper Component]]
- [[Creating Rhino-Grasshopper Script Plugins]] · [[Publishing Rhino-Grasshopper Script Plugins]]
- [[What is Rhino3dm]]; ruedas de rhino3dm en https://pypi.org/project/rhino3dm/
- Todas en `raw/developer-rhino3d/`, traídas con `herramientas/guias_mcneel.py` (2026-10-13). La guía *Your First Plugin (Cross-Platform)* se descartó porque McNeel la marca como obsoleta.
