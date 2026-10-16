---
title: "Catálogo Grasshopper — Kangaroo2"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Kangaroo2"
libraries: ["Kangaroo2 Components 2.5.3"]
components: 101
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/kangaroo, simulacion, geometria/mallas]
---

# Kangaroo2

101 objetos · librería: Kangaroo2 Components 2.5.3 · autor: Daniel Piker

Mapas: [[Mapa - Simulación, optimización y ML]] (101) · [[Mapa - Mallas y SubD]] (22) · [[Mapa - Fabricación]] (1)

## Goals-6dof

### AlignFaces

Alinea caras de un par de cuerpos rígidos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| PlaneA *(opcional)* | `PlaneA` | Plane | item | El marco de uno de los cuerpos rígidos |
| PlaneB *(opcional)* | `PlaneB` | Plane | item | El marco del otro cuerpo rígido |
| FaceA *(opcional)* | `FaceA` | Plane | item | El plano del cuerpo A a alinear |
| FaceB *(opcional)* | `FaceB` | Plane | item | El plano del cuerpo B a alinear |
| Flip | `Flip` | Boolean | item | Invierte la dirección relativa de los planos |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| AlignFaces | `A` | Generic Data | item | A |

### Beam

Viga que resiste flexión y torsión

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| StartFrame *(opcional)* | `StartFrame` | Plane | item | El plano en un extremo de la viga, con su eje Z alineado con la dirección de la viga |
| EndFrame *(opcional)* | `EndFrame` | Plane | item | Debe ser paralelo a StartFrame |
| StartNode *(opcional)* | `StartNode` | Plane | item | El plano que define el nodo al que se une el inicio de la viga. Si no se entrega, por defecto se alinea con XY |
| EndNode *(opcional)* | `EndNode` | Plane | item | El plano que define el nodo al que se une el final de la viga. Si no se entrega, por defecto se alinea con XY |
| E | `E` | Number | item | Módulo de Young |
| A | `A` | Number | item | Área de la sección transversal |
| Ix | `Ix` | Number | item | Segundo momento de área respecto de X |
| Iy | `Iy` | Number | item | Segundo momento de área respecto de Y |
| GJ | `GJ` | Number | item | Módulo de corte × constante de torsión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Beam | `B` | Generic Data | item | B |

### Concentric

Alinea los ejes de un par de cuerpos rígidos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| PlaneA *(opcional)* | `PlaneA` | Plane | item | El marco de uno de los cuerpos rígidos |
| PlaneB *(opcional)* | `PlaneB` | Plane | item | El marco del otro cuerpo rígido |
| AxisA | `AxisA` | Line | item | El eje del primer cuerpo |
| AxisB | `AxisB` | Line | item | El eje del otro cuerpo |
| Flip | `Flip` | Boolean | item | Invierte la dirección relativa de los ejes |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Concentric | `C` | Generic Data | item | C |

### RigidBody

Cuerpo rígido (RigidBody)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Part *(opcional)* | `Part` | Generic Data | item | Pieza como malla o Brep |
| Plane *(opcional)* | `Plane` | Plane | item | El marco inicial del cuerpo. Si no se entrega, se usa un plano alineado con XY en el centroide |
| Points *(opcional)* | `Points` | Point | lista | Puntos opcionales a unir al cuerpo rígido |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| RigidBody | `RB` | Generic Data | item | RB |
| Planes | `P` | Plane | item | Los planos de los cuerpos rígidos |

### RigidBodyCollide

Colisión entre un par de cuerpos rígidos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MeshA *(opcional)* | `MeshA` | Mesh | item | MeshA |
| MeshB *(opcional)* | `MeshB` | Mesh | item | MeshB |
| PlaneA *(opcional)* | `PlaneA` | Plane | item | El marco inicial de meshA |
| PlaneB *(opcional)* | `PlaneB` | Plane | item | El marco inicial de meshB |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SolidCollide | `SC` | Generic Data | item | SC |

### RigidPointSet

Un conjunto de puntos que mantienen sus posiciones relativas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `Points` | Point | lista | Conjunto de puntos rígido |
| Plane *(opcional)* | `Plane` | Plane | item | El marco inicial del cuerpo. Si no se entrega, se usa un plano alineado con XY en el centroide |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| RigidBody | `RB` | Generic Data | item | RB |
| Planes | `P` | Plane | item | Los planos de los cuerpos rígidos |

### SolidPlaneCollide

Colisión entre un plano y un sólido

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Solid *(opcional)* | `Solid` | Mesh | item | Sólido |
| SolidPlane *(opcional)* | `SolidPlane` | Plane | item | El marco inicial del sólido |
| CollisionPlane *(opcional)* | `CollisionPlane` | Plane | item | El plano con el que colisionar |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SolidPlaneCollide | `SP` | Generic Data | item | SP |

### Support

Define las condiciones de apoyo de un extremo de viga o de un cuerpo rígido

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame *(opcional)* | `Frame` | Plane | item | El plano a restringir |
| Target *(opcional)* | `Target` | Plane | item | Plano objetivo. Si no se entrega, se usa el marco inicial |
| X | `X` | Boolean | item | Traslación en X |
| Y | `Y` | Boolean | item | Traslación en Y |
| Z | `Z` | Boolean | item | Traslación en Z |
| XX | `XX` | Boolean | item | Rotación respecto de X |
| YY | `YY` | Boolean | item | Rotación respecto de Y |
| ZZ | `ZZ` | Boolean | item | Rotación respecto de Z |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Support | `S` | Generic Data | item | S |

## Goals-Angle

### Angle

Ángulo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| LineA *(opcional)* | `LineA` | Line | item | Primer segmento de línea |
| LineB *(opcional)* | `LineB` | Line | item | Segundo segmento de línea |
| RestAngle *(opcional)* | `RestAngle` | Number | item | Ángulo de reposo en radianes; si no se entrega, se usa el ángulo actual |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle | `A` | Generic Data | item | Salida de Angle |

### AngleSnap (AS)

Ajusta el ángulo entre 2 líneas al múltiplo entero más cercano de un valor dado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| LineA *(opcional)* | `LineA` | Line | item | Primer segmento de línea |
| LineB *(opcional)* | `LineB` | Line | item | Segundo segmento de línea |
| Factor *(opcional)* | `Factor` | Number | item | El ángulo pasa a ser un múltiplo entero de este valor (en radianes) |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle | `A` | Generic Data | item | Salida de Angle |

### ClampAngle

Mantiene el ángulo entre 2 líneas dentro de un rango dado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| LineA *(opcional)* | `LineA` | Line | item | Primer segmento de línea |
| LineB *(opcional)* | `LineB` | Line | item | Segundo segmento de línea |
| UpperLimit | `Upper` | Number | item | Ángulo máximo permitido en radianes |
| LowerLimit | `Lower` | Number | item | Ángulo mínimo permitido en radianes |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ClampAngle | `C` | Generic Data | item | Salida de ClampAngle |

### EqualAngle (EA)

Iguala los ángulos entre varios pares de líneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| LineA *(opcional)* | `LineA` | Line | lista | Primer segmento de línea de cada par |
| LineB *(opcional)* | `LineB` | Line | lista | Segundo segmento de línea de cada par |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| EqualAngle | `EA` | Generic Data | item | Goal EqualAngle |

### G2

Mantiene la continuidad de curvatura entre 2 curvas NURBS

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | 5 puntos: los tres puntos de control del final de la 1.ª curva y los 3 del inicio de la 2.ª curva, con el del medio compartido por ambas |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| G2 | `G2` | Generic Data | item | Goal G2 |

### Rod

Varilla que resiste flexión y estiramiento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `Polyline` | Curve | item | Polilínea a convertir en varilla |
| LengthFactor | `LengthFactor` | Number | item | Longitud objetivo de las aristas como múltiplo de la longitud actual |
| AngleFactor | `AngleFactor` | Number | item | Ángulo objetivo como múltiplo del ángulo actual |
| AxialStrength | `AxialStrength` | Number | item | Intensidad axial |
| BendStrength | `BendStrength` | Number | item | Intensidad de flexión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| R | `R` | Generic Data | lista | salida |

## Goals-Co

### CoCircular

CoCircular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos a hacer coplanares |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CoCircular | `C` | Generic Data | item | Salida de CoCircular |

### CoLinear

CoLinear

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos a hacer colineales |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CoLinear | `C` | Generic Data | item | Salida de CoLinear |

### CoPlanar

CoPlanar

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos a hacer coplanares |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Coplanar | `C` | Generic Data | item | Salida de Coplanar |

### CoSpherical

CoSpherical

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos a hacer coesféricos |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CoSpherical | `C` | Generic Data | item | Salida de CoSpherical |

## Goals-Col

### Collider

Colisiones entre segmentos de línea con grosor y esferas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects *(opcional)* | `Objects` | Generic Data | lista | Líneas o puntos |
| Radii *(opcional)* | `Radii` | Number | lista | Un radio por cada elemento de Objects. También puede ser un solo valor para todos |
| IgnoreA *(opcional)* | `IgnoreA` | Integer | lista | Primer índice de un par a excluir de las colisiones |
| IgnoreB *(opcional)* | `IgnoreB` | Integer | lista | Segundo índice de un par a excluir de las colisiones |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Collider | `C` | Generic Data | item | Salida de Collider |

### CurveCollide (CC)

Colisiones entre curvas cerradas en un plano dado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas cerradas que colisionan |
| Frames *(opcional)* | `F` | Plane | lista | El marco de cada curva (si no se entrega, se usa un plano alineado con WorldXY en el centroide de la curva) |
| PassiveCurves *(opcional)* | `P` | Curve | lista | Curvas pasivas (participan en las colisiones pero no se mueven) |
| BasePlane | `B` | Plane | item | Plano en el que se revisan las colisiones |
| Strength | `S` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Goal | `G` | Generic Data | item | Conecta esto a la entrada GoalObjects de un componente Kangaroo Solver |
| Frames | `F` | Plane | lista | Los planos de cada una de las curvas |

### CurvePointCollide (CPC)

Mantiene un conjunto de puntos fuera o dentro de una curva 2D dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos afectados |
| Curve *(opcional)* | `Curve` | Curve | item | Una curva 2D cerrada |
| Plane | `Pl` | Plane | item | Plano en el que se consideran las colisiones |
| Interior | `In` | Boolean | item | Si es False, los puntos se mantienen fuera de la curva. Si es True, se mantienen dentro |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| S | `S` | Generic Data | item | S |

### ImageCircles (ImgCircles)

Empaquetado de círculos con tamaños según los colores de una imagen

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `Pts` | Point | lista | Ubicaciones iniciales de los centros de los círculos |
| Mesh | `M` | Mesh | item | Malla coloreada: las zonas más oscuras reciben círculos más pequeños |
| Min | `Min` | Number | item | Radio del círculo más pequeño |
| Max | `Max` | Number | item | Radio del círculo más grande |
| Curves *(opcional)* | `Crvs` | Curve | lista | Curvas de colisión opcionales |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ImageCircles | `I` | Generic Data | item | Goal ImageCircles |

### SoftBodyCollide

Colisiones entre una colección de mallas deformables

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes *(opcional)* | `Meshes` | Mesh | lista | Mallas que colisionan entre sí |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SoftBodyCollide | `SB` | Generic Data | item | SB |

### SolidPointCollide (SPC)

Mantiene un conjunto de puntos fuera o dentro de una malla dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos afectados |
| Solid *(opcional)* | `Solid` | Mesh | item | Un sólido cerrado (Brep o malla) |
| Interior | `In` | Boolean | item | Si es False, los puntos se mantienen fuera del sólido. Si es True, se mantienen dentro |
| Unidirectional | `Uni` | Boolean | item | Si es True, la malla se usa solo como entrada y no se ve afectada por las colisiones |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| S | `S` | Generic Data | item | S |

### SphereCollide (SC)

Colisiones entre grandes cantidades de esferas del mismo tamaño

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Lista de puntos en los centros de las esferas que colisionan |
| Radius | `R` | Number | item | El radio de las esferas |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| S | `S` | Generic Data | item | S |

## Goals-Lin

### ClampLength

Mantiene la longitud dentro de límites dados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Curve | item | Línea |
| LowerLimit *(opcional)* | `LowerLimit` | Number | item | La longitud se mantiene sobre este valor |
| UpperLimit *(opcional)* | `UpperLimit` | Number | item | La longitud se mantiene bajo este valor |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Clamp | `C` | Generic Data | item | Clamp |

### ConstantTension (CT)

Un elemento que adapta su rigidez para mantener una fuerza constante

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Curve | item | Línea |
| Strength | `Strength` | Number | item | Intensidad: positiva para tracción, negativa para compresión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ConstantTension | `CT` | Generic Data | item | Salida de ConstantTension |

### Direction

Alinea un segmento de línea con un vector dado o, si no se entrega, con el más cercano de los vectores XYZ del mundo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Line | item | Línea |
| Direction *(opcional)* | `Direction` | Vector | item | Dirección; si no se entrega, se usa el eje ortogonal más cercano |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Direction | `D` | Generic Data | item | Salida de Direction |

### DynamicWeight1d (DW)

Una carga en la dirección Z negativa, cuya magnitud se actualiza según la longitud de la línea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Curve | item | Línea |
| Weight | `W` | Number | item | Peso por unidad de longitud |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| DW | `DW` | Generic Data | item | Salida de DynamicWeight |

### EqualLength

EqualLength

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Curve | lista | Lista de líneas a igualar en longitud |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Equal | `E` | Generic Data | item | Salida de EqualLength |

### Length(Line)

Length(Line)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Curve | item | Línea |
| Length *(opcional)* | `Length` | Number | item | Longitud; si no se entrega, se usa la longitud inicial |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Spring | `S` | Generic Data | item | Salida del resorte (Spring) |

### LengthRatio

Mantiene una proporción fija entre las longitudes de un par de líneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| LineA *(opcional)* | `LineA` | Line | item | Primer segmento de línea |
| LineB *(opcional)* | `LineB` | Line | item | Segundo segmento de línea |
| Ratio *(opcional)* | `Ratio` | Number | item | Longitud B dividida por longitud A |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle | `A` | Generic Data | item | Salida de Angle |

### LengthSnap

Ajusta la longitud a múltiplos enteros de un número dado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Curve | item | Línea |
| Factor *(opcional)* | `Factor` | Number | item | La longitud pasa a ser un múltiplo entero de este valor |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Snap | `S` | Generic Data | item | Salida de Snap |

### PlasticLength (PL)

Intenta conservar la longitud de la línea de forma elástica hasta que se deforma más allá del límite; entonces cambia su longitud de reposo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line *(opcional)* | `Line` | Curve | item | Línea |
| Limit | `L` | Number | item | Distancia máxima de deformación elástica |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Spring | `S` | Generic Data | item | Salida del resorte (Spring) |

## Goals-Mesh

### Conicalize (Conical)

Ajusta una malla de cuadriláteros para que sus vértices sean cónicos, de modo que la malla tenga un offset cara a cara (ver el paper 'The focal geometry of circular and conical meshes'). Úsalo junto con Planarize

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Conicalize | `C` | Generic Data | lista | Salida de Planarize |

### CyclicQuad

Hace que un cuadrilátero tenga una circunferencia circunscrita

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cyclic | `C` | Generic Data | lista | Salida de Cyclic |

### Developablize

Convierte una malla triangular en parches desarrollables con pliegues. Basado en el paper 'Developability of Triangle Meshes' de Stein, Grinspun y Crane

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| D | `D` | Generic Data | lista | salida |

### EdgeLengths

Define las longitudes de las aristas de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Malla a la que definir las longitudes de arista |
| LengthFactor | `LengthFactor` | Number | item | Longitud objetivo de las aristas como múltiplo de la longitud actual |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| EL | `EL` | Generic Data | lista | salida |

### Hinge

Bisagra (Hinge)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| FoldStart *(opcional)* | `FoldStart` | Point | item | FoldStart |
| FoldEnd *(opcional)* | `FoldEnd` | Point | item | FoldEnd |
| Tip1 *(opcional)* | `Tip1` | Point | item | Tip1 |
| Tip2 *(opcional)* | `Tip2` | Point | item | Tip2 |
| RestAngle *(opcional)* | `RestAngle` | Number | item | Ángulo de reposo; si no se entrega, se usa el ángulo actual |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hinge | `H` | Generic Data | item | Salida de Hinge |

### Isothermic (Iso)

Hace que una malla de cuadriláteros sea S-isotérmica, como se describe en el paper 'Quasiisothermic Mesh Layout' de Sechelmann, Rörig y Bobenko

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Una malla de cuadriláteros a hacer isotérmica |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| G | `G` | Generic Data | item | Goals isotérmicos |

### LiveSoap (LS)

Para generar mallas mínimas y CMC (curvatura media nula y constante, respectivamente) que adaptan su conectividad durante la relajación para mantener la calidad de los triángulos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a minimizar |
| UseVolume | `U` | Boolean | item | Si es True, busca una malla CMC con un volumen dado. Si es False, busca una superficie mínima |
| VolumeChange | `V` | Number | item | Diferencia de volumen respecto de la malla inicial. Se ignora si UseVolume es False |
| Strength | `S` | Number | item | Intensidad |
| Reset | `R` | Boolean | item | Reinicia el mallado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| LS | `LS` | Generic Data | item | Salida de LiveSoap |

### NoFoldThrough

Evita que los lados de una bisagra se atraviesen entre sí

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| FoldStart *(opcional)* | `FoldStart` | Point | item | FoldStart |
| FoldEnd *(opcional)* | `FoldEnd` | Point | item | FoldEnd |
| Tip1 *(opcional)* | `Tip1` | Point | item | Tip1 |
| Tip2 *(opcional)* | `Tip2` | Point | item | Tip2 |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| HingeLimit | `H` | Generic Data | item | Salida de HingeLimit |

### Planarize

Planarize

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planarize | `P` | Generic Data | lista | Salida de Planarize |

### PlasticHinge (PH)

Como Hinge, pero plegar más allá del umbral plástico/elástico cambia el ángulo de reposo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| FoldStart *(opcional)* | `FoldStart` | Point | item | FoldStart |
| FoldEnd *(opcional)* | `FoldEnd` | Point | item | FoldEnd |
| Tip1 *(opcional)* | `Tip1` | Point | item | Tip1 |
| Tip2 *(opcional)* | `Tip2` | Point | item | Tip2 |
| RestAngle *(opcional)* | `RestAngle` | Number | item | Ángulo de reposo (en radianes); si no se entrega, se usa el ángulo actual |
| Limit | `Limit` | Number | item | Ángulo máximo de deformación elástica en radianes |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hinge | `H` | Generic Data | item | Salida de Hinge |

### PolygonArea

PolygonArea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline *(opcional)* | `Polyline` | Curve | item | Polilínea |
| Area *(opcional)* | `Area` | Number | item | Área |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | A |

### Pressure

Una fuerza normal a cada triángulo, proporcional a su área

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pressure | `P` | Generic Data | lista | salida |

### Smooth

Smooth

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Smooth | `P` | Generic Data | lista | salida |

### SoapFilm (SG)

Para generar mallas de curvatura media nula

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a minimizar |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SoapFilm | `S` | Generic Data | item | Salida de Soap |

### TangentialSmooth (TSmooth)

Suaviza una malla solo en los planos tangentes locales. Se usa junto con SoapFilm

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | M |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Smooth | `P` | Generic Data | lista | salida |

### TangentIncircles

TangentIncircles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh *(opcional)* | `M` | Mesh | item | Malla triangular |
| Boundary *(opcional)* | `B` | Curve | item | Curva de borde opcional |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| TangentIncircles | `TI` | Generic Data | lista | Salida de TI |

### VertexLoads

Aplica cargas verticales iguales a todos los vértices de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Malla a la que aplicar las cargas |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L | `L` | Generic Data | lista | salida |

### Volume

Define el volumen total de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | M |
| Volume *(opcional)* | `V` | Number | item | Volumen objetivo; si no se entrega, se usa el volumen inicial |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Volume | `V` | Generic Data | item | Salida de Volume |

### Wind

Viento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar el viento |
| WindVector | `W` | Vector | item | Dirección e intensidad del viento |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Wind | `W` | Generic Data | lista | salida |

## Goals-On

### OnCurve

Mantiene un punto sobre una curva dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos a mantener sobre una curva |
| Curve *(opcional)* | `Curve` | Curve | item | Curva |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P | `P` | Generic Data | item | P |

### OnMesh

Mantiene un punto sobre una malla dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos a mantener sobre una malla |
| Mesh *(opcional)* | `Mesh` | Mesh | item | Malla |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P | `P` | Generic Data | item | P |

### OnPlane

Mantiene un punto sobre un plano dado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Puntos a mantener sobre un plano |
| Plane *(opcional)* | `Plane` | Plane | item | Plano (por defecto WorldXY) |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P | `P` | Generic Data | item | P |

## Goals-Pt

### Anchor

Ancla (Anchor)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point *(opcional)* | `P` | Point | item | Punto a anclar |
| Target *(opcional)* | `T` | Point | item | Ubicación hacia la que se tira el ancla. Si se deja vacía, se usa la ubicación inicial. |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | Salida de Anchor |

### AnchorXYZ

Fija un punto solo en los ejes del mundo elegidos. Si necesitas reiniciar la posición inicial, desconecta y vuelve a conectar la entrada Point.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point *(opcional)* | `P` | Point | item | Punto a anclar |
| X | `X` | Boolean | item | True para impedir el movimiento en la dirección X |
| Y | `Y` | Boolean | item | True para impedir el movimiento en la dirección Y |
| Z | `Z` | Boolean | item | True para impedir el movimiento en la dirección Z |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | Salida de Anchor XYZ |

### Bomb (B)

Provoca una explosión después de una cantidad dada de iteraciones

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location *(opcional)* | `Location` | Point | item | El punto que será el centro de la explosión |
| Points *(opcional)* | `Points` | Point | lista | Los puntos afectados por la explosión |
| DetonationTime | `Detonation` | Integer | item | La iteración del solver en la que ocurre la explosión |
| Strength | `Strength` | Number | item | Intensidad |
| Reset | `Reset` | Boolean | item | Conéctalo al mismo botón que conectaste a la entrada reset del componente Solver |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bomb | `B` | Generic Data | item | Goal Bomb |

### Coincident (C)

Equivale a una restricción de longitud cero entre un par de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point0 *(opcional)* | `P0` | Point | item | Punto 0 |
| Point1 *(opcional)* | `P1` | Point | item | Punto 1 |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Coincident | `C` | Generic Data | item | Coincident |

### Floor

Piso (Floor)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Strength *(opcional)* | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Floor | `H` | Generic Data | item | Salida de Floor |

### FloorFriction (Floor)

Piso con fricción estática

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `P` | Point | lista | Puntos sobre los que actúa |
| Limit | `L` | Number | item | Límite; pon 0 para no tener fricción |
| Strength | `S` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Floor | `F` | Generic Data | item | Goal Floor |

### Load

Carga (Load)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point *(opcional)* | `P` | Generic Data | item | Punto (como índice o como Point) |
| Force vector | `FV` | Vector | item | FV |
| Weighting | `W` | Number | item | Factor de ponderación escalar (para la mayoría de los usos puedes dejar el valor por defecto 1.0) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unary | `U` | Generic Data | item | Salida de Unary |

### MagnetSnap (MS)

Une puntos entre sí según su proximidad

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Points` | Point | lista | Lista de puntos entre los que se aplica el ajuste |
| Range | `R` | Number | item | La distancia a la que se activa el ajuste |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| S | `S` | Generic Data | item | S |

### PlasticAnchor

PlasticAnchor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point *(opcional)* | `P` | Point | item | Punto a anclar |
| Limit | `L` | Number | item | Distancia a la que el punto objetivo empieza a deslizarse |
| Strength | `Strength` | Number | item | Intensidad |
| Reset | `R` | Boolean | item | Reinicia las posiciones plásticas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | Salida de A |

### Transform

Mantiene una transformación dada entre 2 puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P0 *(opcional)* | `P0` | Point | item | Primer punto |
| P1 *(opcional)* | `P1` | Point | item | Segundo punto |
| T *(opcional)* | `T` | Transform | item | Transformación de P0 a P1 |
| Strength | `Strength` | Number | item | Intensidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transform | `T` | Generic Data | item | Salida de Transform |

## Main

### BouncySolver

Solver con inercia (momentum)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| GoalObjects *(opcional)* | `GoalObjects` | Generic Data | árbol | GoalObjects |
| Reset | `Reset` | Boolean | item | Reinicio completo (reconstruye por completo la lista de partículas y su indexación) |
| Threshold | `Threshold` | Number | item | Se detiene cuando el movimiento promedio es menor que esto (por defecto 1e-15) |
| Tolerance | `Tolerance` | Number | item | Los puntos a menos de esta distancia se combinan en una sola partícula |
| Damping | `Damping` | Number | item | Valor entre 0 y 1: cuánta velocidad se conserva entre iteraciones |
| Iterations | `Iterations` | Integer | item | Cantidad de iteraciones internas que se hacen por cada salida de resultados |
| On | `On` | Boolean | item | Si es True, Kangaroo sigue iterando hasta alcanzar el valor umbral dado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| I | `I` | Integer | item | Iteraciones |
| V | `V` | Point | lista | V |
| O | `O` | Generic Data | lista | Salidas de GoalFunction |

### Grab

Permite arrastrar partículas de Kangaroo en las vistas de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| On | `On` | Boolean | item | Cuando está activo, arrastra vértices en la vista de Rhino con el botón izquierdo del mouse |
| Strength | `Strength` | Number | item | Intensidad |
| Range | `Range` | Number | item | Distancia máxima desde la que se pueden tomar puntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grab | `G` | Generic Data | item | Conectar a la entrada Goals |

### Show

Mostrar

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| G *(opcional)* | `G` | Generic Data | item | Geometría |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| G | `G` | Generic Data | item | Conectar a la entrada GoalFunctions |

### Soft & Hard Solver (Soft&HardSolver)

Solver con entradas separadas para goals blandos y goals de restricción dura

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SoftGoals *(opcional)* | `SoftGoals` | Generic Data | árbol | Estos goals se cumplen solo si no entran en conflicto con los goals duros |
| HardGoals *(opcional)* | `HardGoals` | Generic Data | árbol | Estos goals prevalecen sobre los goals blandos |
| HardIterations | `HardIterations` | Integer | item | La cantidad de iteraciones duras que se hacen después de cada paso blando |
| SoftMultiplier | `SoftMultiplier` | Number | item | Multiplicador del movimiento blando. Se puede bajar a cero al final si quieres la máxima precisión |
| Reset | `Reset` | Boolean | item | Reinicio completo (reconstruye por completo la lista de partículas y su indexación) |
| Threshold | `Threshold` | Number | item | Se detiene cuando el movimiento promedio es menor que esto (por defecto 1e-15) |
| Tolerance | `Tolerance` | Number | item | Los puntos a menos de esta distancia se combinan en una sola partícula |
| On | `On` | Boolean | item | Si es True, Kangaroo sigue iterando hasta alcanzar el valor umbral dado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| I | `I` | Integer | item | Iteraciones |
| V | `V` | Point | lista | V |
| O | `O` | Generic Data | árbol | Árbol de salida de GoalFunction |

### Solver

El componente principal donde se combinan y aplican los goals

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| GoalObjects *(opcional)* | `GoalObjects` | Generic Data | árbol | GoalObjects |
| Reset | `Reset` | Boolean | item | Reinicio completo (reconstruye por completo la lista de partículas y su indexación) |
| Threshold | `Threshold` | Number | item | Se detiene cuando el movimiento promedio es menor que esto (por defecto 1e-15) |
| Tolerance | `Tolerance` | Number | item | Los puntos a menos de esta distancia se combinan en una sola partícula |
| On | `On` | Boolean | item | Si es True, Kangaroo sigue iterando hasta alcanzar el valor umbral dado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| I | `I` | Integer | item | Iteraciones |
| V | `V` | Point | lista | V |
| O | `O` | Generic Data | árbol | Árbol de salida de GoalFunction |

### StepSolver

Solver que avanza solo cuando se refresca la entrada. Útil para hacer animaciones

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| GoalObjects *(opcional)* | `GoalObjects` | Generic Data | árbol | GoalObjects |
| Tolerance | `Tolerance` | Number | item | Los puntos a menos de esta distancia se combinan en una sola partícula |
| Momentum | `Momentum` | Boolean | item | Si es False, la simulación intenta converger lo más rápido posible. Si es True, la dinámica es más física |
| Damping | `Damping` | Number | item | Valor entre 0 y 1: cuánta velocidad se conserva entre iteraciones. Solo se usa si Momentum está activo |
| SubIterations | `SubIterations` | Integer | item | Cantidad de iteraciones por cuadro |
| Animate | `Animate` | Boolean | item | Si es False, la simulación se reinicia. Si es True, la solución avanza un cuadro cada vez que se recibe esta entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| I | `I` | Integer | item | Iteraciones |
| V | `V` | Point | lista | V |
| O | `O` | Generic Data | lista | Salidas de GoalFunction |

### ZombieSolver

Una versión del componente solver que hace todas las iteraciones internamente y entrega el resultado final

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| GoalObjects *(opcional)* | `GoalObjects` | Generic Data | árbol | GoalObjects |
| Threshold | `Threshold` | Number | item | Se detiene cuando el movimiento promedio es menor que esto (por defecto 1e-10) |
| Tolerance | `Tolerance` | Number | item | Los puntos a menos de esta distancia se combinan en una sola partícula |
| MaxIterations | `MaxIterations` | Integer | item | Si no se alcanza el umbral de energía, se detiene después de esta cantidad de iteraciones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| I | `I` | Integer | item | Iteraciones |
| V | `V` | Point | lista | V |
| O | `O` | Generic Data | lista | Salidas de GoalFunction |

## Mesh

### Bipartite

Intenta asignar un booleano a cada vértice de una malla de modo que ningún par de vértices conectados tenga el mismo valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Integer | item | Asignaciones de los vértices |

### ByParent

Refina una malla, separando las salidas por cara de origen

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a refinar |
| Level | `L` | Integer | item | Nivel de subdivisión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Lista de mallas refinadas |

### Checkerboard

Intenta asignar un booleano a cada cara de una malla de modo que ningún par de caras adyacentes tenga el mismo valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar el patrón de tablero de ajedrez |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Integer | item | Asignaciones de las caras |

### Combine&Clean (Clean)

Combina y limpia una lista de mallas, quitando vértices no usados y duplicados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Mallas a combinar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla limpia y combinada |

### Diagonalize (Diag)

Reemplaza cada arista por una cara nueva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a diagonalizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| DiagonalMesh | `M` | Mesh | item | Malla diagonal |

### FaceFaceOffset (FaceFace)

Aplica offset a una malla cónica de modo que las caras correspondientes queden a distancia constante

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de entrada |
| Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset | `O` | Mesh | item | La malla con offset |
| Beams | `B` | Mesh | item | Vigas entre las 2 mallas |

### FoldAngle

Mide el ángulo actual entre dos triángulos alrededor de su arista común

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P1 | `P1` | Point | item | Inicio de la arista común que comparten ambos triángulos |
| P2 | `P2` | Point | item | Final de la arista común que comparten ambos triángulos |
| P3 | `P3` | Point | item | Punta del primer triángulo |
| P4 | `P4` | Point | item | Punta del segundo triángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle | `A` | Number | item | Ángulo entre los triángulos |

### HingePoints

Obtiene los 4 puntos de cada arista interior para usar en una fuerza Hinge

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de la que obtener los puntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 1 | `1` | Point | lista | Punto 1 |
| 2 | `2` | Point | lista | Punto 2 |
| 3 | `3` | Point | lista | Punto 3 |
| 4 | `4` | Point | lista | Punto 4 |

### MeshCorners (MC)

Extrae las esquinas más agudas que cierto ángulo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Angle | `A` | Number | item | Ángulo interior bajo el cual un vértice se considera esquina |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corners | `C` | Point | lista | Esquinas |

### MeshDirection (MD)

Ordena las direcciones de las caras de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a ordenar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SortedMesh | `M` | Mesh | item | Malla con las direcciones de las caras ordenadas |

### MeshMap

Mapea puntos de una malla a otra

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SourceMesh | `M1` | Mesh | item | Malla desde la que mapear |
| TargetMesh | `M2` | Mesh | item | Malla hacia la que mapear |
| Point | `P` | Point | item | Punto a mapear |
| Distance | `D` | Number | item | Distancia máxima de búsqueda |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto mapeado |

### MeshTurn (Turn)

Rota el orden de los vértices de cada cara

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla cuyas caras se giran |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SortedMesh | `M` | Mesh | item | Malla con las caras giradas |

### NakedVertices (NV)

Ordena los vértices de una malla en 2 listas según estén o no rodeados por caras

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ClothedIndex | `ClothedI` | Integer | item | Índices de los vértices rodeados por caras |
| NakedIndex | `NakedI` | Integer | item | Índices de los vértices no rodeados por caras |
| ClothedPts | `ClothedPts` | Point | item | Ubicaciones de los vértices rodeados por caras |
| NakedPts | `NakedPts` | Point | item | Ubicaciones de los vértices no rodeados por caras |

### PlanarityAnalysis (PA)

Muestra la planaridad de las caras como una malla coloreada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a analizar |
| Max | `X` | Number | item | Valor que se muestra como rojo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| M | `M` | Mesh | item | Malla coloreada según su desviación de la planaridad: verde = plana, rojo = máxima |
| P | `P` | Number | lista | Desviación de planaridad por cara: la distancia más corta entre diagonales dividida por la longitud promedio de las diagonales. |

### Refine

Divide cada cuadrilátero en 4 cuadriláteros y cada triángulo en 4 triángulos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a refinar |
| Level | `L` | Integer | item | Nivel de subdivisión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla refinada |

### RefineStrips (Strips)

Subdivisión direccional: refina los cuadriláteros en una sola dirección

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a refinar |
| Level | `L` | Integer | item | Nivel de subdivisión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla refinada |

### RemeshByColour

Rehace la malla con longitudes de arista que dependen de los colores de los vértices de la malla de entrada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Malla coloreada de entrada |
| LengthInterval | `LengthInterval` | Domain | item | Intervalo de longitud de arista de negro a blanco |
| FixCurves *(opcional)* | `FixC` | Curve | lista | Curvas que se mantienen nítidas durante el remallado. Pueden ser curvas de borde o interiores |
| FixVertices *(opcional)* | `FixV` | Point | lista | Puntos que se mantienen fijos durante el remallado |
| Flip | `Flip` | Integer | item | Criterio para decidir cuándo voltear aristas (0 según la valencia, 1 según el ángulo) |
| Iterations | `Iter` | Integer | item | Cantidad de pasos entre salidas |
| Reset | `Reset` | Boolean | item | True para inicializar, False para ejecutar el remallado. Conecta un timer para remallar continuamente |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Resultado del remallado |

### Stripper

Divide una malla en franjas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Strips | `S` | Mesh | lista | Lista de franjas de malla |

### TangentCircles (TC)

Genera círculos inscritos en las caras, un empaquetado de círculos centrado en los vértices, o el dual por círculos inscritos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Incircles | `I` | Circle | lista | Círculos inscritos |
| Circle Packing | `C` | Circle | lista | C |
| Dual | `D` | Curve | item | Dual basado en los centros de los círculos inscritos |

### Unroller

Desenrolla una franja de cuadriláteros

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Strip | `M` | Mesh | item | Malla a desenrollar (debe ser una franja de cuadriláteros que no se cierre sobre sí misma) |
| Unroll | `T` | Number | item | Cuánto desenrollar (0 mantiene la original, 1 la desenrolla por completo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unrolled | `U` | Mesh | item | Malla desenrollada |

### VertexNeighbours (VN)

Devuelve las posiciones de los vértices conectados por una arista al vértice dado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Vertex number | `V` | Integer | item | El entero del vértice central del que obtener los vecinos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertex | `C` | Point | item | La posición del vértice central |
| Neighbours | `N` | Point | item | Posiciones de los vértices vecinos |
| Normal | `V` | Vector | item | La normal de la malla en el vértice central |

### WarpWeft

Separa las aristas de una malla en 2 listas según la dirección de urdimbre y trama

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Warp | `A` | Line | lista | Líneas en la primera dirección |
| Weft | `B` | Line | lista | Líneas en la primera dirección |
| NakedA | `NA` | Boolean | lista | Lista de booleanos que indica si cada línea de A está en el borde de la malla |
| NakedB | `NB` | Boolean | lista | Lista de booleanos que indica si cada línea de B está en el borde de la malla |

## Utility

### DotDisplay (Dot)

Muestra los puntos como círculos rellenos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Puntos a mostrar |

### interconnectPoints (inter)

Dibuja una línea entre cada par de puntos de una lista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| pts | `P` | Point | lista | Lista de puntos a interconectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| interconnections | `I` | Curve | lista | Líneas de interconexión |

### Möbius Transformation (MB)

Transformaciones de Möbius 3D de cualquier geometría mediante rotación 4D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría de entrada a transformar |
| Circle | `C` | Circle | item | Círculo que define la transformación. Los puntos sobre este círculo se quedan en él, y todos los demás se tiran a través y alrededor de él |
| T | `T` | Number | item | Cantidad de transformación. 2π la devuelve a la original |
| Q | `Q` | Number | item | Este parámetro controla la rotación alrededor del eje del círculo. Pon 1 para rotaciones isoclínicas |
| FixSphere | `F` | Boolean | item | Si es True, transforma y escala la geometría para que los puntos sobre la esfera definida por el círculo de entrada se queden en esa esfera |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría transformada |

### removeDuplicateLines (dupLn)

Quita líneas similares de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| lines | `L` | Line | lista | Lista de líneas a limpiar |
| tolerance *(opcional)* | `t` | Number | item | Las líneas cuyos puntos inicial/final estén a menos de esta distancia se combinan |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| unique lines | `Q` | Line | lista | Lista de líneas únicas |

### removeDuplicatePts (dupPt)

Quita puntos similares de una lista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| points | `P` | Point | lista | Lista de puntos a limpiar |
| tolerance *(opcional)* | `t` | Number | item | Si dos puntos están a menos de esta distancia en todos los ejes x, y y z, se combinan |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| unique points | `Q` | Point | lista | Lista de puntos únicos |

### SplitAtCorners

Divide una polilínea en varias partes según el ángulo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Poly | `P` | Curve | item | La polilínea a dividir |
| Angle | `A` | Number | item | Ángulo en radianes en el que dividir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corners | `C` | Point | lista | Puntos en los que el ángulo superó el umbral |
| Parts | `S` | Curve | lista | Una lista de polilíneas separadas |
