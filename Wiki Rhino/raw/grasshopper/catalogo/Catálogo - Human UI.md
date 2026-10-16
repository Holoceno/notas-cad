---
title: "Catálogo Grasshopper — Human UI"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Human UI"
libraries: ["Human UI 0.8.10"]
components: 81
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/human-ui, programacion/scripts]
---

# Human UI

81 objetos · librería: Human UI 0.8.10 · autor: Andrew Heumann

Mapas: [[Mapa - Scripts, interfaz y archivos]] (81)

## UI Containers

### Create Border (Border)

Envuelve elementos con un borde.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Element | `E` | Generic Data | item | El elemento de interfaz a incluir |
| Border Thickness | `T` | Number | item | Grosor del borde |
| Border Color | `C` | Colour | item | Color del borde |
| Corner Radius | `R` | Number | item | Radio de las esquinas del borde |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Border | `B` | Generic Data | item | El borde |

### Create Expander (Expander)

Un desplegable plegable para contenido

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Elements | `E` | Generic Data | lista | Los elementos de interfaz que van dentro del desplegable |
| Header | `H` | Text | item | El texto a mostrar en el encabezado del desplegable |
| Open | `O` | Boolean | item | El estado inicial del desplegable: True para abierto, False para plegado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Expander | `E` | Generic Data | item | El elemento desplegable |

### Create Grid (Grid)

Crea un contenedor con elementos en posición absoluta. El orden de entrada determina su orden Z; define los márgenes con el componente "Adjust Element Positioning" para ubicar los elementos dentro de la grilla. Usa definiciones de columnas y filas para crear grillas más avanzadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Elements | `E` | Generic Data | lista | Los elementos de interfaz que se colocan en la grilla |
| Width *(opcional)* | `W` | Number | item | El ancho de la grilla |
| Height *(opcional)* | `H` | Number | item | El alto de la grilla |
| Row Definitions *(opcional)* | `RD` | Text | lista | Lista opcional de altos de fila. Usa números para tamaños absolutos y números con * para proporciones (como 1* y 2* para una división 1/3 - 2/3) |
| Column Definitions *(opcional)* | `CD` | Text | lista | Lista opcional de anchos de columna. Usa números para tamaños absolutos y números con * para proporciones (como 1* y 2* para una división 1/3 - 2/3) |
| Element Row *(opcional)* | `ER` | Integer | lista | Las filas en las que se colocan los elementos, contando desde 0 arriba. |
| Element Column *(opcional)* | `EC` | Integer | lista | Las columnas en las que se colocan los elementos, contando desde 0 a la izquierda. |
| Element Row Span *(opcional)* | `ERS` | Integer | lista | Cuántas filas debe abarcar cada elemento. Por defecto es 1. |
| Element Column Span *(opcional)* | `ECS` | Integer | lista | Cuántas columnas debe abarcar cada elemento. Por defecto es 1. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Grid | `S` | Generic Data | item | El grupo combinado de elementos |

### Create Scroll Viewer (ScrollViewer)

Permite que un elemento se desplace (scroll) independientemente del resto de la ventana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Elements | `E` | Generic Data | lista | Los elementos de interfaz que van en el grupo desplazable |
| Horizontal Scroll Bar Visibility | `HV` | Integer | item | Si se muestra o no la barra de desplazamiento horizontal |
| Vertical Scroll Bar Visibility | `VV` | Integer | item | Si se muestra o no la barra de desplazamiento vertical |
| Width *(opcional)* | `W` | Number | item | El ancho de la región desplazable |
| Height *(opcional)* | `H` | Number | item | El alto de la región desplazable |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ScrollViewer | `S` | Generic Data | item | El grupo desplazable de elementos |

### Create Simple Grid (SimpleGrid)

Crea un contenedor con elementos en una grilla según la estructura de rutas entregada. Cada ruta de rama se trata como una columna y los elementos se colocan en la columna de arriba hacia abajo. Usa el componente "Adjust Element Positioning" para ubicar elementos dentro de la celda. Usa definiciones de columnas y filas para controlar los tamaños.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Elements | `E` | Generic Data | árbol | Los elementos de interfaz que se colocan en la grilla. Cada rama forma una columna con los elementos entregados, de arriba hacia abajo. |
| Grid Membership *(opcional)* | `M` | Integer | lista | Lista de índices para colocar elementos en distintas grillas. El largo de la lista debe coincidir con la cantidad de rutas de Elements. |
| Width *(opcional)* | `W` | Number | item | El ancho de la grilla |
| Height *(opcional)* | `H` | Number | item | El alto de la grilla |
| Row Definitions *(opcional)* | `RD` | Text | lista | Patrón repetitivo opcional de altos de fila: usa 'Auto' para heredar, números para tamaños absolutos y números con * para proporciones (como 1* y 2* para una división 1/3 - 2/3) |
| Column Definitions *(opcional)* | `CD` | Text | lista | Lista plana opcional de anchos de columna: usa 'Auto' para heredar, números para tamaños absolutos y números con * para proporciones (como 1* y 2* para una división 1/3 - 2/3) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Simple Grid | `S` | Generic Data | item | El grupo combinado de elementos |

### Create Stack (Stack)

Crea un grupo de elementos de interfaz apilados vertical u horizontalmente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Elements | `E` | Generic Data | lista | Los elementos de interfaz a agrupar |
| Horizontal | `H` | Boolean | item | Poner en True para ordenarlos en horizontal; False para vertical. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Stack | `S` | Generic Data | item | El grupo combinado de elementos |

### Create View Box (ViewBox)

Escala un grupo de elementos de interfaz colocándolos en un ViewBox.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Elements | `E` | Generic Data | lista | Los elementos de interfaz a escalar |
| Width | `W` | Number | item | El ancho del viewbox |
| Height | `H` | Number | item | El alto del viewbox |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ViewBox | `VB` | Generic Data | item | El viewbox |

### Create WrapPanel (WrapPanel)

Crea un grupo de elementos de interfaz en un WrapPanel, vertical u horizontal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Elements | `E` | Generic Data | lista | Los elementos de interfaz a agrupar |
| Horizontal | `H` | Boolean | item | Poner en True para ordenarlos en horizontal; False para vertical. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| WrapPanel | `S` | Generic Data | item | El grupo combinado de elementos |

### Tabbed View (Tabs)

Crea una serie de vistas con pestañas que pueden contener diseños de elementos de interfaz

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tab Names *(opcional)* | `N` | Text | lista | Las etiquetas de las pestañas que estás creando. |
| Tab Text Size *(opcional)* | `S` | Number | item | El tamaño de fuente de los elementos de las pestañas |
| Tab Icon Source *(opcional)* | `I` | Text | lista | La ruta a una imagen de ícono, una por pestaña |
| Tab 0 *(opcional)* | `T0` | Generic Data | lista | Los elementos de interfaz a incluir en la pestaña 0 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tabs | `T` | Generic Data | item | El control de pestañas |

## UI Elements

### Attach Tooltip to Element (Tooltip)

Agrega un tooltip a un elemento de interfaz

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Elements to Attach to | `E` | Generic Data | item | Los elementos a los que se agrega el tooltip |
| Tooltip Content | `C` | Generic Data | item | El contenido (texto o elementos) del tooltip |
| Show Delay | `SD` | Integer | item | Cuánto tiempo en ms pasa antes de mostrar el tooltip |
| Duration | `D` | Integer | item | Cuánto tiempo en ms se muestra el tooltip |

### Create 3D View (3DView)

Crea una vista 3D orbitable con una malla definida por el usuario

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh to display | `M` | Mesh | lista | La o las mallas a mostrar en la vista |
| Mesh Colors | `C` | Colour | lista | El color con que se muestra la malla. |
| View Width | `W` | Number | item | El ancho de la vista 3D |
| View Height | `H` | Number | item | El alto de la vista 3D |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 3DView | `V` | Generic Data | item | La vista 3D que contiene tu malla. |

### Create Browser (Browser)

Crea una ventana de navegador web.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| URL | `U` | Text | item | La URI/URL de la página a mostrar |
| Width *(opcional)* | `W` | Integer | item | Ancho de la ventana |
| Height *(opcional)* | `H` | Integer | item | Alto de la ventana |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Browser | `WB` | Generic Data | item | El navegador web creado |

### Create Button (Button)

Crea un objeto botón.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button Name *(opcional)* | `N` | Text | item | El texto a mostrar en el botón |
| Image Path *(opcional)* | `I` | Text | item | La imagen a mostrar en el botón. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button | `B` | Generic Data | item | El botón creado |

### Create Checkbox (Checkbox)

Crea una sola casilla de verificación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Label | `L` | Text | item | La etiqueta de la casilla. |
| Starting Value | `V` | Boolean | item | El valor inicial (marcada/desmarcada) de la casilla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Checkbox | `CB` | Generic Data | item | La casilla creada. |

### Create Checklist (Checklist)

Crea un cuadro de lista con casillas de verificación.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Checklist Items | `L` | Text | lista | La lista inicial de opciones a mostrar en la lista de casillas. |
| Selected | `S` | Boolean | lista | El estado inicial de todas las casillas. Por defecto todas desmarcadas. |
| Height *(opcional)* | `H` | Number | item | Alto opcional del cuadro de lista, en píxeles. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Checklist | `CL` | Generic Data | item | El objeto lista de casillas |

### Create Color Picker (ColorPicker)

Crea un selector de color interactivo, con un conjunto de colores opcional

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Default Color *(opcional)* | `D` | Colour | item | El color que muestra el selector al cargar. Opcional. |
| Available Colors *(opcional)* | `C` | Colour | lista | Lista opcional de colores posibles para limitar la selección del usuario. Si se deja vacía, se muestra el conjunto estándar de colores. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color Picker | `P` | Generic Data | item | El elemento de interfaz selector de color. Úsalo junto con un componente "Add Elements". |

### Create Data Table (DataTable)

Crea una vista de tabla de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Text | árbol | Los datos a mostrar en la tabla, organizados en ramas por columna. |
| Column Headings | `C` | Text | lista | El encabezado de cada columna, uno por cada columna de Data |
| Allow Sorting | `S` | Boolean | item | Poner en True para permitir ordenar por los valores de una columna |
| Column Sizing Mode | `CS` | Integer | item | Modo de tamaño de las columnas. Elige entre valores "especiales" predefinidos o entrega un ancho numérico fijo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| DataTable | `DT` | Generic Data | item | El elemento tabla de datos |

### Create File Picker (FilePicker)

Crea un cuadro de diálogo para elegir la ruta de un archivo, una carpeta o dónde guardar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button Label Text | `BT` | Text | item | El texto a mostrar en el botón a la derecha del cuadro de texto |
| Dialog Type | `DT` | Integer | item | El tipo de diálogo a mostrar: Open, Save o Folder |
| Must Exist | `ME` | Boolean | item | Poner en True si el archivo (en un diálogo de abrir) debe existir |
| Filter | `F` | Text | item | Los filtros de archivo a usar. Indica nombres de tipo separados de los filtros de ruta con el carácter \|, como "Grasshopper Files\|*.gh", y une varios también con \|. |
| Starting Path *(opcional)* | `SP` | Text | item | La carpeta inicial opcional con la que se abre el diálogo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Picker | `P` | Generic Data | item | El elemento selector de archivos |

### Create Gradient Editor (Gradient)

Crea un degradado editable en la interfaz

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Gradient(s) *(opcional)* | `G` | Generic Data | lista | El degradado o colección de degradados predefinidos a incluir. Si el menú de predefinidos no se muestra, los múltiples se ignoran. |
| Default Gradient *(opcional)* | `D` | Generic Data | lista | El degradado por defecto a mostrar; solo se usa si el menú de predefinidos está activado. |
| Show Editor | `E` | Boolean | item | Poner en True para mostrar un editor de degradado interactivo |
| Show Presets | `P` | Boolean | item | Poner en True para mostrar un menú desplegable de degradados predefinidos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Gradient Editor | `GE` | Generic Data | item | El elemento editor de degradado |

### Create Graph Mapper (GraphMapper)

Crea un Graph Mapper Bézier

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Graph Mapper *(opcional)* | `G` | Generic Data | item | Un Graph Mapper opcional que representa la configuración inicial. Conéctalo directamente o usa Metahopper para obtener una referencia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Graph Mapper | `G` | Generic Data | item | El elemento de interfaz Graph Mapper |

### Create Image (Image)

Crea un objeto imagen para agregar a la ventana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Image Source | `src` | Text | item | La ubicación del archivo de la imagen a agregar. |
| Image Width | `W` | Number | item | El ancho de la imagen |
| Image Height *(opcional)* | `H` | Number | item | El alto de la imagen. Pon 0 o déjalo vacío para escalar la imagen proporcionalmente a su ancho. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Image | `I` | Generic Data | item | El objeto imagen. Úsalo junto con un componente "Add Elements". |

### Create Label (Label)

Crea una etiqueta en la ventana.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Label Text | `T` | Text | item | El texto a mostrar en la etiqueta |
| Label Size | `S` | Integer | item | El tamaño de la etiqueta a mostrar |
| Justification | `J` | Integer | item | Justificación del texto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Label | `L` | Generic Data | item | Las etiquetas creadas. |

### Create List Box (ListBox)

Crea un cuadro de lista desde el que se pueden seleccionar elementos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List Items | `L` | Text | lista | La lista inicial de opciones a mostrar en la lista. |
| Selected Index | `I` | Integer | item | El índice seleccionado inicialmente. Por defecto, el primer elemento. |
| Height | `H` | Number | item | Alto del cuadro de lista, en píxeles. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List Box | `LB` | Generic Data | item | El objeto cuadro de lista |

### Create Markdown Viewer (MDV)

Crea un bloque de texto con formato a partir de una entrada en Markdown

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | El texto con formato Markdown que quieres mostrar |
| Styles File *(opcional)* | `SF` | Text | item | La ruta opcional a un archivo styles.xaml. Si no se entrega, se usan los valores por defecto |
| Asset Directory *(opcional)* | `AD` | Text | item | La carpeta raíz opcional para recursos como imágenes incrustadas en tu Markdown |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Markdown Viewer | `MDV` | Generic Data | item | El elemento visor de Markdown. |

### Create Multidimensional Slider (MD Slider)

Crea un slider 2D que va de {0,0} a {1,1}

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Starting Value *(opcional)* | `S` | Point | item | El punto inicial (entre 0,0 y 1,1) con el que quieres que parta el slider. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MD Slider | `S` | Generic Data | item | El slider 2D (MD Slider). |

### Create Objects from XAML (XAML)

Crea elementos de interfaz a partir de sintaxis XAML escrita

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| XAML | `X` | Text | item | El texto XAML |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object | `O` | Generic Data | item | El árbol de objetos XAML |

### Create Pulldown Menu (Pulldown)

Crea un menú desplegable desde el que se pueden seleccionar elementos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Label | `L` | Text | item | Etiqueta opcional del cuadro de texto |
| List Items | `L` | Generic Data | lista | La lista inicial de opciones a mostrar en la lista. |
| Selected Index *(opcional)* | `I` | Integer | item | El índice seleccionado inicialmente. Por defecto, el primer elemento. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pulldown | `PD` | Generic Data | lista | El objeto menú desplegable |

### Create Radio Button (RadioBtn)

Crea un solo botón de opción (radio button). Asegúrate de asignarle un grupo para que se alternen correctamente

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Radio Button Name | `N` | Text | item | El nombre del botón de opción. |
| Radio Button Group | `G` | Text | item | El grupo al que pertenece el botón de opción. Solo se puede seleccionar un botón por grupo a la vez. |
| Initially Selected | `S` | Boolean | item | Si este botón debe estar seleccionado al inicio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Radio Button | `RB` | Generic Data | item | El botón de opción creado. |

### Create Range Slider (RangeSlider)

Crea un slider doble que describe un rango

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Slider Range | `R` | Domain | item | El rango que define el mínimo y el máximo del slider |
| Starting Range | `SR` | Domain | item | El valor inicial seleccionado en el slider |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Range Slider | `RS` | Generic Data | item | El elemento slider de rango. |

### Create Rhino Command Button (CmdButton)

Crea un botón especial que ejecuta un comando de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button Name *(opcional)* | `N` | Text | item | El texto a mostrar en el botón |
| Image Path *(opcional)* | `I` | Text | item | La imagen a mostrar en el botón. |
| Rhino Script | `S` | Text | item | El script de línea de comandos que se ejecuta al presionar el botón |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button | `B` | Generic Data | item | El botón creado |

### Create Rhino Pick Button (PickBtn)

Crea un botón especial para seleccionar geometría desde Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button Name *(opcional)* | `N` | Text | item | El texto a mostrar en el botón |
| Image Path *(opcional)* | `I` | Text | item | La imagen a mostrar en el botón. |
| Prompt | `P` | Text | item | El mensaje a mostrar al usuario |
| Allow Multiple | `AM` | Boolean | item | Poner en True para permitir seleccionar varios elementos |
| Allow None | `AN` | Boolean | item | Poner en True para permitir no seleccionar nada |
| Type | `T` | Integer | item | Los tipos de geometría permitidos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button | `B` | Generic Data | item | El botón creado |

### Create Separator (Separator)

Crea un objeto separador de línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Thickness | `T` | Number | item | El grosor del separador. |
| Horizontal | `H` | Boolean | item | El separador es horizontal. |
| Color *(opcional)* | `C` | Colour | item | El color del separador (opcional). |
| Width *(opcional)* | `W` | Number | item | El ancho del separador (opcional). Por defecto es Stretch. |
| Height *(opcional)* | `H` | Number | item | El alto del separador (opcional). Por defecto es Stretch. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Separator | `S` | Generic Data | item | El separador creado |

### Create Shape (Shape)

Crea una forma simple a partir de una polilínea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Curve | lista | La forma a agregar, como polilínea(s) |
| Fill Color *(opcional)* | `FC` | Colour | item | El color de relleno. Déjalo vacío para no rellenar |
| Stroke Weight *(opcional)* | `SW` | Number | item | El grosor del trazo. Déjalo vacío o en 0 para no tener trazo. |
| Stroke Color *(opcional)* | `SC` | Colour | item | El color del trazo |
| Scale *(opcional)* | `Scl` | Number | item | Usa este valor para cambiar el tamaño de la forma. |
| Width *(opcional)* | `W` | Integer | item | El ancho del contenedor de la forma. Déjalo vacío para ajuste automático. |
| Height *(opcional)* | `H` | Integer | item | El alto del contenedor de la forma. Déjalo vacío para ajuste automático. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Generic Data | item | La forma creada. |

### Create Shapes (Shapes)

Crea formas a partir de polilíneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shapes | `S` | Curve | lista | Las formas a agregar, como polilínea(s) |
| Fill Color *(opcional)* | `FC` | Colour | lista | Los colores de relleno. Déjalo vacío para no rellenar |
| Stroke Weight *(opcional)* | `SW` | Number | lista | Los grosores de trazo. Déjalo vacío o en 0 para no tener trazo. |
| Stroke Color *(opcional)* | `SC` | Colour | lista | Los colores de trazo |
| Scale *(opcional)* | `Scl` | Number | item | Usa este valor para cambiar el tamaño de la forma. |
| Width *(opcional)* | `W` | Integer | item | El ancho del contenedor de la forma. Déjalo vacío para ajuste automático. |
| Height *(opcional)* | `H` | Integer | item | El alto del contenedor de la forma. Déjalo vacío para ajuste automático. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Generic Data | item | La forma creada. |

### Create Slider (Slider)

Crea un slider con una etiqueta y una lectura del valor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Slider | `Sl` | Generic Data | árbol | El o los sliders a agregar a la ventana. |
| Snap Value *(opcional)* | `Sn` | Number | lista | Un valor opcional al que redondear/ajustar el slider. Reemplaza la configuración nativa del slider de GH. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sliders | `S` | Generic Data | lista | Los elementos de interfaz slider. Úsalos junto con un componente "Add Elements". |

### Create Text Block (TB)

Crea un bloque de texto de varias líneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | El texto a mostrar en el bloque de texto |
| Text Size | `S` | Integer | item | El tamaño de la etiqueta a mostrar |
| Justification | `J` | Integer | item | Justificación del texto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Block | `TB` | Generic Data | item | El bloque de texto creado. |

### Create Text Box (TextBox)

Crea un cuadro para ingresar texto, con un botón para pasar su valor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Label | `L` | Text | item | Etiqueta opcional del cuadro de texto |
| Default Text | `D` | Text | item | El texto inicial del cuadro de texto |
| Update Button | `U` | Boolean | item | Poner en True para asociar el cuadro de texto a un botón para las actualizaciones. Si no, cada cambio en el contenido del cuadro dispara el evento. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Box | `TB` | Generic Data | item | El cuadro de texto creado. |

### Create Toggle (Toggle)

Crea un interruptor de encendido/apagado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Default | `D` | Boolean | item | Si el interruptor está encendido por defecto |
| Label *(opcional)* | `L` | Text | item | La etiqueta opcional del interruptor |
| On Label *(opcional)* | `On` | Text | item | El texto a mostrar cuando está encendido |
| Off Label *(opcional)* | `Off` | Text | item | El texto a mostrar cuando está apagado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Toggle | `T` | Generic Data | item | El elemento interruptor. |

### Create True-Only Button (True Button)

Crea un objeto botón que solo entrega True.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button Name *(opcional)* | `N` | Text | item | El texto a mostrar en el botón |
| Image Path *(opcional)* | `I` | Text | item | La imagen a mostrar en el botón. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button | `B` | Generic Data | item | El botón creado |

## UI Graphs + Charts

### Chart Appearance (ChartAppearance)

Úsalo para definir la apariencia de un gráfico

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Chart to modify | `C` | Generic Data | item | El objeto gráfico a modificar |
| Colors *(opcional)* | `Co` | Colour | lista | Los colores del gráfico |
| Legend *(opcional)* | `L` | Boolean | item | ¿Mostrar leyenda? |
| Title *(opcional)* | `T` | Boolean | item | ¿Mostrar título? |

### Create Chart (Chart)

Crea un gráfico a partir de datos y categorías.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Number | lista | La lista de valores a graficar. |
| Names | `N` | Text | lista | Los nombres de los datos a graficar |
| Title *(opcional)* | `T` | Text | item | El título del gráfico |
| SubTitle *(opcional)* | `sT` | Text | item | El subtítulo del gráfico |
| Chart Type | `CT` | Integer | item | El tipo de gráfico a crear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Chart | `C` | Generic Data | item | El objeto gráfico |

### Create Multi Chart (MultiChart)

Crea un gráfico múltiple a partir de conjuntos de datos y categorías.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Number | árbol | La lista de valores a graficar. |
| Names | `N` | Text | lista | Los nombres de los datos a graficar |
| Title *(opcional)* | `T` | Text | item | El título del gráfico |
| SubTitle *(opcional)* | `sT` | Text | item | El subtítulo del gráfico |
| ClusterTitle | `cT` | Text | lista | El título de cada grupo del gráfico |
| Chart Type | `CT` | Integer | item | El tipo de gráfico a crear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| MultiChart | `MC` | Generic Data | lista | El objeto gráfico múltiple |

### Set Chart Contents (SetChart)

Úsalo para definir el contenido de un gráfico

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Chart to modify | `C` | Generic Data | item | El objeto gráfico a modificar |
| New Chart Values *(opcional)* | `V` | Number | lista | Los nuevos valores a incluir en el gráfico |
| New Chart Names *(opcional)* | `N` | Text | lista | Los nombres de los datos a graficar |
| Title *(opcional)* | `T` | Text | item | El título del gráfico |
| SubTitle *(opcional)* | `sT` | Text | item | El subtítulo del gráfico |

### Set Multi Chart Contents (SetMultiChart)

Úsalo para definir el contenido de un gráfico múltiple

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Chart to modify | `G` | Generic Data | item | El objeto gráfico múltiple a modificar |
| New Chart Values | `D` | Number | árbol | Los nuevos valores a incluir en el gráfico múltiple |
| New Chart Names *(opcional)* | `N` | Text | lista | Los nombres de los datos a graficar |
| Title *(opcional)* | `T` | Text | item | El título del gráfico |
| SubTitle *(opcional)* | `sT` | Text | item | El subtítulo del gráfico |
| ClusterTitle *(opcional)* | `cT` | Text | lista | El título de cada grupo de barras |

## UI Main

### Add Elements (AddElems)

Agrega controles WPF a una ventana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Window | `W` | Generic Data | item | La ventana a la que se agregan los elementos |
| Elements | `E` | Generic Data | lista | Los controles y demás elementos que quieres agregar a la ventana |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Added Elements | `E` | Generic Data | lista | Los elementos agregados. |
| Element Names | `N` | Text | lista | Los nombres de los elementos agregados. |

### Adjust Element Appearance (AdjustElem)

Ajusta el color y la apariencia de elementos individuales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Elements to Adjust | `E` | Generic Data | item | Los elementos a ajustar |
| Foreground *(opcional)* | `FC` | Colour | item | El color de primer plano del elemento |
| Background *(opcional)* | `BC` | Colour | item | El color de fondo del elemento |
| Font Size *(opcional)* | `S` | Number | item | El tamaño de fuente del elemento |

### Adjust Element Positioning (AdjustPos)

Ajusta los márgenes, el tamaño y otros datos de posición de un elemento. El posicionamiento absoluto puede comportarse de forma rara; úsalo bajo tu propio riesgo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Elements to adjust | `E` | Generic Data | item | El UIElement que quieres reubicar. |
| Margin *(opcional)* | `M` | Text | item | El valor del margen. Ingresa un solo número para todos los lados, o cuatro valores separados por comas para definir izquierda, arriba, derecha y abajo por separado. |
| Absolute Positioning | `Abs` | Boolean | item | Poner en True para posicionar respecto de la esquina superior izquierda del documento |
| Width *(opcional)* | `W` | Number | item | Reemplaza el ancho del elemento |
| Height *(opcional)* | `H` | Number | item | Reemplaza el alto del elemento |
| Horizontal Alignment *(opcional)* | `HA` | Integer | item | Alineación horizontal |
| Vertical Alignment *(opcional)* | `VA` | Integer | item | Alineación vertical |

### Capture Window or Element to File (Capture)

Captura una ventana de HUI o un elemento individual como imagen

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Window or Element | `W` | Generic Data | item | La ventana a capturar |
| File Path | `F` | Text | item | La ruta del archivo donde se guarda la imagen |
| Scale Factor | `S` | Number | item | Un factor de escala aplicado al tamaño de la ventana o elemento para capturas en alta resolución |
| Run | `R` | Boolean | item | Poner en True para activar la captura. |
| Capture Entire Window | `EW` | Boolean | item | Si se entrega una ventana, captura todo su contenido dentro del área desplazable. No se muestra la barra de título. Este parámetro se ignora si se entrega un elemento específico. |

### Get Element Properties (GetProps)

Intenta obtener todas las propiedades de cualquier elemento. ¡Es experimental!

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Element | `E` | Generic Data | item | El elemento del que obtener las propiedades |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Property Names | `N` | Text | lista | Los nombres de las propiedades |
| Property Types | `T` | Text | lista | Los tipos de las propiedades |

### Get Screen Dimensions (GetScreen)

Obtiene las dimensiones de la pantalla actual

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Width | `W` | Number | item | Ancho |
| Height | `H` | Number | item | Alto |

### Hide/Show Element (HideShow)

Permite ocultar o mostrar un elemento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Element to Hide/Show | `E` | Generic Data | item | Los elementos a ocultar/mostrar |
| Show | `S` | Boolean | item | Poner en True para mostrar el elemento, False para ocultarlo |
| Collapse | `C` | Boolean | item | Si es True, no se reserva espacio para el elemento; si es False, el espacio se mantiene pero el elemento se oculta |
| Disable | `D` | Boolean | item | Si es True, el elemento se verá "en gris" y el usuario no podrá interactuar con él. |

### Launch Transparent Window (LaunchXPWin)

Este componente abre una nueva ventana de controles, vacía y transparente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Show | `S` | Boolean | item | Pon este booleano en True para mostrar la ventana de controles. |
| Name | `N` | Text | item | El nombre de la ventana a mostrar. |
| Width | `W` | Integer | item | Ancho inicial de la ventana. |
| Height | `H` | Integer | item | Alto inicial de la ventana. |
| Font Family *(opcional)* | `F` | Text | item | Familia tipográfica opcional para los elementos de interfaz de esta ventana. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Window Object | `W` | Generic Data | item | El objeto ventana. Otros componentes pueden acceder a él para agregar controles u obtener datos de la ventana. |

### Launch Window (LaunchWin)

Este componente abre una nueva ventana de controles vacía.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Show | `S` | Boolean | item | Pon este booleano en True para mostrar la ventana de controles. |
| Name | `N` | Text | item | El nombre de la ventana a mostrar. |
| Width | `W` | Integer | item | Ancho inicial de la ventana. |
| Height | `H` | Integer | item | Alto inicial de la ventana. |
| Font Family *(opcional)* | `F` | Text | item | Familia tipográfica opcional para los elementos de interfaz de esta ventana. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Window Object | `W` | Generic Data | item | El objeto ventana. Otros componentes pueden acceder a él para agregar controles u obtener datos de la ventana. |

### Make Child Window (ChildWin)

Hace que una ventana sea hija de otra

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Parent Window | `P` | Generic Data | item | La ventana madre |
| Child Window | `C` | Generic Data | item | La ventana hija |
| Default Option *(opcional)* | `D` | Integer | item | Úsalo si quieres devolver la ventana hija a uno de los modos por defecto y romper su relación con la madre. |

### Restore Element States (Restore)

Restaura los estados guardados de los elementos de interfaz

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Restore | `R` | Boolean | item | Poner en True para restaurar el estado. Probablemente no conviene dejarlo en True mientras agregas estados nuevos. |
| Saved States | `SS` | Generic Data | item | La colección de estados guardados |
| State Name to restore | `N` | Text | item | El nombre del estado a restaurar |

### Save Element States (SaveStates)

Este componente permite guardar el estado de los elementos seleccionados para recuperarlo después

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Elements | `E` | Generic Data | lista | Todos los controles y demás elementos de la ventana |
| Name Filter(s) *(opcional)* | `F` | Text | lista | Los filtros opcionales de los elementos que quieres guardar. |
| Save State | `S` | Boolean | item | Poner en True para guardar el estado actual de todos los elementos seleccionados |
| State Name | `N` | Text | item | El nombre con el que se guarda el estado. Si el nombre ya existe, el estado guardado se sobrescribe |
| Clear Saved States | `C` | Boolean | item | Poner en True para borrar todos los estados guardados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Saved States | `SS` | Generic Data | item | Los estados guardados de los elementos. Conéctalos a un componente "Restore State" para restaurarlos. |
| Saved State Names | `N` | Text | lista | Los nombres de todos los estados guardados |

### Set Element Property (SetProp)

Intenta definir cualquier propiedad de un elemento. ¡Es experimental!

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Element | `E` | Generic Data | item | El elemento a modificar |
| Property Name | `P` | Text | item | El nombre de la propiedad a definir |
| Value to set | `V` | Generic Data | item | El valor u objeto que se asigna a la propiedad |

### Set Window Properties (WinProps)

Modifica varias propiedades de una ventana.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Window | `W` | Generic Data | item | La ventana a modificar |
| Starting Location *(opcional)* | `L` | Point | item | El punto (en coordenadas de pantalla: 0,0 es arriba a la izquierda) donde se ubica la esquina superior izquierda de la ventana. |
| Theme *(opcional)* | `T` | Integer | item | El tema base de la ventana. |
| Accent Color *(opcional)* | `A` | Text | item | El color de acento de la ventana. Usa la opción "Create Accent List" del menú del componente para no tener que adivinar |
| Show Title Bar *(opcional)* | `TB` | Boolean | item | Poner en False para ocultar la barra de título de la ventana. |
| Background Color *(opcional)* | `BG` | Colour | item | Define el color de fondo de la ventana. |
| Scale Factor | `SF` | Number | item | Un factor de escala absoluto para modificar el tamaño de la ventana. |

### Value Listener (Values)

Este componente obtiene los valores de los elementos de interfaz de la ventana. Por defecto se actualiza solo cuando esos valores cambian.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Elements | `E` | Generic Data | lista | Elemento(s) de interfaz a escuchar. Se pueden obtener directamente del componente que creó el elemento o de la salida del componente "Add Elements". |
| Name Filter(s) *(opcional)* | `F` | Text | lista | Los filtros opcionales de los elementos que quieres escuchar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `V` | Generic Data | árbol | Los valores de los elementos escuchados |
| Indices | `I` | Integer | árbol | En objetos de tipo lista (lista de casillas, menú desplegable, etc.) devuelve el índice seleccionado; si no, devuelve -1. |

### Window Status (WinStat)

Obtiene el estado actual de la ventana indicada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Window | `W` | Generic Data | item | La ventana a revisar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Status | `S` | Text | item | El estado de la ventana |

## UI Output

### Add Elements to Shape(s) (AddElem2Shape)

Pone elementos de interfaz (¡como texto!) encima de un elemento de forma(s)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape to add to | `S` | Generic Data | item | El objeto forma al que se agregan los elementos |
| Element to add | `E` | Generic Data | lista | El o los elementos a agregar a las formas. Para texto usa, por ejemplo, un TextBlock o un Label. |
| Element Location | `L` | Point | lista | El punto en el que se posiciona el elemento |
| Scale | `Sc` | Number | item | La escala (debe coincidir con la que usas para tu forma) |

### Set 3D View (Set3DView)

Permite modificar el contenido de una vista 3D existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 3D View | `V` | Generic Data | item | La vista 3D a modificar |
| Mesh to display | `M` | Mesh | lista | La o las mallas a mostrar en la vista |
| Mesh Colors *(opcional)* | `C` | Colour | lista | El color con que se muestra la malla. |

### Set 3D View Properties (Set3DViewProps)

Controles adicionales para modificar una vista 3D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 3D View | `V` | Generic Data | item | La vista 3D a modificar |
| Show View Cube *(opcional)* | `VC` | Boolean | item | Mostrar el cubo de vista |
| Allow Pan *(opcional)* | `AP` | Boolean | item | Permitir que el usuario desplace (pan) la vista 3D |
| Allow Zoom *(opcional)* | `AZ` | Boolean | item | Permitir que el usuario haga zoom en la vista 3D |
| Allow Move *(opcional)* | `AM` | Boolean | item | Permitir que el usuario mueva la vista 3D |
| Allow Rotation *(opcional)* | `AR` | Boolean | item | Permitir que el usuario rote la vista 3D |
| Perspective/Parallel *(opcional)* | `Par` | Boolean | item | Poner en True para vista paralela, False para perspectiva |
| Camera Location *(opcional)* | `CL` | Point | item | La ubicación de la cámara |
| Camera Target *(opcional)* | `CT` | Point | item | El objetivo de la cámara |
| Camera Transition Time *(opcional)* | `CTT` | Number | item | El tiempo que tarda en actualizarse la posición de la cámara |

### Set 3D View Textured (Set3DViewTex)

Permite modificar el contenido de una vista 3D existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 3D View | `V` | Generic Data | item | La vista 3D a modificar |
| Mesh to display | `M` | Mesh | lista | La o las mallas a mostrar en la vista |
| Mesh Colors *(opcional)* | `C` | Colour | lista | El color con que se muestra la malla. |
| Mesh Texture | `T` | Text | lista | Las texturas con que se muestra cada malla |

### Set Browser (SetBrowser)

Controla el elemento navegador: botones atrás/adelante, el sitio mostrado, etc.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Browser | `B` | Generic Data | item | El elemento de interfaz navegador a modificar |
| Back *(opcional)* | `Bk` | Boolean | item | Poner en True para que el navegador retroceda una página |
| Forward *(opcional)* | `Fwd` | Boolean | item | Poner en True para que el navegador avance una página |
| Refresh *(opcional)* | `Rf` | Boolean | item | Poner en True para recargar la ventana actual |
| URL *(opcional)* | `U` | Text | item | La URL a la que debe acceder el navegador. |

### Set Button (SetBtn)

Cambia el contenido de un elemento botón existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Button to modify | `B` | Generic Data | item | El objeto botón a modificar |
| Button Name *(opcional)* | `N` | Text | item | El nuevo texto a mostrar en el botón |
| Image Path *(opcional)* | `I` | Text | item | La nueva imagen a mostrar en el botón. |

### Set CheckBox (SetCheckBox)

Modifica un objeto casilla de verificación existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Check Box to modify | `CB` | Generic Data | item | El objeto casilla a modificar |
| New Check Box Label *(opcional)* | `L` | Text | item | La nueva etiqueta a mostrar junto a la casilla |
| New Value *(opcional)* | `V` | Boolean | item | El nuevo valor (marcada/desmarcada) de la casilla. |

### Set Checklist Contents (SetChecklist)

Úsalo para definir el contenido de una lista de casillas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Checklist to modify | `L` | Generic Data | item | El objeto lista a modificar |
| New checklist contents | `C` | Text | lista | Los nuevos elementos a mostrar en la lista de casillas |
| Selected *(opcional)* | `S` | Boolean | lista | Valores booleanos opcionales que controlan si los elementos están seleccionados |

### Set Color Picker (SetColorPicker)

Úsalo para definir los valores de un selector de color

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color picker to modify | `CP` | Generic Data | item | El objeto selector de color a modificar |
| Default Color *(opcional)* | `D` | Colour | item | El color que muestra el selector. Opcional. |
| Available Colors *(opcional)* | `C` | Colour | lista | Lista opcional de colores posibles para limitar la selección del usuario. Si se deja vacía, no cambia el conjunto de colores disponibles. |

### Set Data Table (SetDataTable)

Actualiza el contenido de una tabla de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data Table to Set | `DT` | Generic Data | item | La tabla de datos a modificar |
| Data | `D` | Text | árbol | Los datos a mostrar en la tabla, organizados en ramas por columna. |
| Column Headings *(opcional)* | `C` | Text | lista | El encabezado de cada columna, uno por cada columna de Data |

### Set Expander (SetExp)

Define las propiedades de un contenedor desplegable

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Expander | `E` | Generic Data | item | El desplegable a modificar |
| Name *(opcional)* | `N` | Text | item | El nuevo nombre del desplegable |
| Expanded Open *(opcional)* | `O` | Boolean | item | Poner en True para desplegar o False para plegar |

### Set Image (SetImg)

Cambia el contenido de un control de imagen existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Image to modify | `I` | Generic Data | item | El objeto imagen a modificar |
| New Image Path | `I2` | Text | item | La ruta a una nueva imagen que reemplaza a la de la ventana |

### Set Label Contents (SetLabel)

Modifica el contenido de un objeto etiqueta existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Label to modify | `L` | Generic Data | item | El objeto etiqueta a modificar |
| New Label contents | `C` | Text | item | El nuevo texto a mostrar en la etiqueta |

### Set List Contents (SetList)

Úsalo para definir el contenido de un cuadro de lista o de un menú desplegable

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List to modify | `L` | Generic Data | item | El objeto lista a modificar |
| New list contents | `C` | Text | lista | Los nuevos elementos a mostrar en la etiqueta |
| Selected Index *(opcional)* | `I` | Integer | item | El índice opcional a seleccionar en la lista actualizada |

### Set Multidimensional Slider (SetMDSlider)

Modifica el valor de un slider multidimensional.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI MD Slider | `S` | Generic Data | item | El slider multidimensional de la interfaz a actualizar |
| Point *(opcional)* | `P` | Point | item | El punto en el que se fija el slider multidimensional |

### Set Shape (SetShape)

Reemplaza una forma existente en la ventana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape to Modify | `S` | Generic Data | item | El objeto forma a modificar. |
| Shape Curve *(opcional)* | `SC` | Curve | lista | La forma a agregar, como polilínea(s) |
| Fill Color *(opcional)* | `FC` | Colour | item | El color de relleno. Déjalo vacío para no rellenar |
| Stroke Weight *(opcional)* | `SW` | Number | item | El grosor del trazo. Déjalo vacío o en 0 para no tener trazo. |
| Stroke Color *(opcional)* | `SC` | Colour | item | El color del trazo |
| Scale *(opcional)* | `Scl` | Number | item | Usa este valor para cambiar el tamaño de la forma. |
| Width *(opcional)* | `W` | Integer | item | El ancho del contenedor de la forma. Déjalo vacío para ajuste automático. |
| Height *(opcional)* | `H` | Integer | item | El alto del contenedor de la forma. Déjalo vacío para ajuste automático. |

### Set Shapes (SetShapes)

Reemplaza una forma existente en la ventana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape to Modify | `S` | Generic Data | item | El objeto forma a modificar. |
| Shape Curves *(opcional)* | `SC` | Curve | lista | Las formas a agregar, como polilínea(s) |
| Fill Colors *(opcional)* | `FC` | Colour | lista | Los colores de relleno. Déjalo vacío para no rellenar |
| Stroke Weights *(opcional)* | `SW` | Number | lista | El grosor del trazo. Déjalo vacío o en 0 para no tener trazo. |
| Stroke Colors *(opcional)* | `SC` | Colour | lista | El color del trazo |
| Scale *(opcional)* | `Scl` | Number | item | Usa este valor para cambiar el tamaño de la forma. |
| Width *(opcional)* | `W` | Integer | item | El ancho del contenedor de la forma. Déjalo vacío para ajuste automático. |
| Height *(opcional)* | `H` | Integer | item | El alto del contenedor de la forma. Déjalo vacío para ajuste automático. |

### Set Slider (SetSlider)

Modifica el rango y el valor de un slider.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| UI Slider | `S` | Generic Data | item | El slider de la interfaz a actualizar |
| Value *(opcional)* | `V` | Number | item | El valor en el que se fija el slider |
| Range *(opcional)* | `R` | Domain | item | El nuevo rango del slider |

### Set Tabbed View (SetTab)

Define las propiedades de una vista con pestañas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tabbed View | `T` | Generic Data | item | La vista con pestañas a modificar |
| Tab Names *(opcional)* | `N` | Text | lista | La lista de nombres de cada pestaña (opcional) |
| Show Tabs *(opcional)* | `S` | Boolean | lista | Entrega una lista de booleanos para ocultar/mostrar pestañas de forma selectiva (opcional) |
| Set Tab Index *(opcional)* | `I` | Integer | item | El índice de la pestaña a seleccionar (opcional) |

### Set TextBlock Contents (SetTextBlock)

Modifica el contenido de un objeto bloque de texto existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Block to modify | `TB` | Generic Data | item | El objeto bloque de texto a modificar |
| New Text Block contents | `C` | Text | item | El nuevo texto a mostrar en el bloque de texto |

### Set TextBox Contents (SetTextBox)

Modifica el contenido de un objeto cuadro de texto existente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Box to modify | `TB` | Generic Data | item | El objeto cuadro de texto a modificar |
| New Text Box contents | `C` | Text | item | El nuevo texto a mostrar en el cuadro de texto |
