---
title: "Catálogo Grasshopper — Curve"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Curve"
libraries: ["Curve Components 8.35.26251.13001", "Grasshopper 1.0.0008", "Surface Components 8.35.26251.13001", "Vector Components 8.35.26251.13001", "VectorizeGh"]
components: 110
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, geometria/curvas]
---

# Curve

110 objetos · librería: Curve Components 8.35.26251.13001, Grasshopper 1.0.0008, Surface Components 8.35.26251.13001, Vector Components 8.35.26251.13001, VectorizeGh · autor: Robert McNeel & Associates

Mapas: [[Mapa - Curvas]] (110) · [[Mapa - Morph y tween]] (1) · [[Mapa - Brep y sólidos]] (1)

## Analysis

### Closed (Cls)

Prueba si una curva es cerrada o periódica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closed | `C` | Boolean | item | True si la curva es cerrada o periódica |
| Periodic | `P` | Boolean | item | True si la curva es periódica |

### Control Points (CP)

Extrae los puntos de control y los nodos NURBS de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de control de la forma NURBS. |
| Weights | `W` | Number | lista | Pesos de los puntos de control. |
| Knots | `K` | Number | lista | Vector de nodos de la forma NURBS. |

### Control Polygon (CPoly)

Extrae el polígono de control NURBS de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon | `C` | Curve | item | Curva del polígono de control de la curva de entrada, ajustada según su periodicidad. |
| Points | `P` | Point | lista | Puntos del polígono de control. |

### Curvature

Evalúa la curvatura de una curva en un parámetro dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en la curva en {t} |
| Curvature | `K` | Vector | item | Vector de curvatura en {t} |
| Curvature | `C` | Curve | item | Círculo de curvatura en {t} |

### Curvature Graph (CrvGraph)

Dibuja los gráficos de curvatura de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva para mostrar el gráfico de curvatura |
| Density | `D` | Integer | item | Densidad de muestreo del gráfico |
| Scale | `S` | Integer | item | Escala del gráfico |

### Curve Closest Point (Crv CP)

Busca el punto más cercano en una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto a proyectar sobre la curva |
| Curve | `C` | Curve | item | Curva sobre la que proyectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de la curva más cercano al punto base |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva del punto más cercano |
| Distance | `D` | Number | item | Distancia entre el punto base y la curva |

### Curve Domain (CrvDom)

Mide y define el dominio de la curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a medir/modificar |
| Domain *(opcional)* | `D` | Domain | item | Dominio opcional; si se omite, la curva no se modifica. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva con el nuevo dominio. |
| Domain | `D` | Domain | item | Dominio de la curva original. |

### Curve Frame (Frame)

Obtiene el marco de curvatura de una curva en un parámetro dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame | `F` | Plane | item | Marco de la curva en {t} |

### Curve Middle (MidPt)

Obtiene el punto medio de una curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva para el punto medio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Midpoint | `M` | Point | item | Punto medio de la curva |

### Curve Nearest Object (CrvNear)

Busca el objeto más cercano a una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva desde la que buscar |
| Geometry | `G` | Geometry | lista | Formas en las que buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto de la curva más cercano a la forma más próxima |
| Point B | `B` | Point | item | Punto de la forma más próxima más cercano a la curva |
| Index | `I` | Integer | item | Índice de la forma más próxima |

### Curve Proximity (CrvProx)

Busca el par de puntos más cercanos entre dos curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva |
| Curve B | `B` | Curve | item | Segunda curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto de la curva A más cercano a la curva B |
| Point B | `B` | Point | item | Punto de la curva B más cercano a la curva A |
| Distance | `D` | Number | item | Distancia mínima entre las dos curvas |

### Curve Side (Side)

Determina a qué lado de una curva está un punto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva base |
| Point | `P` | Point | item | Punto a medir. |
| Plane *(opcional)* | `Pl` | Plane | item | Plano opcional en el que medir. Si se omite, se usa el plano de la curva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Side | `S` | Integer | item | Lado de la curva en el que se encontró el punto (-1=izquierda, 0=coincidente, +1=derecha). |
| Left | `L` | Boolean | item | Booleano que indica si el punto está a la izquierda de la curva. |
| Right | `R` | Boolean | item | Booleano que indica si el punto está a la derecha de la curva. |

### Deconstruct Arc (DArc)

Obtiene el plano base, el radio y el dominio angular de un arco.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Arc | item | Arco o círculo a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Plane | `B` | Plane | item | Plano base del arco o círculo |
| Radius | `R` | Number | item | Radio del arco o círculo |
| Angle | `A` | Domain | item | Dominio angular (en radianes) del arco |

### Deconstruct Rectangle (DRec)

Obtiene el plano base y los intervalos de los lados de un rectángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Plane | `B` | Plane | item | Plano base del rectángulo |
| X Interval | `X` | Domain | item | Intervalo de tamaño a lo largo del eje X del plano base |
| Y Interval | `Y` | Domain | item | Intervalo de tamaño a lo largo del eje Y del plano base |

### Derivatives (CDiv)

Evalúa las derivadas de una curva en un parámetro dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en la curva en {t} |
| First derivative | `1` | Vector | item | Primera derivada de la curva en t (velocidad) |

### Discontinuity (Disc)

Busca todas las discontinuidades a lo largo de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a analizar |
| Level | `L` | Integer | item | Nivel de discontinuidad a buscar (1=C1, 2=C2, 3=C infinito) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos en las discontinuidades |
| Parameters | `t` | Number | lista | Parámetros de la curva en las discontinuidades |

### End Points (End)

Extrae los puntos extremos de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start | `S` | Point | item | Punto inicial de la curva |
| End | `E` | Point | item | Punto final de la curva |

### Evaluate Curve (Eval)

Evalúa una curva en el parámetro indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en la curva en {t} |
| Tangent | `T` | Vector | item | Vector tangente en {t} |
| Angle | `A` | Number | item | Ángulo (en radianes) entre la curva entrante y la saliente en {t} |

### Evaluate Length (Eval)

Evalúa una curva en un factor de su longitud. El factor se puede dar en unidades de la curva o normalizado. Cambia el parámetro [N] para alternar entre los dos modos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Length | `L` | Number | item | Factor de longitud para evaluar la curva |
| Normalized | `N` | Boolean | item | Si es True, el factor de longitud está normalizado (0.0 ~ 1.0) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en la longitud indicada |
| Tangent | `T` | Vector | item | Vector tangente en la longitud indicada |
| Parameter | `t` | Number | item | Parámetro de la curva en la longitud indicada |

### Extremes (X-tremez)

Busca los extremos (puntos más alto y más bajo) de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva base |
| Plane | `P` | Plane | item | Plano que define la dirección de los extremos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Highest | `H` | Point | item | Punto más alto de la curva. |
| Lowest | `L` | Point | item | Punto más bajo de la curva. |

### Horizontal Frame (HFrame)

Obtiene un marco alineado horizontalmente a lo largo de una curva en un parámetro dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame | `F` | Plane | item | Marco horizontal de la curva en {t} |

### Length (Len)

Mide la longitud de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a medir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L` | Number | item | Longitud de la curva |

### Length Domain (LenD)

Mide la longitud de un subdominio de la curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a medir |
| Domain | `D` | Domain | item | Subdominio de la curva a medir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L` | Number | item | Longitud de la curva en el subdominio |

### Length Parameter (LenP)

Mide la longitud de una curva hasta un parámetro y desde él.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a medir |
| Parameter | `t` | Number | item | Parámetro a lo largo de la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L-` | Number | item | Longitud de la curva desde el inicio hasta el parámetro |
| Length | `L+` | Number | item | Longitud de la curva desde el parámetro hasta el final |

### Perp Frame (PFrame)

Calcula el marco perpendicular (sin torsión) en un parámetro dado de la curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame | `F` | Plane | item | Marco perpendicular de la curva en {t} |

### Planar

Prueba si una curva es plana.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar | `p` | Boolean | item | Planaridad de la curva |
| Plane | `P` | Plane | item | Plano de la curva |
| Deviation | `D` | Number | item | Desviación respecto del plano de la curva |

### Point In Curve (InCurve)

Prueba si un punto está contenido en una curva cerrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto para la prueba de inclusión en la región |
| Curve | `C` | Curve | item | Región de contorno (solo curvas cerradas) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Relationship | `R` | Integer | item | Relación punto/región (0 = fuera, 1 = coincidente, 2 = dentro) |
| Point | `P'` | Point | item | Punto proyectado sobre el plano de la región. |

### Point in Curves (InCurves)

Prueba si un punto está contenido en varias curvas cerradas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto para la prueba de inclusión |
| Curves | `C` | Curve | lista | Regiones de contorno (solo curvas cerradas) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Relationship | `R` | Integer | item | Relación punto/región (0 = fuera, 1 = coincidente, 2 = dentro) |
| Index | `I` | Integer | item | Índice de la primera región que contiene el punto |
| Point | `P'` | Point | item | Punto proyectado sobre el plano de la región. |

### Point On Curve (CurvePoint, parámetro)

Evalúa una curva en una ubicación específica

Tipo de dato: **Point**

### Polygon Center (PCen)

Busca el punto central (promedio) de una polilínea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea a promediar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center(V) | `Cv` | Point | item | Promedio de los vértices de la polilínea. |
| Center(E) | `Ce` | Point | item | Promedio de las aristas de la polilínea |
| Center(A) | `Ca` | Point | item | Centroide del área de la forma de la polilínea |

### Segment Lengths (LenSeg)

Busca los segmentos más corto y más largo de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a medir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shortest Length | `Sl` | Number | item | Longitud del segmento más corto |
| Shortest Domain | `Sd` | Domain | item | Dominio de la curva del segmento más corto |
| Longest Length | `Ll` | Number | item | Longitud del segmento más largo |
| Longest Domain | `Ld` | Domain | item | Dominio de la curva del segmento más largo |

### Torsion

Evalúa la torsión de una curva en un parámetro dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a evaluar |
| Parameter | `t` | Number | item | Parámetro en el dominio de la curva a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en la curva en {t} |
| Torsion | `T` | Number | item | Torsión de curvatura en {t} |

## Division

### Contour (ex) (Contour)

Crea un conjunto de contornos de una curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a contornear |
| Plane | `P` | Plane | item | Plano base de los contornos |
| Offsets *(opcional)* | `O` | Number | lista | Desfases de los contornos desde el plano base (si se omiten, debes indicar distancias) |
| Distances *(opcional)* | `D` | Number | lista | Distancias entre contornos (si se omiten, debes indicar desfases) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Contours | `C` | Point | árbol | Puntos de contorno resultantes (agrupados por sección) |
| Parameters | `t` | Number | árbol | Parámetros de la curva de todos los puntos de contorno |

### Curve Contour (Contour)

Crea un conjunto de contornos de una curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a contornear |
| Point | `P` | Point | item | Punto inicial de los contornos |
| Direction | `N` | Vector | item | Dirección normal de los contornos |
| Distance | `D` | Number | item | Distancia entre contornos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Contours | `C` | Point | árbol | Puntos de contorno resultantes (agrupados por sección) |
| Parameters | `t` | Number | árbol | Parámetros de la curva de todos los puntos de contorno |

### Curve Frames (Frames)

Genera una cantidad de marcos de curva equiespaciados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Count | `N` | Integer | item | Cantidad de segmentos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frames | `F` | Plane | lista | Marcos de la curva |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de división |

### Dash Pattern (Dash)

Convierte una curva en un patrón de trazos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a convertir en trazos |
| Pattern | `Pt` | Number | lista | Una colección de longitudes de trazo y de espacio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dashes | `D` | Curve | lista | Segmentos de trazo |
| Gaps | `G` | Curve | lista | Segmentos de espacio |

### Divide Curve (Divide)

Divide una curva en segmentos de igual longitud

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Count | `N` | Integer | item | Cantidad de segmentos |
| Kinks | `K` | Boolean | item | Divide los segmentos en los quiebres (kinks) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de división |
| Tangents | `T` | Vector | lista | Vectores tangentes en los puntos de división |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de división |

### Divide Distance (DivDist)

Divide una curva con una distancia predefinida entre puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Distance | `D` | Number | item | Distancia entre puntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de división |
| Tangents | `T` | Vector | lista | Vectores tangentes en los puntos de división |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de división |

### Divide Length (DivLength)

Divide una curva en segmentos de una longitud predefinida

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Length | `L` | Number | item | Longitud de los segmentos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de división |
| Tangents | `T` | Vector | lista | Vectores tangentes en los puntos de división |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de división |

### Horizontal Frames (HFrames)

Genera una cantidad de marcos de curva equiespaciados y alineados horizontalmente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Count | `N` | Integer | item | Cantidad de segmentos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frames | `F` | Plane | lista | Marcos de curvatura |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de división |

### Perp Frames (PFrames)

Genera una cantidad de marcos perpendiculares equiespaciados a lo largo de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Count | `N` | Integer | item | Cantidad de segmentos |
| Align | `A` | Boolean | item | Alinear los marcos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frames | `F` | Plane | lista | Marcos de la curva |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de los marcos |

### Shatter

Fragmenta una curva en segmentos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Parameters | `t` | Number | lista | Parámetros en los que dividir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Segments | `S` | Curve | lista | Fragmentos resultantes |

## Primitive

### Arc

Crea un arco definido por un plano base, un radio y un dominio angular.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base del arco |
| Radius | `R` | Number | item | Radio del arco |
| Angle | `A` | Domain | item | Dominio angular en radianes |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Arc | item | Arco resultante |
| Length | `L` | Number | item | Longitud del arco |

### Arc 3Pt (Arc)

Crea un arco que pasa por tres puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto inicial del arco |
| Point B | `B` | Point | item | Punto en el interior del arco |
| Point C | `C` | Point | item | Punto final del arco |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Geometry | item | Arco resultante |
| Plane | `P` | Plane | item | Plano del arco |
| Radius | `R` | Number | item | Radio del arco |

### Arc SED (Arc)

Crea un arco definido por un punto inicial, un punto final y un vector tangente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start | `S` | Point | item | Punto inicial del arco |
| End | `E` | Point | item | Punto final del arco |
| Direction | `D` | Vector | item | Dirección (tangente) en el inicio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Geometry | item | Arco resultante |
| Plane | `P` | Plane | item | Plano del arco |
| Radius | `R` | Number | item | Radio del arco |

### BiArc

Crea un biarco a partir de los puntos extremos y sus tangentes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start Point | `S` | Point | item | Punto inicial del biarco. |
| Start Tangent | `Ts` | Vector | item | Vector tangente en el inicio del biarco. |
| End Point | `E` | Point | item | Punto final del biarco. |
| End Tangent | `Te` | Vector | item | Vector tangente en el final del biarco. |
| Ratio | `R` | Number | item | Proporción del peso de los segmentos del biarco |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First arc | `A1` | Arc | item | Primer segmento de la curva biarco |
| Second arc | `A2` | Arc | item | Segundo segmento de la curva biarco |
| Bi-Arc | `B` | Curve | item | Biarco resultante. |

### Circle (Cir)

Crea un círculo definido por un plano base y un radio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base del círculo |
| Radius | `R` | Number | item | Radio del círculo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo resultante |

### Circle 3Pt (Circle)

Crea un círculo definido por tres puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primer punto del círculo |
| Point B | `B` | Point | item | Segundo punto del círculo |
| Point C | `C` | Point | item | Tercer punto del círculo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo resultante |
| Plane | `P` | Plane | item | Plano del círculo |
| Radius | `R` | Number | item | Radio del círculo |

### Circle CNR (Circle)

Crea un círculo definido por un centro, una normal y un radio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center | `C` | Point | item | Punto central |
| Normal | `N` | Vector | item | Vector normal del plano del círculo |
| Radius | `R` | Number | item | Radio del círculo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo resultante |

### Circle Fit (FCircle)

Ajusta un círculo a una colección de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a ajustar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo resultante |
| Radius | `R` | Number | item | Radio del círculo |
| Deviation | `D` | Number | item | Distancia máxima entre el círculo y los puntos |

### Circle TanTan (CircleTT)

Crea un círculo tangente a dos curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva de la restricción de tangencia |
| Curve B | `B` | Curve | item | Segunda curva de la restricción de tangencia |
| Point | `P` | Point | item | Guía para el punto central del círculo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo resultante |

### Circle TanTanTan (CircleTTT)

Crea un círculo tangente a tres curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva de la restricción de tangencia |
| Curve B | `B` | Curve | item | Segunda curva de la restricción de tangencia |
| Curve C | `C` | Curve | item | Tercera curva de la restricción de tangencia |
| Point | `P` | Point | item | Guía para el punto central del círculo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo resultante |

### Ellipse

Crea una elipse definida por un plano base y dos radios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la elipse |
| Radius 1 | `R1` | Number | item | Radio en la dirección {x} |
| Radius 2 | `R2` | Number | item | Radio en la dirección {y} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ellipse | `E` | Curve | item | Elipse resultante |
| Focus 1 | `F1` | Point | item | Primer foco |
| Focus 2 | `F2` | Point | item | Segundo foco |

### Fit Line (FLine)

Ajusta una línea a una colección de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a ajustar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Segmento de línea |

### InCircle

Crea el círculo inscrito de un triángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Point | item | Primera esquina del triángulo |
| Corner B | `B` | Point | item | Segunda esquina del triángulo |
| Corner C | `C` | Point | item | Tercera esquina del triángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo resultante |
| Plane | `P` | Plane | item | Plano del círculo |
| Radius | `R` | Number | item | Radio del círculo |

### InEllipse

Crea la elipse inscrita (elipse de Steiner) de un triángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Point | item | Primera esquina del triángulo |
| Corner B | `B` | Point | item | Segunda esquina del triángulo |
| Corner C | `C` | Point | item | Tercera esquina del triángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ellipse | `E` | Curve | item | Elipse resultante |
| Plane | `P` | Plane | item | Plano de la elipse |

### Line (Ln)

Crea una línea entre dos puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start Point | `A` | Point | item | Punto inicial de la línea |
| End Point | `B` | Point | item | Punto final de la línea |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Segmento de línea |

### Line 2Plane (Ln2Pl)

Crea una línea entre dos planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea guía. |
| Plane A | `A` | Plane | item | Primer plano a intersectar con la guía. |
| Plane B | `B` | Plane | item | Segundo plano a intersectar con la guía. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Segmento de línea entre A y B |

### Line 4Pt (Ln4Pt)

Crea una línea a partir de cuatro puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea guía. |
| Point A | `A` | Point | item | Primer punto a proyectar sobre la guía. |
| Point B | `B` | Point | item | Segundo punto a proyectar sobre la guía. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Segmento de línea entre A y B |

### Line SDL (Line)

Crea un segmento de línea definido por un punto inicial, una tangente y una longitud.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start | `S` | Point | item | Punto inicial de la línea |
| Direction | `D` | Vector | item | Tangente (dirección) de la línea |
| Length | `L` | Number | item | Longitud de la línea |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Segmento de línea |

### Modified Arc (ModArc)

Crea un arco a partir de otro arco.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Arc | item | Arco base |
| Radius *(opcional)* | `R` | Number | item | Nuevo radio (opcional) |
| Angle *(opcional)* | `A` | Domain | item | Nuevo dominio angular (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Arc | item | Arco modificado |

### Polygon

Crea un polígono, con aristas redondeadas opcionales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base del polígono |
| Radius | `R` | Number | item | Radio del polígono (distancia del centro a la punta). |
| Segments | `S` | Integer | item | Cantidad de segmentos |
| Fillet Radius | `Rf` | Number | item | Radio de fillet de las esquinas del polígono |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon | `P` | Curve | item | Polígono |
| Length | `L` | Number | item | Longitud de la curva del polígono |

### Polygon Edge (PolEdge)

Crea un polígono a partir de una sola arista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge Start | `E0` | Point | item | Punto inicial de la arista del polígono. |
| Edge End | `E1` | Point | item | Punto final de la arista del polígono. |
| Plane Point | `P` | Point | item | Punto en el plano del polígono. |
| Segments | `S` | Integer | item | Cantidad de segmentos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon | `P` | Curve | item | Polígono |
| Centre | `C` | Point | item | Centro del polígono |
| Corner Radius | `Rc` | Number | item | Distancia del centro a una esquina del polígono. |
| Edge Radius | `Rc` | Number | item | Distancia del centro a los puntos medios de las aristas. |

### Rectangle

Crea un rectángulo sobre un plano

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base del rectángulo |
| X Size | `X` | Domain | item | Dimensiones del rectángulo en la dirección X del plano. |
| Y Size | `Y` | Domain | item | Dimensiones del rectángulo en la dirección Y del plano. |
| Radius | `R` | Number | item | Radio de fillet de las esquinas del rectángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Generic Data | item | Rectángulo |
| Length | `L` | Number | item | Longitud de la curva del rectángulo |

### Rectangle 2Pt (Rec 2Pt)

Crea un rectángulo a partir de un plano base y dos puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base del rectángulo |
| Point A | `A` | Point | item | Primera esquina. |
| Point B | `B` | Point | item | Segunda esquina. |
| Radius | `R` | Number | item | Radio de fillet de las esquinas del rectángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Generic Data | item | Rectángulo definido por P, A y B |
| Length | `L` | Number | item | Longitud de la curva del rectángulo |

### Rectangle 3Pt (Rec 3Pt)

Crea un rectángulo a partir de tres puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primera esquina del rectángulo |
| Point B | `B` | Point | item | Segunda esquina del rectángulo |
| Point C | `C` | Point | item | Punto en la arista del rectángulo opuesta a AB |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo definido por A, B y C. |
| Length | `L` | Number | item | Longitud de la curva del rectángulo |

### Tangent Arcs (TArc)

Crea arcos tangentes entre círculos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle A | `A` | Circle | item | Primer círculo base |
| Circle B | `B` | Circle | item | Segundo círculo base |
| Radius | `R` | Number | item | Radio de los arcos tangentes |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc A | `A` | Arc | item | Primera solución de arco tangente |
| Arc B | `B` | Arc | item | Segunda solución de arco tangente |

### Tangent Lines (Tan)

Crea líneas tangentes entre un punto y un círculo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de las líneas tangentes |
| Circle | `C` | Circle | item | Círculo base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tangent 1 | `T1` | Line | item | Tangente principal |
| Tangent 2 | `T2` | Line | item | Tangente secundaria |

### Tangent Lines (Ex) (TanEx)

Crea líneas tangentes exteriores entre círculos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle A | `A` | Circle | item | Primer círculo base |
| Circle B | `B` | Circle | item | Segundo círculo base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tangent 1 | `T1` | Line | item | Tangente exterior principal |
| Tangent 2 | `T2` | Line | item | Tangente exterior secundaria |

### Tangent Lines (In) (TanIn)

Crea líneas tangentes interiores entre círculos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle A | `A` | Circle | item | Primer círculo base |
| Circle B | `B` | Circle | item | Segundo círculo base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tangent 1 | `T1` | Line | item | Tangente interior principal |
| Tangent 2 | `T2` | Line | item | Tangente interior secundaria |

## Spline

### Bezier Span (BzSpan)

Construye un tramo Bézier a partir de los puntos extremos y sus tangentes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start point | `A` | Point | item | Inicio de la curva |
| Start tangent | `At` | Vector | item | Tangente en el inicio |
| End point | `B` | Point | item | Final de la curva |
| End tangent | `Bt` | Vector | item | Tangente en el final |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Tramo Bézier resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### Blend Curve (BlendC)

Crea una curva de mezcla (blend) entre dos curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva para la mezcla |
| Curve B | `B` | Curve | item | Segunda curva para la mezcla |
| Bulge A | `Fa` | Number | item | Factor de abombamiento en A |
| Bulge B | `Fb` | Number | item | Factor de abombamiento en B |
| Continuity | `C` | Integer | item | Continuidad de la mezcla (0=posición, 1=tangencia, 2=curvatura) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Blend | `B` | Curve | item | Curva de mezcla que conecta el final de A con el inicio de B |

### Blend Curve Pt (BlendCPt)

Crea una curva de mezcla (blend) entre dos curvas que pasa por un punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva para la mezcla |
| Curve B | `B` | Curve | item | Segunda curva para la mezcla |
| Point | `P` | Point | item | Punto por el que pasa la mezcla |
| Continuity | `C` | Integer | item | Continuidad de la mezcla (1=tangencia, 2=curvatura) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Blend | `B` | Curve | item | Curva de mezcla que conecta el final de A con el inicio de B, idealmente coincidente con P |

### Catenary (Cat)

Crea una catenaria (cadena colgante) entre dos puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto inicial de la catenaria |
| Point B | `B` | Point | item | Punto final de la catenaria |
| Length | `L` | Number | item | Longitud de la cadena (debe ser mayor que la distancia \|AB\|) |
| Gravity | `G` | Vector | item | Dirección de la gravedad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Catenary | `C` | Curve | item | Cadena catenaria |

### Connect Curves (Connect)

Conecta una secuencia de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas a conectar |
| Continuity | `G` | Integer | item | Continuidad de las mezclas (0=posición, 1=tangencia, 2=curvatura) |
| Close | `L` | Boolean | item | Crea un circuito cerrado con todas las curvas |
| Bulge | `B` | Number | item | Factor de abombamiento de los segmentos de conexión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Segmentos unidos y curvas de conexión |

### Curve On Surface (CrvSrf)

Crea una curva interpolada que pasa por un conjunto de puntos sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| UV coordinates | `uv` | Point | lista | Coordenadas {v} de los puntos de interpolación |
| Closed | `C` | Boolean | item | Curva cerrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva NURBS resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### Geodesic

Construye una geodésica sobre una superficie entre dos puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base de la geodésica |
| Start | `S` | Point | item | Punto inicial de la geodésica |
| End | `E` | Point | item | Punto final de la geodésica |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geodesic | `G` | Curve | item | Geodésica sobre la superficie |

### Interpolate (IntCrv)

Crea una curva interpolada que pasa por un conjunto de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Puntos de interpolación |
| Degree | `D` | Integer | item | Grado de la curva |
| Periodic | `P` | Boolean | item | Curva periódica |
| KnotStyle | `K` | Integer | item | Espaciado de nodos (0=uniforme, 1=cuerda, 2=raíz de la cuerda) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva NURBS resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### Interpolate (t) (IntCrv(t))

Crea una curva interpolada que pasa por un conjunto de puntos, con tangentes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Puntos de interpolación |
| Tangent Start | `Ts` | Vector | item | Tangente en el inicio de la curva |
| Tangent End | `Te` | Vector | item | Tangente en el final de la curva |
| KnotStyle | `K` | Integer | item | Espaciado de nodos (0=uniforme, 1=cuerda, 2=raíz de la cuerda) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva NURBS resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### Iso Curve (Iso)

Construye isocurvas {uv} sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| UV point | `uv` | Point | item | Coordenada {uv} sobre la superficie para extraer la isocurva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Isocurve | `U` | Curve | lista | Isocurvas en la dirección {u} |
| V Isocurve | `V` | Curve | lista | Isocurvas en la dirección {v} |

### Kinky Curve (KinkCrv)

Construye una curva interpolada que pasa por un conjunto de puntos, con un umbral de ángulo de quiebre (kink).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Puntos de interpolación |
| Degree | `D` | Integer | item | Grado de la curva |
| Angle | `A` | Number | item | Umbral de ángulo de quiebre (en radianes) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva NURBS resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### Knot Vector (Knots)

Construye un vector de nodos para una curva NURBS.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Count | `N` | Integer | item | Cantidad de puntos de control. |
| Degree | `D` | Integer | item | Grado de la curva. |
| Periodic | `P` | Boolean | item | Periodicidad de la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Knots | `K` | Number | lista | Vector de nodos NURBS. |

### Nurbs Curve (Nurbs)

Construye una curva NURBS a partir de puntos de control.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Puntos de control de la curva |
| Degree | `D` | Integer | item | Grado de la curva |
| Periodic | `P` | Boolean | item | Curva periódica |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva NURBS resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### Nurbs Curve PWK (NurbCrv)

Construye una curva NURBS a partir de puntos de control, pesos y nodos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de control de la curva |
| Weights *(opcional)* | `W` | Number | lista | Pesos de los puntos de control (opcional) |
| Knots | `K` | Number | lista | Vector de nodos NURBS |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva NURBS resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### PolyArc (PArc)

Crea una policurva formada por segmentos de arco y de línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Coordenadas de los vértices del poliarco |
| Tangent *(opcional)* | `T` | Vector | item | Vector tangente en el inicio (opcional). |
| Closed | `C` | Boolean | item | Cierra la curva poliarco. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| PolyArc | `Crv` | Curve | item | Curva poliarco resultante |

### PolyLine (PLine)

Crea una polilínea que conecta varios puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Puntos de los vértices de la polilínea |
| Closed | `C` | Boolean | item | Cerrar la polilínea |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `Pl` | Curve | item | Polilínea resultante |

### Sub Curve (SubCrv)

Construye una curva a partir de un subdominio de una curva base.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base curve | `C` | Curve | item | Curva base |
| Domain | `D` | Domain | item | Subdominio a extraer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Subcurva resultante |

### Tangent Curve (TanCurve)

Crea una curva que pasa por un conjunto de puntos, con tangentes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Puntos de interpolación |
| Tangents | `T` | Vector | lista | Vectores tangentes de todos los puntos de interpolación |
| Blend | `B` | Number | item | Factor de mezcla |
| Degree | `D` | Integer | item | Grado de la curva (solo se admiten grados impares) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva NURBS resultante |
| Length | `L` | Number | item | Longitud de la curva |
| Domain | `D` | Domain | item | Dominio de la curva |

### Tween Curve (TweenCrv)

Interpola (tween) entre dos curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Curva desde la que interpolar. |
| Curve B | `B` | Curve | item | Curva hacia la que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0=Curve A, 1.0=Curve B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | item | Curva interpolada resultante |

## Util

### Curve To Polyline (ToPoly)

Convierte una curva en una polilínea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a simplificar |
| Tolerance (distance) | `Td` | Number | item | Tolerancia de desviación |
| Tolerance (angle) | `Ta` | Number | item | Tolerancia angular en radianes |
| MinEdge *(opcional)* | `E-` | Number | item | Longitud mínima permitida de segmento (opcional) |
| MaxEdge *(opcional)* | `E+` | Number | item | Longitud máxima permitida de segmento (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Curva convertida |
| Segments | `S` | Integer | item | Cantidad de segmentos de la polilínea |

### Explode

Explota una curva en segmentos más pequeños.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a explotar |
| Recursive | `R` | Boolean | item | Descomposición recursiva hasta que todos los segmentos sean atómicos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Segments | `S` | Curve | lista | Segmentos explotados que forman la curva base |
| Vertices | `V` | Point | lista | Vértices de los segmentos explotados |

### Extend Curve (Ext)

Extiende una curva una distancia dada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a extender |
| Type | `T` | Integer | item | Tipo de extensión (0=línea, 1=arco, 2=suave) |
| Start | `L0` | Number | item | Longitud de extensión en el inicio de la curva |
| End | `L1` | Number | item | Longitud de extensión en el final de la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva extendida |

### Fillet

Aplica fillet a las esquinas agudas de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que aplicar fillet |
| Radius | `R` | Number | item | Radio del fillet |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva con esquinas redondeadas |

### Fillet · 2

Aplica fillet a una curva en un parámetro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que aplicar fillet |
| Parameter | `t` | Number | item | Parámetro de la curva para el fillet |
| Radius | `R` | Number | item | Radio del fillet |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva con fillet |
| Parameter | `t` | Number | item | Parámetro donde finalmente ocurrió el fillet |

### Fillet Distance (Fillet)

Aplica fillet a las esquinas agudas de una curva según una distancia.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que aplicar fillet |
| Distance | `D` | Number | item | Distancia desde la esquina hasta el inicio del fillet |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva con esquinas redondeadas |

### Fit Curve (Fit)

Ajusta una curva a lo largo de otra curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a ajustar |
| Degree *(opcional)* | `D` | Integer | item | Grado de la curva (opcional; si se omite, se usa el grado de entrada) |
| Tolerance *(opcional)* | `Ft` | Number | item | Tolerancia de ajuste (si se omite, se usa la tolerancia del documento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva ajustada |

### Flip Curve (Flip)

Invierte el sentido de una curva, usando una curva guía opcional.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a invertir |
| Guide *(opcional)* | `G` | Curve | item | Curva guía (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva invertida |
| Flag | `F` | Boolean | item | Acción de inversión |

### Join Curves (Join)

Une la mayor cantidad posible de curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas a unir |
| Preserve | `P` | Boolean | item | Conserva la dirección de las curvas de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas unidas y curvas individuales que no se pudieron unir. |

### Offset Curve (Offset)

Aplica offset a una curva con una distancia dada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que aplicar offset |
| Distance | `D` | Number | item | Distancia de offset |
| Plane *(opcional)* | `P` | Plane | item | Plano para la operación de offset |
| Corners | `C` | Integer | item | Tipo de esquina. Valores posibles: ninguna = 0, aguda = 1, redonda = 2, suave = 3, chaflán = 4 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Offsets resultantes |

### Offset Curve Loose (Offset (L))

Aplica offset a los puntos de control de una curva con una distancia dada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que aplicar offset |
| Distance | `D` | Number | item | Distancia de offset |
| Plane *(opcional)* | `P` | Plane | item | Plano para la operación de offset (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Offset resultante |

### Offset on Srf (OffsetS)

Aplica offset a una curva sobre una superficie con una distancia dada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que aplicar offset |
| Distance | `D` | Number | item | Distancia de offset |
| Surface | `S` | Surface | item | Superficie para la operación de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Offsets resultantes |

### Polyline Collapse (PCol)

Colapsa los segmentos cortos de una curva polilínea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Curva polilínea |
| Tolerance | `t` | Number | item | Tolerancia de longitud de segmento |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `Pl` | Curve | item | Polilínea resultante |
| Count | `N` | Integer | item | Cantidad de segmentos colapsados |

### Project Curve (Project)

Proyecta una curva sobre un Brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a proyectar |
| Brep | `B` | Brep | item | Brep sobre el que proyectar |
| Direction | `D` | Vector | item | Dirección de proyección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curvas proyectadas |

### Pull Curve (Pull)

Lleva (pull) una curva sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a llevar |
| Surface | `S` | Surface | item | Superficie hacia la que se lleva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curva llevada sobre la superficie |

### Rebuild Curve (ReB)

Reconstruye una curva con una cantidad específica de puntos de control.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a reconstruir |
| Degree *(opcional)* | `D` | Integer | item | Grado de la curva (opcional; si se omite, se usa el grado de entrada) |
| Count | `N` | Integer | item | Cantidad de puntos de control |
| Tangents | `T` | Boolean | item | Conserva las tangentes de los extremos de la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva reconstruida |

### Reduce (RedPLine)

Reduce una polilínea quitando los vértices menos significativos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea a reducir |
| Tolerance | `T` | Number | item | Tolerancia (desviación permitida entre la original y la reducida) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea reducida |
| Reduction | `R` | Integer | item | Cantidad de vértices quitados en la reducción |

### Seam

Ajusta la costura de una curva cerrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a ajustar |
| Seam | `t` | Number | item | Parámetro de la nueva costura |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva ajustada |

### Simplify Curve (Simplify)

Simplifica una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a simplificar |
| Tolerance *(opcional)* | `t` | Number | item | Tolerancia de desviación (opcional; si se omite, se usa la tolerancia del documento) |
| Angle Tolerance *(opcional)* | `a` | Number | item | Tolerancia angular (opcional; si se omite, se usa la tolerancia del documento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva simplificada |
| Simplified | `S` | Boolean | item | True si la curva se modificó de alguna forma |

### Smooth Polyline (SmoothPLine)

Suaviza los vértices de una curva polilínea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea a suavizar |
| Strength | `S` | Number | item | Intensidad del suavizado (0 = nada, 1 = máximo) |
| Times | `T` | Integer | item | Cantidad de veces que se aplica el suavizado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea suavizada |

### Vectorize

Vectoriza, o calca, un mapa de bits.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Path | `P` | Text | item | Ruta del archivo de imagen. |
| Threshold *(opcional)* | `T` | Number | item | Umbral de brillo de la imagen. Va de 0.0 (negro) a 1.0 (blanco). |
| Speckles *(opcional)* | `S` | Integer | item | Umbral de eliminación de motas de la imagen. Va de 0 a 100. |
| Corners *(opcional)* | `C` | Number | item | Umbral de detección de esquinas. Va de 0.0 (polígonos) a 1.34 (sin esquinas). |
| Tolerance *(opcional)* | `O` | Number | item | Tolerancia de optimización de los segmentos Bézier. Va de 0.0 a 1.0. |
| Border *(opcional)* | `B` | Boolean | item | Incluir la curva del borde. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Crvs` | Curve | lista | Curvas de salida |
