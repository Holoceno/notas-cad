---
title: "Catálogo Grasshopper — Vector"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Vector"
libraries: ["Field Components 8.35.26251.13001", "IO Components 8.35.26251.13001", "Triangulation Components 8.35.26251.13001", "Vector Components 8.35.26251.13001"]
components: 74
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, geometria/puntos-vectores, geometria/patrones]
---

# Vector

74 objetos · librería: Field Components 8.35.26251.13001, IO Components 8.35.26251.13001, Triangulation Components 8.35.26251.13001, Vector Components 8.35.26251.13001 · autor: Robert McNeel & Associates

Mapas: [[Mapa - Puntos, vectores y planos]] (74) · [[Mapa - Patrones y teselados]] (8)

## Field

### Break Field (BreakF)

Separa un campo en sus elementos individuales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo a separar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fields | `F` | Field | lista | Campos elementales |

### Direction Display (FDir)

Muestra las direcciones de fuerza de una sección de un campo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo a evaluar |
| Section | `S` | Rectangle | item | Rectángulo que describe la sección |
| Samples | `N` | Integer | item | Indicador de cantidad de muestras de la sección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Display | `D` | Mesh | item | Malla de visualización de la sección |

### Evaluate Field (EvF)

Evalúa un campo en un punto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo a evaluar |
| Point | `P` | Point | item | Punto en el que evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tensor | `T` | Vector | item | Tensor del campo en la ubicación de muestra |
| Strength | `S` | Number | item | Intensidad del campo en la ubicación de muestra |

### Field Line (FLine)

Calcula la línea de campo que pasa por cierto punto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo a evaluar |
| Point | `P` | Point | item | Punto desde el que partir |
| Steps | `N` | Integer | item | Cantidad de muestras |
| Accuracy | `A` | Number | item | Sugerencia de precisión (solo se respeta aproximadamente) |
| Method | `M` | Integer | item | Solver (1=Euler, 2=RK2, 3=RK3, 4=RK4) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva que aproxima la línea de campo que pasa por P |

### Line Charge (LCharge)

Crea un campo generado por una carga lineal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Geometría del segmento de línea cargado |
| Charge | `C` | Number | item | Carga del objeto punto |
| Bounds *(opcional)* | `B` | Box | item | Límites opcionales del campo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo generado por la carga lineal |

### Merge Fields (MergeF)

Fusiona una colección de campos en uno

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fields | `F` | Field | lista | Campos a fusionar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo fusionado |

### Perpendicular Display (FPerp)

Muestra la perpendicularidad de un campo a través de una sección

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo a evaluar |
| Section | `S` | Rectangle | item | Rectángulo que describe la sección |
| Samples | `N` | Integer | item | Indicador de cantidad de muestras de la sección |
| Positive Colour | `C+` | Colour | item | Color para las fuerzas positivas (hacia arriba) |
| Negative Colour | `C-` | Colour | item | Color para las fuerzas negativas (hacia abajo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Display | `D` | Mesh | item | Malla de visualización de la sección |

### Point Charge (PCharge)

Crea un campo generado por una carga puntual

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Ubicación de la carga puntual |
| Charge | `C` | Number | item | Carga del objeto punto |
| Decay | `D` | Number | item | Decaimiento del potencial de la carga |
| Bounds *(opcional)* | `B` | Box | item | Límites opcionales del campo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo generado por la carga puntual |

### Scalar Display (FScalar)

Muestra los valores escalares de una sección de un campo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo a evaluar |
| Section | `S` | Rectangle | item | Rectángulo que describe la sección |
| Samples | `N` | Integer | item | Indicador de cantidad de muestras de la sección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Display | `D` | Mesh | item | Malla de visualización de la sección |

### Spin Force (FSpin)

Crea un campo generado por una fuerza de giro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Centro y orientación del disco de giro |
| Strength | `S` | Number | item | Intensidad de la fuerza de giro en el centro del disco |
| Radius | `R` | Number | item | Unidad de radio del disco de giro |
| Decay | `D` | Number | item | Decaimiento de la fuerza de giro |
| Bounds *(opcional)* | `B` | Box | item | Límites opcionales del campo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo generado por la fuerza vectorial |

### Tensor Display (FTensor)

Muestra los vectores tensores de una sección de un campo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo a evaluar |
| Section | `S` | Rectangle | item | Rectángulo que describe la sección |
| Samples | `N` | Integer | item | Indicador de cantidad de muestras de la sección |

### Vector Force (FVector)

Crea un campo generado por una fuerza vectorial

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Geometría del segmento de línea cargado |
| Bounds *(opcional)* | `B` | Box | item | Límites opcionales del campo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field | `F` | Field | item | Campo generado por la fuerza vectorial |

## Grid

### Hexagonal (HexGrid)

Grilla 2D con celdas hexagonales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño del radio del hexágono |
| Extent X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección x del plano base |
| Extent Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Curve | árbol | Contornos de las celdas de la grilla |
| Points | `P` | Point | árbol | Puntos en los centros de la grilla |

### Populate 2D (Pop2D)

Puebla una región bidimensional con puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Region | `R` | Rectangle | item | Rectángulo que define la región 2D donde insertar los puntos |
| Count | `N` | Integer | item | Cantidad de puntos a agregar |
| Seed | `S` | Integer | item | Semilla aleatoria para la inserción |
| Points *(opcional)* | `P` | Point | lista | Población preexistente opcional |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Population | `P` | Point | lista | Población de puntos insertados |

### Populate 3D (Pop3D)

Puebla una región tridimensional con puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Region | `R` | Box | item | Caja que define la región 3D donde insertar los puntos |
| Count | `N` | Integer | item | Cantidad de puntos a agregar |
| Seed | `S` | Integer | item | Semilla aleatoria para la inserción |
| Points *(opcional)* | `P` | Point | lista | Población preexistente opcional |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Population | `P` | Point | lista | Población de puntos insertados |

### Populate Geometry (PopGeo)

Puebla geometría genérica con puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a poblar (solo curvas, superficies, breps y mallas) |
| Count | `N` | Integer | item | Cantidad de puntos a agregar |
| Seed | `S` | Integer | item | Semilla aleatoria para la inserción |
| Points *(opcional)* | `P` | Point | lista | Población preexistente opcional |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Population | `P` | Point | lista | Población de puntos insertados |

### Radial (RadGrid)

Grilla radial 2D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Distancia entre los anillos concéntricos de la grilla |
| Extent R | `Er` | Integer | item | Cantidad de celdas de la grilla en la dirección radial |
| Extent P | `Ep` | Integer | item | Cantidad de celdas de la grilla en la dirección polar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Curve | árbol | Contornos de las celdas de la grilla |
| Points | `P` | Point | árbol | Puntos en los nodos de la grilla |

### Rectangular (RecGrid)

Grilla 2D con celdas rectangulares

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size X | `Sx` | Number | item | Tamaño de las celdas en la dirección x del plano base |
| Size Y | `Sy` | Number | item | Tamaño de las celdas en la dirección y del plano base |
| Extent X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección x del plano base |
| Extent Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Rectangle | item | Contornos de las celdas de la grilla |
| Points | `P` | Point | árbol | Puntos en las esquinas de la grilla |

### Square (SqGrid)

Grilla 2D con celdas cuadradas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extent X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección x del plano base |
| Extent Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Rectangle | item | Contornos de las celdas de la grilla |
| Points | `P` | Point | árbol | Puntos en las esquinas de la grilla |

### Triangular (TriGrid)

Grilla 2D con celdas triangulares

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de los lados del triángulo |
| Extent X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección x del plano base |
| Extent Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Curve | árbol | Contornos de las celdas de la grilla |
| Points | `P` | Point | árbol | Puntos en los centros de la grilla |

## Plane

### Adjust Plane (PAdjust)

Ajusta un plano a una nueva dirección normal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano a ajustar |
| Normal | `N` | Vector | item | Nueva dirección del eje z del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano ajustado |

### Align Plane (Align)

Aplica la rotación mínima para alinear un plano con un vector guía

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano a enderezar |
| Direction | `D` | Vector | item | Dirección guía del enderezado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano enderezado |
| Angle | `A` | Number | item | Ángulo de rotación |

### Align Planes (Align)

Alinea planos minimizando su rotación en serie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `P` | Plane | lista | Planos a alinear |
| Master *(opcional)* | `M` | Plane | item | Plano maestro opcional (si se omite, el primer plano de P es el maestro). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `P` | Plane | lista | Planos alineados |

### Construct Plane (Pl)

Construye un plano a partir de un punto de origen y los ejes {x}, {y}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Origin | `O` | Point | item | Origen del plano |
| X-Axis | `X` | Vector | item | Dirección del eje X del plano |
| Y-Axis | `Y` | Vector | item | Dirección del eje Y del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano construido |

### Deconstruct Plane (DePlane)

Descompone un plano en sus partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Origin | `O` | Point | item | Punto de origen |
| X-Axis | `X` | Vector | item | Vector del eje X |
| Y-Axis | `Y` | Vector | item | Vector del eje Y |
| Z-Axis | `Z` | Vector | item | Vector del eje Z |

### Flip Plane (PFlip)

Invierte o intercambia los ejes de un plano

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano a ajustar |
| Reverse X | `X` | Boolean | item | Invierte la dirección del eje x |
| Reverse Y | `Y` | Boolean | item | Invierte la dirección del eje y |
| Swap axes | `S` | Boolean | item | Intercambia las direcciones de los ejes x e y |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano invertido |

### Line + Line (LnLn)

Crea un plano a partir de dos segmentos de línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line A | `A` | Line | item | Primera línea de restricción. El origen del plano queda en el inicio de la línea. |
| Line B | `B` | Line | item | Segunda línea de restricción. La línea B debe ser coplanar con la línea A, pero no paralela. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Definición del plano |

### Line + Pt (LnPt)

Crea un plano a partir de una línea y un punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea de restricción. El origen del plano queda en el punto inicial de la línea y el eje x del plano es paralelo a la dirección de la línea. |
| Point | `P` | Point | item | Punto sobre el plano. El punto no debe ser colineal con la línea. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Definición del plano |

### Plane 3Pt (Pl 3Pt)

Crea un plano que pasa por tres puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto de origen |
| Point B | `B` | Point | item | Punto de dirección X |
| Point C | `C` | Point | item | Punto de orientación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Definición del plano |

### Plane Closest Point (CP)

Busca el punto más cercano en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `S` | Point | item | Punto de muestra |
| Plane | `P` | Plane | item | Plano de proyección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto proyectado |
| UV Point | `uv` | Point | item | Coordenadas {uv} del punto proyectado |
| Distance | `D` | Number | item | Distancia con signo entre el punto y el plano |

### Plane Coordinates (PlCoord)

Obtiene las coordenadas de un punto en el sistema de ejes de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de entrada |
| System | `S` | Plane | item | Sistema de coordenadas local |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| X coordinate | `X` | Number | item | Coordenada {x} del punto |
| Y coordinate | `Y` | Number | item | Coordenada {y} del punto |
| Z coordinate | `Z` | Number | item | Coordenada {z} del punto |

### Plane Fit (PlFit)

Ajusta un plano a un conjunto de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a ajustar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Definición del plano |
| Deviation | `dx` | Number | item | Desviación máxima entre los puntos y el plano |

### Plane Normal (Pl)

Crea un plano perpendicular a un vector.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Origin | `O` | Point | item | Origen del plano |
| Z-Axis | `Z` | Vector | item | Dirección del eje Z del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Definición del plano |

### Plane Offset (Pl Offset)

Desplaza (offset) un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Plane | `P` | Plane | item | Plano base para el desplazamiento |
| Offset | `O` | Number | item | Distancia de desplazamiento (a lo largo del eje z del plano base) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano desplazado |

### Plane Origin (Pl Origin)

Cambia el punto de origen de un plano

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| Origin | `O` | Point | item | Nuevo punto de origen del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Definición del plano |

### Rotate Plane (PRot)

Rota un plano alrededor de su eje z

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano a rotar |
| Angle | `A` | Number | item | Rotación (antihoraria) alrededor del eje z del plano, en radianes |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano rotado |

### XY Plane (XY)

Plano XY del mundo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Origin | `O` | Point | item | Origen del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano XY del mundo |

### XZ Plane (XZ)

Plano XZ del mundo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Origin | `O` | Point | item | Origen del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano XZ del mundo |

### YZ Plane (YZ)

Plano YZ del mundo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Origin | `O` | Point | item | Origen del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano YZ del mundo |

## Point

### Barycentric (BCentric)

Crea un punto a partir de coordenadas baricéntricas {u,v,w}

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primer punto de anclaje |
| Point B | `B` | Point | item | Segundo punto de anclaje |
| Point C | `C` | Point | item | Tercer punto de anclaje |
| Coordinate U | `U` | Number | item | Primera coordenada baricéntrica |
| Coordinate V | `V` | Number | item | Segunda coordenada baricéntrica |
| Coordinate W | `W` | Number | item | Tercera coordenada baricéntrica |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en coordenadas baricéntricas |

### Closest Point (CP)

Busca el punto más cercano en una colección de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto desde el que buscar |
| Cloud | `C` | Point | lista | Nube de puntos en la que buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest Point | `P` | Point | item | Punto de [C] más cercano a [P] |
| CP Index | `i` | Integer | item | Índice del punto más cercano |
| Distance | `D` | Number | item | Distancia entre [P] y [C](i) |

### Closest Points (CPs)

Busca los puntos más cercanos en una colección de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto desde el que buscar |
| Cloud | `C` | Point | lista | Nube de puntos en la que buscar |
| Count | `N` | Integer | item | Cantidad de puntos más cercanos a buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest Point | `P` | Point | lista | Punto de [C] más cercano a [P] |
| CP Index | `i` | Integer | lista | Índice del punto más cercano |
| Distance | `D` | Number | lista | Distancia entre [P] y [C](i) |

### Construct Point (Pt)

Construye un punto a partir de coordenadas {xyz}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| X coordinate | `X` | Number | item | Coordenada {x} |
| Y coordinate | `Y` | Number | item | Coordenada {y} |
| Z coordinate | `Z` | Number | item | Coordenada {z} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `Pt` | Point | item | Coordenada del punto |

### Cull Duplicates (CullPt)

Elimina (cull) los puntos que coinciden dentro de una tolerancia

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos sobre los que operar |
| Tolerance | `T` | Number | item | Distancia de tolerancia de proximidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos depurados |
| Indices | `I` | Integer | lista | Mapa de índices de los puntos depurados |
| Valence | `V` | Integer | lista | Cantidad de puntos de entrada que representa este punto de salida |

### Deconstruct (pDecon)

Descompone un punto en sus partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| X component | `X` | Number | item | Componente {x} del punto |
| Y component | `Y` | Number | item | Componente {y} del punto |
| Z component | `Z` | Number | item | Componente {z} del punto |

### Distance (Dist)

Calcula la distancia euclidiana entre dos puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primer punto |
| Point B | `B` | Point | item | Segundo punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Distance | `D` | Number | item | Distancia entre A y B |

### Numbers to Points (Num2Pt)

Convierte una lista de números en una lista de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Números a combinar en puntos |
| Mask | `M` | Coordinate Mask | item | Máscara para componer las coordenadas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Lista ordenada de puntos |

### Point Cloud Attributes (Point Cloud)

Atributos de la nube de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cloud *(opcional)* | `Cloud` | Point Cloud | item | Nube de puntos |
| Locations *(opcional)* | `Locations` | Point | lista | Las ubicaciones de los puntos de la nube de puntos |
| Normals *(opcional)* | `Normals` | Vector | lista | Los vectores normales de la nube de puntos |
| Colours *(opcional)* | `Colours` | Colour | lista | Los colores de la nube de puntos |
| Hidden *(opcional)* | `Hidden` | Boolean | lista | Los indicadores de visibilidad de la nube de puntos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cloud | `Cloud` | Point Cloud | item | Nube de puntos |
| Locations | `Locations` | Point | lista | Las ubicaciones de los puntos de la nube de puntos |
| Normals | `Normals` | Vector | lista | Los vectores normales de la nube de puntos |
| Colours | `Colours` | Colour | lista | Los colores de la nube de puntos |
| Hidden | `Hidden` | Boolean | lista | Los indicadores de visibilidad de la nube de puntos. |

### Point Cloud Closest Point (Point Cloud CP)

Busca el punto más cercano en una nube de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `Point` | Point | item | El punto desde el que buscar |
| Cloud | `Cloud` | Point Cloud | item | Nube de puntos en la que buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest Point | `Closest Point` | Point | item | El punto de la nube más cercano al punto de entrada |
| Index | `Index` | Integer | item | El índice del punto más cercano de la nube |
| Distance | `Distance` | Number | item | La distancia entre el punto más cercano de la nube y el punto de entrada |

### Point Cylindrical (Pt)

Crea un punto a partir de coordenadas cilíndricas {ángulo, radio, elevación}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base plane | `P` | Plane | item | Plano que define el espacio de coordenadas cilíndricas |
| Angle | `A` | Number | item | Ángulo en radianes para la rotación P(x,y) |
| Radius | `R` | Number | item | Radio del cilindro |
| Elevation | `E` | Number | item | Elevación del punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `Pt` | Point | item | Punto en coordenadas cilíndricas |

### Point Groups (PGroups)

Crea grupos de puntos cercanos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a agrupar |
| Distance | `D` | Number | item | Umbral de distancia para incluir en un grupo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Groups | `G` | Point | árbol | Grupos de puntos |
| Indices | `I` | Integer | árbol | Índices de los grupos |

### Point Oriented (Pt)

Crea un punto a partir de coordenadas {u,v,w} de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base plane | `P` | Plane | item | Plano que define el espacio de coordenadas |
| U component | `U` | Number | item | Parámetro U en el plano |
| V component | `V` | Number | item | Parámetro V en el plano |
| W component | `W` | Number | item | Parámetro W en el plano (elevación) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `Pt` | Point | item | Punto en coordenadas orientadas |

### Point Polar (Pt)

Crea un punto a partir de coordenadas polares {phi, theta, desfase}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base plane | `P` | Plane | item | Plano que define el espacio de coordenadas polares |
| XY angle | `xy` | Number | item | Ángulo en radianes para la rotación P(x,y) |
| Z angle | `z` | Number | item | Ángulo en radianes para la rotación P(z) |
| Offset | `d` | Number | item | Distancia de desfase del punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `Pt` | Point | item | Punto en coordenadas polares |

### Points to Numbers (Pt2Num)

Convierte una lista de puntos en una lista de números

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a interpretar |
| Mask | `M` | Coordinate Mask | item | Máscara para extraer las coordenadas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Lista ordenada de coordenadas |

### Project Point (Project)

Proyecta un punto sobre una colección de formas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto a proyectar |
| Direction | `D` | Vector | item | Dirección de proyección |
| Geometry | `G` | Geometry | lista | Geometría sobre la que proyectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto proyectado |
| Index | `I` | Integer | item | Índice del objeto sobre el que se proyectó |

### Pull Point (Pull)

Lleva (pull) un punto hacia distintos tipos de geometría.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto desde el que buscar |
| Geometry | `G` | Geometry | lista | Geometría que atrae |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest Point | `P` | Point | item | Punto de [G] más cercano a [P] |
| Distance | `D` | Number | item | Distancia entre [P] y su proyección sobre [G] |
| Index | `I` | Integer | item | Índice en [G] |

### Reduce Point Cloud (Reduce)

Reduce la cantidad de puntos de una nube de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cloud | `Cloud` | Point Cloud | item | Nube de puntos a reducir |
| Samples | `Samples` | Integer | item | La cantidad de puntos que debe tener la nueva nube |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cloud | `Cloud` | Point Cloud | item | Una submuestra de la nube de puntos original |

### Sort Along Curve (AlongCrv)

Ordena puntos a lo largo de una curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a ordenar |
| Curve | `C` | Curve | item | Curva a lo largo de la cual ordenar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos ordenados |
| Indices | `I` | Integer | lista | Mapa de índices de los puntos |

### Sort Points (Sort Pt)

Ordena puntos por coordenadas euclidianas (primero x, luego y, luego z)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a ordenar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos ordenados |
| Indices | `I` | Integer | lista | Mapa de índices de los puntos |

### To Polar (Polar)

Convierte un punto 3D a coordenadas polares de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto 3D a convertir |
| System | `S` | Plane | item | Plano que define el espacio de coordenadas polares |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Phi | `P` | Number | item | Ángulo plano en radianes (antihorario, a partir del eje X del plano) |
| Theta | `T` | Number | item | Ángulo vertical en radianes |
| Radius | `R` | Number | item | Distancia desde el origen del sistema hasta el punto |

## Vector

### Amplitude (Amp)

Define la amplitud (longitud) de un vector.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector base |
| Amplitude | `A` | Number | item | Valor de amplitud (longitud) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector resultante |

### Angle

Calcula el ángulo entre dos vectores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector A | `A` | Vector | item | Primer vector |
| Vector B | `B` | Vector | item | Segundo vector |
| Plane *(opcional)* | `P` | Plane | item | Plano opcional para un ángulo 2D |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle | `A` | Number | item | Ángulo (en radianes) entre los vectores |
| Reflex | `R` | Number | item | Ángulo reflejo (en radianes) entre los vectores |

### Cross Product (XProd)

Calcula el producto cruz de vectores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector A | `A` | Vector | item | Primer vector |
| Vector B | `B` | Vector | item | Segundo vector |
| Unitize | `U` | Boolean | item | Unitizar la salida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector del producto cruz |
| Length | `L` | Number | item | Longitud del vector |

### Deconstruct Vector (DeVec)

Descompone un vector en sus partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| X component | `X` | Number | item | Componente {x} del vector |
| Y component | `Y` | Number | item | Componente {y} del vector |
| Z component | `Z` | Number | item | Componente {z} del vector |

### Dot Product (DProd)

Calcula el producto punto de vectores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector A | `A` | Vector | item | Primer vector |
| Vector B | `B` | Vector | item | Segundo vector |
| Unitize | `U` | Boolean | item | Unitizar la entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dot product | `D` | Number | item | Producto punto de los vectores |

### Reverse (Rev)

Invierte un vector (lo multiplica por -1).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector invertido |

### Rotate (VRot)

Rota un vector alrededor de un eje.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector a rotar |
| Axis | `X` | Vector | item | Eje de rotación |
| Angle | `A` | Number | item | Ángulo de rotación (en radianes) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector rotado |

### Unit Vector (Unit)

Unitiza un vector.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector unitario |

### Unit X (X)

Vector unitario paralelo al eje {x} del mundo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factor | `F` | Number | item | Multiplicador del vector unitario |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unit vector | `V` | Vector | item | Vector {x} del mundo |

### Unit Y (Y)

Vector unitario paralelo al eje {y} del mundo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factor | `F` | Number | item | Multiplicador del vector unitario |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unit vector | `V` | Vector | item | Vector {y} del mundo |

### Unit Z (Z)

Vector unitario paralelo al eje {z} del mundo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factor | `F` | Number | item | Multiplicador del vector unitario |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unit vector | `V` | Vector | item | Vector {z} del mundo |

### Vector 2Pt (Vec2Pt)

Crea un vector entre dos puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto base |
| Point B | `B` | Point | item | Punto de la punta |
| Unitize | `U` | Boolean | item | Unitizar la salida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector |
| Length | `L` | Number | item | Longitud del vector |

### Vector Length (VLen)

Calcula la longitud (amplitud) de un vector.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector a medir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L` | Number | item | Longitud del vector |

### Vector XYZ (Vec)

Crea un vector a partir de sus componentes {xyz}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| X component | `X` | Number | item | Componente {x} del vector |
| Y component | `Y` | Number | item | Componente {y} del vector |
| Z component | `Z` | Number | item | Componente {z} del vector |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector | `V` | Vector | item | Vector construido |
| Length | `L` | Number | item | Longitud del vector |
