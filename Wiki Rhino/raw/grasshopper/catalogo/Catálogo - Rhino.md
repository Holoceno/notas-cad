---
title: "Catálogo Grasshopper — Rhino"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Rhino"
libraries: ["IO Components 8.35.26251.13001"]
components: 105
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, rhino/vista, rhino/documento]
---

# Rhino

105 objetos · librería: IO Components 8.35.26251.13001 · autor: Robert McNeel & Associates

Mapas: [[Mapa - Visualización y anotaciones]] (59) · [[Mapa - Documento de Rhino]] (46)

## Annotations

### Aligned Dimension (DimAligned)

Cota alineada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Aligned Dimension *(opcional)* | `Aligned Dimension` | Linear Dimension | item | La cota alineada de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Point A *(opcional)* | `Point A` | Point | item | Primer punto de la cota |
| Point B *(opcional)* | `Point B` | Point | item | Segundo punto de la cota |
| Offset *(opcional)* | `Offset` | Number | item | Desfase de la línea base. |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Aligned Dimension | `Aligned Dimension` | Linear Dimension | item | La cota alineada de Rhino |
| Plane | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Point A | `Point A` | Point | item | Primer punto de la cota |
| Point B | `Point B` | Point | item | Segundo punto de la cota |
| Offset | `Offset` | Number | item | Desfase de la línea base. |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Angle Dimension (Arc) (DimAngle-A)

Cota angular a partir de arcos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle Dimension *(opcional)* | `Angle Dimension` | Angular Dimension | item | La cota angular de Rhino |
| Arc *(opcional)* | `Arc` | Arc | item | Arco guía |
| Offset *(opcional)* | `Offset` | Number | item | Desfase de la cota |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle Dimension | `Angle Dimension` | Angular Dimension | item | La cota angular de Rhino |
| Arc | `Arc` | Arc | item | Arco guía |
| Offset | `Offset` | Number | item | Desfase de la cota |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Angle Dimension (Lines) (DimAngle-L)

Cota angular a partir de líneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle Dimension *(opcional)* | `Angle Dimension` | Angular Dimension | item | La cota angular de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Line A *(opcional)* | `Line A` | Line | item | La línea que define la dirección del primer lado del ángulo. |
| Line B *(opcional)* | `Line B` | Line | item | La línea que define la dirección del segundo lado del ángulo. |
| Dimension Location *(opcional)* | `Dimension Location` | Point | item | Un punto sobre el arco de la cota. |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle Dimension | `Angle Dimension` | Angular Dimension | item | La cota angular de Rhino |
| Plane | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Line A | `Line A` | Line | item | La línea que define la dirección del primer lado del ángulo. |
| Line B | `Line B` | Line | item | La línea que define la dirección del segundo lado del ángulo. |
| Dimension Location | `Dimension Location` | Point | item | Un punto sobre el arco de la cota. |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Angle Dimension (Points) (DimAngle-P)

Cota angular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle Dimension *(opcional)* | `Angle Dimension` | Angular Dimension | item | La cota angular de Rhino |
| Center *(opcional)* | `Center` | Point | item | Punto central del ángulo |
| Point A *(opcional)* | `Point A` | Point | item | Extremo de la primera dirección del ángulo |
| Point B *(opcional)* | `Point B` | Point | item | Extremo de la segunda dirección del ángulo |
| Dimension Location *(opcional)* | `Dimension Location` | Point | item | Un punto sobre la línea de cota. |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle Dimension | `Angle Dimension` | Angular Dimension | item | La cota angular de Rhino |
| Center | `Center` | Point | item | Punto central del ángulo |
| Point A | `Point A` | Point | item | Extremo de la primera dirección del ángulo |
| Point B | `Point B` | Point | item | Extremo de la segunda dirección del ángulo |
| Dimension Location | `Dimension Location` | Point | item | Un punto sobre la línea de cota. |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Annotation Arrow Settings (AS-Arrows)

Ajustes de flechas del estilo de anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arrow Settings *(opcional)* | `Arrow Settings` | Annotation Arrow Settings | item | Ajustes de flechas |
| Arrow 1 *(opcional)* | `Arrow 1` | Arrow Type | item | Flecha 1 |
| Arrow 2 *(opcional)* | `Arrow 2` | Arrow Type | item | Flecha 2 |
| Arrow Size *(opcional)* | `Arrow Size` | Number | item | Tamaño de flecha |
| Fit Arrow *(opcional)* | `Fit Arrow` | Integer | item | Ajuste de flechas: 0) Auto: se muestran dentro cuando hay espacio; 1) Forzar flechas dentro de las líneas de extensión; 2) Forzar flechas fuera de las líneas de extensión |
| Dimension Inline *(opcional)* | `Dimension Inline` | Boolean | item | Dibuja la línea de cota entre las líneas de extensión si las flechas están fuera |
| Leader Arrow *(opcional)* | `Leader Arrow` | Arrow Type | item | Flecha de la directriz |
| Leader Arrow Size *(opcional)* | `Leader Arrow Size` | Number | item | Tamaño de la flecha de la directriz |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arrow Settings | `Arrow Settings` | Annotation Arrow Settings | item | Ajustes de flechas |
| Arrow 1 | `Arrow 1` | Arrow Type | item | Flecha 1 |
| Arrow 2 | `Arrow 2` | Arrow Type | item | Flecha 2 |
| Arrow Size | `Arrow Size` | Number | item | Tamaño de flecha |
| Fit Arrow | `Fit Arrow` | Integer | item | Ajuste de flechas: 0) Auto: se muestran dentro cuando hay espacio; 1) Forzar flechas dentro de las líneas de extensión; 2) Forzar flechas fuera de las líneas de extensión |
| Dimension Inline | `Dimension Inline` | Boolean | item | Dibuja la línea de cota entre las líneas de extensión si las flechas están fuera |
| Leader Arrow | `Leader Arrow` | Arrow Type | item | Flecha de la directriz |
| Leader Arrow Size | `Leader Arrow Size` | Number | item | Tamaño de la flecha de la directriz |

### Annotation Dimension Settings (AS-Dimension)

Ajustes de cotas del estilo de anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dimension Settings *(opcional)* | `Dimension Settings` | Dimension Settings | item | Ajustes de cotas |
| View Oriented *(opcional)* | `View Oriented` | Boolean | item | Texto orientado a la vista |
| Text Location *(opcional)* | `Text Location` | Integer | item | Ubicación del texto: 0) El texto va sobre la línea de cota; 1) El texto va centrado en la línea de cota |
| Text Rotation *(opcional)* | `Text Rotation` | Integer | item | Rotación del texto: 0) Texto horizontal en el plano del objeto de anotación; 1) Texto alineado con la última dirección de la directriz o con la línea de cota; 2) Texto rotado con un ángulo explícito |
| Radial View Oriented *(opcional)* | `Radial View Oriented` | Boolean | item | Orientación del texto radial horizontal respecto de la vista |
| Radial Text Location *(opcional)* | `Radial Text Location` | Integer | item | Ubicación del texto radial: 0) El texto va sobre la línea de cota; 1) El texto va centrado en la línea de cota |
| Radial Text Rotation *(opcional)* | `Radial Text Rotation` | Integer | item | Rotación del texto radial: 0) Texto horizontal en el plano del objeto de anotación; 1) Texto alineado con la última dirección de la directriz o con la línea de cota; 2) Texto rotado con un ángulo explícito |
| Dimension Line Extension *(opcional)* | `Dimension Line Extension` | Number | item | Extensión de la línea de cota |
| Extension Line Extension *(opcional)* | `Extension Line Extension` | Number | item | Extensión de la línea de extensión |
| Extension Line Offset *(opcional)* | `Extension Line Offset` | Number | item | Desfase de la línea de extensión |
| Fixed Extension *(opcional)* | `Fixed Extension` | Boolean | item | Activar longitud de extensión fija |
| Fixed Extension Length *(opcional)* | `Fixed Extension Length` | Number | item | Longitud de extensión fija |
| Suppress Extension 1 *(opcional)* | `Suppress Extension 1` | Boolean | item | Suprimir extensión 1 |
| Suppress Extension 2 *(opcional)* | `Suppress Extension 2` | Boolean | item | Suprimir extensión 2 |
| Baseline Spacing *(opcional)* | `Baseline Spacing` | Number | item | Separación de la línea base |
| Centermark Size *(opcional)* | `Centermark Size` | Number | item | Tamaño de la marca de centro |
| Centermark Type *(opcional)* | `Centermark Type` | Integer | item | Tipo de marca de centro: 0) Sin marca de centro; 1) Solo marca; 2) Marca y líneas hasta el radio |
| Decimal Separator *(opcional)* | `Decimal Separator` | Text | item | Separador decimal |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dimension Settings | `Dimension Settings` | Dimension Settings | item | Ajustes de cotas |
| View Oriented | `View Oriented` | Boolean | item | Texto orientado a la vista |
| Text Location | `Text Location` | Integer | item | Ubicación del texto: 0) El texto va sobre la línea de cota; 1) El texto va centrado en la línea de cota |
| Text Rotation | `Text Rotation` | Integer | item | Rotación del texto: 0) Texto horizontal en el plano del objeto de anotación; 1) Texto alineado con la última dirección de la directriz o con la línea de cota; 2) Texto rotado con un ángulo explícito |
| Radial View Oriented | `Radial View Oriented` | Boolean | item | Orientación del texto radial horizontal respecto de la vista |
| Radial Text Location | `Radial Text Location` | Integer | item | Ubicación del texto radial: 0) El texto va sobre la línea de cota; 1) El texto va centrado en la línea de cota |
| Radial Text Rotation | `Radial Text Rotation` | Integer | item | Rotación del texto radial: 0) Texto horizontal en el plano del objeto de anotación; 1) Texto alineado con la última dirección de la directriz o con la línea de cota; 2) Texto rotado con un ángulo explícito |
| Dimension Line Extension | `Dimension Line Extension` | Number | item | Extensión de la línea de cota |
| Extension Line Extension | `Extension Line Extension` | Number | item | Extensión de la línea de extensión |
| Extension Line Offset | `Extension Line Offset` | Number | item | Desfase de la línea de extensión |
| Fixed Extension | `Fixed Extension` | Boolean | item | Activar longitud de extensión fija |
| Fixed Extension Length | `Fixed Extension Length` | Number | item | Longitud de extensión fija |
| Suppress Extension 1 | `Suppress Extension 1` | Boolean | item | Suprimir extensión 1 |
| Suppress Extension 2 | `Suppress Extension 2` | Boolean | item | Suprimir extensión 2 |
| Baseline Spacing | `Baseline Spacing` | Number | item | Separación de la línea base |
| Centermark Size | `Centermark Size` | Number | item | Tamaño de la marca de centro |
| Centermark Type | `Centermark Type` | Integer | item | Tipo de marca de centro: 0) Sin marca de centro; 1) Solo marca; 2) Marca y líneas hasta el radio |
| Decimal Separator | `Decimal Separator` | Text | item | Separador decimal |

### Annotation Dot (Dot)

Punto de anotación (dot)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation Dot *(opcional)* | `Annotation Dot` | Text Dot | item | El punto de anotación de Rhino |
| Location *(opcional)* | `Location` | Point | item | Ubicación del punto de anotación |
| Primary Text *(opcional)* | `Primary Text` | Text | item | Texto principal que se muestra en el punto de anotación |
| Text Height *(opcional)* | `Text Height` | Integer | item | Altura del texto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation Dot | `Annotation Dot` | Text Dot | item | El punto de anotación de Rhino |
| Location | `Location` | Point | item | Ubicación del punto de anotación |
| Primary Text | `Primary Text` | Text | item | Texto principal que se muestra en el punto de anotación |
| Text Height | `Text Height` | Integer | item | Altura del texto |

### Annotation Leader Settings (AS-Leaders)

Ajustes de directrices del estilo de anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Leader Settings *(opcional)* | `Leader Settings` | Leader Settings | item | Ajustes de directrices |
| Leader Curve Type *(opcional)* | `Leader Curve Type` | Integer | item | Tipo de curva de la directriz: 0) Ninguna; 1) Polilínea; 2) Spline |
| Has Landing *(opcional)* | `Has Landing` | Boolean | item | Tiene rellano (landing) |
| Landing Length *(opcional)* | `Landing Length` | Number | item | Longitud del rellano |
| View Oriented *(opcional)* | `View Oriented` | Boolean | item | Texto orientado a la vista |
| Horizontal Text Alignment *(opcional)* | `Horizontal Text Alignment` | Integer | item | Alineación horizontal del texto: 0) Izquierda: se ancla a la izquierda de las líneas de texto (independiente de los glifos mostrados); 1) Centro: el punto de anclaje va al centro del avance horizontal del texto (no de la caja de los glifos); 2) Derecha: el punto de anclaje va a la derecha del avance horizontal del texto (no de la caja de los glifos); 3) Auto: solo para directrices; el anclaje se ajusta a derecha o izquierda según la dirección de la cola de la directriz en la vista. Si la cola va a la izquierda, la alineación es a la derecha; si va a la derecha, la alineación es a la izquierda. |
| Vertical Text Alignment *(opcional)* | `Vertical Text Alignment` | Integer | item | Alineación vertical del texto: 0) Arriba: se ancla en la parte superior de una "I" de la primera línea (independiente de los glifos mostrados); 1) Medio de la primera línea: se ancla al medio de una "I" de la primera línea; 2) Base de la primera línea: se ancla a la línea base de la primera línea; 3) Medio: se ancla al medio del avance vertical del texto; 4) Medio de la última línea: se ancla a la línea base de la última línea; 5) Abajo: se ancla a la línea base de la última línea; 6) Base de la caja contenedora: se ancla a la parte inferior de la caja de los glifos visibles. (Las opciones 0 a 5 son independientes de los glifos mostrados.) |
| Leader Text Orientation *(opcional)* | `Leader Text Orientation` | Integer | item | Orientación del texto: 0) Horizontal: el texto es horizontal en el plano del objeto de anotación; 1) Alineado: el texto se alinea con la última dirección de la directriz o con la línea de cota; 2) Personalizado: el texto se rota con un ángulo explícito |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Leader Settings | `Leader Settings` | Leader Settings | item | Ajustes de directrices |
| Leader Curve Type | `Leader Curve Type` | Integer | item | Tipo de curva de la directriz: 0) Ninguna; 1) Polilínea; 2) Spline |
| Has Landing | `Has Landing` | Boolean | item | Tiene rellano (landing) |
| Landing Length | `Landing Length` | Number | item | Longitud del rellano |
| View Oriented | `View Oriented` | Boolean | item | Texto orientado a la vista |
| Horizontal Text Alignment | `Horizontal Text Alignment` | Integer | item | Alineación horizontal del texto: 0) Izquierda: se ancla a la izquierda de las líneas de texto (independiente de los glifos mostrados); 1) Centro: el punto de anclaje va al centro del avance horizontal del texto (no de la caja de los glifos); 2) Derecha: el punto de anclaje va a la derecha del avance horizontal del texto (no de la caja de los glifos); 3) Auto: solo para directrices; el anclaje se ajusta a derecha o izquierda según la dirección de la cola de la directriz en la vista. Si la cola va a la izquierda, la alineación es a la derecha; si va a la derecha, la alineación es a la izquierda. |
| Vertical Text Alignment | `Vertical Text Alignment` | Integer | item | Alineación vertical del texto: 0) Arriba: se ancla en la parte superior de una "I" de la primera línea (independiente de los glifos mostrados); 1) Medio de la primera línea: se ancla al medio de una "I" de la primera línea; 2) Base de la primera línea: se ancla a la línea base de la primera línea; 3) Medio: se ancla al medio del avance vertical del texto; 4) Medio de la última línea: se ancla a la línea base de la última línea; 5) Abajo: se ancla a la línea base de la última línea; 6) Base de la caja contenedora: se ancla a la parte inferior de la caja de los glifos visibles. (Las opciones 0 a 5 son independientes de los glifos mostrados.) |
| Leader Text Orientation | `Leader Text Orientation` | Integer | item | Orientación del texto: 0) Horizontal: el texto es horizontal en el plano del objeto de anotación; 1) Alineado: el texto se alinea con la última dirección de la directriz o con la línea de cota; 2) Personalizado: el texto se rota con un ángulo explícito |

### Annotation Style

Estilo de anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation Style *(opcional)* | `Annotation Style` | Model Annotation Style | item | El estilo de anotación del modelo de Rhino. |
| Name *(opcional)* | `Name` | Text | item | Nombre del estilo de anotación |
| Model Scale *(opcional)* | `Model Scale` | Number | item | Escala del espacio modelo |
| Text Settings *(opcional)* | `Text Settings` | Text Settings | item | Ajustes de texto |
| Dimension Settings *(opcional)* | `Dimension Settings` | Dimension Settings | item | Ajustes de cotas |
| Arrow Settings *(opcional)* | `Arrow Settings` | Annotation Arrow Settings | item | Ajustes de flechas |
| Units Settings *(opcional)* | `Units Settings` | Units Settings | item | Ajustes de unidades |
| Leader Settings *(opcional)* | `Leader Settings` | Leader Settings | item | Ajustes de directrices |
| Tolerance Settings *(opcional)* | `Tolerance Settings` | Tolerance Settings | item | Ajustes de tolerancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation Style | `Annotation Style` | Model Annotation Style | item | El estilo de anotación del modelo de Rhino. |
| Name | `Name` | Text | item | Nombre del estilo de anotación |
| Model Scale | `Model Scale` | Number | item | Escala del espacio modelo |
| Text Settings | `Text Settings` | Text Settings | item | Ajustes de texto |
| Dimension Settings | `Dimension Settings` | Dimension Settings | item | Ajustes de cotas |
| Arrow Settings | `Arrow Settings` | Annotation Arrow Settings | item | Ajustes de flechas |
| Units Settings | `Units Settings` | Units Settings | item | Ajustes de unidades |
| Leader Settings | `Leader Settings` | Leader Settings | item | Ajustes de directrices |
| Tolerance Settings | `Tolerance Settings` | Tolerance Settings | item | Ajustes de tolerancia |

### Annotation Style Overrides (A-Style)

Obtiene/define el estilo de anotación y los atributos reemplazados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation | `Annotation` | Geometry | item | La anotación |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |
| Model Scale *(opcional)* | `Model Scale` | Number | item | Escala del espacio modelo |
| Text Settings *(opcional)* | `Text Settings` | Text Settings | item | Reemplazos de ajustes de texto aplicados a la anotación |
| Dimension Settings *(opcional)* | `Dimension Settings` | Dimension Settings | item | Reemplazos de ajustes de cotas aplicados a la anotación |
| Arrow Settings *(opcional)* | `Arrow Settings` | Annotation Arrow Settings | item | Reemplazos de ajustes de flechas aplicados a la anotación |
| Units Settings *(opcional)* | `Units Settings` | Units Settings | item | Reemplazos de ajustes de unidades aplicados a la anotación |
| Leader Settings *(opcional)* | `Leader Settings` | Leader Settings | item | Reemplazos de ajustes de directrices aplicados a la anotación |
| Tolerance Settings *(opcional)* | `Tolerance Settings` | Tolerance Settings | item | Reemplazos de ajustes de tolerancia aplicados a la anotación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation | `Annotation` | Geometry | item | La anotación |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |
| Model Scale | `Model Scale` | Number | item | Escala del espacio modelo |
| Text Settings | `Text Settings` | Text Settings | item | Reemplazos de ajustes de texto aplicados a la anotación |
| Dimension Settings | `Dimension Settings` | Dimension Settings | item | Reemplazos de ajustes de cotas aplicados a la anotación |
| Arrow Settings | `Arrow Settings` | Annotation Arrow Settings | item | Reemplazos de ajustes de flechas aplicados a la anotación |
| Units Settings | `Units Settings` | Units Settings | item | Reemplazos de ajustes de unidades aplicados a la anotación |
| Leader Settings | `Leader Settings` | Leader Settings | item | Reemplazos de ajustes de directrices aplicados a la anotación |
| Tolerance Settings | `Tolerance Settings` | Tolerance Settings | item | Reemplazos de ajustes de tolerancia aplicados a la anotación |

### Annotation Text Overrides (A-Text)

Gestiona los atributos del texto de la anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation | `Annotation` | Geometry | item | La anotación |
| Text *(opcional)* | `Text` | Text | item | Texto a mostrar en la anotación |
| View Oriented *(opcional)* | `View Oriented` | Boolean | item | Muestra el texto de la anotación siempre orientado a la vista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation | `Annotation` | Geometry | item | La anotación |
| Text | `Text` | Text | item | Texto mostrado en la anotación |
| View Oriented | `View Oriented` | Boolean | item | Muestra el texto de la anotación siempre orientado a la vista |

### Annotation Text Settings (AS-Text)

Ajustes de texto del estilo de anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Settings *(opcional)* | `Text Settings` | Text Settings | item | Ajustes de texto |
| Font *(opcional)* | `Font` | Font | item | Fuente tipográfica |
| Text Height *(opcional)* | `Text Height` | Number | item | Altura del texto |
| Text Gap *(opcional)* | `Text Gap` | Number | item | Separación del texto |
| Mask *(opcional)* | `Mask` | Integer | item | Máscara: 0) Ninguna; 1) Fondo; 2) Color sólido |
| Mask Colour *(opcional)* | `Mask Colour` | Colour | item | Color de la máscara |
| Mask Margins *(opcional)* | `Mask Margins` | Number | item | Márgenes de la máscara |
| Mask Frame *(opcional)* | `Mask Frame` | Integer | item | Marco de la máscara: 0) Ninguno; 1) Rectangular; 2) Cápsula |
| View Oriented *(opcional)* | `View Oriented` | Boolean | item | Texto orientado a la vista |
| Draw Forward *(opcional)* | `Draw Forward` | Boolean | item | El texto se lee al derecho cuando se ve desde atrás |
| Horizontal Alignment *(opcional)* | `Horizontal Alignment` | Integer | item | Alineación horizontal del texto: 0) Izquierda: se ancla a la izquierda de las líneas de texto (independiente de los glifos mostrados); 1) Centro: el punto de anclaje va al centro del avance horizontal del texto (no de la caja de los glifos); 2) Derecha: el punto de anclaje va a la derecha del avance horizontal del texto (no de la caja de los glifos); 3) Auto: solo para directrices; el anclaje se ajusta a derecha o izquierda según la dirección de la cola de la directriz en la vista. Si la cola va a la izquierda, la alineación es a la derecha; si va a la derecha, la alineación es a la izquierda. |
| Vertical Alignment *(opcional)* | `Vertical Alignment` | Integer | item | Alineación vertical del texto: 0) Arriba: se ancla en la parte superior de una "I" de la primera línea; 3) Medio: se ancla al medio del avance vertical del texto; 5) Abajo: se ancla a la línea base de la última línea. (Independiente de los glifos mostrados.) |
| Fit Text *(opcional)* | `Fit Text` | Integer | item | Ajuste del texto: 0) Auto: se muestra dentro cuando hay espacio; 1) Texto dentro: fuerza el texto dentro de las extensiones; 2) Texto a la derecha: lo fuerza fuera, a la derecha de las extensiones; 3) Texto a la izquierda: lo fuerza fuera, a la izquierda de las extensiones; 4) Sugerencia derecha: lo mueve fuera, a la derecha, cuando no cabe dentro; 5) Sugerencia izquierda: lo mueve fuera, a la izquierda, cuando no cabe dentro |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Settings | `Text Settings` | Text Settings | item | Ajustes de texto |
| Font | `Font` | Font | item | Fuente tipográfica |
| Text Height | `Text Height` | Number | item | Altura del texto |
| Text Gap | `Text Gap` | Number | item | Separación del texto |
| Mask | `Mask` | Integer | item | Máscara: 0) Ninguna; 1) Fondo; 2) Color sólido |
| Mask Colour | `Mask Colour` | Colour | item | Color de la máscara |
| Mask Margins | `Mask Margins` | Number | item | Márgenes de la máscara |
| Mask Frame | `Mask Frame` | Integer | item | Marco de la máscara: 0) Ninguno; 1) Rectangular; 2) Cápsula |
| View Oriented | `View Oriented` | Boolean | item | Texto orientado a la vista |
| Draw Forward | `Draw Forward` | Boolean | item | El texto se lee al derecho cuando se ve desde atrás |
| Horizontal Alignment | `Horizontal Alignment` | Integer | item | Alineación horizontal del texto: 0) Izquierda: se ancla a la izquierda de las líneas de texto (independiente de los glifos mostrados); 1) Centro: el punto de anclaje va al centro del avance horizontal del texto (no de la caja de los glifos); 2) Derecha: el punto de anclaje va a la derecha del avance horizontal del texto (no de la caja de los glifos); 3) Auto: solo para directrices; el anclaje se ajusta a derecha o izquierda según la dirección de la cola de la directriz en la vista. Si la cola va a la izquierda, la alineación es a la derecha; si va a la derecha, la alineación es a la izquierda. |
| Vertical Alignment | `Vertical Alignment` | Integer | item | Alineación vertical del texto: 0) Arriba: se ancla en la parte superior de una "I" de la primera línea; 3) Medio: se ancla al medio del avance vertical del texto; 5) Abajo: se ancla a la línea base de la última línea. (Independiente de los glifos mostrados.) |
| Fit Text | `Fit Text` | Integer | item | Ajuste del texto: 0) Auto: se muestra dentro cuando hay espacio; 1) Texto dentro: fuerza el texto dentro de las extensiones; 2) Texto a la derecha: lo fuerza fuera, a la derecha de las extensiones; 3) Texto a la izquierda: lo fuerza fuera, a la izquierda de las extensiones; 4) Sugerencia derecha: lo mueve fuera, a la derecha, cuando no cabe dentro; 5) Sugerencia izquierda: lo mueve fuera, a la izquierda, cuando no cabe dentro |

### Annotation Tolerance Settings (AS-Tolerance)

Ajustes de tolerancia del estilo de anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tolerance Settings *(opcional)* | `Tolerance Settings` | Tolerance Settings | item | Ajustes de tolerancia |
| Tolerance Format *(opcional)* | `Tolerance Format` | Integer | item | Formato de tolerancia: 0) Ninguno: no se muestra tolerancia; 1) Simétrica: tolerancia simétrica +/-; 2) Desviación: distancia +tol, -tol; 3) Límites: distancia con límites superior e inferior |
| Tolerance Resolution *(opcional)* | `Tolerance Resolution` | Integer | item | Resolución de la tolerancia |
| Alt. Tolerance Resolution *(opcional)* | `Alt. Tolerance Resolution` | Integer | item | Resolución alternativa de la tolerancia |
| Tolerance Upper Value *(opcional)* | `Tolerance Upper Value` | Number | item | Valor superior de la tolerancia |
| Tolerance Lower Value *(opcional)* | `Tolerance Lower Value` | Number | item | Valor inferior de la tolerancia |
| Tolerance Height Scale *(opcional)* | `Tolerance Height Scale` | Number | item | Escala de altura de la tolerancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tolerance Settings | `Tolerance Settings` | Tolerance Settings | item | Ajustes de tolerancia |
| Tolerance Format | `Tolerance Format` | Integer | item | Formato de tolerancia: 0) Ninguno: no se muestra tolerancia; 1) Simétrica: tolerancia simétrica +/-; 2) Desviación: distancia +tol, -tol; 3) Límites: distancia con límites superior e inferior |
| Tolerance Resolution | `Tolerance Resolution` | Integer | item | Resolución de la tolerancia |
| Alt. Tolerance Resolution | `Alt. Tolerance Resolution` | Integer | item | Resolución alternativa de la tolerancia |
| Tolerance Upper Value | `Tolerance Upper Value` | Number | item | Valor superior de la tolerancia |
| Tolerance Lower Value | `Tolerance Lower Value` | Number | item | Valor inferior de la tolerancia |
| Tolerance Height Scale | `Tolerance Height Scale` | Number | item | Escala de altura de la tolerancia |

### Annotation Units Settings (AS-Units)

Ajustes de unidades del estilo de anotación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Units Settings *(opcional)* | `Units Settings` | Units Settings | item | Ajustes de unidades |
| Length Units Format *(opcional)* | `Length Units Format` | Integer | item | Formato de unidades de longitud: 0) Unidades del modelo decimales; 1) Pulgadas fraccionarias; 2) Pies y pulgadas fraccionarios; 3) Milímetros decimales; 4) Centímetros decimales; 5) Metros decimales; 6) Kilómetros decimales; 7) Pulgadas decimales; 8) Pies decimales; 9) Millas decimales |
| Length Factor *(opcional)* | `Length Factor` | Number | item | Factor de longitud |
| Linear Resolution *(opcional)* | `Linear Resolution` | Integer | item | Resolución lineal |
| Roundoff *(opcional)* | `Roundoff` | Number | item | Redondeo |
| Prefix *(opcional)* | `Prefix` | Text | item | Prefijo |
| Suffix *(opcional)* | `Suffix` | Text | item | Sufijo |
| Zero Suppression *(opcional)* | `Zero Suppression` | Integer | item | Supresión de ceros en ángulos: 0) Sin supresión de ceros; 1) Suprimir ceros a la izquierda; 2) Suprimir ceros a la derecha; 3) Suprimir ceros a la izquierda y a la derecha; 4) Suprimir cero pies; 8) Suprimir cero pulgadas; 12) Suprimir cero pies y cero pulgadas |
| Fraction Format *(opcional)* | `Fraction Format` | Integer | item | Formato de fracciones: 0) Sin apilar; 1) Apiladas con línea horizontal; 2) Apiladas con línea inclinada |
| Fraction Height Scale *(opcional)* | `Fraction Height Scale` | Number | item | Escala de altura de las fracciones |
| Angular Units Format *(opcional)* | `Angular Units Format` | Integer | item | Formato de unidades angulares: 0) Grados decimales; 1) Grados, minutos, segundos; 2) Radianes decimales; 3) Gradianes decimales |
| Angle Resolution *(opcional)* | `Angle Resolution` | Integer | item | Resolución angular |
| Angle Roundoff *(opcional)* | `Angle Roundoff` | Number | item | Redondeo |
| Angle Zero Suppression *(opcional)* | `Angle Zero Suppression` | Integer | item | Supresión de ceros en ángulos: 0) Sin supresión de ceros; 1) Suprimir ceros a la izquierda; 2) Suprimir ceros a la derecha; 3) Suprimir ceros a la izquierda y a la derecha; 4) Suprimir cero pies; 8) Suprimir cero pulgadas; 12) Suprimir cero pies y cero pulgadas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Units Settings | `Units Settings` | Units Settings | item | Ajustes de unidades |
| Length Units Format | `Length Units Format` | Integer | item | Formato de unidades de longitud: 0) Unidades del modelo decimales; 1) Pulgadas fraccionarias; 2) Pies y pulgadas fraccionarios; 3) Milímetros decimales; 4) Centímetros decimales; 5) Metros decimales; 6) Kilómetros decimales; 7) Pulgadas decimales; 8) Pies decimales; 9) Millas decimales |
| Length Factor | `Length Factor` | Number | item | Factor de longitud |
| Linear Resolution | `Linear Resolution` | Integer | item | Resolución lineal |
| Roundoff | `Roundoff` | Number | item | Redondeo |
| Prefix | `Prefix` | Text | item | Prefijo |
| Suffix | `Suffix` | Text | item | Sufijo |
| Zero Suppression | `Zero Suppression` | Integer | item | Supresión de ceros en ángulos: 0) Sin supresión de ceros; 1) Suprimir ceros a la izquierda; 2) Suprimir ceros a la derecha; 3) Suprimir ceros a la izquierda y a la derecha; 4) Suprimir cero pies; 8) Suprimir cero pulgadas; 12) Suprimir cero pies y cero pulgadas |
| Fraction Format | `Fraction Format` | Integer | item | Formato de fracciones: 0) Sin apilar; 1) Apiladas con línea horizontal; 2) Apiladas con línea inclinada |
| Fraction Height Scale | `Fraction Height Scale` | Number | item | Escala de altura de las fracciones |
| Angular Units Format | `Angular Units Format` | Integer | item | Formato de unidades angulares: 0) Grados decimales; 1) Grados, minutos, segundos; 2) Radianes decimales; 3) Gradianes decimales |
| Angle Resolution | `Angle Resolution` | Integer | item | Resolución angular |
| Angle Roundoff | `Angle Roundoff` | Number | item | Redondeo |
| Angle Zero Suppression | `Angle Zero Suppression` | Integer | item | Supresión de ceros en ángulos: 0) Sin supresión de ceros; 1) Suprimir ceros a la izquierda; 2) Suprimir ceros a la derecha; 3) Suprimir ceros a la izquierda y a la derecha; 4) Suprimir cero pies; 8) Suprimir cero pulgadas; 12) Suprimir cero pies y cero pulgadas |

### Centermark

Marca de centro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centermark *(opcional)* | `Centermark` | Radial Centermark | item | La marca de centro de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Curve *(opcional)* | `Curve` | Curve | item | La curva plana a la que asignar la marca de centro. |
| Parameter *(opcional)* | `Parameter` | Number | item | Parámetro en el dominio de la curva desde el que marcar el centro |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centermark | `Centermark` | Radial Centermark | item | La marca de centro de Rhino |
| Plane | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Center Point | `Center Point` | Point | item | La ubicación de la marca de centro |
| Radius | `Radius` | Number | item | El radio de la curva en el parámetro |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Evaluate Annotation Text (Evaluate)

Obtiene el texto de la anotación con las expresiones de campos de texto evaluadas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation | `Annotation` | Geometry | item | La anotación a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `Text` | Text | item | El texto evaluado de la anotación |

### Leader

Directriz (leader)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Leader *(opcional)* | `Leader` | Leader | item | La directriz de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Curve *(opcional)* | `Curve` | Curve | item | La curva que se convierte en directriz |
| Text *(opcional)* | `Text` | Text | item | El texto usado en la directriz |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Leader | `Leader` | Leader | item | La directriz de Rhino |
| Plane | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Curve | `Curve` | Curve | item | La curva que se convierte en directriz |
| Text | `Text` | Text | item | El texto usado en la directriz |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Linear Dimension (DimLinear)

Cota lineal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linear Dimension *(opcional)* | `Linear Dimension` | Linear Dimension | item | La cota lineal de Rhino |
| Base Line *(opcional)* | `Base Line` | Line | item | Línea base de la cota |
| Point A *(opcional)* | `Point A` | Point | item | Primer punto de la cota |
| Point B *(opcional)* | `Point B` | Point | item | Segundo punto de la cota |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linear Dimension | `Linear Dimension` | Linear Dimension | item | La cota lineal de Rhino |
| Base Line | `Base Line` | Line | item | Línea base de la cota |
| Point A | `Point A` | Point | item | Primer punto de la cota |
| Point B | `Point B` | Point | item | Segundo punto de la cota |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Model Font (Font)

Fuente tipográfica

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Font *(opcional)* | `Font` | Font | item | Definición de fuente del modelo |
| Font Family *(opcional)* | `Font Family` | Text | item | Nombre de la familia tipográfica |
| Font Weight *(opcional)* | `Font Weight` | Integer | item | Peso de la fuente: 0) Sin definir; 1) Thin; 2) Ultralight; 3) Light; 4) Regular; 5) Medium; 6) Semibold; 7) Bold; 8) Ultrabold; 9) Heavy |
| Font Style *(opcional)* | `Font Style` | Integer | item | Estilo de la fuente: 0) Sin definir; 1) Upright (estilo por defecto); 2) Itálica; 3) Oblicua |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Font | `Font` | Font | item | Definición de fuente del modelo |
| Font Family | `Font Family` | Text | item | Nombre de la familia tipográfica |
| Font Weight | `Font Weight` | Integer | item | Peso de la fuente: 0) Sin definir; 1) Thin; 2) Ultralight; 3) Light; 4) Regular; 5) Medium; 6) Semibold; 7) Bold; 8) Ultrabold; 9) Heavy |
| Font Style | `Font Style` | Integer | item | Estilo de la fuente: 0) Sin definir; 1) Upright (estilo por defecto); 2) Itálica; 3) Oblicua |

### Ordinate Dimension (DimOrdinate)

Cota por coordenadas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ordinate Dimension *(opcional)* | `Ordinate Dimension` | Ordinate Dimension | item | La cota por coordenadas de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | El plano base desde el que se mide la cota. |
| Direction *(opcional)* | `Direction` | Integer | item | Dirección de medición: 1) eje X del plano base; 2) eje Y del plano base |
| Feature Location *(opcional)* | `Feature Location` | Point | item | La ubicación del elemento acotado. |
| Dimension Location *(opcional)* | `Dimension Location` | Point | item | La ubicación del extremo de la directriz de la cota por coordenadas |
| Offset 1 *(opcional)* | `Offset 1` | Number | item | Distancia de desfase hasta el primer quiebre de la directriz |
| Offset 2 *(opcional)* | `Offset 2` | Number | item | Distancia de desfase hasta el segundo quiebre de la directriz |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ordinate Dimension | `Ordinate Dimension` | Ordinate Dimension | item | La cota por coordenadas de Rhino |
| Plane | `Plane` | Plane | item | El plano base desde el que se mide la cota. |
| Direction | `Direction` | Integer | item | Dirección de medición: 1) eje X del plano base; 2) eje Y del plano base |
| Feature Location | `Feature Location` | Point | item | La ubicación del elemento acotado. |
| Dimension Location | `Dimension Location` | Point | item | La ubicación del extremo de la directriz de la cota por coordenadas |
| Offset 1 | `Offset 1` | Number | item | Distancia de desfase hasta el primer quiebre de la directriz |
| Offset 2 | `Offset 2` | Number | item | Distancia de desfase hasta el segundo quiebre de la directriz |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Query Annotation Styles (Styles)

Consulta un documento de Rhino para obtener todos los estilos de anotación disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation Styles | `Annotation Styles` | Model Annotation Style | lista | La lista resultante de estilos de anotación disponibles en el modelo. |

### Query Installed Fonts (Fonts)

Consulta todas las fuentes disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Font Family *(opcional)* | `Ff` | Text Pattern | item | Nombre opcional de familia tipográfica para filtrar. Un comodín (*) devuelve todas las fuentes disponibles. |
| Font Weight *(opcional)* | `W` | Integer | item | Valor opcional de peso de fuente para filtrar. |
| Font Style *(opcional)* | `S` | Integer | item | Valor opcional de estilo de fuente para filtrar. |
| Font Stretch *(opcional)* | `St` | Integer | item | Valor opcional de ancho de fuente (stretch) para filtrar. |
| Symbol *(opcional)* | `Sy` | Boolean | item | Símbolo |
| Single Stroke *(opcional)* | `Ss` | Boolean | item | Trazo simple |
| Engraving *(opcional)* | `E` | Boolean | item | Grabado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Font | `F` | Font | lista | La lista resultante de fuentes disponibles |

### Radial Dimension (DimRadial)

Cota radial

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Radial Dimension *(opcional)* | `Radial Dimension` | Radial Dimension | item | La cota radial de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Curve *(opcional)* | `Curve` | Curve | item | La curva plana a la que asignar la cota de radio. |
| Curve Point *(opcional)* | `Curve Point` | Point | item | El punto de la curva desde el que medir el radio o diámetro. Si el punto no está sobre la curva, se usa el punto más cercano de la curva. |
| Dimension Location *(opcional)* | `Dimension Location` | Point | item | La ubicación del extremo de la directriz de la cota. El radio o diámetro se mide en este plano. |
| Dimension Type *(opcional)* | `Dimension Type` | Integer | item | Tipo de cota: 3) Diámetro; 4) Radio |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Radial Dimension | `Radial Dimension` | Radial Dimension | item | La cota radial de Rhino |
| Plane | `Plane` | Plane | item | Plano en el que está esta anotación. |
| Center Point | `Center Point` | Point | item | El punto central de la cota de radio. |
| Curve Point | `Curve Point` | Point | item | El punto de la curva desde el que medir el radio o diámetro. |
| Dimension Location | `Dimension Location` | Point | item | La ubicación del extremo de la directriz de la cota. |
| Dimension Type | `Dimension Type` | Integer | item | Tipo de cota: 3) Diámetro; 4) Radio |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

### Text Entity (Text)

Entidad de texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Entity *(opcional)* | `Text Entity` | Text Entity | item | La entidad de texto de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | Plano en el que está esta entidad de texto |
| Text *(opcional)* | `Text` | Text | item | Texto simple a mostrar en la entidad de texto |
| Style *(opcional)* | `Style` | Model Annotation Style | item | El estilo de anotación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Entity | `Text Entity` | Text Entity | item | La entidad de texto de Rhino |
| Plane | `Plane` | Plane | item | Plano en el que está esta entidad de texto |
| Text | `Text` | Text | item | Texto simple a mostrar en la entidad de texto |
| Style | `Style` | Model Annotation Style | item | El estilo de anotación. |

## Content

### Contains Text Filter (Contains)

Crea un filtro que determina si un texto aparece dentro de otro texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Key | `Key` | Text | item | La clave a usar como criterio de filtrado |
| Text | `Text` | Text | item | El texto en el que buscar |
| Case *(opcional)* | `Case` | Boolean | item | Compara distinguiendo mayúsculas y minúsculas |
| Culture *(opcional)* | `Culture` | Culture | item | Cultura (idioma/región) a usar para comparar textos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter | `Filter` | Predicate | item | Un filtro que determina si un texto aparece dentro de otro texto |

### Content Cache (Cache)

Empuja contenido hacia un modelo de Rhino o lo trae desde él

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content *(opcional)* | `Content` | Model Content | lista | Contenido a guardar en caché |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Model Content | lista | Contenido resultante |

### Content Identity (Identity)

Obtiene algunos detalles sobre la identidad del contenido del modelo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | El contenido del modelo |
| Path *(opcional)* | `Path` | Text | item | El nombre de ruta completo del contenido, con el esquema "Raíz::Padre::Nombre" |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | El contenido del modelo de entrada |
| Id | `Id` | Guid | item | El Id del contenido del modelo |
| Path | `Path` | Text | item | El nombre de ruta completo del contenido, con el esquema "Raíz::Padre::Nombre" |

### Content Information (Information)

Obtiene o define información de los elementos de contenido de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | El contenido del modelo de Rhino |
| Parent *(opcional)* | `Parent` | Text | item | Ruta del padre del contenido. Para anidarlo, usa el esquema "Raíz::Padre"; si no, usa un texto vacío. |
| Name *(opcional)* | `Name` | Text | item | El nombre del contenido |
| Tags *(opcional)* | `Tags` | Text | lista | Las etiquetas del contenido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | El contenido del modelo de Rhino |
| Parent | `Parent` | Text | item | Ruta del padre del contenido. Si está anidado, sigue el esquema "Raíz::Nombre del padre"; si no, es un texto vacío. |
| Name | `Name` | Text | item | El nombre del contenido |
| Tags | `Tags` | Text | lista | Las etiquetas del contenido |

### Convert Units (C-Units)

Realiza una conversión de unidades sobre los datos de entrada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | Datos en las unidades de origen |
| Source | `Source` | Unit System | item | Sistema de unidades de origen |
| Target | `Target` | Unit System | item | Sistema de unidades de destino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | Datos en las unidades de destino |

### Duplicate Content (C-Duplicate)

Duplica el contenido de entrada con una nueva identidad. Borra el Id del contenido actual y opcionalmente permite definir un nuevo padre y nombre.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | Contenido del modelo |
| Name *(opcional)* | `Name` | Text | item | Nuevo nombre del contenido |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | Contenido del modelo |

### Equality Filter (Equals)

Crea un filtro que determina si un valor es igual a otro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Key | `Key` | Text | item | La clave a usar como criterio de filtrado |
| Value | `Value` | Generic Data | item | El valor a comparar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Equal | `Equal` | Predicate | item | Un filtro que determina si un objeto es igual a otro |
| Unequal | `Unequal` | Predicate | item | Un filtro que determina si un objeto no es igual a otro |

### Evaluate Text Fields (Evaluate)

Evalúa las expresiones de campos de un texto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `Text` | Text | item | El texto con expresiones de campos a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `Text` | Text | item | La expresión de texto con formato |
| Values | `Values` | Text | lista | Los valores evaluados de los campos de texto |

### Filter Content (Filter)

Separa contenido según una condición de filtro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | lista | El contenido a filtrar |
| Filter | `Filter` | Predicate | item | Determina el criterio de filtrado que debe cumplir el contenido para incluirse |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | lista | Contenido de entrada filtrado por valor |

### Greater Than Filter (Greater)

Crea un filtro que determina si un valor es mayor que otro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Key | `Key` | Text | item | La clave a usar como criterio de filtrado |
| Value | `Value` | Generic Data | item | El valor a comparar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Greater Than | `Greater Than` | Predicate | item | Un filtro que determina si un valor es mayor que otro |
| … or Equal | `… or Equal` | Predicate | item | Un filtro que determina si un valor es mayor o igual que otro |

### Group Content (Group)

Agrupa contenido por clave

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | lista | El contenido a agrupar |
| Key | `Key` | Text | item | La clave a usar como criterio de agrupación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | árbol | Contenido de entrada agrupado por valor |
| Values | `Values` | Generic Data | lista | La lista ordenada de valores de la clave |

### Import Content (Import)

Importa un modelo desde un archivo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | Ubicación del archivo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `Objects` | Model Object | lista | Objetos importados |
| Layers | `Layers` | Model Layer | lista | Capas importadas |
| Linetypes | `Linetypes` | Model Linetype | lista | Tipos de línea importados |
| Hatch Patterns | `Hatch Patterns` | Model Hatch Pattern | lista | Patrones de sombreado importados |
| Annotation Styles | `Annotation Styles` | Model Annotation Style | lista | Estilos de anotación importados |
| Materials | `Materials` | Model Material | lista | Materiales importados |
| Block Definitions | `Block Definitions` | Model Block Definition | lista | Definiciones de bloque |

### Intersection Filter (Intersection)

Combina varios filtros en una intersección, que devuelve True solo si todos los filtros de entrada se cumplen.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filters | `Filters` | Predicate | lista | Una lista de filtros a intersectar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter | `Filter` | Predicate | item | Un filtro que devuelve True solo si todos los filtros de entrada se cumplen. |

### Less Than Filter (Less)

Crea un filtro que determina si un valor es menor que otro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Key | `Key` | Text | item | La clave a usar como criterio de filtrado |
| Value | `Value` | Generic Data | item | El valor a comparar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Less Than | `Less Than` | Predicate | item | Un filtro que determina si un valor es menor que otro |
| … or Equal | `… or Equal` | Predicate | item | Un filtro que determina si un valor es menor o igual que otro |

### Logical And Filter (And)

Combina dos filtros con un operador lógico AND

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter A | `Filter A` | Predicate | item | El primer filtro |
| Filter B | `Filter B` | Predicate | item | El segundo filtro |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter | `Filter` | Predicate | item | Un filtro combinado que determina si se cumplen el Filtro A y el Filtro B |

### Logical Not Filter (Not)

Crea un filtro como el NOT lógico de otro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter | `Filter` | Predicate | item | El filtro a negar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Not Filter | `Not Filter` | Predicate | item | Un filtro combinado que determina si el filtro de entrada no se cumple |

### Logical Or Filter (Or)

Combina dos filtros con un operador lógico OR.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter A | `Filter A` | Predicate | item | El primer filtro |
| Filter B | `Filter B` | Predicate | item | El segundo filtro |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter | `Filter` | Predicate | item | Un filtro combinado que determina si se cumple el Filtro A o el Filtro B |

### Match Text Filter (Match)

Crea un filtro que determina si un valor de texto coincide con un patrón.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Key | `Key` | Text | item | La clave a usar como criterio de filtrado |
| Pattern | `Pattern` | Text | item | El patrón de texto con el que comparar |
| Case *(opcional)* | `Case` | Boolean | item | Compara distinguiendo mayúsculas y minúsculas |
| Culture *(opcional)* | `Culture` | Culture | item | Cultura (idioma/región) a usar para comparar textos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter | `Filter` | Predicate | item | Un filtro que determina si un texto coincide con un patrón |

### Order Content (Order)

Ordena contenido por clave

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | lista | El contenido a ordenar |
| Key | `Key` | Text | item | La clave a usar como criterio de orden |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | lista | Contenido de entrada ordenado por valor |
| Values | `Values` | Generic Data | lista | La lista ordenada de valores |

### Query Directory (Directory)

Consulta el sistema de archivos bajo la ruta de carpeta indicada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Directory | `Directory` | Text | item | Una ruta de carpeta del sistema de archivos. Las rutas relativas se resuelven desde la carpeta del documento de Grasshopper. |
| Max Depth *(opcional)* | `Max Depth` | Integer | item | Profundidad máxima de consulta dentro de la carpeta de entrada. |
| Name *(opcional)* | `Name` | Text Pattern | item | Un patrón de nombre para filtrar los resultados. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Directory | `Directory` | Text | item | La ruta absoluta de la carpeta en el sistema de archivos |
| Directories | `Directories` | Text | árbol | La lista resultante de subcarpetas disponibles |
| Files | `Files` | Text | árbol | La lista resultante de archivos disponibles |

### Text Field Expression (Field Expression)

Construye una expresión de campo que se puede usar como campo de texto en anotaciones o como valor de texto de usuario.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object | `Object` | Model Object | item | Objeto del que extraer su texto de usuario |
| Key | `Key` | Text | item | Clave del texto de usuario |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Field Expression | `Fe` | Text | item | La expresión de campo de texto con formato |

### Union Filter (Union)

Combina varios filtros en una unión, que devuelve True si al menos un filtro de entrada se cumple.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filters | `Filters` | Predicate | lista | Una lista de filtros a unir. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Filter | `Filter` | Predicate | item | Un filtro que devuelve True si al menos un filtro de entrada se cumple. |

### Unit System (U-System)

Sistema de unidades

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unit System | `Unit System` | Unit System | item | Un sistema de unidades |
| Name *(opcional)* | `Name` | Text | item | El nombre del sistema de unidades. |
| Factor *(opcional)* | `Factor` | Number | item | Factor de unidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unit System | `Unit System` | Unit System | item | Un sistema de unidades |
| Name | `Name` | Text | item | El nombre del sistema de unidades. |
| Meters | `Meters` | Number | item | Metros por unidad |

### User Text (U-Text)

Modifica la colección de textos clave/valor de un elemento del modelo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | Contenido del modelo |
| Keys *(opcional)* | `Keys` | Text | lista | Claves |
| Values *(opcional)* | `Values` | Generic Data | lista | Valores |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Model Content | item | Contenido del modelo |
| Keys | `Keys` | Text | lista | Claves |
| Values | `Values` | Text | lista | Valores |

## Drafting

### Colour Gradient

Degradado de color

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Gradient *(opcional)* | `Gradient` | Colour Gradient | item | Degradado de color |
| Start Point *(opcional)* | `Start Point` | Point | item | Punto inicial del degradado de color |
| End Point *(opcional)* | `End Point` | Point | item | Punto final del degradado de color |
| Repeat *(opcional)* | `Repeat` | Number | item | Factor de repetición del degradado. [1.0, ∞) |
| Type *(opcional)* | `Type` | Integer | item | Tipo de degradado: 0) Sólido; 1) Lineal reflejado; 2) Lineal envolvente; 3) Radial reflejado; 4) Radial envolvente |
| Colours *(opcional)* | `Colours` | Colour Stop | lista | Los puntos de color (color stops) que definen el degradado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Gradient | `Gradient` | Colour Gradient | item | Degradado de color |
| Start Point | `Start Point` | Point | item | Punto inicial del degradado de color |
| End Point | `End Point` | Point | item | Punto final del degradado de color |
| Repeat | `Repeat` | Number | item | Factor de repetición del degradado. |
| Type | `Type` | Integer | item | Tipo de degradado: 0) Sólido; 1) Lineal reflejado; 2) Lineal envolvente; 3) Radial reflejado; 4) Radial envolvente |
| Colours | `Colours` | Colour Stop | lista | Los puntos de color (color stops) que definen el degradado |

### Drafting Scale

Obtiene o define el factor de escala de anotaciones, tipos de línea y/o patrones de sombreado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation Model Scaling *(opcional)* | `Annotation Model Scaling` | Boolean | item | Activa el escalado en espacio modelo de las anotaciones |
| Annotation Layout Scaling *(opcional)* | `Annotation Layout Scaling` | Boolean | item | Activa el escalado en espacio de layout de las anotaciones |
| Hatch Scaling *(opcional)* | `Hatch Scaling` | Boolean | item | Activa el escalado en espacio modelo de los sombreados |
| Hatch Scale *(opcional)* | `Hatch Scale` | Number | item | El factor de escala de los patrones de sombreado en espacio modelo |
| Linetype Scale *(opcional)* | `Linetype Scale` | Number | item | El factor de escala de los tipos de línea en espacio modelo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Annotation Model Scaling | `Annotation Model Scaling` | Boolean | item | Activa el escalado en espacio modelo de las anotaciones |
| Annotation Layout Scaling | `Annotation Layout Scaling` | Boolean | item | Activa el escalado en espacio de layout de las anotaciones |
| Hatch Scaling | `Hatch Scaling` | Boolean | item | Activa el escalado en espacio modelo de los sombreados |
| Hatch Scale | `Hatch Scale` | Number | item | El factor de escala de los patrones de sombreado en espacio modelo |
| Linetype Scale | `Linetype Scale` | Number | item | El factor de escala de los tipos de línea en espacio modelo |

### Export Hatch Pattern (E-Hatch)

Exporta patrones de sombreado a un archivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | Ubicación donde guardar el patrón de sombreado como archivo de Rhino (*.pat). |
| Hatch Patterns | `Hatch Patterns` | Model Hatch Pattern | lista | Lista de patrones de sombreado a exportar |
| Overwrite | `Overwrite` | Boolean | item | Sobrescribir el archivo existente |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | Ruta del archivo de patrones de sombreado |
| Hatch Patterns | `Hatch Patterns` | Model Hatch Pattern | lista | Lista de patrones de sombreado exportados |
| Exported | `Exported` | Boolean | item | Exportado |

### Gradient Colour Stop (Colour Stop)

Punto de color del degradado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color Stop *(opcional)* | `Color Stop` | Colour Stop | item | Un punto de color (color stop) se define por un color en un parámetro dado |
| Colour *(opcional)* | `Colour` | Colour | item | Color |
| Position *(opcional)* | `Position` | Number | item | Parámetro numérico del color [0.0..1.0] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color Stop | `Color Stop` | Colour Stop | item | Un punto de color (color stop) se define por un color en un parámetro dado |
| Colour | `Colour` | Colour | item | Color |
| Position | `Position` | Number | item | Parámetro numérico del color [0.0..1.0] |

### Import Hatch Pattern (I-Hatch)

Importa un patrón de sombreado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | La ruta a un archivo de patrones de sombreado (*.pat). Quita esta entrada para cargar el archivo por defecto "hatchpatterns.txt" |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Patterns | `Hatch Patterns` | Model Hatch Pattern | lista | El patrón de sombreado del modelo de Rhino. |

### Model Hatch (Hatch)

Sombreado del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch *(opcional)* | `Hatch` | Hatch | item | El sombreado de Rhino |
| Boundary *(opcional)* | `Boundary` | Surface | item | La superficie o curva plana que define los bordes del sombreado |
| Plane *(opcional)* | `Plane` | Plane | item | El plano base del patrón de sombreado |
| Hatch Pattern *(opcional)* | `Hatch Pattern` | Model Hatch Pattern | item | Estilo del patrón de sombreado |
| Base Point *(opcional)* | `Base Point` | Point | item | El punto base del patrón de sombreado |
| Rotation *(opcional)* | `Rotation` | Number | item | Rotación del patrón |
| Scale *(opcional)* | `Scale` | Number | item | Escala del patrón |
| Show Boundary *(opcional)* | `Show Boundary` | Boolean | item | Mostrar el borde |
| Background *(opcional)* | `Background` | Colour | item | Color de fondo |
| Fill Style *(opcional)* | `Fill Style` | Colour Gradient | item | Estilo de relleno |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch | `Hatch` | Hatch | item | El sombreado de Rhino |
| Boundary | `Boundary` | Curve | lista | Las curvas planas que definen los bordes del sombreado |
| Plane | `Plane` | Plane | item | El plano base del patrón de sombreado |
| Hatch Pattern | `Hatch Pattern` | Model Hatch Pattern | item | Estilo del patrón de sombreado |
| Base Point | `Base Point` | Point | item | El punto base del patrón de sombreado |
| Rotation | `Rotation` | Number | item | Rotación del patrón |
| Scale | `Scale` | Number | item | Escala del patrón |
| Show Boundary | `Show Boundary` | Boolean | item | Mostrar el borde |
| Background | `Background` | Colour | item | Color de fondo |
| Fill Style | `Fill Style` | Colour Gradient | item | Estilo de relleno |

### Model Hatch Line (Hatch Line)

Línea de sombreado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Line *(opcional)* | `Hatch Line` | Hatch Line | item | La línea del patrón de sombreado. |
| Start *(opcional)* | `Start` | Point | item | El punto inicial de la línea de sombreado. |
| Direction *(opcional)* | `Direction` | Vector | item | La dirección tangente de la línea de sombreado. |
| Shift *(opcional)* | `Shift` | Number | item | Define el desplazamiento 2D de esta línea para las repeticiones de segmentos: el corrimiento del patrón de una línea a otra. |
| Offset *(opcional)* | `Offset` | Number | item | Define el desfase 2D de esta línea para las repeticiones de línea: la distancia entre cada repetición de la línea que estás definiendo. |
| Segments *(opcional)* | `Segments` | Number | lista | Una lista de longitudes de segmento. Los valores positivos se interpretan como línea y los negativos como espacio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Line | `Hatch Line` | Hatch Line | item | La línea del patrón de sombreado. |
| Start | `Start` | Point | item | El punto inicial de la línea de sombreado. |
| Direction | `Direction` | Vector | item | La dirección tangente de la línea de sombreado. |
| Shift | `Shift` | Number | item | Define el desplazamiento 2D de esta línea para las repeticiones de segmentos: el corrimiento del patrón de una línea a otra. |
| Offset | `Offset` | Number | item | Define el desfase 2D de esta línea para las repeticiones de línea: la distancia entre cada repetición de la línea que estás definiendo. |
| Segments | `Segments` | Number | lista | Una lista de longitudes de segmento. Los valores positivos se interpretan como línea y los negativos como espacio. |

### Model Hatch Pattern (Hatch Pattern)

Patrón de sombreado del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Pattern *(opcional)* | `Hatch Pattern` | Model Hatch Pattern | item | El patrón de sombreado del modelo de Rhino. |
| Name *(opcional)* | `Name` | Text | item | El nombre del patrón de sombreado |
| Hatch Lines *(opcional)* | `Hatch Lines` | Hatch Line | lista | Una lista de líneas de sombreado que definen el patrón. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Pattern | `Hatch Pattern` | Model Hatch Pattern | item | El patrón de sombreado del modelo de Rhino. |
| Name | `Name` | Text | item | El nombre del patrón de sombreado |
| Hatch Lines | `Hatch Lines` | Hatch Line | lista | Una lista de líneas de sombreado que definen el patrón. |

### Model Linetype (Linetype)

Tipo de línea del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linetype *(opcional)* | `Linetype` | Model Linetype | item | El tipo de línea del modelo de Rhino |
| Name *(opcional)* | `Name` | Text | item | El nombre del tipo de línea |
| Segments *(opcional)* | `Segments` | Number | lista | Una lista de longitudes de segmento en milímetros. Los valores positivos se interpretan como línea y los negativos como espacio. Si se deja vacía o sin definir, el tipo de línea es continuo. |
| Cap Style *(opcional)* | `Cap Style` | Integer | item | Estilo de remate: 0) Redondo; 1) Plano; 2) Cuadrado |
| Join Style *(opcional)* | `Join Style` | Integer | item | Estilo de unión: 0) Redonda; 1) Inglete; 2) Bisel |
| Width *(opcional)* | `Width` | Number | item | El ancho del tipo de línea cuando no hay puntos de ahusamiento definidos |
| Width Units *(opcional)* | `Width Units` | Unit System | item | Los valores de ancho de línea usan estas unidades para determinar el tamaño de la línea en pantalla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linetype | `Linetype` | Model Linetype | item | El tipo de línea del modelo de Rhino |
| Name | `Name` | Text | item | El nombre del tipo de línea |
| Segments | `Segments` | Number | lista | Una lista de longitudes de segmento en milímetros. Los valores positivos se interpretan como línea y los negativos como espacio. Si el parámetro está vacío o sin definir, la línea es continua. |
| Cap Style | `Cap Style` | Integer | item | Estilo de remate: 0) Redondo; 1) Plano; 2) Cuadrado |
| Join Style | `Join Style` | Integer | item | Estilo de unión: 0) Redonda; 1) Inglete; 2) Bisel |
| Width | `Width` | Number | item | El ancho del tipo de línea cuando no hay puntos de ahusamiento definidos |
| Width Units | `Width Units` | Unit System | item | Los valores de ancho de línea usan estas unidades para determinar el tamaño de la línea en pantalla. |

### Query Model Hatch Patterns (Hatches)

Consulta un documento de Rhino para obtener todos los patrones de sombreado disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Patterns | `Hatch Patterns` | Model Hatch Pattern | lista | La lista resultante de patrones de sombreado disponibles en el modelo. |

### Query Model Linetypes (Linetypes)

Consulta un documento de Rhino para obtener todos los tipos de línea disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linetypes | `Linetypes` | Model Linetype | lista | La lista resultante de tipos de línea disponibles en el modelo. |

## Model

### Explode Object (Explode)

Explota un objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object | `Object` | Model Object | item | Objeto del modelo a explotar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `Objects` | Model Object | lista | Objetos del modelo explotados |

### Export Model Block Definition (E-Block)

Exporta una definición de bloque como archivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definition | `Block Definition` | Model Block Definition | item | Definición de bloque |
| File Path | `File Path` | Text | item | Ubicación donde guardar la definición de bloque como archivo. |
| Overwrite | `Overwrite` | Boolean | item | Sobrescribir el archivo existente |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definition | `Block Definition` | Model Block Definition | item | Definición de bloque |
| File Path | `File Path` | Text | item | Ruta del archivo exportado |
| Exported | `Exported` | Boolean | item | Exportado |

### Hide Model Layer (L-Hide)

Define la visibilidad de capas para las vistas del modelo y los detalles nuevos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer | `Layer` | Model Layer | item | Capa del modelo |
| Model *(opcional)* | `Model` | Boolean | item | Define si la(s) capa(s) de entrada están ocultas en el modelo |
| New Detail *(opcional)* | `New Detail` | Boolean | item | Define si la(s) capa(s) de entrada están ocultas en los detalles nuevos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer | `Layer` | Model Layer | item | Capa del modelo |
| Model | `Model` | Boolean | item | Define si la(s) capa(s) de entrada están ocultas en el modelo |
| New Detail | `New Detail` | Boolean | item | Define si la(s) capa(s) de entrada están ocultas en los detalles nuevos |

### Import Model Block Definition (I-Block)

Importa un archivo y crea una nueva definición de bloque.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | Ubicación del archivo a usar para la definición de bloque. |
| Update Type | `Update Type` | Integer | item | Tipo de actualización de la definición de bloque: 0) Incrustado; 2) Vinculado e incrustado; 3) Vinculado |
| Name *(opcional)* | `Name` | Text | item | El nombre de la definición de bloque. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definition | `Block Definition` | Model Block Definition | item | Definición de bloque |

### Model Block Definition (Block Definition)

Definición de bloque

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definition *(opcional)* | `Block Definition` | Model Block Definition | item | Definición de bloque del modelo |
| Objects *(opcional)* | `Objects` | Model Object | lista | Objetos del modelo que definen el bloque. |
| Name *(opcional)* | `Name` | Text | item | El nombre de la definición de bloque. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definition | `Block Definition` | Model Block Definition | item | Definición de bloque del modelo |
| Objects | `Objects` | Model Object | lista | Objetos del modelo que definen el bloque. |
| Name | `Name` | Text | item | El nombre de la definición de bloque. |

### Model Block Instance (Block Instance)

Instancia de bloque

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Instance *(opcional)* | `Block Instance` | Block Instance | item | Instancia de bloque |
| Transform *(opcional)* | `Transform` | Transform | item | Transformación aplicada a la geometría de la definición de bloque. También se aceptan Point y Plane. |
| Block Definition *(opcional)* | `Block Definition` | Model Block Definition | item | Definición de bloque |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Instance | `Block Instance` | Block Instance | item | Instancia de bloque |
| Transform | `Transform` | Transform | item | Transformación aplicada a la geometría de la definición de bloque. Transform también se convierte a Point y Plane. |
| Block Definition | `Block Definition` | Model Block Definition | item | Definición de bloque |

### Model Earth Location (Earth Location)

Asocia una ubicación y orientación del modelo con valores de latitud, longitud y elevación en la Tierra.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location *(opcional)* | `Location` | Earth Location | item | Ubicación terrestre |
| Name *(opcional)* | `Name` | Text | item | Nombre de esta ubicación terrestre |
| Anchor *(opcional)* | `Anchor` | Plane | item | Plano en coordenadas del modelo a asociar con los valores de longitud, latitud y elevación. El origen del plano representa el punto base del modelo, y los ejes X e Y representan las direcciones Este y Norte respectivamente |
| Latitude *(opcional)* | `Latitude` | Number | item | Latitud en la Tierra. -90 = polo sur, 0 = ecuador, +90 = polo norte |
| Longitude *(opcional)* | `Longitude` | Number | item | Longitud en la Tierra. [-180, +180] |
| Elevation *(opcional)* | `Elevation` | Number | item | Elevación en la Tierra, en unidades del modelo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `Location` | Earth Location | item | Ubicación terrestre |
| Name | `Name` | Text | item | Nombre de esta ubicación terrestre |
| Anchor | `Anchor` | Plane | item | Plano en coordenadas del modelo a asociar con los valores de longitud, latitud y elevación. El origen del plano representa el punto base del modelo, y los ejes X e Y representan las direcciones Este y Norte respectivamente |
| Latitude | `Latitude` | Number | item | Latitud en la Tierra. -90 = polo sur, 0 = ecuador, +90 = polo norte |
| Longitude | `Longitude` | Number | item | Longitud en la Tierra. [-180, +180] |
| Elevation | `Elevation` | Number | item | Elevación en la Tierra, en unidades del modelo. |

### Model Layer (Layer)

Capa del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer *(opcional)* | `Layer` | Model Layer | item | Definición de capa del modelo |
| Name *(opcional)* | `Name` | Text | item | Nombre de la capa |
| Hidden *(opcional)* | `Hidden` | Boolean | item | Oculta |
| Locked *(opcional)* | `Locked` | Boolean | item | Bloqueada |
| Display Colour *(opcional)* | `Display Colour` | Colour | item | Color de visualización |
| Material *(opcional)* | `Material` | Model Material | item | Material de la capa |
| Linetype *(opcional)* | `Linetype` | Model Linetype | item | Tipo de línea |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer | `Layer` | Model Layer | item | Definición de capa del modelo |
| Name | `Name` | Text | item | Nombre de la capa |
| Hidden | `Hidden` | Boolean | item | Oculta |
| Locked | `Locked` | Boolean | item | Bloqueada |
| Display Colour | `Display Colour` | Colour | item | Color de visualización |
| Material | `Material` | Model Material | item | Material de la capa |
| Linetype | `Linetype` | Model Linetype | item | Tipo de línea |

### Query Model Block Definitions (Block Definitions)

Consulta un documento de Rhino para obtener todas las definiciones de bloque disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definitions | `Block Definitions` | Model Block Definition | lista | La lista resultante de definiciones de bloque disponibles en el modelo. |

### Query Model Layers (Layers)

Consulta un documento de Rhino para obtener todas las capas disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layers | `Layers` | Model Layer | lista | La lista resultante de capas disponibles en el modelo. |

### Query Model Location (Model Location)

Consulta un documento de Rhino para obtener su ubicación terrestre

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `Location` | Earth Location | item | La ubicación terrestre del modelo |

## Objects

### Display Attributes (Display)

Atributos de visualización del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Display *(opcional)* | `Display` | Display Attributes | item | Atributos de visualización del objeto |
| Display Colour *(opcional)* | `Display Colour` | Display Colour | item | Color de visualización del objeto |
| Display Mode *(opcional)* | `Display Mode` | Display Mode | item | Modo de visualización del objeto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Display | `Display` | Display Attributes | item | Atributos de visualización del objeto |
| Display Colour | `Display Colour` | Display Colour | item | Color de visualización del objeto |
| Display Mode | `Display Mode` | Display Mode | item | Modo de visualización del objeto |

### Display Colour

Atributos de color de visualización del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Display Colour *(opcional)* | `Display Colour` | Display Colour | item | Color de visualización del objeto |
| Source *(opcional)* | `Source` | Integer | item | Fuente del color: 0) Por capa; 1) Por objeto; 2) Por material; 3) Por padre |
| Colour *(opcional)* | `Colour` | Colour | item | Color |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Display Colour | `Display Colour` | Display Colour | item | Color de visualización del objeto |
| Source | `Source` | Integer | item | Fuente del color: 0) Por capa; 1) Por objeto; 2) Por material; 3) Por padre |
| Colour | `Colour` | Colour | item | Color |

### Drafting Attributes (Drafting)

Atributos de dibujo del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Drafting *(opcional)* | `Drafting` | Drafting Attributes | item | Atributos de dibujo del objeto |
| Linetype *(opcional)* | `Linetype` | Linetype | item | Tipo de línea del objeto |
| Linetype Scale *(opcional)* | `Linetype Scale` | Number | item | Escala del tipo de línea del objeto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Drafting | `Drafting` | Drafting Attributes | item | Atributos de dibujo del objeto |
| Linetype | `Linetype` | Linetype | item | Tipo de línea del objeto |
| Linetype Scale | `Linetype Scale` | Number | item | Escala del tipo de línea del objeto |

### Model Object (Object)

Objeto del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object *(opcional)* | `Object` | Model Object | item | Objeto del modelo |
| Geometry *(opcional)* | `Geometry` | Geometry | item | Geometría |
| Name *(opcional)* | `Name` | Text | item | Nombre |
| Layer *(opcional)* | `Layer` | Model Layer | item | Capa |
| Visibility *(opcional)* | `Visibility` | Visibility Attributes | item | Visibilidad |
| Display *(opcional)* | `Display` | Display Attributes | item | Atributos de visualización |
| Drafting *(opcional)* | `Drafting` | Drafting Attributes | item | Atributos de dibujo |
| Render *(opcional)* | `Render` | Render Attributes | item | Atributos de render |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object | `Object` | Model Object | item | Objeto del modelo |
| Geometry | `Geometry` | Geometry | item | Geometría |
| Name | `Name` | Text | item | Nombre |
| Layer | `Layer` | Model Layer | item | Capa |
| Visibility | `Visibility` | Visibility Attributes | item | Visibilidad |
| Display | `Display` | Display Attributes | item | Atributos de visualización |
| Drafting | `Drafting` | Drafting Attributes | item | Atributos de dibujo |
| Render | `Render` | Render Attributes | item | Atributos de render |

### Object Linetype

Atributos de tipo de línea del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linetype *(opcional)* | `Linetype` | Linetype | item | Tipo de línea del objeto |
| Source *(opcional)* | `Source` | Integer | item | Fuente del tipo de línea: 0) Por capa; 1) Por objeto; 3) Por padre |
| Model Linetype *(opcional)* | `Model Linetype` | Model Linetype | item | El tipo de línea del modelo de Rhino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linetype | `Linetype` | Linetype | item | Tipo de línea del objeto |
| Source | `Source` | Integer | item | Fuente del tipo de línea: 0) Por capa; 1) Por objeto; 3) Por padre |
| Model Linetype | `Model Linetype` | Model Linetype | item | El tipo de línea del modelo de Rhino |

### Print Colour

Atributos de color de impresión del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Print Colour *(opcional)* | `Print Colour` | Print Colour | item | Color de impresión del objeto |
| Source *(opcional)* | `Source` | Integer | item | Fuente del color: 0) Por capa; 1) Por objeto; 2) Por visualización; 3) Por padre |
| Colour *(opcional)* | `Colour` | Colour | item | Color |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Print Colour | `Print Colour` | Print Colour | item | Color de impresión del objeto |
| Source | `Source` | Integer | item | Fuente del color: 0) Por capa; 1) Por objeto; 2) Por visualización; 3) Por padre |
| Colour | `Colour` | Colour | item | Color |

### Print Width

Atributos de grosor de impresión del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Print Width *(opcional)* | `Print Width` | Print Width | item | Grosor de impresión del objeto |
| Source *(opcional)* | `Source` | Integer | item | Fuente del grosor de impresión: 0) Por capa; 1) Por objeto; 3) Por padre |
| Width *(opcional)* | `Width` | Print Width | item | Grosor de impresión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Print Width | `Print Width` | Print Width | item | Grosor de impresión del objeto |
| Source | `Source` | Integer | item | Fuente del grosor de impresión: 0) Por capa; 1) Por objeto; 3) Por padre |
| Width | `Width` | Print Width | item | Grosor de impresión |

### Query Model Objects (M-Objects)

Consulta un documento de Rhino para obtener todos los objetos del modelo disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro opcional por nombre de objeto. Clic derecho sobre este parámetro para definir el método de coincidencia. |
| Layer *(opcional)* | `Layer` | Text Pattern | item | Filtro opcional por nombre de capa. Clic derecho sobre este parámetro para definir el método de coincidencia. |
| Group *(opcional)* | `Group` | Text Pattern | item | Filtro opcional por nombre de grupo. Clic derecho sobre este parámetro para definir el método de coincidencia. |
| Locked | `Locked` | Boolean | item | Incluir objetos bloqueados. |
| Hidden | `Hidden` | Boolean | item | Incluir objetos ocultos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `Objects` | Model Object | lista | La lista resultante de objetos de Rhino disponibles. |

### Render Attributes (Render)

Atributos de render del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Render *(opcional)* | `Render` | Render Attributes | item | Atributos de render del objeto |
| Object Material *(opcional)* | `Object Material` | Object Material | item | Material de render del objeto |
| Casts Shadows *(opcional)* | `Casts Shadows` | Boolean | item | Proyecta sombras |
| Receives Shadows *(opcional)* | `Receives Shadows` | Boolean | item | Recibe sombras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Render | `Render` | Render Attributes | item | Atributos de render del objeto |
| Object Material | `Object Material` | Object Material | item | Material de render del objeto |
| Casts Shadows | `Casts Shadows` | Boolean | item | Proyecta sombras |
| Receives Shadows | `Receives Shadows` | Boolean | item | Recibe sombras |

### Render Material (Object Material)

Atributos de material de render del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object Material *(opcional)* | `Object Material` | Object Material | item | Material de render del objeto |
| Source *(opcional)* | `Source` | Integer | item | Fuente del material: 0) Por capa; 1) Por objeto; 3) Por padre |
| Material *(opcional)* | `Material` | Model Material | item | Material del modelo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object Material | `Object Material` | Object Material | item | Material de render del objeto |
| Source | `Source` | Integer | item | Fuente del material: 0) Por capa; 1) Por objeto; 3) Por padre |
| Material | `Material` | Model Material | item | Material del modelo |

### Visibility Attributes (Visibility)

Atributos de visibilidad del objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Visibility *(opcional)* | `Visibility` | Visibility Attributes | item | Visibilidad |
| Hidden *(opcional)* | `Hidden` | Boolean | item | Oculta |
| Locked *(opcional)* | `Locked` | Boolean | item | Bloqueada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Visibility | `Visibility` | Visibility Attributes | item | Visibilidad |
| Hidden | `Hidden` | Boolean | item | Oculta |
| Locked | `Locked` | Boolean | item | Bloqueada |

## Render

### Directional Light (D-Light)

Luz direccional

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Directional Light *(opcional)* | `Directional Light` | Light | item | La luz direccional |
| Location *(opcional)* | `Location` | Point | item | Ubicación de la luz direccional |
| Direction *(opcional)* | `Direction` | Vector | item | Dirección de los rayos de luz |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Directional Light | `Directional Light` | Light | item | La luz direccional |
| Location | `Location` | Point | item | Ubicación de la luz direccional |
| Direction | `Direction` | Vector | item | Dirección de los rayos de luz |

### Import Model Environment (I-Environment)

Importa un entorno del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | La ruta a un archivo de entorno de Rhino (*.renv). Las rutas relativas se resuelven usando la carpeta de soporte de Rhino. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Environment | `Environment` | Model Environment | item | El entorno del modelo de Rhino. |

### Import Model Material (I-Material)

Importa un material del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | La ruta a un archivo de material de Rhino (*.rmtl). Las rutas relativas se resuelven usando la carpeta de soporte de Rhino. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `Material` | Model Material | item | El material del modelo de Rhino. |

### Light Attributes (Light)

Modifica o inspecciona los atributos de una luz.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Light | `Light` | Light | item | La luz |
| Enabled *(opcional)* | `Enabled` | Boolean | item | Define si la luz está encendida (True) o apagada (False) |
| Colour *(opcional)* | `Colour` | Colour | item | Color difuso |
| Intensity *(opcional)* | `Intensity` | Number | item | Intensidad de la luz [0.0..∞) |
| Shadow Intensity *(opcional)* | `Shadow Intensity` | Number | item | Intensidad de la sombra [0.0..1.0] |
| Falloff *(opcional)* | `Falloff` | Integer | item | Atenuación: 0) Constante; 1) Lineal; 2) Cuadrática inversa |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Light | `Light` | Light | item | La luz |
| Enabled | `Enabled` | Boolean | item | Define si la luz está encendida (True) o apagada (False) |
| Colour | `Colour` | Colour | item | Color difuso |
| Intensity | `Intensity` | Number | item | Intensidad de la luz [0.0..∞) |
| Shadow Intensity | `Shadow Intensity` | Number | item | Intensidad de la sombra [0.0..1.0] |
| Falloff | `Falloff` | Integer | item | Atenuación: 0) Constante; 1) Lineal; 2) Cuadrática inversa |

### Linear Light

Luz lineal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linear Light *(opcional)* | `Linear Light` | Light | item | La luz lineal de Rhino |
| Line *(opcional)* | `Line` | Line | item | El eje del cilindro de la luz lineal |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linear Light | `Linear Light` | Light | item | La luz lineal de Rhino |
| Line | `Line` | Line | item | El eje del cilindro de la luz lineal |

### Model Basic Environment (Basic Environment)

Entorno básico del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Environment *(opcional)* | `Environment` | Model Environment | item | Entorno básico |
| Name *(opcional)* | `Name` | Text | item | Nombre |
| Background Colour *(opcional)* | `Background Colour` | Colour | item | Color de fondo |
| Projection *(opcional)* | `Projection` | Integer | item | Proyección: 0) Plana; 1) Esférica; 2) Mapa de entorno (Emap); 3) Caja; 4) Automática; 5) Light Probe; 6) Cube Map; 7) Cube Map en cruz vertical; 8) Cube Map en cruz horizontal; 9) Hemisférica |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Environment | `Environment` | Model Environment | item | Entorno básico |
| Name | `Name` | Text | item | Nombre |
| Background Colour | `Background Colour` | Colour | item | Color de fondo |
| Projection | `Projection` | Integer | item | Proyección: 0) Plana; 1) Esférica; 2) Mapa de entorno (Emap); 3) Caja; 4) Automática; 5) Light Probe; 6) Cube Map; 7) Cube Map en cruz vertical; 8) Cube Map en cruz horizontal; 9) Hemisférica |

### Model Material (Material)

Material del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material *(opcional)* | `Material` | Model Material | item | El material del modelo de Rhino |
| Name *(opcional)* | `Name` | Text | item | El nombre del material |
| Shader *(opcional)* | `Shader` | Shader | item | El material de visualización (es decir, el sombreador) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `Material` | Model Material | item | El material del modelo de Rhino. |
| Name | `Name` | Text | item | El nombre del material |
| Shader | `Shader` | Shader | item | El material de visualización (es decir, el sombreador) |

### Point Light

Luz puntual

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point Light *(opcional)* | `Point Light` | Light | item | La luz puntual de Rhino |
| Location *(opcional)* | `Location` | Point | item | Ubicación de la luz puntual |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point Light | `Point Light` | Light | item | La luz puntual de Rhino |
| Location | `Location` | Point | item | Ubicación de la luz puntual |

### Query Model Environments (Environments)

Consulta un documento de Rhino para obtener todos los entornos de render disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Environments | `Environments` | Model Environment | lista | La lista resultante de entornos disponibles en el modelo. |

### Query Model Lights (Lights)

Consulta un documento de Rhino para obtener todas las luces disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |
| Layer *(opcional)* | `Layer` | Text Pattern | item | Filtro opcional por nombre de capa. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lights | `Lights` | Model Object | lista | La lista resultante de luces disponibles en el modelo. |

### Query Model Materials (Materials)

Consulta un documento de Rhino para obtener todos los materiales de render disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Materials | `Materials` | Model Material | lista | La lista resultante de materiales disponibles en el modelo. |

### Query Render Options (Render)

Consulta un documento de Rhino para obtener sus opciones de render

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sun | `Sun` | Model Content | item | La luz solar de Rhino |
| Skylight | `Skylight` | Model Content | item | La luz de cielo (skylight) de Rhino |

### Rectangular Light

Luz rectangular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangular Light *(opcional)* | `Rectangular Light` | Light | item | La luz rectangular de Rhino |
| Plane *(opcional)* | `Plane` | Plane | item | El plano de la luz rectangular |
| Length *(opcional)* | `Length` | Number | item | Dimensión de largo de la luz rectangular |
| Width *(opcional)* | `Width` | Number | item | Dimensión de ancho de la luz rectangular |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangular Light | `Rectangular Light` | Light | item | La luz rectangular de Rhino |
| Plane | `Plane` | Plane | item | El plano de la luz rectangular |
| Length | `Length` | Number | item | Dimensión de largo de la luz rectangular |
| Width | `Width` | Number | item | Dimensión de ancho de la luz rectangular |

### Skylight

La luz de cielo (skylight) de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Skylight *(opcional)* | `Skylight` | Model Content | item | La luz de cielo (skylight) de Rhino |
| Enabled *(opcional)* | `Enabled` | Boolean | item | Define si la luz de cielo está encendida (True) o apagada (False) |
| Custom Environment *(opcional)* | `Custom Environment` | Boolean | item | Define si la luz de cielo usa un entorno personalizado para los reflejos. |
| Environment *(opcional)* | `Environment` | Model Environment | item | Entorno de la luz de cielo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Skylight | `Skylight` | Model Content | item | La luz de cielo (skylight) de Rhino |
| Enabled | `Enabled` | Boolean | item | Define si la luz de cielo está encendida (True) o apagada (False) |
| Custom Environment | `Custom Environment` | Boolean | item | Define si la luz de cielo usa un entorno personalizado para los reflejos. |
| Environment | `Environment` | Model Environment | item | Entorno de la luz de cielo |

### Spotlight

Foco (spotlight)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Spotlight *(opcional)* | `Spotlight` | Light | item | El foco de Rhino |
| Location *(opcional)* | `Location` | Point | item | Ubicación del foco |
| Target *(opcional)* | `Target` | Point | item | Ubicación del objetivo del foco |
| Spotlight Hardness *(opcional)* | `Spotlight Hardness` | Number | item | Dureza del foco [0.0..1.0] |
| Spotlight Angle *(opcional)* | `Spotlight Angle` | Number | item | Ángulo del foco [0..π/2.0] o [0°..90°] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Spotlight | `Spotlight` | Light | item | El foco de Rhino |
| Location | `Location` | Point | item | Ubicación del foco |
| Target | `Target` | Point | item | Ubicación del objetivo del foco |
| Spotlight Hardness | `Spotlight Hardness` | Number | item | Dureza del foco [0.0..1.0] |
| Spotlight Angle | `Spotlight Angle` | Number | item | Ángulo del foco [0..π/2.0] o [0°..90°] |

### Sun

Sol a partir de un punto de anclaje terrestre y una fecha/hora.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sun *(opcional)* | `Sun` | Model Content | item | El sol de Rhino |
| Enabled *(opcional)* | `Enabled` | Boolean | item | Define si el sol está encendido (True) o apagado (False) |
| Intensity *(opcional)* | `Intensity` | Number | item | Intensidad de la luz |
| Date Time *(opcional)* | `Date Time` | Time | item | La fecha y hora del observador. Ojo: se guardan como hora solar local, es decir, la hora que ves en la interfaz de Rhino en 'Local'. |
| Latitude *(opcional)* | `Latitude` | Number | item | Latitud en la Tierra. +90 = polo norte, 0 = ecuador, -90 = polo sur |
| Longitude *(opcional)* | `Longitude` | Number | item | Longitud en la Tierra. [-180..+180] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sun | `Sun` | Model Content | item | El sol de Rhino |
| Enabled | `Enabled` | Boolean | item | Define si el sol está encendido (True) o apagado (False) |
| Intensity | `Intensity` | Number | item | Intensidad de la luz |
| Date Time | `Date Time` | Time | item | La fecha y hora del observador. Ojo: se guardan como hora solar local, es decir, la hora que ves en la interfaz de Rhino en 'Local'. |
| Latitude | `Latitude` | Number | item | Latitud en la Tierra. +90 = polo norte, 0 = ecuador, -90 = polo sur |
| Longitude | `Longitude` | Number | item | Longitud en la Tierra. [-180..+180] |

### Sun (Manual Control) (Sun)

Sol a partir del ángulo del norte y los valores de azimut y altitud.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sun *(opcional)* | `Sun` | Model Content | item | El sol de Rhino |
| Enabled *(opcional)* | `Enabled` | Boolean | item | Define si el sol está encendido (True) o apagado (False) |
| Intensity *(opcional)* | `Intensity` | Number | item | Intensidad de la luz |
| Azimuth *(opcional)* | `Azimuth` | Number | item | El ángulo de azimut: el ángulo de brújula medido desde el norte. [0..+360] |
| Altitude *(opcional)* | `Altitude` | Number | item | El ángulo de altitud: el ángulo sobre el plano del suelo. [-90..+90] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sun | `Sun` | Model Content | item | El sol de Rhino |
| Enabled | `Enabled` | Boolean | item | Define si el sol está encendido (True) o apagado (False) |
| Intensity | `Intensity` | Number | item | Intensidad de la luz |
| Azimuth | `Azimuth` | Number | item | El ángulo de azimut: el ángulo de brújula medido desde el norte. [0..+360] |
| Altitude | `Altitude` | Number | item | El ángulo de altitud: el ángulo sobre el plano del suelo. [-90..+90] |

### Sun Preview (S-Preview)

Previsualiza un sol o su luna asociada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sun | `Sun` | Model Content | item | El sol a previsualizar |
| Location *(opcional)* | `Location` | Earth Location | item | Ubicación del observador |
| Distance *(opcional)* | `Distance` | Number | item | Distancia del sol al origen |
| Scale *(opcional)* | `Scale` | Number | item | Escala del radio del sol |

## Viewports

### Model View (View)

Vista del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| View *(opcional)* | `View` | View | item | La vista del modelo |
| Title *(opcional)* | `Title` | Text | item | El título de la vista guardada |
| Perspective *(opcional)* | `Perspective` | Boolean | item | Determina si la proyección de la vista es en perspectiva (True) o paralela (False). |
| Location *(opcional)* | `Location` | Plane | item | La ubicación de la cámara |
| Target *(opcional)* | `Target` | Number | item | La distancia del objetivo a la ubicación de la cámara |
| X Extents *(opcional)* | `X Extents` | Domain | item | Ancho del marco de la vista |
| Y Extents *(opcional)* | `Y Extents` | Domain | item | Alto del marco de la vista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| View | `View` | View | item | La vista del modelo |
| Title | `Title` | Text | item | El título de la vista guardada |
| Perspective | `Perspective` | Boolean | item | Determina si la proyección de la vista es en perspectiva (True) o paralela (False). |
| Location | `Location` | Plane | item | La ubicación de la cámara |
| Target | `Target` | Number | item | La distancia del objetivo a la ubicación de la cámara |
| X Extents | `X Extents` | Domain | item | Ancho del marco de la vista |
| Y Extents | `Y Extents` | Domain | item | Alto del marco de la vista |

### Model Viewport

Vista (viewport) del modelo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Viewport *(opcional)* | `Viewport` | Model Viewport | item | La vista (viewport) de Rhino |
| Name *(opcional)* | `Name` | Text | item | El nombre de la vista |
| View *(opcional)* | `View` | View | item | La orientación de la vista |
| Display Mode *(opcional)* | `Display Mode` | Display Mode | item | El modo de visualización de la vista (viewport) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Viewport | `Viewport` | Model Viewport | item | La vista (viewport) de Rhino |
| Name | `Name` | Text | item | El nombre de la vista |
| View | `View` | View | item | La orientación de la vista |
| Display Mode | `Display Mode` | Display Mode | item | El modo de visualización de la vista |

### Query Layouts (Layouts)

Consulta un documento de Rhino para obtener todas las vistas de layout disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layouts | `Layouts` | Layout Viewport | lista | La lista resultante de vistas de layout disponibles |

### Query Named Views (Named Views)

Consulta un documento de Rhino para obtener todas las vistas guardadas disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Views | `Views` | Model Content | lista | La lista resultante de vistas guardadas disponibles en el modelo |

### Query Viewports (Viewports)

Consulta un documento de Rhino para obtener todas las vistas (viewports) disponibles

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `Name` | Text Pattern | item | Filtro por nombre. Clic derecho sobre este parámetro para definir el método de coincidencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Viewports | `Viewports` | Model Viewport | lista | La lista resultante de vistas disponibles en el modelo |

### Zoom Extents (Zoom Ext)

Hace zoom en la vista para mostrar todos los objetos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| View | `View` | View | item | La vista a ajustar. |
| Extents | `Extents` | Geometry | lista | Geometría a incluir en el zoom de extensión. |
| Border *(opcional)* | `Border` | Number | item | Factor de borde. Si es > 1.0, el volumen de visión se agranda en este factor para dejar un borde alrededor de la vista. Un factor de 1.1 funciona bien en proyecciones paralelas; se sugiere 0.0 en proyecciones en perspectiva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| View | `View` | View | item | La vista ajustada. |
| Extents | `Extents` | Box | lista | Extensión de la geometría en la vista entregada. |
| Border | `Border` | Number | item | Factor de borde. Si es > 1.0, el volumen de visión se agranda en este factor para dejar un borde alrededor de la vista. Un factor de 1.1 funciona bien en proyecciones paralelas; se sugiere 0.0 en proyecciones en perspectiva. |
