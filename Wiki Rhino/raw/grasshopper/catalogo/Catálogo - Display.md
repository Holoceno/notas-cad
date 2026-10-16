---
title: "Catálogo Grasshopper — Display"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Display"
libraries: ["Curve Components 8.35.26251.13001", "Field Components 8.35.26251.13001", "Grasshopper 1.0.0008", "IO Components 8.35.26251.13001", "Math Components 8.35.26251.13001", "Vector Components 8.35.26251.13001"]
components: 46
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, rhino/vista]
---

# Display

46 objetos · librería: Curve Components 8.35.26251.13001, Field Components 8.35.26251.13001, Grasshopper 1.0.0008, IO Components 8.35.26251.13001, Math Components 8.35.26251.13001, Vector Components 8.35.26251.13001 · autor: Robert McNeel & Associates

Mapas: [[Mapa - Visualización y anotaciones]] (46)

## Colour

### Colour CMYK (CMYK)

Crea un color a partir de canales {CMYK} en coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cyan | `C` | Number | item | Canal cian (definido en el rango {0.0 a 1.0}) |
| Magenta | `M` | Number | item | Canal magenta (definido en el rango {0.0 a 1.0}) |
| Yellow | `Y` | Number | item | Canal amarillo (definido en el rango {0.0 a 1.0}) |
| Key | `K` | Number | item | Canal negro/key (definido en el rango {0.0 a 1.0}) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Colour HSL (HSL)

Crea un color a partir de canales {HSL} en coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa (definido en el rango {0.0 a 1.0}) |
| Hue | `H` | Number | item | Canal de tono (definido en el rango {0.0 a 1.0}) |
| Saturation | `S` | Number | item | Canal de saturación (definido en el rango {0.0 a 1.0}) |
| Luminance | `L` | Number | item | Canal de luminancia (definido en el rango {0.0 a 1.0}) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Colour HSV (HSV)

Crea un color a partir de canales {HSV} en coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa (definido en el rango {0.0 a 1.0}) |
| Hue | `H` | Number | item | Canal de tono (definido en el rango {0.0 a 1.0}) |
| Saturation | `S` | Number | item | Canal de saturación (definido en el rango {0.0 a 1.0}) |
| Value | `V` | Number | item | Canal de valor (valor/brillo definido en el rango {0.0 a 1.0}) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Colour L*ab (L*AB)

Crea un color a partir de canales {CIE L*ab} en coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa (definido en el rango {0.0 a 1.0}) |
| Luminance | `L` | Number | item | Canal de luminancia (definido en el rango {0.0 a 1.0}) |
| A | `A` | Number | item | Primer canal de color (A definido en el rango {-1.0 a 1.0}) |
| B | `B` | Number | item | Canal de color opuesto (B definido en el rango {-1.0 a 1.0}) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Colour LCH (LCH)

Crea un color a partir de canales {CIE LCH} en coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa (definido en el rango {0.0 a 1.0}) |
| Luminance | `L` | Number | item | Canal de luminancia (definido en el rango {0.0 a 1.0}) |
| Chroma | `C` | Number | item | Canal de croma (definido en el rango {0.0 a 1.0}) |
| Hue | `H` | Number | item | Canal de tono (definido en el rango {0.0 a 1.0}) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Colour RGB (RGB)

Crea un color a partir de canales {RGB}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Integer | item | Canal alfa (255 = opaco) |
| Red | `R` | Integer | item | Canal rojo |
| Green | `G` | Integer | item | Canal verde |
| Blue | `B` | Integer | item | Canal azul |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Colour RGB (f) (fRGB)

Crea un color a partir de canales {RGB} en coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa (1.0 = opaco) |
| Red | `R` | Number | item | Canal rojo |
| Green | `G` | Number | item | Canal verde |
| Blue | `B` | Number | item | Canal azul |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Colour XYZ (XYZ)

Crea un color a partir de canales {XYZ} en coma flotante (especificación CIE 1931).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa (definido en el rango {0.0 a 1.0}) |
| X | `X` | Number | item | Estímulo X (definido en el rango {0.0 a 1.0}) |
| Y | `Y` | Number | item | Estímulo Y (definido en el rango {0.0 a 1.0}) |
| Z | `Z` | Number | item | Estímulo Z (definido en el rango {0.0 a 1.0}) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color resultante |

### Split AHSL (AHSL)

Separa un color en canales {AHSL} en coma flotante

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa |
| Hue | `H` | Number | item | Tono |
| Saturation | `S` | Number | item | Saturación |
| Luminance | `L` | Number | item | Luminancia |

### Split AHSV (AHSV)

Separa un color en canales {AHSV} en coma flotante

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa |
| Hue | `H` | Number | item | Tono |
| Saturation | `S` | Number | item | Saturación |
| Value | `V` | Number | item | Valor (brillo) |

### Split ARGB (ARGB)

Separa un color en canales {ARGB} en coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `A` | Number | item | Canal alfa |
| Red | `R` | Number | item | Canal rojo |
| Green | `G` | Number | item | Canal verde |
| Blue | `B` | Number | item | Canal azul |

## Dimensions

### Aligned Dimension (AlignDim)

Crea una cota de distancia entre dos puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano de la cota |
| Point A | `A` | Point | item | Primer punto de la cota |
| Point B | `B` | Point | item | Segundo punto de la cota |
| Offset | `O` | Number | item | Desfase de la línea base |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Angular Dimension (AngleDim)

Crea una cota de ángulo entre puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center | `C` | Point | item | Punto central del ángulo |
| Point A | `A` | Point | item | Extremo de la primera dirección del ángulo |
| Point B | `B` | Point | item | Extremo de la segunda dirección del ángulo |
| Reflex | `R` | Boolean | item | Crea la cota del ángulo reflejo |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Angular Dimensions (Mesh) (AngleDimMesh)

Crea cotas de ángulo en todas las esquinas de una malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a acotar |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |
| Length Factor | `F` | Number | item | Radio de la cota como fracción de la longitud de la arista. |
| Minimum Angle *(opcional)* | `A0` | Number | item | Ángulo umbral bajo el cual no se dibujan las cotas. |
| Maximum Angle *(opcional)* | `A1` | Number | item | Ángulo umbral sobre el cual no se dibujan las cotas. |

### Arc Dimension (ArcDim)

Crea una cota de ángulo a partir de un arco.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arc | `A` | Arc | item | Arco guía |
| Offset | `O` | Number | item | Desfase de la cota |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Circular Dimension (CircleDim)

Crea una cota de ángulo proyectada sobre un círculo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | item | Círculo guía de la cota |
| Point A | `A` | Point | item | Primer punto del ángulo |
| Point B | `B` | Point | item | Segundo punto del ángulo |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Gradient Hatch (GHatch)

Crea un sombreado (hatch) de degradado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundaries | `B` | Curve | lista | Curvas de contorno de los sombreados |
| Axis | `A` | Line | item | Eje del degradado |
| Colour 1 | `C1` | Colour | item | Color al inicio del eje. |
| Colour 2 | `C2` | Colour | item | Color al final del eje. |

### Line Dimension (LineDim)

Crea una cota de distancia a lo largo de una línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea base de la cota |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Linear Dimension (LinearDim)

Crea una cota de distancia entre puntos, proyectada sobre una línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea base de la cota |
| Point A | `A` | Point | item | Primer punto de la cota |
| Point B | `B` | Point | item | Segundo punto de la cota |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Make2D

Crea un dibujo de líneas ocultas a partir de la geometría

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría a incluir (solo Breps, mallas y curvas). |
| Clipping Planes *(opcional)* | `C` | Plane | lista | Planos de recorte (opcional). |
| View | `V` | View | item | Detalles de la proyección Make2D |
| Tangent Edges | `Te` | Boolean | item | Si se calculan o no las aristas tangentes. |
| Tangent Seams | `Ts` | Boolean | item | Si se calculan o no las costuras tangentes. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Visible curves | `V` | Curve | lista | Lista de curvas visibles |
| Visible index | `Vi` | Integer | lista | Para cada curva visible, índice del objeto de origen |
| Visible type | `Vt` | Text | lista | Para cada curva visible, descripción del tipo |
| Hidden curves | `H` | Curve | lista | Lista de curvas ocultas |
| Hidden index | `Hi` | Integer | lista | Para cada curva oculta, índice del objeto de origen |
| Hidden type | `Ht` | Text | lista | Para cada curva oculta, descripción del tipo |

### Make2D Parallel View (M2D Parallel)

Define una vista paralela para una solución Make2D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Projection | `P` | Rectangle | item | Proyección de la vista. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| View | `V` | View | item | Vista paralela |

### Make2D Perspective View (M2D Perspective)

Define una vista en perspectiva para una solución Make2D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Camera | `C` | Point | item | Posición de la cámara |
| Frame | `F` | Rectangle | item | Encuadre de la proyección. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| View | `V` | View | item | Vista paralela |

### Marker Dimension (MarkDim)

Crea una anotación de texto en un punto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea base de la cota |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Pattern Hatch (PHatch)

Crea un sombreado (hatch) con patrón

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundaries | `B` | Curve | lista | Curvas de contorno de los sombreados |
| Pattern | `P` | Integer | item | Estilo del patrón de sombreado |
| Scale | `S` | Number | item | Escala del patrón |
| Angle | `A` | Number | item | Ángulo del patrón |

### Serial Dimension (SerialDim)

Crea una cota de distancia entre varios puntos, proyectada sobre una línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea base de la cota |
| Points | `P` | Point | lista | Puntos de la cota; el primero marca el punto cero |
| Text | `T` | Text | item | Texto de la cota |
| Size | `S` | Number | item | Tamaño de la cota |

### Text Tag (Tag)

Representa una lista de etiquetas de texto en una vista de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `L` | Point | item | Ubicación de la etiqueta de texto |
| Text | `T` | Text | item | El texto a mostrar |
| Colour *(opcional)* | `C` | Colour | item | Color de la etiqueta (opcional) |

### Text Tag 3D (Tag)

Representa una lista de etiquetas de texto 3D en una vista de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `L` | Plane | item | Ubicación y orientación de la etiqueta de texto |
| Text *(opcional)* | `T` | Text | item | El texto a mostrar |
| Size | `S` | Number | item | Tamaño del texto |
| Colour *(opcional)* | `C` | Colour | item | Color de la etiqueta (opcional) |
| Justification | `J` | Integer | item | Justificación del texto |

## Graphs

### Bar Graph (parámetro)

Representación en gráfico de barras de un conjunto de números

Tipo de dato: **Number**

### Image Gallery (Gallery, objeto especial)

Muestra una secuencia de imágenes

### Legend

Muestra una leyenda formada por etiquetas y colores

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour *(opcional)* | `C` | Colour | lista | Colores de la leyenda |
| Tags *(opcional)* | `T` | Text | lista | Etiquetas de la leyenda |
| Rectangle *(opcional)* | `R` | Rectangle | item | Rectángulo de la leyenda en el espacio 3D (opcional) |

### Pie Chart (Pie, parámetro)

Muestra un conjunto de fragmentos de texto como gráfico de torta

Tipo de dato: **Text**

### Quick Graph (Graph, parámetro)

Muestra un conjunto de valores Y como gráfico

Tipo de dato: **Number**

### Value Tracker (Tracker, parámetro)

Registra una colección de valores numéricos a lo largo del tiempo

Tipo de dato: **Timed numbers**

## Preview

### Cloud Display (Cloud)

Dibuja una colección de puntos como una nube difusa

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `P` | Point | lista | Ubicación de cada mancha |
| Colours *(opcional)* | `C` | Colour | lista | Color de cada mancha |
| Size *(opcional)* | `S` | Number | item | Tamaño de cada mancha |

### Create Material (Material)

Crea un material OpenGL.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Diffuse | `Kd` | Colour | item | Color del canal difuso |
| Specular | `Ks` | Colour | item | Color del brillo especular |
| Emission | `Ke` | Colour | item | Color emisivo del material |
| Transparency | `T` | Number | item | Cantidad de transparencia (0.0 = opaco, 1.0 = transparente) |
| Shine | `S` | Integer | item | Cantidad de brillo (0 = nada, 1 = brillo bajo, 100 = brillo máximo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Shader | item | Material resultante |

### Custom Curve Preview (Curve Preview)

Vista previa personalizada de curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curvas a dibujar |
| Linetype *(opcional)* | `L` | Model Linetype | item | El tipo de línea del modelo de Rhino que se usa para dibujar las curvas |
| Colour | `C` | Colour | item | El color que se usa para dibujar las curvas |

### Custom Preview (Preview)

Permite vistas previas personalizadas de la geometría

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a previsualizar |
| Material | `M` | Shader | item | El material que reemplaza al original |

### Deconstruct Material (DMaterial)

Descompone un material de visualización (sombreador) en sus distintos atributos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Shader | item | El material de visualización |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Diffuse | `Kd` | Colour | item | Color del canal difuso. |
| Specular | `Ks` | Colour | item | Color del brillo especular. |
| Emission | `Ke` | Colour | item | Color emisivo del material. |
| Transparency | `T` | Number | item | Cantidad de transparencia (0.0 = opaco, 1.0 = transparente) |
| Shine | `S` | Integer | item | La cantidad de brillo (0 = nada, 1 = brillo bajo, 100 = brillo máximo) |

### Dot Display (Dots)

Dibuja una colección de puntos de colores

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Ubicación del punto |
| Colour | `C` | Colour | item | Color del punto |
| Size | `S` | Number | item | Tamaño del punto |

### Symbol (Advanced) (SymAdv)

Propiedades avanzadas de visualización de símbolos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Style | `X` | Integer | item | Estilo del símbolo |
| Size Primary | `S1` | Number | item | Tamaño del símbolo |
| Size Secondary | `S2` | Number | item | Tamaño alternativo o desfase (según el estilo). |
| Rotation | `R` | Number | item | Ángulo de rotación |
| Fill | `Cf` | Colour | item | Color de relleno |
| Edge | `Ce` | Colour | item | Color del borde |
| Width | `W` | Number | item | Ancho del borde |
| Adjust | `A` | Boolean | item | Ajusta el tamaño aparente según la vista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Symbol Display | `D` | Symbol Display | item | Propiedades de visualización del símbolo |

### Symbol (Simple) (SymSim)

Propiedades simples de visualización del símbolo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Style | `X` | Integer | item | Estilo del símbolo |
| Size | `S` | Number | item | Radio principal o tamaño exterior |
| Rotation | `R` | Number | item | Ángulo de rotación |
| Colour | `C` | Colour | item | Color principal |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Symbol Display | `D` | Symbol Display | item | Propiedades de visualización del símbolo |

### Symbol Display (Symbol)

Muestra símbolos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `P` | Point | item | Ubicación del símbolo |
| Display | `D` | Symbol Display | item | Propiedades de visualización del símbolo |

## Vector

### Point List (Points)

Muestra detalles de listas de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `P` | Point | lista | Puntos a mostrar |
| Size *(opcional)* | `S` | Number | item | Tamaño del texto (opcional, en unidades de Rhino) |

### Point Order (Order)

Muestra el orden de una lista de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points *(opcional)* | `P` | Point | lista | Puntos a mostrar |

### Vector Display (VDis)

Previsualiza vectores en la vista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Anchor *(opcional)* | `A` | Point | item | Punto de anclaje del vector a previsualizar |
| Vector *(opcional)* | `V` | Vector | item | Vector a previsualizar |

### Vector Display Ex (VDisEx)

Previsualiza vectores en la vista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point *(opcional)* | `P` | Point | item | Punto inicial del vector |
| Vector *(opcional)* | `V` | Vector | item | Vector a mostrar |
| Colour *(opcional)* | `C` | Colour | item | Color del vector |
| Width *(opcional)* | `W` | Integer | item | Ancho de las líneas del vector |
