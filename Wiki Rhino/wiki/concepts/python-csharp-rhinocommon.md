---
title: "Traducir entre Python y C# con RhinoCommon"
type: concept
tags: [tipo/concepto, software/rhinocommon, lenguaje/python, lenguaje/csharp, programacion/scripts]
palabras-clave: [python, c#, csharp, traducir, sintaxis, out, ref, tupla, null, None, using, import, List, foreach, IronPython, Python 3, Python.NET, RunScript, DataTree, scriptcontext, RhinoDoc]
sources: [raw/developer-rhino3d/rhinopython/Providing Arguments for By-Reference Parameters.md, raw/developer-rhino3d/rhinopython/Calling Overloaded Methods from Python.md, raw/developer-rhino3d/rhinopython/Python 3 in Rhino.md, raw/developer-rhino3d/scripting/Grasshopper Scripting - C♯.md, raw/developer-rhino3d/scripting/Grasshopper Scripting - Python.md, raw/rhinopy/Offset Curve.md, raw/rhinocs/Offset Curve (cs).md]
created: 2026-10-13
updated: 2026-10-13
---

RhinoCommon es una librería .NET: Python y C# usan **las mismas clases y los mismos métodos** (`Curve.Offset`, `Brep.CreateBooleanDifference`). Pasar de un lenguaje al otro es cambiar la **sintaxis**, no la API. Por eso lo que el usuario ya sabe de RhinoCommon en Python vale entero en C#. La mejor práctica para aprender son las 158 muestras oficiales, que traen el mismo ejemplo en los dos lenguajes ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp]]).

## Tabla de traducción

| Qué | Python 3 (Rhino 8) | C# |
|---|---|---|
| Importar | `import Rhino` · `from Rhino.Geometry import Point3d` | `using Rhino.Geometry;` |
| Crear un objeto | `p = Point3d(0, 0, 0)` | `var p = new Point3d(0, 0, 0);` |
| Tipos | no se declaran | se declaran (`double r = 5;`) o se infieren con `var` |
| Nulo | `None` | `null` |
| Verdadero / falso | `True` / `False` | `true` / `false` |
| Y / o / no | `and` / `or` / `not` | `&&` / `\|\|` / `!` |
| Lista | `pts = []` · `pts.append(p)` | `var pts = new List<Point3d>();` · `pts.Add(p);` |
| Largo | `len(lista)` (lista de Python) · `.Count` (lista de .NET) | `.Count` (List) · `.Length` (arreglo) |
| Recorrer | `for p in pts:` | `foreach (var p in pts) { ... }` |
| Contar | `for i in range(n):` | `for (int i = 0; i < n; i++) { ... }` |
| Bloques | sangría | llaves `{ }` y `;` al final de cada línea |
| Función | `def area(c): return ...` | `double Area(Curve c) { return ...; }` |
| Texto con valores | `f"{n} piezas"` | `$"{n} piezas"` |
| Imprimir | `print(x)` | `Console.WriteLine(x)` (script o componente) · `RhinoApp.WriteLine(x)` (línea de comandos) |
| Comentario | `# ...` | `// ...` |
| Documento activo | `scriptcontext.doc` | `RhinoDoc.ActiveDoc` (script) · parámetro `doc` (comando de plugin) |
| ¿Se agregó el objeto? | `if id != System.Guid.Empty:` | `if (id != Guid.Empty)` |

### Las cuatro diferencias que sí importan

1. **Parámetros `out` → tupla.** En C# un método entrega varios resultados con `out`. En Python **no se pasa** ese argumento: el método devuelve una tupla.
   ```python
   ok, t = crv.ClosestPoint(pt)                # Python
   ```
   ```csharp
   bool ok = crv.ClosestPoint(pt, out double t);   // C#
   ```
   Lo mismo con `RhinoGet`: `rc, obj_ref = RhinoGet.GetOneObject(...)` en Python, `RhinoGet.GetOneObject(..., out ObjRef obj_ref)` en C#.
2. **Enums llamados `None`** (en Python 3): `CurveOffsetCornerStyle.None` es un error de sintaxis porque `None` es palabra reservada. Python 3 los expone como `NONE`. En C# y en IronPython 2 sigue siendo `None`.
3. **Colecciones de .NET**: un método que devuelve `IEnumerable` entrega un iterador en Python 3. `list(...)` lo convierte para usar `len()` o índices. Los arreglos (`Curve[]`) se recorren igual en los dos.
4. **Sobrecargas**: C# elige la versión del método por los tipos al compilar. Python la adivina al ejecutar y a veces no puede ("Multiple targets could match"). En IronPython se fuerza con `metodo.Overloads[tipos](...)`.

Además, en Python 3, una clase que hereda de una de .NET (un `DisplayConduit`, por ejemplo) **debe** llamar `super().__init__()`.

## Lado a lado: Offset Curve

La misma muestra oficial, sin el envoltorio ([[Offset Curve|Python]] · [[Offset Curve (cs)|C#]]):

```python
rc, obj_ref = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve)
if rc != Result.Success:
    return rc
curve = obj_ref.Curve()
rc, point = RhinoGet.GetPoint("Select Side", False)
curves = curve.Offset(point, Vector3d.ZAxis, 1.0, doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None)
for offset_curve in curves:
    doc.Objects.AddCurve(offset_curve)
```

```csharp
ObjRef obj_ref;
var rs = RhinoGet.GetOneObject("Select Curve", false, ObjectType.Curve, out obj_ref);
if (rs != Result.Success)
  return rs;
var curve = obj_ref.Curve();
Point3d point;
rs = RhinoGet.GetPoint("Select Side", false, out point);
var curves = curve.Offset(point, Vector3d.ZAxis, 1.0, doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None);
foreach (var offset_curve in curves)
  doc.Objects.AddCurve(offset_curve);
```

Para fijarse:

- La línea del `Offset` es **idéntica** en los dos.
- `out obj_ref` y `out point` en C# corresponden a `rc, obj_ref = ...` y `rc, point = ...` en Python.
- Para correr el Python en el motor **Python 3**, hay que cambiar `CurveOffsetCornerStyle.None` por `.NONE`. Tal como está, es IronPython 2.
- **Errata de McNeel**: la muestra C# oficial escribe `offset-curve` como nombre de variable, y eso no compila (un guion no puede ir en un nombre). Arriba ya va corregido como `offset_curve`. Las muestras no se prueban todas: leerlas con ojo crítico.

## En un componente de script de Grasshopper

| | Python 3 | C# |
|---|---|---|
| Modo simple (*Script-Mode*) | `a = x + y` | `a = x + y;` |
| Modo SDK | `class MyComponent(Grasshopper.Kernel.GH_ScriptInstance)` con `def RunScript(self, x, y):` que **devuelve** las salidas | `class Script_Instance : GH_ScriptInstance` con `RunScript(double x, double y, ref object a)`: las salidas van por `ref` |
| Entrada con acceso *List* | `list` de Python (convertida automáticamente) | `List<T>` |
| Entrada con acceso *Tree* | `DataTree[object]` | `DataTree<T>` |
| Entrada sin conectar | `None` | `null`, o el valor por defecto si el tipo es por valor (`double` → 0) |
| Vista previa propia | `DrawViewportWires(self, args)` | `DrawViewportWires(IGH_PreviewArgs args)` |

Crear un árbol en los dos lenguajes: ver la sección "En código" de [[wiki/concepts/data-trees]].

## Errores típicos al traducir

| Síntoma | Causa | Arreglo |
|---|---|---|
| Python: `SyntaxError` en `.None` | enum `None` en Python 3 | `.NONE` |
| Python: "expected 3 arguments, got 4" o similar | se pasó un argumento `out` | quitarlo y recibir la tupla |
| C#: "Cannot convert type 'object'" | salida o entrada sin *Type Hint* | poner el hint, o convertir con `(Curve)x` |
| C#: `NullReferenceException` | un método devolvió `null` (operación fallida) | comprobar `if (resultado == null)` antes de usarlo, como hacen las muestras |
| Python: `len()` falla sobre el resultado | es un iterador de .NET | `list(resultado)` |

## Conexiones

- Mapas: [[Mapa - Programación]] · [[Mapa - Scripts, interfaz y archivos]]
- [[wiki/concepts/ecosistema-programacion-rhino]]: dónde corre cada lenguaje
- [[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp]]: 158 ejemplos para practicar
- [[wiki/sources/2026-10-13-guias-scripting-rhino8]]: Python 3 vs 2, componentes de script
- [[wiki/concepts/rhinocommon-document-api]]: `doc.Objects.Add…` y `scriptcontext`
- [[wiki/concepts/interactive-object-selection]]: `GetObject` en los dos lenguajes
- [[wiki/entities/rhinocommon]]

## Fuentes

- Parámetros `out`/`ref` y sobrecargas: [[Providing Arguments for By-Reference Parameters]] · [[Calling Overloaded Methods from Python]] (escritas para IronPython).
- Cambios de Python 3 (enums `NONE`, iteradores, `super().__init__()`): [[Python 3 in Rhino]].
- Componentes de script (modos, `RunScript`, `ref`, tipos por valor, *marshalling*): [[Grasshopper Scripting - C♯]] · [[Grasshopper Scripting - Python]].
- Ejemplo: [[Offset Curve]] · [[Offset Curve (cs)]].
- La tabla de sintaxis general (bucles, listas, texto) es síntesis propia con conocimiento general de Python y C#.
