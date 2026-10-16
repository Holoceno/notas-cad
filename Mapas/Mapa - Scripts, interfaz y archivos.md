---
tags: [tipo/mapa, programacion/scripts, programacion/interfaz, programacion/archivos, software/grasshopper, lenguaje/python, lenguaje/csharp]
---

# Scripts, interfaz y archivos

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Todo lo que no es geometría pura: componentes de **script** (Python 3, C#), **entradas** (sliders, botones, listas de valores), **bucles** (Anemone), **interfaces** propias (Human UI) y **archivos** (Excel, CSV, JSON, leer y escribir). Para aprender a programar ver [[Mapa - Programación]].

## Teoría y código
- [[Mapa - Programación]]: Python, C#, RhinoCommon y pruebas
- [[wiki/sources/2026-10-13-guias-scripting-rhino8]]: el componente Script por dentro (Script-Mode y SDK-Mode, Type Hints, acceso Item/List/Tree, paquetes)
- [[wiki/concepts/python-csharp-rhinocommon]] · [[wiki/concepts/plugins-rhino-grasshopper]] (publicar componentes Script como plugin)
- [[wiki/sources/2026-05-04-rhinopy-input-ui]]: opciones de línea de comandos, filtros, GetPoint
- [[wiki/concepts/data-trees]]: List Access en scripts (una ejecución por rama)

## Para empezar
- Scripts: [[Catálogo - Maths#Python 3 Script (Py3)|Python 3 Script]] · [[Catálogo - Maths#C♯ Script (C♯)|C♯ Script]] · [[Catálogo - Maths#Expression|Expression]]
- Entradas: [[Catálogo - Params#Number Slider (parámetro)|Number Slider]] · [[Catálogo - Params#Boolean Toggle (Toggle, parámetro)|Boolean Toggle]] · [[Catálogo - Params#Button (parámetro)|Button]] · [[Catálogo - Params#Value List (List, parámetro)|Value List]] · [[Catálogo - Params#Panel (parámetro)|Panel]]
- Control: [[Catálogo - Params#Data Dam (Dam)|Data Dam]] · [[Catálogo - Anemone#Loop Start|Loop Start]] / [[Catálogo - Anemone#Loop End|Loop End]]
- Archivos: [[Catálogo - Params#Read File (File)|Read File]] · [[Catálogo - LunchBox#Excel Reader (ExcelRead)|Excel Reader]] · [[Catálogo - LunchBox#Read CSV (CSV)|Read CSV]] · [[Catálogo - LunchBox#Create JSON (JSON)|Create JSON]]
- Interfaz: [[Catálogo - Human UI#Launch Window (LaunchWin)|Launch Window]] · [[Catálogo - Human UI#Add Elements (AddElems)|Add Elements]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (19)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Command Line Options | [[Add Command Line Options\|Py]] · [[Add Command Line Options (cs)\|C#]] | Opciones en la línea de comandos: entero, decimal, sí/no y lista | `GetPoint.AddOptionInteger / AddOptionToggle / AddOptionList` |
| Array By Distance | [[Array By Distance\|Py]] · [[Array By Distance (cs)\|C#]] | Matriz a lo largo de una dirección con vista previa mientras se mueve el mouse | `Transform.Translation + GetPoint.DynamicDraw (DrawObject)` |
| Custom Geometry Filter | [[Custom Geometry Filter\|Py]] · [[Custom Geometry Filter (cs)\|C#]] | Selección que solo acepta círculos de radio 10 | `función filtro en rs.GetObject / GetObject.SetCustomGeometryFilter` |
| Custom Python | [[Custom Python (cs)\|C#]] | Ejecuta un script de Python desde un comando en C# | `Rhino.Runtime.PythonScript.Create → ExecuteScript` |
| Custom Undo | [[Custom Undo\|Py]] · [[Custom Undo (cs)\|C#]] | Registra acciones propias en Deshacer y Rehacer | `doc.AddCustomUndoEvent(nombre, funcion, dato)` |
| Determine Language Setting | [[Determine Language Setting\|Py]] · [[Determine Language Setting (cs)\|C#]] | Idioma de la interfaz de Rhino | `rs.LocaleID → CultureInfo` |
| Display Conduit | [[Display Conduit (cs)\|C#]] | Conduit básico: dibuja los ejes del plano de construcción | `DisplayConduit.CalculateBoundingBox / PreDrawObjects` |
| Dynamically Draw Geometry when Picking Points | [[Dynamically Draw Geometry when Picking Points\|Py]] · [[Dynamically Draw Geometry when Picking Points (cs)\|C#]] | Vista previa de un círculo mientras se elige el radio | `clase GetPoint propia con OnDynamicDraw` |
| Dynamically Drawing Text Strings | [[Dynamically Drawing Text Strings\|Py]] · [[Dynamically Drawing Text Strings (cs)\|C#]] | Texto en pantalla que sigue al cursor (coordenadas de pantalla) | `Viewport.GetTransform(World, Screen), e.Display.Draw2dText` |
| Export Control Points | [[Export Control Points (cs)\|C#]] | Escribe los puntos de control de una curva en un archivo de texto | `ToNurbsCurve().Points → SaveFileDialog → StreamWriter` |
| Get Angle | [[Get Angle\|Py]] · [[Get Angle (cs)\|C#]] | Pide un ángulo con el mouse desde un punto base | `RhinoGet.GetAngle(...)` |
| Get Multiple With Options | [[Get Multiple With Options\|Py]] · [[Get Multiple With Options (cs)\|C#]] | Selección múltiple con opciones y preselección | `GetObject.GetMultiple + AddOptionInteger, EnablePreSelect` |
| Orthogonal Mode | [[Orthogonal Mode\|Py]] · [[Orthogonal Mode (cs)\|C#]] | Activa el modo Orto mientras se elige un punto | `ApplicationSettings.ModelAidSettings.Ortho` |
| Pick Point | [[Pick Point\|Py]] · [[Pick Point (cs)\|C#]] | Pide un punto o selecciona objetos punto | `GetPoint / GetObject con ObjectType.Point` |
| Pick Points | [[Pick Points (cs)\|C#]] | Puntos temporales dibujados con un conduit y seleccionables | `DisplayConduit + clase GetPoint propia` |
| Pre and Post-Pick Objects | [[Pre and Post-Pick Objects\|Py]] · [[Pre and Post-Pick Objects (cs)\|C#]] | Combina la preselección con la selección posterior | `GetObject.EnablePreSelect / EnablePostSelect` |
| Replace the Color Picking Dialog | [[Replace the Color Picking Dialog (cs)\|C#]] | Reemplaza el diálogo de color de Rhino por uno propio | `Dialogs.SetCustomColorDialog` |
| Tweak Colors | [[Tweak Colors (cs)\|C#]] | Cambia los colores de la interfaz de Rhino | `AppearanceSettings.SetPaintColor` |
| User Data | [[User Data (cs)\|C#]] | Guarda datos propios dentro de un objeto (viajan en el .3dm) | `clase UserData con Read / Write (ArchivableDictionary)` |

## Componentes de Grasshopper (209)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Input (24)

- [[Catálogo - Params#Atom Data (Atom)|Atom Data (Atom)]] — Obtiene información detallada de un átomo
- [[Catálogo - Params#Boolean Toggle (Toggle, parámetro)|Boolean Toggle (Toggle, parámetro)]] — Interruptor booleano (True/False)
- [[Catálogo - Params#Button (parámetro)|Button (parámetro)]] — Objeto botón con dos valores
- [[Catálogo - Params#Calendar (parámetro)|Calendar (parámetro)]] — Representa un calendario
- [[Catálogo - Params#Clock (parámetro)|Clock (parámetro)]] — Representa un reloj de 24 horas
- [[Catálogo - Params#Colour Picker (Colour, parámetro)|Colour Picker (Colour, parámetro)]] — Entrega un objeto selector de color
- [[Catálogo - Params#Colour Swatch (Swatch, parámetro)|Colour Swatch (Swatch, parámetro)]] — Muestra de color (paleta)
- [[Catálogo - Params#Colour Wheel (Wheel, parámetro)|Colour Wheel (Wheel, parámetro)]] — Crea una paleta de colores relacionados
- [[Catálogo - Params#Control Knob (Knob, parámetro)|Control Knob (Knob, parámetro)]] — Una perilla radial para definir números
- [[Catálogo - Params#Digit Scroller (parámetro)|Digit Scroller (parámetro)]] — Selector numérico para números individuales
- [[Catálogo - Params#Gradient|Gradient]] — Representa un degradado de varios colores
- [[Catálogo - Params#Graph Mapper (Graph, parámetro)|Graph Mapper (Graph, parámetro)]] — Representa una función de mapeo numérico
- [[Catálogo - Params#Image Resource (parámetro)|Image Resource (parámetro)]] — Una URI de imagen previsualizable
- [[Catálogo - Params#Image Sampler (Image, parámetro)|Image Sampler (Image, parámetro)]] — Entrega rutinas de muestreo de imágenes (mapas de bits)
- [[Catálogo - Params#Import 3DM (3DM)|Import 3DM (3DM)]] — Importa geometría a un RhinoDoc
- [[Catálogo - Params#Import Coordinates (Coords)|Import Coordinates (Coords)]] — Importa coordenadas de puntos desde archivos de texto genéricos
- [[Catálogo - Params#Import Image (IMG)|Import Image (IMG)]] — Importa datos de imagen desde archivos bmp, jpg o png
- [[Catálogo - Params#Import PDB (PDB)|Import PDB (PDB)]] — Importa datos de archivos *.pdb del Protein Data Bank
- [[Catálogo - Params#Import SHP (SHP)|Import SHP (SHP)]] — Importa datos de archivos GIS *.shp
- [[Catálogo - Params#MD Slider (parámetro)|MD Slider (parámetro)]] — Un slider multidimensional
- [[Catálogo - Params#Number Slider (parámetro)|Number Slider (parámetro)]] — Slider numérico para valores individuales
- [[Catálogo - Params#Panel (parámetro)|Panel (parámetro)]] — Un panel para notas y valores de texto personalizados
- [[Catálogo - Params#Read File (File)|Read File (File)]] — Lee el contenido de un archivo
- [[Catálogo - Params#Value List (List, parámetro)|Value List (List, parámetro)]] — Entrega una lista de valores predefinidos para elegir

### Params › Primitive (1)

- [[Catálogo - Params#File Path (Path, parámetro)|File Path (Path, parámetro)]] — Contiene una colección de rutas de archivo

### Params › Util (28)

- [[Catálogo - Params#Bifocals|Bifocals]] — Agrega etiquetas flotantes a todos los componentes, con algunas excepciones. Doble clic para…
- [[Catálogo - Params#Cherry Picker (Item, parámetro)|Cherry Picker (Item, parámetro)]] — Toma un solo elemento de un árbol de datos
- [[Catálogo - Params#Cluster Input (Input, parámetro)|Cluster Input (Input, parámetro)]] — Representa un parámetro de entrada de un cluster
- [[Catálogo - Params#Cluster Output (Output, parámetro)|Cluster Output (Output, parámetro)]] — Representa un parámetro de salida de un cluster
- [[Catálogo - Params#Context Bake (C-Bake)|Context Bake (C-Bake)]] — Contenido para hacer bake al final del comando GrasshopperPlayer o con Hops y Rhino.Compute
- [[Catálogo - Params#Context Print (C-Print)|Context Print (C-Print)]] — Datos de texto para imprimir al final del comando GrasshopperPlayer
- [[Catálogo - Params#Data Dam (Dam)|Data Dam (Dam)]] — Retrasa los datos en su paso por el documento
- [[Catálogo - Params#Data Input (Input)|Data Input (Input)]] — Lee un conjunto de datos desde un archivo
- [[Catálogo - Params#Data Output (Output)|Data Output (Output)]] — Escribe un conjunto de datos en un archivo
- [[Catálogo - Params#Data Recorder (Rec, parámetro)|Data Recorder (Rec, parámetro)]] — Registra datos a lo largo del tiempo
- [[Catálogo - Params#Fitness Landscape (LScape)|Fitness Landscape (LScape)]] — Muestra un paisaje de aptitud (fitness) 2.5D
- [[Catálogo - Params#Galapagos (objeto especial)|Galapagos (objeto especial)]] — Interfaz con el solver evolutivo Galapagos
- [[Catálogo - Params#Gene Pool (Genes, parámetro)|Gene Pool (Genes, parámetro)]] — Contiene una colección de genes (es decir, variables)
- [[Catálogo - Params#Get Boolean (parámetro)|Get Boolean (parámetro)]] — Entrada booleana contextual
- [[Catálogo - Params#Get File Path (parámetro)|Get File Path (parámetro)]] — Entrada contextual de ruta de archivo
- [[Catálogo - Params#Get Geometry (parámetro)|Get Geometry (parámetro)]] — Entrada contextual de geometría
- [[Catálogo - Params#Get Integer (parámetro)|Get Integer (parámetro)]] — Entrada contextual de entero
- [[Catálogo - Params#Get Line (parámetro)|Get Line (parámetro)]] — Entrada contextual de línea
- [[Catálogo - Params#Get Number (parámetro)|Get Number (parámetro)]] — Entrada contextual numérica
- [[Catálogo - Params#Get Plane (parámetro)|Get Plane (parámetro)]] — Entrada contextual de plano
- [[Catálogo - Params#Get Point (parámetro)|Get Point (parámetro)]] — Entrada contextual de punto
- [[Catálogo - Params#Get String (parámetro)|Get String (parámetro)]] — Entrada contextual de texto
- [[Catálogo - Params#Jump (objeto especial)|Jump (objeto especial)]] — Salta entre distintas ubicaciones del lienzo
- [[Catálogo - Params#Param Viewer (Viewer, parámetro)|Param Viewer (Viewer, parámetro)]] — Un visor de estructuras de datos
- [[Catálogo - Params#Relay (parámetro)|Relay (parámetro)]] — Un objeto relé de conexiones (wire relay)
- [[Catálogo - Params#Scribble (objeto especial)|Scribble (objeto especial)]] — Una nota rápida
- [[Catálogo - Params#Suirify (parámetro)|Suirify (parámetro)]] — Simplificación de árboles de datos al estilo Suirify
- [[Catálogo - Params#Trigger (objeto especial)|Trigger (objeto especial)]] — Dispara actualizaciones de ciertos componentes, de forma manual o cíclica

### Maths › Script (7)

- [[Catálogo - Maths#C♯ Script (C♯)|C♯ Script (C♯)]] — Componente de script C#
- [[Catálogo - Maths#Evaluate (Eval)|Evaluate (Eval)]] — Evalúa una expresión con una cantidad flexible de variables
- [[Catálogo - Maths#Expression|Expression]] — Evalúa una expresión
- [[Catálogo - Maths#IronPython 2 Script (IPy2)|IronPython 2 Script (IPy2)]] — Componente de script IronPython 2
- [[Catálogo - Maths#Python 3 Script (Py3)|Python 3 Script (Py3)]] — Componente de script Python 3
- [[Catálogo - Maths#Script (S)|Script (S)]] — Componente de script
- [[Catálogo - Maths#VB Script (VB)|VB Script (VB)]] — Un componente con script VB.NET

### Anemone › Classic (2)

- [[Catálogo - Anemone#Loop End|Loop End]] — Termina el bucle con este componente. Doble clic para pausar el bucle
- [[Catálogo - Anemone#Loop Start|Loop Start]] — Inicia el bucle con este componente. Doble clic para volver a ejecutar

### Anemone › Util (1)

- [[Catálogo - Anemone#Time Buffer (Buffer)|Time Buffer (Buffer)]] — Espera un tiempo determinado antes de pasar los datos

### eleFront › 09 Files (9)

- [[Catálogo - eleFront#Construct FilePath (ConPath)|Construct FilePath (ConPath)]] — Construye una ruta de archivo a partir de carpetas, nombre de archivo y extensión
- [[Catálogo - eleFront#Deconstruct FilePath (DecPath)|Deconstruct FilePath (DecPath)]] — Divide una ruta de archivo en carpeta y nombre de archivo
- [[Catálogo - eleFront#Export Generic (ExpGen)|Export Generic (ExpGen)]] — Exporta a cualquier tipo de archivo que admita Rhino
- [[Catálogo - eleFront#Export to Rhino File (Exp3dm)|Export to Rhino File (Exp3dm)]] — Exporta objetos a un archivo 3dm
- [[Catálogo - eleFront#Get Current File (File)|Get Current File (File)]] — Devuelve el nombre y la carpeta del archivo actual
- [[Catálogo - eleFront#List Files (Files)|List Files (Files)]] — Lista todos los archivos de una carpeta que coinciden con una máscara de búsqueda
- [[Catálogo - eleFront#Merge Rhino Files (MergeF)|Merge Rhino Files (MergeF)]] — Fusiona archivos de Rhino en uno solo, con distintos ajustes
- [[Catálogo - eleFront#Modify Rhino File (Modify3dm)|Modify Rhino File (Modify3dm)]] — Agrega o quita objetos de un archivo de Rhino externo
- [[Catálogo - eleFront#Select Folder (SelFolder)|Select Folder (SelFolder)]] — Selecciona de forma interactiva una ruta de carpeta usando listas de valores autocompletadas. Conecta una…

### Human UI › UI Containers (9)

- [[Catálogo - Human UI#Create Border (Border)|Create Border (Border)]] — Envuelve elementos con un borde
- [[Catálogo - Human UI#Create Expander (Expander)|Create Expander (Expander)]] — Un desplegable plegable para contenido
- [[Catálogo - Human UI#Create Grid (Grid)|Create Grid (Grid)]] — Crea un contenedor con elementos en posición absoluta. El orden de entrada determina su orden Z; define los…
- [[Catálogo - Human UI#Create Scroll Viewer (ScrollViewer)|Create Scroll Viewer (ScrollViewer)]] — Permite que un elemento se desplace (scroll) independientemente del resto de la ventana
- [[Catálogo - Human UI#Create Simple Grid (SimpleGrid)|Create Simple Grid (SimpleGrid)]] — Crea un contenedor con elementos en una grilla según la estructura de rutas entregada. Cada ruta de rama se…
- [[Catálogo - Human UI#Create Stack (Stack)|Create Stack (Stack)]] — Crea un grupo de elementos de interfaz apilados vertical u horizontalmente
- [[Catálogo - Human UI#Create View Box (ViewBox)|Create View Box (ViewBox)]] — Escala un grupo de elementos de interfaz colocándolos en un ViewBox
- [[Catálogo - Human UI#Create WrapPanel (WrapPanel)|Create WrapPanel (WrapPanel)]] — Crea un grupo de elementos de interfaz en un WrapPanel, vertical u horizontal
- [[Catálogo - Human UI#Tabbed View (Tabs)|Tabbed View (Tabs)]] — Crea una serie de vistas con pestañas que pueden contener diseños de elementos de interfaz

### Human UI › UI Elements (30)

- [[Catálogo - Human UI#Attach Tooltip to Element (Tooltip)|Attach Tooltip to Element (Tooltip)]] — Agrega un tooltip a un elemento de interfaz
- [[Catálogo - Human UI#Create 3D View (3DView)|Create 3D View (3DView)]] — Crea una vista 3D orbitable con una malla definida por el usuario
- [[Catálogo - Human UI#Create Browser (Browser)|Create Browser (Browser)]] — Crea una ventana de navegador web
- [[Catálogo - Human UI#Create Button (Button)|Create Button (Button)]] — Crea un objeto botón
- [[Catálogo - Human UI#Create Checkbox (Checkbox)|Create Checkbox (Checkbox)]] — Crea una sola casilla de verificación
- [[Catálogo - Human UI#Create Checklist (Checklist)|Create Checklist (Checklist)]] — Crea un cuadro de lista con casillas de verificación
- [[Catálogo - Human UI#Create Color Picker (ColorPicker)|Create Color Picker (ColorPicker)]] — Crea un selector de color interactivo, con un conjunto de colores opcional
- [[Catálogo - Human UI#Create Data Table (DataTable)|Create Data Table (DataTable)]] — Crea una vista de tabla de datos
- [[Catálogo - Human UI#Create File Picker (FilePicker)|Create File Picker (FilePicker)]] — Crea un cuadro de diálogo para elegir la ruta de un archivo, una carpeta o dónde guardar
- [[Catálogo - Human UI#Create Gradient Editor (Gradient)|Create Gradient Editor (Gradient)]] — Crea un degradado editable en la interfaz
- [[Catálogo - Human UI#Create Graph Mapper (GraphMapper)|Create Graph Mapper (GraphMapper)]] — Crea un Graph Mapper Bézier
- [[Catálogo - Human UI#Create Image (Image)|Create Image (Image)]] — Crea un objeto imagen para agregar a la ventana
- [[Catálogo - Human UI#Create Label (Label)|Create Label (Label)]] — Crea una etiqueta en la ventana
- [[Catálogo - Human UI#Create List Box (ListBox)|Create List Box (ListBox)]] — Crea un cuadro de lista desde el que se pueden seleccionar elementos
- [[Catálogo - Human UI#Create Markdown Viewer (MDV)|Create Markdown Viewer (MDV)]] — Crea un bloque de texto con formato a partir de una entrada en Markdown
- [[Catálogo - Human UI#Create Multidimensional Slider (MD Slider)|Create Multidimensional Slider (MD Slider)]] — Crea un slider 2D que va de {0,0} a {1,1}
- [[Catálogo - Human UI#Create Objects from XAML (XAML)|Create Objects from XAML (XAML)]] — Crea elementos de interfaz a partir de sintaxis XAML escrita
- [[Catálogo - Human UI#Create Pulldown Menu (Pulldown)|Create Pulldown Menu (Pulldown)]] — Crea un menú desplegable desde el que se pueden seleccionar elementos
- [[Catálogo - Human UI#Create Radio Button (RadioBtn)|Create Radio Button (RadioBtn)]] — Crea un solo botón de opción (radio button). Asegúrate de asignarle un grupo para que se alternen…
- [[Catálogo - Human UI#Create Range Slider (RangeSlider)|Create Range Slider (RangeSlider)]] — Crea un slider doble que describe un rango
- [[Catálogo - Human UI#Create Rhino Command Button (CmdButton)|Create Rhino Command Button (CmdButton)]] — Crea un botón especial que ejecuta un comando de Rhino
- [[Catálogo - Human UI#Create Rhino Pick Button (PickBtn)|Create Rhino Pick Button (PickBtn)]] — Crea un botón especial para seleccionar geometría desde Rhino
- [[Catálogo - Human UI#Create Separator (Separator)|Create Separator (Separator)]] — Crea un objeto separador de línea
- [[Catálogo - Human UI#Create Shape (Shape)|Create Shape (Shape)]] — Crea una forma simple a partir de una polilínea
- [[Catálogo - Human UI#Create Shapes (Shapes)|Create Shapes (Shapes)]] — Crea formas a partir de polilíneas
- [[Catálogo - Human UI#Create Slider (Slider)|Create Slider (Slider)]] — Crea un slider con una etiqueta y una lectura del valor
- [[Catálogo - Human UI#Create Text Block (TB)|Create Text Block (TB)]] — Crea un bloque de texto de varias líneas
- [[Catálogo - Human UI#Create Text Box (TextBox)|Create Text Box (TextBox)]] — Crea un cuadro para ingresar texto, con un botón para pasar su valor
- [[Catálogo - Human UI#Create Toggle (Toggle)|Create Toggle (Toggle)]] — Crea un interruptor de encendido/apagado
- [[Catálogo - Human UI#Create True-Only Button (True Button)|Create True-Only Button (True Button)]] — Crea un objeto botón que solo entrega True

### Human UI › UI Graphs + Charts (5)

- [[Catálogo - Human UI#Chart Appearance (ChartAppearance)|Chart Appearance (ChartAppearance)]] — Úsalo para definir la apariencia de un gráfico
- [[Catálogo - Human UI#Create Chart (Chart)|Create Chart (Chart)]] — Crea un gráfico a partir de datos y categorías
- [[Catálogo - Human UI#Create Multi Chart (MultiChart)|Create Multi Chart (MultiChart)]] — Crea un gráfico múltiple a partir de conjuntos de datos y categorías
- [[Catálogo - Human UI#Set Chart Contents (SetChart)|Set Chart Contents (SetChart)]] — Úsalo para definir el contenido de un gráfico
- [[Catálogo - Human UI#Set Multi Chart Contents (SetMultiChart)|Set Multi Chart Contents (SetMultiChart)]] — Úsalo para definir el contenido de un gráfico múltiple

### Human UI › UI Main (16)

- [[Catálogo - Human UI#Add Elements (AddElems)|Add Elements (AddElems)]] — Agrega controles WPF a una ventana
- [[Catálogo - Human UI#Adjust Element Appearance (AdjustElem)|Adjust Element Appearance (AdjustElem)]] — Ajusta el color y la apariencia de elementos individuales
- [[Catálogo - Human UI#Adjust Element Positioning (AdjustPos)|Adjust Element Positioning (AdjustPos)]] — Ajusta los márgenes, el tamaño y otros datos de posición de un elemento. El posicionamiento absoluto puede…
- [[Catálogo - Human UI#Capture Window or Element to File (Capture)|Capture Window or Element to File (Capture)]] — Captura una ventana de HUI o un elemento individual como imagen
- [[Catálogo - Human UI#Get Element Properties (GetProps)|Get Element Properties (GetProps)]] — Intenta obtener todas las propiedades de cualquier elemento. ¡Es experimental!
- [[Catálogo - Human UI#Get Screen Dimensions (GetScreen)|Get Screen Dimensions (GetScreen)]] — Obtiene las dimensiones de la pantalla actual
- [[Catálogo - Human UI#Hide/Show Element (HideShow)|Hide/Show Element (HideShow)]] — Permite ocultar o mostrar un elemento
- [[Catálogo - Human UI#Launch Transparent Window (LaunchXPWin)|Launch Transparent Window (LaunchXPWin)]] — Este componente abre una nueva ventana de controles, vacía y transparente
- [[Catálogo - Human UI#Launch Window (LaunchWin)|Launch Window (LaunchWin)]] — Este componente abre una nueva ventana de controles vacía
- [[Catálogo - Human UI#Make Child Window (ChildWin)|Make Child Window (ChildWin)]] — Hace que una ventana sea hija de otra
- [[Catálogo - Human UI#Restore Element States (Restore)|Restore Element States (Restore)]] — Restaura los estados guardados de los elementos de interfaz
- [[Catálogo - Human UI#Save Element States (SaveStates)|Save Element States (SaveStates)]] — Este componente permite guardar el estado de los elementos seleccionados para recuperarlo después
- [[Catálogo - Human UI#Set Element Property (SetProp)|Set Element Property (SetProp)]] — Intenta definir cualquier propiedad de un elemento. ¡Es experimental!
- [[Catálogo - Human UI#Set Window Properties (WinProps)|Set Window Properties (WinProps)]] — Modifica varias propiedades de una ventana
- [[Catálogo - Human UI#Value Listener (Values)|Value Listener (Values)]] — Este componente obtiene los valores de los elementos de interfaz de la ventana. Por defecto se actualiza solo…
- [[Catálogo - Human UI#Window Status (WinStat)|Window Status (WinStat)]] — Obtiene el estado actual de la ventana indicada

### Human UI › UI Output (21)

- [[Catálogo - Human UI#Add Elements to Shape(s) (AddElem2Shape)|Add Elements to Shape(s) (AddElem2Shape)]] — Pone elementos de interfaz (¡como texto!) encima de un elemento de forma(s)
- [[Catálogo - Human UI#Set 3D View (Set3DView)|Set 3D View (Set3DView)]] — Permite modificar el contenido de una vista 3D existente
- [[Catálogo - Human UI#Set 3D View Properties (Set3DViewProps)|Set 3D View Properties (Set3DViewProps)]] — Controles adicionales para modificar una vista 3D
- [[Catálogo - Human UI#Set 3D View Textured (Set3DViewTex)|Set 3D View Textured (Set3DViewTex)]] — Permite modificar el contenido de una vista 3D existente
- [[Catálogo - Human UI#Set Browser (SetBrowser)|Set Browser (SetBrowser)]] — Controla el elemento navegador: botones atrás/adelante, el sitio mostrado, etc
- [[Catálogo - Human UI#Set Button (SetBtn)|Set Button (SetBtn)]] — Cambia el contenido de un elemento botón existente
- [[Catálogo - Human UI#Set CheckBox (SetCheckBox)|Set CheckBox (SetCheckBox)]] — Modifica un objeto casilla de verificación existente
- [[Catálogo - Human UI#Set Checklist Contents (SetChecklist)|Set Checklist Contents (SetChecklist)]] — Úsalo para definir el contenido de una lista de casillas
- [[Catálogo - Human UI#Set Color Picker (SetColorPicker)|Set Color Picker (SetColorPicker)]] — Úsalo para definir los valores de un selector de color
- [[Catálogo - Human UI#Set Data Table (SetDataTable)|Set Data Table (SetDataTable)]] — Actualiza el contenido de una tabla de datos
- [[Catálogo - Human UI#Set Expander (SetExp)|Set Expander (SetExp)]] — Define las propiedades de un contenedor desplegable
- [[Catálogo - Human UI#Set Image (SetImg)|Set Image (SetImg)]] — Cambia el contenido de un control de imagen existente
- [[Catálogo - Human UI#Set Label Contents (SetLabel)|Set Label Contents (SetLabel)]] — Modifica el contenido de un objeto etiqueta existente
- [[Catálogo - Human UI#Set List Contents (SetList)|Set List Contents (SetList)]] — Úsalo para definir el contenido de un cuadro de lista o de un menú desplegable
- [[Catálogo - Human UI#Set Multidimensional Slider (SetMDSlider)|Set Multidimensional Slider (SetMDSlider)]] — Modifica el valor de un slider multidimensional
- [[Catálogo - Human UI#Set Shape (SetShape)|Set Shape (SetShape)]] — Reemplaza una forma existente en la ventana
- [[Catálogo - Human UI#Set Shapes (SetShapes)|Set Shapes (SetShapes)]] — Reemplaza una forma existente en la ventana
- [[Catálogo - Human UI#Set Slider (SetSlider)|Set Slider (SetSlider)]] — Modifica el rango y el valor de un slider
- [[Catálogo - Human UI#Set Tabbed View (SetTab)|Set Tabbed View (SetTab)]] — Define las propiedades de una vista con pestañas
- [[Catálogo - Human UI#Set TextBlock Contents (SetTextBlock)|Set TextBlock Contents (SetTextBlock)]] — Modifica el contenido de un objeto bloque de texto existente
- [[Catálogo - Human UI#Set TextBox Contents (SetTextBox)|Set TextBox Contents (SetTextBox)]] — Modifica el contenido de un objeto cuadro de texto existente

### LunchBox › Data (11)

- [[Catálogo - LunchBox#Convert JSON to XML (JSON-XML)|Convert JSON to XML (JSON-XML)]] — Convierte un texto JSON a XML
- [[Catálogo - LunchBox#Convert XML to JSON (XML-JSON)|Convert XML to JSON (XML-JSON)]] — Convierte un texto XML a JSON
- [[Catálogo - LunchBox#Create CSV (CSV)|Create CSV (CSV)]] — Crea un texto CSV
- [[Catálogo - LunchBox#Create Data Grid (DataGrid)|Create Data Grid (DataGrid)]] — Crea una vista de grilla de datos. Los datos se pueden guardar como archivo CSV
- [[Catálogo - LunchBox#Create DataSet (DataSet)|Create DataSet (DataSet)]] — Crea un DataSet
- [[Catálogo - LunchBox#Create DataTable (DataTable)|Create DataTable (DataTable)]] — Crea un DataTable
- [[Catálogo - LunchBox#Create JSON (JSON)|Create JSON (JSON)]] — Crea JSON a partir de un DataSet
- [[Catálogo - LunchBox#Create XML from Tree (XML Tree)|Create XML from Tree (XML Tree)]] — Crea XML a partir de un árbol de Grasshopper con texto o números
- [[Catálogo - LunchBox#Read CSV (CSV)|Read CSV (CSV)]] — Lee un texto CSV (valores separados por comas)
- [[Catálogo - LunchBox#Read XML by Tag (XML)|Read XML by Tag (XML)]] — Lee datos XML por etiqueta
- [[Catálogo - LunchBox#Write XML File (Write XML)|Write XML File (Write XML)]] — Crea XML a partir de un DataSet

### LunchBox › Serialization (6)

- [[Catálogo - LunchBox#Create GUID (GUID)|Create GUID (GUID)]] — Crea un GUID (identificador único global) válido
- [[Catálogo - LunchBox#Decrypt Text (Decrypt)|Decrypt Text (Decrypt)]] — Descifra texto con una frase de contraseña
- [[Catálogo - LunchBox#Deserialize Geometry (Deserialize)|Deserialize Geometry (Deserialize)]] — Deserializa un texto (JSON, XML o binario) a geometría de Grasshopper
- [[Catálogo - LunchBox#Encrypt Text (Encrypt)|Encrypt Text (Encrypt)]] — Cifra texto con una frase de contraseña
- [[Catálogo - LunchBox#Hash Objects (Hash)|Hash Objects (Hash)]] — Usa un algoritmo de hash seguro (SHA) para obtener el hash de geometría o textos
- [[Catálogo - LunchBox#Serialize Geometry (Serialize)|Serialize Geometry (Serialize)]] — Serializa geometría de Grasshopper a formatos de texto (JSON, XML o binario)

### LunchBox › Workflow (11)

- [[Catálogo - LunchBox#Create Layers (Layer)|Create Layers (Layer)]] — Crea una lista de capas en Rhino
- [[Catálogo - LunchBox#Excel Reader (ExcelRead)|Excel Reader (ExcelRead)]] — Lee un archivo de Excel abierto
- [[Catálogo - LunchBox#Excel Writer (ExcelWrite)|Excel Writer (ExcelWrite)]] — Escribe en un archivo de Excel abierto
- [[Catálogo - LunchBox#Launch Application (LaunchApp)|Launch Application (LaunchApp)]] — Abre una aplicación o un archivo externo
- [[Catálogo - LunchBox#Layer Information (Layer Info)|Layer Information (Layer Info)]] — Obtiene información de las capas del documento actual
- [[Catálogo - LunchBox#Layer Reference (Layer Ref)|Layer Reference (Layer Ref)]] — Referencia geometría de capas con sus GUID y nombres
- [[Catálogo - LunchBox#Object Bake (Bake)|Object Bake (Bake)]] — Hace bake de objetos en una capa del documento activo de Rhino
- [[Catálogo - LunchBox#Object Save (Save)|Object Save (Save)]] — Guarda geometría en una ubicación de archivo indicada
- [[Catálogo - LunchBox#Rhino Command (RhCOM)|Rhino Command (RhCOM)]] — Envía un comando a la línea de comandos de Rhino
- [[Catálogo - LunchBox#Text Reader (Reader)|Text Reader (Reader)]] — Lee un flujo de texto desde un archivo
- [[Catálogo - LunchBox#Text Writer (Writer)|Text Writer (Writer)]] — Escribe un flujo de texto en un archivo

### Parakeet › Util (28)

- [[Catálogo - Parakeet#Add Clipping Plane (Clip Plane)|Add Clipping Plane (Clip Plane)]] — Genera un plano de recorte en Rhino
- [[Catálogo - Parakeet#Case Formatter (CaseFmt)|Case Formatter (CaseFmt)]] — Convierte un texto a varios estilos comunes de mayúsculas/minúsculas
- [[Catálogo - Parakeet#Clean Number (CleanNumber)|Clean Number (CleanNumber)]] — Convierte el formato científico (y otros formatos numéricos) a números simples
- [[Catálogo - Parakeet#Construct Tree Branch (TBranch)|Construct Tree Branch (TBranch)]] — Crea una rama de árbol usando una ruta de rama y elementos
- [[Catálogo - Parakeet#Create Material (PMaterial)|Create Material (PMaterial)]] — Crea un material a partir de una imagen como textura, un color y valores de reflexión y suavidad. (El mapeo…
- [[Catálogo - Parakeet#Custom Round|Custom Round]] — Redondea un número a un paso personalizado
- [[Catálogo - Parakeet#Delay|Delay]] — Dispara un solo pulso True después de un retraso dado (en segundos) desde un flanco de subida del Trigger
- [[Catálogo - Parakeet#Delete Files (Del files)|Delete Files (Del files)]] — Borra archivos de una carpeta
- [[Catálogo - Parakeet#FaceMe Plane (FaceMe)|FaceMe Plane (FaceMe)]] — Genera un plano orientado hacia la cámara activa. Mientras On esté en True, el resultado se actualiza solo al…
- [[Catálogo - Parakeet#Fast Closest Points (FCPs+)|Fast Closest Points (FCPs+)]] — Busca los N puntos más cercanos a cada punto de entrada. Conserva la ruta del árbol de entrada: una rama de…
- [[Catálogo - Parakeet#Golden Point (GoldenPt)|Golden Point (GoldenPt)]] — Crea un punto [C] sobre una línea dada [AB] tal que AC/BC=φ (razón áurea ≈ 2.618)
- [[Catálogo - Parakeet#Hide Canvas (HideGH)|Hide Canvas (HideGH)]] — Oculta la ventana del editor de Grasshopper
- [[Catálogo - Parakeet#If Value Changed (ValChanged)|If Value Changed (ValChanged)]] — Entrega un pulso True cada vez que cambia la lista de enteros de entrada
- [[Catálogo - Parakeet#Interpolate Color|Interpolate Color]] — Interpola una colección de colores
- [[Catálogo - Parakeet#Mouse|Mouse]] — Obtiene las coordenadas del cursor y el estado de los botones del mouse
- [[Catálogo - Parakeet#Mouse Buttons Blocker (MouseBlock)|Mouse Buttons Blocker (MouseBlock)]] — Bloquea de forma selectiva los clics izquierdo, derecho y/o central del mouse en la vista de Rhino
- [[Catálogo - Parakeet#Number Analyzer (NumAnalyze)|Number Analyzer (NumAnalyze)]] — Calcula un conjunto completo de propiedades estadísticas de una lista de números
- [[Catálogo - Parakeet#Pack Curves (PackCrv)|Pack Curves (PackCrv)]] — Empaqueta curvas sobre el plano XY (nesting simple)
- [[Catálogo - Parakeet#Reflection Point (ReflectP)|Reflection Point (ReflectP)]] — Devuelve el reflejo de un punto [o lista de puntos] respecto de un plano
- [[Catálogo - Parakeet#RefreshAll (Rfrsh)|RefreshAll (Rfrsh)]] — Recalcula o refresca todos los componentes del lienzo actual
- [[Catálogo - Parakeet#Scissors (Scissor)|Scissors (Scissor)]] — Simula una estructura de tijera circular desplegable
- [[Catálogo - Parakeet#Sequential Activator (Activator)|Sequential Activator (Activator)]] — El activador secuencial genera una lista de valores decimales que se activan progresivamente de 0.0 a 1.0…
- [[Catálogo - Parakeet#Text Search (TxtSearch)|Text Search (TxtSearch)]] — Busca una palabra clave en una lista de textos y devuelve los elementos que coinciden
- [[Catálogo - Parakeet#Timer|Timer]] — Entrega True durante una duración dada (en segundos) después de un flanco de subida del Trigger y luego…
- [[Catálogo - Parakeet#Unit Changer (UnitChanger)|Unit Changer (UnitChanger)]] — Cambia las unidades de Rhino
- [[Catálogo - Parakeet#Value List Controler (VList Cntl)|Value List Controler (VList Cntl)]] — Controla los nombres y valores de una Value List
- [[Catálogo - Parakeet#WirelessGate (WLGate)|WirelessGate (WLGate)]] — Pasa datos de forma inalámbrica
- [[Catálogo - Parakeet#Zoom to (Zoom)|Zoom to (Zoom)]] — Ubica la cámara a cierta distancia apuntando a un punto

<!-- AUTO:fin -->
