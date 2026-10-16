---
title: "Catálogo Grasshopper — Transform"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Transform"
libraries: ["Grasshopper 1.0.0008", "Kangaroo2 Components 2.5.3", "Surface Components 8.35.26251.13001", "Transform Components 8.35.26251.13001"]
components: 56
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/kangaroo, geometria/transformaciones, geometria/morph]
---

# Transform

56 objetos · librería: Grasshopper 1.0.0008, Kangaroo2 Components 2.5.3, Surface Components 8.35.26251.13001, Transform Components 8.35.26251.13001 · autor: Daniel Piker, Robert McNeel & Associates

Mapas: [[Mapa - Transformaciones]] (36) · [[Mapa - Morph y tween]] (20)

## Affine

### Box Mapping (BoxMap)

Transforma geometría de una caja a otra.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Source | `S` | Box | item | Caja desde la que mapear |
| Target | `T` | Box | item | Caja hacia la que mapear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría mapeada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Camera Obscura (CO)

Transformación de cámara oscura (reflejo respecto de un punto).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Point | `P` | Point | item | Punto de reflejo |
| Factor | `F` | Number | item | Factor de escala |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría reflejada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Orient Direction (Orient)

Orienta un objeto usando solo restricciones de dirección.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Point A | `pA` | Point | item | Punto de referencia |
| Direction A | `dA` | Vector | item | Dirección de referencia |
| Point B | `pB` | Point | item | Punto objetivo |
| Direction B | `dB` | Vector | item | Dirección objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría reorientada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Project

Proyecta un objeto sobre un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Generic Data | item | Geometría a proyectar |
| Plane | `P` | Plane | item | Plano de proyección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría proyectada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Project Along (ProjectA)

Proyecta un objeto sobre un plano en una dirección.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Generic Data | item | Geometría a proyectar |
| Plane | `P` | Plane | item | Plano de proyección |
| Direction | `D` | Vector | item | Dirección de proyección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría proyectada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Rectangle Mapping (RecMap)

Transforma geometría de un rectángulo a otro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Source | `S` | Rectangle | item | Rectángulo desde el que mapear |
| Target | `T` | Rectangle | item | Rectángulo hacia el que mapear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría mapeada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Scale

Escala un objeto de forma uniforme en todas las direcciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Center | `C` | Point | item | Centro del escalado |
| Factor | `F` | Number | item | Factor de escala |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría escalada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Scale NU

Escala un objeto con factores no uniformes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Plane | `P` | Plane | item | Plano base |
| Scale X | `X` | Number | item | Factor de escala en la dirección {x} |
| Scale Y | `Y` | Number | item | Factor de escala en la dirección {y} |
| Scale Z | `Z` | Number | item | Factor de escala en la dirección {z} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría escalada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Shear

Sesga (shear) un objeto según un vector de sesgo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Base | `P` | Plane | item | Plano base |
| Grip | `G` | Point | item | Punto de referencia |
| Target | `T` | Point | item | Punto objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría sesgada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Shear Angle (Shear)

Sesga (shear) un objeto según ángulos de inclinación.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Base | `P` | Plane | item | Plano base |
| Angle X | `Ax` | Number | item | Rotación alrededor del eje {x}, en radianes |
| Angle Y | `Ay` | Number | item | Rotación alrededor del eje {y}, en radianes |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría sesgada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Triangle Mapping (TriMap)

Transforma geometría de un triángulo a otro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Source | `S` | Curve | item | Triángulo desde el que mapear |
| Target | `T` | Curve | item | Triángulo hacia el que mapear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría mapeada |
| Transform | `X` | Transform | item | Datos de la transformación |

## Array

### Box Array (ArrBox)

Crea un arreglo de geometría en caja.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Cell | `C` | Box | item | Celda 3D del arreglo en caja |
| X Count | `X` | Integer | item | Cantidad de elementos del arreglo en la dirección x. |
| Y Count | `Y` | Integer | item | Cantidad de elementos del arreglo en la dirección y. |
| Z Count | `Z` | Integer | item | Cantidad de elementos del arreglo en la dirección z. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría en arreglo |
| Transform | `X` | Transform | lista | Datos de la transformación |

### Curve Array (ArrCurve)

Crea un arreglo de geometría a lo largo de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Curve | `C` | Curve | item | Curva de riel del arreglo |
| Count | `N` | Integer | item | Cantidad de elementos del arreglo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría en arreglo |
| Transform | `X` | Transform | lista | Datos de la transformación |

### Kaleidoscope (KScope)

Aplica una transformación de caleidoscopio a un objeto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Plane | `P` | Plane | item | Plano del caleidoscopio |
| Segments | `S` | Integer | item | Segmentos del caleidoscopio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría reflejada |
| Transform | `X` | Transform | lista | Datos de la transformación |

### Linear Array (ArrLinear)

Crea un arreglo lineal de geometría.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Direction | `D` | Vector | item | Dirección e intervalo del arreglo lineal |
| Count | `N` | Integer | item | Cantidad de elementos del arreglo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría en arreglo |
| Transform | `X` | Transform | lista | Datos de la transformación |

### Polar Array (ArrPolar)

Crea un arreglo polar de geometría.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Plane | `P` | Plane | item | Plano del arreglo polar |
| Count | `N` | Integer | item | Cantidad de elementos del arreglo. |
| Angle | `A` | Number | item | Ángulo de barrido en radianes (antihorario, a partir del eje x del plano) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría en arreglo |
| Transform | `X` | Transform | lista | Datos de la transformación |

### Rectangular Array (ArrRec)

Crea un arreglo rectangular de geometría.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Cell | `C` | Rectangle | item | Celda del arreglo rectangular |
| X Count | `X` | Integer | item | Cantidad de elementos del arreglo en la dirección x. |
| Y Count | `Y` | Integer | item | Cantidad de elementos del arreglo en la dirección y. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría en arreglo |
| Transform | `X` | Transform | lista | Datos de la transformación |

## Euclidean

### Mirror

Refleja (espejo) un objeto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Plane | `P` | Plane | item | Plano de reflejo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría reflejada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Move

Traslada (mueve) un objeto a lo largo de un vector.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Motion | `T` | Vector | item | Vector de traslación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría trasladada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Move Away From (MoveAway)

Traslada (aleja) un objeto de otro objeto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a mover |
| Emitter | `E` | Geometry | item | Geometría de la que alejarse |
| Distance | `D` | Number | item | Distancia a mover (los valores negativos acercan) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría trasladada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Move To Plane (MoveToPlane)

Traslada (mueve) un objeto hasta un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Plane | `P` | Plane | item | Plano objetivo |
| Above | `A` | Boolean | item | Mover cuando está sobre el plano |
| Below | `B` | Boolean | item | Mover cuando está bajo el plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría trasladada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Orient

Orienta un objeto. La orientación a veces se llama "transformación de cambio de base" (ChangeBasis): permite reasignar geometría de un sistema de ejes a otro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Source | `A` | Plane | item | Plano inicial |
| Target | `B` | Plane | item | Plano final |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría reorientada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Rotate

Rota un objeto en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Angle | `A` | Number | item | Ángulo de rotación en radianes |
| Plane | `P` | Plane | item | Plano de rotación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría rotada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Rotate 3D (Rot3D)

Rota un objeto alrededor de un punto central y un vector eje.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Angle | `A` | Number | item | Ángulo de rotación en radianes |
| Center | `C` | Point | item | Centro de rotación |
| Axis | `X` | Vector | item | Eje de rotación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría rotada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Rotate Axis (RotAx)

Rota un objeto alrededor de un eje.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Angle | `A` | Number | item | Ángulo de rotación en radianes |
| Axis | `X` | Line | item | Eje de rotación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría rotada |
| Transform | `X` | Transform | item | Datos de la transformación |

### Rotate Direction (Rotate)

Rota un objeto de una dirección a otra.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría base |
| Center | `C` | Point | item | Punto central de la rotación |
| From | `F` | Vector | item | Dirección inicial |
| To | `T` | Vector | item | Dirección final |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría rotada |
| Transform | `X` | Transform | item | Datos de la transformación |

## Morph

### Bend Deform (Bend)

Deforma una forma doblándola

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a deformar |
| Bending Arc | `B` | Arc | item | Segmento de arco de doblado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada |

### Blend Box (BlendBox)

Crea una caja torcida entre dos superficies.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface A | `Sa` | Surface | item | Primera superficie |
| Domain A | `Da` | Domain² | item | Dominio en la primera superficie |
| Surface B | `Sb` | Surface | item | Segunda superficie |
| Domain B | `Db` | Domain² | item | Dominio en la segunda superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `B` | Twisted Box | item | Caja de mezcla resultante |

### Box Morph (Morph)

Deforma (morph) un objeto dentro de una caja torcida.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Reference | `R` | Box | item | Caja de referencia |
| Target | `T` | Twisted Box | item | Caja objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría trasladada |

### Flow

Realinea objetos de una curva base a una curva objetivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Base | `C0` | Curve | item | Curva base |
| Target | `C1` | Curve | item | Curva objetivo |
| Reverse Base | `R0` | Boolean | item | Si es True, se invierte la dirección de la curva base. |
| Reverse Target | `R1` | Boolean | item | Si es True, se invierte la dirección de la curva objetivo. |
| Stretch | `S` | Boolean | item | Si es True, la longitud de los objetos en la dirección de las curvas cambia para reflejar las dimensiones de las curvas. |
| Rigid | `R` | Boolean | item | La geometría no se deforma al transformarse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada (morph) |

### Maelstrom

Deforma objetos en espiral, como si estuvieran atrapados en un remolino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Plane | `P` | Plane | item | Plano base de la espiral. |
| First | `R0` | Number | item | Primer radio |
| Second | `R1` | Number | item | Segundo radio |
| Angle | `A` | Number | item | Ángulo de enrollado en radianes |
| Rigid | `R` | Boolean | item | La geometría no se deforma al transformarse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada (morph) |

### Map to Surface (Map Srf)

Mapea una curva sobre una superficie mediante sus puntos de control.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a mapear |
| Source | `S` | Surface | item | Superficie base del espacio de coordenadas inicial |
| Target | `T` | Surface | item | Superficie del espacio de coordenadas objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva mapeada |

### Mirror Curve (Mirror)

Refleja una forma en una curva libre.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a reflejar |
| Curve | `C` | Curve | item | Curva de reflejo |
| Tangent | `T` | Boolean | item | Tangente de reflejo (si es True, el reflejo se extiende más allá de los extremos de la curva) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría reflejada |

### Mirror Surface (Mirror)

Refleja geometría en una superficie libre.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a reflejar |
| Surface | `S` | Surface | item | Superficie de reflejo |
| Frame | `F` | Boolean | item | Marco de reflejo (si es True, el reflejo se extiende más allá del borde de la superficie) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría reflejada |

### MorphToMesh (M2M)

Deforma (morph) geometría desde polígonos de referencia hacia celdas con offset de una malla de triángulos, cuadriláteros o ngons

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Generic Data | lista | Geometría a transformar |
| Mesh *(opcional)* | `M` | Mesh | item | Malla de triángulos, cuadriláteros o ngons hacia la que deformar |
| Offsets | `O` | Number | lista | Distancia o distancias por vértice |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría transformada |
| Reference Polygons | `Ref` | Curve | lista | La geometría ubicada dentro de estos polígonos se mapea a las caras de la malla con la misma cantidad de lados |

### Point Deform (PDeform)

Deforma una forma moviendo sus puntos de control de forma individual

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a deformar |
| Points | `P` | Point | lista | Ubicaciones de los puntos de control a deformar. |
| Motion | `M` | Vector | lista | Vector de movimiento para cada punto de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada |

### Spatial Deform (Deform)

Realiza una deformación espacial según una sintaxis espacial personalizada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a deformar |
| Syntax | `S` | Point | lista | Puntos que describen la sintaxis espacial. |
| Forces | `F` | Vector | lista | Fuerzas (una por cada punto del espacio) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada |

### Spatial Deform (custom) (Deform)

Realiza una deformación espacial según una sintaxis espacial personalizada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a deformar |
| Syntax | `S` | Point | lista | Puntos que describen la sintaxis espacial. |
| Forces | `F` | Vector | lista | Fuerzas (una por cada punto del espacio) |
| Falloff | `f` | Text | item | Función de atenuación (para la variable 'x') |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada |

### Splop

Envuelve geometría sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a deformar |
| Plane | `P` | Plane | item | Plano de origen de la deformación |
| Surface | `S` | Surface | item | Superficie sobre la que envolver la geometría |
| Parameter | `uv` | Point | item | Parámetro U,V sobre la superficie usado para orientar |
| Angle | `A` | Number | item | Ángulo de rotación en radianes |
| Rigid | `R` | Boolean | item | La geometría no se deforma al transformarse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada (morph) |

### Sporph

Deforma un objeto desde una superficie de origen hacia una superficie objetivo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Base | `S0` | Surface | item | Superficie base |
| Base UV *(opcional)* | `P0` | Point | item | Parámetro U,V sobre la superficie base usado para orientar. |
| Target | `S1` | Surface | item | Superficie objetivo |
| Target UV *(opcional)* | `P1` | Point | item | Parámetro U,V sobre la superficie objetivo usado para orientar. |
| Rigid | `R` | Boolean | item | La geometría no se deforma al transformarse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada (morph) |

### Stretch

Deforma objetos estirándolos a lo largo de un eje finito.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Axis | `X` | Line | item | Eje de estiramiento |
| Length | `L` | Number | item | Longitud del nuevo eje de estiramiento. |
| Rigid | `R` | Boolean | item | La geometría no se deforma al transformarse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada (morph) |

### Surface Box (SBox)

Crea una caja torcida sobre un parche de superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Domain | `D` | Domain² | item | Dominio de la superficie |
| Height | `H` | Number | item | Altura de la caja de superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `B` | Twisted Box | item | Caja de superficie resultante |

### Surface Morph (SrfMorph)

Deforma (morph) geometría a las coordenadas UVW de una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a deformar |
| Reference | `R` | Box | item | Caja de referencia desde la que mapear |
| Surface | `S` | Surface | item | Superficie sobre la que mapear |
| U Domain | `U` | Domain | item | Extensión U en el espacio de la superficie |
| V Domain | `V` | Domain | item | Extensión V en el espacio de la superficie |
| W Domain | `W` | Domain | item | Extensión W en el espacio de la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada |

### Taper

Deforma objetos acercándolos o alejándolos de un eje

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Axis | `X` | Line | item | Eje de ahusamiento |
| Start | `R0` | Number | item | Radio al inicio del eje de ahusamiento |
| End | `R1` | Number | item | Radio al final del eje de ahusamiento |
| Flat | `F` | Boolean | item | Si es True, se crea un ahusamiento en una dirección y una dimensión. |
| Infinite | `I` | Boolean | item | Si es True, la deformación ocurre en toda la geometría aunque el eje sea más corto. Si es False, la deformación ocurre solo a lo largo del eje. |
| Rigid | `R` | Boolean | item | La geometría no se deforma al transformarse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada (morph) |

### Twist

Deforma objetos torciéndolos alrededor de un eje.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Axis | `X` | Line | item | Eje de torsión |
| Angle | `A` | Number | item | Ángulo de torsión en radianes |
| Infinite | `I` | Boolean | item | Si es True, la deformación es constante en todo el objeto, aunque el eje sea más corto que el objeto. |
| Rigid | `R` | Boolean | item | La geometría no se deforma al transformarse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría deformada (morph) |

### Twisted Box (TBox)

Crea una caja torcida a partir de puntos de esquina.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Point | item | Primera esquina (0,0,0) |
| Corner B | `B` | Point | item | Segunda esquina (1,0,0) |
| Corner C | `C` | Point | item | Tercera esquina (1,1,0) |
| Corner D | `D` | Point | item | Cuarta esquina (0,1,0) |
| Corner E | `E` | Point | item | Quinta esquina (0,0,1) |
| Corner F | `F` | Point | item | Sexta esquina (1,0,1) |
| Corner G | `G` | Point | item | Séptima esquina (1,1,1) |
| Corner H | `H` | Point | item | Última esquina (0,1,1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `B` | Twisted Box | item | Caja torcida que une todas las esquinas |

## Util

### Compound (Comp)

Combina (compone) dos transformaciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `T` | Transform | lista | Transformaciones a combinar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Compound | `X` | Transform | item | Transformación compuesta |

### Group

Agrupa un conjunto de geometría

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría a agrupar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group | `G` | Group | item | Objetos agrupados |

### Inverse Transform (Inverse)

Invierte una transformación.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transform | `T` | Transform | item | Transformación a invertir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transform | `T` | Transform | item | Transformación invertida |

### Merge Group (GMerge)

Fusiona dos conjuntos de geometría

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group A | `A` | Group | item | Primer grupo |
| Group B | `B` | Group | item | Segundo grupo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group | `G` | Group | item | Grupo fusionado |

### Named Group (Group)

Agrupa un conjunto de geometría bajo un nombre

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group *(opcional)* | `G` | Group | item | Grupo de geometría |
| Geometry *(opcional)* | `G` | Geometry | lista | Geometría a agrupar |
| Name *(opcional)* | `N` | Text | item | Nombre del grupo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group | `G` | Group | item | Grupo de geometría |
| Geometry | `G` | Geometry | lista | Geometría del grupo |
| Name | `N` | Text | item | Nombre del grupo |

### Split

Divide una transformación compuesta en sus fragmentos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transform | `T` | Transform | item | Transformación compuesta |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fragments | `F` | Transform | lista | Fragmentos que forman la transformación compuesta |

### Split Group (GSplit)

Divide un grupo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group | `G` | Group | item | Grupo a dividir |
| Indices | `I` | Integer | lista | Índices de división |
| Wrap | `W` | Boolean | item | Envolver (wrap) los índices |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group A | `A` | Group | item | Grupo que incluye todos los índices |
| Group B | `B` | Group | item | Grupo que excluye todos los índices (oculto) |

### Transform

Transforma un objeto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría base |
| Transform | `T` | Transform | item | Transformación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría transformada |

### Transform Matrix (Matrix, parámetro)

Una matriz de transformación de 4x4

Tipo de dato: **Transform**

### Ungroup

Desagrupa un conjunto de geometría

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Group | `G` | Group | item | Grupo a separar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría dentro del conjunto |
