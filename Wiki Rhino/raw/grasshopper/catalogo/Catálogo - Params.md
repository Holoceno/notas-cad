---
title: "Catálogo Grasshopper — Params"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Params"
libraries: ["Bifocals", "Galapagos 1.0.0.0", "Grasshopper 1.0.0008", "IO Components 8.35.26251.13001", "Math Components 8.35.26251.13001", "Transform Components 8.35.26251.13001", "opennest_2 Info 2.12.0.0"]
components: 142
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/opennest, programacion/scripts, fabricacion, rhino/documento]
---

# Params

142 objetos · librería: Bifocals, Galapagos 1.0.0.0, Grasshopper 1.0.0008, IO Components 8.35.26251.13001, Math Components 8.35.26251.13001, Transform Components 8.35.26251.13001, opennest_2 Info 2.12.0.0 · autor: David Rutten, Marc Syp, Petras Vestartas, Robert McNeel & Associates

Mapas: [[Mapa - Scripts, interfaz y archivos]] (53) · [[Mapa - Fabricación]] (23) · [[Mapa - Documento de Rhino]] (21) · [[Mapa - Visualización y anotaciones]] (12) · [[Mapa - Brep y sólidos]] (8) · [[Mapa - Data trees y listas]] (8) · [[Mapa - Matemáticas]] (8) · [[Mapa - Curvas]] (5) · [[Mapa - Puntos, vectores y planos]] (5) · [[Mapa - Mallas y SubD]] (3) · [[Mapa - Simulación, optimización y ML]] (3) · [[Mapa - Superficies y NURBS]] (1) · [[Mapa - Transformaciones]] (1) · [[Mapa - Morph y tween]] (1)

## Geometry

### Angular Dimension (parámetro)

Contiene una colección de cotas angulares

Tipo de dato: **Angular Dimension**

### Annotation Dot (parámetro)

Contiene una colección de puntos de anotación (dots)

Tipo de dato: **Text Dot**

### Block Instance (parámetro)

Contiene una colección de instancias de bloque

Tipo de dato: **Block Instance**

### Box (parámetro)

Contiene una colección de cajas

Tipo de dato: **Box**

### Brep (parámetro)

Contiene una colección de Breps (Boundary REPresentations)

Tipo de dato: **Brep**

### Centermark (parámetro)

Contiene una colección de marcas de centro

Tipo de dato: **Radial Centermark**

### Circle (parámetro)

Contiene una colección de círculos

Tipo de dato: **Circle**

### Circular Arc (Arc, parámetro)

Contiene una colección de arcos circulares

Tipo de dato: **Arc**

### Curve (Crv, parámetro)

Contiene una colección de curvas genéricas

Tipo de dato: **Curve**

### Extrusion (parámetro)

Contiene una colección de extrusiones

Tipo de dato: **Extrusion**

### Field (parámetro)

Contiene una colección de campos vectoriales

Tipo de dato: **Field**

### Geometry (Geo, parámetro)

Contiene una colección de geometría genérica

Tipo de dato: **Geometry**

### Geometry Cache (parámetro)

Empuja geometría hacia el documento de Rhino o la trae desde él

Tipo de dato: **Geometry**

### Geometry Pipeline (Pipeline, parámetro)

Define un pipeline de geometría de Rhino a Grasshopper

Tipo de dato: **Geometry**

### Group (Grp, parámetro)

Contiene una colección de grupos geométricos

Tipo de dato: **Group**

### Hatch (parámetro)

Contiene una colección de sombreados (hatches)

Tipo de dato: **Hatch**

### Leader (parámetro)

Contiene una colección de directrices (leaders)

Tipo de dato: **Leader**

### Light (parámetro)

Contiene una colección de luces

Tipo de dato: **Light**

### Line (parámetro)

Contiene una colección de segmentos de línea

Tipo de dato: **Line**

### Linear Dimension (parámetro)

Contiene una colección de cotas lineales

Tipo de dato: **Linear Dimension**

### Mesh (parámetro)

Contiene una colección de mallas poligonales

Tipo de dato: **Mesh**

### Mesh Face (Face, parámetro)

Contiene una colección de caras de malla triangulares o cuadrangulares

Tipo de dato: **Mesh face**

### Ordinate Dimension (parámetro)

Contiene una colección de cotas por coordenadas

Tipo de dato: **Ordinate Dimension**

### Plane (Pln, parámetro)

Contiene una colección de sistemas de ejes tridimensionales

Tipo de dato: **Plane**

### Point (Pt, parámetro)

Contiene una colección de puntos tridimensionales

Tipo de dato: **Point**

### Point Cloud (PCloud, parámetro)

Contiene una colección de nubes de puntos

Tipo de dato: **Point Cloud**

### Radial Dimension (parámetro)

Contiene una colección de cotas radiales

Tipo de dato: **Radial Dimension**

### Rectangle (Rec, parámetro)

Contiene una colección de rectángulos

Tipo de dato: **Rectangle**

### SubD (parámetro)

Contiene una colección de SubDs

Tipo de dato: **SubD**

### Surface (Srf, parámetro)

Contiene una colección de superficies genéricas

Tipo de dato: **Surface**

### Text Entity (parámetro)

Contiene una colección de entidades de texto

Tipo de dato: **Text Entity**

### Transform (parámetro)

Contiene una colección de transformaciones tridimensionales

Tipo de dato: **Transform**

### Twisted Box (TBox, parámetro)

Contiene una colección de cajas torcidas (twisted boxes)

Tipo de dato: **Twisted Box**

### Vector (Vec, parámetro)

Contiene una colección de vectores tridimensionales

Tipo de dato: **Vector**

### View (parámetro)

Contiene una colección de marcos de vista

Tipo de dato: **View**

## Input

### Atom Data (Atom)

Obtiene información detallada de un átomo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Atom | `A` | Atom | item | Átomo a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Ubicación del átomo |
| Element | `E` | Text | item | Nombre del elemento del átomo |
| Chain | `C` | Text | item | ID de la cadena a la que pertenece este átomo |
| Residue | `R` | Text | item | Nombre del residuo al que pertenece este átomo |
| Charge | `e` | Integer | item | Carga de este átomo |
| Occupancy | `O` | Number | item | Ocupación de este átomo |
| Temperature | `T` | Number | item | Factor de temperatura de este átomo |
| Atomic Number | `AN` | Integer | item | Número atómico del átomo |
| Serial Number | `SN` | Integer | item | Número de serie del átomo |
| Residue Number | `RN` | Integer | item | Número de serie del residuo |

### Boolean Toggle (Toggle, parámetro)

Interruptor booleano (True/False)

Tipo de dato: **Boolean**

### Button (parámetro)

Objeto botón con dos valores

Tipo de dato: **Data**

### Calendar (parámetro)

Representa un calendario

Tipo de dato: **Time**

### Clock (parámetro)

Representa un reloj de 24 horas

Tipo de dato: **Time**

### Colour Picker (Colour, parámetro)

Entrega un objeto selector de color

Tipo de dato: **Colour**

### Colour Swatch (Swatch, parámetro)

Muestra de color (paleta)

Tipo de dato: **Colour**

### Colour Wheel (Wheel, parámetro)

Crea una paleta de colores relacionados

Tipo de dato: **Colour**

### Control Knob (Knob, parámetro)

Una perilla radial para definir números

Tipo de dato: **Number**

### Digit Scroller (parámetro)

Selector numérico para números individuales

Tipo de dato: **Number**

### Gradient

Representa un degradado de varios colores

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lower limit | `L0` | Number | item | Límite inferior del rango del degradado |
| Upper limit | `L1` | Number | item | Límite superior del rango del degradado |
| Parameter | `t` | Number | item | Parámetro a lo largo del rango del degradado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colour | `C` | Colour | item | Color del degradado en el parámetro |

### Graph Mapper (Graph, parámetro)

Representa una función de mapeo numérico

Tipo de dato: **Value**

### Image Resource (parámetro)

Una URI de imagen previsualizable.

Tipo de dato: **Text**

### Image Sampler (Image, parámetro)

Entrega rutinas de muestreo de imágenes (mapas de bits).

Tipo de dato: **Sample**

### Import 3DM (3DM)

Importa geometría a un RhinoDoc

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File | `F` | Text | item | Ubicación del archivo |
| Layer | `L` | Text | item | Filtro por nombre de capa |
| Name | `N` | Text | item | Filtro por nombre de objeto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría importada |

### Import Coordinates (Coords)

Importa coordenadas de puntos desde archivos de texto genéricos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File | `F` | Text | item | Ubicación del archivo de texto de puntos |
| Separator | `S` | Text | item | Separador de los fragmentos de coordenadas |
| Comment *(opcional)* | `C` | Text | item | Inicio opcional de las líneas de comentario |
| X Index | `X` | Integer | item | Índice de la coordenada X del punto |
| Y Index | `Y` | Integer | item | Índice de la coordenada Y del punto |
| Z Index | `Z` | Integer | item | Índice de la coordenada Z del punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos importados |

### Import Image (IMG)

Importa datos de imagen desde archivos bmp, jpg o png.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File | `F` | Text | item | Ubicación del archivo de imagen |
| Rectangle *(opcional)* | `R` | Rectangle | item | Rectángulo de destino opcional de la imagen |
| X Samples *(opcional)* | `X` | Integer | item | Cantidad de muestras en la dirección X de la imagen |
| Y Samples *(opcional)* | `Y` | Integer | item | Cantidad de muestras en la dirección Y de la imagen |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Image | `I` | Mesh | item | Una representación en malla de la imagen |

### Import PDB (PDB)

Importa datos de archivos *.pdb del Protein Data Bank.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File | `F` | Text | item | Ubicación del archivo *.pdb |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Atoms | `A` | Atom | lista | Todos los átomos del archivo PDB |
| Bonds | `B` | Line | lista | Enlaces entre átomos |

### Import SHP (SHP)

Importa datos de archivos GIS *.shp.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File | `F` | Text | item | Ubicación del archivo *.shp |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos del archivo |
| Curves | `C` | Curve | lista | Curvas del archivo |
| Regions | `R` | Brep | lista | Regiones del archivo |

### MD Slider (parámetro)

Un slider multidimensional

Tipo de dato: **Point**

### Number Slider (parámetro)

Slider numérico para valores individuales

Tipo de dato: **Number**

### Panel (parámetro)

Un panel para notas y valores de texto personalizados

Tipo de dato: **Text**

### Read File (File)

Lee el contenido de un archivo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File | `F` | Text | item | URI del archivo a leer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `C` | Generic Data | lista | Contenido del archivo |

### Value List (List, parámetro)

Entrega una lista de valores predefinidos para elegir

Tipo de dato: **Goo**

## OpenNest2

### Bounding Box Edges (BBoxEdges)

Devuelve las dos aristas base de la caja contenedora orientada de un objeto y sus longitudes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| G | `Geo` | Geometry | item | Geometría a contener |
| P *(opcional)* | `Plane` | Plane | item | Plano de orientación de la caja |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L0 | `Line0` | Line | item | Primera arista base de la caja contenedora |
| L1 | `Line1` | Line | item | Segunda arista base de la caja contenedora |
| D0 | `Dist0` | Number | item | Longitud de la primera arista base |
| D1 | `Dist1` | Number | item | Longitud de la segunda arista base |
| B | `Box` | Box | item | Caja contenedora orientada |

### Box Packing (PackBox)

Empaqueta cajas 3D dentro de un contenedor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Con | `C` | Geometry | lista | Contenedor en el que empaquetar |
| Geo | `G` | Geometry | lista | Geometría a empaquetar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geo | `G` | Geometry | lista | Geometría empaquetada |
| Tra | `T` | Transform | lista | Transformaciones del empaquetado |

### Geometry

Prepara piezas para el anidado (nesting): separa los contornos (con agujeros) de los atributos adjuntos; opcionalmente simplifica, calcula la envolvente convexa y crea copias.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Outlines | `Outlines` | Geometry | árbol | Curvas cerradas O superficies planas (se convierten internamente según su tipo). Si las geometrías tienen agujeros, crea primero un árbol de datos y pon cada elemento en su propia rama. Si no, el algoritmo intentará ordenar las polilíneas revisando los posibles agujeros. |
| Simplify *(opcional)* | `Simplify` | Number | item | Divisiones de segmento: 0 = CONSERVA TODOS los vértices (sin simplificar; lo mejor para anidar contornos finos); x>0 divide por distancia; x<0 máximo 3 puntos por subsegmento (fusiona los colineales dentro de 10 grados) |
| Hull *(opcional)* | `Hull` | Boolean | item | Reemplaza cada contorno por su envolvente convexa |
| Copies *(opcional)* | `Copies` | Integer | lista | Cantidad de copias por pieza |
| Offset *(opcional)* | `Offset` | Number | item | Separación SOLO para el anidado (unidades del modelo; 0 = desactivado, rápido). Piezas: el contorno exterior crece y los agujeros se achican, para que las piezas colocadas mantengan esta separación. Lo que se coloca y se entrega siguen siendo las curvas ORIGINALES. |
| Rotations *(opcional)* | `Rotations` | Integer | lista | Restricción de rotación OPCIONAL por pieza (un valor por pieza, se repite como Copies). Vacío / 0 = la pieza hereda el ajuste global Rotations del solver (por defecto). N > 0 = ESTA pieza solo puede usar N orientaciones (pasos de 360/N grados). 1 = fija, sin rotación (por ejemplo, por la veta). Permite que las piezas rectangulares se queden en 4 orientaciones mientras las piezas de forma libre rotan libremente en UN mismo anidado. |
| Attributes *(opcional)* | `Attributes` | Geometry | árbol | Geometría adicional: puntos, líneas, superficies, mallas... Usa un árbol de datos, una lista de geometría adicional por rama. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `Geometry` | Generic Data | lista | Piezas preparadas para el anidado |
| Borders | `Borders` | Curve | árbol | Curvas de contorno de cada pieza |

### Geometry (Rhino) (Geometry Rhino)

Construye piezas para anidar a partir de objetos de Rhino referenciados, separando los contornos de los atributos (texto, curvas) y ordenándolos automáticamente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer *(opcional)* | `Layer` | Text | item | Capa de borde en Rhino que debes crear para seleccionar objetos. |
| Copies | `Copies` | Integer | lista | La cantidad de copias debe ser igual a las ramas del árbol; cada entrada de guids se trata como una rama separada |
| Simplify *(opcional)* | `Simplify` | Number | lista | [divisions, hull] opcional. divisions: 0 = conserva los vértices de la polilínea tal cual (sin simplificar, POR DEFECTO); x>0 divide los segmentos curvos por distancia; x<0 máximo 3 puntos por subsegmento. hull (2.º valor, 0/1): reemplaza cada pieza por su envolvente convexa. Basta con un valor (hull por defecto es 0). |
| Sort *(opcional)* | `Sort` | Number | item | Ordena las polilíneas. |
| Offset *(opcional)* | `Offset` | Number | item | Separación SOLO para el anidado (unidades del modelo; 0 = desactivado, rápido). Piezas: el contorno exterior crece y los agujeros se achican, para que las piezas colocadas mantengan esta separación. Lo que se coloca y se entrega siguen siendo las curvas ORIGINALES. |
| Rotations *(opcional)* | `Rotations` | Integer | lista | Restricción de rotación OPCIONAL por pieza (un valor por rama de guids, se repite como Copies). Vacío / 0 = la pieza hereda el ajuste global Rotations del solver (por defecto). N > 0 = ESTA pieza solo puede usar N orientaciones (pasos de 360/N grados). 1 = fija, sin rotación (por ejemplo, por la veta). |
| Guid *(opcional)* | `Guid` | Guid | árbol | Geometría referenciada como guid (puede ser malla, brep o curvas en una misma lista) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `Geometry` | Generic Data | lista | Geometría de anidado armada para entregar al solver |
| Borders | `Borders` | Curve | árbol | Curvas de contorno agrupadas por pieza |
| BC | `BC` | Curve | árbol | Curvas de borde de la envolvente convexa por pieza |
| Groups | `Groups` | Integer | árbol | Índices de grupo de los objetos por pieza |
| All | `All` | Geometry | árbol | Toda la geometría referenciada agrupada por pieza |

### Geometry (Surfaces) (Geometry Srf)

Construye piezas para anidar a partir de superficies planas en vez de curvas; los agujeros se leen de los bordes de la superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `Surfaces` | Brep | lista | Superficies planas de contorno. Si quieres anidar en varias planchas, separa las superficies en el árbol de datos. |
| Simplify *(opcional)* | `Simplify` | Number | item | Divisiones de segmento: 0 toma solo los extremos; x>0 divide por distancia; x<0 máximo 3 puntos por subsegmento |
| Hull *(opcional)* | `Hull` | Boolean | item | Usa la envolvente convexa de cada contorno simplificado. |
| Copies *(opcional)* | `Copies` | Integer | lista | Cantidad de copias por pieza. |
| Offset *(opcional)* | `Offset` | Number | item | Separación SOLO para el anidado (unidades del modelo; 0 = desactivado, rápido). Piezas: el contorno exterior crece y los agujeros se achican, para que las piezas colocadas mantengan esta separación. Lo que se coloca y se entrega siguen siendo las curvas ORIGINALES. |
| Rotations *(opcional)* | `Rotations` | Integer | lista | Restricción de rotación OPCIONAL por pieza (un valor por pieza, se repite como Copies). Vacío / 0 = la pieza hereda el ajuste global Rotations del solver (por defecto). N > 0 = ESTA pieza solo puede usar N orientaciones (pasos de 360/N grados). 1 = fija, sin rotación (por ejemplo, por la veta). Permite que las piezas rectangulares se queden en 4 orientaciones mientras las piezas de forma libre rotan libremente en UN mismo anidado. |
| Attributes *(opcional)* | `Attributes` | Geometry | árbol | Geometría adicional que acompaña a cada pieza: puntos, líneas, superficies, mallas... Árbol de datos: una rama por superficie (rama i -> superficie i). Usa el +/- del componente para agregar más puertos Attributes. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `Geometry` | Generic Data | lista | Piezas de anidado listas para el solver. |
| Borders | `Borders` | Curve | lista | Curvas de contorno de cada pieza. |

### Inscribed Circle (InscribeCircle)

Busca el círculo más grande que cabe dentro de cada polilínea cerrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `P` | Curve | lista | Polilíneas cerradas en las que inscribir círculos |
| Tolerance | `T` | Number | item | Precisión del ajuste |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circle | `C` | Circle | lista | Círculo inscrito más grande |

### Merge

Combina dos flujos de geometría de OpenNest en uno.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | lista | Geometría de OpenNest. |
| Geometry | `G` | Generic Data | lista | Geometría de OpenNest. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría combinada. |

### NestOptions

Construye los textos de opciones para un solver de anidado. Solver = -1 (Auto, por defecto) sigue al solver al que está conectado; 0 (OpenNest2) / 1 (OpenNestCollision) lo fuerza. Las demás entradas cambian al conjunto de opciones de ese solver. Conecta la salida a la entrada Options del componente solver.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Solver *(opcional)* | `Solver` | Integer | item | Para qué solver son estas opciones. -1 = Auto (sigue al solver al que está conectada esta salida); 0 = OpenNest2 (NFP + algoritmo genético); 1 = OpenNestCollision (física). Al cambiarlo, las entradas de abajo pasan al conjunto de opciones de ese solver. |
| Rotations *(opcional)* | `Rotations` | Integer | item | Orientaciones que puede probar cada pieza (360/n). El valor por defecto 4 es más rápido; súbelo (por ejemplo a 8) para un empaquetado más apretado. Rango 1-3600. Por defecto 4. |
| Packing *(opcional)* | `Packing` | Integer | item | Estrategia de ubicación. Bottom Left = coloca cada pieza en el lugar factible más bajo y luego más a la izquierda. Valores: 0=Box, 1=Gravity, 2=Squeeze, 3=Bottom Left. Por defecto 1. |
| Seed *(opcional)* | `Seed` | Integer | item | Semilla aleatoria (misma semilla = mismo resultado). Rango 0-100000. Por defecto 30. |
| Mutation *(opcional)* | `Mutation` | Integer | item | Tasa de mutación del algoritmo genético. Rango 0-100. Por defecto 10. |
| Population *(opcional)* | `Population` | Integer | item | Tamaño de la población del algoritmo genético. Rango 1-100000. Por defecto 10. |
| All Rotations *(opcional)* | `All Rotations` | Integer | item | Prueba todas las orientaciones de cada pieza para el empaquetado más apretado; solo en el motor C++ (el motor C# lo ignora y usa 'Rotations'). Activado por defecto; limitado a 8 orientaciones para que un valor grande de 'Rotations' no cuelgue el solver. Valores: 0=desactivado, 1=activado. Por defecto 1. |
| Element Holes *(opcional)* | `Element Holes` | Integer | item | Anida piezas más pequeñas DENTRO de los agujeros de las piezas más grandes. Valores: 0=desactivado, 1=rellenar. Por defecto 1. |
| Batch *(opcional)* | `Batch` | Integer | item | Mantiene juntas las piezas relacionadas para ordenarlas. ACTIVADO (por defecto): cada RAMA del árbol de datos de Geometry es un lote que se anida en su propio bloque compacto y se coloca UN LOTE POR PLANCHA (rama 0 -> plancha 0, rama 1 -> plancha 1, ...; si hay más ramas que planchas, se reparten en ronda sobre las planchas). Da forma al árbol antes (por ejemplo con Partition List) para controlar la agrupación. Una lista plana (una rama) da un solo anidado combinado. DESACTIVADO: anida todo combinado en la menor cantidad de planchas (lo más denso). Valores: 0=desactivado, 1=activado. Por defecto 1. |
| Sheet Font *(opcional)* | `Sheet Font` | Text | item | Etiqueta del número de plancha: nombre de la fuente + tamaño del texto. Por defecto "MecSoft_Font-1 1". |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Options | `Options` | Text | lista | Textos de opciones ("clave valor" por línea) para el solver seleccionado; conéctalos a la entrada Options del componente solver. |

### OpenNest1

Anida curvas/superficies SIN PROCESAR sobre planchas con el solver de no-fit-polygon (sin componente Geometry ni atributos). Corre en un hilo en segundo plano con vista previa en vivo, así Rhino sigue respondiendo. Run = TRUE resuelve y vuelve a resolver al cambiar una entrada; Reset limpia. Admite varios intentos (Tries) con distintos inicios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Geometry | árbol | Planchas: superficies planas cerradas (contorno exterior + agujeros) o curvas cerradas. Una sola plancha se copia automáticamente para que las piezas puedan pasar a más planchas. |
| Geo | `Geo` | Geometry | árbol | Piezas a anidar: curvas cerradas o superficies planas. Varias ramas del árbol de datos se combinan en un solo anidado (para anidado agrupado por lotes, una rama por plancha, usa OpenNest2 u OpenNestCollision, que tienen la opción Batch). |
| Spacing *(opcional)* | `Spacing` | Number | item | Separación a mantener entre las piezas colocadas Y respecto del borde de la plancha. Se aplica como offset de anidado directamente a piezas y planchas (este componente recibe polilíneas sin procesar, no nest_geo/nest_sheets), así que reemplaza a las entradas Offset de Geometry/Sheets. Lo que se entrega sigue siendo la geometría ORIGINAL. |
| Placement *(opcional)* | `Placement` | Integer | item | Índice de la estrategia de ubicación (0 Box, 1 Gravity, 2 Squeeze, 3 Bottom-Left). |
| Tolerance *(opcional)* | `Tolerance` | Number | item | Tolerancia de simplificación de curvas. |
| Rotations *(opcional)* | `Rotations` | Integer | item | Ángulos de orientación por pieza. Menos = mucho más rápido en conjuntos grandes (la caché NFP inicial crece con las rotaciones); más = un poco más apretado. |
| Iterations *(opcional)* | `Iterations` | Integer | item | Generaciones del solver a evolucionar. Ves cómo cada una se aprieta en la vista previa; más = más apretado pero más lento. Lo típico es ~4–10. |
| Seed *(opcional)* | `Seed` | Integer | item | Semilla aleatoria para resultados reproducibles. |
| Reset *(opcional)* | `Reset` | Boolean | item | Poner en TRUE (conecta un Button) para limpiar todo el componente al instante y descartar cualquier cálculo en curso. |
| Run *(opcional)* | `Run` | Boolean | item | Conecta un Boolean Toggle. TRUE = resuelve ahora y vuelve a resolver automáticamente cuando cambia una entrada (hilo en segundo plano, Rhino sigue respondiendo, vista previa en vivo). FALSE = no entrega nada y borra el resultado anterior (salidas vacías + vista previa limpia). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Curve | lista | Las planchas que se usaron, tal como se entregaron. Spacing contrae internamente el contenedor de anidado, pero nunca el contorno informado. |
| Geo | `Geo` | Geometry | árbol | Las piezas ORIGINALES movidas sobre las planchas (las mismas curvas que entraron; solo cambia la posición). Spacing se aplica a un contorno de anidado SEPARADO, así que aparece como separación ENTRE piezas y nunca como una curva más gruesa. Los bordes curvos se anidan mediante un polígono que los circunscribe, así que la separación real es Spacing o un poco más, nunca menos. Si el contorno de una pieza o plancha no admite offset (anillo degenerado, o un contraído que lo consume), el componente muestra una ADVERTENCIA con cuántos son: esos quedan SIN separación. |
| ID | `ID` | Integer | lista | Número de id del polígono |
| Transform | `Transform` | Transform | lista | Transformación de ubicación por pieza. |
| IDS | `IDS` | Integer | lista | Número de id de la plancha |

### OpenNest2

Anida piezas sobre planchas con el solver genético de no-fit-polygon, conservando los atributos de cada pieza. Entrégale los componentes Sheets y Geometry.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Generic Data | árbol | De la pestaña OpenNest, usa el componente Sheets. |
| Geometry | `Geometry` | Generic Data | árbol | De la pestaña OpenNest, usa el componente Geometry. Cuando la opción Batch está ACTIVADA, cada RAMA del árbol de datos se anida como su propio lote agrupado (se mantiene junto como un bloque, un lote por plancha; da forma al árbol antes, por ejemplo con Partition List, para controlar la agrupación); una entrada plana (una rama) es un solo anidado combinado. |
| Options *(opcional)* | `Options` | Text | lista | Lista opcional de textos de opciones "clave valor"; conecta aquí el componente Nest Options. Cada línea reemplaza la fila de opción correspondiente en el lienzo (las filas de abajo muestran los valores realmente usados); las claves no conectadas mantienen su valor del lienzo. Ejemplos: "num_of_rotations 8", "placement_type 1", "spacing 0.5", "MecSoft_Font-1 1" (fuente de la plancha: nombre + tamaño). Las líneas desconocidas generan una advertencia. |
| Iterations *(opcional)* | `Iterations` | Integer | item | Generaciones del algoritmo genético a evolucionar. Cada generación evalúa toda la población y conserva la mejor, así que el resultado mejora con las generaciones. Lo típico es ~10-40 (una vista previa naranja en vivo se aprieta mientras corre; presiona ESC para detener y conservar la mejor). Úsalo junto con la opción 'population' (por defecto 10). |
| Run *(opcional)* | `Run` | Boolean | item | Conecta un Boolean Toggle. TRUE = resuelve ahora y vuelve a resolver cuando cambia una entrada (hilo en segundo plano, vista previa en vivo); FALSE = no entrega nada y borra el resultado anterior (salidas vacías + vista previa limpia). (Las opciones se siguen editando en el cuerpo del componente; ESC detiene un cálculo en curso pero conserva el resultado parcial mientras Run se mantenga en TRUE.) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Curve | árbol | Polilíneas que representan las planchas. |
| Borders | `Borders` | Curve | árbol | Curvas de contorno de las piezas colocadas. |
| All Geo | `All Geometry` | Geometry | árbol | Toda la geometría colocada, agrupada por plancha. |
| Transforms | `Transforms` | Transform | árbol | Transformación de movimiento/rotación que ubica cada pieza. |
| Sheet Id | `Sheet Id` | Integer | árbol | Índice de la plancha en la que quedó cada pieza. |
| Sheet Txt | `Sheet Txt` | Curve | árbol | Etiquetas de número de plancha como curvas de texto. |
| Attributes | `Attributes` | Geometry | árbol | Geometría de atributos que acompaña a cada pieza. |

### OpenNest3D

Anidado 3D malla-malla (empaquetado espectral / FFT). Empaqueta mallas dentro de una caja contenedora.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Parts | `Parts` | Mesh | lista | Mallas a anidar en el contenedor. |
| Container | `Container` | Box | item | Caja contenedora (su tamaño X/Y/Z es el volumen de trabajo; Z es 'arriba'). |
| Resolution *(opcional)* | `Resolution` | Integer | item | Vóxeles a lo largo del eje más largo del contenedor (más alto = más fino y más lento). |
| Orientations *(opcional)* | `Orientations` | Integer | item | Orientaciones de cubo que se prueban por pieza: 1, 4, 6 o 24 (más = más apretado y más lento). |
| Height Penalty *(opcional)* | `Height Penalty` | Number | item | Peso que empuja las piezas hacia el piso (z). <=0 usa el valor por defecto 1e8. |
| Quantities *(opcional)* | `Quantities` | Integer | lista | Copias opcionales por pieza (por defecto 1 de cada una). |
| Run *(opcional)* | `Run` | Boolean | item | Ejecuta el cálculo (puede tardar segundos). Desactivado por defecto. |
| Clearance *(opcional)* | `Clearance` | Number | item | Separación mínima entre piezas Y respecto de las paredes del contenedor, en unidades del modelo. 0 = desactivado (las piezas pueden tocarse). Se redondea hacia arriba a vóxeles enteros (paso = eje más largo del contenedor / Resolution); además hace que la colisión sea conservadora con una Resolution gruesa. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Placed | `Placed` | Mesh | lista | Las piezas movidas/rotadas dentro del contenedor (una por instancia). |
| Transform | `Transform` | Transform | lista | Transformación de ubicación por instancia (mundo = R*p + t). |
| Container | `Container` | Integer | lista | Id del contenedor por instancia (0 = colocada, -1 = no cupo). |
| Part Index | `Part Index` | Integer | lista | Índice de la pieza de origen (en la lista de entrada) por instancia. |

### OpenNestCollision

Anida piezas sobre planchas con el solver de colisión física: empaqueta de forma apretada y puede rellenar las cavidades de las piezas. Entrégale los componentes Sheets y Geometry.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Generic Data | árbol | De la pestaña OpenNest, usa el componente Sheets. |
| Geometry | `Geometry` | Generic Data | árbol | De la pestaña OpenNest, usa el componente Geometry. Cuando la opción Batch está ACTIVADA, cada RAMA del árbol de datos se anida como su propio lote agrupado (se mantiene junto como un bloque, un lote por plancha; da forma al árbol antes, por ejemplo con Partition List, para controlar la agrupación); una entrada plana (una rama) es un solo anidado combinado. |
| Options *(opcional)* | `Options` | Text | lista | Lista opcional de textos de opciones "clave valor"; conecta aquí el componente Nest Options. Cada línea reemplaza la fila de opción correspondiente en el lienzo (las filas de abajo muestran los valores realmente usados); las claves no conectadas mantienen su valor del lienzo. Ejemplos: "num_of_rotations 8", "placement_type 1", "spacing 0.5", "MecSoft_Font-1 1" (fuente de la plancha: nombre + tamaño). Las líneas desconocidas generan una advertencia. |
| Iterations *(opcional)* | `Iterations` | Integer | item | Rondas de relajación: más rondas empaquetan más apretado pero más lento. ~4000 = el empaquetado apretado todo en una plancha; usa menos para una vista previa rápida y aproximada. |
| Run *(opcional)* | `Run` | Boolean | item | Conecta un Boolean Toggle. TRUE = resuelve ahora y vuelve a resolver cuando cambia una entrada (hilo en segundo plano, vista previa en vivo); FALSE = no entrega nada y borra el resultado anterior (salidas vacías + vista previa limpia). (Las opciones se siguen editando en el cuerpo del componente; ESC detiene un cálculo en curso pero conserva el resultado parcial mientras Run se mantenga en TRUE.) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Curve | árbol | Polilíneas de contorno de las planchas usadas para el anidado. |
| Borders | `Borders` | Curve | árbol | Curvas de contorno de las piezas colocadas. |
| All Geo | `All Geometry` | Geometry | árbol | Toda la geometría de las piezas colocadas. |
| Transforms | `Transforms` | Transform | árbol | Transformaciones de ubicación de cada pieza. |
| Sheet Id | `Sheet Id` | Integer | árbol | Índice de la plancha en la que quedó cada pieza. |
| Sheet Txt | `Sheet Txt` | Curve | árbol | Curvas de las etiquetas de número de plancha. |
| Attributes | `Attributes` | Geometry | árbol | Geometría de atributos por pieza. |

### Pack Objects (Pack)

Dispone objetos en una fila, orientando cada uno de 3D a 2D con la separación elegida.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geo | `G` | Geometry | árbol | Objetos a empaquetar |
| Plane | `P` | Plane | árbol | Plano base para orientar de 3D a 2D |
| X *(opcional)* | `X` | Number | item | Distancia de desfase; un número negativo no incluye la caja contenedora |
| Y *(opcional)* | `Y` | Number | item | Distancia de desfase; un número negativo no incluye la caja contenedora |
| tolerance *(opcional)* | `t` | Number | item | Rota los objetos en pasos de t radianes hasta Math.Pi y se queda con el de caja contenedora mínima |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geo | `G` | Geometry | árbol | Objetos empaquetados |
| Transformation | `T` | Transform | árbol | Transformación aplicada a cada objeto |

### Principal Component Analysis (PCA)

Caja contenedora orientada, alineada con las aristas de la pieza: un rectángulo de área mínima para conjuntos de puntos planos y una caja de volumen mínimo para sólidos. Devuelve el plano alineado, la caja y sus 8 puntos de esquina.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Conjunto de puntos a analizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| P | `Plane` | Plane | item | Plano alineado con las aristas de la caja orientada |
| B | `Box` | Box | item | Caja contenedora orientada |
| Pt | `Points` | Point | lista | Puntos de esquina de la caja contenedora |

### Project to Plane (Project)

Proyecta una polilínea sobre su plano de mejor ajuste y devuelve ese plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea a proyectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polyline | `P` | Curve | item | Polilínea proyectada |
| Plane | `Pl` | Plane | item | Plano de mejor ajuste |

### Region Slits (RSlits)

Corta ranuras de encaje donde se encuentran regiones planas (una versión corregida del componente nativo).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Regions | `R` | Curve | lista | Regiones planas a intersectar |
| Width | `W` | Number | item | Ancho de las ranuras |
| Gap | `G` | Number | item | Tamaño de holgura adicional en los puntos donde se encuentran las ranuras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Regions | `R` | Surface | árbol | Regiones con ranuras |
| Topology | `T` | Integer | árbol | Topología de las ranuras |

### Rhino Objects (RhinoObjects)

Lee objetos de Rhino referenciados, con atributos como texto, y los convierte en Breps planos para el anidado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry as guid | `G` | Guid | árbol | Geometría referenciada como guid (puede ser malla, brep o curvas en una misma lista) |
| T | `T` | Number | item | Tolerancia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | lista | Breps planos |
| Geometry as guid | `G` | Guid | árbol | Geometría referenciada como guid (puede ser malla, brep o curvas en una misma lista) |

### Sheets

Define las planchas sobre las que anidar (con agujeros opcionales) a partir de polilíneas cerradas; admite separación, filas y copias.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polylines | `Polylines` | Curve | árbol | Polilíneas cerradas de las planchas, con agujeros opcionales. |
| Gap *(opcional)* | `Gap` | Number | lista | Separación entre planchas. |
| Rows *(opcional)* | `Rows` | Number | lista | Cantidad de planchas por fila antes de partir. |
| Copies *(opcional)* | `Copies` | Number | item | Cantidad de copias de la misma plancha. |
| Offset *(opcional)* | `Offset` | Number | item | MARGEN interior para el anidado (unidades del modelo; 0 = desactivado, rápido). Las piezas mantienen esta distancia del borde de la plancha; los agujeros de la plancha crecen en esa medida. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Generic Data | item | Tipo de dato nest_sheets de OpenNest. |
| Polylines | `Polylines` | Curve | árbol | Polilíneas de contorno de las planchas generadas. |

### Sheets (Surfaces) (Sheets Srf)

Define las planchas sobre las que anidar a partir de superficies planas en vez de polilíneas; los agujeros salen de los bordes de la superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `Surfaces` | Brep | lista | Superficies planas con agujeros opcionales. |
| Gap *(opcional)* | `Gap` | Number | lista | Separación entre planchas. |
| Rows *(opcional)* | `Rows` | Number | lista | Cantidad de planchas por fila; si se supera, se parte. |
| Count *(opcional)* | `Count` | Number | lista | Cantidad de copias de la misma plancha. |
| Offset *(opcional)* | `Offset` | Number | item | MARGEN interior para el anidado (unidades del modelo; 0 = desactivado, rápido). Las piezas mantienen esta distancia del borde de la plancha; los agujeros de la plancha crecen en esa medida. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sheets | `Sheets` | Generic Data | item | Tipo de dato nest_sheets de OpenNest. |
| Polylines | `Polylines` | Curve | árbol | Polilíneas de borde de las planchas. |

### Simplify

Reduce la cantidad de vértices de una curva cerrada, aplicando automáticamente hacia afuera el offset justo para que la original quede dentro, así las piezas anidadas nunca se superponen.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Curves` | Curve | lista | Curvas cerradas a simplificar. |
| Simplify | `Simplify` | Number | item | Cantidad de simplificación (distancia de Douglas-Peucker, en unidades del modelo): cuánto detalle se descarta. Más grande = menos vértices. El offset hacia afuera necesario para que la original quede encerrada se calcula AUTOMÁTICAMENTE (siempre <= este valor) y se informa en la salida Offset. 0 = solo limpiar (sin reducir). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Curves` | Curve | lista | Polilíneas cerradas simplificadas (se GARANTIZA que cada una contiene a su original). |
| Vertices | `Vertices` | Integer | lista | Cantidad de vértices de cada curva simplificada. |
| Offset | `Offset` | Number | lista | La distancia hacia afuera aplicada automáticamente a cada curva para que la original quede dentro (unidades del modelo). 0 = no hizo falta. |

### Text

Construye contornos de texto como curvas para corte láser o fresado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `L` | Plane | item | Ubicación y orientación del texto |
| Text | `T` | Text | item | Texto a mostrar |
| Size | `S` | Number | item | Tamaño del texto |
| Font *(opcional)* | `F` | Text | item | Fuente; si no se entrega, se usa la más adecuada. Para negrita cursiva -> NombreFuente True True; para negrita -> NombreFuente True False |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Texto como curvas |

### Transform Object (TGuid)

Transforma un objeto de Rhino referenciado en su lugar, conservando todas sus propiedades.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guid | `Guid` | Guid | item | Geometría referenciada como guid |
| Transform | `Transform` | Transform | item | Transformación a aplicar al objeto |
| Run | `Run` | Boolean | item | Poner en True para aplicar la transformación |

### Unroll

Desenrolla un Brep o malla desarrollable a plano, llevando consigo sus curvas, puntos y textos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh or Brep *(opcional)* | `M or B` | Generic Data | item | Malla o Brep a desenrollar. |
| Curves *(opcional)* | `C` | Curve | lista | Curvas a desenrollar junto con la superficie |
| Points *(opcional)* | `P` | Point | lista | Puntos a desenrollar junto con la superficie |
| Text *(opcional)* | `TXT` | Text | lista | Etiquetas de texto a desenrollar junto con la superficie |
| Text point *(opcional)* | `TP` | Point | lista | Puntos de anclaje de las etiquetas de texto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep desenrollado |
| Curves | `C` | Curve | lista | Curvas desenrolladas |
| Points | `P` | Point | lista | Puntos desenrollados |
| TextDotsLocation | `TXT L` | Generic Data | lista | Ubicaciones de las etiquetas de texto desenrolladas |
| TextDots | `TXT` | Generic Data | lista | Etiquetas de texto desenrolladas |

## Primitive

### Boolean (Bool, parámetro)

Contiene una colección de valores booleanos

Tipo de dato: **Boolean**

### Colour (Col, parámetro)

Contiene una colección de colores RGB

Tipo de dato: **Colour**

### Complex (C, parámetro)

Contiene una colección de números complejos

Tipo de dato: **Complex**

### Culture (parámetro)

Contiene una colección de especificadores de cultura (idioma/región)

Tipo de dato: **Culture**

### Data (parámetro)

Contiene una colección de datos genéricos

Tipo de dato: **Generic Data**

### Data Path (Path, parámetro)

Contiene una colección de rutas de árbol de datos

Tipo de dato: **Path**

### Domain (parámetro)

Contiene una colección de dominios numéricos

Tipo de dato: **Domain**

### Domain² (parámetro)

Contiene una colección de dominios numéricos 2D

Tipo de dato: **Domain²**

### Earth Anchor Point (Anchor, parámetro)

Contiene un punto de anclaje terrestre que asocia un punto y una orientación del modelo con una latitud, longitud y elevación.

Tipo de dato: **Earth Location**

### File Path (Path, parámetro)

Contiene una colección de rutas de archivo

Tipo de dato: **Text**

### Font (parámetro)

Contiene una colección de fuentes

Tipo de dato: **Font**

### Guid (ID, parámetro)

Contiene una colección de identificadores únicos globales (GUID)

Tipo de dato: **Guid**

### Integer (Int, parámetro)

Contiene una colección de números enteros

Tipo de dato: **Integer**

### Matrix (parámetro)

Contiene una colección de matrices numéricas

Tipo de dato: **Matrix**

### Number (Num, parámetro)

Contiene una colección de números de coma flotante

Tipo de dato: **Number**

### Shader (parámetro)

Contiene una colección de materiales de visualización

Tipo de dato: **Shader**

### Text (Txt, parámetro)

Contiene una colección de fragmentos de texto

Tipo de dato: **Text**

### Time (parámetro)

Contiene una colección de horas y fechas

Tipo de dato: **Time**

### Unit System (parámetro)

Contiene una colección de sistemas de unidades del modelo

Tipo de dato: **Unit System**

## Rhino

### Display Mode (parámetro)

Contiene una colección de modos de visualización

Tipo de dato: **Display Mode**

### Layout Viewport (Layout, parámetro)

Contiene una colección de diseños de página (layouts) de Rhino

Tipo de dato: **Layout Viewport**

### Model Annotation Style (Style, parámetro)

Contiene una colección de estilos de anotación del modelo

Tipo de dato: **Model Annotation Style**

### Model Attribute Key (Key, parámetro)

Contiene una colección de claves de atributos

Tipo de dato: **Text**

### Model Block Definition (Block Definition, parámetro)

Contiene una colección de definiciones de bloque del modelo

Tipo de dato: **Model Block Definition**

### Model Environment (Environment, parámetro)

Contiene una colección de entornos del modelo

Tipo de dato: **Model Environment**

### Model Hatch Pattern (Hatch Pattern, parámetro)

Contiene una colección de patrones de sombreado del modelo

Tipo de dato: **Model Hatch Pattern**

### Model Layer (Layer, parámetro)

Contiene una colección de capas del modelo

Tipo de dato: **Model Layer**

### Model Linetype (Linetype, parámetro)

Contiene una colección de tipos de línea del modelo

Tipo de dato: **Model Linetype**

### Model Material (Material, parámetro)

Contiene una colección de materiales del modelo

Tipo de dato: **Model Material**

### Model Object (Object, parámetro)

Contiene una colección de objetos del modelo

Tipo de dato: **Model Object**

### Model Print Width (Print Width, parámetro)

Contiene una colección de grosores de impresión del modelo

Tipo de dato: **Print Width**

### Model Viewport (Viewport, parámetro)

Contiene una colección de vistas de Rhino

Tipo de dato: **Model Viewport**

## Util

### Bifocals

Agrega etiquetas flotantes a todos los componentes, con algunas excepciones. Doble clic para activar/desactivar; ver el menú del clic derecho para las opciones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Exceptions *(opcional)* | `E` | Text | lista | Lista de nombres de componentes a excluir |

### Cherry Picker (Item, parámetro)

Toma un solo elemento de un árbol de datos

Tipo de dato: **Goo**

### Cluster Input (Input, parámetro)

Representa un parámetro de entrada de un cluster

Tipo de dato: **Goo**

### Cluster Output (Output, parámetro)

Representa un parámetro de salida de un cluster

Tipo de dato: **Goo**

### Context Bake (C-Bake)

Contenido para hacer bake al final del comando GrasshopperPlayer o con Hops y Rhino.Compute.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `Content` | Generic Data | árbol | Contenido a recolectar para hacer bake |

### Context Print (C-Print)

Datos de texto para imprimir al final del comando GrasshopperPlayer.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `Tx` | Text | árbol | Texto a imprimir. |

### Data Dam (Dam)

Retrasa los datos en su paso por el documento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data A *(opcional)* | `A` | Generic Data | árbol | Datos a retener (buffer) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data A | `A` | Generic Data | árbol | Datos retenidos (buffer) |

### Data Input (Input)

Lee un conjunto de datos desde un archivo.

### Data Output (Output)

Escribe un conjunto de datos en un archivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data Input *(opcional)* | `A` | Generic Data | árbol | Datos a incluir en el archivo. |

### Data Recorder (Rec, parámetro)

Registra datos a lo largo del tiempo

Tipo de dato: **Goo**

### Fitness Landscape (LScape)

Muestra un paisaje de aptitud (fitness) 2.5D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bounds | `B` | Rectangle | item | Límites del paisaje |
| Values | `V` | Number | lista | Valores del paisaje |
| Count | `N` | Integer | item | Cantidad de muestras en la dirección X |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Landscape | `L` | Mesh | item | Malla del paisaje |

### Galapagos (objeto especial)

Interfaz con el solver evolutivo Galapagos

### Gene Pool (Genes, parámetro)

Contiene una colección de genes (es decir, variables)

Tipo de dato: **Number**

### Get Boolean (parámetro)

Entrada booleana contextual.

Tipo de dato: **Boolean**

### Get File Path (parámetro)

Entrada contextual de ruta de archivo.

Tipo de dato: **Text**

### Get Geometry (parámetro)

Entrada contextual de geometría.

Tipo de dato: **Geometry**

### Get Integer (parámetro)

Entrada contextual de entero.

Tipo de dato: **Integer**

### Get Line (parámetro)

Entrada contextual de línea.

Tipo de dato: **Line**

### Get Number (parámetro)

Entrada contextual numérica.

Tipo de dato: **Number**

### Get Plane (parámetro)

Entrada contextual de plano.

Tipo de dato: **Plane**

### Get Point (parámetro)

Entrada contextual de punto.

Tipo de dato: **Point**

### Get String (parámetro)

Entrada contextual de texto.

Tipo de dato: **Text**

### Jump (objeto especial)

Salta entre distintas ubicaciones del lienzo

### Param Viewer (Viewer, parámetro)

Un visor de estructuras de datos.

Tipo de dato: **Path**

### Relay (parámetro)

Un objeto relé de conexiones (wire relay)

Tipo de dato: **Goo**

### Scribble (objeto especial)

Una nota rápida

### Suirify (parámetro)

Simplificación de árboles de datos al estilo Suirify.

Tipo de dato: **Goo**

### Trigger (objeto especial)

Dispara actualizaciones de ciertos componentes, de forma manual o cíclica.
