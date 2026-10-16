---
tags: [tipo/mapa, geometria/morph, geometria/transformaciones, software/grasshopper, plugin/pufferfish]
---

# Morph y tween

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

- **Morph**: deformar geometría llevándola de un espacio de referencia a otro: caja → caja torcida, superficie → superficie, doblar, torcer.
- **Tween**: generar formas intermedias entre dos (o más) formas.
- **Twisted Box** (Pufferfish): una caja de 8 esquinas libres. Es la base para poblar una superficie con un componente deformado: paneles, celosías, módulos.

## Teoría y código
- [[wiki/concepts/transformaciones-geometricas]]: las transformaciones afines; aquí se rompe la linealidad
- RhinoCommon: `Rhino.Geometry.Morphs` (`BendSpaceMorph`, `TwistSpaceMorph`, `TaperSpaceMorph`, `FlowSpaceMorph`, `StretchSpaceMorph`...) y luego `morph.Morph(geo)`

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) |
|---|---|---|
| Caja a caja (o twisted box) | [[Catálogo - Transform#Box Morph (Morph)\|Box Morph]] | — (lo implementa Grasshopper) |
| Doblar / torcer / ahusar | [[Catálogo - Transform#Bend Deform (Bend)\|Bend]] / [[Catálogo - Transform#Twist\|Twist]] / [[Catálogo - Transform#Taper\|Taper]] | `rg.Morphs.BendSpaceMorph`, `TwistSpaceMorph`, `TaperSpaceMorph` |
| Seguir una curva | [[Catálogo - Transform#Flow\|Flow]] | `rg.Morphs.FlowSpaceMorph(curva_a, curva_b, False)` |
| Curvas intermedias | [[Catálogo - Curve#Tween Curve (TweenCrv)\|Tween Curve]] | `rg.Curve.CreateTweenCurves(a, b, n, tol)` |

## Para empezar
[[Catálogo - Transform#Surface Box (SBox)|Surface Box]] + [[Catálogo - Transform#Box Morph (Morph)|Box Morph]] (el clásico panelizado) · [[Catálogo - Pufferfish#Construct Twisted Box (CoTBox)|Construct Twisted Box]] · [[Catálogo - Pufferfish#Twisted Box Array (TBoxArray)|Twisted Box Array]] · [[Catálogo - Pufferfish#Tween Two Twisted Boxes (Twn2TBoxs)|Tween Two Twisted Boxes]] · [[Catálogo - Curve#Tween Curve (TweenCrv)|Tween Curve]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (2)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Space Morph | [[Space Morph (cs)\|C#]] | Deformaciones: Twist, Bend, Taper, Maelstrom, Stretch, Sporph, Flow y Splop | `TwistSpaceMorph, BendSpaceMorph... → morph.Morph(geometria)` |
| Tween Curve | [[Tween Curve (cs)\|C#]] | Curvas intermedias entre dos curvas | `Curve.CreateTweenCurves(c0, c1, n)` |

## Componentes de Grasshopper (131)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (1)

- [[Catálogo - Params#Twisted Box (TBox, parámetro)|Twisted Box (TBox, parámetro)]] — Contiene una colección de cajas torcidas (twisted boxes)

### Curve › Spline (1)

- [[Catálogo - Curve#Tween Curve (TweenCrv)|Tween Curve (TweenCrv)]] — Interpola (tween) entre dos curvas

### Transform › Morph (20)

- [[Catálogo - Transform#Bend Deform (Bend)|Bend Deform (Bend)]] — Deforma una forma doblándola
- [[Catálogo - Transform#Blend Box (BlendBox)|Blend Box (BlendBox)]] — Crea una caja torcida entre dos superficies
- [[Catálogo - Transform#Box Morph (Morph)|Box Morph (Morph)]] — Deforma (morph) un objeto dentro de una caja torcida
- [[Catálogo - Transform#Flow|Flow]] — Realinea objetos de una curva base a una curva objetivo
- [[Catálogo - Transform#Maelstrom|Maelstrom]] — Deforma objetos en espiral, como si estuvieran atrapados en un remolino
- [[Catálogo - Transform#Map to Surface (Map Srf)|Map to Surface (Map Srf)]] — Mapea una curva sobre una superficie mediante sus puntos de control
- [[Catálogo - Transform#Mirror Curve (Mirror)|Mirror Curve (Mirror)]] — Refleja una forma en una curva libre
- [[Catálogo - Transform#Mirror Surface (Mirror)|Mirror Surface (Mirror)]] — Refleja geometría en una superficie libre
- [[Catálogo - Transform#MorphToMesh (M2M)|MorphToMesh (M2M)]] — Deforma (morph) geometría desde polígonos de referencia hacia celdas con offset de una malla de triángulos…
- [[Catálogo - Transform#Point Deform (PDeform)|Point Deform (PDeform)]] — Deforma una forma moviendo sus puntos de control de forma individual
- [[Catálogo - Transform#Spatial Deform (custom) (Deform)|Spatial Deform (custom) (Deform)]] — Realiza una deformación espacial según una sintaxis espacial personalizada
- [[Catálogo - Transform#Spatial Deform (Deform)|Spatial Deform (Deform)]] — Realiza una deformación espacial según una sintaxis espacial personalizada
- [[Catálogo - Transform#Splop|Splop]] — Envuelve geometría sobre una superficie
- [[Catálogo - Transform#Sporph|Sporph]] — Deforma un objeto desde una superficie de origen hacia una superficie objetivo
- [[Catálogo - Transform#Stretch|Stretch]] — Deforma objetos estirándolos a lo largo de un eje finito
- [[Catálogo - Transform#Surface Box (SBox)|Surface Box (SBox)]] — Crea una caja torcida sobre un parche de superficie
- [[Catálogo - Transform#Surface Morph (SrfMorph)|Surface Morph (SrfMorph)]] — Deforma (morph) geometría a las coordenadas UVW de una superficie
- [[Catálogo - Transform#Taper|Taper]] — Deforma objetos acercándolos o alejándolos de un eje
- [[Catálogo - Transform#Twist|Twist]] — Deforma objetos torciéndolos alrededor de un eje
- [[Catálogo - Transform#Twisted Box (TBox)|Twisted Box (TBox)]] — Crea una caja torcida a partir de puntos de esquina

### Pufferfish › Color (3)

- [[Catálogo - Pufferfish#Tween Consecutive Colors (TwnConCols)|Tween Consecutive Colors (TwnConCols)]] — Interpola (tween) consecutivamente entre un conjunto de colores
- [[Catálogo - Pufferfish#Tween Through Colors (TwnThruCols)|Tween Through Colors (TwnThruCols)]] — Interpola (tween) a través de un conjunto de colores
- [[Catálogo - Pufferfish#Tween Two Colors (Twn2Cols)|Tween Two Colors (Twn2Cols)]] — Interpola (tween) entre dos colores

### Pufferfish › Curve (9)

- [[Catálogo - Pufferfish#Tween Consecutive Curves (TwnConCrvs)|Tween Consecutive Curves (TwnConCrvs)]] — Interpola (tween) consecutivamente entre un conjunto de curvas
- [[Catálogo - Pufferfish#Tween Consecutive Curves Along Curve (TwnConCrvsCrv)|Tween Consecutive Curves Along Curve (TwnConCrvsCrv)]] — Interpola (tween) consecutivamente entre un conjunto de curvas a lo largo de una curva guía (u opcionalmente…
- [[Catálogo - Pufferfish#Tween Consecutive Curves On Surface (TwnConCrvsSrf)|Tween Consecutive Curves On Surface (TwnConCrvsSrf)]] — Interpola (tween) consecutivamente entre un conjunto de curvas sobre una superficie; si las curvas no están…
- [[Catálogo - Pufferfish#Tween Through Curves (TwnThruCrvs)|Tween Through Curves (TwnThruCrvs)]] — Interpola (tween) a través de un conjunto de curvas
- [[Catálogo - Pufferfish#Tween Through Curves Along Curve (TwnThruCrvsCrv)|Tween Through Curves Along Curve (TwnThruCrvsCrv)]] — Interpola (tween) a través de un conjunto de curvas a lo largo de una curva guía (u opcionalmente de dos…
- [[Catálogo - Pufferfish#Tween Through Curves On Surface (TwnThruCrvsSrf)|Tween Through Curves On Surface (TwnThruCrvsSrf)]] — Interpola (tween) a través de un conjunto de curvas sobre una superficie; si las curvas no están sobre la…
- [[Catálogo - Pufferfish#Tween Two Curves (Twn2Crvs)|Tween Two Curves (Twn2Crvs)]] — Interpola (tween) entre dos curvas
- [[Catálogo - Pufferfish#Tween Two Curves Along Curve (Twn2CrvsCrv)|Tween Two Curves Along Curve (Twn2CrvsCrv)]] — Interpola (tween) entre dos curvas a lo largo de una curva guía (u opcionalmente de dos curvas guía)
- [[Catálogo - Pufferfish#Tween Two Curves On Surface (Twn2CrvsSrf)|Tween Two Curves On Surface (Twn2CrvsSrf)]] — Interpola (tween) entre dos curvas sobre una superficie; si las curvas no están sobre la superficie, se…

### Pufferfish › Domain (6)

- [[Catálogo - Pufferfish#Tween Consecutive Domains (TwnConDoms)|Tween Consecutive Domains (TwnConDoms)]] — Interpola (tween) consecutivamente entre un conjunto de dominios
- [[Catálogo - Pufferfish#Tween Consecutive Domains² (TwnConDoms²)|Tween Consecutive Domains² (TwnConDoms²)]] — Interpola (tween) consecutivamente entre un conjunto de dominios²
- [[Catálogo - Pufferfish#Tween Through Domains (TwnThruDoms)|Tween Through Domains (TwnThruDoms)]] — Interpola (tween) a través de un conjunto de dominios
- [[Catálogo - Pufferfish#Tween Through Domains² (TwnThruDoms²)|Tween Through Domains² (TwnThruDoms²)]] — Interpola (tween) a través de un conjunto de dominios²
- [[Catálogo - Pufferfish#Tween Two Domains (Twn2Doms)|Tween Two Domains (Twn2Doms)]] — Interpola (tween) entre dos dominios
- [[Catálogo - Pufferfish#Tween Two Domains² (Twn2Doms²)|Tween Two Domains² (Twn2Doms²)]] — Interpola (tween) entre dos dominios²

### Pufferfish › Mesh (3)

- [[Catálogo - Pufferfish#Tween Consecutive Meshes (TwnConMshs)|Tween Consecutive Meshes (TwnConMshs)]] — Interpola (tween) consecutivamente entre un conjunto de mallas; las mallas deben tener la misma topología.…
- [[Catálogo - Pufferfish#Tween Through Meshes (TwnThruMshs)|Tween Through Meshes (TwnThruMshs)]] — Interpola (tween) a través de un conjunto de mallas; las mallas deben tener la misma topología. También puede…
- [[Catálogo - Pufferfish#Tween Two Meshes (Twn2Mshs)|Tween Two Meshes (Twn2Mshs)]] — Interpola (tween) entre dos mallas; las mallas deben tener la misma topología. También puede interpolar los…

### Pufferfish › Number (3)

- [[Catálogo - Pufferfish#Tween Consecutive Numbers (TwnConNums)|Tween Consecutive Numbers (TwnConNums)]] — Interpola (tween) consecutivamente entre un conjunto de números
- [[Catálogo - Pufferfish#Tween Through Numbers (TwnThruNums)|Tween Through Numbers (TwnThruNums)]] — Interpola (tween) a través de un conjunto de números
- [[Catálogo - Pufferfish#Tween Two Numbers (Twn2Nums)|Tween Two Numbers (Twn2Nums)]] — Interpola (tween) entre dos números

### Pufferfish › Plane (9)

- [[Catálogo - Pufferfish#Tween Consecutive Planes (TwnConPlns)|Tween Consecutive Planes (TwnConPlns)]] — Interpola (tween) consecutivamente entre un conjunto de planos
- [[Catálogo - Pufferfish#Tween Consecutive Planes On Curve (TwnConPlnsCrv)|Tween Consecutive Planes On Curve (TwnConPlnsCrv)]] — Interpola (tween) consecutivamente entre un conjunto de planos sobre una curva; si los orígenes de los planos…
- [[Catálogo - Pufferfish#Tween Consecutive Planes On Surface (TwnConPlnsSrf)|Tween Consecutive Planes On Surface (TwnConPlnsSrf)]] — Interpola (tween) consecutivamente entre un conjunto de planos sobre una superficie; si los orígenes de los…
- [[Catálogo - Pufferfish#Tween Through Planes (TwnThruPlns)|Tween Through Planes (TwnThruPlns)]] — Interpola (tween) a través de un conjunto de planos
- [[Catálogo - Pufferfish#Tween Through Planes On Curve (TwnThruPlnsCrv)|Tween Through Planes On Curve (TwnThruPlnsCrv)]] — Interpola (tween) a través de un conjunto de planos sobre una curva; si los orígenes de los planos no están…
- [[Catálogo - Pufferfish#Tween Through Planes On Surface (TwnThruPlnsSrf)|Tween Through Planes On Surface (TwnThruPlnsSrf)]] — Interpola (tween) a través de un conjunto de planos sobre una superficie; si los orígenes de los planos no…
- [[Catálogo - Pufferfish#Tween Two Planes (Twn2Plns)|Tween Two Planes (Twn2Plns)]] — Interpola (tween) entre dos planos
- [[Catálogo - Pufferfish#Tween Two Planes On Curve (Twn2PlnsCrv)|Tween Two Planes On Curve (Twn2PlnsCrv)]] — Interpola (tween) entre dos planos sobre una curva; si los orígenes de los planos no están sobre la curva, se…
- [[Catálogo - Pufferfish#Tween Two Planes On Surface (Twn2PlnsSrf)|Tween Two Planes On Surface (Twn2PlnsSrf)]] — Interpola (tween) entre dos planos sobre una superficie; si los orígenes de los planos no están sobre la…

### Pufferfish › Point (9)

- [[Catálogo - Pufferfish#Tween Consecutive Points (TwnConPts)|Tween Consecutive Points (TwnConPts)]] — Interpola (tween) consecutivamente entre un conjunto de puntos
- [[Catálogo - Pufferfish#Tween Consecutive Points On Curve (TwnConPtsCrv)|Tween Consecutive Points On Curve (TwnConPtsCrv)]] — Interpola (tween) consecutivamente entre un conjunto de puntos sobre una curva; si los puntos no están sobre…
- [[Catálogo - Pufferfish#Tween Consecutive Points On Surface (TwnConPtsSrf)|Tween Consecutive Points On Surface (TwnConPtsSrf)]] — Interpola (tween) consecutivamente entre un conjunto de puntos sobre una superficie; si los puntos no están…
- [[Catálogo - Pufferfish#Tween Through Points (TwnThruPts)|Tween Through Points (TwnThruPts)]] — Interpola (tween) a través de un conjunto de puntos
- [[Catálogo - Pufferfish#Tween Through Points On Curve (TwnThruPtsCrv)|Tween Through Points On Curve (TwnThruPtsCrv)]] — Interpola (tween) a través de un conjunto de puntos sobre una curva; si los puntos no están sobre la curva…
- [[Catálogo - Pufferfish#Tween Through Points On Surface (TwnThruPtsSrf)|Tween Through Points On Surface (TwnThruPtsSrf)]] — Interpola (tween) a través de un conjunto de puntos sobre una superficie; si los puntos no están sobre la…
- [[Catálogo - Pufferfish#Tween Two Points (Twn2Pts)|Tween Two Points (Twn2Pts)]] — Interpola (tween) entre dos puntos
- [[Catálogo - Pufferfish#Tween Two Points On Curve (Twn2PtsCrv)|Tween Two Points On Curve (Twn2PtsCrv)]] — Interpola (tween) entre dos puntos sobre una curva; si los puntos no están sobre la curva, se llevan hacia…
- [[Catálogo - Pufferfish#Tween Two Points On Surface (Twn2PtsSrf)|Tween Two Points On Surface (Twn2PtsSrf)]] — Interpola (tween) entre dos puntos sobre una superficie; si los puntos no están sobre la superficie, se…

### Pufferfish › SubD (7)

- [[Catálogo - Pufferfish#Tween Consecutive SubDs (TwnConSubDs, user object)|Tween Consecutive SubDs (TwnConSubDs, user object)]] — Interpola (tween) consecutivamente entre un conjunto de SubDs; las SubDs deben tener la misma topología.…
- [[Catálogo - Pufferfish#Tween Through SubDs (TwnThruSubDs, user object)|Tween Through SubDs (TwnThruSubDs, user object)]] — Interpola (tween) a través de un conjunto de SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)
- [[Catálogo - Pufferfish#Tween Two SubDs (Twn2SubDs, user object)|Tween Two SubDs (Twn2SubDs, user object)]] — Interpola (tween) entre dos SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)
- [[Catálogo - Pufferfish#Twisted Box Consecutive SubDs (TBoxConSubDs, user object)|Twisted Box Consecutive SubDs (TBoxConSubDs, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre un conjunto de SubDs a partir…
- [[Catálogo - Pufferfish#Twisted Box SubD (TBoxSubD, user object)|Twisted Box SubD (TBoxSubD, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas sobre una SubD, a partir de sus caras y un espesor…
- [[Catálogo - Pufferfish#Twisted Box Through SubDs (TBoxThruSubDs, user object)|Twisted Box Through SubDs (TBoxThruSubDs, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de SubDs a partir de sus caras…
- [[Catálogo - Pufferfish#Twisted Box Two SubDs (TBox2SubDs, user object)|Twisted Box Two SubDs (TBox2SubDs, user object)]] — Crea un arreglo en capas de cajas torcidas conectadas entre dos SubDs a partir de sus caras; las SubDs deben…

### Pufferfish › Surface (4)

- [[Catálogo - Pufferfish#Tween Consecutive Surfaces (TwnConSrfs)|Tween Consecutive Surfaces (TwnConSrfs)]] — Interpola (tween) consecutivamente entre un conjunto de superficies; las superficies recortadas se tratan…
- [[Catálogo - Pufferfish#Tween Through Surfaces (TwnThruSrfs)|Tween Through Surfaces (TwnThruSrfs)]] — Interpola (tween) a través de un conjunto de superficies; las superficies recortadas se tratan como sin…
- [[Catálogo - Pufferfish#Tween Two Surfaces (Twn2Srfs)|Tween Two Surfaces (Twn2Srfs)]] — Interpola (tween) entre dos superficies; las superficies recortadas se tratan como sin recortar
- [[Catálogo - Pufferfish#Tween Two Surfaces Along Curve (Twn2SrfsCrv)|Tween Two Surfaces Along Curve (Twn2SrfsCrv)]] — Interpola (tween) entre dos superficies a lo largo de una curva guía (u opcionalmente de dos curvas guía)…

### Pufferfish › Transform (5)

- [[Catálogo - Pufferfish#Morph To Twisted Box (Morph2Tbox)|Morph To Twisted Box (Morph2Tbox)]] — Deforma (morph) geometrías desde cajas de referencia hacia cajas torcidas objetivo. (*Solo Rhino 6; en Rhino…
- [[Catálogo - Pufferfish#Transform Twisted Box (TranTBox)|Transform Twisted Box (TranTBox)]] — Transforma una caja torcida (porque las cajas torcidas no funcionan con los componentes de transformación…
- [[Catálogo - Pufferfish#Tween Consecutive Transforms (TwnConTrans)|Tween Consecutive Transforms (TwnConTrans)]] — Interpola (tween) consecutivamente entre un conjunto de transformaciones
- [[Catálogo - Pufferfish#Tween Through Transforms (TwnThruTrans)|Tween Through Transforms (TwnThruTrans)]] — Interpola (tween) a través de un conjunto de transformaciones
- [[Catálogo - Pufferfish#Tween Two Transforms (Twn2Trans)|Tween Two Transforms (Twn2Trans)]] — Interpola (tween) entre dos transformaciones

### Pufferfish › Twisted Box (48)

- [[Catálogo - Pufferfish#2Pt Twisted Box (2PtTBox)|2Pt Twisted Box (2PtTBox)]] — Crea una caja torcida definida por 2 puntos
- [[Catálogo - Pufferfish#Average Twisted Box (AvrTBox)|Average Twisted Box (AvrTBox)]] — Calcula el promedio aritmético de un conjunto de cajas torcidas
- [[Catálogo - Pufferfish#Center Twisted Box (CenTBox)|Center Twisted Box (CenTBox)]] — Crea una caja torcida centrada en un plano
- [[Catálogo - Pufferfish#Construct Twisted Box (CoTBox)|Construct Twisted Box (CoTBox)]] — Construye una caja torcida a partir de un conjunto de 8 puntos de esquina
- [[Catálogo - Pufferfish#Deconstruct Twisted Box (DeTBox)|Deconstruct Twisted Box (DeTBox)]] — Descompone una caja torcida en sus 8 puntos de esquina, 12 líneas de arista o 6 polilíneas de cara
- [[Catálogo - Pufferfish#Deform Twisted Box (DeformTBox)|Deform Twisted Box (DeformTBox)]] — Deforma una caja torcida moviendo sus puntos de esquina con vectores de movimiento
- [[Catálogo - Pufferfish#Domain Twisted Box (DomTBox)|Domain Twisted Box (DomTBox)]] — Crea una caja torcida definida por un plano base y dominios de tamaño
- [[Catálogo - Pufferfish#Evaluate Twisted Box (EvalTBox)|Evaluate Twisted Box (EvalTBox)]] — Ubica un punto dentro o sobre una caja torcida, evaluado en el espacio normalizado {uvw}
- [[Catálogo - Pufferfish#Mesh Boolean Twisted Boxes (MshBoolTBoxs)|Mesh Boolean Twisted Boxes (MshBoolTBoxs)]] — Recorta (quita) un conjunto de cajas torcidas mediante una intersección o diferencia booleana con una o…
- [[Catálogo - Pufferfish#Mesh Trim Twisted Boxes (MshTrimTBoxs)|Mesh Trim Twisted Boxes (MshTrimTBoxs)]] — Recorta (quita) las partes de un conjunto de cajas torcidas que están a un lado de una malla. [Multihilo]
- [[Catálogo - Pufferfish#Plane Trim Twisted Boxes (PlnTrimTBoxs)|Plane Trim Twisted Boxes (PlnTrimTBoxs)]] — Recorta (quita) las partes de un conjunto de cajas torcidas que están a un lado de un plano. [Multihilo]
- [[Catálogo - Pufferfish#Polysurface Boolean Twisted Boxes (PsrfBoolTBoxs)|Polysurface Boolean Twisted Boxes (PsrfBoolTBoxs)]] — Recorta (quita) un conjunto de cajas torcidas mediante una intersección o diferencia booleana con una o…
- [[Catálogo - Pufferfish#Reference Twisted Box (RefTBox)|Reference Twisted Box (RefTBox)]] — Crea una caja torcida a partir de una polisuperficie (Brep) tipo caja referenciada desde Rhino, con 6 caras y…
- [[Catálogo - Pufferfish#Subdivide Twisted Box (SubDivTBox)|Subdivide Twisted Box (SubDivTBox)]] — Subdivide de forma recursiva una caja torcida en cajas torcidas más pequeñas
- [[Catálogo - Pufferfish#Surface Trim Twisted Boxes (SrfTrimTBoxs)|Surface Trim Twisted Boxes (SrfTrimTBoxs)]] — Recorta (quita) las partes de un conjunto de cajas torcidas que están a un lado de una superficie. [Multihilo]
- [[Catálogo - Pufferfish#Thicken Twisted Box (ThickTBox)|Thicken Twisted Box (ThickTBox)]] — Da espesor a una caja torcida con capas de cajas torcidas, según parámetros que dividen el dominio del espesor
- [[Catálogo - Pufferfish#Tween Consecutive Twisted Boxes (TwnConTBoxs)|Tween Consecutive Twisted Boxes (TwnConTBoxs)]] — Interpola (tween) consecutivamente entre un conjunto de cajas torcidas
- [[Catálogo - Pufferfish#Tween Through Twisted Boxes (TwnThruTBoxs)|Tween Through Twisted Boxes (TwnThruTBoxs)]] — Interpola (tween) a través de un conjunto de cajas torcidas
- [[Catálogo - Pufferfish#Tween Two Twisted Boxes (Twn2TBoxs)|Tween Two Twisted Boxes (Twn2TBoxs)]] — Interpola (tween) entre dos cajas torcidas
- [[Catálogo - Pufferfish#Twisted Box Array (TBoxArray)|Twisted Box Array (TBoxArray)]] — Crea un arreglo en capas de cajas torcidas conectadas dentro de una caja, según parámetros que dividen su…
- [[Catálogo - Pufferfish#Twisted Box Centers (TBoxCents)|Twisted Box Centers (TBoxCents)]] — Busca el punto central (promedio) de los puntos de esquina, líneas de arista o polilíneas de cara de una caja…
- [[Catálogo - Pufferfish#Twisted Box Consecutive Curves (TBoxConCrvs)|Twisted Box Consecutive Curves (TBoxConCrvs)]] — Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre curvas, según un espesor y…
- [[Catálogo - Pufferfish#Twisted Box Consecutive Meshes (TBoxConMshs)|Twisted Box Consecutive Meshes (TBoxConMshs)]] — Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre un conjunto de mallas a partir…
- [[Catálogo - Pufferfish#Twisted Box Consecutive Surfaces (TBoxConSrfs)|Twisted Box Consecutive Surfaces (TBoxConSrfs)]] — Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre un conjunto de superficies…
- [[Catálogo - Pufferfish#Twisted Box Corners (TBox Corners)|Twisted Box Corners (TBox Corners)]] — Obtiene las 8 esquinas de una caja torcida
- [[Catálogo - Pufferfish#Twisted Box Curve (TBoxCrv)|Twisted Box Curve (TBoxCrv)]] — Crea cajas torcidas conectadas a lo largo de una curva, según parámetros que dividen el dominio
- [[Catálogo - Pufferfish#Twisted Box Curve Variable (TBoxCrvVar)|Twisted Box Curve Variable (TBoxCrvVar)]] — Crea cajas torcidas conectadas a lo largo de una curva, según parámetros que dividen el dominio, con tamaños…
- [[Catálogo - Pufferfish#Twisted Box Extrude (TBoxExtr)|Twisted Box Extrude (TBoxExtr)]] — Crea cajas torcidas conectadas a partir de una curva o superficie de perfil, a lo largo de un vector, una…
- [[Catálogo - Pufferfish#Twisted Box Loft (TBoxLoft)|Twisted Box Loft (TBoxLoft)]] — Crea cajas torcidas entre curvas o superficies de sección
- [[Catálogo - Pufferfish#Twisted Box Mesh (TBoxMsh)|Twisted Box Mesh (TBoxMsh)]] — Crea un arreglo en capas de cajas torcidas conectadas sobre una malla, a partir de sus caras y un espesor…
- [[Catálogo - Pufferfish#Twisted Box Pipe (TBoxPipe)|Twisted Box Pipe (TBoxPipe)]] — Crea cajas torcidas conectadas por el interior de una superficie tipo tubo, según parámetros que dividen el…
- [[Catálogo - Pufferfish#Twisted Box Pipe Variable (TBoxPipeVar)|Twisted Box Pipe Variable (TBoxPipeVar)]] — Crea cajas torcidas conectadas por el interior de una superficie tipo tubo, con un conjunto separado de…
- [[Catálogo - Pufferfish#Twisted Box Strip (TBoxStrip)|Twisted Box Strip (TBoxStrip)]] — Crea cajas torcidas conectadas a lo largo de dos curvas de riel, según parámetros que dividen el dominio
- [[Catálogo - Pufferfish#Twisted Box Strip Variable (TTBoxStripVar)|Twisted Box Strip Variable (TTBoxStripVar)]] — Crea cajas torcidas conectadas a lo largo de dos curvas de riel, con un conjunto separado de parámetros de…
- [[Catálogo - Pufferfish#Twisted Box Strips (TBoxStrips)|Twisted Box Strips (TBoxStrips)]] — Crea cajas torcidas conectadas a lo largo de un conjunto de curvas de riel, según parámetros que dividen el…
- [[Catálogo - Pufferfish#Twisted Box Surface (TBoxSrf)|Twisted Box Surface (TBoxSrf)]] — Crea un arreglo en capas de cajas torcidas conectadas sobre una superficie, según un espesor y parámetros que…
- [[Catálogo - Pufferfish#Twisted Box Sweep (TBoxSweep)|Twisted Box Sweep (TBoxSweep)]] — Crea cajas torcidas conectadas a lo largo de cuatro curvas de riel, según parámetros que dividen el dominio
- [[Catálogo - Pufferfish#Twisted Box Sweep Variable (TBoxSweepVar)|Twisted Box Sweep Variable (TBoxSweepVar)]] — Crea cajas torcidas conectadas a lo largo de cuatro curvas de riel, con un conjunto separado de parámetros de…
- [[Catálogo - Pufferfish#Twisted Box Through Curves (TBoxThruCrvs)|Twisted Box Through Curves (TBoxThruCrvs)]] — Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de curvas, según un espesor y…
- [[Catálogo - Pufferfish#Twisted Box Through Meshes (TBoxThruMshs)|Twisted Box Through Meshes (TBoxThruMshs)]] — Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de mallas a partir de sus…
- [[Catálogo - Pufferfish#Twisted Box Through Surfaces (TBoxThruSrfs)|Twisted Box Through Surfaces (TBoxThruSrfs)]] — Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de superficies, según…
- [[Catálogo - Pufferfish#Twisted Box Tube (TBoxTube)|Twisted Box Tube (TBoxTube)]] — Crea un arreglo tubular en capas de cajas torcidas conectadas a lo largo de una curva, según parámetros que…
- [[Catálogo - Pufferfish#Twisted Box Tube Variable (TBoxTubeVar)|Twisted Box Tube Variable (TBoxTubeVar)]] — Crea un arreglo tubular en capas de cajas torcidas conectadas a lo largo de una curva, según parámetros que…
- [[Catálogo - Pufferfish#Twisted Box Two Curves (TBox2Crvs)|Twisted Box Two Curves (TBox2Crvs)]] — Crea un arreglo en capas de cajas torcidas conectadas entre dos curvas, según un espesor y parámetros que…
- [[Catálogo - Pufferfish#Twisted Box Two Meshes (TBox2Mshs)|Twisted Box Two Meshes (TBox2Mshs)]] — Crea un arreglo en capas de cajas torcidas conectadas entre dos mallas a partir de sus caras; funciona con…
- [[Catálogo - Pufferfish#Twisted Box Two Surfaces (TBox2Srfs)|Twisted Box Two Surfaces (TBox2Srfs)]] — Crea un arreglo en capas de cajas torcidas conectadas entre dos superficies, según parámetros que dividen el…
- [[Catálogo - Pufferfish#Twisted Box Volume (TBoxVol)|Twisted Box Volume (TBoxVol)]] — Calcula las propiedades de volumen de una caja torcida
- [[Catálogo - Pufferfish#Weighted Average Twisted Box (WavTBox)|Weighted Average Twisted Box (WavTBox)]] — Calcula el promedio aritmético ponderado de un conjunto de cajas torcidas

### Pufferfish › Vector (3)

- [[Catálogo - Pufferfish#Tween Consecutive Vectors (TwnConVecs)|Tween Consecutive Vectors (TwnConVecs)]] — Interpola (tween) consecutivamente entre un conjunto de vectores
- [[Catálogo - Pufferfish#Tween Through Vectors (TwnThruVecs)|Tween Through Vectors (TwnThruVecs)]] — Interpola (tween) a través de un conjunto de vectores
- [[Catálogo - Pufferfish#Tween Two Vectors (Twn2Vecs)|Tween Two Vectors (Twn2Vecs)]] — Interpola (tween) entre dos vectores

<!-- AUTO:fin -->
