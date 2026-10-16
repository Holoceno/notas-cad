---
title: "Catálogo Grasshopper — Pufferfish"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Pufferfish"
libraries: ["Pufferfish 3.0.0.0"]
components: 330
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/pufferfish, geometria/morph, geometria/curvas, geometria/puntos-vectores, matematicas, geometria/superficies, geometria/mallas]
---

# Pufferfish

330 objetos · librería: Pufferfish 3.0.0.0 · autor: Michael Pryor

Mapas: [[Mapa - Morph y tween]] (109) · [[Mapa - Curvas]] (58) · [[Mapa - Puntos, vectores y planos]] (58) · [[Mapa - Matemáticas]] (49) · [[Mapa - Superficies y NURBS]] (43) · [[Mapa - Mallas y SubD]] (37) · [[Mapa - Transformaciones]] (20) · [[Mapa - Brep y sólidos]] (19) · [[Mapa - Visualización y anotaciones]] (9) · [[Mapa - Data trees y listas]] (8) · [[Mapa - Fabricación]] (1)

## Color

### Color To Point (Col2Pt)

Convierte un color en un punto usando los valores RGB del color como valores XYZ del punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color | `Cl` | Colour | item | Color a convertir en punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto resultante del color |
| Alpha | `a` | Integer | item | Valor de transparencia alfa del color (0 = transparencia total, 255 = sin transparencia) |

### Grayscale Color (GrayCol)

Convierte un color a escala de grises con distintos esquemas comunes de ponderación de luminosidad.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color | `Cl` | Colour | item | Color a convertir a escala de grises |
| Luminosity Type | `L` | Integer | item | Determina qué esquema común de ponderación de luminosidad usar: 0 = R*0.2989, G*0.5870, B*0.1140; 1 = R*0.2627, G*0.6780, B*0.0593; 2 = R*0.2126, G*0.7152, B*0.0722; 3 = R*0.3333, G*0.3333, B*0.3333 |
| Alpha | `a` | Boolean | item | Quita la transparencia (valor alfa) del color |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grayscaled | `G` | Colour | item | Color en escala de grises resultante |

### Invert Color (InvCol)

Invierte un color.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color | `Cl` | Colour | item | Color a invertir |
| Alpha | `a` | Boolean | item | Invierte la transparencia (valor alfa) del color |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inverted | `I` | Colour | item | Color invertido resultante |

### Mirror Combine Colors (MirComCols)

Refleja un conjunto de colores desde su final o su inicio y lo combina con el conjunto original.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colors | `Cl` | Colour | lista | Conjunto de colores a reflejar y combinar |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = final del conjunto, True = inicio del conjunto) |
| Join | `J` | Boolean | item | Une el conjunto de colores reflejado y combinado (quita el color duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de colores: 0 = reflejado, 1 = invertido |
| Alpha | `a` | Boolean | item | Invierte las transparencias (valores alfa) de los colores reflejados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirrored | `M` | Colour | lista | Conjunto de colores reflejado y combinado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |

### Mirror Cut Colors (MirCutCols)

Corta un conjunto de colores en un índice, refleja el lado conservado del corte respecto de ese índice y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colors | `Cl` | Colour | lista | Conjunto de colores a cortar y reflejar |
| Mirror Index | `Mi` | Integer | item | Índice respecto del cual se refleja el lado conservado del corte. Un índice negativo invierte el conjunto de colores y quita desde arriba. |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = reflejar después del índice, True = reflejar antes del índice) |
| Join | `J` | Boolean | item | Une el conjunto de colores cortado y reflejado (quita el color duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de colores: 0 = reflejado, 1 = invertido |
| Alpha | `a` | Boolean | item | Invierte las transparencias (valores alfa) de los colores reflejados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Colour | lista | Conjunto de colores cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Intersected | `I` | Boolean | item | True si el índice de reflejo intersectó el conjunto de colores, False si no lo intersectó |

### Point To Color (Pt2Col)

Convierte un punto en un color usando los valores XYZ del punto como valores RGB del color.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto a convertir en color |
| Alpha | `a` | Integer | item | Valor de transparencia alfa para el color (0 = transparencia total, 255 = sin transparencia) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color | `Cl` | Colour | item | Color resultante del punto |

### Tween Consecutive Colors (TwnConCols)

Interpola (tween) consecutivamente entre un conjunto de colores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colors | `Cl` | Colour | lista | Conjunto de colores entre los que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = color en Cl, 1.0 = color en Cl +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de colores de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Alpha | `a` | Boolean | item | Incluye las transparencias (valores alfa) de los colores en la interpolación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Colour | lista | Colores interpolados resultantes |

### Tween Through Colors (TwnThruCols)

Interpola (tween) a través de un conjunto de colores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colors | `Cl` | Colour | lista | Conjunto de colores a través de los cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = color al inicio de Cl, 1.0 = color al final de Cl), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = color en el índice 0, número de índice del último color = color en el último índice). El rango del factor de un color al siguiente es: el número de índice de un color = el color en ese índice, el número de índice del siguiente color = el siguiente color de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un color a medio camino entre el color del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de colores de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de colores de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Alpha | `a` | Boolean | item | Incluye las transparencias (valores alfa) de los colores en la interpolación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Colour | lista | Color interpolado resultante |

### Tween Two Colors (Twn2Cols)

Interpola (tween) entre dos colores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color A | `A` | Colour | item | Color desde el que interpolar |
| Color B | `B` | Colour | item | Color hacia el que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Color A, 1.0 = Color B) |
| Alpha | `a` | Boolean | item | Incluye las transparencias (valores alfa) de los colores en la interpolación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Colour | item | Color interpolado resultante |

## Curve

### Align Curve Seams (AliCrvSeams)

Alinea las costuras de un conjunto de curvas cerradas, de forma iterativa o no, a partir de la primera curva del conjunto (u opcionalmente de un punto guía inicial), con la opción de ajustarlas a las esquinas. Si una curva no es cerrada, sale sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas cerradas cuyas costuras se alinean |
| Guide *(opcional)* | `G` | Point | item | Punto guía opcional para el inicio de la alineación de costuras (reemplaza la ubicación de la costura de la primera curva del conjunto) |
| Seam *(opcional)* | `t` | Number | item | Parámetro para ajustar la costura de la primera curva del conjunto (salvo que se use un punto guía) |
| Snap | `S` | Boolean | item | Si la curva tiene esquinas, ajusta la costura alineada a la esquina o quiebre más cercano |
| Iterative | `I` | Boolean | item | Si es True, la costura de cada curva se alinea en secuencia con la costura ajustada de la curva anterior del conjunto. Si es False, la costura de cada curva se alinea directamente con la costura de la primera curva o con el punto guía inicial opcional |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Aligned | `A` | Curve | lista | Curvas resultantes con las costuras alineadas |
| Points | `P` | Point | lista | Puntos en las costuras alineadas de las curvas |
| Result Boolean | `R` | Boolean | lista | True si la curva es cerrada y tiene la costura alineada, False si la curva es abierta |

### Arc/Circle/Ellipse (ACE)

Obtiene la representación como arco, círculo o elipse de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de la que obtener el arco, círculo o elipse |
| Get Type | `T` | Integer | item | Determina qué tipo de curva obtener: 0 = arco, 1 = círculo, 2 = elipse |
| Tolerance | `t` | Number | item | Tolerancia para obtener el arco, círculo o elipse (si se omite, se usa la tolerancia de distancia cero de RhinoMath, 1.0e-12) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc/Circle/Ellipse | `ACE` | Generic Data | item | Arco, círculo o elipse resultante |

### Average Curve (AvrCrv)

Calcula el promedio aritmético de un conjunto de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas a promediar |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da promedios de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da promedios de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Curve | item | Media aritmética (promedio) de todas las curvas de entrada |

### Bounding Rectangle (BRec)

Crea un rectángulo contenedor orientado a un plano que une toda la geometría, o rectángulos contenedores separados para cada geometría.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría a contener con el rectángulo contenedor |
| Plane | `Pl` | Plane | item | Plano de orientación del rectángulo contenedor |
| Axis | `A` | Integer | item | Eje del plano de orientación a lo largo del cual buscar el rectángulo contenedor: 0 = eje {z} del plano, 1 = eje {y} del plano, 2 = eje {x} del plano |
| Slide | `S` | Number | item | Desliza el rectángulo contenedor a lo largo del eje (0.0 = inicio del volumen contenedor, 1.0 = final del volumen contenedor) |
| Union | `U` | Boolean | item | Si es True, se crea un solo rectángulo contenedor para toda la geometría de entrada. Si es False, cada geometría tiene su propio rectángulo contenedor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bounding | `B` | Rectangle | lista | Rectángulo o rectángulos contenedores resultantes |
| Dimension X | `X` | Number | lista | Dimensión {x} en el plano del o los rectángulos contenedores |
| Dimension Y | `Y` | Number | lista | Dimensión {y} en el plano del o los rectángulos contenedores |

### Close Curve (ClsCrv)

Cierra una curva abierta de distintas formas; si la curva ya es cerrada o es lineal, sale sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a cerrar |
| Close Type | `T` | Integer | item | Determina cómo se cierra la curva: 0 = lineal, 1 = tangencia, 2 = curvatura, 3 = unir extremos |
| Bulge | `B` | Number | item | Factor de abombamiento del segmento de cierre de la curva |
| Tolerance | `t` | Number | item | Distancia permitida opcional entre el inicio y el final de la curva. Si la abertura es mayor que la tolerancia, la curva no se cierra. Si la tolerancia es 0.0, la curva se cierra sin importar el tamaño de la abertura. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closed | `C` | Curve | item | Curva cerrada resultante |
| Result Boolean | `R` | Boolean | item | True si la curva abierta se cerró, False si no se cerró o ya estaba cerrada |

### Compatibilize Polylines (ComPLines)

Hace compatibles (iguales) en cantidad de puntos de control un conjunto de polilíneas, sin cambiar su forma.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `Pl` | Curve | lista | Conjunto de polilíneas a hacer compatibles |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Compatibilized | `C` | Curve | lista | Polilíneas compatibles resultantes |
| Result Boolean | `R` | Boolean | lista | True si la polilínea se hizo compatible (cambió su cantidad de puntos de control), False si ya era compatible |

### Constrained Area Ellipse (ConsAreaEli)

Crea una elipse o círculo del tamaño de un área dada, con factores de proporción {x} e {y}, centrado en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base de la elipse |
| Area | `A` | Number | item | Área de la elipse |
| Factor X | `x` | Number | item | Factor de proporción en la dirección {x} del plano (usa el mismo valor para {x} e {y} para un círculo) |
| Factor Y | `y` | Number | item | Factor de proporción en la dirección {y} del plano (usa el mismo valor para {x} e {y} para un círculo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ellipse | `E` | Curve | item | Elipse resultante restringida por área |

### Constrained Area Polygon (ConsAreaPly)

Crea un polígono irregular o regular del tamaño de un área dada, con factores de proporción {x} e {y}, centrado en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base del polígono |
| Sides | `S` | Integer | item | Cantidad de lados del polígono |
| Area | `A` | Number | item | Área del polígono |
| Factor X | `x` | Number | item | Factor de proporción en la dirección {x} del plano (usa el mismo valor para {x} e {y} para un polígono regular) |
| Factor Y | `y` | Number | item | Factor de proporción en la dirección {y} del plano (usa el mismo valor para {x} e {y} para un polígono regular) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon | `P` | Curve | item | Polígono resultante restringido por área |

### Constrained Area Rectangle (ConsAreaRec)

Crea un rectángulo o cuadrado del tamaño de un área dada, con factores de proporción {x} e {y}, centrado en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base del rectángulo |
| Area | `A` | Number | item | Área del rectángulo |
| Factor X | `x` | Number | item | Factor de proporción en la dirección {x} del plano (usa el mismo valor para {x} e {y} para un cuadrado) |
| Factor Y | `y` | Number | item | Factor de proporción en la dirección {y} del plano (usa el mismo valor para {x} e {y} para un cuadrado) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo resultante restringido por área |
| Dimension X | `X` | Number | item | Dimensión {x} en el plano del rectángulo |
| Dimension Y | `Y` | Number | item | Dimensión {y} en el plano del rectángulo |

### Curve Align Curve Seams (CrvAliCrvSeams)

Alinea las costuras de un conjunto de curvas cerradas a lo largo de una curva guía, con la opción de ajustarlas a las esquinas. Si una curva no es cerrada, sale sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas cerradas cuyas costuras se alinean |
| Guide | `G` | Curve | item | Curva guía a lo largo de la cual alinear las costuras |
| Snap | `S` | Boolean | item | Si la curva tiene esquinas, ajusta la costura alineada a la esquina o quiebre más cercano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Aligned | `A` | Curve | lista | Curvas resultantes con las costuras alineadas |
| Points | `P` | Point | lista | Puntos en las costuras alineadas de las curvas |
| Result Boolean | `R` | Boolean | lista | True si la curva es cerrada y tiene la costura alineada, False si la curva es abierta |

### Curve Degree (CrvDeg)

Obtiene el valor del grado de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de la que obtener el grado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Degree | `D` | Integer | item | Valor del grado de la curva |

### Curve Length At (CrvLenAt)

Obtiene la longitud a lo largo de una curva desde su inicio hasta un punto de la curva (u opcionalmente hasta un parámetro); si el punto no está sobre la curva, se lleva hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual medir |
| Point *(opcional)* | `P` | Point | item | Punto de la curva hasta el que medir |
| Parameter *(opcional)* | `t` | Number | item | Parámetro opcional de la curva hasta el que medir en vez de un punto (reemplaza al punto si también se entrega uno) |
| Normalized | `N` | Boolean | item | Si es True, la longitud de salida está normalizada (0.0 - 1.0) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L` | Number | item | Longitud a lo largo de la curva desde el inicio hasta el punto |
| Parameter | `t` | Number | item | Parámetro de la curva en el punto |

### Curve Length Between (CrvLenBtwn)

Obtiene las longitudes a lo largo de una curva entre puntos de la curva (u opcionalmente entre parámetros); si los puntos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual medir |
| Points *(opcional)* | `P` | Point | lista | Conjunto de puntos de la curva entre los que medir |
| Parameters *(opcional)* | `t` | Number | lista | Conjunto opcional de parámetros de la curva entre los que medir en vez de puntos (reemplaza a los puntos si también se entregan) |
| Normalized | `N` | Boolean | item | Si es True, las longitudes de salida están normalizadas (0.0 - 1.0) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lengths | `L` | Number | lista | Longitudes a lo largo de la curva entre los puntos |
| Parameters | `t` | Number | lista | Parámetros de la curva en los puntos |

### Curve Spans (CrvSpans)

Obtiene el subdominio de cada tramo (span) de una curva e información de los tramos: cantidad, longitud de cada uno, grado de cada uno y parámetros de la curva en sus extremos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de la que obtener información de los tramos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sub-Domains | `S` | Domain | lista | Subdominio de cada tramo que forma la curva. Para extraer cada tramo como curva separada, usa estos valores como entrada Domain (D) del componente Sub Curve de Grasshopper. |
| Amount | `A` | Integer | item | Cantidad de tramos que forman la curva |
| Lengths | `L` | Number | lista | Longitud de cada tramo que forma la curva |
| Degrees | `D` | Integer | lista | Grado de cada tramo que forma la curva |
| Parameters | `t` | Number | lista | Parámetros de la curva en los extremos de los tramos. Para obtener el punto entre cada tramo, usa estos valores como entrada Parameters (t) del componente Evaluate Curve de Grasshopper. |

### Curve Statistics (CrvStats)

Obtiene estadísticas de una curva: cantidad de puntos de control, de puntos de edición, de quiebres, de segmentos, de tramos y de vectores de nodos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de la que obtener estadísticas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Control Point Count | `C` | Integer | item | Cantidad de puntos de control de la curva |
| Edit Point Count | `E` | Integer | item | Cantidad de puntos de edición de la curva |
| Kink Point Count | `K` | Integer | item | Cantidad de puntos de quiebre de la curva |
| Segment Count | `S` | Integer | item | Cantidad de segmentos de la curva |
| Span Count | `S` | Integer | item | Cantidad de tramos de la curva |
| Knot Vector Count | `K` | Integer | item | Cantidad de vectores de nodos de la curva |

### Discrete Polyline (DPLine)

Crea una polilínea formada por segmentos orientados según vectores objetivo, buscando para cada vector entre los vértices de referencia el vector objetivo más cercano en ángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| References | `R` | Point | lista | Vértices de referencia |
| Targets | `T` | Vector | lista | Conjunto de vectores objetivo |
| Keep Length | `K` | Boolean | item | Mantiene las longitudes entre los vértices de referencia para los segmentos de la polilínea discreta; la polilínea resultante se desvía más de los vértices de referencia, pero tiene la misma longitud que tendría una polilínea normal por esos vértices |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Discrete | `D` | Curve | item | Polilínea discreta resultante |

### Fit Curve Segments (FitCrvSegs)

Busca en una curva los segmentos de los grados indicados y ajusta nuevos segmentos a través de ellos con un grado dado, sin cambiar la forma general.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva cuyos segmentos se ajustan |
| Search | `S` | Integer | lista | Valores de grado de los segmentos a buscar |
| Degree *(opcional)* | `D` | Integer | item | Grado al que ajustar los segmentos buscados (si se omite, se usan los grados de los segmentos de la curva de entrada) |
| Deviation Tolerance | `d` | Number | item | Distancia de tolerancia que la curva ajustada puede desviarse de la curva a ajustar (si se omite, se usa la tolerancia del documento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fitted | `F` | Curve | item | Curva resultante con los segmentos ajustados |
| Amount | `A` | Integer | item | Cantidad de segmentos que forman la curva |
| Degrees F | `fD` | Integer | lista | Grado de cada segmento que forma la curva ajustada resultante |
| Degrees C | `cD` | Integer | lista | Grado de cada segmento que forma la curva de entrada |
| Result Booleans | `R` | Boolean | lista | True si el segmento de la curva se ajustó, False si no |

### Fit Curve Smooth (FitCrvSmo)

Ajusta una nueva curva a una curva existente suavizando los ángulos de quiebre, sin cambiar la forma general.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a ajustar |
| Degree *(opcional)* | `D` | Integer | item | Grado al que ajustar la curva (si se omite, se usa el grado de la curva de entrada) |
| Deviation Tolerance | `d` | Number | item | Distancia de tolerancia que la curva ajustada puede desviarse de la curva a ajustar (si se omite, se usa la tolerancia del documento) |
| Angle Tolerance | `a` | Number | item | Ángulo de tolerancia en grados para suavizar los quiebres (si se omite, se usa la tolerancia angular del documento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fitted | `F` | Curve | item | Curva ajustada resultante |

### Is Arc/Circle/Ellipse (IsACE)

Prueba si una curva es un arco, un círculo o una elipse según la definición de Rhino. Una curva puede ser de varios tipos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a probar si es arco, círculo o elipse |
| Tolerance | `t` | Number | item | Tolerancia para determinar si una curva es arco, círculo o elipse (si se omite, se usa la tolerancia de distancia cero de RhinoMath, 1.0e-12) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Boolean | item | True si la curva es un arco |
| Circle | `C` | Boolean | item | True si la curva es un círculo |
| Ellipse | `E` | Boolean | item | True si la curva es una elipse |

### Is Curve Kinky (CrvKinky)

Prueba si una curva tiene quiebres y obtiene información de ellos: cantidad y longitud a lo largo de la curva donde está cada uno.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva en la que buscar quiebres |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Kinked | `K` | Boolean | item | True si la curva tiene quiebres |
| Amount | `A` | Integer | item | Cantidad de quiebres de la curva |
| Lengths | `L` | Number | lista | Longitud a lo largo de la curva donde está cada quiebre |

### Is Curve Linear (CrvLinr)

Prueba si una curva es lineal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a probar si es lineal |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linear | `L` | Boolean | item | True si la curva es lineal |

### Is Curve Segmented (CrvSegs)

Prueba si una curva tiene segmentos y obtiene información de ellos: cantidad, longitud de cada uno y grado de cada uno.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva en la que buscar segmentos y obtener su información. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Segments | `S` | Boolean | item | True si la curva tiene más de un segmento |
| Amount | `A` | Integer | item | Cantidad de segmentos que forman la curva |
| Lengths | `L` | Number | lista | Longitud de cada segmento que forma la curva |
| Degrees | `D` | Integer | lista | Grado de cada segmento que forma la curva |

### Mesh Loop Edges (MshLoopEdgs)

Extrae las polilíneas de los bucles de aristas (edge loops) de una malla de cuadriláteros en un índice de vértice dado. Métodos base de Mateusz Zwierzycki

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de cuadriláteros de la que extraer las polilíneas de los bucles de aristas |
| Index | `i` | Integer | item | Índice del vértice de la malla en el que extraer las polilíneas de los bucles de aristas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Loops | `L` | Curve | lista | Polilíneas resultantes de los bucles de aristas de la malla |

### Mesh Naked Edges (MshNakedEdgs)

Extrae las polilíneas de las aristas desnudas de una malla, si existen.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de la que obtener las polilíneas de aristas desnudas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Naked | `N` | Curve | lista | Polilíneas resultantes de las aristas desnudas de la malla |
| Result Boolean | `R` | Boolean | item | True si la malla tiene aristas desnudas, False si no tiene |

### Mirror Cut Curve (MirCutCrv)

Corta una curva con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a cortar y reflejar |
| Mirror Plane | `MP` | Plane | item | Plano respecto del cual se refleja el lado conservado del corte de la curva |
| Reach | `R` | Number | item | Las partes de la curva a menos de esta distancia del plano de reflejo también se cortan |
| Offset | `O` | Number | item | Distancia de desfase de las partes conservadas de la curva respecto del plano de reflejo (o desde el alcance, si el alcance no es cero) |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo |
| Join | `J` | Boolean | item | Une las curvas cortadas y reflejadas |
| Keep | `K` | Boolean | item | Conserva la curva y la refleja normalmente si el corte la hace desaparecer |
| Connection Type | `T` | Integer | item | Determina cómo se conectan las curvas cortadas y reflejadas: 0 = lineal, 1 = tangencia, 2 = curvatura, 3 = unir extremos |
| Bulge | `B` | Number | item | Factor de abombamiento de las conexiones de las curvas cortadas y reflejadas (-B = abombamiento negativo, 0.0 = sin abombamiento, +B = abombamiento positivo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Curve | lista | Curvas cortadas y reflejadas resultantes |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de curvas cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Reach Plane | `RP` | Plane | item | El plano a la distancia de alcance |
| Offset Plane | `OP` | Plane | item | El plano a la distancia de desfase |
| Intersected | `I` | Boolean | item | True si el corte con reflejo intersectó la curva, False si no la intersectó |

### Net On Surface (NetSrf)

Crea una red de curvas interpoladas sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie sobre la que aplicar la red |
| Count U | `U` | Integer | item | Cantidad de curvas de la red en la dirección {u} |
| Count V | `V` | Integer | item | Cantidad de ondas de la red en la dirección {v} |
| Flip | `F` | Boolean | item | Invierte la dirección de las curvas de la red sobre la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de la red sobre la superficie |

### Offset Curve (OffCrv)

Aplica offset a una curva, con la opción de hacerlo hacia ambos lados a distancias distintas y tapar los extremos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que aplicar offset |
| Plane | `Pl` | Plane | item | Plano para la operación de offset |
| Distance | `D` | Number | item | Distancia de offset |
| Both Sides | `B` | Number | item | Distancia de offset opcional para ambos lados; usa el número inverso de la distancia para el offset en la dirección opuesta (si la distancia es positiva usa un número negativo, y viceversa) |
| Kinks | `K` | Integer | item | Si la curva tiene quiebres, determina cómo se les aplica offset: 0 = agudo, 1 = redondo, 2 = suave, 3 = chaflán |
| Cap Type | `T` | Integer | item | Determina cómo tapar los extremos de la curva: 0 = ninguno, 1 = lineal, 2 = tangencia, 3 = curvatura |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset | `O` | Curve | lista | Curva con offset resultante |

### Offset Curve From Surface (OffCrvFromSrf)

Aplica offset a una curva alejándola de una superficie según las direcciones normales de la superficie, con la opción de hacerlo hacia ambos lados a distancias distintas y tapar los extremos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a alejar de la superficie con offset |
| Surface | `S` | Surface | item | Superficie de la que alejar la curva |
| Distance | `D` | Number | item | Distancia de offset desde la superficie |
| Both Sides | `B` | Number | item | Distancia de offset opcional para ambos lados; usa el número inverso de la distancia para el offset en la dirección opuesta (si la distancia es positiva usa un número negativo, y viceversa) |
| Cap Type | `T` | Integer | item | Determina cómo tapar los extremos de la curva: 0 = ninguno, 1 = lineal, 2 = tangencia, 3 = curvatura |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset | `O` | Curve | lista | Curva con offset resultante desde la superficie |

### Open Curve (OpnCrv)

Abre una curva cerrada desde su costura, o acorta una curva abierta desde sus extremos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a abrir |
| Length | `L` | Number | item | Longitud de curva a quitar: a cada lado de la costura en curvas cerradas, desde cada extremo en curvas abiertas (si se omite, se usa la tolerancia del documento) |
| Normalized | `N` | Boolean | item | Si es True, la longitud se usa normalizada (0.5 = mitad de la curva). Si es False, se usa la longitud real (longitud de la curva/2 = mitad de la curva). |
| Seam | `t` | Number | item | Parámetro para ajustar el lugar de apertura (costura) de una curva cerrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Opened | `O` | Curve | item | Curva abierta resultante |
| Result Boolean | `R` | Boolean | item | True si la curva cerrada se abrió, False si no se abrió o ya estaba abierta |

### Parameter Curve Divide Rectangle (ParamCrvDivRec)

Genera una grilla de curvas sobre un rectángulo dividiendo su dominio con parámetros {x} e {y}, o genera una isocurva del rectángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo a dividir |
| Parameters X *(opcional)* | `x` | Number | lista | Parámetros de división a lo largo del dominio {x} del rectángulo, para curvas que van en la dirección {y}; usa un solo valor para hacer una isocurva del rectángulo ({x} 0.0 = inicio del rectángulo, 1.0 = final). Para mejores resultados, los parámetros {x} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters Y *(opcional)* | `y` | Number | lista | Parámetros de división a lo largo del dominio {y} del rectángulo, para curvas que van en la dirección {x}; usa un solo valor para hacer una isocurva del rectángulo ({y} 0.0 = inicio del rectángulo, 1.0 = final). Para mejores resultados, los parámetros {y} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves X | `X` | Curve | lista | Curvas de división resultantes sobre el rectángulo, en la dirección {x} |
| Curves Y | `Y` | Curve | lista | Curvas de división resultantes sobre el rectángulo, en la dirección {y} |

### Parameter Curve Divide Surface (ParamCrvDivSrf)

Genera una grilla de curvas sobre una superficie dividiendo su dominio con parámetros {u} y {v}, o genera una isocurva de la superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir |
| Parameters U *(opcional)* | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie, para curvas que van en la dirección {v}; usa un solo valor para hacer una isocurva de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V *(opcional)* | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la superficie, para curvas que van en la dirección {u}; usa un solo valor para hacer una isocurva de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves U | `U` | Curve | lista | Curvas de división resultantes sobre la superficie, en la dirección {u} |
| Curves V | `V` | Curve | lista | Curvas de división resultantes sobre la superficie, en la dirección {v} |

### Parameter Rectangle Grid (ParamRecGrid)

Genera una grilla de celdas rectangulares en un rectángulo dividiendo su dominio con parámetros {x} e {y}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo a dividir |
| Parameters X | `x` | Number | lista | Parámetros de división a lo largo del dominio {x} del rectángulo ({x} 0.0 = inicio del rectángulo, 1.0 = final). Para mejores resultados, los parámetros {x} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters Y | `y` | Number | lista | Parámetros de división a lo largo del dominio {y} del rectángulo ({y} 0.0 = inicio del rectángulo, 1.0 = final). Para mejores resultados, los parámetros {y} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Rectangle | árbol | Contornos de las celdas de la grilla resultante en el rectángulo |
| Points | `P` | Point | árbol | Puntos en las esquinas de la grilla |

### Parameter Rectangle Isocurve (ParamRecIso)

Genera una isocurva sobre un rectángulo a partir de un parámetro {x} o {y} que divide su dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo del que obtener la isocurva |
| Parameter | `t` | Number | item | Parámetro de la isocurva a lo largo del rectángulo (0.0 = inicio de la dirección, 1.0 = final de la dirección) |
| Direction | `D` | Boolean | item | Si es True, obtiene la isocurva que va en la dirección {x} del rectángulo. Si es False, la que va en la dirección {y} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Isocurve | `I` | Curve | item | Isocurva resultante sobre el rectángulo |

### Parameter Surface Grid (ParamSrfGrid)

Genera una grilla de celdas rectangulares sobre una superficie dividiendo su dominio con parámetros {u} y {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Curve | árbol | Contornos de las celdas de la grilla resultante sobre la superficie. Para llevar las celdas a la curvatura de la superficie, usa el componente Pull Curve de Grasshopper |
| Points | `P` | Point | árbol | Puntos en las esquinas de la grilla |

### Parameter Surface Isocurve (ParamSrfIso)

Genera una isocurva sobre una superficie a partir de un parámetro {u} o {v} que divide su dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie de la que obtener la isocurva |
| Parameter | `t` | Number | item | Parámetro de la isocurva a lo largo de la superficie (0.0 = inicio de la dirección, 1.0 = final de la dirección) |
| Direction | `D` | Boolean | item | Si es True, obtiene la isocurva que va en la dirección {u} de la superficie. Si es False, la que va en la dirección {v} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Isocurve | `I` | Curve | item | Isocurva resultante sobre la superficie |

### Plane Trim Curve (PlnTrimCrv)

Recorta (quita) las partes de una curva que están a un lado de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Plane | `Pl` | Plane | item | Plano con el que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Curve | lista | Curvas recortadas resultantes |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de intersección del plano con la curva |
| Intersected | `I` | Boolean | item | True si el plano recortó la curva, False si no |

### Point Fit Rectangle (PtFitRec)

Ajusta un rectángulo a un conjunto de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos al que ajustar el rectángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fit | `F` | Rectangle | item | Rectángulo resultante ajustado al conjunto de puntos |

### Points Trim Curve (PtsTrimCrv)

Recorta una curva con un conjunto de puntos (u opcionalmente de parámetros) como un patrón de trazos; si los puntos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Points *(opcional)* | `P` | Point | lista | Puntos con los que recortar |
| Parameters *(opcional)* | `t` | Number | lista | Parámetros opcionales con los que recortar en vez de puntos (reemplazan a los puntos si también se entregan) |
| Flip | `F` | Boolean | item | Invierte el patrón de recorte para cambiar qué partes de la curva se quitan |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Curve | lista | Curvas recortadas resultantes |
| Sub-Domains | `S` | Domain | lista | Subdominio de la curva para cada parte que queda después del recorte |
| Intersected | `I` | Boolean | item | True si los puntos recortaron la curva, False si no |

### Prude Curve (PrudeCrv)

Quita las partes con quiebres de una curva (discontinuidades) mezclando sus segmentos; si la curva no tiene quiebres, sale sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a la que quitar los quiebres |
| Length | `L` | Number | item | Longitud a lo largo de la curva desde el quiebre hasta el inicio de la mezcla (si se omite, se usa la tolerancia del documento) |
| Blend Type | `T` | Integer | item | Determina cómo se mezclan los quiebres: 0 = tangencia, 1 = curvatura |
| Bulge | `B` | Number | item | Factor de abombamiento de la mezcla del quiebre |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Prude | `P` | Curve | item | Curva resultante sin quiebres |
| Result Boolean | `R` | Boolean | item | True si se quitaron quiebres de la curva, False si la curva ya no tenía quiebres |

### Rebuild Curve (RebCrv)

Reconstruye una curva con una cantidad de puntos, un grado y un dominio dados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a reconstruir |
| Count *(opcional)* | `P` | Integer | item | Cantidad de puntos de control (si se omite, se usa la de la curva de entrada) |
| Degree *(opcional)* | `D` | Integer | item | Grado de la curva (si se omite, se usa el de la curva de entrada) |
| Domain *(opcional)* | `I` | Domain | item | Dominio de la curva (si se omite, se usa el de la curva de entrada) |
| End Tangents | `E` | Boolean | item | Conserva las tangentes de los extremos de la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rebuilt | `R` | Curve | item | Curva reconstruida resultante |

### Rebuild Curve Segments (RebCrvSegs)

Busca en una curva los segmentos de los grados indicados y los reconstruye con un grado y una cantidad de puntos de control dados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva cuyos segmentos se reconstruyen |
| Search | `S` | Integer | lista | Valores de grado de los segmentos a buscar |
| Degree *(opcional)* | `D` | Integer | item | Grado con que reconstruir los segmentos buscados (si se omite, se usan los grados de los segmentos de la curva de entrada) |
| Count *(opcional)* | `P` | Integer | item | Cantidad de puntos de control con que reconstruir los segmentos buscados (si se omite, se usan las de los segmentos de la curva de entrada) |
| End Tangents | `E` | Boolean | item | Conserva las tangentes de los extremos de los segmentos reconstruidos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rebuilt | `R` | Curve | item | Curva resultante con los segmentos reconstruidos |
| Amount | `A` | Integer | item | Cantidad de segmentos que forman la curva |
| Degrees R | `rD` | Integer | lista | Grado de cada segmento que forma la curva resultante con segmentos reconstruidos |
| Degrees C | `cD` | Integer | lista | Grado de cada segmento que forma la curva de entrada |
| Result Booleans | `R` | Boolean | lista | True si el segmento de la curva se reconstruyó, False si no |

### Relocate Curve Ends (ReCrvEnds)

Reubica los extremos de una curva en nuevos puntos inicial y final sin tener que reconstruir la curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva cuyos puntos extremos se reubican |
| Start *(opcional)* | `S` | Point | item | Punto al que reubicar el inicio de la curva (si no se entrega, el inicio no se reubica) |
| End *(opcional)* | `E` | Point | item | Punto al que reubicar el final de la curva (si no se entrega, el final no se reubica) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Relocated | `R` | Curve | item | Curva resultante con los extremos reubicados |

### Remap Curve Domain (ReCrvDom)

Reasigna el rango del dominio {t} de una curva a un rango de entrada, con la opción de igualar el rango del dominio {t} de una curva guía.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva cuyo rango de dominio {t} se reasigna |
| Guide *(opcional)* | `G` | Curve | item | Curva guía opcional cuyo rango de dominio {t} se iguala (reemplaza al dominio si también se entrega uno) |
| Domain *(opcional)* | `I` | Domain | item | Rango de dominio al que reasignar la curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Remapped | `R` | Curve | item | Curva resultante con el rango de dominio {t} reasignado |
| Original | `O` | Domain | item | El rango original del dominio {t} de la curva |
| New | `N` | Domain | item | El nuevo rango del dominio {t} de la curva |

### Reparameterize Curve (ReparamCrv)

Reparametriza una curva para que su dominio (t) vaya de 0 a 1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a reparametrizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reparameterized | `R` | Curve | item | Curva reparametrizada resultante, con dominio (t) de 0 a 1 |
| Original | `O` | Domain | item | El rango original del dominio (t) de la curva |

### Seam To Curve Corner (Seam2CrvCorn)

Ajusta la costura de una curva cerrada con esquinas para que quede en la esquina más cercana a la costura inicial (u opcionalmente a un punto guía); si la curva no es cerrada o no tiene esquinas, sale sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva cerrada con esquinas cuya costura se ajusta |
| Guide *(opcional)* | `G` | Point | item | Punto guía opcional para buscar la esquina más cercana (reemplaza la ubicación inicial de la costura) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Adjusted | `A` | Curve | item | Curva resultante con la costura ajustada a la esquina más cercana |
| Point | `P` | Point | item | Punto en la costura de la curva ajustada a la esquina más cercana |
| Result Boolean | `R` | Boolean | item | True si la curva es cerrada y tiene la costura en una esquina, False si la curva es abierta o no tiene esquinas |

### Slide Curve Along Curve (SlideCrvCrv)

Desliza una curva a lo largo de una curva guía (u opcionalmente de dos curvas guía).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a deslizar a lo largo de la curva guía |
| Guide 1 | `G¹` | Curve | item | Curva guía a lo largo de la cual deslizar |
| Guide 2 *(opcional)* | `G²` | Curve | item | Segunda curva guía opcional a lo largo de la cual deslizar (mejor si va en la dirección de Guide 1) |
| Factor | `F` | Number | lista | Factor de deslizamiento (0.0 = inicio, 1.0 = final) |
| Align | `A` | Boolean | item | Alinea la curva deslizada con la curva de entrada, cuando se usa una sola curva guía |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da deslizamientos de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da deslizamientos de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Slid | `S` | Curve | lista | Curva resultante deslizada a lo largo de la curva |

### Smooth Curve (SmoCrv)

Suaviza una curva de forma recursiva (fairing) sin cambiar su cantidad de puntos de control.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a suavizar |
| Steps | `N` | Integer | item | Cantidad de pasos recursivos de suavizado |
| Start Type | `S` | Integer | item | Determina cómo se conserva el inicio de la curva: 0 = conservar solo el punto inicial, 1 = conservar los dos primeros puntos, 2 = conservar los tres primeros puntos |
| End Type | `E` | Integer | item | Determina cómo se conserva el final de la curva: 0 = conservar solo el punto final, 1 = conservar los dos últimos puntos, 2 = conservar los tres últimos puntos |
| Deviation Tolerance | `d` | Number | item | Distancia de tolerancia que la curva suavizada puede desviarse de la curva a suavizar |
| Angle Tolerance | `a` | Number | item | Ángulo de tolerancia en grados para suavizar los quiebres |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Smoothed | `S` | Curve | item | Curva suavizada resultante |

### Superimpose Curve (SuperCrv)

Superpone la cantidad de puntos de control, el grado y el dominio de una curva de referencia sobre una curva objetivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reference | `R` | Curve | item | Curva de referencia de la que tomar las propiedades |
| Target | `T` | Curve | item | Curva objetivo sobre la que superponer las propiedades |
| Points | `P` | Boolean | item | Superpone los puntos de control de la curva de referencia sobre la curva objetivo |
| Degree | `D` | Boolean | item | Superpone el grado de la curva de referencia sobre la curva objetivo |
| Domain | `I` | Boolean | item | Superpone el dominio de la curva de referencia sobre la curva objetivo |
| End Tangents | `E` | Boolean | item | Conserva las tangentes de los extremos de la curva objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Superimposed | `S` | Curve | item | Curva superpuesta resultante |

### Tween Consecutive Curves (TwnConCrvs)

Interpola (tween) consecutivamente entre un conjunto de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas entre las que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = curva en C, 1.0 = curva en C +1) |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = recto, 1 = normal, 2 = ajustado, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | lista | Curvas interpoladas resultantes |

### Tween Consecutive Curves Along Curve (TwnConCrvsCrv)

Interpola (tween) consecutivamente entre un conjunto de curvas a lo largo de una curva guía (u opcionalmente de dos curvas guía).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas sobre la curva guía entre las que interpolar |
| Guide 1 | `G¹` | Curve | item | Curva guía a lo largo de la cual interpolar (mejor si va de la primera curva de C a la última) |
| Guide 2 *(opcional)* | `G²` | Curve | item | Segunda curva guía opcional a lo largo de la cual interpolar (mejor si va en la dirección de Guide 1) |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = curva en C, 1.0 = curva en C +1) |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | lista | Curvas interpoladas resultantes a lo largo de la curva |

### Tween Consecutive Curves On Surface (TwnConCrvsSrf)

Interpola (tween) consecutivamente entre un conjunto de curvas sobre una superficie; si las curvas no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas sobre la superficie entre las que interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar las curvas |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = curva en C, 1.0 = curva en C +1) |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = recto, 1 = normal, 2 = ajustado, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | lista | Curvas interpoladas resultantes sobre la superficie |

### Tween Through Curves (TwnThruCrvs)

Interpola (tween) a través de un conjunto de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas a través de las cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = curva al inicio de C, 1.0 = curva al final de C), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = curva en el índice 0, número de índice de la última curva = curva en el último índice). El rango del factor de una curva a la siguiente es: el número de índice de una curva = la curva en ese índice, el número de índice de la siguiente curva = la siguiente curva de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una curva a medio camino entre la curva del índice 2 y la del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de curvas de entrada |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = recto, 1 = normal, 2 = ajustado, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | lista | Curva interpolada resultante |

### Tween Through Curves Along Curve (TwnThruCrvsCrv)

Interpola (tween) a través de un conjunto de curvas a lo largo de una curva guía (u opcionalmente de dos curvas guía).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas sobre la curva guía a través de las cuales interpolar |
| Guide 1 | `G¹` | Curve | item | Curva guía a lo largo de la cual interpolar (mejor si va de la primera curva de C a la última) |
| Guide 2 *(opcional)* | `G²` | Curve | item | Segunda curva guía opcional a lo largo de la cual interpolar (mejor si va en la dirección de Guide 1) |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = curva al inicio de C, 1.0 = curva al final de C), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = curva en el índice 0, número de índice de la última curva = curva en el último índice). El rango del factor de una curva a la siguiente es: el número de índice de una curva = la curva en ese índice, el número de índice de la siguiente curva = la siguiente curva de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una curva a medio camino entre la curva del índice 2 y la del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo de las guías entre las curvas extremas, sin considerar las ubicaciones del conjunto de curvas de entrada |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | lista | Curva interpolada resultante a lo largo de la curva |

### Tween Through Curves On Surface (TwnThruCrvsSrf)

Interpola (tween) a través de un conjunto de curvas sobre una superficie; si las curvas no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas sobre la superficie a través de las cuales interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar la curva |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = curva al inicio de C, 1.0 = curva al final de C), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = curva en el índice 0, número de índice de la última curva = curva en el último índice). El rango del factor de una curva a la siguiente es: el número de índice de una curva = la curva en ese índice, el número de índice de la siguiente curva = la siguiente curva de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una curva a medio camino entre la curva del índice 2 y la del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de curvas de entrada |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = recto, 1 = normal, 2 = ajustado, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | lista | Curva interpolada resultante sobre la superficie |

### Tween Two Curves (Twn2Crvs)

Interpola (tween) entre dos curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Curva desde la que interpolar |
| Curve B | `B` | Curve | item | Curva hacia la que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Curve A, 1.0 = Curve B) |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | item | Curva interpolada resultante |

### Tween Two Curves Along Curve (Twn2CrvsCrv)

Interpola (tween) entre dos curvas a lo largo de una curva guía (u opcionalmente de dos curvas guía).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Curva sobre la curva guía desde la que interpolar |
| Curve B | `B` | Curve | item | Curva sobre la curva guía hacia la que interpolar |
| Guide 1 | `G¹` | Curve | item | Curva guía a lo largo de la cual interpolar (mejor si va de Curve A a Curve B) |
| Guide 2 *(opcional)* | `G²` | Curve | item | Segunda curva guía opcional a lo largo de la cual interpolar (mejor si va en la dirección de Guide 1) |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Curve A, 1.0 = Curve B) |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | item | Curva interpolada resultante a lo largo de la curva |

### Tween Two Curves On Surface (Twn2CrvsSrf)

Interpola (tween) entre dos curvas sobre una superficie; si las curvas no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Curva sobre la superficie desde la que interpolar |
| Curve B | `B` | Curve | item | Curva sobre la superficie hacia la que interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar la curva |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Curve A, 1.0 = Curve B) |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Curve | item | Curva interpolada resultante sobre la superficie |

### Weighted Average Curve (WavCrv)

Calcula el promedio ponderado aritmético de un conjunto de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada curva |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da promedios de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da promedios de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Curve | item | Media aritmética (promedio) de todas las curvas de entrada |

## Domain

### Average Domain (AvrDom)

Calcula el promedio aritmético de un conjunto de dominios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `I` | Domain | lista | Conjunto de dominios a promediar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Domain | item | Media aritmética (promedio) de todos los dominios de entrada |

### Average Domain² (AvrDom²)

Calcula el promedio aritmético de un conjunto de dominios².

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain²s | `I²` | Domain² | lista | Conjunto de dominios² a promediar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Domain² | item | Media aritmética (promedio) de todos los dominios² de entrada |

### Mirror Combine Domains (MirComDoms)

Refleja un conjunto de dominios desde su final o su inicio y lo combina con el conjunto original.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `I` | Domain | lista | Conjunto de dominios a reflejar y combinar |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = final del conjunto, True = inicio del conjunto) |
| Join | `J` | Boolean | item | Une el conjunto de dominios reflejado y combinado (quita el dominio duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de dominios: 0 = reflejado, 1 = invertido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirrored | `M` | Domain | lista | Conjunto de dominios reflejado y combinado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de dominios reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |

### Mirror Combine Domains² (MirComDoms²)

Refleja un conjunto de dominios² desde su final o su inicio y lo combina con el conjunto original.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain²s | `I²` | Domain² | lista | Conjunto de dominios² a reflejar y combinar |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = final del conjunto, True = inicio del conjunto) |
| Join | `J` | Boolean | item | Une el conjunto de dominios² reflejado y combinado (quita el dominio² duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de dominios²: 0 = reflejado, 1 = invertido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirrored | `M` | Domain² | lista | Conjunto de dominios² reflejado y combinado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de dominios² reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |

### Mirror Cut Domains (MirCutDoms)

Corta un conjunto de dominios en un índice, refleja el lado conservado del corte respecto de ese índice y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `I` | Domain | lista | Conjunto de dominios a cortar y reflejar |
| Mirror Index | `Mi` | Integer | item | Índice respecto del cual se refleja el lado conservado del corte. Un índice negativo invierte el conjunto de dominios y quita desde arriba. |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = reflejar después del índice, True = reflejar antes del índice) |
| Join | `J` | Boolean | item | Une el conjunto de dominios cortado y reflejado (quita el dominio duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de dominios: 0 = reflejado, 1 = invertido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Domain | lista | Conjunto de dominios cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de dominios cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Intersected | `I` | Boolean | item | True si el índice de reflejo intersectó el conjunto de dominios, False si no lo intersectó |

### Mirror Cut Domains² (MirCutDoms²)

Corta un conjunto de dominios² en un índice, refleja el lado conservado del corte respecto de ese índice y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain²s | `I²` | Domain² | lista | Conjunto de dominios² a cortar y reflejar |
| Mirror Index | `Mi` | Integer | item | Índice respecto del cual se refleja el lado conservado del corte. Un índice negativo invierte el conjunto de dominios² y quita desde arriba. |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = reflejar después del índice, True = reflejar antes del índice) |
| Join | `J` | Boolean | item | Une el conjunto de dominios² cortado y reflejado (quita el dominio² duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de dominios²: 0 = reflejado, 1 = invertido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Domain² | lista | Conjunto de dominios² cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de dominios² cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Intersected | `I` | Boolean | item | True si el índice de reflejo intersectó el conjunto de dominios², False si no lo intersectó |

### Reparameterize Domains (ReparamDoms)

Reparametriza un conjunto de dominios para que sus valores de inicio y final vayan de 0 a 1, o de forma invertida de 1 a 0.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `I` | Domain | lista | Conjunto de dominios a reparametrizar |
| Starts | `S` | Boolean | item | Reparametriza los valores de inicio del conjunto de dominios |
| Ends | `E` | Boolean | item | Reparametriza los valores de final del conjunto de dominios |
| Invert | `I` | Boolean | item | Invierte el rango de valores de inicio y final para que vaya de 1 a 0 en vez de 0 a 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reparameterized | `R` | Domain | lista | Conjunto de dominios reparametrizado resultante |
| Original S | `sO` | Domain | item | El rango original de valores de inicio del conjunto de dominios |
| Original E | `eO` | Domain | item | El rango original de valores de final del conjunto de dominios |

### Reparameterize Domains² (ReparamDoms²)

Reparametriza un conjunto de dominios² para que los valores de inicio y final de sus dominios {u} y {v} vayan de 0 a 1, o de forma invertida de 1 a 0.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain²s | `I²` | Domain² | lista | Conjunto de dominios² a reparametrizar |
| Starts U | `uS` | Boolean | item | Reparametriza los valores de inicio {u} del conjunto de dominios² |
| Ends U | `uE` | Boolean | item | Reparametriza los valores de final {u} del conjunto de dominios² |
| Starts V | `vS` | Boolean | item | Reparametriza los valores de inicio {v} del conjunto de dominios² |
| Ends V | `vE` | Boolean | item | Reparametriza los valores de final {v} del conjunto de dominios² |
| Invert | `I` | Boolean | item | Invierte los rangos de valores de inicio y final para que vayan de 1 a 0 en vez de 0 a 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reparameterized | `R` | Domain² | lista | Conjunto de dominios² reparametrizado resultante |
| Original SU | `usO` | Domain | item | El rango original de valores de inicio {u} del conjunto de dominios² |
| Original EU | `ueO` | Domain | item | El rango original de valores de final {u} del conjunto de dominios² |
| Original SV | `vsO` | Domain | item | El rango original de valores de inicio {v} del conjunto de dominios² |
| Original EV | `veO` | Domain | item | El rango original de valores de final {v} del conjunto de dominios² |

### Slide Within Domain (SlideInDom)

Se desliza entre el inicio y el final de un dominio para obtener un número dentro de él.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain | item | Dominio dentro del cual deslizarse |
| Factor | `F` | Number | item | Factor de deslizamiento (0.0 = inicio del dominio, 1.0 = final del dominio) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Slid | `S` | Number | item | Número resultante dentro del dominio |

### Slide Within Domain² (SlideInDom²)

Se desliza entre el inicio y el final de un dominio² para obtener un número de dominio {u} y {v} dentro de él.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain² | `I²` | Domain² | item | Dominio² dentro del cual deslizarse |
| Factor U | `uF` | Number | item | Factor de deslizamiento {u} (0.0 = inicio {u} del dominio², 1.0 = final {u} del dominio²) |
| Factor V | `vF` | Number | item | Factor de deslizamiento {v} (0.0 = inicio {v} del dominio², 1.0 = final {v} del dominio²) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Slid U | `uS` | Number | item | Número de dominio {u} resultante dentro del dominio² |
| Slid V | `vS` | Number | item | Número de dominio {v} resultante dentro del dominio² |

### Tween Consecutive Domains (TwnConDoms)

Interpola (tween) consecutivamente entre un conjunto de dominios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `I` | Domain | lista | Conjunto de dominios entre los que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = dominio en I, 1.0 = dominio en I +1) |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Domain | lista | Dominios interpolados resultantes |

### Tween Consecutive Domains² (TwnConDoms²)

Interpola (tween) consecutivamente entre un conjunto de dominios².

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain²s | `I²` | Domain² | lista | Conjunto de dominios² entre los que interpolar |
| Factor U | `uF` | Number | lista | Factor de interpolación {u} (0.0 = dominio² {u} en I², 1.0 = dominio² {u} en I² +1) |
| Factor V | `vF` | Number | lista | Factor de interpolación {v} (0.0 = dominio² {v} en I², 1.0 = dominio² {v} en I² +1) |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Domain² | lista | Dominios² interpolados resultantes |

### Tween Through Domains (TwnThruDoms)

Interpola (tween) a través de un conjunto de dominios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `I` | Domain | lista | Conjunto de dominios a través de los cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = dominio al inicio de I, 1.0 = dominio al final de I), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = dominio en el índice 0, número de índice del último dominio = dominio en el último índice). El rango del factor de un dominio al siguiente es: el número de índice de un dominio = el dominio en ese índice, el número de índice del siguiente dominio = el siguiente dominio de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un dominio a medio camino entre el dominio del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa entre los extremos del conjunto de dominios de entrada, sin considerar sus ubicaciones |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Domain | lista | Dominio interpolado resultante |

### Tween Through Domains² (TwnThruDoms²)

Interpola (tween) a través de un conjunto de dominios².

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain²s | `I²` | Domain² | lista | Conjunto de dominios² a través de los cuales interpolar |
| Factor U | `uF` | Number | lista | Factor de interpolación {u} (0.0 = dominio² {u} al inicio, 1.0 = dominio² {u} al final), salvo que Normalized sea False |
| Factor V | `vF` | Number | lista | Factor de interpolación {v} (0.0 = dominio² {v} al inicio, 1.0 = dominio² {v} al final), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = dominio² {u}{v} en el índice 0, número de índice del último dominio² {u}{v} = dominio² {u}{v} en el último índice). El rango del factor de un dominio² {u}{v} al siguiente es: el número de índice de un dominio² {u}{v} = el dominio² {u}{v} en ese índice, el número de índice del siguiente = el siguiente de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un dominio² {u}{v} a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa entre los extremos del conjunto de dominios² de entrada, sin considerar sus ubicaciones |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Domain² | lista | Dominio² interpolado resultante |

### Tween Two Domains (Twn2Doms)

Interpola (tween) entre dos dominios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain A | `A` | Domain | item | Dominio desde el que interpolar |
| Domain B | `B` | Domain | item | Dominio hacia el que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Domain A, 1.0 = Domain B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Domain | item | Dominio interpolado resultante |

### Tween Two Domains² (Twn2Doms²)

Interpola (tween) entre dos dominios².

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain² A | `A` | Domain² | item | Dominio² desde el que interpolar |
| Domain² B | `B` | Domain² | item | Dominio² hacia el que interpolar |
| Factor U | `uF` | Number | item | Factor de interpolación {u} (0.0 = dominio² {u} A, 1.0 = dominio² {u} B) |
| Factor V | `vF` | Number | item | Factor de interpolación {v} (0.0 = dominio² {v} A, 1.0 = dominio² {v} B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Domain² | item | Dominio² interpolado resultante |

### Two Way Domain (2WayDom)

Construye un dominio a partir de un número que pasa a ser los extremos negativo y positivo del dominio desde cero.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extent | `E` | Number | item | Número que será los extremos negativo y positivo del dominio desde cero |
| Direction | `D` | Boolean | item | Si es True, el dominio es creciente (de negativo a positivo). Si es False, el dominio es decreciente (de positivo a negativo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain | item | Dominio bidireccional resultante |

### Two Way Domain² (2WayDom²)

Construye un dominio² a partir de un número {u} y un número {v} que pasan a ser los extremos negativo y positivo de cada dirección del dominio² desde cero.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extent U | `uE` | Number | item | Número que será los extremos {u} negativo y positivo del dominio² desde cero |
| Extent V | `vE` | Number | item | Número que será los extremos {v} negativo y positivo del dominio² desde cero |
| Direction | `D` | Boolean | item | Si es True, el dominio² es creciente (de negativo a positivo). Si es False, es decreciente (de positivo a negativo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain² | `I²` | Domain² | item | Dominio² bidireccional resultante |

### Weighted Average Domain (WavDom)

Calcula el promedio aritmético ponderado de un conjunto de dominios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `I` | Domain | lista | Conjunto de dominios a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada dominio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Domain | item | Media aritmética (promedio) de todos los dominios de entrada |

### Weighted Average Domain² (WavDom²)

Calcula el promedio aritmético ponderado de un conjunto de dominios².

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain²s | `I²` | Domain² | lista | Conjunto de dominios² a promediar |
| Weights U | `uW` | Number | lista | Colección de pesos para los dominios {u} de cada dominio² |
| Weights V | `vW` | Number | lista | Colección de pesos para los dominios {v} de cada dominio² |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Domain² | item | Media aritmética (promedio) de todos los dominios² de entrada |

## List

### Dispatch Indices (DispDexs)

Reparte (dispatch) una lista de elementos en dos listas según un conjunto de índices: los que están en esos índices y los que no. Los elementos en los índices se ordenan según el conjunto de índices de entrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista de elementos a repartir |
| Indices | `i` | Integer | lista | Conjunto de índices de reparto (no debe tener índices repetidos) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| At i | `i=` | Generic Data | lista | Lista resultante de los elementos en los índices de reparto |
| Not i | `i≠` | Generic Data | lista | Lista resultante de los elementos que no están en los índices de reparto |

### Last Index (LastDex)

Obtiene el último índice de una lista (largo de la lista - 1).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista de datos de la que obtener el último índice |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Index | `i` | Integer | item | El último índice de la lista |

### List Indices (ListDexs)

Obtiene la lista de índices de una lista de elementos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista de elementos de la que obtener la lista de índices |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Indices | `i` | Integer | lista | Lista de índices de la lista de elementos |

### Mirror Combine Items (MirComItems)

Refleja un conjunto de elementos de lista desde su final o su inicio y lo combina con el conjunto original.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Items | `L` | Generic Data | lista | Conjunto de elementos de lista a reflejar y combinar |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = final del conjunto, True = inicio del conjunto) |
| Join | `J` | Boolean | item | Une el conjunto de elementos reflejado y combinado (quita el elemento duplicado al medio del conjunto) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirrored | `M` | Generic Data | lista | Conjunto de elementos reflejado y combinado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |

### Mirror Cut Items (MirCutItems)

Corta un conjunto de elementos de lista en un índice, refleja el lado conservado del corte respecto de ese índice y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Items | `L` | Generic Data | lista | Conjunto de elementos de lista a cortar y reflejar |
| Mirror Index | `Mi` | Integer | item | Índice respecto del cual se refleja el lado conservado del corte. Un índice negativo invierte el conjunto y quita desde arriba. |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = reflejar después del índice, True = reflejar antes del índice) |
| Join | `J` | Boolean | item | Une el conjunto de elementos cortado y reflejado (quita el elemento duplicado al medio del conjunto) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Generic Data | lista | Conjunto de elementos cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Intersected | `I` | Boolean | item | True si el índice de reflejo intersectó el conjunto de elementos, False si no lo intersectó |

### Null Placeholder (Null)

Entrega un elemento nulo que se puede usar como marcador de posición en listas.

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Null | `N` | Generic Data | item | Un marcador de posición nulo. Para reemplazar elementos nulos en una lista usa el componente Replace Nulls de Grasshopper. |

### Point Sort Items (PtSortItems)

Ordena un conjunto de elementos de lista de forma sincronizada, según el orden por punto más cercano iterativo de un conjunto de puntos, a partir de un punto inicial.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Items *(opcional)* | `L` | Generic Data | lista | Conjunto de elementos de lista a ordenar junto con el conjunto de puntos (si no se entrega nada, solo se ordena el conjunto de puntos) |
| Start | `S` | Point | item | Punto inicial desde el que ordenar el conjunto de puntos |
| Points | `P` | Point | lista | Conjunto de puntos a ordenar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sorted Items | `sL` | Generic Data | lista | Conjunto de elementos ordenado resultante |
| Sorted Indices | `i` | Integer | lista | Conjunto de índices ordenado resultante |
| Sorted Points | `sP` | Point | lista | Conjunto de puntos ordenado resultante |

### Sift Indices (SiftDexs)

Separa (sift) una lista de elementos en dos listas según un conjunto de índices: los que están en esos índices y los que no. Cada lista resultante tiene el mismo largo y orden que la de entrada, pero se rellena con marcadores nulos donde los elementos fueron a la otra lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista de elementos a separar |
| Indices | `i` | Integer | lista | Conjunto de índices de separación (no debe tener índices repetidos) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| At i | `i=` | Generic Data | lista | Lista resultante de los elementos en los índices de separación, con marcadores nulos en lugar de los elementos de la lista 'Not i'. Opera sobre esta lista y luego vuelve a combinarla con la lista 'Not i' usando el componente Combine Data de Grasshopper, que reemplaza los nulos. |
| Not i | `i≠` | Generic Data | lista | Lista resultante de los elementos que no están en los índices de separación, con marcadores nulos en lugar de los elementos de la lista 'At i'. Opera sobre esta lista y luego vuelve a combinarla con la lista 'At i' usando el componente Combine Data de Grasshopper, que reemplaza los nulos. |

## Mesh

### Angle Split Mesh (AngSplitMsh)

Divide una malla en mallas separadas midiendo una tolerancia angular entre las normales de caras adyacentes; si la tolerancia no divide la malla, sale sin cambios. Métodos base de Mateusz Zwierzycki

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a dividir |
| Angle | `A` | Number | item | Tolerancia angular, en grados, a medir entre las normales de caras adyacentes. Las caras adyacentes cuyas normales formen un ángulo menor que este se dividen en su arista compartida |
| Opposite | `O` | Boolean | item | Mantiene juntas las caras adyacentes que tienen normales opuestas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Split | `S` | Mesh | item | Mallas divididas resultantes |
| Result Boolean | `R` | Boolean | item | True si la malla se dividió, False si no |

### Average Mesh (AvrMsh)

Calcula el promedio aritmético de un conjunto de mallas; las mallas deben tener la misma topología. También puede promediar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas a promediar |
| Colored | `C` | Boolean | item | Promedia los colores de los vértices de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Mesh | item | Media aritmética (promedio) de todas las mallas de entrada |

### Blend Consecutive Meshes (BlndConMshs)

Mezcla (blend) consecutivamente entre un conjunto de mallas a través de sus vértices, con un conjunto de factores donde cada uno controla la cantidad de mezcla entre los vértices que comparten el mismo índice de una malla a otra; las mallas deben tener la misma topología. También puede mezclar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas entre las que mezclar |
| Factors | `F` | Number | lista | Factores de mezcla, uno por cada conjunto de vértices que comparten el mismo índice de una malla a otra (0.0 = vértices de la malla en M, 1.0 = vértices de la malla en M +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la mezcla se pondera según los vértices de las mallas de entrada y la curvatura de los caminos de mezcla de los vértices |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de mezcla continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura de los caminos de mezcla de los vértices; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpolan los caminos de mezcla de los vértices: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Colored Type | `C` | Integer | item | Determina cómo se mezclan los colores de los vértices: 0 = no se mezclan, 1 = rápido, 2 = preciso |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Blend | `B` | Mesh | lista | Mallas mezcladas resultantes |

### Blend Through Meshes (BlndThruMshs)

Mezcla (blend) a través de un conjunto de mallas por sus vértices, con un conjunto de factores donde cada uno controla la cantidad de mezcla a través de los vértices que comparten el mismo índice en todas las mallas; las mallas deben tener la misma topología. También puede mezclar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas a través de las cuales mezclar |
| Factors | `F` | Number | lista | Factores de mezcla, uno por cada conjunto de vértices que comparten el mismo índice en todas las mallas (0.0 = vértices de la malla al inicio de M, 1.0 = vértices de la malla al final de M), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = vértices de la malla en el índice 0, número de índice de la última malla = vértices de la malla en el último índice). El rango del factor de los vértices de una malla a los de la siguiente es: el número de índice de una malla = sus vértices, el número de índice de la siguiente malla = los vértices de la siguiente malla de la lista, y los factores entre esos índices dan las mezclas correspondientes. Por ejemplo, un factor de 2.5 da vértices a medio camino entre los de la malla del índice 2 y los de la del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la mezcla se evalúa a lo largo de los caminos de mezcla de los vértices, sin considerar las ubicaciones de los vértices de las mallas de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la mezcla se pondera según los vértices de las mallas de entrada y la curvatura de los caminos de mezcla de los vértices |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de mezcla continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura de los caminos de mezcla de los vértices; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpolan los caminos de mezcla de los vértices: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Colored Type | `C` | Integer | item | Determina cómo se mezclan los colores de los vértices: 0 = no se mezclan, 1 = rápido, 2 = preciso |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Blend | `B` | Mesh | lista | Malla mezclada resultante |

### Blend Two Meshes (Blnd2Mshs)

Mezcla (blend) entre dos mallas por sus vértices, con un conjunto de factores donde cada uno controla la cantidad de mezcla entre cada par de vértices que comparten el mismo índice de una malla a la otra; las mallas deben tener la misma topología. También puede mezclar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh A | `A` | Mesh | item | Malla desde la que mezclar |
| Mesh B | `B` | Mesh | item | Malla hacia la que mezclar |
| Factors | `F` | Number | lista | Factores de mezcla, uno por cada par de vértices que comparten el mismo índice de una malla a la otra (0.0 = vértices de Mesh A, 1.0 = vértices de Mesh B) |
| Colored | `C` | Boolean | item | Mezcla los colores de los vértices de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Blend | `B` | Mesh | item | Malla mezclada resultante |

### Close Mesh (ClsMsh)

Cierra una malla abierta rellenando sus aberturas con caras nuevas; si la malla ya es cerrada, sale sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a cerrar |
| Quadrangulate | `Q` | Boolean | item | Crea caras cuadrangulares cuando sea posible |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closed | `C` | Mesh | item | Malla cerrada resultante |
| Amount | `A` | Integer | item | Cantidad de aberturas de la malla de entrada |
| Openings | `O` | Curve | lista | Polilíneas de contorno de las aberturas de la malla de entrada |
| Result Boolean | `R` | Boolean | lista | True para cada abertura de la malla que se cerró, False para cada abertura que no se cerró o si toda la malla ya era cerrada |

### Displace Mesh (DisMsh)

Desplaza una malla por sus vértices con un conjunto de distancias, donde cada distancia controla cuánto se desplaza cada vértice en su dirección normal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a desplazar |
| Distances | `D` | Number | lista | Distancias de desplazamiento, una por vértice |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Displaced | `D` | Mesh | item | Malla desplazada resultante |
| Vectors | `V` | Vector | lista | Vectores normales de desplazamiento resultantes |

### Is Mesh Closed (MshClsd)

Prueba si una malla es cerrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a probar si es cerrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closed | `C` | Boolean | item | True si la malla es cerrada |

### Is Mesh Disjoint (MshDisjn)

Prueba si una malla tiene piezas desconectadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a probar si tiene piezas desconectadas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Disjoint | `D` | Boolean | item | True si la malla tiene piezas desconectadas. Para extraer cada pieza como malla separada, usa la malla de entrada con el componente Disjoint Mesh de Grasshopper. |
| Amount | `A` | Integer | item | Cantidad de piezas desconectadas de la malla |

### Mesh Statistics (MshStats)

Obtiene estadísticas de una malla: cantidad de vértices, de caras, de caras cuadrangulares, de caras triangulares, de colores y de piezas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de la que obtener estadísticas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertex Count | `V` | Integer | item | Cantidad de vértices de la malla |
| Face Count | `F` | Integer | item | Cantidad de caras de la malla |
| Quad Face Count | `Q` | Integer | item | Cantidad de caras cuadrangulares de la malla |
| Triangle Face Count | `T` | Integer | item | Cantidad de caras triangulares de la malla |
| Color Count | `C` | Integer | item | Cantidad de colores de la malla |
| Piece Count | `P` | Integer | item | Cantidad de piezas desconectadas de la malla |

### Mirror Cut Mesh (MirCutMsh)

Corta una malla con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a cortar y reflejar |
| Mirror Plane | `MP` | Plane | item | Plano respecto del cual se refleja el lado conservado del corte de la malla |
| Reach | `R` | Number | item | Las partes de la malla a menos de esta distancia del plano de reflejo también se cortan |
| Offset | `O` | Number | item | Distancia de desfase de las partes conservadas de la malla respecto del plano de reflejo (o desde el alcance, si el alcance no es cero) |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo |
| Join | `J` | Boolean | item | Une la malla cortada y reflejada |
| Keep | `K` | Boolean | item | Conserva la malla y la refleja normalmente si el corte la hace desaparecer |
| Connection Type | `T` | Integer | item | Determina cómo se conectan las mallas cortadas y reflejadas: 0 = dividir caras, con conexión; 1 = quitar caras, con conexión; 2 = encoger caras, con conexión; 3 = dividir caras, sin conexión; 4 = quitar caras, sin conexión; 5 = encoger caras, sin conexión |
| Bulge | `B` | Number | item | Factor de abombamiento de las conexiones de la malla cortada y reflejada (-B = abombamiento negativo, 0.0 = sin abombamiento, +B = abombamiento positivo) |
| Divisions | `D` | Integer | item | Cantidad de caras por lado de la conexión de la malla |
| Weld Vertices | `W` | Number | item | Suelda los vértices de la malla que están a cierta proximidad entre sí (0.0 = no soldar; un número mayor que 0 = soldar los vértices a menos de esa distancia) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Mesh | lista | Mallas cortadas y reflejadas resultantes |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de mallas cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Reach Plane | `RP` | Plane | item | El plano a la distancia de alcance |
| Offset Plane | `OP` | Plane | item | El plano a la distancia de desfase |
| Intersected | `I` | Boolean | item | True si el corte con reflejo intersectó la malla, False si no la intersectó |

### Offset Mesh (OffMsh)

Aplica offset a una malla, con la opción de hacerlo hacia ambos lados a distancias distintas y crear un sólido.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que aplicar offset |
| Distance | `D` | Number | item | Distancia de offset |
| Both Sides | `B` | Number | item | Distancia de offset opcional para ambos lados; usa el número inverso de la distancia para el offset en la dirección opuesta (si la distancia es positiva usa un número negativo, y viceversa) |
| Create Solid | `C` | Boolean | item | Si es True, crea un offset sólido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset | `O` | Mesh | lista | Malla con offset resultante |

### Parameter Extrude Mesh (ParamExtrMsh)

Crea una malla extruida a partir de una curva de perfil a lo largo de un vector, una curva o hacia un punto, dividiendo el dominio con parámetros {u} y {v}, por longitudes entre puntos de control o por precisión angular, con la opción de tapar las extrusiones de perfiles cerrados. Métodos base de Mateusz Zwierzycki

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Profile | `P` | Curve | item | Curva de perfil a extruir como malla |
| Direction | `D` | Generic Data | item | Vector, curva o punto de dirección de extrusión. Entrega un vector para extruir a lo largo de un vector, una curva para extruir a lo largo de una curva o un punto para extruir hacia un punto |
| Parameters U *(opcional)* | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la curva de perfil para las caras de la malla ({u} 0.0 = inicio del perfil, 1.0 = final del perfil), salvo que Length sea True o Angle no sea 0.0. Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V *(opcional)* | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la dirección de extrusión para las caras de la malla ({v} 0.0 = inicio de la extrusión, 1.0 = final de la extrusión), salvo que length {v} sea True o angle {v} no sea 0.0 al usar una curva como dirección de extrusión. Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {u} se pondera según la curvatura de la curva de perfil |
| Lengths | `L` | Boolean | item | Si es True, las divisiones de caras de la curva de perfil se definen por las longitudes entre sus puntos de control en vez de los parámetros {u} (útil para que las divisiones se ajusten a cada segmento de un perfil polilínea) |
| Angle | `A` | Number | item | Si Angle no es 0.0, las divisiones de caras de la curva de perfil se definen por precisión angular en grados en vez de los parámetros {u} (útil para que las divisiones se ajusten a la curvatura del perfil) |
| Cap | `C` | Boolean | item | Tapa los extremos abiertos de una extrusión de malla de perfil cerrado |
| Triangulate | `T` | Boolean | item | Triangula las caras de la malla |
| Weighted V | `vW` | Boolean | item | Si es True y se usa una curva como dirección de extrusión, la distribución de los parámetros {v} se pondera según la curvatura de esa curva |
| Lengths V | `vL` | Boolean | item | Si es True y se usa una curva como dirección de extrusión, las divisiones de caras de esa curva se definen por las longitudes entre sus puntos de control en vez de los parámetros {v} (útil para que las divisiones se ajusten a cada segmento de una curva de dirección polilínea) |
| Angle V | `vA` | Number | item | Si Angle no es 0.0 y se usa una curva como dirección de extrusión, las divisiones de caras de esa curva se definen por precisión angular en grados en vez de los parámetros {v} (útil para que las divisiones se ajusten a la curvatura de la curva de dirección) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extruded | `E` | Mesh | item | Malla extruida resultante |

### Parameter Loft Mesh (ParamLoftMsh)

Crea una malla con loft a través de un conjunto de curvas de sección, dividiendo el dominio con parámetros {u} y {v}, por longitudes entre puntos de control o por precisión angular, con puntos inicial y final opcionales hacia los que hacer el loft. Métodos base de Mateusz Zwierzycki

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sections | `S` | Curve | lista | Conjunto de curvas de sección a través de las cuales hacer el loft como malla |
| Parameters U *(opcional)* | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de las curvas de sección para las caras de la malla ({u} 0.0 = inicio de la sección, 1.0 = final de la sección), salvo que Length sea True o Angle no sea 0.0. Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división del dominio {v} entre cada curva de sección para las caras de la malla ({v} 0.0 = sección en S, 1.0 = sección en S +1). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {u} se pondera según la curvatura de las curvas de sección |
| Lengths | `L` | Boolean | item | Si es True, las divisiones de caras de las curvas de sección se definen por las longitudes entre sus puntos de control en vez de los parámetros {u} (útil para que las divisiones se ajusten a cada segmento de secciones polilínea) |
| Angle | `A` | Number | item | Si Angle no es 0.0, las divisiones de caras de las curvas de sección se definen por su precisión angular en grados en vez de los parámetros {u} (útil para que las divisiones se ajusten a la curvatura de las secciones) |
| Closed | `C` | Boolean | item | Loft cerrado: si es True, la última curva de sección hace loft de vuelta a la primera (o al punto inicial o final opcional) |
| Triangulate | `T` | Boolean | item | Triangula las caras de la malla |
| Point Start *(opcional)* | `sP` | Point | item | Punto inicial opcional del loft de malla (también sirve para tapar el inicio de un loft cuya primera sección es cerrada) |
| Point End *(opcional)* | `eP` | Point | item | Punto final opcional del loft de malla (también sirve para tapar el final de un loft cuya última sección es cerrada) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lofted | `L` | Mesh | item | Malla con loft resultante |

### Parameter Pipe Mesh (ParamPipeMsh)

Crea una malla tubular a lo largo de una curva, dividiendo el dominio con parámetros {u} y {v}, por longitudes entre puntos de control o por precisión angular, con distintos tipos de extremo. Métodos base de Mateusz Zwierzycki

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual crear la tubería como malla |
| Radius | `R` | Number | item | Radio de la malla tubular |
| Parameters U *(opcional)* | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la curva para las caras de la malla ({u} 0.0 = inicio de la curva, 1.0 = final de la curva), salvo que Length sea True o Angle no sea 0.0. Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división alrededor del dominio {v} de la curva para las caras de la malla ({v} 0.0 = mínimo de la revolución, 1.0 = máximo de la revolución). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {u} se pondera según la curvatura de la curva |
| Lengths | `L` | Boolean | item | Si es True, las divisiones de caras de la curva se definen por las longitudes entre sus puntos de control en vez de los parámetros {u} (útil para que las divisiones se ajusten a cada segmento de una curva polilínea) |
| Angle | `A` | Number | item | Si Angle no es 0.0, las divisiones de caras de la curva se definen por precisión angular en grados en vez de los parámetros {u} (útil para que las divisiones se ajusten a la curvatura de la curva) |
| Rotation | `R` | Number | item | Rotación del radio de la malla tubular alrededor de la curva, en grados |
| End Type | `E` | Integer | item | Determina cómo terminar la malla tubular: 0 = ninguno, 1 = plano, 2 = redondo |
| Triangulate | `T` | Boolean | item | Triangula las caras de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Piped | `P` | Mesh | item | Malla tubular resultante |

### Parameter Plane Mesh (ParamPlnMsh)

Genera una malla plana en un rectángulo dividiendo su dominio con parámetros {x} e {y}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo a dividir como malla |
| Parameters X | `x` | Number | lista | Parámetros de división a lo largo del dominio {x} del rectángulo ({x} 0.0 = inicio del rectángulo, 1.0 = final). Para mejores resultados, los parámetros {x} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters Y | `y` | Number | lista | Parámetros de división a lo largo del dominio {y} del rectángulo ({y} 0.0 = inicio del rectángulo, 1.0 = final). Para mejores resultados, los parámetros {y} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Triangulate | `T` | Boolean | item | Triangula las caras de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla plana resultante del rectángulo |

### Parameter Surface Mesh (ParamSrfMsh)

Genera una malla sobre una superficie dividiendo su dominio con parámetros {u} y {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir como malla |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Triangulate | `T` | Boolean | item | Triangula las caras de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla resultante de la superficie |

### Plane Trim Mesh (PlnTrimMsh)

Recorta (quita) las partes de una malla que están a un lado de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a recortar |
| Plane | `Pl` | Plane | item | Plano con el que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |
| Trim Type | `T` | Integer | item | Determina cómo se recorta la malla: 0 = dividir caras, 1 = quitar caras, 2 = encoger caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Mesh | lista | Malla recortada resultante |
| Intersected | `I` | Boolean | item | True si el plano recortó la malla, False si no |

### Polyline To Mesh (PLine2Msh)

Crea una malla a partir de un contorno de polilínea cerrado o abierto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `Pl` | Curve | item | Contorno de polilínea que representa las aristas desnudas de la malla |
| Quadrangulate | `Q` | Boolean | item | Crea caras cuadrangulares cuando sea posible |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla resultante del contorno de polilínea |

### Rebuild Mesh (RebMsh)

Reconstruye una malla con opciones para recalcular normales, quitar caras y vértices no usados, combinar vértices duplicados, unificar normales, invertir normales y soldar vértices cercanos entre sí.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a reconstruir |
| Rebuild Normals | `R` | Boolean | item | Recalcula las normales de los vértices y caras de la malla |
| Cull Unused | `C` | Boolean | item | Quita de la malla los vértices y caras no usados |
| Unify Normals | `U` | Boolean | item | Corrige inconsistencias en las normales de los vértices y caras de la malla |
| Flip Normals | `F` | Boolean | item | Invierte las normales de los vértices y caras de la malla |
| Identical Combine | `I` | Boolean | item | Fusiona los vértices duplicados de la malla |
| Weld Vertices | `W` | Number | item | Suelda los vértices de la malla que están a cierta proximidad entre sí (0.0 = no soldar; un número mayor que 0 = soldar los vértices a menos de esa distancia) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rebuilt | `R` | Mesh | item | Malla reconstruida resultante |

### Recursive Morph Mesh (ReMorphMsh)

Deforma (morph) de forma recursiva geometrías de malla sobre las caras de una malla, empezando por una malla base; la malla resultante de cada paso recursivo pasa a ser la nueva malla base sobre cuyas caras se deforma la geometría del paso siguiente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base Mesh | `B` | Mesh | item | Malla base sobre cuyas caras se deforma la primera geometría de malla (mejores resultados con una malla de pocos polígonos y suavizando la malla resultante) |
| Steps | `N` | Integer | item | Cantidad de pasos recursivos de deformación. ADVERTENCIA: la recursión crea mallas nuevas en cada cara, potencialmente de forma exponencial. Más de 3 pasos puede crear muchísimas caras. Guarda tu trabajo por si el computador se congela con valores altos. |
| Meshes | `M` | Mesh | lista | Una lista de geometrías de malla a deformar, una por cada paso recursivo (mejores resultados con mallas de pocos polígonos y suavizando la malla resultante) |
| References | `R` | Box | lista | Una lista de cajas de referencia desde las que deformar, una por cada paso recursivo (normalmente la caja contenedora de cada geometría de malla a deformar) |
| Thicknesses | `T` | Number | lista | Una lista de espesores de offset desde las caras de la malla para la altura de la deformación, uno por cada paso recursivo |
| Weld Vertices | `W` | Number | item | Suelda los vértices de la malla que están a cierta proximidad entre sí (0.0 = no soldar; un número mayor que 0 = soldar los vértices a menos de esa distancia) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Morphed | `M` | Mesh | item | Malla resultante deformada de forma recursiva |

### Reduce Mesh (ReduMsh)

Reduce la cantidad de caras de una malla hasta un objetivo (mira la línea de comandos de Rhino para ver el % de avance).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a reducir |
| Face Count | `F` | Integer | item | Cantidad objetivo de caras. Es solo una meta: la cantidad de caras de la malla reducida puede variar |
| Accuracy | `A` | Integer | item | Precisión de la reducción (1 = mínima, 10 = máxima) |
| Face Type | `T` | Integer | item | 0 = por defecto (los tipos de cara salen directamente de la reducción); 1 = cuadrangular si es posible (se aplica después de reducir, puede cambiar la cantidad de caras); 2 = triangular todo (se aplica después de reducir, puede cambiar la cantidad de caras) |
| Distort | `D` | Boolean | item | Si es True, la malla se reduce hasta alcanzar la cantidad de caras deseada. Si es False, se reduce solo hasta el punto en que habría que cambiar la forma de la malla |
| Normalize | `N` | Boolean | item | Distribuye de forma más pareja el tamaño de las caras de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reduced | `R` | Mesh | item | Malla reducida resultante |
| Count Difference | `C` | Integer | item | Diferencia en cantidad de caras entre la malla original y la reducida |

### Tween Consecutive Meshes (TwnConMshs)

Interpola (tween) consecutivamente entre un conjunto de mallas; las mallas deben tener la misma topología. También puede interpolar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas entre las que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = malla en M, 1.0 = malla en M +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de mallas de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Colored Type | `C` | Integer | item | Determina cómo se interpolan los colores de los vértices: 0 = no se interpolan, 1 = rápido, 2 = preciso |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Mesh | lista | Mallas interpoladas resultantes |

### Tween Through Meshes (TwnThruMshs)

Interpola (tween) a través de un conjunto de mallas; las mallas deben tener la misma topología. También puede interpolar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas a través de las cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = malla al inicio de M, 1.0 = malla al final de M), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = malla en el índice 0, número de índice de la última malla = malla en el último índice). El rango del factor de una malla a la siguiente es: el número de índice de una malla = la malla en ese índice, el número de índice de la siguiente malla = la siguiente malla de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una malla a medio camino entre la del índice 2 y la del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de mallas de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de mallas de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Colored Type | `C` | Integer | item | Determina cómo se interpolan los colores de los vértices: 0 = no se interpolan, 1 = rápido, 2 = preciso |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Mesh | lista | Malla interpolada resultante |

### Tween Two Meshes (Twn2Mshs)

Interpola (tween) entre dos mallas; las mallas deben tener la misma topología. También puede interpolar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh A | `A` | Mesh | item | Malla desde la que interpolar |
| Mesh B | `B` | Mesh | item | Malla hacia la que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Mesh A, 1.0 = Mesh B) |
| Colored | `C` | Boolean | item | Interpola los colores de los vértices de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Mesh | item | Malla interpolada resultante |

### Voxel Mesh (VoxMsh)

Crea una voxelización orientada a un plano de un conjunto de puntos, como malla sin caras interiores, definida por un tamaño de vóxel en {x}, {y} y {z}. Métodos base de Mateusz Zwierzycki

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a voxelizar como malla |
| Plane | `Pl` | Plane | item | Plano de orientación de la voxelización |
| Size X | `X` | Number | item | Tamaño de los vóxeles en la dirección {x} del plano; usa un tamaño negativo para omitir las caras de la malla en esa dirección |
| Size Y | `Y` | Number | item | Tamaño de los vóxeles en la dirección {y} del plano; usa un tamaño negativo para omitir las caras de la malla en esa dirección |
| Size Z | `Z` | Number | item | Tamaño de los vóxeles en la dirección {z} del plano; usa un tamaño negativo para omitir las caras de la malla en esa dirección |
| Triangulate | `T` | Boolean | item | Triangula las caras de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Voxelized | `V` | Mesh | item | Malla de vóxeles resultante |

### Weighted Average Mesh (WavMsh)

Calcula el promedio aritmético ponderado de un conjunto de mallas; las mallas deben tener la misma topología. También puede promediar los colores de los vértices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada malla |
| Colored | `C` | Boolean | item | Promedia los colores de los vértices de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Mesh | item | Media aritmética (promedio) de todas las mallas de entrada |

## Number

### Curve Graph Mapper (CrvGraphMap)

Reasigna valores con un gráfico personalizado usando curvas de entrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Una o varias curvas de gráfico con las que mapear los valores |
| Rectangle | `R` | Rectangle | item | Rectángulo que define el borde del gráfico; las curvas del gráfico deben estar al menos en parte dentro de este borde |
| Values | `V` | Number | lista | Valores a mapear con el gráfico. Se ubican sobre el eje X, se intersectan con las curvas del gráfico y luego se proyectan al eje Y |
| X Axis *(opcional)* | `X` | Domain | item | Dominio del eje X del gráfico, donde se ubican los valores (si se omite, se usan los límites de la lista de valores de entrada) |
| Y Axis *(opcional)* | `Y` | Domain | item | Dominio del eje Y del gráfico, donde se proyectan los valores (si se omite, se usan los límites de la lista de valores de entrada) |
| Flip | `F` | Boolean | item | Invierte el eje X del gráfico desde abajo hacia arriba |
| Snap | `S` | Boolean | item | Redimensiona el gráfico ajustándolo a la extensión de las curvas del gráfico, en el plano del rectángulo de borde |
| Text Size | `T` | Number | item | Tamaño de las etiquetas del gráfico |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped | `M` | Number | lista | Valores mapeados resultantes, proyectados en el eje Y |
| Graph Curves | `gC` | Curve | lista | Las curvas del gráfico dentro del borde del gráfico |
| Graph Points | `gP` | Point | lista | Los puntos de las curvas del gráfico donde intersectaron los valores de entrada del eje X |
| Value Lines | `vL` | Line | lista | Las líneas desde los valores de entrada del eje X hasta las curvas del gráfico |
| Value Points | `vP` | Point | lista | Los puntos sobre el eje X que representan los valores de entrada |
| Mapped Lines | `mL` | Line | lista | Las líneas desde las curvas del gráfico hasta los valores mapeados en el eje Y |
| Mapped Points | `mP` | Point | lista | Los puntos sobre el eje Y que representan los valores mapeados |
| Boundary | `B` | Surface | item | El fondo del borde del gráfico como superficie |
| Labels | `L` | Curve | lista | Las etiquetas del gráfico como contornos de curva |
| Out Of Bounds | `O` | Boolean | lista | True para los valores de entrada fuera de los límites del dominio del eje X, False para los que están dentro |
| Intersected | `I` | Boolean | lista | True para los valores de entrada del eje X que intersectan una curva del gráfico, False para los que no |

### Deconstruct Number (DeNum)

Descompone un número en su parte entera y su resto decimal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `N` | Number | item | Número a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Whole | `W` | Integer | item | Parte entera del número |
| Remainder | `R` | Number | item | Parte decimal (resto) del número |

### Default Angle Tolerance (DefAt)

Entrega el valor por defecto de la tolerancia angular de RhinoMath (1 grado \| 0.017453 rad).

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Degrees | `D` | Number | item | Tolerancia angular por defecto de RhinoMath, en grados |
| Radians | `R` | Number | item | Tolerancia angular por defecto de RhinoMath, en radianes |

### Document Angle Tolerance (DocAt)

Entrega la tolerancia angular del documento de Rhino (Propiedades del documento > Unidades > Modelo > Tolerancia angular).

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Degrees | `D` | Number | item | Tolerancia angular del documento de Rhino, en grados |
| Radians | `R` | Number | item | Tolerancia angular del documento de Rhino, en radianes |

### Document Distance Tolerance (DocDt)

Entrega la tolerancia absoluta de distancia del documento de Rhino (Propiedades del documento > Unidades > Modelo > Tolerancia absoluta).

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tolerance | `t` | Number | item | Tolerancia absoluta de distancia del documento de Rhino |

### Equality Within Tolerance (EqualsT)

Prueba la igualdad de dos números dentro de una tolerancia (\|A - B\| <= t).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First Number | `A` | Number | item | Número a comparar |
| Second Number | `B` | Number | item | Número con el que comparar |
| Tolerance | `t` | Number | item | Diferencia máxima aceptable entre A y B para considerarlos iguales (si se omite, se usa la tolerancia del documento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Equality | `=` | Boolean | item | True si A está dentro de la tolerancia de B |
| Inequality | `≠` | Boolean | item | True si A no está dentro de la tolerancia de B |

### Highest & Lowest Numbers (HiLoNums)

Obtiene los valores mayor y menor de un conjunto de números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números del que obtener el mayor y el menor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Highest | `H` | Number | item | Número mayor del conjunto |
| Lowest | `L` | Number | item | Número menor del conjunto |

### Invert Boolean (InvBool)

Invierte un booleano: True pasa a False y False pasa a True.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boolean | `B` | Boolean | item | Booleano a invertir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inverted | `I` | Boolean | item | Booleano invertido resultante |
| Number | `N` | Integer | item | Representación numérica del booleano invertido |

### Last Index Range (LastRange)

Crea un rango de números entre 0 y el último índice de una lista (largo de la lista - 1).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista de datos de la que obtener el último índice |
| Steps | `N` | Integer | item | Cantidad de pasos del rango |
| Include | `I` | Boolean | item | Incluye 0 y el último índice en el rango |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Range | `R` | Number | lista | Rango de números entre 0 y el último índice |

### Linearize Numbers (LinearNums)

Linealiza un conjunto de números: un conjunto que se repite como onda se reasigna a incrementos crecientes entre los límites de un dominio, manteniendo las proporciones de los intervalos entre números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a linealizar |
| Domain | `I` | Domain | item | Los límites del dominio entre los que linealizar el conjunto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linearized | `L` | Number | lista | Conjunto de números linealizado resultante |
| Actual | `A` | Domain | item | El rango real del dominio del conjunto linealizado antes de ajustarlo a los límites del dominio |
| Original | `O` | Domain | item | El rango original del dominio del conjunto de números |

### List Length Range (LengRange)

Crea un rango de números entre 0 y el largo de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista de datos de la que obtener el largo |
| Steps | `N` | Integer | item | Cantidad de pasos del rango |
| Include | `I` | Boolean | item | Incluye 0 y el largo de la lista en el rango |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Range | `R` | Number | lista | Rango de números entre 0 y el largo de la lista |

### Mass Division (MDiv)

Realiza la división de todos los números de un conjunto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a dividir en masa |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Divided | `D` | Number | item | Resultado de la división masiva |
| Partial | `P` | Number | lista | Resultados parciales (pasos) de la división masiva |

### Mass Subtraction (MSub)

Realiza la resta de todos los números de un conjunto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a restar en masa |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Subtracted | `S` | Number | item | Resultado de la resta masiva |
| Partial | `P` | Number | lista | Resultados parciales (pasos) de la resta masiva |

### Mirror Combine Numbers (MirComNums)

Refleja un conjunto de números desde su final o su inicio y lo combina con el conjunto original.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a reflejar y combinar |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = final del conjunto, True = inicio del conjunto) |
| Join | `J` | Boolean | item | Une el conjunto de números reflejado y combinado (quita el número duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de números: 0 = reflejado, 1 = invertido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirrored | `M` | Number | lista | Conjunto de números reflejado y combinado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |

### Mirror Cut Numbers (MirCutNums)

Corta un conjunto de números en un índice, refleja el lado conservado del corte respecto de ese índice y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a cortar y reflejar |
| Mirror Index | `Mi` | Integer | item | Índice respecto del cual se refleja el lado conservado del corte. Un índice negativo invierte el conjunto de números y quita desde arriba. |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = reflejar después del índice, True = reflejar antes del índice) |
| Join | `J` | Boolean | item | Une el conjunto de números cortado y reflejado (quita el número duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de números: 0 = reflejado, 1 = invertido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Number | lista | Conjunto de números cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Intersected | `I` | Boolean | item | True si el índice de reflejo intersectó el conjunto de números, False si no lo intersectó |

### Odd & Even Numbers (OddEveNums)

Separa un conjunto de números en impares y pares, con la opción de usar marcadores nulos en los conjuntos separados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a separar en impares y pares |
| Placeholders | `P` | Boolean | item | Usa marcadores nulos en cada conjunto resultante en lugar de los valores que van al otro conjunto, para que los conjuntos resultantes tengan el mismo orden y largo que el conjunto de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Odd | `O` | Number | lista | Conjunto de números impares resultante |
| Even | `E` | Number | lista | Conjunto de números pares resultante |

### Partition Number (PartNum)

Reparte un número de la forma más pareja posible en una cantidad dada de partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `N` | Number | item | Número a repartir |
| Division | `D` | Integer | item | Cantidad de partes |
| Integer | `I` | Boolean | item | División entera |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Partitions | `P` | Number | lista | Partes del número |

### Percentage (Pcent)

Calcula el porcentaje de un número.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `N` | Number | item | Número del que calcular el porcentaje |
| Percent | `P` | Number | item | Porcentaje a calcular |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Percentage | `%` | Number | item | Porcentaje resultante |

### Reparameterize Numbers (ReparamNums)

Reparametriza un conjunto de números para que su dominio vaya de 0 a 1, o de forma invertida de 1 a 0.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a reparametrizar |
| Invert | `I` | Boolean | item | Invierte el rango del dominio para que vaya de 1 a 0 en vez de 0 a 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reparameterized | `R` | Number | lista | Conjunto de números reparametrizado resultante |
| Original | `O` | Domain | item | El rango original del dominio del conjunto de números |

### Reparameterized Range (RepaRange)

Crea un rango de números entre 0 y 1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Steps | `N` | Integer | item | Cantidad de pasos del rango |
| Include | `I` | Boolean | item | Incluye 0 y 1 en el rango |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Range | `R` | Number | lista | Rango de números entre 0 y 1 |

### Round To Decimal Place (RoundD)

Redondea un número a una posición decimal o lo trunca en una posición decimal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number X | `x` | Number | item | Número a redondear |
| Decimal Place | `d` | Integer | item | Posición decimal a la que redondear |
| Round Type | `T` | Integer | item | Determina cómo se redondea el número: 0 = al más cercano, 1 = hacia abajo / truncar, 2 = hacia arriba |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rounded | `R` | Number | item | Número resultante de redondear x a la posición decimal. Los decimales de este número solo se muestran hasta la cantidad definida en las opciones de formato de Grasshopper (File > Preferences > Display > Formatting); esos ajustes solo cambian cómo se muestra el número, no su valor real. Además, Grasshopper no muestra los ceros innecesarios al final. |
| Difference | `D` | Number | item | La diferencia entre el número redondeado resultante y el número de entrada x |

### Round To Factor (RoundF)

Redondea un número a un múltiplo de un factor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number X | `x` | Number | item | Número a redondear |
| Factor | `f` | Number | item | Factor múltiplo al que redondear |
| Round Type | `T` | Integer | item | Determina cómo se redondea el número: 0 = al más cercano, 1 = hacia abajo, 2 = hacia arriba |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rounded | `R` | Number | item | Número resultante de redondear x al múltiplo del factor. Los decimales de este número solo se muestran hasta la cantidad definida en las opciones de formato de Grasshopper (File > Preferences > Display > Formatting); esos ajustes solo cambian cómo se muestra el número, no su valor real. Además, Grasshopper no muestra los ceros innecesarios al final. |
| Difference | `D` | Number | item | La diferencia entre el número redondeado resultante y el número de entrada x |
| Multiplier R | `rM` | Number | item | Cuántas veces cabe el factor en el número redondeado resultante |
| Multiplier X | `xM` | Number | item | Cuántas veces cabe el factor en el número de entrada x |

### Round To Nearest (RoundN)

Redondea los números de x a los números más cercanos de y, con la opción de reasignar el conjunto x a los límites del dominio del conjunto y.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers X | `x` | Number | lista | Conjunto de números a redondear |
| Numbers Y | `y` | Number | lista | Conjunto de números a los que redondear al más cercano (mejor sin valores y repetidos) |
| Remap x | `R` | Boolean | item | Reasigna el conjunto x a los límites del dominio del conjunto y |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Nearest | `N` | Number | lista | Números de y más cercanos a cada número de x (si Remap (R) es True, los números de y más cercanos a cada número x reasignado) |
| Index | `i` | Integer | lista | Índice del número de y más cercano a cada número de x (si Remap (R) es True, al número x reasignado) |
| Difference | `D` | Number | lista | La diferencia entre el conjunto de números más cercanos resultante y el conjunto de entrada x |
| Remapped x | `xR` | Number | lista | El conjunto x reasignado a los límites del dominio del conjunto y si Remap (R) es True; el mismo conjunto x si Remap (R) es False |

### Tween Consecutive Numbers (TwnConNums)

Interpola (tween) consecutivamente entre un conjunto de números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números entre los que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = número en N, 1.0 = número en N +1) |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Number | lista | Números interpolados resultantes |

### Tween Through Numbers (TwnThruNums)

Interpola (tween) a través de un conjunto de números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Conjunto de números a través de los cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = número al inicio de N, 1.0 = número al final de N), salvo que Normalized sea False. |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = número en el índice 0, número de índice del último número = número en el último índice). El rango del factor de un número al siguiente es: el número de índice de un número = el número en ese índice, el número de índice del siguiente = el siguiente número de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un número a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa entre los extremos del conjunto de números de entrada, sin considerar sus ubicaciones |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Number | lista | Número interpolado resultante |

### Tween Two Numbers (Twn2Nums)

Interpola (tween) entre dos números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number A | `A` | Number | item | Número desde el que interpolar |
| Number B | `B` | Number | item | Número hacia el que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Number A, 1.0 = Number B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Number | item | Número interpolado resultante |

### X Minus One (x-1)

Resta uno a x.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number X | `x` | Number | item | Número x al que restar uno |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Minus One | `-1` | Number | item | Resultado de x menos uno |

### X Plus One (x+1)

Suma uno a x.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number X | `x` | Number | item | Número x al que sumar uno |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plus One | `+1` | Number | item | Resultado de x más uno |

### Zero Distance Tolerance (ZeroDt)

Entrega el valor de la tolerancia de distancia cero de RhinoMath (1.0e-12).

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tolerance | `t` | Number | item | Tolerancia de distancia cero de RhinoMath |

## Plane

### Average Plane (AvrPln)

Calcula el promedio aritmético de un conjunto de planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos a promediar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Plane | item | Media aritmética (promedio) de todos los planos de entrada |

### Closest Plane Orientation (CPlnOri)

Busca el plano objetivo más cercano a un plano de referencia según la orientación de uno o varios ejes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reference | `R` | Plane | item | Plano de referencia desde el que buscar |
| Targets | `T` | Plane | lista | Conjunto de planos objetivo en el que buscar |
| Axis | `A` | Integer | item | Determina en qué eje o ejes del plano buscar la orientación más cercana: 0 = {xyz}, 1 = {xy}, 2 = {xz}, 3 = {yz}, 4 = {x}, 5 = {y}, 6 = {z} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest | `C` | Plane | item | Plano objetivo más cercano al plano de referencia según la orientación de los ejes |
| Index | `i` | Integer | item | Índice del plano objetivo más cercano al plano de referencia según la orientación de los ejes |
| Angle X | `xA` | Number | item | Ángulo entre el eje {x} del plano de referencia y el eje {x} del plano objetivo más cercano, en radianes |
| Angle Y | `yA` | Number | item | Ángulo entre el eje {y} del plano de referencia y el eje {y} del plano objetivo más cercano, en radianes |
| Angle Z | `zA` | Number | item | Ángulo entre el eje {z} del plano de referencia y el eje {z} del plano objetivo más cercano, en radianes |

### Flip Plane (FlipPln)

Invierte un plano en los ejes indicados, con la opción de usar un plano guía.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano a invertir |
| Guide *(opcional)* | `G` | Plane | item | Plano guía opcional para determinar si el plano debe invertirse, según el ángulo entre el eje del plano guía y el del plano a invertir |
| Flip X | `X` | Boolean | item | Invierte el eje X del plano |
| Flip Y | `Y` | Boolean | item | Invierte el eje Y del plano |
| Flip Z | `Z` | Boolean | item | Invierte el eje Z del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Flipped | `F` | Plane | item | Plano invertido resultante |
| Result Boolean | `R` | Boolean | item | True si el plano se invirtió, False si no |

### Mirror Cut Planes (MirCutPlns)

Corta un conjunto de planos con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos a cortar y reflejar |
| Mirror Plane | `MP` | Plane | item | Plano respecto del cual se refleja el lado conservado del corte del conjunto de planos |
| Reach | `R` | Number | item | Los planos a menos de esta distancia del plano de reflejo también se cortan |
| Offset | `O` | Number | item | Distancia de desfase de los planos conservados respecto del plano de reflejo (o desde el alcance, si el alcance no es cero) |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo |
| Keep | `K` | Boolean | item | Conserva el conjunto de planos y lo refleja normalmente si el corte lo hace desaparecer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Plane | lista | Conjunto de planos cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división. Para dividir el conjunto de planos cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Reach Plane | `RP` | Plane | item | El plano a la distancia de alcance |
| Offset Plane | `OP` | Plane | item | El plano a la distancia de desfase |
| Intersected | `I` | Boolean | item | True si el corte con reflejo intersectó el conjunto de planos, False si no lo intersectó |

### Offset Plane (OffPln)

Desplaza (offset) un plano según los ejes indicados, con la opción de hacerlo hacia ambos lados a distancias distintas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano a desplazar |
| Distance | `D` | Number | item | Distancia de offset |
| Both Sides | `B` | Number | item | Distancia de offset opcional para ambos lados; usa el número inverso de la distancia para el offset en la dirección opuesta (si la distancia es positiva usa un número negativo, y viceversa) |
| Offset X | `X` | Boolean | item | Desplazamiento en la dirección X del plano |
| Offset Y | `Y` | Boolean | item | Desplazamiento en la dirección Y del plano |
| Offset Z | `Z` | Boolean | item | Desplazamiento en la dirección Z del plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset | `O` | Plane | item | Plano desplazado resultante |

### Parameter Plane Divide Surface (ParamPlnDivSrf)

Genera una grilla de planos orientados según la normal de una superficie, dividiendo su dominio con parámetros {u} y {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | árbol | Planos de división resultantes sobre la superficie |
| Normals | `N` | Vector | árbol | Vectores normales de la superficie resultantes en los orígenes de los planos de división |

### Parameter Plane In Rectangle (ParamPlnInRec)

Ubica un plano orientado según la normal de un rectángulo, dentro del rectángulo, a partir de parámetros {x} e {y} que dividen su dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo en el que ubicar el plano |
| Parameter X | `x` | Number | item | Parámetro a lo largo del dominio {x} del rectángulo ({x} 0.0 = inicio del rectángulo, 1.0 = final) |
| Parameter Y | `y` | Number | item | Parámetro a lo largo del dominio {y} del rectángulo ({y} 0.0 = inicio del rectángulo, 1.0 = final) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano resultante en el rectángulo |
| Normal | `N` | Vector | item | Vector normal del rectángulo resultante en el plano |

### Parameter Plane On Surface (ParamPlnOnSrf)

Ubica un plano orientado según la normal de una superficie, sobre la superficie, a partir de parámetros {u} y {v} que dividen su dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie sobre la que ubicar el plano |
| Parameter U | `u` | Number | item | Parámetro a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final) |
| Parameter V | `v` | Number | item | Parámetro a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano resultante sobre la superficie |
| Normal | `N` | Vector | item | Vector normal de la superficie resultante en el plano |

### Plane Trim Planes (PlnTrimPlns)

Recorta (quita) las partes de un conjunto de planos que están a un lado de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos a recortar |
| Plane | `Pl` | Plane | item | Plano con el que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Plane | lista | Conjunto de planos recortado resultante |
| Kept Indicies | `i` | Integer | lista | Índices, en el conjunto de entrada, de los planos que quedaron después del recorte |
| Intersected | `I` | Boolean | item | True si el plano recortó el conjunto de planos, False si no |

### Tween Consecutive Planes (TwnConPlns)

Interpola (tween) consecutivamente entre un conjunto de planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos entre los que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = plano en Pl, 1.0 = plano en Pl +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de planos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | lista | Planos interpolados resultantes |

### Tween Consecutive Planes On Curve (TwnConPlnsCrv)

Interpola (tween) consecutivamente entre un conjunto de planos sobre una curva; si los orígenes de los planos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos sobre la curva entre los que interpolar |
| Curve | `C` | Curve | item | Curva sobre la que interpolar los planos |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = plano en Pl, 1.0 = plano en Pl +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según la curvatura de la curva de entrada |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | lista | Planos interpolados resultantes sobre la curva |

### Tween Consecutive Planes On Surface (TwnConPlnsSrf)

Interpola (tween) consecutivamente entre un conjunto de planos sobre una superficie; si los orígenes de los planos no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos sobre la superficie entre los que interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar los puntos |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = plano en Pl, 1.0 = plano en Pl +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de planos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | lista | Planos interpolados resultantes sobre la superficie |

### Tween Through Planes (TwnThruPlns)

Interpola (tween) a través de un conjunto de planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos a través de los cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = plano al inicio de Pl, 1.0 = plano al final de Pl), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = plano en el índice 0, número de índice del último plano = plano en el último índice). El rango del factor de un plano al siguiente es: el número de índice de un plano = el plano en ese índice, el número de índice del siguiente plano = el siguiente plano de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un plano a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de planos de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de planos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | lista | Plano interpolado resultante |

### Tween Through Planes On Curve (TwnThruPlnsCrv)

Interpola (tween) a través de un conjunto de planos sobre una curva; si los orígenes de los planos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos sobre la curva a través de los cuales interpolar |
| Curve | `C` | Curve | item | Curva sobre la que interpolar el plano |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = plano al inicio de Pl, 1.0 = plano al final de Pl), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = plano en el índice 0, número de índice del último plano = plano en el último índice). El rango del factor de un plano al siguiente es: el número de índice de un plano = el plano en ese índice, el número de índice del siguiente plano = el siguiente plano de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un plano a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo de la curva entre los planos extremos, sin considerar las ubicaciones del conjunto de planos de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según la curvatura de la curva de entrada |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | lista | Plano interpolado resultante sobre la curva |

### Tween Through Planes On Surface (TwnThruPlnsSrf)

Interpola (tween) a través de un conjunto de planos sobre una superficie; si los orígenes de los planos no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos sobre la superficie a través de los cuales interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar el plano |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = plano al inicio de Pl, 1.0 = plano al final de Pl), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = plano en el índice 0, número de índice del último plano = plano en el último índice). El rango del factor de un plano al siguiente es: el número de índice de un plano = el plano en ese índice, el número de índice del siguiente plano = el siguiente plano de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un plano a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de planos de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de planos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | lista | Plano interpolado resultante sobre la superficie |

### Tween Two Planes (Twn2Plns)

Interpola (tween) entre dos planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane A | `A` | Plane | item | Plano desde el que interpolar |
| Plane B | `B` | Plane | item | Plano hacia el que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Plane A, 1.0 = Plane B) |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | item | Plano interpolado resultante |

### Tween Two Planes On Curve (Twn2PlnsCrv)

Interpola (tween) entre dos planos sobre una curva; si los orígenes de los planos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane A | `A` | Plane | item | Plano sobre la curva desde el que interpolar |
| Plane B | `B` | Plane | item | Plano sobre la curva hacia el que interpolar |
| Curve | `C` | Curve | item | Curva sobre la que interpolar el plano |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Plane A, 1.0 = Plane B) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según la curvatura de la curva de entrada |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | item | Plano interpolado resultante sobre la curva |

### Tween Two Planes On Surface (Twn2PlnsSrf)

Interpola (tween) entre dos planos sobre una superficie; si los orígenes de los planos no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane A | `A` | Plane | item | Plano sobre la superficie desde el que interpolar |
| Plane B | `B` | Plane | item | Plano sobre la superficie hacia el que interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar el plano |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Plane A, 1.0 = Plane B) |
| Quaternion | `Q` | Boolean | item | Interpola con rotación por cuaterniones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Plane | item | Plano interpolado resultante sobre la superficie |

### Weighted Average Plane (WavPln)

Calcula el promedio aritmético ponderado de un conjunto de planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Conjunto de planos a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Plane | item | Media aritmética (promedio) de todos los planos de entrada |

## Point

### Are Points Collinear (PtsCoLinr)

Prueba si un conjunto de puntos es colineal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a probar si son colineales |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Collinear | `C` | Boolean | item | True si los puntos son colineales |

### Are Points Coplanar (PtsCoPlnr)

Prueba si un conjunto de puntos es coplanar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a probar si son coplanares |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Coplanar | `C` | Boolean | item | True si los puntos son coplanares |

### Curve Coil Points (CrvCoilPts)

Crea una serie de puntos que se enrollan en espiral a lo largo de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual crear los puntos en espiral |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio {t} de la curva (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros {t} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de la curva de entrada |
| Offsets | `O` | Domain | lista | Una lista de ubicaciones de desfase, definidas por dominios, de los puntos en espiral respecto de la curva en cada parámetro de división {t} (0.0 a 0.0 = sobre la curva) |
| Rotations | `R` | Number | lista | Una lista de rotaciones de los puntos en espiral alrededor de la curva en cada parámetro de división {t}, en grados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Coiled | `C` | Point | lista | Puntos en espiral resultantes sobre la curva |

### Curve Edit Points (CrvEditPts)

Extrae los puntos de edición de una curva en los promedios de nodos: los puntos por los que pasa una curva interpolada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de la que obtener los puntos de edición |
| Knots | `K` | Boolean | item | Si es True, solo se extraen los puntos de edición en los nodos (extremos de los tramos), es decir, los puntos por los que pasa una curva interpolada. Si es False, se extraen todos los puntos de edición, que son tantos como los puntos de control de la curva (como el comando EditPtOn de Rhino) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de edición sobre la curva |
| Tangents | `T` | Vector | lista | Vectores tangentes en los puntos de edición |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de edición |

### Curve Middle Point (CrvMidPt)

Obtiene el punto en la mitad de la longitud o del dominio de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva de la que obtener el punto medio |
| Evaluation Type | `E` | Boolean | item | Si es True, se evalúa la mitad del dominio de la curva. Si es False, la mitad de su longitud. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Middle | `M` | Point | item | Punto medio de la longitud o del dominio de la curva |
| Tangent | `T` | Vector | item | Vector tangente en el punto medio de la longitud o del dominio de la curva |
| Parameter | `t` | Number | item | Valor de parámetro en el punto medio de la longitud o del dominio de la curva |
| Length | `L` | Number | item | Longitud en el punto medio de la longitud o del dominio de la curva |

### Curve Wave Points (CrvWavePts)

Crea una serie de puntos que ondulan a lo largo de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual crear los puntos en onda |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio {t} de la curva (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros {t} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de la curva de entrada |
| Offsets | `O` | Domain | lista | Una lista de ubicaciones de desfase, definidas por dominios, de los puntos en onda respecto de la curva en cada parámetro de división {t} (0.0 a 0.0 = sobre la curva) |
| Rotations | `R` | Number | lista | Una lista de rotaciones de los puntos en onda alrededor de la curva en cada parámetro de división {t}, en grados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Waved | `W` | Point | lista | Puntos en onda resultantes sobre la curva |

### Map Point To Surface (MapPt2Srf)

Mapea un punto al espacio de una superficie objetivo según su ubicación relativa al espacio de una superficie de origen.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto a mapear |
| Source | `S` | Surface | item | Superficie base del espacio de coordenadas inicial |
| Target | `T` | Surface | item | Superficie del espacio de coordenadas objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped | `M` | Point | item | Punto resultante mapeado al espacio de la superficie objetivo |

### Mirror Cut Points (MirCutPts)

Corta un conjunto de puntos con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a cortar y reflejar |
| Mirror Plane | `MP` | Plane | item | Plano respecto del cual se refleja el lado conservado del corte del conjunto de puntos |
| Reach | `R` | Number | item | Los puntos a menos de esta distancia del plano de reflejo también se cortan |
| Offset | `O` | Number | item | Distancia de desfase de los puntos conservados respecto del plano de reflejo (o desde el alcance, si el alcance no es cero) |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo |
| Keep | `K` | Boolean | item | Conserva el conjunto de puntos y lo refleja normalmente si el corte lo hace desaparecer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Point | lista | Conjunto de puntos cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división. Para dividir el conjunto de puntos cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Reach Plane | `RP` | Plane | item | El plano a la distancia de alcance |
| Offset Plane | `OP` | Plane | item | El plano a la distancia de desfase |
| Intersected | `I` | Boolean | item | True si el corte con reflejo intersectó el conjunto de puntos, False si no lo intersectó |

### Parameter Point Divide Surface (ParamPtDivSrf)

Genera una grilla de puntos sobre una superficie dividiendo su dominio con parámetros {u} y {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | árbol | Puntos de división resultantes sobre la superficie |
| Normals | `N` | Vector | árbol | Vectores normales de la superficie resultantes en los puntos de división |

### Parameter Point In Rectangle (ParamPtInRec)

Ubica un punto en un rectángulo a partir de parámetros {x} e {y} que dividen su dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo en el que ubicar el punto |
| Parameter X | `x` | Number | item | Parámetro a lo largo del dominio {x} del rectángulo ({x} 0.0 = inicio del rectángulo, 1.0 = final) |
| Parameter Y | `y` | Number | item | Parámetro a lo largo del dominio {y} del rectángulo ({y} 0.0 = inicio del rectángulo, 1.0 = final) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto resultante en el rectángulo |
| Normal | `N` | Vector | item | Vector normal del rectángulo resultante en el punto |

### Parameter Point On Surface (ParamPtOnSrf)

Ubica un punto sobre una superficie a partir de parámetros {u} y {v} que dividen su dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie sobre la que ubicar el punto |
| Parameter U | `u` | Number | item | Parámetro a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final) |
| Parameter V | `v` | Number | item | Parámetro a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto resultante sobre la superficie |
| Normal | `N` | Vector | item | Vector normal de la superficie resultante en el punto |

### Pinch'n'Spread Points (P'n'S)

Pellizca y expande (pinch & spread) un conjunto de puntos según valores de radio, intensidad y atenuación en cada punto de ubicación. Las intensidades positivas pellizcan; las negativas expanden.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a pellizcar y expandir |
| Locations | `L` | Point | lista | Conjunto de puntos que definen las ubicaciones donde pellizcar y expandir |
| Radii | `R` | Number | lista | Conjunto de radios que determinan hasta dónde llega el efecto desde los puntos de ubicación, un radio por cada punto |
| Strengths | `S` | Number | lista | Conjunto de intensidades que determinan cuánto pellizcar o expandir dentro de cada radio, una intensidad por radio. Pellizcar (0.0 = más débil, 1.0 = más fuerte). Expandir (0.0 = más débil, -1.0 = más fuerte) |
| Falloffs | `F` | Number | lista | Conjunto de atenuaciones que determinan cómo decae gradualmente la atracción de las intensidades, una por cada intensidad. Atenuación (0.0 = más brusca, 1.0 = más suave) |
| Exponents | `E` | Number | lista | Conjunto de exponentes que determinan la potencia exponencial de atracción de las atenuaciones, uno por cada atenuación |
| Weights 1 | `W¹` | Number | lista | Conjunto de pesos que tiran suavemente de las atenuaciones hacia la dirección del efecto, un peso 1 por cada atenuación. Peso 1 (0.0 = más liviano, 1.0 = más pesado) |
| Weights 2 | `W²` | Number | lista | Conjunto de pesos que tiran bruscamente de las atenuaciones hacia la dirección del efecto, un peso 2 por cada atenuación. Peso 2 (0.0 = más liviano, 1.0 = más pesado) |
| Anchors *(opcional)* | `A` | Point | lista | Puntos de anclaje opcionales, del conjunto de puntos a pellizcar y expandir, que el efecto no moverá |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pinched & Spread | `PS` | Point | lista | Puntos resultantes pellizcados y expandidos |

### Plane Trim Points (PlnTrimPts)

Recorta (quita) las partes de un conjunto de puntos que están a un lado de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a recortar |
| Plane | `Pl` | Plane | item | Plano con el que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Point | lista | Conjunto de puntos recortado resultante |
| Kept Indicies | `i` | Integer | lista | Índices, en el conjunto de entrada, de los puntos que quedaron después del recorte |
| Intersected | `I` | Boolean | item | True si el plano recortó el conjunto de puntos, False si no |

### Point Divide Curve Segments (PtDivCrvSegs)

Divide cada segmento de una curva en partes de igual longitud.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva cuyos segmentos se dividen |
| Number | `N` | Integer | item | Cantidad de divisiones por segmento |
| End Point | `E` | Boolean | item | Si la curva es cerrada, incluye el punto final (el que se duplica con el punto inicial) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de división en cada segmento de la curva |
| Tangents | `T` | Vector | lista | Vectores tangentes en los puntos de división |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de división |

### Point Divide Curve Target Length (PtDivCrvTarg)

Divide una curva en partes de igual longitud, lo más cercanas posible a una longitud objetivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Target | `T` | Number | item | Longitud objetivo de las divisiones de la curva |
| Division Type | `D` | Integer | item | Determina qué longitud de división más cercana se usa: 0 = la más cercana a la longitud objetivo; 1 = hacia abajo (la más cercana menor o igual a la longitud objetivo); 2 = hacia arriba (la más cercana mayor o igual a la longitud objetivo) |
| End Point | `E` | Boolean | item | Si la curva es cerrada, incluye el punto final (el que se duplica con el punto inicial) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de división a longitudes iguales a lo largo de la curva |
| Tangents | `T` | Vector | lista | Vectores tangentes en los puntos de división |
| Parameters | `t` | Number | lista | Valores de parámetro en los puntos de división |
| Length | `L` | Number | item | El valor de longitud usado para las divisiones |
| Result Boolean | `R` | Boolean | item | True si la longitud objetivo era menor que la longitud de la curva, False si era mayor |

### Point Mesh Side (PtMshSide)

Determina a qué lado de una malla está un punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto cuyo lado respecto de la malla se busca |
| Mesh | `M` | Mesh | item | Malla respecto de la cual determinar el lado del punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Side | `S` | Integer | item | Lado de la malla en que se encontró el punto (-1=atrás, 0=sobre la malla, 1=adelante) |
| Front | `F` | Boolean | item | Booleano que indica si el punto está delante de la malla (también True si está sobre ella) |
| Back | `B` | Boolean | item | Booleano que indica si el punto está detrás de la malla (también True si está sobre ella) |
| Distance | `D` | Number | item | Distancia entre el punto y la malla (distancia negativa = detrás de la malla, positiva = delante) |

### Point Plane Side (PtPlnSide)

Determina a qué lado de un plano está un punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto cuyo lado respecto del plano se busca |
| Plane | `Pl` | Plane | item | Plano respecto del cual determinar el lado del punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Side | `S` | Integer | item | Lado del plano en que se encontró el punto (-1=atrás, 0=sobre el plano, 1=adelante) |
| Front | `F` | Boolean | item | Booleano que indica si el punto está delante del plano (también True si está sobre él) |
| Back | `B` | Boolean | item | Booleano que indica si el punto está detrás del plano (también True si está sobre él) |
| Distance | `D` | Number | item | Distancia entre el punto y el plano (distancia negativa = detrás del plano, positiva = delante) |

### Point Surface Edge (PtSrfEdge)

Busca la arista de una superficie más cercana a un punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto del que buscar la arista de superficie más cercana |
| Surface | `S` | Surface | item | Superficie en la que buscar la arista más cercana al punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge | `E` | Curve | item | Arista de la superficie más cercana al punto |
| Edge Index | `i` | Integer | item | Índice de la arista de la superficie más cercana |

### Point Surface Side (PtSrfSide)

Determina a qué lado de una superficie está un punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto cuyo lado respecto de la superficie se busca |
| Surface | `S` | Surface | item | Superficie respecto de la cual determinar el lado del punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Side | `S` | Integer | item | Lado de la superficie en que se encontró el punto (-1=atrás, 0=sobre la superficie, 1=adelante) |
| Front | `F` | Boolean | item | Booleano que indica si el punto está delante de la superficie (también True si está sobre ella) |
| Back | `B` | Boolean | item | Booleano que indica si el punto está detrás de la superficie (también True si está sobre ella) |
| Distance | `D` | Number | item | Distancia entre el punto y la superficie (distancia negativa = detrás de la superficie, positiva = delante) |

### Reparameterize Points (ReparamPts)

Reparametriza un conjunto de puntos para que sus coordenadas {x}, {y}, {z} vayan de 0 a 1, o de forma invertida de 1 a 0.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a reparametrizar |
| Coordinates X | `X` | Boolean | item | Reparametriza las coordenadas {x} del conjunto de puntos |
| Coordinates Y | `Y` | Boolean | item | Reparametriza las coordenadas {y} del conjunto de puntos |
| Coordinates Z | `Z` | Boolean | item | Reparametriza las coordenadas {z} del conjunto de puntos |
| Dimensionality | `D` | Boolean | item | True para 2D, False para 3D |
| Invert | `I` | Boolean | item | Invierte el rango de coordenadas para que vaya de 1 a 0 en vez de 0 a 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reparameterized | `R` | Point | lista | Conjunto de puntos reparametrizado resultante |
| Original X | `xO` | Domain | item | El rango original del dominio de las coordenadas {x} del conjunto de puntos |
| Original Y | `yO` | Domain | item | El rango original del dominio de las coordenadas {y} del conjunto de puntos |
| Original Z | `zO` | Domain | item | El rango original del dominio de las coordenadas {z} del conjunto de puntos |

### Surface Edit Points (SrfEditPts)

Extrae los puntos de edición de una superficie en los promedios de nodos: los puntos por los que pasa una superficie interpolada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie de la que obtener los puntos de edición |
| Knots | `K` | Boolean | item | Si es True, solo se extraen los puntos de edición en los nodos (extremos de los tramos), es decir, los puntos por los que pasa una superficie interpolada. Si es False, se extraen todos los puntos de edición, que son tantos como los puntos de control de la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de edición sobre la superficie |
| Normals | `N` | Vector | lista | Vectores normales en los puntos de edición |
| Count U | `U` | Integer | item | Cantidad de puntos de edición en la dirección {u} de la superficie |
| Count V | `V` | Integer | item | Cantidad de puntos de edición en la dirección {v} de la superficie |
| Parameters | `uv` | Point | lista | Coordenadas de parámetro en los puntos de edición |

### Tween Consecutive Points (TwnConPts)

Interpola (tween) consecutivamente entre un conjunto de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos entre los que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = punto en P, 1.0 = punto en P +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de puntos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | lista | Puntos interpolados resultantes |

### Tween Consecutive Points On Curve (TwnConPtsCrv)

Interpola (tween) consecutivamente entre un conjunto de puntos sobre una curva; si los puntos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos sobre la curva entre los que interpolar |
| Curve | `C` | Curve | item | Curva sobre la que interpolar los puntos |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = punto en P, 1.0 = punto en P +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según la curvatura de la curva de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | lista | Puntos interpolados resultantes sobre la curva |

### Tween Consecutive Points On Surface (TwnConPtsSrf)

Interpola (tween) consecutivamente entre un conjunto de puntos sobre una superficie; si los puntos no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos sobre la superficie entre los que interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar los puntos |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = punto en P, 1.0 = punto en P +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de puntos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | lista | Puntos interpolados resultantes sobre la superficie |

### Tween Through Points (TwnThruPts)

Interpola (tween) a través de un conjunto de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a través de los cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = punto al inicio de P, 1.0 = punto al final de P), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = punto en el índice 0, número de índice del último punto = punto en el último índice). El rango del factor de un punto al siguiente es: el número de índice de un punto = el punto en ese índice, el número de índice del siguiente punto = el siguiente punto de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un punto a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de puntos de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de puntos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | lista | Punto interpolado resultante |

### Tween Through Points On Curve (TwnThruPtsCrv)

Interpola (tween) a través de un conjunto de puntos sobre una curva; si los puntos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos sobre la curva a través de los cuales interpolar |
| Curve | `C` | Curve | item | Curva sobre la que interpolar el punto |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = punto al inicio de P, 1.0 = punto al final de P), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = punto en el índice 0, número de índice del último punto = punto en el último índice). El rango del factor de un punto al siguiente es: el número de índice de un punto = el punto en ese índice, el número de índice del siguiente punto = el siguiente punto de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un punto a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo de la curva entre los puntos extremos, sin considerar las ubicaciones del conjunto de puntos de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según la curvatura de la curva de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | lista | Punto interpolado resultante sobre la curva |

### Tween Through Points On Surface (TwnThruPtsSrf)

Interpola (tween) a través de un conjunto de puntos sobre una superficie; si los puntos no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos sobre la superficie entre los que interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar el punto |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = punto al inicio de P, 1.0 = punto al final de P), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = punto en el índice 0, número de índice del último punto = punto en el último índice). El rango del factor de un punto al siguiente es: el número de índice de un punto = el punto en ese índice, el número de índice del siguiente punto = el siguiente punto de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un punto a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de puntos de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de puntos de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | lista | Punto interpolado resultante sobre la superficie |

### Tween Two Points (Twn2Pts)

Interpola (tween) entre dos puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto desde el que interpolar |
| Point B | `B` | Point | item | Punto hacia el que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Point A, 1.0 = Point B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | item | Punto interpolado resultante |

### Tween Two Points On Curve (Twn2PtsCrv)

Interpola (tween) entre dos puntos sobre una curva; si los puntos no están sobre la curva, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto sobre la curva desde el que interpolar |
| Point B | `B` | Point | item | Punto sobre la curva hacia el que interpolar |
| Curve | `C` | Curve | item | Curva sobre la que interpolar el punto |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Point A, 1.0 = Point B) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según la curvatura de la curva de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | item | Punto interpolado resultante sobre la curva |

### Tween Two Points On Surface (Twn2PtsSrf)

Interpola (tween) entre dos puntos sobre una superficie; si los puntos no están sobre la superficie, se llevan hacia ella.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Punto sobre la superficie desde el que interpolar |
| Point B | `B` | Point | item | Punto sobre la superficie hacia el que interpolar |
| Surface | `S` | Surface | item | Superficie sobre la que interpolar el punto |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Point A, 1.0 = Point B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Point | item | Punto interpolado resultante sobre la superficie |

## SubD

### Average SubD (AvrSubD, user object)

Calcula el promedio aritmético de un conjunto de SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubDs *(opcional)* | `SD` | SubD | item | Conjunto de SubDs a promediar |
| Crease Type *(opcional)* | `Cr` | Integer | item | Determina cómo se pliegan las SubDs (0 = sin pliegues, 1 = en los pliegues, 2 = en las aristas) |
| Corner Type *(opcional)* | `Co` | Integer | item | Determina cómo se tratan las esquinas de las SubDs (0 = sin esquinas, 1 = en las esquinas) |
| Interpolate Vertices *(opcional)* | `Iv` | Boolean | item | Si es True, las SubDs se interpolan pasando por los vértices de su polígono de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | SubD | item | Media aritmética (promedio) de todas las SubDs de entrada |

### Mirror Cut SubD (MirCutSubD, user object)

Corta una SubD con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo combina con el lado conservado. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD *(opcional)* | `SD` | SubD | item | SubD a cortar y reflejar |
| Mirror Plane *(opcional)* | `MP` | Plane | item | Plano respecto del cual se refleja el lado conservado del corte de la SubD |
| Reach *(opcional)* | `R` | Number | item | Las partes de la SubD a menos de esta distancia del plano de reflejo también se cortan |
| Offset *(opcional)* | `O` | Number | item | Distancia de desfase de las partes conservadas de la SubD respecto del plano de reflejo (o desde el alcance, si el alcance no es cero) |
| Flip *(opcional)* | `F` | Boolean | item | Invierte la dirección del reflejo |
| Join *(opcional)* | `J` | Boolean | item | Une la SubD cortada y reflejada |
| Keep *(opcional)* | `K` | Boolean | item | Conserva la SubD y la refleja normalmente si el corte la hace desaparecer |
| Connection Type *(opcional)* | `T` | Integer | item | Determina cómo se conectan las SubDs cortadas y reflejadas (0 = dividir caras, con conexión; 1 = quitar caras, con conexión; 2 = encoger caras, con conexión; 3 = dividir caras, sin conexión; 4 = quitar caras, sin conexión; 5 = encoger caras, sin conexión) |
| Bulge *(opcional)* | `B` | Number | item | Factor de abombamiento de las conexiones de la SubD cortada y reflejada (-B = abombamiento negativo, 0.0 = sin abombamiento, +B = abombamiento positivo) |
| Divisions *(opcional)* | `D` | Integer | item | Cantidad de divisiones de bucles de aristas de la SubD por lado de la conexión |
| Weld Vertices *(opcional)* | `W` | Number | item | Suelda los vértices de la SubD que están a cierta proximidad entre sí (0.0 = no soldar; un número mayor que 0 = soldar los vértices a menos de esa distancia) |
| Crease Type *(opcional)* | `Cr` | Integer | item | Determina cómo se pliegan las SubDs (0 = sin pliegues, 1 = en los pliegues, 2 = en las aristas) |
| Corner Type *(opcional)* | `Co` | Integer | item | Determina cómo se tratan las esquinas de las SubDs (0 = sin esquinas, 1 = en las esquinas) |
| Interpolate Vertices *(opcional)* | `Iv` | Boolean | item | Si es True, las SubDs se interpolan pasando por los vértices de su polígono de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | SubD | item | SubDs cortadas y reflejadas resultantes |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de SubDs cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Reach Plane | `RP` | Plane | item | El plano a la distancia de alcance |
| Offset Plane | `OP` | Plane | item | El plano a la distancia de desfase |
| Intersected | `I` | Boolean | item | True si el corte con reflejo intersectó la SubD, False si no la intersectó |

### Tween Consecutive SubDs (TwnConSubDs, user object)

Interpola (tween) consecutivamente entre un conjunto de SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubDs *(opcional)* | `SD` | SubD | item | Conjunto de SubDs entre las que interpolar |
| Factor *(opcional)* | `F` | Number | item | Factor de interpolación (0.0 = SubD en SD, 1.0 = SubD en SD +1) |
| Weighted *(opcional)* | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de SubDs de entrada y la curvatura del camino de interpolación |
| Loopback *(opcional)* | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree *(opcional)* | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type *(opcional)* | `I` | Integer | item | Determina cómo se interpola el camino de interpolación (0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme) |
| Crease Type *(opcional)* | `Cr` | Integer | item | Determina cómo se pliegan las SubDs (0 = sin pliegues, 1 = en los pliegues, 2 = en las aristas) |
| Corner Type *(opcional)* | `Co` | Integer | item | Determina cómo se tratan las esquinas de las SubDs (0 = sin esquinas, 1 = en las esquinas) |
| Interpolate Vertices *(opcional)* | `Iv` | Boolean | item | Si es True, las SubDs se interpolan pasando por los vértices de su polígono de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tweens | `T` | SubD | item | SubDs interpoladas resultantes |

### Tween Through SubDs (TwnThruSubDs, user object)

Interpola (tween) a través de un conjunto de SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubDs *(opcional)* | `SD` | SubD | item | Conjunto de SubDs a través de las cuales interpolar |
| Factor *(opcional)* | `F` | Number | item | Factor de interpolación (0.0 = SubD al inicio de SD, 1.0 = SubD al final de SD), salvo que Normalized sea False |
| Normalized *(opcional)* | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = SubD en el índice 0, número de índice de la última SubD = SubD en el último índice). El rango del factor de una SubD a la siguiente es: el número de índice de una SubD = la SubD en ese índice, el número de índice de la siguiente = la siguiente SubD de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una SubD a medio camino entre la del índice 2 y la del índice 3. |
| Equalized *(opcional)* | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de SubDs de entrada |
| Weighted *(opcional)* | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de SubDs de entrada y la curvatura del camino de interpolación |
| Loopback *(opcional)* | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree *(opcional)* | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type *(opcional)* | `I` | Integer | item | Determina cómo se interpola el camino de interpolación (0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme) |
| Crease Type *(opcional)* | `Cr` | Integer | item | Determina cómo se pliegan las SubDs (0 = sin pliegues, 1 = en los pliegues, 2 = en las aristas) |
| Corner Type *(opcional)* | `Co` | Integer | item | Determina cómo se tratan las esquinas de las SubDs (0 = sin esquinas, 1 = en las esquinas) |
| Interpolate Vertices *(opcional)* | `Iv` | Boolean | item | Si es True, las SubDs se interpolan pasando por los vértices de su polígono de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | SubD | item | SubD interpolada resultante |

### Tween Two SubDs (Twn2SubDs, user object)

Interpola (tween) entre dos SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD A *(opcional)* | `A` | SubD | item | SubD desde la que interpolar |
| SubD B *(opcional)* | `B` | SubD | item | SubD hacia la que interpolar |
| Factor *(opcional)* | `F` | Number | item | Factor de interpolación (0.0 = SubD A, 1.0 = SubD B) |
| Crease Type *(opcional)* | `Cr` | Integer | item | Determina cómo se pliegan las SubDs (0 = sin pliegues, 1 = en los pliegues, 2 = en las aristas) |
| Corner Type *(opcional)* | `Co` | Integer | item | Determina cómo se tratan las esquinas de las SubDs (0 = sin esquinas, 1 = en las esquinas) |
| Interpolate Vertices *(opcional)* | `Iv` | Boolean | item | Si es True, las SubDs se interpolan pasando por los vértices de su polígono de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | SubD | item | SubD interpolada resultante |

### Twisted Box Consecutive SubDs (TBoxConSubDs, user object)

Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre un conjunto de SubDs a partir de sus caras; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubDs *(opcional)* | `SD` | SubD | item | Conjunto de SubDs entre las que crear el arreglo de cajas torcidas |
| Levels *(opcional)* | `L` | Integer | item | Cantidad de niveles de subdivisión de cada cara de la SubD |
| Parameters W *(opcional)* | `w` | Number | item | Parámetros de división del dominio {w} entre cada SubD ({w} 0.0 = SubD en SD, 1.0 = SubD en SD +1). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted *(opcional)* | `W` | Boolean | item | Si es True, la distribución de los parámetros {w} se pondera según el conjunto de SubDs de entrada y la curvatura del camino de interpolación |
| Loopback *(opcional)* | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {w} continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree *(opcional)* | `D` | Integer | item | Grado de curvatura del camino de interpolación {w}; debe ser un número impar positivo |
| Interpolation Type *(opcional)* | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {w} (0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | item | Arreglo de cajas torcidas resultante, consecutivo entre las SubDs |

### Twisted Box SubD (TBoxSubD, user object)

Crea un arreglo en capas de cajas torcidas conectadas sobre una SubD, a partir de sus caras y un espesor dividido por un dominio de parámetros. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD *(opcional)* | `SD` | SubD | item | SubD sobre la que crear el arreglo de cajas torcidas |
| Thickness *(opcional)* | `T` | Number | item | Espesor total del arreglo de cajas torcidas desde la SubD, con offset desde las caras |
| Levels *(opcional)* | `L` | Integer | item | Cantidad de niveles de subdivisión de cada cara de la SubD |
| Parameters W *(opcional)* | `w` | Number | item | Parámetros de división a lo largo del dominio {w} del espesor ({w} 0.0 = SubD, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | item | Arreglo de cajas torcidas resultante sobre la SubD |

### Twisted Box Through SubDs (TBoxThruSubDs, user object)

Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de SubDs a partir de sus caras; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubDs *(opcional)* | `SD` | SubD | item | Conjunto de SubDs a través de las cuales crear el arreglo de cajas torcidas |
| Levels *(opcional)* | `L` | Integer | item | Cantidad de niveles de subdivisión de cada cara de la SubD |
| Parameters W *(opcional)* | `w` | Number | item | Parámetros de división a través del dominio {w} de las SubDs ({w} 0.0 = SubD al inicio de SD, 1.0 = SubD al final de SD), salvo que Normalized sea False |
| Normalized *(opcional)* | `N` | Boolean | item | Si es False, las reglas de los parámetros {w} son ({w} 0.0 = SubD en el índice 0, número de índice de la última SubD = SubD en el último índice). Para mejores resultados, los parámetros {w} deben estar entre 0 y el índice de la última SubD, en orden numérico y sin repetirse |
| Equalized *(opcional)* | `E` | Boolean | item | Si es True, la distribución de los parámetros {w} se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de SubDs de entrada |
| Weighted *(opcional)* | `W` | Boolean | item | Si es True, la distribución de los parámetros {w} se pondera según el conjunto de SubDs de entrada y la curvatura del camino de interpolación |
| Loopback *(opcional)* | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {w} continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango de los parámetros {w}) |
| Degree *(opcional)* | `D` | Integer | item | Grado de curvatura del camino de interpolación {w}; debe ser un número impar positivo |
| Interpolation Type *(opcional)* | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {w} (0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | item | Arreglo de cajas torcidas resultante a través de las SubDs |

### Twisted Box Two SubDs (TBox2SubDs, user object)

Crea un arreglo en capas de cajas torcidas conectadas entre dos SubDs a partir de sus caras; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD A *(opcional)* | `A` | SubD | item | SubD desde la que crear las cajas torcidas |
| SubD B *(opcional)* | `B` | SubD | item | SubD hacia la que crear las cajas torcidas |
| Levels *(opcional)* | `L` | Integer | item | Cantidad de niveles de subdivisión de cada cara de la SubD |
| Parameters W *(opcional)* | `w` | Number | item | Parámetros de división del dominio {w} entre las SubDs ({w} 0.0 = SubD A, 1.0 = SubD B). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | item | Arreglo de cajas torcidas resultante entre las SubDs |

### Weighted Average SubD (WavSubD, user object)

Calcula el promedio aritmético ponderado de un conjunto de SubDs; las SubDs deben tener la misma topología. (*Solo Rhino 7)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubDs *(opcional)* | `SD` | SubD | item | Conjunto de SubDs a promediar |
| Weights *(opcional)* | `W` | Number | item | Colección de pesos de cada SubD |
| Crease Type *(opcional)* | `Cr` | Integer | item | Determina cómo se pliegan las SubDs (0 = sin pliegues, 1 = en los pliegues, 2 = en las aristas) |
| Corner Type *(opcional)* | `Co` | Integer | item | Determina cómo se tratan las esquinas de las SubDs (0 = sin esquinas, 1 = en las esquinas) |
| Interpolate Vertices *(opcional)* | `Iv` | Boolean | item | Si es True, las SubDs se interpolan pasando por los vértices de su polígono de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | SubD | item | Media aritmética (promedio) de todas las SubDs de entrada |

## Surface

### Append Polysurfaces (AppPsrfs)

Agrega un conjunto de polisuperficies (Breps) desconectadas para formar una sola polisuperficie (Brep), aunque no se toquen ni estén unidas. También puede agregar superficies.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurfaces | `Ps` | Brep | lista | Conjunto de polisuperficies (Breps) o superficies a agregar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Appended | `A` | Brep | item | Polisuperficie (Brep) única resultante, con partes desconectadas |

### Automatic Edge Surface (AutoEdgSrf)

Crea una superficie entre 2, 3 o 4 curvas de borde ordenadas automáticamente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Conjunto de 2, 3 o 4 curvas de borde a ordenar automáticamente para crear la superficie entre ellas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Automatic | `A` | Brep | item | Superficie de bordes automática resultante |

### Automatic Network Surface (AutoNetSrf)

Crea una superficie a partir de una red de curvas ordenada automáticamente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Network | `N` | Curve | lista | Curvas de la red a ordenar automáticamente para crear la superficie de red |
| Continuity Type | `T` | Integer | item | Determina la continuidad de la superficie: 0 = holgada, 1 = posición, 2 = tangencia, 3 = curvatura |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Automatic | `A` | Surface | item | Superficie de red automática resultante |

### Average Surface (AvrSrf)

Calcula el promedio aritmético de un conjunto de superficies; las superficies recortadas se tratan como sin recortar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Conjunto de superficies a promediar |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da promedios de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da promedios de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Surface | item | Media aritmética (promedio) de todas las superficies de entrada |

### Constrained Volume Box (ConsVolBox)

Crea una caja rectangular o regular del tamaño de un volumen dado, con factores de proporción {x}, {y} y {z}, centrada en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base de la caja |
| Volume | `V` | Number | item | Volumen de la caja |
| Factor X | `x` | Number | item | Factor de proporción en la dirección {x} del plano (usa el mismo valor para {x}, {y} y {z} para una caja regular) |
| Factor Y | `y` | Number | item | Factor de proporción en la dirección {y} del plano (usa el mismo valor para {x}, {y} y {z} para una caja regular) |
| Factor Z | `z` | Number | item | Factor de proporción en la dirección {z} del plano (usa el mismo valor para {x}, {y} y {z} para una caja regular) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja resultante restringida por volumen |
| Dimension X | `X` | Number | item | Dimensión {x} en el plano de la caja |
| Dimension Y | `Y` | Number | item | Dimensión {y} en el plano de la caja |
| Dimension Z | `Z` | Number | item | Dimensión {z} en el plano de la caja |

### Constrained Volume Ellipsoid (ConsVolEli)

Crea un elipsoide o esfera del tamaño de un volumen dado, con factores de proporción {x}, {y} y {z}, centrado en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base del elipsoide |
| Volume | `V` | Number | item | Volumen del elipsoide |
| Factor X | `x` | Number | item | Factor de proporción en la dirección {x} del plano (usa el mismo valor para {x}, {y} y {z} para una esfera) |
| Factor Y | `y` | Number | item | Factor de proporción en la dirección {y} del plano (usa el mismo valor para {x}, {y} y {z} para una esfera) |
| Factor Z | `z` | Number | item | Factor de proporción en la dirección {z} del plano (usa el mismo valor para {x}, {y} y {z} para una esfera) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ellipsoid | `E` | Surface | item | Elipsoide resultante restringido por volumen |

### Extrude Tapered Polysurface (ExtrTaper)

Extruye un perfil con conicidad según un ángulo de desmoldeo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Profile | `P` | Curve | item | Curva o superficie de perfil a extruir; funciona mejor si el perfil es plano |
| Direction | `D` | Vector | item | Vector de dirección de extrusión; funciona mejor si es perpendicular al perfil |
| Angle | `A` | Number | item | Ángulo de desmoldeo de la conicidad, en grados |
| Corner Type | `T` | Integer | item | Determina cómo se hacen las esquinas en las extrusiones que se abren hacia afuera: 0 = agudas, 1 = suaves, 2 = redondas, 3 = chaflán, 4 = ninguna |
| Face Merge | `F` | Boolean | item | Fusiona las caras coplanares de la polisuperficie en superficies únicas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extruded | `E` | Brep | lista | Extrusión cónica resultante |

### Fit Surface (FitSrf)

Ajusta una nueva superficie a una superficie existente cuando es posible, sin cambiar la forma general; también funciona con superficies recortadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie a ajustar |
| Degree U *(opcional)* | `U` | Integer | item | Grado al que ajustar la dirección {u} de la superficie (si se omite, se usa el grado {u} de la superficie de entrada) |
| Degree V *(opcional)* | `V` | Integer | item | Grado al que ajustar la dirección {v} de la superficie (si se omite, se usa el grado {v} de la superficie de entrada) |
| Tolerance | `t` | Number | item | Tolerancia de ajuste (si se omite, se usa la tolerancia del documento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fitted | `F` | Brep | item | Superficie ajustada resultante |
| Result Boolean | `R` | Boolean | item | True si la superficie se ajustó |

### Flip Polysurface (FlipPsrf)

Invierte las normales de una polisuperficie (Brep); las polisuperficies cerradas no se pueden invertir y salen sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | item | Polisuperficie (Brep) a invertir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Flipped | `F` | Brep | item | Polisuperficie (Brep) invertida resultante |
| Result Boolean | `R` | Boolean | item | True si la polisuperficie (Brep) se invirtió, False si no se invirtió o es cerrada |

### Is Polysurface Closed (PsrfClsd)

Prueba si una polisuperficie (Brep) es cerrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | item | Polisuperficie (Brep) a probar si es cerrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closed | `C` | Boolean | item | True si la polisuperficie (Brep) es cerrada |

### Is Surface Closed (SrfClsd)

Prueba si una superficie es cerrada y si sus aristas se cierran en las direcciones {u} o {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a probar si es cerrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closed | `C` | Boolean | item | True si la superficie es cerrada como sólido |
| Closed U | `U` | Boolean | item | True si la arista de la superficie se cierra en la dirección {u} |
| Closed V | `V` | Boolean | item | True si la arista de la superficie se cierra en la dirección {v} |

### Is Surface Collapsed (SrfCollapsed)

Prueba si una superficie tiene aristas colapsadas en un punto (singularidades).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie en la que buscar aristas colapsadas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge 1 | `E¹` | Boolean | item | True si la arista 1 (sur) de la superficie está colapsada |
| Edge 2 | `E²` | Boolean | item | True si la arista 2 (este) de la superficie está colapsada |
| Edge 3 | `E³` | Boolean | item | True si la arista 3 (norte) de la superficie está colapsada |
| Edge 4 | `E⁴` | Boolean | item | True si la arista 4 (oeste) de la superficie está colapsada |

### Is Surface Trimmed (SrfTrimd)

Prueba si una superficie está recortada; también puede buscar caras recortadas en una polisuperficie (Brep).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie (o polisuperficie (Brep)) a probar si está recortada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Boolean | lista | True si la superficie (o polisuperficie (Brep)) está recortada |

### Mesh To Polysurface (Msh2Psrf)

Convierte una malla en una polisuperficie NURBS (Brep).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a convertir en polisuperficie |
| Triangles | `T` | Boolean | item | Si es True, las caras triangulares se convierten en superficies triangulares recortadas. Si es False, se convierten en superficies sin recortar donde la primera y la cuarta esquina se superponen |
| Face Merge | `F` | Boolean | item | Fusiona las caras coplanares de la polisuperficie en superficies únicas. ADVERTENCIA: esta opción puede ser pesada según la cantidad de caras coplanares de la malla; guarda antes de usarla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | lista | Polisuperficie (Brep) resultante |

### Mirror Cut Polysurface (MirCutPsrf)

Corta una polisuperficie (Brep) con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo combina con el lado conservado. También puede cortar y reflejar superficies.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | item | Polisuperficie (Brep) o superficie a cortar y reflejar |
| Mirror Plane | `MP` | Plane | item | Plano respecto del cual se refleja el lado conservado del corte de la polisuperficie (Brep) o superficie |
| Reach | `R` | Number | item | Las partes de la polisuperficie (Brep) o superficie a menos de esta distancia del plano de reflejo también se cortan |
| Offset | `O` | Number | item | Distancia de desfase de las partes conservadas respecto del plano de reflejo (o desde el alcance, si el alcance no es cero) |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo |
| Join | `J` | Boolean | item | Une la polisuperficie (Brep) o superficie cortada y reflejada |
| Keep | `K` | Boolean | item | Conserva la polisuperficie (Brep) o superficie y la refleja normalmente si el corte la hace desaparecer |
| Connection Type | `T` | Integer | item | Determina cómo se conectan las polisuperficies (Breps) o superficies cortadas y reflejadas: 0 = recta, 1 = uniforme, 2 = holgada, 3 = ajustada, 4 = ninguna |
| Bulge | `B` | Number | item | Factor de abombamiento de las conexiones de la polisuperficie (Brep) o superficie cortada y reflejada (-B = abombamiento negativo, 0.0 = sin abombamiento, +B = abombamiento positivo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Brep | lista | Polisuperficies (Breps) o superficies cortadas y reflejadas resultantes |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Reach Plane | `RP` | Plane | item | El plano a la distancia de alcance |
| Offset Plane | `OP` | Plane | item | El plano a la distancia de desfase |
| Intersected | `I` | Boolean | item | True si el corte con reflejo intersectó la polisuperficie (Brep) o superficie, False si no |

### Mirror Cut Surface (MirCutSrf)

Corta una superficie con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo combina con el lado conservado (para superficies recortadas usa Mirror Cut Polysurface).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a cortar y reflejar |
| Mirror Plane | `MP` | Plane | item | Plano respecto del cual se refleja el lado conservado del corte de la superficie |
| Reach | `R` | Number | item | Las partes de la superficie a menos de esta distancia del plano de reflejo también se cortan |
| Offset | `O` | Number | item | Distancia de desfase de las partes conservadas de la superficie respecto del plano de reflejo (o desde el alcance, si el alcance no es cero) |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo |
| Join | `J` | Boolean | item | Une las superficies cortadas y reflejadas |
| Keep | `K` | Boolean | item | Conserva la superficie y la refleja normalmente si el corte la hace desaparecer |
| Connection Type | `T` | Integer | item | Determina cómo se conectan las superficies cortadas y reflejadas: 0 = lineal, 1 = tangencia, 2 = curvatura, 3 = ninguna |
| Bulge | `B` | Number | item | Factor de abombamiento de las conexiones de la superficie cortada y reflejada (-B = abombamiento negativo, 0.0 = sin abombamiento, +B = abombamiento positivo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Brep | lista | Superficies cortadas y reflejadas resultantes |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto de superficies cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Reach Plane | `RP` | Plane | item | El plano a la distancia de alcance |
| Offset Plane | `OP` | Plane | item | El plano a la distancia de desfase |
| Intersected | `I` | Boolean | item | True si el corte con reflejo intersectó la superficie, False si no la intersectó |

### Offset Surface (OffSrf)

Aplica offset a una superficie, con la opción de hacerlo hacia ambos lados a distancias distintas y crear un sólido; también funciona con superficies recortadas y con caras de polisuperficie (Brep) como offsets separados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie (o polisuperficie (Brep)) a la que aplicar offset |
| Distance | `D` | Number | item | Distancia de offset |
| Both Sides | `B` | Number | item | Distancia de offset opcional para ambos lados; usa el número inverso de la distancia para el offset en la dirección opuesta (si la distancia es positiva usa un número negativo, y viceversa) |
| Create Solid | `C` | Boolean | item | Si es True, crea un offset sólido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset | `O` | Brep | lista | Superficie (o polisuperficie (Brep)) con offset resultante |

### Parameter Subdivide Surface (ParamSubDivSrf)

Genera una grilla de superficies de subdivisión sobre una superficie, dividiendo su dominio con parámetros {u} y {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Subdivided | `S` | Surface | lista | Superficies de subdivisión resultantes |

### Plane Trim Surface (PlnTrimSrf)

Recorta (quita) las partes de una superficie que están a un lado de un plano; también funciona con superficies recortadas y polisuperficies (Breps).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie (o polisuperficie (Brep)) a recortar |
| Plane | `Pl` | Plane | item | Plano con el que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Brep | lista | Superficie (o polisuperficie (Brep)) recortada resultante |
| Intersected | `I` | Boolean | item | True si el plano recortó la superficie (o polisuperficie (Brep)), False si no |

### Rebuild Surface (RebSrf)

Reconstruye una superficie con una cantidad de puntos, un grado y un dominio dados en las direcciones {u} y {v}; también funciona con superficies recortadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie a reconstruir |
| Count U *(opcional)* | `uP` | Integer | item | Cantidad de puntos de control en la dirección {u} (si se omite, se usa la de la superficie de entrada) |
| Count V *(opcional)* | `vP` | Integer | item | Cantidad de puntos de control en la dirección {v} (si se omite, se usa la de la superficie de entrada) |
| Degree U *(opcional)* | `uD` | Integer | item | Grado de la superficie en la dirección {u} (si se omite, se usa el de la superficie de entrada) |
| Degree V *(opcional)* | `vD` | Integer | item | Grado de la superficie en la dirección {v} (si se omite, se usa el de la superficie de entrada) |
| Domain U *(opcional)* | `uI` | Domain | item | Dominio de la superficie en la dirección {u} (si se omite, se usa el de la superficie de entrada) |
| Domain V *(opcional)* | `vI` | Domain | item | Dominio de la superficie en la dirección {v} (si se omite, se usa el de la superficie de entrada) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rebuilt | `R` | Brep | item | Superficie reconstruida resultante |

### Remap Surface Domain² (ReSrfDom²)

Reasigna el rango del dominio² {uv} de una superficie a un rango de entrada, con la opción de igualar el rango del dominio² {uv} de una superficie guía; también funciona con superficies recortadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie cuyo rango de dominio² {uv} se reasigna |
| Guide *(opcional)* | `G` | Surface | item | Superficie guía opcional cuyo rango de dominio² {uv} se iguala (reemplaza al dominio² si también se entrega uno) |
| Domain² *(opcional)* | `I²` | Domain² | item | Rango de dominio² al que reasignar la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Remapped | `R` | Brep | item | Superficie resultante con el rango de dominio² {uv} reasignado |
| Original | `O` | Domain² | item | El rango original del dominio² {uv} de la superficie |
| New | `N` | Domain² | item | El nuevo rango del dominio² {uv} de la superficie |

### Reparameterize Surface (ReparamSrf)

Reparametriza una superficie para que su dominio² (uv) vaya de 0 a 1; también funciona con superficies recortadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie a reparametrizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reparameterized | `R` | Brep | item | Superficie reparametrizada resultante, con dominio² {uv} de 0 a 1 |
| Original | `O` | Domain² | item | El rango original del dominio² {uv} de la superficie |

### Shell Polysurface (ShellPsrf)

Crea un cascarón hueco con espesor a partir de una polisuperficie cerrada (Brep).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | item | Polisuperficie cerrada (Brep) a la que hacer el vaciado |
| Removal | `R` | Integer | lista | Índices de las caras de la polisuperficie cerrada a quitar para el vaciado; se debe quitar al menos una cara |
| Thickness | `T` | Number | item | Espesor del cascarón |
| Face Merge | `F` | Boolean | item | Fusiona las caras coplanares de la polisuperficie en superficies únicas. ADVERTENCIA: esta opción puede ser pesada según la cantidad de caras coplanares; guarda antes de usarla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell | `S` | Brep | lista | Cascarón de polisuperficie (Brep) resultante |

### Shrink Trimmed Surface (ShrinkTrimSrf)

Encoge la superficie sin recortar subyacente de una superficie recortada para que quede lo más cerca posible de sus bordes de recorte; también puede encoger caras recortadas de polisuperficies (Brep).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Encoge la superficie sin recortar subyacente de una superficie recortada para que quede lo más cerca posible de sus bordes de recorte; también funciona con caras de polisuperficies (Brep). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shrunken | `S` | Brep | item | Superficie (o polisuperficie (Brep)) recortada resultante, con la superficie subyacente encogida |
| Underlying | `U` | Surface | lista | La superficie sin recortar subyacente, ya encogida, de la superficie (o polisuperficie (Brep)) recortada |
| Result Boolean | `R` | Boolean | lista | True si la superficie subyacente de la superficie recortada se encogió. False si ya estaba encogida o si la superficie de entrada no estaba recortada |

### Split Kinky Surface (SplitKinkySrf)

Divide en una polisuperficie (Brep) la superficie de salida de un componente de superficie sin dividir, si tiene quiebres; si no tiene quiebres, sale sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir en los quiebres para formar una polisuperficie (Brep) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | item | Polisuperficie (Brep) resultante dividida en los quiebres |
| Result Boolean | `R` | Boolean | item | True si la superficie tenía quiebres y se dividió, False si no tenía quiebres |

### Superimpose Surface (SuperSrf)

Superpone la cantidad de puntos de control {uv}, el grado {uv}, el dominio {uv} y los recortes de una superficie de referencia sobre una superficie objetivo; también funciona con superficies recortadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reference | `R` | Brep | item | Superficie de referencia de la que tomar las propiedades |
| Target | `T` | Brep | item | Superficie objetivo sobre la que superponer las propiedades |
| Points U | `uP` | Boolean | item | Superpone los puntos de control {u} de la superficie de referencia sobre la objetivo |
| Points V | `vP` | Boolean | item | Superpone los puntos de control {v} de la superficie de referencia sobre la objetivo |
| Degree U | `uD` | Boolean | item | Superpone el grado {u} de la superficie de referencia sobre la objetivo |
| Degree V | `vD` | Boolean | item | Superpone el grado {v} de la superficie de referencia sobre la objetivo |
| Domain U | `uI` | Boolean | item | Superpone el dominio {u} de la superficie de referencia sobre la objetivo |
| Domain V | `vI` | Boolean | item | Superpone el dominio {v} de la superficie de referencia sobre la objetivo |
| Trims | `rT` | Boolean | item | Superpone los recortes de la superficie de referencia sobre la objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Superimposed | `S` | Brep | item | Superficie superpuesta resultante |

### Surface Degree (SrfDeg)

Obtiene el valor del grado de una superficie en sus direcciones {u} y {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie de la que obtener el grado {u} y {v} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Degree U | `U` | Integer | item | Valor del grado de la superficie en la dirección {u} |
| Degree V | `V` | Integer | item | Valor del grado de la superficie en la dirección {v} |

### Surface Spans (Srfpans)

Obtiene los subdominios² de cada tramo (span) de una superficie e información de los tramos: subdominios de cada tramo, cantidad de tramos en cada dirección, longitudes y grados de cada tramo, parámetros de las isocurvas de los tramos y coordenadas de parámetro de la superficie en los extremos de los tramos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie de la que obtener información de los tramos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sub-Domain²s | `S²` | Domain² | lista | Subdominio² de cada tramo que forma la superficie. Para extraer cada tramo como superficie separada, usa estos valores como entrada Domain (D) del componente Isotrim de Grasshopper. |
| Sub-Domain U | `uS` | Domain | lista | Dominio en la dirección {u} de cada tramo que forma la superficie |
| Sub-Domain V | `vS` | Domain | lista | Dominio en la dirección {v} de cada tramo que forma la superficie |
| Amount U | `uA` | Integer | item | Cantidad de tramos en la dirección {u} que forman la superficie |
| Amount V | `vA` | Integer | item | Cantidad de tramos en la dirección {v} que forman la superficie |
| Lengths U | `uL` | Number | lista | Longitud aproximada en la dirección {u} de cada tramo que forma la superficie |
| Lengths V | `vL` | Number | lista | Longitud aproximada en la dirección {v} de cada tramo que forma la superficie |
| Degrees U | `uD` | Integer | lista | Grado en la dirección {u} de cada tramo que forma la superficie |
| Degrees V | `vD` | Integer | lista | Grado en la dirección {v} de cada tramo que forma la superficie |
| Parameters U | `u` | Number | lista | Parámetro en la dirección {u} de cada isocurva de tramo que forma la superficie |
| Parameters V | `v` | Number | lista | Parámetro en la dirección {v} de cada isocurva de tramo que forma la superficie |
| Parameters UV | `uv` | Point | lista | Coordenadas de parámetro de la superficie en los extremos de los tramos. Para obtener el punto entre cada tramo, usa estos valores como entrada Point (uv) del componente Evaluate Surface de Grasshopper. |

### Surface Statistics (SrfStats)

Obtiene estadísticas de una superficie o polisuperficie (Brep): cantidad de caras, de caras sin recortar, de caras recortadas, de aristas, de vértices y de puntos de control.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie o polisuperficie (Brep) de la que obtener estadísticas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Face Count | `F` | Integer | item | Cantidad de caras de la superficie o polisuperficie (Brep) |
| Untrimmed Face Count | `U` | Integer | item | Cantidad de caras sin recortar de la superficie o polisuperficie (Brep) |
| Trimmed Face Count | `T` | Integer | item | Cantidad de caras recortadas de la superficie o polisuperficie (Brep) |
| Edge Count | `E` | Integer | item | Cantidad de aristas de la superficie o polisuperficie (Brep) |
| Vertex Count | `V` | Integer | item | Cantidad de vértices de la superficie o polisuperficie (Brep) |
| Control Point Count | `C` | Integer | item | Cantidad de puntos de control de la superficie o polisuperficie (Brep) |

### Swap Surface Directions (SwapSrfDir)

Intercambia o invierte las direcciones {u} y {v} de una superficie; también funciona con superficies recortadas, pero los recortes también se intercambian.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Superficie cuyas direcciones se cambian |
| Reverse U | `U` | Boolean | item | Invierte la dirección {u} de la superficie |
| Reverse V | `V` | Boolean | item | Invierte la dirección {v} de la superficie |
| Swap UV | `UV` | Boolean | item | Intercambia las direcciones {u} y {v} de la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Swapped | `S` | Brep | item | Superficie resultante con las direcciones intercambiadas |

### Tween Consecutive Surfaces (TwnConSrfs)

Interpola (tween) consecutivamente entre un conjunto de superficies; las superficies recortadas se tratan como sin recortar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Conjunto de superficies entre las que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = superficie en S, 1.0 = superficie en S +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de superficies de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Surface | lista | Superficies interpoladas resultantes |

### Tween Through Surfaces (TwnThruSrfs)

Interpola (tween) a través de un conjunto de superficies; las superficies recortadas se tratan como sin recortar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Conjunto de superficies a través de las cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = superficie al inicio de S, 1.0 = superficie al final de S), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = superficie en el índice 0, número de índice de la última superficie = superficie en el último índice). El rango del factor de una superficie a la siguiente es: el número de índice de una superficie = la superficie en ese índice, el número de índice de la siguiente = la siguiente superficie de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una superficie a medio camino entre la del índice 2 y la del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de superficies de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de superficies de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Surface | lista | Superficie interpolada resultante |

### Tween Two Surfaces (Twn2Srfs)

Interpola (tween) entre dos superficies; las superficies recortadas se tratan como sin recortar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface A | `A` | Surface | item | Superficie desde la que interpolar |
| Surface B | `B` | Surface | item | Superficie hacia la que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Surface A, 1.0 = Surface B) |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Surface | item | Superficie interpolada resultante |

### Tween Two Surfaces Along Curve (Twn2SrfsCrv)

Interpola (tween) entre dos superficies a lo largo de una curva guía (u opcionalmente de dos curvas guía); las superficies recortadas se tratan como sin recortar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface A | `A` | Surface | item | Superficie sobre la curva guía desde la que interpolar |
| Surface B | `B` | Surface | item | Superficie sobre la curva guía hacia la que interpolar |
| Guide 1 | `G¹` | Curve | item | Curva guía a lo largo de la cual interpolar (mejor si va de Surface A a Surface B) |
| Guide 2 *(opcional)* | `G²` | Curve | item | Segunda curva guía opcional a lo largo de la cual interpolar (mejor si va en la dirección de Guide 1) |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Surface A, 1.0 = Surface B) |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da interpolaciones de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da interpolaciones de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Surface | item | Superficie interpolada resultante a lo largo de la curva |

### Unroll Polysurface (UnrollPsrf)

Desenrolla una polisuperficie (Brep) para que sus caras queden planas sobre un plano, con la opción de desenrollar puntos y curvas junto con sus caras. También puede desenrollar superficies.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | item | Polisuperficie (Brep) o superficie a desenrollar |
| Plane *(opcional)* | `Pl` | Plane | item | Plano opcional sobre el que desenrollar; si no se define, se usa el plano XY del mundo |
| Points *(opcional)* | `P` | Point | lista | Puntos opcionales a desenrollar con la polisuperficie (Brep) o superficie; deben estar exactamente sobre sus caras |
| Curves *(opcional)* | `C` | Curve | lista | Curvas opcionales a desenrollar con la polisuperficie (Brep) o superficie; deben estar exactamente sobre sus caras |
| Explode *(opcional)* | `E` | Number | item | Número opcional que explota las caras desenrolladas de la polisuperficie (Brep) como un arreglo lineal desconectado, separadas por esa distancia; los puntos y curvas desenrollados las siguen |
| Area Tolerance *(opcional)* | `a` | Number | item | Tolerancia de desviación de área permitida para determinar si la polisuperficie (Brep) o superficie se puede desenrollar (si se omite, se usa la tolerancia del documento) |
| Edge Tolerance *(opcional)* | `e` | Number | item | Tolerancia de desviación de aristas permitida para determinar si la polisuperficie (Brep) o superficie se puede desenrollar (si se omite, se usa la tolerancia del documento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unrolled | `U` | Brep | lista | Caras desenrolladas resultantes de la polisuperficie (Brep) o superficie |
| Unrolled Points | `Up` | Point | lista | Los puntos desenrollados con las caras de la polisuperficie (Brep) o superficie |
| Unrolled Curves | `Uc` | Curve | lista | Las curvas desenrolladas con las caras de la polisuperficie (Brep) o superficie |

### Unsplit Edge Surface (UnsplitEdge)

Crea una superficie de bordes sin recortar entre 2, 3 o 4 curvas de borde, que no se divide en una polisuperficie (Brep) en los quiebres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Conjunto de 2, 3 o 4 curvas de borde entre las que crear la superficie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unsplit | `U` | Surface | item | Superficie de bordes resultante, única, sin recortar y sin dividir. Al hacer bake en Rhino pasa a ser una polisuperficie (Brep) normal dividida en sus quiebres si los tiene, salvo que antes ejecutes el comando CreaseSplitting en la línea de comandos de Rhino y lo pongas en No. Si la superficie tiene quiebres, puedes convertirla en polisuperficie (Brep) con el componente Split Kinky Surface de Pufferfish. |

### Unsplit Extrude Surface (UnsplitExtr)

Crea una superficie extruida sin recortar a partir de una curva o superficie de perfil, a lo largo de un vector, una curva o hacia un punto, que no se divide en una polisuperficie (Brep) en los quiebres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Profile | `P` | Curve | item | Curva o superficie de perfil a extruir |
| Direction | `D` | Generic Data | item | Vector, curva o punto de dirección de extrusión. Entrega un vector para extruir a lo largo de un vector, una curva para extruir a lo largo de una curva o un punto para extruir hacia un punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unsplit | `U` | Surface | item | Superficie extruida resultante, única, sin recortar y sin dividir. Al hacer bake en Rhino pasa a ser una polisuperficie (Brep) normal dividida en sus quiebres si los tiene, salvo que antes ejecutes el comando CreaseSplitting en la línea de comandos de Rhino y lo pongas en No. Si la superficie tiene quiebres, puedes convertirla en polisuperficie (Brep) con el componente Split Kinky Surface de Pufferfish. |

### Unsplit Loft Surface (UnsplitLoft)

Crea una superficie con loft sin recortar a través de un conjunto de curvas o superficies de sección, que no se divide en una polisuperficie (Brep) en los quiebres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sections | `S` | Curve | lista | Conjunto de curvas o superficies de sección a través de las cuales hacer el loft |
| Closed | `C` | Boolean | item | Loft cerrado: si es True, la última curva de sección hace loft de vuelta a la primera |
| Loft Type | `T` | Integer | item | Determina cómo se hace el loft de las curvas de sección: 0 = normal, 1 = holgado, 2 = ajustado, 3 = uniforme, 4 = recto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unsplit | `U` | Surface | item | Superficie con loft resultante, única, sin recortar y sin dividir. Al hacer bake en Rhino pasa a ser una polisuperficie (Brep) normal dividida en sus quiebres si los tiene, salvo que antes ejecutes el comando CreaseSplitting en la línea de comandos de Rhino y lo pongas en No. Si la superficie tiene quiebres, puedes convertirla en polisuperficie (Brep) con el componente Split Kinky Surface de Pufferfish. |

### Unsplit Rail Revolve Surface (UnsplitRailRev)

Crea una superficie de revolución sin recortar a partir de una curva o superficie de perfil, guiada por una curva de riel alrededor de un eje, que no se divide en una polisuperficie (Brep) en los quiebres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Profile | `P` | Curve | item | Curva o superficie de perfil a revolucionar |
| Axis | `A` | Line | item | Línea de eje alrededor de la cual revolucionar |
| Rail | `R` | Curve | item | Curva de riel que guía la revolución del perfil alrededor del eje |
| Scale | `S` | Boolean | item | Escala localmente la revolución |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unsplit | `U` | Surface | item | Superficie de revolución con riel resultante, única, sin recortar y sin dividir. Al hacer bake en Rhino pasa a ser una polisuperficie (Brep) normal dividida en sus quiebres si los tiene, salvo que antes ejecutes el comando CreaseSplitting en la línea de comandos de Rhino y lo pongas en No. Si la superficie tiene quiebres, puedes convertirla en polisuperficie (Brep) con el componente Split Kinky Surface de Pufferfish. |

### Unsplit Revolve Surface (UnsplitRev)

Crea una superficie de revolución sin recortar a partir de una curva o superficie de perfil alrededor de un eje, que no se divide en una polisuperficie (Brep) en los quiebres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Profile | `P` | Curve | item | Curva o superficie de perfil a revolucionar |
| Axis | `A` | Line | item | Línea de eje alrededor de la cual revolucionar |
| Revolution | `R` | Domain | item | Dominio de la revolución en grados alrededor del eje (0 = inicio, 360 = final) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unsplit | `U` | Surface | item | Superficie de revolución resultante, única, sin recortar y sin dividir. Al hacer bake en Rhino pasa a ser una polisuperficie (Brep) normal dividida en sus quiebres si los tiene, salvo que antes ejecutes el comando CreaseSplitting en la línea de comandos de Rhino y lo pongas en No. Si la superficie tiene quiebres, puedes convertirla en polisuperficie (Brep) con el componente Split Kinky Surface de Pufferfish. |

### Unsplit Sum Surface (UnsplitSum)

Crea una superficie de suma sin recortar a partir de dos curvas de borde, que no se divide en una polisuperficie (Brep) en los quiebres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Curva de borde que define los bordes {u} de la superficie de suma |
| Curve B | `B` | Curve | item | Curva de borde que define los bordes {v} de la superficie de suma |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unsplit | `U` | Surface | item | Superficie de suma resultante, única, sin recortar y sin dividir. Al hacer bake en Rhino pasa a ser una polisuperficie (Brep) normal dividida en sus quiebres si los tiene, salvo que antes ejecutes el comando CreaseSplitting en la línea de comandos de Rhino y lo pongas en No. Si la superficie tiene quiebres, puedes convertirla en polisuperficie (Brep) con el componente Split Kinky Surface de Pufferfish. |

### Unsplit Sweep Surface (UnsplitSwp)

Crea una superficie de barrido (sweep) sin recortar a través de un conjunto de curvas o superficies de sección a lo largo de una curva de riel (u opcionalmente de dos), que no se divide en una polisuperficie (Brep) en los quiebres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sections | `S` | Curve | lista | Curvas o superficies de sección a través de las cuales hacer el barrido |
| Rail 1 | `R¹` | Curve | item | Curva de riel a lo largo de la cual hacer el barrido (mejor si va de la primera sección de S a la última) |
| Rail 2 *(opcional)* | `R²` | Curve | item | Segunda curva de riel opcional para el barrido (mejor si va en la dirección de Rail 1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unsplit | `U` | Surface | item | Superficie de barrido resultante, única, sin recortar y sin dividir. Al hacer bake en Rhino pasa a ser una polisuperficie (Brep) normal dividida en sus quiebres si los tiene, salvo que antes ejecutes el comando CreaseSplitting en la línea de comandos de Rhino y lo pongas en No. Si la superficie tiene quiebres, puedes convertirla en polisuperficie (Brep) con el componente Split Kinky Surface de Pufferfish. |

### Weighted Average Surface (WavSrf)

Calcula el promedio aritmético ponderado de un conjunto de superficies; las superficies recortadas se tratan como sin recortar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Conjunto de superficies a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada superficie |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da promedios de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da promedios de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Surface | item | Media aritmética (promedio) de todas las superficies de entrada |

## Transform

### Average Transform (AvrTran)

Calcula el promedio aritmético de un conjunto de transformaciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `X` | Transform | lista | Conjunto de transformaciones a promediar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Transform | item | Media aritmética (promedio) de todas las transformaciones de entrada |

### Mass Transform (MTran)

Crea una sola transformación masiva combinando un conjunto de transformaciones, como el componente Compound de Grasshopper pero con acceso a los resultados parciales (cada paso de la transformación masiva).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `X` | Transform | lista | Conjunto de transformaciones a combinar en una transformación masiva (salidas X de componentes que transforman, como Move, Scale, Rotate, etc.) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mass Transform | `mX` | Transform | item | Transformación masiva resultante |
| Partial Transforms | `pX` | Transform | lista | Transformaciones parciales (pasos) de la transformación masiva |

### Mirror Combine Transforms (MirComTrans)

Refleja un conjunto de transformaciones desde su final o su inicio y lo combina con el conjunto original.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `X` | Transform | lista | Conjunto de transformaciones a reflejar y combinar |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = final del conjunto, True = inicio del conjunto) |
| Join | `J` | Boolean | item | Une el conjunto de transformaciones reflejado y combinado (quita la transformación duplicada al medio del conjunto) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirrored | `M` | Transform | lista | Conjunto de transformaciones reflejado y combinado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |

### Mirror Cut Transforms (MirCutTrans)

Corta un conjunto de transformaciones en un índice, refleja el lado conservado del corte respecto de ese índice y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `X` | Transform | lista | Conjunto de transformaciones a cortar y reflejar |
| Mirror Index | `Mi` | Integer | item | Índice respecto del cual se refleja el lado conservado del corte. Un índice negativo invierte el conjunto y quita desde arriba. |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = reflejar después del índice, True = reflejar antes del índice) |
| Join | `J` | Boolean | item | Une el conjunto de transformaciones cortado y reflejado (quita la transformación duplicada al medio del conjunto) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Transform | lista | Conjunto de transformaciones cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Intersected | `I` | Boolean | item | True si el índice de reflejo intersectó el conjunto de transformaciones, False si no lo intersectó |

### Morph To Twisted Box (Morph2Tbox)

Deforma (morph) geometrías desde cajas de referencia hacia cajas torcidas objetivo. (*Solo Rhino 6; en Rhino 5 usa el componente Box Morph de Grasshopper.) [Multihilo]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometries | `G` | Geometry | lista | Geometrías a deformar |
| References | `R` | Box | lista | Cajas de referencia desde las que deformar (normalmente la caja contenedora de las geometrías) |
| Targets | `TB` | Twisted Box | lista | Cajas torcidas objetivo hacia las que deformar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Morphed | `M` | Geometry | lista | Geometrías resultantes deformadas a las cajas torcidas |

### Move To Point (Move2Pt)

Mueve (traslada) un objeto de un punto a otro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría a mover (trasladar) |
| Point A | `A` | Point | item | Punto desde el que mover |
| Point B | `B` | Point | item | Punto hacia el que mover |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Moved | `M` | Geometry | item | Geometría movida (trasladada) resultante |
| Vector | `V` | Vector | item | Vector de movimiento (traslación) |
| Transform | `X` | Transform | item | Datos de la transformación |

### Recursive Transform (ReTrans)

Transforma geometría de forma recursiva para obtener una secuencia autorreferente de geometría transformada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a transformar de forma recursiva |
| Transform | `X` | Transform | item | Transformación que se aplica a la geometría en cada paso recursivo (salidas X de componentes que transforman, como Move, Scale, Rotate, etc.). Usa el componente Mass Transform de Pufferfish o el componente Compound de Grasshopper para combinar varias transformaciones en una sola y entregarla aquí, así varias transformaciones pueden afectar la geometría. (*Ten especial cuidado con transformaciones como el escalado: escalar recursivamente en muchos pasos puede generar rápidamente geometría enorme o diminuta y congelar Grasshopper) |
| Steps | `N` | Integer | item | Cantidad de pasos recursivos de transformación |
| Last | `L` | Boolean | item | Si es True, solo se calcula y entrega el último paso de la transformación recursiva. Si es False, se calcula y entrega cada paso. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transformed | `T` | Geometry | lista | Geometría resultante transformada de forma recursiva |

### Rotate Euler (RotEuler)

Rota un objeto según tres ejes de plano y tres ángulos en grados; cada eje se obtiene del plano anterior.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría a rotar |
| Plane | `Pl` | Plane | item | Plano base inicial desde el que parte la rotación |
| Axis 1 | `A¹` | Integer | item | El primer eje de plano alrededor del cual rotar, obtenido del plano base inicial: 0 = {x} del plano base inicial, 1 = {y} del plano base inicial, 2 = {z} del plano base inicial |
| Axis 2 | `A²` | Integer | item | El segundo eje de plano alrededor del cual rotar, obtenido del plano rotado alrededor del eje 1: 0 = {x}, 1 = {y}, 2 = {z} de ese plano |
| Axis 3 | `A³` | Integer | item | El tercer eje de plano alrededor del cual rotar, obtenido del plano rotado alrededor del eje 2: 0 = {x}, 1 = {y}, 2 = {z} de ese plano |
| Degrees 1 | `D¹` | Number | item | El ángulo en grados a rotar alrededor del eje 1 (α) |
| Degrees 2 | `D²` | Number | item | El ángulo en grados a rotar alrededor del eje 2 (β) |
| Degrees 3 | `D³` | Number | item | El ángulo en grados a rotar alrededor del eje 3 (γ) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rotated | `R` | Geometry | item | Geometría rotada resultante |
| Plane 1 | `Pl¹` | Plane | item | El plano después de la rotación alrededor del eje 1 (el eje 1 es un eje del plano base inicial) |
| Plane 2 | `Pl²` | Plane | item | El plano después de la rotación alrededor del eje 2 (el eje 2 es un eje del plano 1) |
| Plane 3 | `Pl³` | Plane | item | El plano después de la rotación alrededor del eje 3 (el eje 3 es un eje del plano 2) |
| Transform | `X` | Transform | item | Datos de la transformación |

### Rotate Quaternion (RotQuat)

Rota un objeto de un plano a otro según un factor de rotación, usando rotación por cuaterniones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría a rotar |
| Plane 1 | `Pl¹` | Plane | item | Plano desde el que parte la rotación |
| Plane 2 | `Pl²` | Plane | item | Plano en el que termina la rotación |
| Factor | `F` | Number | item | Factor de rotación (0.0 = plano Pl¹, 1.0 = plano Pl²) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rotated | `R` | Geometry | item | Geometría rotada resultante |
| Plane | `Pl` | Plane | item | El plano cuaternión en el factor de rotación |
| Axis | `A` | Vector | item | El vector del eje de rotación del cuaternión |
| Degree | `D` | Number | item | El ángulo de rotación del cuaternión, en grados |
| Transform | `X` | Transform | item | Datos de la transformación |

### Rotate World (RotWorld)

Rota un objeto según tres ejes de plano y tres ángulos en grados; cada eje se obtiene de los ejes del plano base inicial.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry *(opcional)* | `G` | Geometry | item | Geometría a rotar |
| Plane | `Pl` | Plane | item | Plano base inicial que define los ejes {x}, {y} y {z} |
| Axis 1 | `A¹` | Integer | item | El primer eje de plano alrededor del cual rotar, obtenido del plano base inicial: 0 = {x} del plano base inicial, 1 = {y} del plano base inicial, 2 = {z} del plano base inicial |
| Axis 2 | `A²` | Integer | item | El segundo eje de plano alrededor del cual rotar, obtenido del plano base inicial: 0 = {x}, 1 = {y}, 2 = {z} del plano base inicial |
| Axis 3 | `A³` | Integer | item | El tercer eje de plano alrededor del cual rotar, obtenido del plano base inicial: 0 = {x}, 1 = {y}, 2 = {z} del plano base inicial |
| Degrees 1 | `D¹` | Number | item | El ángulo en grados a rotar alrededor del eje 1 |
| Degrees 2 | `D²` | Number | item | El ángulo en grados a rotar alrededor del eje 2 |
| Degrees 3 | `D³` | Number | item | El ángulo en grados a rotar alrededor del eje 3 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rotated | `R` | Geometry | item | Geometría rotada resultante |
| Plane 1 | `Pl¹` | Plane | item | El plano después de la rotación alrededor del eje 1 (el eje 1 es un eje del plano base inicial) |
| Plane 2 | `Pl²` | Plane | item | El plano después de la rotación alrededor del eje 2 (el eje 2 es un eje del plano base inicial) |
| Plane 3 | `Pl³` | Plane | item | El plano después de la rotación alrededor del eje 3 (el eje 3 es un eje del plano base inicial) |
| Transform | `X` | Transform | item | Datos de la transformación |

### Scale To Area (Scale2Area)

Escala geometría a un área dada, con factores de proporción {x}, {y} y {z}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a escalar |
| Plane | `Pl` | Plane | item | Plano base para el centro y la orientación del escalado |
| Area | `A` | Number | item | Área a la que escalar la geometría |
| Factor X | `x` | Number | item | Factor de escala proporcional en la dirección {x} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |
| Factor Y | `y` | Number | item | Factor de escala proporcional en la dirección {y} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |
| Factor Z | `z` | Number | item | Factor de escala proporcional en la dirección {z} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Scaled | `S` | Geometry | item | Geometría resultante escalada al área |
| Transform | `X` | Transform | item | Datos de la transformación |

### Scale To Length (Scale2Len)

Escala una curva a una longitud dada, con factores de proporción {x}, {y} y {z}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a escalar |
| Plane | `Pl` | Plane | item | Plano base para el centro y la orientación del escalado |
| Length | `L` | Number | item | Longitud a la que escalar la curva |
| Factor X | `x` | Number | item | Factor de escala proporcional en la dirección {x} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |
| Factor Y | `y` | Number | item | Factor de escala proporcional en la dirección {y} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |
| Factor Z | `z` | Number | item | Factor de escala proporcional en la dirección {z} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Scaled | `S` | Geometry | item | Curva resultante escalada a la longitud |
| Transform | `X` | Transform | item | Datos de la transformación |

### Scale To Volume (Scale2Vol)

Escala geometría a un volumen dado, con factores de proporción {x}, {y} y {z}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a escalar |
| Plane | `Pl` | Plane | item | Plano base para el centro y la orientación del escalado |
| Volume | `V` | Number | item | Volumen al que escalar la geometría |
| Factor X | `x` | Number | item | Factor de escala proporcional en la dirección {x} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |
| Factor Y | `y` | Number | item | Factor de escala proporcional en la dirección {y} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |
| Factor Z | `Z` | Number | item | Factor de escala proporcional en la dirección {z} del plano (usa el mismo valor para {x}, {y} y {z} para un escalado uniforme) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Scaled | `S` | Geometry | item | Geometría resultante escalada al volumen |
| Transform | `X` | Transform | item | Datos de la transformación |

### Slide Within Transform (SlideInTran)

Se desliza entre el inicio y el final de una transformación para obtener un estado de transformación intermedio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transform | `X` | Transform | item | Transformación dentro de la cual deslizarse |
| Factor | `F` | Number | item | Factor de deslizamiento (0.0 = inicio de la transformación, 1.0 = final) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Slid | `S` | Transform | item | Estado de transformación resultante dentro de la transformación |

### Transform Twisted Box (TranTBox)

Transforma una caja torcida (porque las cajas torcidas no funcionan con los componentes de transformación normales como Move, Scale, Rotate, etc.).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida a transformar |
| Transform | `X` | Transform | item | Transformación que se aplica a la caja torcida (salidas X de componentes que transforman, como Move, Scale, Rotate, etc.) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transformed | `T` | Twisted Box | item | Caja torcida transformada resultante |

### Tween Consecutive Transforms (TwnConTrans)

Interpola (tween) consecutivamente entre un conjunto de transformaciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `X` | Transform | lista | Conjunto de transformaciones entre las que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = transformación en X, 1.0 = transformación en X +1) |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Transform | lista | Transformaciones interpoladas resultantes |

### Tween Through Transforms (TwnThruTrans)

Interpola (tween) a través de un conjunto de transformaciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `X` | Transform | lista | Conjunto de transformaciones a través de las cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = transformación al inicio de X, 1.0 = transformación al final de X), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = transformación en el índice 0, número de índice de la última = transformación en el último índice). El rango del factor de una transformación a la siguiente es: el número de índice de una transformación = la transformación en ese índice, el número de índice de la siguiente = la siguiente de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una transformación a medio camino entre la del índice 2 y la del índice 3. |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Transform | item | Transformación interpolada resultante |

### Tween Two Transforms (Twn2Trans)

Interpola (tween) entre dos transformaciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transform A | `A` | Transform | item | Transformación desde la que interpolar |
| Transform B | `B` | Transform | item | Transformación hacia la que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Transform A, 1.0 = Transform B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Transform | item | Transformación interpolada resultante |

### Weighted Average Transform (WavTran)

Calcula el promedio aritmético ponderado de un conjunto de transformaciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Transforms | `X` | Transform | lista | Conjunto de transformaciones a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada transformación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Transform | item | Media aritmética (promedio) de todas las transformaciones de entrada |

### Zeroed Transform (ZeroTran)

Entrega una transformación en cero, que representa ninguna transformación o el estado previo a cualquier transformación; también se llama matriz de transformación identidad.

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Zeroed Transform | `ØX` | Transform | item | Una transformación en cero |

## Twisted Box

### 2Pt Twisted Box (2PtTBox)

Crea una caja torcida definida por 2 puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primera esquina |
| Point B | `B` | Point | item | Segunda esquina |
| Plane | `Pl` | Plane | item | Plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida 2Pt resultante |

### Average Twisted Box (AvrTBox)

Calcula el promedio aritmético de un conjunto de cajas torcidas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a promediar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Twisted Box | item | Media aritmética (promedio) de todas las cajas torcidas de entrada |

### Center Twisted Box (CenTBox)

Crea una caja torcida centrada en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base |
| Size X | `X` | Number | item | Tamaño de la caja torcida en la dirección {x} |
| Size Y | `Y` | Number | item | Tamaño de la caja torcida en la dirección {y} |
| Size Z | `Z` | Number | item | Tamaño de la caja torcida en la dirección {z} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida centrada resultante |

### Construct Twisted Box (CoTBox)

Construye una caja torcida a partir de un conjunto de 8 puntos de esquina.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corners | `C` | Point | lista | Conjunto de 8 puntos de esquina que forman una caja torcida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida resultante que une el conjunto de 8 puntos de esquina |

### Deconstruct Twisted Box (DeTBox)

Descompone una caja torcida en sus 8 puntos de esquina, 12 líneas de arista o 6 polilíneas de cara.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida a descomponer |
| Deconstruct Type | `T` | Integer | item | Determina qué partes de la caja torcida obtener: 0 = puntos de esquina, 1 = líneas de arista, 2 = polilíneas de cara |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Deconstructed | `D` | Generic Data | lista | Las partes seleccionadas de la caja torcida descompuesta |

### Deform Twisted Box (DeformTBox)

Deforma una caja torcida moviendo sus puntos de esquina con vectores de movimiento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida a deformar |
| Corners *(opcional)* | `C` | Point | lista | Puntos de esquina a deformar (si los puntos no son exactamente esquinas, se deforman las esquinas más cercanas) |
| Indices *(opcional)* | `i` | Integer | lista | Índices opcionales de las esquinas a deformar en vez de puntos (reemplazan a los puntos si también se entregan) |
| Motions | `M` | Vector | lista | Vector de movimiento para cada punto de esquina a deformar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Deformed | `D` | Twisted Box | item | Caja torcida deformada resultante |
| Index | `i` | Integer | lista | Índice de cada punto de esquina que se deformó |

### Domain Twisted Box (DomTBox)

Crea una caja torcida definida por un plano base y dominios de tamaño.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base |
| Domain X | `X` | Domain | item | Dominio de la caja torcida en la dirección {x} |
| Domain Y | `Y` | Domain | item | Dominio de la caja torcida en la dirección {y} |
| Domain Z | `Z` | Domain | item | Dominio de la caja torcida en la dirección {z} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida por dominios resultante |

### Evaluate Twisted Box (EvalTBox)

Ubica un punto dentro o sobre una caja torcida, evaluado en el espacio normalizado {uvw}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida a evaluar |
| Parameter U | `u` | Number | item | Parámetro {u} (los valores entre 0.0 y 1.0 están dentro de la caja torcida) |
| Parameter V | `v` | Number | item | Parámetro {v} (los valores entre 0.0 y 1.0 están dentro de la caja torcida) |
| Parameter W | `w` | Number | item | Parámetro {w} (los valores entre 0.0 y 1.0 están dentro de la caja torcida) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Evaluation | `E` | Point | item | Punto evaluado en la coordenada {uvw} |
| Result Boolean | `R` | Boolean | item | True si el punto está dentro o sobre la caja torcida, False si está fuera |

### Mesh Boolean Twisted Boxes (MshBoolTBoxs)

Recorta (quita) un conjunto de cajas torcidas mediante una intersección o diferencia booleana con una o varias mallas cerradas. Más rápido pero menos preciso que el componente Boolean Twisted Boxes With Polysurface. [Multihilo]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a recortar |
| Meshes | `M` | Mesh | lista | Malla o mallas cerradas con las que recortar |
| Boolean Type | `B` | Boolean | item | True para intersección booleana (quita las cajas torcidas fuera de la malla o mallas). False para diferencia booleana (quita las cajas torcidas dentro de la malla o mallas) |
| Keep Type | `K` | Integer | item | Determina cuánto del conjunto recortado se conserva: 0 = completa (se conserva si la caja está completamente del lado que se conserva de la malla); 1 = mitad (se conserva si está al menos a mitad de camino de ese lado; la más rápida); 2 = parcial (se conserva si está al menos en parte de ese lado) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Twisted Box | lista | Conjunto de cajas torcidas recortado resultante |
| Kept Indicies | `i` | Integer | lista | Índices, en el conjunto de entrada, de las cajas torcidas que quedaron después del recorte |
| Intersected | `I` | Boolean | item | True si el conjunto de cajas torcidas se recortó, False si no |

### Mesh Trim Twisted Boxes (MshTrimTBoxs)

Recorta (quita) las partes de un conjunto de cajas torcidas que están a un lado de una malla. [Multihilo]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a recortar |
| Mesh | `M` | Mesh | item | Malla con la que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |
| Keep Type | `K` | Integer | item | Determina cuánto del conjunto recortado se conserva: 0 = completa (se conserva si la caja está completamente del lado que se conserva de la malla); 1 = mitad (se conserva si está al menos a mitad de camino de ese lado; la más rápida); 2 = parcial (se conserva si está al menos en parte de ese lado) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Twisted Box | lista | Conjunto de cajas torcidas recortado resultante |
| Kept Indicies | `i` | Integer | lista | Índices, en el conjunto de entrada, de las cajas torcidas que quedaron después del recorte |
| Intersected | `I` | Boolean | item | True si la malla recortó el conjunto de cajas torcidas, False si no |

### Plane Trim Twisted Boxes (PlnTrimTBoxs)

Recorta (quita) las partes de un conjunto de cajas torcidas que están a un lado de un plano. [Multihilo]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a recortar |
| Plane | `Pl` | Plane | item | Plano con el que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |
| Keep Type | `K` | Integer | item | Determina cuánto del conjunto recortado se conserva: 0 = completa (se conserva si la caja está completamente del lado que se conserva del plano); 1 = mitad (se conserva si está al menos a mitad de camino de ese lado; la más rápida); 2 = parcial (se conserva si está al menos en parte de ese lado) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Twisted Box | lista | Conjunto de cajas torcidas recortado resultante |
| Kept Indicies | `i` | Integer | lista | Índices, en el conjunto de entrada, de las cajas torcidas que quedaron después del recorte |
| Intersected | `I` | Boolean | item | True si el plano recortó el conjunto de cajas torcidas, False si no |

### Polysurface Boolean Twisted Boxes (PsrfBoolTBoxs)

Recorta (quita) un conjunto de cajas torcidas mediante una intersección o diferencia booleana con una o varias polisuperficies cerradas (Breps). Más lento pero más preciso que el componente Boolean Twisted Boxes With Meshes. [Multihilo]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a recortar |
| Polysurfaces | `Ps` | Brep | lista | Polisuperficie(s) cerrada(s) (Breps) con la(s) que recortar |
| Boolean Type | `B` | Boolean | item | True para intersección booleana (quita las cajas torcidas fuera de la(s) polisuperficie(s)). False para diferencia booleana (quita las cajas torcidas dentro de la(s) polisuperficie(s)) |
| Keep Type | `K` | Integer | item | Determina cuánto del conjunto recortado se conserva: 0 = completa (se conserva si la caja está completamente del lado que se conserva de la polisuperficie); 1 = mitad (se conserva si está al menos a mitad de camino de ese lado; la más rápida); 2 = parcial (se conserva si está al menos en parte de ese lado) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Twisted Box | lista | Conjunto de cajas torcidas recortado resultante |
| Kept Indicies | `i` | Integer | lista | Índices, en el conjunto de entrada, de las cajas torcidas que quedaron después del recorte |
| Intersected | `I` | Boolean | item | True si el conjunto de cajas torcidas se recortó, False si no |

### Reference Twisted Box (RefTBox)

Crea una caja torcida a partir de una polisuperficie (Brep) tipo caja referenciada desde Rhino, con 6 caras y 8 esquinas. Funciona mejor con polisuperficies creadas en Rhino con el comando 'Box' y referenciadas en Grasshopper, porque sigue ese orden de vértices de esquina. Para otras cajas, prueba el parámetro Twisted Box o el componente Twisted Box normal de Grasshopper.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polysurface | `Ps` | Brep | item | Polisuperficie (Brep) tipo caja, idealmente referenciada desde Rhino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida de referencia resultante |

### Subdivide Twisted Box (SubDivTBox)

Subdivide de forma recursiva una caja torcida en cajas torcidas más pequeñas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida a subdividir |
| Steps | `N` | Integer | item | Cantidad de pasos recursivos de subdivisión. ADVERTENCIA: la recursión crea cajas torcidas nuevas dentro de cada caja de forma exponencial. Más de 3 pasos puede crear muchísimas cajas. Guarda tu trabajo por si el computador se congela con valores altos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Subdivided | `S` | Twisted Box | lista | Cajas torcidas de subdivisión resultantes |

### Surface Trim Twisted Boxes (SrfTrimTBoxs)

Recorta (quita) las partes de un conjunto de cajas torcidas que están a un lado de una superficie. [Multihilo]

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a recortar |
| Surface | `S` | Surface | item | Superficie con la que recortar |
| Flip | `F` | Boolean | item | Invierte la dirección del recorte |
| Keep Type | `K` | Integer | item | Determina cuánto del conjunto recortado se conserva: 0 = completa (se conserva si la caja está completamente del lado que se conserva de la superficie); 1 = mitad (se conserva si está al menos a mitad de camino de ese lado; la más rápida); 2 = parcial (se conserva si está al menos en parte de ese lado) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trimmed | `T` | Twisted Box | lista | Conjunto de cajas torcidas recortado resultante |
| Kept Indicies | `i` | Integer | lista | Índices, en el conjunto de entrada, de las cajas torcidas que quedaron después del recorte |
| Intersected | `I` | Boolean | item | True si la superficie recortó el conjunto de cajas torcidas, False si no |

### Thicken Twisted Box (ThickTBox)

Da espesor a una caja torcida con capas de cajas torcidas, según parámetros que dividen el dominio del espesor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida a la que dar espesor |
| Thickness | `T` | Number | item | Factor de espesor (0.0 = sin espesor, 1.0 = espesor completo) |
| Parameters W | `w` | Number | lista | Parámetros de división de las capas a lo largo del dominio {w} del espesor (0.0 = caja torcida de entrada, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Hollow | `H` | Boolean | item | Quita la caja torcida central |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Thickened | `T` | Twisted Box | lista | Cajas torcidas de espesor resultantes |

### Tween Consecutive Twisted Boxes (TwnConTBoxs)

Interpola (tween) consecutivamente entre un conjunto de cajas torcidas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas entre las que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = caja torcida en TB, 1.0 = caja torcida en TB +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de cajas torcidas de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Twisted Box | lista | Cajas torcidas interpoladas resultantes |

### Tween Through Twisted Boxes (TwnThruTBoxs)

Interpola (tween) a través de un conjunto de cajas torcidas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a través de las cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = caja torcida al inicio de TB, 1.0 = caja torcida al final de TB), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = caja torcida en el índice 0, número de índice de la última = caja torcida en el último índice). El rango del factor de una caja torcida a la siguiente es: el número de índice de una caja = la caja en ese índice, el número de índice de la siguiente = la siguiente caja de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da una caja torcida a medio camino entre la del índice 2 y la del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de cajas torcidas de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de cajas torcidas de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Twisted Box | lista | Caja torcida interpolada resultante |

### Tween Two Twisted Boxes (Twn2TBoxs)

Interpola (tween) entre dos cajas torcidas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box A | `A` | Twisted Box | item | Caja torcida desde la que interpolar |
| Twisted Box B | `B` | Twisted Box | item | Caja torcida hacia la que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Twisted Box A, 1.0 = Twisted Box B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Twisted Box | item | Caja torcida interpolada resultante |

### Twisted Box Array (TBoxArray)

Crea un arreglo en capas de cajas torcidas conectadas dentro de una caja, según parámetros que dividen su dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja dentro de la cual crear el arreglo de cajas torcidas |
| Parameters X | `x` | Number | lista | Parámetros de división a lo largo del dominio {x} de la caja (0.0 = inicio {x}, 1.0 = final {x}). Para mejores resultados, los parámetros {x} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters Y | `y` | Number | lista | Parámetros de división a lo largo del dominio {y} de la caja (0.0 = inicio {y}, 1.0 = final {y}). Para mejores resultados, los parámetros {y} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters Z | `z` | Number | lista | Parámetros de división a lo largo del dominio {z} de la caja (0.0 = inicio {z}, 1.0 = final {z}). Para mejores resultados, los parámetros {z} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante |

### Twisted Box Centers (TBoxCents)

Busca el punto central (promedio) de los puntos de esquina, líneas de arista o polilíneas de cara de una caja torcida.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida de la que buscar el punto central (promedio) |
| Center Type | `T` | Integer | item | Determina de qué partes de la caja torcida obtener el punto central (promedio): 0 = puntos de esquina, 1 = líneas de arista, 2 = polilíneas de cara |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center | `C` | Point | lista | El punto central (promedio) de las partes seleccionadas de la caja torcida. Usa el componente Twisted Box Volume de Pufferfish para obtener el centro volumétrico |

### Twisted Box Consecutive Curves (TBoxConCrvs)

Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre curvas, según un espesor y parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas entre las que crear el arreglo de cajas torcidas |
| Thickness | `T` | Number | item | Espesor total del arreglo de cajas torcidas, con offset desde las curvas |
| Parameters U | `u` | Number | lista | Parámetros de división del dominio {u} entre cada curva ({u} 0.0 = curva en C, 1.0 = curva en C +1). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo de los dominios {v} de las curvas ({v} 0.0 = inicios de las curvas, 1.0 = finales). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división a lo largo del dominio {w} del espesor ({w} 0.0 = curvas, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {v} se pondera según la curvatura de las curvas de entrada |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {u} continúe desde el final de vuelta al inicio como un circuito cerrado |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {u}: 0 = recto, 1 = normal, 2 = ajustado, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da cajas torcidas de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da cajas torcidas de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante, consecutivo entre las curvas |

### Twisted Box Consecutive Meshes (TBoxConMshs)

Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre un conjunto de mallas a partir de sus caras; funciona con caras cuadrangulares y triangulares. Las mallas deben tener la misma topología.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas entre las que crear el arreglo de cajas torcidas |
| Parameters W | `w` | Number | lista | Parámetros de división del dominio {w} entre cada malla ({w} 0.0 = malla en M, 1.0 = malla en M +1). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {w} se pondera según el conjunto de mallas de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {w} continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación {w}; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {w}: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante, consecutivo entre las mallas |

### Twisted Box Consecutive Surfaces (TBoxConSrfs)

Crea un arreglo en capas de cajas torcidas conectadas, consecutivamente entre un conjunto de superficies, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Conjunto de superficies entre las que crear el arreglo de cajas torcidas |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo de los dominios {u} de las superficies ({u} 0.0 = inicios de las superficies, 1.0 = finales). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo de los dominios {v} de las superficies ({v} 0.0 = inicios de las superficies, 1.0 = finales). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división del dominio {w} entre cada superficie ({w} 0.0 = superficie en S, 1.0 = superficie en S +1). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {w} se pondera según el conjunto de superficies de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {w} continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación {w}; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {w}: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da cajas torcidas de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da cajas torcidas de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante, consecutivo entre las superficies |

### Twisted Box Corners (TBox Corners)

Obtiene las 8 esquinas de una caja torcida.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida de la que obtener las esquinas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Point | item | Primera esquina (0,0,0) |
| Corner B | `B` | Point | item | Segunda esquina (1,0,0) |
| Corner C | `C` | Point | item | Tercera esquina (1,1,0) |
| Corner D | `D` | Point | item | Cuarta esquina (0,1,0) |
| Corner E | `E` | Point | item | Quinta esquina (0,0,1) |
| Corner F | `F` | Point | item | Sexta esquina (1,0,1) |
| Corner G | `G` | Point | item | Séptima esquina (1,1,1) |
| Corner H | `H` | Point | item | Última esquina (0,1,1) |

### Twisted Box Curve (TBoxCrv)

Crea cajas torcidas conectadas a lo largo de una curva, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual crear las cajas torcidas |
| Size X | `X` | Domain | item | Tamaño de dominio de la dimensión {x} de la curva de cajas torcidas |
| Size Y | `Y` | Domain | item | Tamaño de dominio de la dimensión {y} de la curva de cajas torcidas |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio {t} de la curva (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de la curva de entrada |
| Rotation 1 | `R¹` | Number | item | Rotación de la curva de cajas torcidas alrededor de los centros de las cajas, en grados |
| Rotation 2 | `R²` | Number | item | Rotación de la curva de cajas torcidas alrededor de la curva, en grados (si la curva de cajas está centrada en la curva, el efecto se ve igual que la rotación 1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Cajas torcidas resultantes a lo largo de la curva |

### Twisted Box Curve Variable (TBoxCrvVar)

Crea cajas torcidas conectadas a lo largo de una curva, según parámetros que dividen el dominio, con tamaños y rotaciones variables.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual crear las cajas torcidas |
| Sizes X | `X` | Domain | lista | Una lista de tamaños de dominio para la dimensión {x} de la curva de cajas torcidas en cada parámetro de división {t} |
| Sizes Y | `Y` | Domain | lista | Una lista de tamaños de dominio para la dimensión {y} de la curva de cajas torcidas en cada parámetro de división {t} |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio de la curva (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de la curva de entrada |
| Rotations 1 | `R¹` | Number | lista | Una lista de rotaciones de la curva de cajas torcidas alrededor de los centros de las cajas en cada parámetro de división {t}, en grados |
| Rotations 2 | `R¹` | Number | lista | Una lista de rotaciones de la curva de cajas torcidas alrededor de la curva en cada parámetro de división {t}, en grados (si la curva de cajas está centrada en la curva, el efecto se ve igual que la rotación 1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Cajas torcidas resultantes a lo largo de la curva |

### Twisted Box Extrude (TBoxExtr)

Crea cajas torcidas conectadas a partir de una curva o superficie de perfil, a lo largo de un vector, una curva o hacia un punto, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Profile | `P` | Curve | item | Curva o superficie de perfil a extruir como cajas torcidas. Idealmente el perfil debe ser un cuadrilátero (polilínea de 4 lados y 4 esquinas); si no lo es, se convierte. No necesita ser plano ni cerrado. Se aceptan triángulos. |
| Direction | `D` | Generic Data | item | Vector, curva o punto de dirección de extrusión. Entrega un vector para extruir a lo largo de un vector, una curva para extruir a lo largo de una curva o un punto para extruir hacia un punto |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio {t} de la extrusión (0.0 = inicio de la extrusión, 1.0 = final). Para mejores resultados, los parámetros deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True y se usa una curva como dirección de extrusión, la distribución de los parámetros {t} se pondera según la curvatura de esa curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Cajas torcidas extruidas resultantes |

### Twisted Box Loft (TBoxLoft)

Crea cajas torcidas entre curvas o superficies de sección

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sections | `S` | Curve | lista | Curvas o superficies de sección entre las que crear cajas torcidas. Idealmente las secciones deben ser cuadriláteros (polilíneas de 4 lados y 4 esquinas); si no lo son, se convierten. No necesitan ser planas ni cerradas. Se aceptan triángulos. |
| Closed | `C` | Boolean | item | Loft cerrado: si es True, la última curva de sección hace loft de vuelta a la primera como caja torcida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Cajas torcidas con loft resultantes |

### Twisted Box Mesh (TBoxMsh)

Crea un arreglo en capas de cajas torcidas conectadas sobre una malla, a partir de sus caras y un espesor dividido por un dominio de parámetros; funciona con caras cuadrangulares y triangulares.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla sobre la que crear el arreglo de cajas torcidas |
| Thickness | `T` | Number | item | Espesor total del arreglo de cajas torcidas desde la malla, con offset desde las caras |
| Parameters W | `w` | Number | lista | Parámetros de división a lo largo del dominio {w} del espesor ({w} 0.0 = malla, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante sobre la malla |

### Twisted Box Pipe (TBoxPipe)

Crea cajas torcidas conectadas por el interior de una superficie tipo tubo, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie tipo tubo por cuyo interior crear las cajas torcidas |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie tipo tubo (0.0 = inicio {u}, 1.0 = final {u}). Para mejores resultados, los parámetros deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameter V1 | `v¹` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la primera y la quinta esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1 y ser el menor de los parámetros {v} |
| Parameter V2 | `v²` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la segunda y la sexta esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1, ser mayor que {v1} y menor que {v3} |
| Parameter V3 | `v³` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la tercera y la séptima esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1, ser mayor que {v2} y menor que {v4} |
| Parameter V4 | `v⁴` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la cuarta y la octava esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1 y ser el mayor de los parámetros {v} |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {u} se pondera según la curvatura de la superficie tipo tubo de entrada |
| Flip | `F` | Boolean | item | Invierte el flujo de las cajas torcidas si no van en la dirección correcta por el interior de la superficie tipo tubo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Cajas torcidas resultantes por el interior de la superficie tipo tubo |

### Twisted Box Pipe Variable (TBoxPipeVar)

Crea cajas torcidas conectadas por el interior de una superficie tipo tubo, con un conjunto separado de parámetros de división del dominio {u} para cada parámetro {v}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie tipo tubo por cuyo interior crear las cajas torcidas |
| Parameters U1 | `u¹` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie tipo tubo en el parámetro {v1} (0.0 = inicio {u}, 1.0 = final {u}). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {u} |
| Parameters U2 | `u²` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie tipo tubo en el parámetro {v2} (0.0 = inicio {u}, 1.0 = final {u}). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {u} |
| Parameters U3 | `u³` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie tipo tubo en el parámetro {v3} (0.0 = inicio {u}, 1.0 = final {u}). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {u} |
| Parameters U4 | `u⁴` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie tipo tubo en el parámetro {v4} (0.0 = inicio {u}, 1.0 = final {u}). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {u} |
| Parameter V1 | `v¹` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la primera y la quinta esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1 y ser el menor de los parámetros {v} |
| Parameter V2 | `v²` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la segunda y la sexta esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1, ser mayor que {v1} y menor que {v3} |
| Parameter V3 | `v³` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la tercera y la séptima esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1, ser mayor que {v2} y menor que {v4} |
| Parameter V4 | `v⁴` | Number | item | Parámetro de división a lo largo del dominio {v} de la superficie tipo tubo donde están la cuarta y la octava esquina de las cajas torcidas (0.0 = inicio {v}, 1.0 = final {v}). Para mejores resultados, debe estar entre 0 y 1 y ser el mayor de los parámetros {v} |
| Weighted | `W` | Boolean | item | Si es True, las distribuciones de los parámetros {u} se ponderan según la curvatura de la superficie tipo tubo de entrada |
| Flip | `F` | Boolean | item | Invierte el flujo de las cajas torcidas si no van en la dirección correcta por el interior de la superficie tipo tubo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Cajas torcidas resultantes por el interior de la superficie tipo tubo |

### Twisted Box Strip (TBoxStrip)

Crea cajas torcidas conectadas a lo largo de dos curvas de riel, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rail 1 | `R¹` | Curve | item | Curva de riel donde están la primera y la cuarta esquina de las cajas torcidas |
| Rail 2 | `R²` | Curve | item | Curva de riel donde están la segunda y la tercera esquina de las cajas torcidas |
| Thickness | `T` | Number | item | Espesor de la franja de cajas torcidas, con offset desde las curvas de riel |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio {t} de cada curva de riel (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de las curvas de riel de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Franja de cajas torcidas resultante |

### Twisted Box Strip Variable (TTBoxStripVar)

Crea cajas torcidas conectadas a lo largo de dos curvas de riel, con un conjunto separado de parámetros de división del dominio para cada riel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rail 1 | `R¹` | Curve | item | Curva de riel donde están la primera y la cuarta esquina de las cajas torcidas |
| Rail 2 | `R²` | Curve | item | Curva de riel donde están la segunda y la tercera esquina de las cajas torcidas |
| Thickness | `T` | Number | item | Espesor de la franja de cajas torcidas, con offset desde las curvas de riel |
| Parameters T1 | `t¹` | Number | lista | Parámetros de división a lo largo del dominio {t} del riel uno (0.0 = inicio de Rail 1, 1.0 = final de Rail 1). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que la lista de parámetros t¹ |
| Parameters T2 | `t²` | Number | lista | Parámetros de división a lo largo del dominio {t} del riel dos (0.0 = inicio de Rail 2, 1.0 = final de Rail 2). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que la lista de parámetros t² |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de las curvas de riel de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Franja de cajas torcidas resultante |

### Twisted Box Strips (TBoxStrips)

Crea cajas torcidas conectadas a lo largo de un conjunto de curvas de riel, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rails | `R` | Curve | lista | Conjunto de curvas de riel entre las que fluyen las cajas torcidas |
| Thickness | `T` | Number | item | Espesor de las franjas de cajas torcidas, con offset desde las curvas de riel |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio {t} de cada curva de riel (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de las curvas de riel de entrada |
| Closed | `C` | Boolean | item | Franjas cerradas: si es True, la última curva de riel se conecta de vuelta con la primera mediante cajas torcidas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Franja de cajas torcidas resultante |

### Twisted Box Surface (TBoxSrf)

Crea un arreglo en capas de cajas torcidas conectadas sobre una superficie, según un espesor y parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie sobre la que crear el arreglo de cajas torcidas |
| Thickness | `T` | Number | item | Espesor total del arreglo de cajas torcidas, con offset desde la superficie |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la superficie ({u} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo del dominio {v} de la superficie ({v} 0.0 = inicio de la superficie, 1.0 = final). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división a lo largo del dominio {w} del espesor ({w} 0.0 = superficie, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da cajas torcidas de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da cajas torcidas de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante sobre la superficie |

### Twisted Box Sweep (TBoxSweep)

Crea cajas torcidas conectadas a lo largo de cuatro curvas de riel, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rail 1 | `R¹` | Curve | item | Curva de riel donde están la primera y la cuarta esquina de las cajas torcidas |
| Rail 2 | `R²` | Curve | item | Curva de riel donde están la segunda y la tercera esquina de las cajas torcidas |
| Rail 3 | `R³` | Curve | item | Curva de riel donde están la sexta y la séptima esquina de las cajas torcidas |
| Rail 3 | `R⁴` | Curve | item | Curva de riel donde están la quinta y la octava esquina de las cajas torcidas |
| Parameters T | `t` | Number | lista | Parámetros de división a lo largo del dominio {t} de cada curva de riel (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {t} se pondera según la curvatura de las curvas de riel de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Cajas torcidas de barrido resultantes |

### Twisted Box Sweep Variable (TBoxSweepVar)

Crea cajas torcidas conectadas a lo largo de cuatro curvas de riel, con un conjunto separado de parámetros de división del dominio para cada riel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rail 1 | `R¹` | Curve | item | Curva de riel donde están la primera y la cuarta esquina de las cajas torcidas |
| Rail 2 | `R²` | Curve | item | Curva de riel donde están la segunda y la tercera esquina de las cajas torcidas |
| Rail 3 | `R³` | Curve | item | Curva de riel donde están la sexta y la séptima esquina de las cajas torcidas |
| Rail 3 | `R⁴` | Curve | item | Curva de riel donde están la quinta y la octava esquina de las cajas torcidas |
| Parameters T1 | `t¹` | Number | lista | Parámetros de división a lo largo del dominio {t} del riel uno (0.0 = inicio de Rail 1, 1.0 = final). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {t} |
| Parameters T2 | `t²` | Number | lista | Parámetros de división a lo largo del dominio {t} del riel dos (0.0 = inicio de Rail 2, 1.0 = final). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {t} |
| Parameters T3 | `t³` | Number | lista | Parámetros de división a lo largo del dominio {t} del riel tres (0.0 = inicio de Rail 3, 1.0 = final). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {t} |
| Parameters T4 | `t⁴` | Number | lista | Parámetros de división a lo largo del dominio {t} del riel cuatro (0.0 = inicio de Rail 4, 1.0 = final). Para mejores resultados, deben estar entre 0 y 1, en orden numérico, sin repetirse y con la misma cantidad que las otras listas de parámetros {t} |
| Weighted | `W` | Boolean | item | Si es True, las distribuciones de los parámetros {t} se ponderan según la curvatura de las curvas de riel de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Cajas torcidas de barrido resultantes |

### Twisted Box Through Curves (TBoxThruCrvs)

Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de curvas, según un espesor y parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Conjunto de curvas a través de las cuales crear el arreglo de cajas torcidas |
| Thickness | `T` | Number | item | Espesor total del arreglo de cajas torcidas, con offset desde las curvas |
| Parameters U | `u` | Number | lista | Parámetros de división a través del dominio {u} de las curvas ({u} 0.0 = curva al inicio de C, 1.0 = curva al final de C), salvo que Normalized sea False. Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo de los dominios {v} de las curvas ({v} 0.0 = inicios de las curvas, 1.0 = finales). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división a lo largo del dominio {w} del espesor ({w} 0.0 = curvas, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Normalized | `N` | Boolean | item | Si es False, las reglas de los parámetros {u} son ({u} 0.0 = curva en el índice 0, número de índice de la última curva = curva en el último índice). Para mejores resultados, los parámetros {u} deben estar entre 0 y el índice de la última curva, en orden numérico y sin repetirse |
| Equalized | `E` | Boolean | item | Si es True, la distribución de los parámetros {u} se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de curvas de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {v} se pondera según la curvatura de las curvas de entrada |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {u} continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango de los parámetros {u}) |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {u}: 0 = recto, 1 = normal, 2 = ajustado, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da cajas torcidas de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da cajas torcidas de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante a través de las curvas |

### Twisted Box Through Meshes (TBoxThruMshs)

Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de mallas a partir de sus caras; funciona con caras cuadrangulares y triangulares. Las mallas deben tener la misma topología.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Conjunto de mallas a través de las cuales crear el arreglo de cajas torcidas |
| Parameters W | `w` | Number | lista | Parámetros de división a través del dominio {w} de las mallas ({w} 0.0 = malla al inicio de M, 1.0 = malla al final de M), salvo que Normalized sea False. Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Normalized | `N` | Boolean | item | Si es False, las reglas de los parámetros {w} son ({w} 0.0 = malla en el índice 0, número de índice de la última malla = malla en el último índice). Para mejores resultados, los parámetros {w} deben estar entre 0 y el índice de la última malla, en orden numérico y sin repetirse |
| Equalized | `E` | Boolean | item | Si es True, la distribución de los parámetros {w} se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de mallas de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {w} se pondera según el conjunto de mallas de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {w} continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango de los parámetros {w}) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación {w}; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {w}: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante a través de las mallas |

### Twisted Box Through Surfaces (TBoxThruSrfs)

Crea un arreglo en capas de cajas torcidas conectadas a través de un conjunto de superficies, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Conjunto de superficies a través de las cuales crear el arreglo de cajas torcidas |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo de los dominios {u} de las superficies ({u} 0.0 = inicios de las superficies, 1.0 = finales). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo de los dominios {v} de las superficies ({v} 0.0 = inicios de las superficies, 1.0 = finales). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división a través del dominio {w} de las superficies ({w} 0.0 = superficie al inicio de S, 1.0 = superficie al final de S), salvo que Normalized sea False. Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Normalized | `N` | Boolean | item | Si es False, las reglas de los parámetros {w} son ({w} 0.0 = superficie en el índice 0, número de índice de la última superficie = superficie en el último índice). Para mejores resultados, los parámetros {w} deben estar entre 0 y el índice de la última superficie, en orden numérico y sin repetirse |
| Equalized | `E` | Boolean | item | Si es True, la distribución de los parámetros {w} se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de superficies de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {w} se pondera según el conjunto de superficies de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación de los parámetros {w} continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango de los parámetros {w}) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación {w}; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino de interpolación {w}: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da cajas torcidas de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da cajas torcidas de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante a través de las superficies |

### Twisted Box Tube (TBoxTube)

Crea un arreglo tubular en capas de cajas torcidas conectadas a lo largo de una curva, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual crear el arreglo tubular de cajas torcidas |
| Radius | `R` | Number | item | Radio exterior del arreglo tubular de cajas torcidas |
| Thickness | `T` | Number | item | Espesor del arreglo tubular de cajas torcidas, con offset hacia adentro desde las esquinas del radio exterior |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la curva (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división alrededor del dominio {v} de la curva (0.0 = mínimo de la revolución, 1.0 = máximo). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división a lo largo del dominio {w} del espesor (0.0 = radio, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {u} se pondera según la curvatura de la curva de entrada |
| Offset | `O` | Domain | item | Ubicación del centro desfasado del arreglo tubular respecto de la curva, definida por un dominio (0.0 a 0.0 = centrado en la curva) |
| Rotation 1 | `R¹` | Number | item | Rotación del arreglo tubular de cajas torcidas alrededor de los centros del radio, en grados |
| Rotation 2 | `R²` | Number | item | Rotación del arreglo tubular de cajas torcidas alrededor de la curva, en grados (si el arreglo está centrado en la curva, el efecto se ve igual que la rotación 1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo tubular de cajas torcidas resultante a lo largo de la curva |

### Twisted Box Tube Variable (TBoxTubeVar)

Crea un arreglo tubular en capas de cajas torcidas conectadas a lo largo de una curva, según parámetros que dividen el dominio, con diámetros, espesores y rotaciones variables.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a lo largo de la cual crear el arreglo tubular de cajas torcidas |
| Radii | `R` | Number | lista | Una lista de radios exteriores del arreglo tubular en cada parámetro de división {u} |
| Thicknesses | `T` | Number | lista | Una lista de espesores del arreglo tubular en cada parámetro de división {u}, con offset hacia adentro desde las esquinas del radio exterior |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo del dominio {u} de la curva (0.0 = inicio de la curva, 1.0 = final). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división alrededor del dominio {v} de la curva (0.0 = mínimo de la revolución, 1.0 = máximo). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división a lo largo del dominio {w} del espesor (0.0 = radios, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {u} se pondera según la curvatura de la curva de entrada |
| Offsets | `O` | Domain | lista | Una lista de ubicaciones del centro desfasado del arreglo tubular respecto de la curva en cada parámetro de división {u}, definidas por dominios (0.0 a 0.0 = centrado en la curva) |
| Rotations 1 | `R¹` | Number | lista | Una lista de rotaciones del arreglo tubular alrededor de los centros de los radios en cada parámetro de división {u}, en grados |
| Rotations 2 | `R¹` | Number | lista | Una lista de rotaciones del arreglo tubular alrededor de la curva en cada parámetro de división {u}, en grados (si el arreglo está centrado en la curva, el efecto se ve igual que la rotación 1) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo tubular de cajas torcidas resultante a lo largo de la curva |

### Twisted Box Two Curves (TBox2Crvs)

Crea un arreglo en capas de cajas torcidas conectadas entre dos curvas, según un espesor y parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Curva desde la que crear el arreglo de cajas torcidas |
| Curve B | `B` | Curve | item | Curva hacia la que crear el arreglo de cajas torcidas |
| Thickness | `T` | Number | item | Espesor total del arreglo de cajas torcidas, con offset desde las curvas |
| Parameters U | `u` | Number | lista | Parámetros de división del dominio {u} entre las curvas ({u} 0.0 = Curve A, 1.0 = Curve B). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo de los dominios {v} de las curvas ({v} 0.0 = inicios de las curvas, 1.0 = finales). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división a lo largo del dominio {w} del espesor ({w} 0.0 = curvas, 1.0 = espesor). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Weighted | `W` | Boolean | item | Si es True, la distribución de los parámetros {v} se pondera según la curvatura de las curvas de entrada |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la curva reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las curvas de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las curvas y el grado entero de entrada, intentando conservar su forma. Refit da cajas torcidas de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las curvas de entrada, sus puntos de control se recrean dividiendo la curva en partes iguales según la cantidad de puntos de entrada. Point Sample da cajas torcidas de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante entre las curvas |

### Twisted Box Two Meshes (TBox2Mshs)

Crea un arreglo en capas de cajas torcidas conectadas entre dos mallas a partir de sus caras; funciona con caras cuadrangulares y triangulares. Las mallas deben tener la misma topología.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh A | `A` | Mesh | item | Malla desde la que crear las cajas torcidas |
| Mesh B | `B` | Mesh | item | Malla hacia la que crear las cajas torcidas |
| Parameters W | `w` | Number | lista | Parámetros de división del dominio {w} entre las mallas ({w} 0.0 = Mesh A, 1.0 = Mesh B). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante entre las mallas |

### Twisted Box Two Surfaces (TBox2Srfs)

Crea un arreglo en capas de cajas torcidas conectadas entre dos superficies, según parámetros que dividen el dominio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface A | `A` | Surface | item | Superficie desde la que crear el arreglo de cajas torcidas |
| Surface B | `B` | Surface | item | Superficie hacia la que crear el arreglo de cajas torcidas |
| Parameters U | `u` | Number | lista | Parámetros de división a lo largo de los dominios {u} de las superficies ({u} 0.0 = inicios de las superficies, 1.0 = finales). Para mejores resultados, los parámetros {u} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters V | `v` | Number | lista | Parámetros de división a lo largo de los dominios {v} de las superficies ({v} 0.0 = inicios de las superficies, 1.0 = finales). Para mejores resultados, los parámetros {v} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Parameters W | `w` | Number | lista | Parámetros de división del dominio {w} entre las superficies ({w} 0.0 = Surface A, 1.0 = Surface B). Para mejores resultados, los parámetros {w} deben estar entre 0 y 1, en orden numérico y sin repetirse |
| Refit | `R` | Integer | item | Método de coincidencia Refit opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y grado de la superficie reajustada.) Si es un entero mayor que cero, se usa el método Refit cuando es posible. Al reajustar las superficies de entrada, sus puntos de control se redistribuyen, se agregan o se quitan según la curvatura de las superficies y el grado entero de entrada, intentando conservar su forma. Refit da cajas torcidas de forma más ceñida, con puntos de control distribuidos según la curvatura. |
| Point Sample | `P` | Integer | item | Método de coincidencia Point Sample opcional. (Sin entero o 0 = desactivado; entero mayor que 0 = activado y cantidad de puntos de muestra.) Si es un entero mayor que cero, se usa el método Point Sample. Al muestrear las superficies de entrada, sus puntos de control se recrean dividiendo la superficie en partes iguales según la cantidad de puntos de entrada. Point Sample da cajas torcidas de forma más holgada, con puntos de control distribuidos de forma uniforme. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Arreglo de cajas torcidas resultante entre las superficies |

### Twisted Box Volume (TBoxVol)

Calcula las propiedades de volumen de una caja torcida.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Box | `TB` | Twisted Box | item | Caja torcida para calcular el volumen |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Volume | `V` | Number | item | Volumen de la caja torcida |
| Centroid | `C` | Point | item | Centroide del volumen de la caja torcida |

### Weighted Average Twisted Box (WavTBox)

Calcula el promedio aritmético ponderado de un conjunto de cajas torcidas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Twisted Boxes | `TB` | Twisted Box | lista | Conjunto de cajas torcidas a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada caja torcida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Twisted Box | item | Media aritmética (promedio) de todas las cajas torcidas de entrada |

## Vector

### Closest Vector (CVec)

Busca el vector objetivo más cercano en ángulo a un vector de referencia.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reference | `R` | Vector | item | Vector de referencia desde el que buscar |
| Targets | `T` | Vector | lista | Conjunto de vectores objetivo en el que buscar |
| Keep Length | `K` | Boolean | item | Conserva la longitud del vector de referencia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest | `C` | Vector | item | Vector objetivo más cercano en ángulo al vector de referencia |
| Index | `i` | Integer | item | Índice del vector objetivo más cercano en ángulo al vector de referencia |
| Angle | `A` | Number | item | Ángulo entre el vector de referencia y el vector objetivo más cercano, en radianes |

### Mirror Combine Vectors (MirComVecs)

Refleja un conjunto de vectores desde su final o su inicio y lo combina con el conjunto original.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vectors | `V` | Vector | lista | Conjunto de vectores a reflejar y combinar |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = final del conjunto, True = inicio del conjunto) |
| Join | `J` | Boolean | item | Une el conjunto de vectores reflejado y combinado (quita el vector duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de vectores: 0 = reflejado, 1 = invertido |
| Plane *(opcional)* | `Pl` | Plane | item | Plano opcional para reflejar las direcciones de los vectores al usar el tipo reflejado; si no, solo se refleja el orden del conjunto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirrored | `M` | Vector | lista | Conjunto de vectores reflejado y combinado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |

### Mirror Cut Vectors (MirCutVecs)

Corta un conjunto de vectores en un índice, refleja el lado conservado del corte respecto de ese índice y lo combina con el lado conservado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vectors | `V` | Vector | lista | Conjunto de vectores a cortar y reflejar |
| Mirror Index | `Mi` | Integer | item | Índice respecto del cual se refleja el lado conservado del corte. Un índice negativo invierte el conjunto de vectores y quita desde arriba. |
| Flip | `F` | Boolean | item | Invierte la dirección del reflejo (False = reflejar después del índice, True = reflejar antes del índice) |
| Join | `J` | Boolean | item | Une el conjunto de vectores cortado y reflejado (quita el vector duplicado al medio del conjunto) |
| Mirror Type | `T` | Integer | item | Determina cómo se refleja el conjunto de vectores: 0 = reflejado, 1 = invertido |
| Plane *(opcional)* | `Pl` | Plane | item | Plano opcional para reflejar las direcciones de los vectores al usar el tipo reflejado; si no, solo se refleja el orden del conjunto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mirror Cut | `M` | Vector | lista | Conjunto de vectores cortado y reflejado resultante |
| Split Index | `i` | Integer | item | El índice de división (solo si Join es False). Para dividir el conjunto cortado y reflejado en el punto del reflejo, usa esto como índice en el componente Split List de Grasshopper. |
| Intersected | `I` | Boolean | item | True si el índice de reflejo intersectó el conjunto de vectores, False si no lo intersectó |

### Reparameterize Vectors (ReparamVecs)

Reparametriza un conjunto de vectores para que su longitud (amplitud) vaya de 0 a 1, o de forma invertida de 1 a 0.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vectors | `V` | Vector | lista | Conjunto de vectores a reparametrizar |
| Invert | `I` | Boolean | item | Invierte el rango de longitudes (amplitudes) para que vaya de 1 a 0 en vez de 0 a 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reparameterized | `R` | Vector | lista | Conjunto de vectores reparametrizado resultante |
| Original | `O` | Domain | item | El rango original de longitudes (amplitudes) del conjunto de vectores |

### Tween Consecutive Vectors (TwnConVecs)

Interpola (tween) consecutivamente entre un conjunto de vectores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vectors | `V` | Vector | lista | Conjunto de vectores entre los que interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = vector en V, 1.0 = vector en V +1) |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de vectores de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Vector | lista | Vectores interpolados resultantes |

### Tween Through Vectors (TwnThruVecs)

Interpola (tween) a través de un conjunto de vectores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vectors | `V` | Vector | lista | Conjunto de vectores a través de los cuales interpolar |
| Factor | `F` | Number | lista | Factor de interpolación (0.0 = vector al inicio de V, 1.0 = vector al final de V), salvo que Normalized sea False |
| Normalized | `N` | Boolean | item | Si es False, las reglas del factor son (0.0 = vector en el índice 0, número de índice del último vector = vector en el último índice). El rango del factor de un vector al siguiente es: el número de índice de un vector = el vector en ese índice, el número de índice del siguiente = el siguiente vector de la lista, y los factores entre esos índices dan las interpolaciones correspondientes. Por ejemplo, un factor de 2.5 da un vector a medio camino entre el del índice 2 y el del índice 3. |
| Equalized | `E` | Boolean | item | Si es True, la distribución de la interpolación se evalúa a lo largo del camino de interpolación sin considerar las ubicaciones del conjunto de vectores de entrada |
| Weighted | `W` | Boolean | item | Si es True, la distribución de la interpolación se pondera según el conjunto de vectores de entrada y la curvatura del camino de interpolación |
| Loopback | `L` | Boolean | item | Si es True, permite que el camino de interpolación continúe desde el final de vuelta al inicio como un circuito cerrado (si Normalized es False, aumenta en 1 el máximo del rango del factor) |
| Degree | `D` | Integer | item | Grado de curvatura del camino de interpolación; debe ser un número impar positivo |
| Interpolation Type | `I` | Integer | item | Determina cómo se interpola el camino: 0 = lineal, 1 = cuerda, 2 = raíz cuadrada, 3 = uniforme |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Vector | lista | Vector interpolado resultante |

### Tween Two Vectors (Twn2Vecs)

Interpola (tween) entre dos vectores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vector A | `A` | Vector | item | Vector desde el que interpolar |
| Vector B | `B` | Vector | item | Vector hacia el que interpolar |
| Factor | `F` | Number | item | Factor de interpolación (0.0 = Vector A, 1.0 = Vector B) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tween | `T` | Vector | item | Vector interpolado resultante |

### Vector Star (VecStar)

Crea una subdivisión espacial recursiva de vectores, orientada a un plano, que sale desde el origen de un plano base

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base para la orientación y ubicación de la estrella de vectores |
| Steps | `N` | Integer | item | Cantidad de pasos recursivos de subdivisión |
| Subdivision Type | `T` | Integer | item | Determina cómo se subdivide la estrella de vectores: 0 = cúbica, 1 = esférica |
| Dimensionality | `D` | Boolean | item | True para 2D, False para 3D |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vectors | `V` | Vector | lista | Vectores de subdivisión espacial resultantes |
| Lines | `L` | Line | lista | Representación de los vectores como líneas |

### Vector World (VecWorld)

Crea vectores alineados con los ejes de un plano que salen desde el origen de un plano base

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano base para la orientación y ubicación de los vectores |
| Direction Type | `T` | Integer | item | Determina las direcciones de vectores a usar: 0 = cardinales, 1 = intercardinales, 2 = cardinales + intercardinales |
| Dimensionality | `D` | Boolean | item | True para 2D, False para 3D |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vectors | `V` | Vector | lista | Vectores alineados con los ejes resultantes |
| Lines | `L` | Line | lista | Representación de los vectores como líneas |
