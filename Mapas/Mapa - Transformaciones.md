---
tags: [tipo/mapa, geometria/transformaciones, matematicas/matrices, software/grasshopper, software/rhinocommon, software/cadquery]
---

# Transformaciones

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Mover, rotar, escalar, reflejar y orientar. Detrás de todas hay una **matriz 4×4** (`Transform`): se pueden combinar multiplicándolas e invertir. Para deformaciones no lineales (doblar, torcer, mapear a una superficie) ver [[Mapa - Morph y tween]].

## Teoría y código
- [[wiki/concepts/transformaciones-geometricas]]: matrices 4×4 y coordenadas homogéneas
- [[wiki/sources/2026-05-03-matrices-y-transformaciones]] · [[wiki/sources/2026-05-04-rhinopy-operaciones-espaciales]]

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Mover | [[Catálogo - Transform#Move\|Move]] | `rg.Transform.Translation(v)` | `.translate((x, y, z))` |
| Rotar | [[Catálogo - Transform#Rotate\|Rotate]] | `rg.Transform.Rotation(ang_rad, eje, centro)` | `.rotate(p0, p1, grados)` |
| Escalar | [[Catálogo - Transform#Scale\|Scale]] | `rg.Transform.Scale(centro, factor)` | — |
| Reflejar | [[Catálogo - Transform#Mirror\|Mirror]] | `rg.Transform.Mirror(plano)` | `.mirror("YZ")` |
| Plano a plano | [[Catálogo - Transform#Orient\|Orient]] | `rg.Transform.PlaneToPlane(origen, destino)` | — |
| Combinar | [[Catálogo - Transform#Compound (Comp)\|Compound]] | `xf2 * xf1` (primero xf1) | — |
| Invertir | [[Catálogo - Transform#Inverse Transform (Inverse)\|Inverse Transform]] | `ok, inv = xf.TryGetInverse()` | — |
| Aplicar | (cualquiera) | `copia = geo.Duplicate(); copia.Transform(xf)` | — |
| Arreglo polar | [[Catálogo - Transform#Polar Array (ArrPolar)\|Polar Array]] | bucle con `Transform.Rotation` | `.polarArray(r, 0, 360, n)` |

En Grasshopper los componentes devuelven también la `Transform` usada: se puede reaplicar a otra geometría (por ejemplo a los atributos de una pieza de [[wiki/entities/opennest|OpenNest]]).

## Para empezar
[[Catálogo - Transform#Move|Move]] · [[Catálogo - Transform#Rotate|Rotate]] · [[Catálogo - Transform#Orient|Orient]] · [[Catálogo - Transform#Scale NU|Scale NU]] · [[Catálogo - Transform#Mirror|Mirror]] · [[Catálogo - Transform#Linear Array (ArrLinear)|Linear Array]] · [[Catálogo - Transform#Rectangular Array (ArrRec)|Rectangular Array]] · [[Catálogo - Transform#Transform|Transform]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (7)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Array By Distance | [[Array By Distance\|Py]] · [[Array By Distance (cs)\|C#]] | Matriz a lo largo de una dirección con vista previa mientras se mueve el mouse | `Transform.Translation + GetPoint.DynamicDraw (DrawObject)` |
| Constrained Copy | [[Constrained Copy\|Py]] · [[Constrained Copy (cs)\|C#]] | Copia una curva plana con el punto restringido a su normal | `GetPoint.Constrain(linea) → Transform.Translation` |
| Move Grip Objects | [[Move Grip Objects (cs)\|C#]] | Mueve los puntos de control de una superficie según su normal | `RhinoObject.GetGrips → GripObject.Move → doc.Objects.GripUpdate` |
| Move Points | [[Move Points\|Py]] · [[Move Points (cs)\|C#]] | Mueve puntos de un lugar a otro | `Transform.Translation → doc.Objects.Transform` |
| Move Points Non Uniform | [[Move Points Non Uniform\|Py]] · [[Move Points Non Uniform (cs)\|C#]] | Mueve puntos sumando a cada coordenada | `doc.Objects.Replace(objRef, punto)` |
| Orient On Surface | [[Orient On Surface\|Py]] · [[Orient On Surface (cs)\|C#]] | Orienta objetos sobre una superficie según su normal | `Surface.FrameAt(u, v) → Transform.PlaneToPlane` |
| Transform Breps | [[Transform Breps\|Py]] · [[Transform Breps (cs)\|C#]] | Mueve un Brep con una transformación | `Transform.Translation(x, y, z) → doc.Objects.Transform` |

## Componentes de Grasshopper (57)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (1)

- [[Catálogo - Params#Transform (parámetro)|Transform (parámetro)]] — Contiene una colección de transformaciones tridimensionales

### Transform › Affine (11)

- [[Catálogo - Transform#Box Mapping (BoxMap)|Box Mapping (BoxMap)]] — Transforma geometría de una caja a otra
- [[Catálogo - Transform#Camera Obscura (CO)|Camera Obscura (CO)]] — Transformación de cámara oscura (reflejo respecto de un punto)
- [[Catálogo - Transform#Orient Direction (Orient)|Orient Direction (Orient)]] — Orienta un objeto usando solo restricciones de dirección
- [[Catálogo - Transform#Project|Project]] — Proyecta un objeto sobre un plano
- [[Catálogo - Transform#Project Along (ProjectA)|Project Along (ProjectA)]] — Proyecta un objeto sobre un plano en una dirección
- [[Catálogo - Transform#Rectangle Mapping (RecMap)|Rectangle Mapping (RecMap)]] — Transforma geometría de un rectángulo a otro
- [[Catálogo - Transform#Scale|Scale]] — Escala un objeto de forma uniforme en todas las direcciones
- [[Catálogo - Transform#Scale NU|Scale NU]] — Escala un objeto con factores no uniformes
- [[Catálogo - Transform#Shear|Shear]] — Sesga (shear) un objeto según un vector de sesgo
- [[Catálogo - Transform#Shear Angle (Shear)|Shear Angle (Shear)]] — Sesga (shear) un objeto según ángulos de inclinación
- [[Catálogo - Transform#Triangle Mapping (TriMap)|Triangle Mapping (TriMap)]] — Transforma geometría de un triángulo a otro

### Transform › Array (6)

- [[Catálogo - Transform#Box Array (ArrBox)|Box Array (ArrBox)]] — Crea un arreglo de geometría en caja
- [[Catálogo - Transform#Curve Array (ArrCurve)|Curve Array (ArrCurve)]] — Crea un arreglo de geometría a lo largo de una curva
- [[Catálogo - Transform#Kaleidoscope (KScope)|Kaleidoscope (KScope)]] — Aplica una transformación de caleidoscopio a un objeto
- [[Catálogo - Transform#Linear Array (ArrLinear)|Linear Array (ArrLinear)]] — Crea un arreglo lineal de geometría
- [[Catálogo - Transform#Polar Array (ArrPolar)|Polar Array (ArrPolar)]] — Crea un arreglo polar de geometría
- [[Catálogo - Transform#Rectangular Array (ArrRec)|Rectangular Array (ArrRec)]] — Crea un arreglo rectangular de geometría

### Transform › Euclidean (9)

- [[Catálogo - Transform#Mirror|Mirror]] — Refleja (espejo) un objeto
- [[Catálogo - Transform#Move|Move]] — Traslada (mueve) un objeto a lo largo de un vector
- [[Catálogo - Transform#Move Away From (MoveAway)|Move Away From (MoveAway)]] — Traslada (aleja) un objeto de otro objeto
- [[Catálogo - Transform#Move To Plane (MoveToPlane)|Move To Plane (MoveToPlane)]] — Traslada (mueve) un objeto hasta un plano
- [[Catálogo - Transform#Orient|Orient]] — Orienta un objeto. La orientación a veces se llama "transformación de cambio de base" (ChangeBasis): permite…
- [[Catálogo - Transform#Rotate|Rotate]] — Rota un objeto en un plano
- [[Catálogo - Transform#Rotate 3D (Rot3D)|Rotate 3D (Rot3D)]] — Rota un objeto alrededor de un punto central y un vector eje
- [[Catálogo - Transform#Rotate Axis (RotAx)|Rotate Axis (RotAx)]] — Rota un objeto alrededor de un eje
- [[Catálogo - Transform#Rotate Direction (Rotate)|Rotate Direction (Rotate)]] — Rota un objeto de una dirección a otra

### Transform › Util (10)

- [[Catálogo - Transform#Compound (Comp)|Compound (Comp)]] — Combina (compone) dos transformaciones
- [[Catálogo - Transform#Group|Group]] — Agrupa un conjunto de geometría
- [[Catálogo - Transform#Inverse Transform (Inverse)|Inverse Transform (Inverse)]] — Invierte una transformación
- [[Catálogo - Transform#Merge Group (GMerge)|Merge Group (GMerge)]] — Fusiona dos conjuntos de geometría
- [[Catálogo - Transform#Named Group (Group)|Named Group (Group)]] — Agrupa un conjunto de geometría bajo un nombre
- [[Catálogo - Transform#Split|Split]] — Divide una transformación compuesta en sus fragmentos
- [[Catálogo - Transform#Split Group (GSplit)|Split Group (GSplit)]] — Divide un grupo
- [[Catálogo - Transform#Transform|Transform]] — Transforma un objeto
- [[Catálogo - Transform#Transform Matrix (Matrix, parámetro)|Transform Matrix (Matrix, parámetro)]] — Una matriz de transformación de 4x4
- [[Catálogo - Transform#Ungroup|Ungroup]] — Desagrupa un conjunto de geometría

### Pufferfish › Transform (20)

- [[Catálogo - Pufferfish#Average Transform (AvrTran)|Average Transform (AvrTran)]] — Calcula el promedio aritmético de un conjunto de transformaciones
- [[Catálogo - Pufferfish#Mass Transform (MTran)|Mass Transform (MTran)]] — Crea una sola transformación masiva combinando un conjunto de transformaciones, como el componente Compound…
- [[Catálogo - Pufferfish#Mirror Combine Transforms (MirComTrans)|Mirror Combine Transforms (MirComTrans)]] — Refleja un conjunto de transformaciones desde su final o su inicio y lo combina con el conjunto original
- [[Catálogo - Pufferfish#Mirror Cut Transforms (MirCutTrans)|Mirror Cut Transforms (MirCutTrans)]] — Corta un conjunto de transformaciones en un índice, refleja el lado conservado del corte respecto de ese…
- [[Catálogo - Pufferfish#Morph To Twisted Box (Morph2Tbox)|Morph To Twisted Box (Morph2Tbox)]] — Deforma (morph) geometrías desde cajas de referencia hacia cajas torcidas objetivo. (*Solo Rhino 6; en Rhino…
- [[Catálogo - Pufferfish#Move To Point (Move2Pt)|Move To Point (Move2Pt)]] — Mueve (traslada) un objeto de un punto a otro
- [[Catálogo - Pufferfish#Recursive Transform (ReTrans)|Recursive Transform (ReTrans)]] — Transforma geometría de forma recursiva para obtener una secuencia autorreferente de geometría transformada
- [[Catálogo - Pufferfish#Rotate Euler (RotEuler)|Rotate Euler (RotEuler)]] — Rota un objeto según tres ejes de plano y tres ángulos en grados; cada eje se obtiene del plano anterior
- [[Catálogo - Pufferfish#Rotate Quaternion (RotQuat)|Rotate Quaternion (RotQuat)]] — Rota un objeto de un plano a otro según un factor de rotación, usando rotación por cuaterniones
- [[Catálogo - Pufferfish#Rotate World (RotWorld)|Rotate World (RotWorld)]] — Rota un objeto según tres ejes de plano y tres ángulos en grados; cada eje se obtiene de los ejes del plano…
- [[Catálogo - Pufferfish#Scale To Area (Scale2Area)|Scale To Area (Scale2Area)]] — Escala geometría a un área dada, con factores de proporción {x}, {y} y {z}
- [[Catálogo - Pufferfish#Scale To Length (Scale2Len)|Scale To Length (Scale2Len)]] — Escala una curva a una longitud dada, con factores de proporción {x}, {y} y {z}
- [[Catálogo - Pufferfish#Scale To Volume (Scale2Vol)|Scale To Volume (Scale2Vol)]] — Escala geometría a un volumen dado, con factores de proporción {x}, {y} y {z}
- [[Catálogo - Pufferfish#Slide Within Transform (SlideInTran)|Slide Within Transform (SlideInTran)]] — Se desliza entre el inicio y el final de una transformación para obtener un estado de transformación…
- [[Catálogo - Pufferfish#Transform Twisted Box (TranTBox)|Transform Twisted Box (TranTBox)]] — Transforma una caja torcida (porque las cajas torcidas no funcionan con los componentes de transformación…
- [[Catálogo - Pufferfish#Tween Consecutive Transforms (TwnConTrans)|Tween Consecutive Transforms (TwnConTrans)]] — Interpola (tween) consecutivamente entre un conjunto de transformaciones
- [[Catálogo - Pufferfish#Tween Through Transforms (TwnThruTrans)|Tween Through Transforms (TwnThruTrans)]] — Interpola (tween) a través de un conjunto de transformaciones
- [[Catálogo - Pufferfish#Tween Two Transforms (Twn2Trans)|Tween Two Transforms (Twn2Trans)]] — Interpola (tween) entre dos transformaciones
- [[Catálogo - Pufferfish#Weighted Average Transform (WavTran)|Weighted Average Transform (WavTran)]] — Calcula el promedio aritmético ponderado de un conjunto de transformaciones
- [[Catálogo - Pufferfish#Zeroed Transform (ZeroTran)|Zeroed Transform (ZeroTran)]] — Entrega una transformación en cero, que representa ninguna transformación o el estado previo a cualquier…

<!-- AUTO:fin -->
