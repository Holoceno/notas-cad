---
title: "Catálogo Grasshopper — Parakeet"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Parakeet"
libraries: ["Parakeet 1.2.0", "Wang Tile 1.2.0"]
components: 184
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/parakeet, geometria/patrones, programacion/scripts, geometria/curvas, geometria/superficies]
---

# Parakeet

184 objetos · librería: Parakeet 1.2.0, Wang Tile 1.2.0 · autor: Esmaeil Mottaghi & Arman Khalilbeigi

Mapas: [[Mapa - Patrones y teselados]] (151) · [[Mapa - Scripts, interfaz y archivos]] (28) · [[Mapa - Curvas]] (25) · [[Mapa - Superficies y NURBS]] (18) · [[Mapa - Brep y sólidos]] (7) · [[Mapa - Mallas y SubD]] (6) · [[Mapa - Fabricación]] (1)

## Curve

### AddOrnament (AddOrn)

Mapea una curva sobre una línea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Curves | `BC` | Curve | item | Curva base |
| Ornament Curves | `OCr` | Curve | lista | Curvas de ornamento |
| Direction | `Dir` | Line | item | La dirección del ornamento |
| parameter | `Pr` | Number | item | La ubicación del ornamento sobre la curva base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Relacate Ornaments | `PO` | Curve | lista | Reubicar ornamentos |

### Align Curves (AlignCrv)

Alinea una lista de curvas según una curva guía, ajustando la costura y la dirección de las curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | item | Curvas a alinear |
| Guide | `G` | Curve | item | Curvas guía |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | item | Curvas alineadas |

### Approx. Convex Hull (ConvexH)

Este componente calcula una Alpha Shape aproximada de un conjunto de puntos 3D con un método de envolvente convexa basado en proyección 2.5D. Ajusta un plano a la nube de puntos de entrada, proyecta los puntos sobre ese plano, construye una envolvente convexa 2D con el algoritmo de envoltura de regalo (gift wrapping) y luego vuelve a proyectarla a 3D.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `Pts` | Point | lista | Lista de puntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ConvexHull | `CH` | Point | item | Puntos de la envolvente convexa aproximada. |

### Complex Transform A (Complex T A)

Aplica una transformación compleja a una red de curvas (llamada de forma imprecisa transformación 4D o hiperbólica)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| BC *(opcional)* | `BC` | Curve | árbol | Curvas base a transformar |
| Xs *(opcional)* | `Xs` | Number | item | Valor de desfase en la dirección X de las curvas |
| Ys *(opcional)* | `Ys` | Number | item | Valor de desfase en la dirección Y de las curvas |
| P *(opcional)* | `P` | Number | item | Potencia compleja (puede ser negativa). Rango sugerido: [-2,2] |
| Md *(opcional)* | `Md` | Integer | item | Un valor entero que determina distintos modos de comportamiento del componente: un número entre 0 y 3 que decide cómo tratar la distancia y la orientación de las curvas base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| TC | `TC` | Curve | item | Curvas transformadas |

### Curve to Arcs and Lines (Curve > Arc/Line)

Convierte una curva en arcos y líneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a convertir en arcos y líneas |
| Tolerance | `T` | Number | item | La tolerancia: la desviación máxima desde los puntos medios de los arcos hasta la curva. En caso de duda, usa la tolerancia absoluta del espacio modelo del documento. |
| Angle tolerance | `AT` | Number | item | La tolerancia angular en radianes: la desviación máxima de la dirección de los extremos de los arcos respecto de la dirección de la curva. En caso de duda, usa la tolerancia angular del espacio modelo del documento. |
| Minimum Length | `minL` | Number | item | La longitud mínima de segmento. |
| Maximuum Length | `maxL` | Number | item | La longitud máxima de segmento. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arcs/Lines | `Cr` | Curve | item | Arcos y líneas convertidos |

### Discontinuity With Threshold (Discontinuity+)

Busca discontinuidades angulares (quiebres G1) a lo largo de una curva usando un umbral de ángulo dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a analizar |
| Angle Threshold | `T` | Number | item | Umbral angular (en grados) para detectar quiebres |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos en las discontinuidades angulares (quiebres) |
| Parameters | `t` | Number | lista | Parámetros de la curva en las discontinuidades |

### Divide Curve Variable (DivideVar)

Divide una curva según su curvatura, con parámetros variables

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Telorance | `T` | Number | item | Distancia máxima entre los puntos generados y la curva |
| Max Edge Count | `ME` | Number | item | Cantidad máxima de segmentos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos |

### Dual Garph (Dual)

Genera el grafo dual de una lista de polígonos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygons | `P` | Curve | lista | Polígonos de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dual Graph | `D` | Curve | lista | Grafo dual como polígonos |

### Extend on surface (Extend Cr)

Extiende una curva sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a extender |
| Surface | `S` | Surface | item | Superficie para la operación de extensión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Extensión resultante |

### FontSelector (fonts)

Lista todas las fuentes instaladas en este equipo. Usa el parámetro Fi para obtener la fuente número 'i' de la lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fi | `Fi` | Integer | item | Índice de la fuente a seleccionar. Ver la salida Fonts para la lista de fuentes disponibles |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fonts | `F` | Text | lista | Lista de todas las fuentes (nombres de familia) disponibles |
| iFont | `iF` | Text | item | Nombre de la fuente seleccionada |

### Graph Coloring (GraphC)

Obtiene un entero por cada punto de la red. La coloración de grafos es un caso especial del etiquetado de grafos: asigna etiquetas a los elementos de un grafo cumpliendo ciertas restricciones. En su forma más simple, colorea los vértices de un grafo de modo que dos vértices adyacentes no tengan el mismo color.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| LP *(opcional)* | `LP` | Integer | árbol | Topología línea-punto (o componente LP Network Topology) como árbol |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| GC | `GC` | Integer | item | Etiquetas del grafo |

### Join Curves Plus (Join Curves +)

Une la mayor cantidad posible de curvas que estén a menos de una distancia

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas a unir |
| Tolerance | `T` | Number | item | Distancia máxima entre curvas para unirlas |
| Preserve | `P` | Boolean | item | Conserva la dirección de las curvas de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `JC` | Curve | lista | Curvas unidas y curvas individuales que no se pudieron unir |

### Loop Trancate (Trancate)

Trunca un patrón (red 2D o 3D de líneas/curvas) de forma recursiva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Patrón a truncar (facetar) [se aceptan patrones 2D y 3D] |
| Distance | `D` | Number | item | Distancia de truncamiento normalizada (entre 0~1) |
| Iteration | `I` | Integer | item | Cantidad de ciclos de truncamiento (preferiblemente menos de 3) |
| Tolerance | `T` | Number | item | Tolerancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trancated Curves | `TC` | Curve | lista | Patrón truncado |

### Map Curves (MapCrv2Crv)

Mapea una colección de polilíneas y curvas de una polilínea a otra. Las polilíneas de origen y destino deben tener la misma cantidad de vértices (o segmentos).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| C *(opcional)* | `C` | Curve | lista | Polilínea(s) a mapear |
| SP *(opcional)* | `SP` | Curve | item | Polilínea desde la que mapear |
| TP *(opcional)* | `TP` | Curve | item | Polilínea sobre la que mapear |
| Mode *(opcional)* | `Mode` | Integer | item | Modo de mapeo: ¿ignorar las diferencias entre el plano 'C' y el plano 'SP'? (0 o 1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MC | `MC` | Curve | item | Polilínea(s) y curvas mapeadas |

### MapToLine (MapToLn)

Mapea una curva sobre una línea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | item | Curvas a mapear |
| Source Line | `SL` | Line | item | Línea desde la que mapear las curvas |
| Target Line | `T` | Line | item | Línea sobre la que mapear las curvas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Curves | `C` | Curve | item | Curvas mapeadas |

### Mirrored Subdivide Quad (QuadSubM)

Subdivide un polígono cerrado en celdas cuadrangulares y refleja las piezas de forma alternada (útil para generar patrones geométricos)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polyline(s) | `B` | Curve | item | Lista de polilíneas cerradas (celdas) a subdividir |
| Mirror? | `M` | Boolean | item | Poner en 'True' para reflejar las celdas subdivididas de forma alternada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Subdivided Cells | `C` | Curve | lista | Celdas subdivididas |

### Network Regions (Region)

Obtiene regiones (áreas cerradas) de una red de curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas entre las que buscar regiones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Regions | `R` | Curve | lista | Curvas de las regiones |

### Network Regions + (Region+)

Obtiene regiones (áreas cerradas) de una red de curvas + datos de half-edge

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| N *(opcional)* | `N` | Point | lista | Lista de puntos de la red (nodos) |
| E *(opcional)* | `E` | Integer | lista | Lista de aristas de la red |
| PP *(opcional)* | `PP` | Integer | árbol | Topología punto-punto (o componente PP Network Topology) como árbol |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rgi | `Rgi` | Integer | item | Lista de índices N de cada región |
| Rgp | `Rgp` | Point | item | Lista de puntos de cada región |
| HE | `HE` | Integer | item | Índice del half-edge. |
| HEp | `HEp` | Integer | item | Índice del par del half-edge |
| HEnext | `HEnext` | Integer | item | Para cada half-edge, el par de índices del half-edge siguiente |
| HEprev | `HEprev` | Integer | item | Para cada half-edge, el par de índices del half-edge anterior |
| VoHE | `VoHE` | Integer | item | Para cada vértice, uno de sus half-edges salientes |
| FoHE | `FoHE` | Integer | item | Para cada cara, uno de sus half-edges salientes |
| HEFace | `HEFace` | Integer | item | Para cada half-edge, una de las caras que lo contiene |

### Network Topology

Obtiene la topología completa de una red de líneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | lista | Red de líneas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Nodes | `N` | Point | lista | Nodos de la red como puntos |
| Edges | `E` | Line | lista | Aristas de la red como líneas |
| Point \| Point Topology | `PP` | Integer | árbol | Para cada punto, índices de los puntos que se conectan a él |
| Point \| Line Topology | `PL` | Integer | árbol | Para cada punto, índices de las líneas que se conectan a él |
| Line \| Point Topology | `LP` | Integer | árbol | Para cada línea, índices de los puntos que se conectan a ella |
| Line \| Line Topology | `LL` | Integer | árbol | Para cada línea, índices de las líneas que se conectan a ella |

### ParaText (text)

Escribe un texto sobre un plano dado y entrega su silueta como una lista de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L *(opcional)* | `L` | Plane | item | Ubicación del texto como plano |
| T *(opcional)* | `T` | Text | item | Texto a convertir en curvas |
| F *(opcional)* | `F` | Text | item | Nombre de la fuente. Usa el componente 'Font Selector' de Parakeet para obtener los nombres de las fuentes disponibles. |
| D *(opcional)* | `D` | Integer | item | Grado de la(s) curva(s) (se mantiene por compatibilidad de conexiones; las curvas nativas de Rhino son matemáticamente exactas) |
| St *(opcional)* | `St` | Integer | item | Estilo de fuente: 1: negrita, 2: cursiva, 0: normal (por defecto), 8: tachado, 4: subrayado |
| S *(opcional)* | `S` | Number | item | Tamaño |
| Js *(opcional)* | `Js` | Integer | item | Justificación del texto respecto del plano 'L': 0: arriba izquierda, 1: arriba centro, 2: arriba derecha, 3: medio izquierda, 4: medio centro (por defecto), 5: medio derecha, 6: abajo izquierda, 7: abajo centro, 8: abajo derecha |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pt | `Pt` | Point | item | Puntos de control del texto |
| Crvs | `Crvs` | Curve | item | Texto como lista de curvas |

### Polygon by Area (Polygon Area)

Crea un polígono según un área dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Plane | `P` | Plane | item | Plano base |
| Area | `A` | Number | item | Área del polígono |
| Segments | `S` | Integer | item | Cantidad de segmentos del polígono |
| Fillet Radius | `R` | Number | item | Radio de fillet de las esquinas del polígono |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon | `P` | Curve | item | Polígono |

### Random Seam

Ajusta al azar la costura de las curvas (y polilíneas) dadas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas a ajustar |
| Seed | `S` | Integer | item | Semilla del motor aleatorio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas ajustadas |

### Remove Duplicate Curves+ (RmDupCrv+)

Elimina curvas duplicadas usando longitud, dirección y muestreo de puntos con un umbral de tolerancia.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Lista de curvas a filtrar |
| Threshold | `T` | Number | item | Tolerancia de distancia para detectar duplicados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unique Indexes | `UI` | Integer | lista | Índices de las curvas únicas en la lista de entrada |
| Duplicate Indexes | `DI` | Integer | lista | Índices de las curvas duplicadas en la lista de entrada |

### Remove Short Segments (RmvShortSgmnt)

Quita los segmentos cortos de una curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de entrada |
| tolerance | `T` | Number | item | Tolerancia que define qué es un segmento corto. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de salida |

### SeparateDifferentCurves (SepCrvs)

Separa distintos tipos de curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygons | `P` | Curve | lista | Polígonos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Separated Polygons | `SP` | Curve | árbol | Polígonos separados |

## M.C.Escher Tilings

### Escher Hexagonal A (EscherHexA)

Genera un teselado de curvas personalizadas sobre una grilla cuadrada [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Curves | `C` | Curve | lista | 1, 2 o 3 curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | ¡Red de curvas estilo Escher! |

### Escher Hexagonal B (EscherHexB)

Genera un teselado de curvas personalizadas sobre una grilla cuadrada [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Curves | `C` | Curve | lista | 1, 2 o 3 curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas |

### Escher Quadriladeral A (EscherQuadA)

Genera un teselado de curvas personalizadas sobre una grilla cuadrada [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Curve(s) | `C` | Curve | lista | 1 o 2 curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | ¡Red de curvas estilo Escher! |

### Escher Trilateral A (EscherTriA)

Genera un teselado de curvas personalizadas sobre una grilla cuadrada [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Curves | `C` | Curve | lista | 1, 2 o 3 curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | ¡Red de curvas estilo Escher! |

### Meta Escher Hexagonal A (MetaEscherHexA)

Genera un teselado heterogéneo (parquet de deformación) de curvas personalizadas sobre una grilla hexagonal [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| #1 Curve(s) | `C1` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| #2 Curve(s) | `C2` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| #3 Curve(s) | `C3` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| Meta Points | `MP` | Point | lista | Punto(s) para manipular la metamorfosis del patrón (similar a puntos atractores) |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | ¡Red de curvas estilo Escher! [parquet de deformación] |

### Meta Escher Hexagonal B (MetaEscherHexB)

Genera un teselado heterogéneo (parquet de deformación) de curvas personalizadas sobre una grilla hexagonal [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| #1 Curve(s) | `C1` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| #2 Curve(s) | `C2` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| #3 Curve(s) | `C3` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| Meta Points | `MP` | Point | lista | Punto(s) para manipular la metamorfosis del patrón (similar a puntos atractores) |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | ¡Red de curvas estilo Escher! [parquet de deformación] |

### Meta Escher Quadriladeral (MetaEscherQuad)

Genera un teselado heterogéneo (parquet de deformación) de curvas personalizadas sobre una grilla cuadrilátera (cuadrada) [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| #1 Curve(s) | `C1` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| #2 Curve(s) | `C2` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| Meta Points | `MP` | Point | lista | Punto(s) para manipular la metamorfosis del patrón (similar a puntos atractores) |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | ¡Red de curvas estilo Escher! [parquet de deformación] |

### Meta Escher Trilateral (MetaEscherTri)

Genera un teselado heterogéneo (parquet de deformación) de curvas personalizadas sobre una grilla trilátera (triangular) [conocido sobre todo por los dibujos de M. C. Escher (1898-1972)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| #1 Curve(s) | `C1` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| #2 Curve(s) | `C2` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| #3 Curve(s) | `C3` | Curve | lista | Lista de curvas personalizadas (de cualquier grado) [las curvas se alinean/mapean respectivamente sobre las aristas de la grilla y se interpolan entre sí]. Idealmente entrega al menos 2 curvas |
| Meta Points | `MP` | Point | lista | Punto(s) para manipular la metamorfosis del patrón (similar a puntos atractores) |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | ¡Red de curvas estilo Escher! [parquet de deformación] |

### Wang Tile (WangTile)

Solver de bordes Wang Tile: genera patrones de borde continuos y basados en restricciones, usando mapeo estocástico de aristas y lógica de colapso de función de onda (wave function collapse). Mapea las geometrías de entrada extremo a extremo sobre una grilla cuadrada, respetando estrictamente las reglas de adyacencia definidas por el usuario para que no queden huecos ni distorsiones de escala.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base_Plane *(opcional)* | `BP` | Plane | item | Plano base de la grilla |
| X *(opcional)* | `X` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Y *(opcional)* | `Y` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| Size *(opcional)* | `Size` | Number | item | Tamaño de la(s) celda(s) de la grilla |
| Geom *(opcional)* | `G` | Curve | lista | Las curvas base mapeadas a las aristas de la grilla. Cada elemento representa un "tipo de arista" topológico único o "color Wang" (por ejemplo, elemento 0 = recto, 1 = lengüeta, 2 = muesca). Ojo: las curvas de entrada se rotan y escalan para encajar extremo a extremo sobre las líneas de la grilla |
| Rules *(opcional)* | `Rules` | Text | lista | Diccionario de teselas: el diccionario de restricciones que define qué tipos de arista pueden formar una tesela válida. Se ingresa como lista de textos de 4 dígitos que representan las aristas en sentido horario: norte, este, sur, oeste (por ejemplo, "0123" asigna el elemento 0 al norte, el 1 al este, etc.). Si se deja vacío, el solver asume que todas las permutaciones son válidas. |
| Rotate *(opcional)* | `Rotate` | Boolean | item | Permitir rotaciones: si es True, el solver amplía automáticamente el diccionario de reglas para incluir las permutaciones en sentido horario y antihorario de los textos de 4 dígitos entregados. Si es False, las teselas quedan fijas en la orientación indicada |
| Seed *(opcional)* | `Seed` | Integer | item | La semilla del solver estocástico para generar distintas variantes de patrón válidas a partir del mismo conjunto de reglas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `Pattern` | Generic Data | item | Patrón de salida del script. |
| Cells | `Cells` | Generic Data | item | Celdas de salida del script. |
| Indices | `Indices` | Generic Data | item | IDs de las teselas: una lista de IDs enteros que corresponden uno a uno con la salida Cells. Las configuraciones de celda topológicamente idénticas comparten el mismo ID. |

## Mesh

### Angle Split Mesh (AngSplitMesh)

Divide una malla en piezas separadas desoldando las aristas que superan un umbral de ángulo dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de entrada a dividir |
| Angle | `A` | Integer | item | Umbral de ángulo en grados: se dividen las aristas más agudas que este valor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Piezas de malla resultantes |

### Mesh Centroid (MeshCentroid)

Devuelve el centroide de una malla. Opcionalmente lo proyecta sobre la superficie de la malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de entrada |
| On Mesh | `OM` | Boolean | item | Si es True, proyecta el centroide al punto más cercano de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centroid | `C` | Point | item | Centroide de la malla (o el punto más cercano en la malla si On Mesh es True) |

### Mesh Surface Variable (MeshSrfVar)

Crea una malla según la curvatura de la superficie base (caras más grandes en zonas planas)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| Tolerance | `T` | Number | item | Desviación máxima de la malla respecto de la superficie |
| Laplacian | `L` | Integer | item | Cantidad de iteraciones de suavizado laplaciano en cada vértice de la malla |
| Iteration | `I` | Integer | item | Cantidad de iteraciones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Mesh Topology

Obtiene la topología completa de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Mesh | `M` | Mesh | item | Malla base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Vértices de la malla como puntos |
| Edges | `E` | Line | lista | Aristas de la malla como líneas |
| Faces | `F` | Mesh | lista | Caras de la malla como mallas individuales |
| Point \| Point Topology | `PP` | Integer | árbol | Para cada punto, índices de los puntos que se conectan a él |
| Point \| Line Topology | `PL` | Integer | árbol | Para cada punto, índices de las líneas que se conectan a él |
| Point \| Face Topology | `PF` | Integer | árbol | Para cada punto, índices de las caras de la malla que se conectan a él |
| Line \| Point Topology | `LP` | Integer | árbol | Para cada línea, índices de los puntos que se conectan a ella |
| Line \| Line Topology | `LL` | Integer | árbol | Para cada línea, índices de las líneas que se conectan a ella |
| Line \| Face Topology | `LF` | Integer | árbol | Para cada línea, índices de las caras que se conectan a ella |
| Face \| Point Topology | `FP` | Integer | árbol | Para cada cara, índices de los puntos que se conectan a ella |
| Face \| Line Topology | `FL` | Integer | árbol | Para cada cara, índices de las líneas que se conectan a ella |
| Face \| Face Topology | `FF` | Integer | árbol | Para cada cara, índices de las caras que se conectan a ella |

### MeshCap

Tapa todos los agujeros cubriendo las aristas desnudas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | lista | Malla a tapar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Malla tapada |

### Polyline To Mesh (Poly2Mesh)

Convierte polilíneas cerradas en mallas. Opcionalmente las extruye con un espesor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | lista | Polilíneas cerradas a convertir |
| Thickness | `T` | Number | item | Espesor de extrusión (0 = malla plana) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Mallas resultantes |

## Pattern Generation

### 2D Aggregation

Genera un sistema agregado formado por una curva base cualquiera

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Curve | `B` | Curve | lista | Curva base (polilínea cerrada) a proliferar |
| Iteration | `I` | Integer | item | Cantidad de iteraciones |
| Branch Count | `B` | Integer | item | Cantidad de proliferaciones en cada iteración |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Aggregated Curves | `C` | Curve | lista | Curvas agregadas |
| Curve Count | `Cc` | Integer | lista | Cantidad de curvas generadas en cada iteración, como lista |

### 3D Aggregation

Genera un sistema agregado formado por una malla base cualquiera

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Mesh | `B` | Mesh | lista | Malla cerrada/abierta a proliferar |
| Iterations | `I` | Integer | item | Cantidad de iteraciones |
| Obstacles | `O` | Mesh | lista | Lista de mallas a evitar durante la expansión; si no se necesita obstáculo, conecta la 'Base Mesh' |
| BranchCount | `B` | Integer | item | Cantidad de proliferaciones en cada iteración |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Aggregated Meshes | `M` | Mesh | lista | Mallas agregadas |
| Mesh Count | `Bc` | Integer | lista | Cantidad de mallas generadas en cada iteración, como lista |

### BZ Pattern (BZ)

Simula la reacción de Belousov-Zhabotinsky (BZ), una reacción química conocida por producir patrones autoorganizados de espirales y ondas. La simulación modela la interacción de tres sustratos químicos (A, B, C) en una grilla 2D con un enfoque de autómatas celulares, donde las concentraciones evolucionan según ecuaciones de reacción-difusión. Qué hace: inicializa una grilla 2D con concentraciones de los sustratos A, B y C, al azar o según valores del usuario, y actualiza la grilla de forma iterativa con las ecuaciones de la reacción BZ, produciendo espirales y ondas que evolucionan. Ojo: debes conectar un trigger o timer al componente para que se vuelva a calcular. Notas de uso: conecta un componente TRIGGER para animar la simulación y actualizar los patrones en el tiempo; usa un componente Custom Preview para ver los puntos y colores en Rhino; experimenta con `alpha`, `beta` y `gamma` (por ejemplo, `alpha = 1.2` para frentes de onda más largos) para variar el comportamiento de espirales y ondas; en grillas grandes (por ejemplo 100x100), reduce las dimensiones o ajusta el intervalo del Timer para mejorar el rendimiento. Créditos: este componente se basa en el modelo descrito en "A Simple Model of the Belousov-Zhabotinsky Reaction from First Principles" de Alasdair Turner, publicado el 19 de marzo de 2009 en la Bartlett School of Graduate Studies, University College London. El paper entrega las ecuaciones de reacción de tres sustratos y el enfoque de autómatas celulares adaptado aquí. Todo el crédito es del trabajo de Turner, disponible en http://www.aac.bartlett.ucl.ac.uk/processing/samples/bzr.pdf, que entrega las ecuaciones y la metodología base de todas las implementaciones que he visto. También existe una implementación en C# de Laurent Delrieu y Daniel Abalde en https://discourse.mcneel.com/t/belousov-zhabotinsky-reaction/118013, pero esta implementación en Python está pensada para generar patrones, por Arman

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| reset *(opcional)* | `reset` | Boolean | item | Si es `True`, reinicializa la grilla con concentraciones aleatorias; False significa ejecutar |
| width *(opcional)* | `width` | Integer | item | Cantidad de celdas de la grilla en la dirección X. |
| height *(opcional)* | `height` | Integer | item | Cantidad de celdas de la grilla en la dirección Y. |
| seed *(opcional)* | `seed` | Integer | item | Semilla para la inicialización aleatoria. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| points | `points` | Point | item | Puntos de la grilla. |
| colors | `colors` | Colour | item | Un color BZ por cada punto. |
| CMesh | `CM` | Mesh | item | Malla coloreada |

### BZ Pattern + (BZadv)

Simula la reacción de Belousov-Zhabotinsky (BZ), una reacción química conocida por producir patrones autoorganizados de espirales y ondas. La simulación modela la interacción de tres sustratos químicos (A, B, C) en una grilla 2D con un enfoque de autómatas celulares, donde las concentraciones evolucionan según ecuaciones de reacción-difusión. Qué hace: inicializa una grilla 2D con concentraciones de los sustratos A, B y C, al azar o según valores del usuario, y actualiza la grilla de forma iterativa con las ecuaciones de la reacción BZ, produciendo espirales y ondas que evolucionan. Ojo: debes conectar un trigger o timer al componente para que se vuelva a calcular. Notas de uso: conecta un componente TRIGGER para animar la simulación y actualizar los patrones en el tiempo; usa un componente Custom Preview para ver los puntos y colores en Rhino; experimenta con `alpha`, `beta` y `gamma` (por ejemplo, `alpha = 1.2` para frentes de onda más largos) para variar el comportamiento de espirales y ondas; en grillas grandes (por ejemplo 100x100), reduce las dimensiones o ajusta el intervalo del Timer para mejorar el rendimiento. Créditos: este componente se basa en el modelo descrito en "A Simple Model of the Belousov-Zhabotinsky Reaction from First Principles" de Alasdair Turner, publicado el 19 de marzo de 2009 en la Bartlett School of Graduate Studies, University College London. El paper entrega las ecuaciones de reacción de tres sustratos y el enfoque de autómatas celulares adaptado aquí. Todo el crédito es del trabajo de Turner, disponible en http://www.aac.bartlett.ucl.ac.uk/processing/samples/bzr.pdf, que entrega las ecuaciones y la metodología base de todas las implementaciones que he visto. También existe una implementación en C# de Laurent Delrieu y Daniel Abalde en https://discourse.mcneel.com/t/belousov-zhabotinsky-reaction/118013, pero esta implementación en Python está pensada para generar patrones, por Arman

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| reset *(opcional)* | `reset` | Boolean | item | Si es True, reinicializa la grilla con concentraciones nuevas o aleatorias; False significa ejecutar |
| con_A *(opcional)* | `con_A` | Number | lista | Lista plana de `ancho * alto` números que define las concentraciones iniciales del sustrato A (0.0 a 1.0). Si no se entrega o su largo es incorrecto, A se inicializa al azar. (La lista debe tener el mismo tamaño que la lista de puntos de la grilla.) |
| con_B *(opcional)* | `con_B` | Number | lista | Lista plana con las concentraciones iniciales del sustrato B. Si no se entrega o su largo es incorrecto, B se inicializa al azar. (La lista debe tener el mismo tamaño que la lista de puntos de la grilla.) |
| con_C *(opcional)* | `con_C` | Number | lista | Lista plana con las concentraciones iniciales del sustrato C. Si no se entrega o su largo es incorrecto, C se inicializa al azar. (La lista debe tener el mismo tamaño que la lista de puntos de la grilla.) |
| alpha *(opcional)* | `alpha` | Number | item | Parámetro de tasa de reacción que controla el crecimiento de A, impulsado por B e inhibido por C. Por defecto: 1.0. |
| beta *(opcional)* | `beta` | Number | item | Parámetro de tasa de reacción del crecimiento de B, impulsado por C e inhibido por A. Por defecto: 1.0. |
| gamma *(opcional)* | `gamma` | Number | item | Parámetro de tasa de reacción del crecimiento de C, impulsado por A e inhibido por B. Por defecto: 1.0. |
| height_scale *(opcional)* | `height_scale` | Number | item | Escala la altura Z de los puntos según la concentración de A, para visualizar en 3D. |
| width *(opcional)* | `width` | Integer | item | Cantidad de celdas de la grilla en la dirección X |
| height *(opcional)* | `height` | Integer | item | Cantidad de celdas de la grilla en la dirección Y |
| seed *(opcional)* | `seed` | Integer | item | Semilla para la inicialización aleatoria. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pt | `Pt` | Point | item | Puntos BZ. |
| CP | `CP` | Colour | item | Un color BZ por cada punto. |

### Cymatic Pattern (Cymatics)

[Componente experimental] Crea patrones cimáticos (también llamados placas de Chladni; https://monoskop.org/Ernst_Chladni). Ojo: los números 'N' y 'M' deben tener valores distintos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| N | `N` | Integer | item | Factor 'N' |
| M | `M` | Integer | item | Factor 'M' |
| Length | `L` | Number | item | Largo de la placa |
| Tolerance | `T` | Number | item | Tolerancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cymatics | `C` | Curve | lista | Patrón cimático |

### Cymatic Pattern Ex (Cymatics Ex)

[Componente experimental] Crea patrones cimáticos (también llamados placas de Chladni; https://monoskop.org/Ernst_Chladni). Ojo: los números 'N' y 'M' deben tener valores distintos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| N | `N` | Integer | item | Factor 'N' |
| M | `M` | Integer | item | Factor 'M' |
| Length | `L` | Number | item | Largo de la placa |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cymatics | `C` | Curve | lista | Patrón cimático |

### Discretized Aggregation (DDLA)

Genera una versión discretizada del algoritmo de agregación limitada por difusión (DLA) en 2D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Integer | item | Cantidad de puntos de la grilla base en la dirección x |
| y *(opcional)* | `y` | Integer | item | Cantidad de puntos de la grilla base en la dirección y |
| CS *(opcional)* | `CS` | Number | item | Tamaño de celda de la grilla base |
| Ri *(opcional)* | `Ri` | Point | lista | Posición de la raíz: usa 'MD Slider(s)' [o un 'Construct Point'] para elegir desde dónde nace la red. El valor debe estar normalizado (entre 0~1). Por ejemplo, un MD Slider en (0.5, 0.5) significa que la red parte desde el centro de la grilla base |
| Mode *(opcional)* | `Mode` | Boolean | item | Si es 'True', se siguen agregando puntos nuevos mientras 'Time' lo permita |
| Seed *(opcional)* | `Seed` | Integer | item | Un número entero que cambia el comportamiento aleatorio |
| Time *(opcional)* | `Time` | Number | item | Tiempo máximo, en segundos, que el componente puede pensar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| GridPt | `GridPt` | Point | item | Grilla base |
| Lines | `Lines` | Line | item | Red DDLA |

### Floral Pattern A (FloralA)

Genera un patrón floral originado en una lista de puntos (patrón arabesco)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| StartPoints | `P` | Point | lista | Puntos desde los que inician los patrones |
| First Branch Count | `FBC` | Integer | item | Cantidad de curvas en el primer paso |
| Curve Size | `S` | Number | item | Tamaño de cada elemento del patrón |
| Size Deviation | `SD` | Number | item | Factor de desviación del parámetro Size [un número de cero a uno; cero: sin desviación, uno: desviación máxima] |
| Rotation Factor | `R` | Number | item | Factor de rotación |
| Rotation Deviation | `RD` | Number | item | Factor de desviación del parámetro Rotation [un número de cero a uno; cero: sin desviación, uno: desviación máxima] |
| Branch Count | `B` | Integer | item | Cantidad de curvas en cada punto |
| Branch Count Deviation | `BD` | Number | item | Desviación de la cantidad de ramas |
| Seed | `S` | Integer | item | Un número entero que cambia el comportamiento aleatorio |
| Iteration | `Itr` | Integer | item | Cantidad de iteraciones (pasos de crecimiento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Floral Pattern | `FC` | Curve | lista | Curvas del patrón |
| Floral Curve Level | `L` | Integer | lista | Un número asociado a cada curva que indica su jerarquía |

### Flow Path (Flow)

Genera un camino de flujo de fluido [discreto] sobre una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla base |
| Start Points | `P` | Point | lista | Puntos de inicio del flujo |
| Step | `Sl` | Number | item | Distancia entre dos puntos consecutivos de cada camino de flujo (número más bajo = camino más suave) |
| Flow Direction | `FD` | Boolean | item | ¿El camino fluye hacia abajo? |
| Itreations | `Itrs` | Integer | item | Cantidad de iteraciones de cálculo |
| Flow Resolution | `FR` | Integer | item | Resolución del camino de flujo (número más alto = camino más suave) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Flow Path | `FP` | Point | árbol | Puntos del camino de flujo |

### Fractal Polyline (Fractal)

Genera una polilínea fractal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| F *(opcional)* | `F` | Curve | item | Polilínea base del fractal |
| C *(opcional)* | `C` | Curve | item | Polilínea sobre la que se genera el fractal |
| Fp *(opcional)* | `Fp` | Boolean | item | ¿Invertir la curva C? |
| Itr *(opcional)* | `Itr` | Integer | item | Cantidad de iteraciones [idealmente menos de 5] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| FP | `FP` | Curve | item | Polilínea fractal |

### Fracture Pattern A (FractureA)

Genera un patrón de fractura parecido a grietas o quiebres en una baldosa

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Plane | `P` | Plane | item | Plano base de la superficie |
| X | `X` | Number | item | Dimensión X de la baldosa base en la dirección X del plano base |
| Y | `Y` | Number | item | Dimensión de la baldosa base en la dirección Y del plano base |
| A | `A` | Number | item | Desviación de los ángulos |
| G | `G` | Integer | item | Cantidad de grietas en las generaciones siguientes |
| Seed | `S` | Integer | item | Un número entero que cambia el comportamiento aleatorio |
| Iteration | `Itr` | Integer | item | Cantidad de iteraciones (pasos de crecimiento) |
| Tolerance | `T` | Number | item | Tolerancia de cálculo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cracked Surfaces | `C` | Surface | lista | Superficies agrietadas |

### Gilbert Tesselation A (GilbertA)

Genera un patrón basado en una reinterpretación de la teselación de Gilbert. Compartido bajo licencia Atribución-NoComercial (CC BY-NC); para uso comercial, contactar al correo de soporte

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Punto para la teselación de Gilbert |
| Curve Count | `Cc` | Integer | item | Cantidad de curvas en cada punto |
| Bounds | `B` | Domain | item | Un dominio que define el intervalo en que se distribuyen las curvas |
| Randomness | `R` | Number | item | Un valor normalizado [entre 0 y 1] que define la aleatoriedad de las curvas |
| Seed | `S` | Integer | item | Semilla |
| Offset | `RO` | Number | item | Desfase del rectángulo contenedor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `GP` | Line | lista | Patrón de teselación de Gilbert |
| Boundary | `B` | Curve | item | Rectángulo contenedor |

### Gilbert Tesselation B (GilbertB)

Genera un patrón basado en una reinterpretación de la teselación de Gilbert. Compartido bajo licencia Atribución-NoComercial (CC BY-NC); para uso comercial, contactar al correo de soporte

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Punto para la teselación de Gilbert |
| Curve | `Crv` | Curve | item | Curva base |
| Curve Count | `Cc` | Integer | item | Cantidad de curvas en cada punto |
| Bounds | `B` | Domain | item | Un dominio que define el intervalo en que se distribuyen las curvas |
| Randomness | `R` | Number | item | Un valor normalizado [entre 0 y 1] que define la aleatoriedad de las curvas |
| Seed | `S` | Integer | item | Semilla |
| Offset | `RO` | Number | item | Desfase del rectángulo contenedor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `GP` | Curve | lista | Patrón de teselación de Gilbert |
| Boundary | `B` | Curve | item | Rectángulo contenedor |

### Gilbert Tesselation C (GilbertC)

Genera un patrón basado en una reinterpretación de la teselación de Gilbert. Compartido bajo licencia Atribución-NoComercial (CC BY-NC); para uso comercial, contactar al correo de soporte

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Punto para la teselación de Gilbert |
| Curve | `Crv` | Curve | item | Curva base |
| Offset | `RO` | Number | item | Desfase del rectángulo contenedor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `GP` | Curve | lista | Patrón de teselación de Gilbert |
| Boundary | `B` | Curve | item | Rectángulo contenedor |

### Growth On Brep (GrowthB)

Genera un patrón de una sola polilínea que se parece al crecimiento natural de células y órganos [también conocido como "crecimiento diferencial"]. Conecta un Timer de Grasshopper para refrescar el componente. Inspirado en Long Nguyen

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Una superficie (o Brep) sobre la que se genera el patrón |
| Distance | `D` | Number | item | Distancia máxima (posible) entre los vértices del patrón |
| Mode | `M` | Integer | item | Un número entero que define la polilínea inicial (0, 1 o 2) |
| MinP | `MinP` | Integer | item | Cantidad mínima de puntos desde la que se genera el patrón |
| MaxP | `MaxP` | Integer | item | Cantidad máxima de puntos que puede tener el patrón resultante |
| Reset | `R` | Boolean | item | Poner en True para reiniciar la simulación de crecimiento (usa un 'Button' booleano) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | item | Patrón de crecimiento diferencial |

### Growth On Mesh (GrowthM)

Genera un patrón de una sola polilínea que se parece al crecimiento natural de células y órganos [también conocido como "crecimiento diferencial"]. Conecta un Timer de Grasshopper para refrescar el componente. Inspirado en Long Nguyen

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Una malla sobre la que se genera el patrón |
| Distance | `D` | Number | item | Distancia máxima (posible) entre los vértices del patrón |
| Mode | `M` | Boolean | item | Un número entero que define la polilínea inicial (0, 1 o 2) |
| StartFaceIndex | `SFI` | Integer | item | El índice de la primera cara desde la que empezar |
| MinP | `MinP` | Integer | item | Cantidad mínima de puntos desde la que se genera el patrón |
| MaxP | `MaxP` | Integer | item | Cantidad máxima de puntos que puede tener el patrón resultante |
| Reset | `R` | Boolean | item | Poner en True para reiniciar la simulación de crecimiento (usa un 'Button' booleano) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | item | Patrón de crecimiento diferencial |

### Kelidoscope

Genera un patrón basado en el mecanismo de un caleidoscopio. Compartido bajo licencia Atribución-NoComercial (CC BY-NC); para uso comercial, contactar al correo de soporte

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| BasePlane | `P` | Plane | item | Plano base |
| Curves | `Crs` | Curve | lista | Lista de curvas (y polilíneas) con las que formar el patrón |
| Count | `Cn` | Integer | item | Cantidad de divisiones en la dirección polar |
| Angle | `A` | Number | item | Ángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| K-Pattern | `KP` | Curve | lista | Patrón caleidoscopio |

### Knit

Genera un patrón tejido sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| Extend U | `Eu` | Integer | item | Cantidad de curvas en la dirección U |
| Extend V | `Ev` | Integer | item | Cantidad de curvas en la dirección V |
| Height | `H` | Number | item | Altura del patrón tejido |
| Degree | `D` | Integer | item | Grado de las curvas de salida |
| Orientation | `O` | Boolean | item | Orientación ortogonal o diagonal |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Knited Curves U | `Ku` | Curve | lista | Curvas tejidas en la dirección U |
| Knited Curves V | `Kv` | Curve | lista | Curvas tejidas en la dirección V |

### Marching Square Pattern (MarchingS)

Genera un patrón de contornos a partir de una malla. Marching squares es un algoritmo de gráfica computacional que genera contornos para un campo escalar bidimensional

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Mesh | `M` | Mesh | item | Malla base |
| VertexValues | `VV` | Number | lista | Define un valor (número) para cada vértice {entre 0~1} |
| Threshold | `T` | Number | item | Umbral (isoparámetro) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern Curves | `P` | Line | lista | Curvas del patrón |

### Maze

Genera un laberinto perfecto (con un algoritmo de backtracking) a partir de una malla dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla base |
| Seed | `S` | Integer | item | Semilla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Maze Pattern | `MP` | Line | lista | Patrón de laberinto |

### Maze II (Maze2)

Un patrón de pseudolaberinto para fines arquitectónicos. Este componente genera un laberinto perfecto aleatorio con el algoritmo de Kruskal sobre una grilla del ancho y alto indicados. El laberinto se representa como una grilla 2D de celdas con muros (`'1'`) y pasos abiertos (`'0'`). La salida incluye la representación geométrica de los muros como líneas de Rhino y una representación de texto de la grilla con ceros y unos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Integer | item | Ancho del laberinto |
| y *(opcional)* | `y` | Integer | item | Alto del laberinto |
| S *(opcional)* | `S` | Number | item | Tamaño de celda |
| seed *(opcional)* | `seed` | Integer | item | Semilla aleatoria para generar laberintos reproducibles. Usa la misma semilla para generar laberintos idénticos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ml | `ml` | Line | item | Líneas del laberinto. |
| mm | `mm` | Text | item | Mapa del laberinto. |

### Maze III (Maze3Pts)

Una representación con puntos de un laberinto: divide los puntos en dos grupos, imitando una división tipo laberinto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Integer | item | Cantidad de celdas en X |
| y *(opcional)* | `y` | Integer | item | Cantidad de celdas en Y. |
| Sd *(opcional)* | `Sd` | Integer | item | Semilla: controla el comportamiento aleatorio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mtopo | `Mtopo` | Text | item | Topología del laberinto. |
| A | `A` | Point | item | Puntos A del laberinto. |
| B | `B` | Point | item | Puntos B del laberinto. |

### Mesh Peeler I (MPeel I)

Pela una malla según distancias geodésicas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Face Indices | `FI` | Integer | lista | Lista de índices de caras desde las que empieza el pelado |
| Steps | `S` | Integer | lista | Números que indican el paso (ancho) de cada franja |
| Variable width | `V` | Boolean | item | Si es 'False', el pelado es aleatorio |
| Seed | `S` | Integer | item | Semilla: un número entero para mezclar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| dM | `M` | Mesh | lista | Malla discretizada (pelada) |
| dP | `P` | Curve | lista | Patrón discretizado |

### Mesh Peeler II (MPeel II)

Pela una malla según distancias geodésicas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |
| Indices of removed Faces | `RFI` | Integer | lista | Lista de índices de caras a quitar de la malla inicial |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| dM | `M` | Mesh | lista | Malla discretizada (pelada) |

### Minimum Spacing Tree (MST)

Genera un árbol de expansión mínima (MST): una red que conecta todos los vértices, sin ciclos y con la menor longitud total de aristas posible

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Points | `P` | Point | lista | Puntos para crear la red |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Minimum Spanning Tree | `MST` | Line | lista | Árbol de expansión mínima |

### Pattern Genotype A (PatternGenA)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype B (PatternGenB)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype C (PatternGenC)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype D (PatternGenD)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype E (PatternGenE)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype F (PatternGenF)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype G (PatternGenG)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype H (PatternGenH)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype I (PatternGenI)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype J (PatternGenJ)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | item | Patrón geométrico |

### Pattern Genotype K (PatternGenK)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Factor | `F` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype L (PT) (PatternGenL (PT))

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) \| Este genotipo devuelve teselados pentagonales (conocidos como teselados pentagonales de tipo 4 y 5) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Rotation Factor | `R` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |
| Scale Factor | `S` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype M (PT) (PatternGenM (PT))

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) \| Este genotipo devuelve teselados pentagonales (conocidos como teselados pentagonales de tipo 3) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Rotation Factor | `R` | Number | item | Factor de genotipo normalizado (un número entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype N (TA) (PatternGenN)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Blend | `B` | Number | item | Un valor normalizado [entre 0 y 1] como factor de mezcla |
| StartIndex | `Si` | Integer | item | Un número entero que define el índice inicial |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype O (PatternGenO)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [patrón Truchet]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | lista | Polilíneas base (celdas) |
| Orientation | `O` | Boolean | item | Si es 'True', se invierte la orientación de la entrada |
| Prune | `P` | Boolean | item | Si es 'True', el patrón resultante se poda. |
| Self Intersection | `SI` | Boolean | item | Si es 'True', intenta crear un patrón sin autointersecciones |
| Step Number | `N` | Integer | item | Cantidad de pasos en cada arista |
| Bulge Factor | `Bf` | Number | item | Factor de abombamiento |
| Degree | `D` | Integer | item | Grado de las curvas |
| Seed | `S` | Integer | item | Semilla: un número entero para mezclar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón [curvas Truchet] |
| Linear Pattern | `LP` | Curve | lista | Patrón [curvas Truchet], representación lineal |

### Pattern Genotype P (PatternGenP)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Rotatio Factor | `Fr` | Number | item | Factor de rotación del genotipo |
| Bulge Factor | `Fb` | Number | item | Factor de abombamiento del genotipo |
| Degree | `D` | Integer | item | Grado de la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Genotype Q (PatternGenQ)

Un método para generar patrones sobre celdas personalizadas (consejo: funciona mejor con celdas de la categoría "Tiling" de Parakeet) [basado en la tesis de Esmaeil Mottaghi, ver https://paragenic.ca/; compartido bajo licencia Creative Commons Atribución-CompartirIgual (CC BY-SA)]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Segment Count | `N` | Integer | item | Cantidad de segmentos en que dividir las curvas. |
| Factor 1 | `F1` | Number | item | Define dónde empiezan a formarse los arcos, desplazando el punto medio de la curva hacia los extremos (0 = los arcos empiezan al centro, 1 = empiezan cerca de los extremos). |
| Factor 2 | `F2` | Number | item | Define la altura del arco controlando cuánto se tiran los puntos desde la base hacia el arco (0 = sin altura, 1 = altura total). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Pattern Statistics (PatternStat)

Obtiene algunas estadísticas de un patrón (red de líneas/curvas)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón a analizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shortest Segment | `SS` | Number | item | Longitud del segmento más corto |
| Longest Segment | `LS` | Number | item | Longitud del segmento más largo |
| Closed Regions | `R` | Integer | item | Cantidad total de regiones cerradas |
| Invalid Curve | `I` | Boolean | item | 'True' si el patrón de entrada contiene al menos una curva inválida |

### Star Pattern I (StarPatternI)

Un método geométrico para diseñar patrones islámicos (basado en un método presentado por Craig S. Kaplan; http://www.cgl.uwaterloo.ca/csk/). Para obtener un patrón heterogéneo, ingresa distintos parámetros (A y D) para cada celda

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Grid | `C` | Curve | item | Grilla base |
| Angle | `A` | Number | item | Ángulo entre las líneas internas (o parámetro θ), en radianes |
| Distance | `D` | Number | item | (o parámetro ɸ) |
| Shift Size | `S` | Integer | item | Tamaño del desplazamiento |
| Bulge Factor | `Fb` | Number | item | Factor de abombamiento del genotipo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón |

### Star Pattern II (StarPatternII)

Un método geométrico para diseñar patrones islámicos (basado en un método presentado por Hankin Lee y Craig S. Kaplan; http://www.cgl.uwaterloo.ca/csk/). Para obtener un patrón heterogéneo, ingresa distintos parámetros (A y D) para cada celda

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Grid | `C` | Curve | item | Grilla base |
| Angle | `A` | Number | item | Ángulo entre las líneas internas (o parámetro θ), en radianes |
| Factor | `F` | Number | item | Factor |
| Distance | `D` | Number | item | (o parámetro ɸ) |
| Shift Size | `S` | Integer | item | Tamaño del desplazamiento |
| Angle Factor | `AF` | Number | item |  |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón |

### Star Pattern III (StarPatternIII)

Un método geométrico para diseñar patrones islámicos (un método presentado por Eric Broug, http://broug.com/). Para obtener un patrón heterogéneo, ingresa distintos parámetros (A y D) para cada celda

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Curve | item | Polilíneas base (celdas) |
| Star Size | `SS` | Number | item | El tamaño de la estrella central |
| Parameter B | `P` | Number | item | Parámetro B |
| Degree | `d` | Integer | item | El grado de las curvas de salida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón geométrico |

### Tileable Pattern (p4) (Tilep4)

Un método para generar patrones repetibles (tileables).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P *(opcional)* | `P` | Plane | item | Plano base de la grilla |
| S *(opcional)* | `S` | Number | item | Tamaño de la(s) celda(s) de la grilla |
| Ex *(opcional)* | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Ey *(opcional)* | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| BC *(opcional)* | `BC` | Curve | lista | Lista de curvas base (y polilíneas) para generar el patrón |
| BCPlane *(opcional)* | `BCPlane` | Plane | item | Plano de las curvas BC |
| BCoffset *(opcional)* | `BCoffset` | Number | item | Un valor normalizado [entre 0 y 1] que define el valor de desfase |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid | `Grid` | Curve | item | Celdas de la grilla como árbol |
| C | `C` | Curve | item | Patrón repetible como árbol |

### Tileable Pattern (p4g) (Tilep4g)

Un método para generar patrones repetibles (tileables).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P *(opcional)* | `P` | Plane | item | Plano base de la grilla |
| S *(opcional)* | `S` | Number | item | Tamaño de la(s) celda(s) de la grilla |
| Ex *(opcional)* | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Ey *(opcional)* | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| BC *(opcional)* | `BC` | Curve | lista | Lista de curvas base (y polilíneas) para generar el patrón |
| BCPlane *(opcional)* | `BCPlane` | Plane | item | Plano de las curvas BC |
| BCoffset *(opcional)* | `BCoffset` | Number | item | Un valor normalizado [entre 0 y 1] que define el valor de desfase |
| Mode *(opcional)* | `Mode` | Integer | item | Un número entero que define qué partes de 'BC' se seleccionan para generar el patrón [0 a 3] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid | `Grid` | Curve | item | Celdas de la grilla como árbol |
| C | `C` | Curve | item | Patrón repetible como árbol |

### Tileable Pattern (p4m) (Tilep4m)

Un método para generar patrones repetibles (tileables).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P *(opcional)* | `P` | Plane | item | Plano base de la grilla |
| S *(opcional)* | `S` | Number | item | Tamaño de la(s) celda(s) de la grilla |
| Ex *(opcional)* | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Ey *(opcional)* | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| BC *(opcional)* | `BC` | Curve | lista | Lista de curvas base (y polilíneas) para generar el patrón |
| BCPlane *(opcional)* | `BCPlane` | Plane | item | Plano de las curvas BC |
| BCoffset *(opcional)* | `BCoffset` | Number | item | Un valor normalizado [entre 0 y 1] que define el valor de desfase |
| Mode *(opcional)* | `Mode` | Integer | item | Un número entero que define qué partes de BC se seleccionan para generar el patrón [0 a 3] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid | `Grid` | Curve | item | Celdas de la grilla como árbol |
| C | `C` | Curve | item | Patrón repetible como árbol |

### Tileable Pattern (pgg) (Tilepgg)

Un método para generar patrones repetibles (tileables).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P *(opcional)* | `P` | Plane | item | Plano base de la grilla |
| Sx *(opcional)* | `Sx` | Number | item | Tamaño de la(s) celda(s) de la grilla en la dirección X |
| Sy *(opcional)* | `Sy` | Number | item | Tamaño de la(s) celda(s) de la grilla en la dirección Y |
| Ex *(opcional)* | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Ey *(opcional)* | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| BC *(opcional)* | `BC` | Curve | lista | Lista de curvas base (y polilíneas) para generar el patrón |
| BCPlane *(opcional)* | `BCPlane` | Plane | item | Plano de las curvas BC |
| BCoffset *(opcional)* | `BCoffset` | Number | item | Un valor normalizado [entre 0 y 1] que define el valor de desfase |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid | `Grid` | Curve | item | Celdas de la grilla como árbol |
| C | `C` | Curve | item | Patrón repetible como árbol |

### Tileable Pattern (pmg) (Tilepmg)

Un método para generar patrones repetibles (tileables).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P *(opcional)* | `P` | Plane | item | Plano base de la grilla |
| Sx *(opcional)* | `Sx` | Number | item | Tamaño de la(s) celda(s) de la grilla en la dirección X |
| Marshalling signal parameter *(opcional)* | `Sy` | Generic Data | item | Tamaño de la(s) celda(s) de la grilla en la dirección Y |
| Ex *(opcional)* | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Ey *(opcional)* | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| BC *(opcional)* | `BC` | Curve | lista | Lista de curvas base (y polilíneas) para generar el patrón |
| BCPlane *(opcional)* | `BCPlane` | Plane | item | Plano de las curvas BC |
| BCoffset *(opcional)* | `BCoffset` | Number | item | Un valor normalizado [entre 0 y 1] que define el valor de desfase |
| Mode *(opcional)* | `Mode` | Boolean | item | ¿Invertir el patrón? |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid | `Grid` | Curve | item | Celdas de la grilla como árbol |
| C | `C` | Curve | item | Patrón repetible como árbol |

### Tileable Pattern (pmm) (Tilepmm)

Un método para generar patrones repetibles (tileables).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P *(opcional)* | `P` | Plane | item | Plano base de la grilla |
| Sx *(opcional)* | `Sx` | Number | item | Tamaño de la(s) celda(s) de la grilla en la dirección X |
| Sy *(opcional)* | `Sy` | Number | item | Tamaño de la(s) celda(s) de la grilla en la dirección Y |
| Ex *(opcional)* | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Ey *(opcional)* | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |
| BC *(opcional)* | `BC` | Curve | lista | Lista de curvas base (y polilíneas) para generar el patrón |
| BCPlane *(opcional)* | `BCPlane` | Plane | item | Plano de las curvas BC |
| BCoffset *(opcional)* | `BCoffset` | Number | item | Un valor normalizado [entre 0 y 1] que define el valor de desfase |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid | `Grid` | Curve | item | Celdas de la grilla como árbol |
| C | `C` | Curve | item | Patrón repetible como árbol |

### Travelling Salesman (TSP)

Resuelve el problema del vendedor viajero (TSP)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `Pts` | Point | lista | Puntos a visitar |
| Start Index | `I` | Integer | item | Índice del punto inicial |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Path | `P` | Curve | item | Recorrido optimizado como polilínea |
| Length | `L` | Number | item | Longitud total del recorrido |
| Indices | `I` | Integer | lista | Orden de visita como índices de los puntos de entrada |

### Venation I

Genera una red de curvas tipo nervadura [ramificada] entre una lista de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Venation Points | `P` | Point | lista | Puntos para crear la red de nervaduras |
| Root Indeces | `SPi` | Integer | lista | Índices de los puntos de [P] que se consideran raíces de la nervadura |
| Branch Count | `B` | Integer | item | Cantidad máxima de ramas nuevas en cada punto |
| Cut Off Distance | `C` | Number | item | Distancia máxima que explora cada punto para crear una rama nueva |
| Iterations | `Itrs` | Integer | item | Cantidad de iteraciones de cálculo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Venation Pattern | `V` | Line | árbol | Una red ramificada de líneas que representa el crecimiento paso a paso del sistema de nervaduras. |

### Venation II

Genera una red de curvas tipo nervadura [ramificada] entre una lista de puntos. El algoritmo se basa en el ensayo de Adam Runions, Martin Fuhrer, Brendan Lane y Pavol Federl titulado "Modeling and visualization of leaf venation patterns", de la Universidad de Calgary

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos u "auxinas" que generan la red de nervaduras, idealmente sobre una malla |
| Base Mesh | `M` | Mesh | item | Malla sobre la que se lleva la red de nervaduras |
| Root Points | `RP` | Point | lista | Puntos que funcionan como "raíces" de la nervadura |
| Cut Off Distance | `CO` | Number | item | Distancia máxima que explora cada punto para crear una rama nueva |
| Step Size | `S` | Number | item | Tamaño del paso con que crece la "planta" en cada iteración |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Venation Network | `V` | Line | árbol | Una red ramificada de líneas que representa el crecimiento paso a paso del sistema de nervaduras. |

### Wave Pattern (WavePt)

Genera un patrón de ondas basado en una imagen, originado en una lista de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla coloreada de entrada |
| StartPoints | `P` | Point | lista | Puntos desde los que inician los patrones |
| Threshold | `T` | Number | item | Umbral |
| Step Count | `C` | Integer | item | Cantidad de pasos |
| Type | `T` | Integer | item | 5 tipos de patrón: de 0 a 4 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Wave Pattern | `Pt` | Point | árbol | La lista de puntos para generar las curvas |

### Wondering Salesman (WSP)

Este componente calcula los caminos topológicos más largos desde nodos raíz indicados hasta nodos objetivo dentro de una topología de red dada. Identifica los nodos objetivo según su conectividad (los puntos con menor valencia) y luego busca las rutas máximas desde las raíces hasta los puntos objetivo más lejanos. En otras palabras, obtiene el camino topológico más largo, similar a un "problema de recorrido máximo". Entrega un árbol con todos los caminos de longitud máxima desde cada raíz hasta el nodo objetivo más cercano; cada rama representa un camino más largo único. Los caminos son simples (sin ciclos) y se determinan con una búsqueda en anchura (BFS). Ojo: este componente puede volverse muy pesado en redes grandes por el algoritmo BFS recursivo, que explora todos los caminos posibles para encontrar los más largos. La complejidad crece exponencialmente con la cantidad de nodos y conexiones, lo que puede causar demoras importantes o mucho uso de memoria en topologías extensas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| PP *(opcional)* | `PP` | Integer | árbol | Topología punto-punto como árbol (usa la salida 'PP' de Network Topology de Parakeet) |
| roots *(opcional)* | `roots` | Integer | lista | Una lista de índices como ids de los puntos iniciales |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Path | `Path` | Integer | item | Camino de salida del script. |
| TPi | `TPi` | Integer | item | Una lista de índices de nodos con la valencia mínima (grado 1), identificados como nodos objetivo. |

## Primitive

### Geodesic Dome

Genera una cúpula geodésica a partir de un icosaedro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Point | `B` | Point | item | Punto base |
| Radius | `R` | Number | item | Radio |
| Dome Frequency | `F` | Integer | item | Frecuencia de la cúpula (nivel de subdivisión) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geodeic Dome | `GD` | Mesh | item | Cúpula geodésica como malla |
| Base Mesh | `B` | Mesh | item | Malla subdividida sin proyectar |
| Geodesic Points | `GP` | Point | lista | Puntos geodésicos |
| Geodesic Edges | `GE` | Curve | lista | Bordes de las caras de la cúpula geodésica |

### Klein Bottle

Crea una botella de Klein como superficie NURBS

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Division | `U` | Integer | item | Cantidad de divisiones en la dirección U de la superficie |
| X Factor | `X` | Number | item | Factor de escala en la dirección X |
| Y Factor | `Y` | Number | item | Factor de escala en la dirección Y |
| Radius | `R` | Number | item | Radio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Klein Bottle | `S` | Surface | item | Botella de Klein |
| Klein Bottle Points | `P` | Point | lista | Botella de Klein como puntos |
| Klein Bottle Mesh | `M` | Mesh | item | Botella de Klein como malla |

### Klein Surface

Crea una superficie NURBS de Klein

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Division | `U` | Integer | item | Cantidad de divisiones en la dirección U de la superficie |
| Radius 1 | `R1` | Number | item | Radio 1 |
| Radius 2 | `R2` | Number | item | Radio 2 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Klein Surface | `S` | Surface | item | Superficie de Klein |
| Klein surface Points | `P` | Point | lista | Superficie de Klein como puntos |
| Klein surface Mesh | `M` | Mesh | item | Superficie de Klein como malla |

### Mobius Surface (Mobius)

Crea una superficie de Möbius con parámetros variables

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Plane | `P` | Plane | item | Plano base |
| Radius | `R` | Number | item | Radio |
| InnerRotation | `Ir` | Number | item | Rotación interior en radianes \| Ojo: se recomiendan múltiplos impares de Pi |
| OuterRotation | `Or` | Number | item | Rotación exterior en radianes \| Ojo: se recomiendan múltiplos impares de Pi |
| Length | `L` | Number | item | Longitud de la línea de perfil |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mobius Surface | `S` | Surface | item | Superficie de Möbius |
| Mobius Planes | `P` | Plane | lista | Planos de Möbius |

### PlukerSurface (PlukerSrf)

Crea una superficie de Plücker con parámetros variables

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Division | `U` | Integer | item | Cantidad de divisiones en la dirección U de la superficie |
| P Factor | `P` | Number | item | Factor P (factor de Pi en la curva seno exterior) |
| Radius | `R` | Number | item | Radio de Plücker |
| Height | `H` | Number | item | Alto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plucker surface | `S` | Surface | item | Superficie de Plücker |
| Plucker surface points | `P` | Point | lista | Superficie de Plücker como puntos |
| Plucker surface Mesh | `M` | Mesh | item | Superficie de Plücker como malla |

## Surface

### BooleanSplit

Divide un Brep con otro(s) Brep(s) [división Brep\|Brep]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Brep | lista | Primer conjunto de Brep(s) |
| B | `B` | Brep | lista | Segundo conjunto de Brep(s) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `SB` | Brep | lista | Breps divididos |

### Brep join plus (Brep join +)

Une varios Breps que estén a menos de una distancia

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | lista | Breps a unir |
| Tolerance | `T` | Number | item | Distancia máxima entre Breps para unirlos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| joinedBreps | `JB` | Brep | lista | Breps unidos |

### Brep Remove Holes (BrepRemoveHoles)

Quita los agujeros de un B-rep (funciona con superficies NURBS recortadas y sin recortar)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep (o superficie(s)) cuyos agujeros se rellenan |
| Tolerance | `T` | Number | item | Tolerancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep rellenado |

### Brep Topology

Obtiene la topología completa de un Brep

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Vértices del Brep como puntos |
| Edges | `E` | Line | lista | Aristas del Brep como líneas |
| Faces | `F` | Brep | lista | Caras del Brep como superficies individuales |
| Point \| Point Topology | `PP` | Integer | árbol | Para cada punto, índices de los puntos que se conectan a él |
| Point \| Line Topology | `PL` | Integer | árbol | Para cada punto, índices de las líneas que se conectan a él |
| Point \| Face Topology | `PF` | Integer | árbol | Para cada punto, índices de las caras del Brep que se conectan a él |
| Line \| Point Topology | `LP` | Integer | árbol | Para cada línea, índices de los puntos que se conectan a ella |
| Line \| Line Topology | `LL` | Integer | árbol | Para cada línea, índices de las líneas que se conectan a ella |
| Line \| Face Topology | `LF` | Integer | árbol | Para cada línea, índices de las caras que se conectan a ella |
| Face \| Point Topology | `FP` | Integer | árbol | Para cada cara, índices de los puntos que se conectan a ella |
| Face \| Line Topology | `FL` | Integer | árbol | Para cada cara, índices de las líneas que se conectan a ella |
| Face \| Face Topology | `FF` | Integer | árbol | Para cada cara, índices de las caras que se conectan a ella |

### CreateSolid

Crea un sólido (Brep cerrado) encerrado por superficies y polisuperficies que se intersectan

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `S` | Brep | lista | Breps o superficies a recortar y unir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Solid | `B` | Brep | item | Brep cerrado resultante |

### Extend Surface (ExtendSrf)

Extiende una superficie desde una arista y una distancia dadas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `B` | Surface | item | Superficie a extender |
| Edge indexes | `i` | Integer | lista | Índices de las aristas de la superficie a extender |
| Extend Distance | `D` | Number | item | Distancia de extensión |
| Extend Type | `E` | Boolean | item | Tipo de extensión (True = suave, False = lineal) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extended Surface | `S` | Surface | item | Superficie extendida |

### Map To Surface (MapToSrf)

Mapea una curva sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas a mapear |
| Source Surface | `S` | Surface | item | Superficie desde la que mapear las curvas |
| Target Surface | `T` | Surface | item | Superficie sobre la que mapear las curvas |
| U Subdivision | `U` | Integer | item | Cantidad de repeticiones de la curva en la dirección U |
| V Subdivision | `V` | Integer | item | Cantidad de repeticiones de la curva en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Curves | `C` | Curve | lista | Curvas mapeadas |

### Offset Brep (BrepOffset)

Aplica offset a un Brep con parámetros variables

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep al que aplicar offset |
| Distance | `D` | Number | item | Distancia de offset |
| Solid | `S` | Boolean | item | Poner en 'True' para crear un brep sólido (tapado) |
| Both Sides | `B` | Boolean | item | ¿Offset hacia ambos lados? |
| Round Corners | `C` | Boolean | item | Poner en 'True' para que las esquinas sean redondeadas |
| MergeFaces | `M` | Boolean | item | Poner en 'True' para fusionar las caras coplanares |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | lista | Brep resultante |

### Panelized Sum Surface (PQSumSrf)

Crea una panelización de cuadriláteros planos sobre una superficie, generada por dos curvas de perfil (basado en un método de Tang, https://geometry.stanford.edu/person.php?id=tangcc)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First curve | `A` | Curve | item | Primera curva |
| Second curve | `B` | Curve | item | Segunda curva |
| U Division | `U` | Integer | item | División U |
| V Division | `V` | Integer | item | División V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panelized surfaces | `S` | Surface | lista | Superficies panelizadas |

### RemoveDuplicateSurface (RemoveDupSrf)

Quita las superficies idénticas de una lista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Superficies a limpiar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Superficies únicas |
| Unique Surfaces indexes | `Si` | Integer | lista | Índices de las superficies únicas en la lista de entrada |

### Reverse Surface (ReverseSrf)

Invierte las direcciones U y V (dominio) de una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie |
| Reverse Mode | `R` | Integer | item | 0 = sin cambios en UV, 1 = invertir la primera dirección, 2 = invertir la segunda dirección, 3 = invertir ambas direcciones, 4 = invertir la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie invertida |

### Unjoin Brep Faces (Unjoin Brep)

Explota un Brep desde algunas aristas específicas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep a explotar |
| Brep Edge Indices | `EI` | Integer | lista | Índices de las aristas del Brep desde donde ocurre la explosión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | lista | Brep a explotar |

### Voronoi On Surface (VoronoiSrf)

Genera un patrón de Voronoi sobre una superficie NURBS dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos para el patrón de Voronoi (sobre la superficie) |
| Target | `S` | Surface | item | Superficie objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Voronoi | `V` | Curve | lista | Patrón de Voronoi como polilíneas cerradas (celdas) |

## Tiling

### Hyperbolic Tiling A (hTilingA)

Crea un teselado hiperbólico (similar al modelo del disco de Poincaré)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `PL` | Plane | item | Plano base |
| p | `p` | Integer | item | Un número entero que debe cumplir la ecuación (p-2)*(q-2)>=4; determina la cantidad de aristas de cada celda |
| q | `q` | Integer | item | Un número entero que debe cumplir la ecuación (p-2)*(q-2)>=4; determina la valencia de cada nodo (cantidad de puntos vecinos de cada vértice) |
| Rotatation Factor | `RPl` | Number | item | Factor de rotación del plano base |
| Origin Shift | `SO` | Number | item | Un número normalizado [entre 0~1] para desplazar el punto de origen |
| Rotate Origin Point | `RO` | Number | item | Factor de rotación del origen |
| Scale | `Sc` | Number | item | Factor de escala |
| Step | `S` | Integer | item | Cantidad de pasos de subdivisión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curved Polygons | `CP` | Curve | lista | Celdas del teselado como curvas cerradas |
| Linear Polygons | `LP` | Curve | lista | Celdas del teselado como polígonos cerrados |

### 2-Uniform Tiling A (2TilingA)

Crea un teselado euclidiano 2-uniforme de polígonos convexos con configuración de vértices ([3.4.6.4 ; 3^2.4.3.4])

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### 2-Uniform Tiling B (2TilingB)

Crea un teselado euclidiano 2-uniforme de polígonos convexos con configuración de vértices ([4.6.12 ; 3.4.6.4])

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### 2-Uniform Tiling C (2TilingC)

Crea un teselado euclidiano 2-uniforme de polígonos convexos con configuración de vértices ([3.3.3.4.4; 6.4.3.4])

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### 2-Uniform Tiling D (2TilingD)

Crea un teselado euclidiano 2-uniforme de polígonos convexos con configuración de vértices ([3.3.4.3.4; 4.4.3.3.3])

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### 2-Uniform Tiling E (2TilingE)

Crea un teselado euclidiano 2-uniforme de polígonos convexos con configuración de vértices ([4.3.12.3; 12.12.3])

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### 2-Uniform Tiling F (2TilingF)

Crea un teselado euclidiano 2-uniforme de polígonos convexos con configuración de vértices ([3^6; 3^2.4.12])

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### 4-Uniform Tiling A (4TilingA)

Crea un teselado euclidiano 4-uniforme de polígonos convexos con configuración de vértices ([(3.4.6.4)^2 ; (4.6.12)^2])

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Brick Type A (Brick A)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Brick Type B (Brick B)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks_1 | `B1` | Curve | lista | Ladrillos como celdas |
| Bricks_2 | `B2` | Curve | lista | Ladrillos como celdas |

### Brick Type C (Brick C)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Brick Type D (Brick D)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks_1 | `B1` | Curve | lista | Ladrillos como celdas |
| Bricks_2 | `B2` | Curve | lista | Ladrillos como celdas |

### Brick Type E (Brick E)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Brick Type F (Brick F)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Brick Type G (Brick G)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Brick Type H (Brick H)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Brick Type I (Brick I)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Brick Type J (Brick J)

Crea ladrillos como polilíneas cerradas (celdas) sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Surface | `S` | Surface | item | Superficie base |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U de la superficie base |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V de la superficie base |
| Offset Distance | `D` | Number | item | Distancia de offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks1 | `B1` | Curve | lista | Ladrillos como celdas |
| Bricks2 | `B1` | Curve | lista | Ladrillos como celdas |

### Brick Type K (Brick K)

Genera una grilla con patrón espiga (herringbone) usando un módulo de curva paramétrico.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Plane | `Pl` | Plane | item | Plano base desde el que parte el patrón espiga. |
| Module Length | `L` | Number | item | Largo de cada módulo de espiga. |
| Module Width | `W` | Number | item | Ancho de cada módulo de espiga. |
| Row Count | `R` | Integer | item | Cantidad de filas de la grilla de espiga. |
| Column Count | `C` | Integer | item | Cantidad de columnas de la grilla de espiga. |
| Offset Distance | `D` | Number | item | Separación/desfase opcional entre piezas (valor de medio ancho). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bricks | `B` | Curve | lista | Ladrillos como celdas |

### Elongated triangular (Tiling H sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (3.3.3.4.4), también conocido como teselado triangular alargado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Penrose

Crea un teselado de Penrose (Penrose de tipo 2) formado por polígonos cuadriláteros

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Iteration | `I` | Integer | item | Cantidad de iteraciones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | lista | Polilínea |

### Pentagonal Tiling 01_A (PTiling 01A)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size 1 | `S1` | Number | item | Tamaño de las celdas de la grilla |
| Size 2 | `S2` | Number | item | Tamaño de las celdas de la grilla |
| Size 3 | `S3` | Number | item | Tamaño de las celdas de la grilla |
| Size 4 | `S4` | Number | item | Tamaño de las celdas de la grilla |
| Rotation 1 | `R1` | Number | item | Rotación |
| Rotation 2 | `R2` | Number | item | Rotación |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 01_B (PTiling 01B)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size 1 | `S1` | Number | item | Tamaño de las celdas de la grilla |
| Size 2 | `S2` | Number | item | Tamaño de las celdas de la grilla |
| Rotation 1 | `R1` | Number | item | Rotación |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 02_A (PTiling 02A)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size A | `a` | Number | item | Tamaño A |
| Size B | `b` | Number | item | Tamaño B |
| Size C | `c` | Number | item | Tamaño C |
| Rotation1 | `R1` | Number | item | Rotación 1 |
| Rotation2 | `R2` | Number | item | Rotación 2 |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 02_B (PTiling 02B)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size A | `S1` | Number | item | Tamaño 1 |
| Size B | `S2` | Number | item | Tamaño 2 |
| Rotation1 | `R1` | Number | item | Rotación 1 |
| Rotation2 | `R2` | Number | item | Rotación 2 |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 06 (PTiling 06)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Rotation | `R` | Number | item | Rotación |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 07 (PTiling 07)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Rotation | `R` | Number | item | Rotación |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 09 (PTiling 09)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Rotation | `R` | Number | item | Rotación |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 10 (PTiling 10)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Rotation | `R` | Number | item | Rotación |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 13 (PTiling 13)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Rotation | `R` | Number | item | Rotación |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Pentagonal Tiling 15 (PTiling 15)

Crea un teselado pentagonal euclidiano irregular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Quadrilateral Tiling (QuadTiling)

Genera un teselado (grilla) a partir de cualquier curva cuadrilátera, regular o irregular (cualquier polilínea cerrada de 4 puntos y 4 aristas)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Based Curve | `C` | Curve | item | Curva base cuadrilátera (cualquier polilínea cerrada de 4 puntos y 4 aristas) |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Quadrilateral Tiling | `QT` | Curve | lista | Teselado cuadrilátero |

### Rhombitrihexagonal (Tiling C sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (3.4.6.4), también conocido como teselado rombitrihexagonal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Snub square (Tiling B sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (3.3.4.3.4), también conocido como teselado cuadrado romo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Snub Trihexagonal (Tiling A sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (3.3.3.3.6), también conocido como teselado trihexagonal romo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Trihexagonal (Tiling G sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (3.6.6), también conocido como teselado trihexagonal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Trilateral Tiling I (TriTiling I)

Genera un teselado (grilla) a partir de cualquier curva trilátera, regular o irregular (cualquier polilínea cerrada de 3 puntos y 3 aristas)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Based Curve | `C` | Curve | item | Curva base trilátera (cualquier polilínea cerrada de 3 puntos y 3 aristas) |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trilateral Tiling I | `TT` | Curve | lista | Teselado trilátero |

### Trilateral Tiling II (TriTiling II)

Genera un teselado (grilla) a partir de cualquier curva trilátera, regular o irregular (cualquier polilínea cerrada de 3 puntos y 3 aristas)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Based Curve | `C` | Curve | item | Curva base trilátera (cualquier polilínea cerrada de 3 puntos y 3 aristas) |
| U Count | `U` | Integer | item | Cantidad de repeticiones en la dirección U |
| V Count | `V` | Integer | item | Cantidad de repeticiones en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trilateral Tiling II | `TT` | Curve | lista | Teselado trilátero |

### Truncated hexagonal (Tiling E sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (3.12.12), también conocido como teselado hexagonal truncado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Truncated square (Tiling D sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (4.8.8), también conocido como teselado cuadrado truncado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

### Truncated trihexagonal (Tiling F sr)

Crea un teselado euclidiano semirregular de polígonos convexos con configuración de vértices (4.6.12), también conocido como teselado trihexagonal truncado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la grilla |
| Size | `S` | Number | item | Tamaño de las celdas de la grilla |
| Extend X | `Ex` | Integer | item | Cantidad de celdas de la grilla en la dirección X del plano base |
| Extend Y | `Ey` | Integer | item | Cantidad de celdas de la grilla en la dirección Y del plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid Cells | `C` | Curve | lista | Contornos de las celdas de la grilla |

## Util

### Add Clipping Plane (Clip Plane)

Genera un plano de recorte en Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano de recorte |
| Flip | `FP` | Boolean | item | Invierte el plano de recorte |
| Show/Hide | `SH` | Boolean | item | Mostrar u ocultar el plano de recorte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| id | `id` | Text | item | El ID del plano de recorte |

### Case Formatter (CaseFmt)

Convierte un texto a varios estilos comunes de mayúsculas/minúsculas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto de entrada a formatear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| lowercase | `low` | Text | item | todo en minúsculas |
| UPPERCASE | `UP` | Text | item | TODO EN MAYÚSCULAS |
| Title Case | `Title` | Text | item | Primera Letra De Cada Palabra En Mayúscula |
| camelCase | `camel` | Text | item | primeraPalabraMinúscula, restoCapitalizado (camelCase) |
| PascalCase | `Pascal` | Text | item | TodasLasPalabrasCapitalizadas (PascalCase) |
| snake_case | `snake` | Text | item | palabras_unidas_con_guion_bajo |
| kebab-case | `kebab` | Text | item | palabras-unidas-con-guion |

### Clean Number (CleanNumber)

Convierte el formato científico (y otros formatos numéricos) a números simples

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `N` | Number | item | Número en formato científico |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `N` | Text | item | Número en formato general (texto) |

### Construct Tree Branch (TBranch)

Crea una rama de árbol usando una ruta de rama y elementos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Branch Index | `BP` | Integer | lista | Índice de rama para cada elemento: un entero por elemento (por ejemplo 0,0,1,1,2 → los elementos van a las ramas {0},{1},{2}) |
| Branch Items | `BI` | Generic Data | lista | Elementos a repartir en las ramas: deben coincidir con la cantidad de BP |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree Branch | `TB` | Generic Data | árbol | Rama del árbol |

### Create Material (PMaterial)

Crea un material a partir de una imagen como textura, un color y valores de reflexión y suavidad. (El mapeo de textura se basa en el mapa UV de la superficie.) Usa el material de salida con el componente 'Custom Preview' de Grasshopper

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Texture *(opcional)* | `TP` | Text | item | Ruta de la imagen de textura (ubicación del archivo de imagen) |
| Color | `C` | Colour | item | Color |
| Reflection Value | `R` | Number | item | Debe estar entre 0~1 |
| Smoothness Value | `S` | Number | item | Debe estar entre 0~1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Generic Data | item | Material. Úsalo con el componente 'Custom Preview' de Grasshopper |

### Custom Round

Redondea un número a un paso personalizado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Números a redondear |
| Scope | `S` | Number | item | Paso del redondeo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rounded Numbers | `N` | Number | lista | Números redondeados |

### Delay

Dispara un solo pulso True después de un retraso dado (en segundos) desde un flanco de subida del Trigger.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trigger | `T` | Boolean | item | El flanco de subida (False → True) inicia la cuenta regresiva |
| Seconds | `S` | Number | item | Retraso en segundos antes de disparar el pulso True |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Out | `O` | Boolean | item | Entrega True durante un cálculo después del retraso y luego vuelve a False |

### Delete Files (Del files)

Borra archivos de una carpeta

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| delete | `del` | Boolean | item | Borrar |
| Folder path | `FP` | Text | item | Ruta de la carpeta |
| File names | `FN` | Text | lista | Nombres de los archivos a borrar (por ejemplo: archivo.txt) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Repository files | `EF` | Text | lista | Archivos existentes en la carpeta |

### FaceMe Plane (FaceMe)

Genera un plano orientado hacia la cámara activa. Mientras On esté en True, el resultado se actualiza solo al mover el mouse.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de origen del plano orientado a la cámara |
| On | `On` | Boolean | item | True para activar el seguimiento del mouse, False para desactivarlo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `FP` | Plane | item | Plano orientado hacia la cámara activa |
| CameraPosition | `CP` | Point | item | Posición de la cámara activa |

### Fast Closest Points (FCPs+)

Busca los N puntos más cercanos a cada punto de entrada. Conserva la ruta del árbol de entrada: una rama de salida por punto de entrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | árbol | Puntos de consulta (la estructura del árbol se conserva en la salida) |
| Cloud | `C` | Point | lista | Nube de puntos en la que buscar |
| Number | `N` | Integer | item | Cantidad de puntos más cercanos a buscar por punto de consulta |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest Points | `CP` | Point | árbol | Puntos más cercanos: una rama por punto de entrada |
| Indexes | `iCP` | Integer | árbol | Índices de los puntos más cercanos en la nube: una rama por punto de entrada |
| Distances | `D` | Number | árbol | Distancias a los puntos más cercanos: una rama por punto de entrada |

### Golden Point (GoldenPt)

Crea un punto [C] sobre una línea dada [AB] tal que AC/BC=φ (razón áurea ≈ 2.618)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primer punto |
| Point B | `B` | Point | item | Segundo punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Golden Point | `C` | Point | item | Punto C tal que AC/BC=φ |

### Hide Canvas (HideGH)

Oculta la ventana del editor de Grasshopper.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hide | `H` | Boolean | item | Poner en True para ocultar la ventana de Grasshopper |

### If Value Changed (ValChanged)

Entrega un pulso True cada vez que cambia la lista de enteros de entrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `V` | Integer | lista | Lista de enteros a vigilar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Changed | `C` | Boolean | item | True durante un cálculo cuando cambia la entrada; después False |

### Interpolate Color

Interpola una colección de colores

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colors | `C` | Colour | lista | Colores a interpolar |
| Interpolation Parameters | `t` | Number | lista | Parámetros de interpolación normalizados (entre 0~1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Interpolated Colors | `C` | Colour | lista | Colores interpolados |

### Mouse

Obtiene las coordenadas del cursor y el estado de los botones del mouse

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Triger | `T` | Boolean | item | Poner en 'True' para ejecutar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cursor Position | `P` | Point | item | Coordenadas cartesianas del cursor del mouse como punto |
| Left Mouse Button | `L` | Boolean | item | True si el botón izquierdo del mouse está presionado |
| Middle Mouse Button | `M` | Boolean | item | True si el botón central del mouse está presionado |
| Right Mouse Button | `R` | Boolean | item | True si el botón derecho del mouse está presionado |

### Mouse Buttons Blocker (MouseBlock)

Bloquea de forma selectiva los clics izquierdo, derecho y/o central del mouse en la vista de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Left | `L` | Boolean | item | Bloquear el botón izquierdo del mouse |
| Block Right | `R` | Boolean | item | Bloquear el botón derecho del mouse |
| Block Middle | `M` | Boolean | item | Bloquear el botón central del mouse |

### Number Analyzer (NumAnalyze)

Calcula un conjunto completo de propiedades estadísticas de una lista de números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `V` | Number | lista | Lista de números a analizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Min | `Min` | Number | item | Valor mínimo |
| Max | `Max` | Number | item | Valor máximo |
| Average | `Avg` | Number | item | Media aritmética |
| Mode | `Mode` | Number | item | Valor más frecuente (moda) |
| Median | `Med` | Number | item | Valor central (mediana) |
| Variance | `Var` | Number | item | Varianza |
| Std Dev | `StdDev` | Number | item | Desviación estándar |
| Skewness | `Skew` | Number | item | Asimetría |
| Kurtosis | `Kurt` | Number | item | Curtosis |
| Q1 | `Q1` | Number | item | Primer cuartil |
| Q3 | `Q3` | Number | item | Tercer cuartil |
| IQR | `IQR` | Number | item | Rango intercuartílico |
| Range | `Rng` | Number | item | Máximo menos mínimo |
| Mode Indexes | `MIdx` | Integer | lista | Índices del valor modal en la lista de entrada |
| Histogram Bins | `Hist` | Number | lista | Conteos por intervalo (10 intervalos de igual ancho) |
| Value Index Tree | `VTree` | Integer | árbol | Árbol: cada rama = un valor único; elementos = índices en la lista de entrada |
| Branch Values | `BVals` | Number | lista | Valores únicos correspondientes a cada rama del árbol de índices por valor |

### Pack Curves (PackCrv)

Empaqueta curvas sobre el plano XY (nesting simple)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CT *(opcional)* | `CT` | Curve | árbol | Curvas a anidar como árbol; los elementos de cada rama se consideran una sola pieza y se anidan juntos |
| CP *(opcional)* | `CP` | Plane | árbol | Plano de las curvas: un plano por cada rama de CT |
| D *(opcional)* | `D` | Number | item | Separación del empaquetado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| NR | `NR` | Curve | item | Rectángulo contenedor |
| NC | `NC` | Curve | item | Curvas empaquetadas |

### Reflection Point (ReflectP)

Devuelve el reflejo de un punto [o lista de puntos] respecto de un plano

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto(s) a reflejar |
| Plane | `Pl` | Plane | item | Plano de reflexión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto(s) reflejados |

### RefreshAll (Rfrsh)

Recalcula o refresca todos los componentes del lienzo actual

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Polylines | `B` | Boolean | item | Polilíneas base (celdas) |

### Scissors (Scissor)

Simula una estructura de tijera circular desplegable

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base |
| Number of Elements | `E` | Integer | item | Cantidad de elementos de tijera |
| Width | `W` | Number | item | Ancho de los elementos de tijera |
| Size | `S` | Number | item | Tamaño de los elementos de tijera |
| Deployment Factor | `Df` | Number | item | Un número normalizado [entre 0~1] que determina el estado actual de la estructura de tijera |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Scissors | `SS` | Curve | árbol | Estructura de tijera |
| Scissors Lines | `SSl` | Curve | árbol | Líneas de la estructura de tijera |

### Sequential Activator (Activator)

El activador secuencial genera una lista de valores decimales que se activan progresivamente de 0.0 a 1.0 según un parámetro de entrada normalizado. La activación ocurre en secuencia: el primer valor llega a 1.0 antes de que el segundo empiece a subir, y así sucesivamente, hasta que todos los valores quedan activados cuando la entrada llega a 1.0. Este componente es especialmente útil para controlar animaciones, cadenas paramétricas o comportamientos por etapas en sistemas de diseño. Permite una activación suave y ordenada de los elementos, ideal para efectos en el tiempo, simulaciones o transformaciones paso a paso. Casos de uso: activación por etapas o en cascada en simulaciones (por ejemplo efecto dominó o actuación robótica).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Activation factor *(opcional)* | `f` | Number | item | Entrada de activación normalizada de 0.0 a 1.0. Controla el avance de la secuencia. |
| Count *(opcional)* | `C` | Integer | item | Cantidad de valores secuenciales a entregar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| fs | `fs` | Number | item | Una lista de C valores decimales de 0.0 a 1.0, cada uno se activa a su turno a medida que A aumenta. |

### Text Search (TxtSearch)

Busca una palabra clave en una lista de textos y devuelve los elementos que coinciden.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Texts | `T` | Text | lista | Lista de textos en la que buscar |
| Keyword | `K` | Text | item | Palabra a buscar (sin distinguir mayúsculas) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Found | `F` | Boolean | item | True si se encontró al menos una coincidencia |
| Matches | `M` | Text | lista | Lista de textos que contienen la palabra clave |

### Timer

Entrega True durante una duración dada (en segundos) después de un flanco de subida del Trigger y luego vuelve a False.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trigger | `T` | Boolean | item | El flanco de subida (False → True) inicia el temporizador |
| Seconds | `S` | Number | item | Duración en segundos que se mantiene en True |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Out | `O` | Boolean | item | True mientras el temporizador corre; False en otro caso |

### Unit Changer (UnitChanger)

Cambia las unidades de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| apply | `R` | Boolean | item | Aplicar el cambio |
| Unit Index | `UI` | Integer | item | 0=Angstroms 1=AstronomicalUnits 2=Centimeters 3=CustomUnits 4=Decimeters 5=Dekameters 6=Feet 7=Gigameters 8=Hectometers 9=Inches 10=Kilometers 11=LightYears 12=Megameters 13=Meters 14=Microinches 15=Microns 16=Miles 17=Millimeters 18=Mils 19=Nanometers 20=NauticalMiles 21=None 22=Parsecs 23=PrinterPoints 24=PrinterPicas 25=Yards |
| change Scale | `Sc` | Boolean | item | Poner en True para escalar los objetos de Rhino |

### Value List Controler (VList Cntl)

Controla los nombres y valores de una Value List

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| < Value List | `<` | Generic Data | lista | Conecta aquí una Value List para controlarla |
| Items'Name | `INames` | Text | lista | Lista de nombres de todos los elementos |
| Items'Value | `IValues` | Text | lista | Lista de valores de todos los elementos |

### WirelessGate (WLGate)

Pasa datos de forma inalámbrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Passing switch | `S` | Boolean | item | Activa la transferencia de datos |
| Data | `D` | Generic Data | árbol | Datos a transferir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Target NickName | `Nick` | Text | item | Abreviatura del parámetro de salida dinámico |

### Zoom to (Zoom)

Ubica la cámara a cierta distancia apuntando a un punto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Target point | `P` | Point | item | Punto objetivo de la cámara |
| Reset | `R` | Boolean | item | Poner en 'True' para ejecutar |
| Distance | `D` | Number | item | Distancia de la cámara al punto objetivo |
