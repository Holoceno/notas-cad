---
title: "Plugins de Rhino y Grasshopper: del script al plugin"
type: concept
tags: [tipo/concepto, programacion/plugins, software/rhinocommon, software/grasshopper, lenguaje/csharp, lenguaje/python]
palabras-clave: [plugin, rhp, gha, rui, yak, rhproj, script plugin, ScriptEditor, Visual Studio, VS Code, dotnet, Rhino.Templates, Command, RunCommand, GH_Component, SolveInstance, Package Manager, legacy]
sources: [raw/developer-rhino3d/scripting/Creating Rhino-Grasshopper Script Plugins.md, raw/developer-rhino3d/scripting/Publishing Rhino-Grasshopper Script Plugins.md, raw/developer-rhino3d/rhinocommon/Your First Plugin (Windows).md, raw/developer-rhino3d/rhinocommon/Your First Plugin (Mac).md, raw/developer-rhino3d/rhinocommon/What is RhinoCommon.md, raw/developer-rhino3d/scripting/Grasshopper Scripting - C♯.md]
created: 2026-10-13
updated: 2026-10-13
---

Un **plugin** empaqueta código para que Rhino lo cargue como **comandos** (`.rhp`) y Grasshopper como **componentes** (`.gha`), instalables en cualquier equipo. En Rhino 8 hay dos caminos que terminan en los mismos archivos. El **script plugin** se arma desde el `ScriptEditor` con scripts de Python o C# y definiciones de Grasshopper, sin Visual Studio. El **plugin en C#** se escribe desde una plantilla en Visual Studio (Windows) o VS Code (Mac). El primero sirve para empezar ya; el segundo, para cuando haga falta control total. El primero además genera el código del segundo.

## Detalles

### Qué es cada archivo

| Archivo | Qué es |
|---|---|
| `.rhp` | plugin de Rhino: comandos |
| `.gha` | plugin de Grasshopper: componentes |
| `.rui` | barra de herramientas con botones para los comandos |
| `.yak` | paquete del gestor de Rhino (*Package Manager*): lleva todo lo anterior y los datos compartidos |
| `.rhproj` | proyecto del Script Editor (la "receta" del script plugin) |
| `.sln` / `.csproj` | solución y proyecto de C# (Visual Studio / VS Code / `dotnet`) |

### Camino A: script plugin (sin escribir C#)

1. `ScriptEditor` → *File › Create Project* → guardar `MiToolkit.rhproj` y elegir el autor (obligatorio).
2. **Commands/** → agregar scripts. Cada uno se vuelve un comando de Rhino, por ejemplo el script de OVERKILL → comando `Overkill`. También sirve una definición de Grasshopper con entradas **contextuales** (*Get Integer*, *Get Geometry*): Rhino pide esos datos en la línea de comandos.
3. **Components/** → agregar una definición `.gh`. Si tiene componentes *Script*, cada uno se publica como componente. Si tiene entradas y salidas **contextuales**, la definición completa se publica como **un** componente.
4. **Libraries/** → código compartido entre comandos y componentes (un módulo de Python con `__init__.py` o una carpeta de archivos `.cs`). Aquí iría el **núcleo** de OVERKILL.
5. **Shared/** → archivos de datos que viajan con el plugin (un JSON de materiales y espesores, por ejemplo). Se encuentran en el equipo de destino con `PlugIn.PathFromId`.
6. *Publish Project* → elegir la versión mínima de Rhino (*Build Target*) → *Build Package*. Desde la terminal: `rhinocode project build MiToolkit.rhproj`.

Antes de publicar un componente conviene darle a cada entrada un nombre legible, un *Tooltip* y la marca *Required*. Al compilar, el componente publicado hereda acceso, *Type Hint* y vista previa del componente original.

Si después cambian las entradas de un componente ya publicado, se duplica en la definición y el viejo se marca **Legacy**: queda oculto pero las definiciones antiguas siguen funcionando.

### Camino B: plugin en C#

| | Windows | Mac |
|---|---|---|
| Crear | Visual Studio → plantilla *RhinoCommon Plugin for Rhino 3D (C#)* | VS Code → `dotnet new install Rhino.Templates` y `dotnet new rhino --version 8 -sample` |
| Probar | F5 abre Rhino con el plugin | *Run and Debug* abre Rhino |

Anatomía mínima:

```csharp
public class MiToolkitPlugin : Rhino.PlugIns.PlugIn { }        // una sola instancia

public class OverkillCommand : Rhino.Commands.Command
{
    public override string EnglishName => "Overkill";          // nombre en la línea de comandos (único)
    protected override Result RunCommand(RhinoDoc doc, RunMode mode)
    {
        // 1. pedir (GetObject) · 2. calcular (núcleo) · 3. agregar a doc.Objects
        return Result.Success;
    }
}
```

Es el **mismo esqueleto** de las muestras oficiales ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp]]): una muestra C# se convierte en comando pegando su cuerpo dentro de `RunCommand`.

### Cómo se corresponden los dos caminos

| Script plugin | Plugin en C# |
|---|---|
| variable `__rhino_doc__` | parámetro `doc` de `RunCommand` |
| `__rhino_runmode__`, `__is_interactive__` | parámetro `mode` (`RunMode.Interactive`) |
| `__rhino_command__` | la clase `Command` misma |
| componente Script en *SDK-Mode*: `RunScript`, `BeforeRunScript`, `AfterRunScript`, `DrawViewportWires` | `GH_Component`: `SolveInstance`, `BeforeSolveInstance`, `AfterSolveInstance`, `DrawViewportWires` |
| el `.sln` que genera *Publish* | el punto de partida para seguir en C# |

Por eso conviene empezar por el script plugin: al publicarlo, el Script Editor escribe una solución de C# con los mismos comandos y componentes, lista para abrir en Visual Studio o VS Code.

### Instalar en otro equipo

- Para probar: arrastrar el `.rhp` a Rhino (o *Opciones › Plug-ins › Instalar*) y copiar el `.gha` a la carpeta de componentes de Grasshopper (*File › Special Folders › Components Folder*).
- Para distribuir: el paquete `.yak` se publica en el servidor de paquetes de Rhino y se instala desde el *Package Manager*. **Ojo**: el servidor oficial es **público**. El código que no sea público no debe subirse ahí.

### Aplicación a mis proyectos

- **OVERKILL**: script (hoy) → script plugin con el comando `Overkill` y un componente para Grasshopper, compartiendo el núcleo en *Libraries/* → C# si crece. Es la "alternativa sin C#" que ya mencionaba Plugins Rhino y Grasshopper.
- **Toolkit en C#** (Core / Core.Tests / GH): sigue siendo el plan a largo plazo. La solución generada por el script plugin puede servir de molde. En Linux se compila y se prueban los tests con `dotnet`, pero Rhino no corre ahí: la depuración dentro de Rhino es en Windows o en el Mac.

## Conexiones

- Mapas: [[Mapa - Programación]] · [[Mapa - Scripts, interfaz y archivos]] · [[Mapa - Entorno y herramientas]]
- [[wiki/concepts/ecosistema-programacion-rhino]]: la escalera completa (Grasshopper → script → plugin)
- [[wiki/concepts/python-csharp-rhinocommon]]: pasar el núcleo de Python a C#
- [[wiki/sources/2026-10-13-guias-plugins-rhino]] · [[wiki/sources/2026-10-13-guias-scripting-rhino8]]
- [[wiki/entities/rhinocommon]] · [[wiki/entities/grasshopper]]

## Fuentes

- Script plugins: [[Creating Rhino-Grasshopper Script Plugins]] · [[Publishing Rhino-Grasshopper Script Plugins]].
- Plugin en C#: [[Your First Plugin (Windows)]] · [[Your First Plugin (Mac)]] · [[What is RhinoCommon]].
- Métodos `SolveInstance`, `DrawViewportWires` y sus pares en el componente de script: [[Grasshopper Scripting - C♯]].
- Instalar arrastrando el `.rhp`, la carpeta de componentes y la nota sobre el servidor público: conocimiento general, **pendiente de confirmar** con la guía de Yak (*Creating a Rhino Plugin Package*) cuando se agregue a `raw/`.
- Pendientes de traer para completar esta página: *Installing Tools* (Windows/Mac), *Your First Component* (Windows/Mac), *Simple Component*, *Creating a Rhino Plugin Package* (Yak), *RhinoCode CLI*.
