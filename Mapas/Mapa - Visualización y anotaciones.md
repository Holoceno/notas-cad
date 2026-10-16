---
tags: [tipo/mapa, rhino/vista, rhino/anotaciones, fabricacion/planos, software/grasshopper, software/rhinocommon]
---

# Visualización y anotaciones

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Colores, vista previa, gráficos, textos, cotas, hatches y Make2D. Sirve para presentar (colores por análisis, leyendas) y para **documentar** (planos con cotas). Para el flujo de planos 2D ver [[Mapa - CAD 2D y planos]].

## Teoría y código
- [[wiki/concepts/rhinocommon-anotaciones-api]] · [[wiki/sources/2026-05-04-rhinopy-anotaciones]]
- [[wiki/sources/2026-05-04-rhinopy-vista]]: viewports, display, clipping planes
- [[wiki/sources/2026-05-04-rhinopy-input-ui]]: Display Conduit (dibujar sin crear objetos)

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) |
|---|---|---|
| Color RGB | [[Catálogo - Display#Colour RGB (RGB)\|Colour RGB]] | `System.Drawing.Color.FromArgb(r, g, b)` |
| Vista previa con material | [[Catálogo - Display#Custom Preview (Preview)\|Custom Preview]] | `DisplayConduit` (fuera de GH) |
| Texto en el modelo | [[Catálogo - Rhino#Text Entity (Text)\|Text Entity]] | `rg.TextEntity.Create(...)` → `doc.Objects.AddText(...)` |
| Cota lineal | [[Catálogo - Rhino#Linear Dimension (DimLinear)\|Linear Dimension]] | `rg.LinearDimension.Create(...)` → `doc.Objects.AddLinearDimension(...)` |
| Dibujo 2D de un modelo 3D | [[Catálogo - Display#Make2D\|Make2D]] | `rg.HiddenLineDrawing.Compute(parametros, True)` |

## Para empezar
[[Catálogo - Display#Custom Preview (Preview)|Custom Preview]] · [[Catálogo - Display#Gradient Hatch (GHatch)|Gradient Hatch]] · [[Catálogo - Display#Text Tag 3D (Tag)|Text Tag 3D]] · [[Catálogo - Display#Legend|Legend]] · [[Catálogo - Display#Make2D|Make2D]] · [[Catálogo - Display#Aligned Dimension (AlignDim)|Aligned Dimension]] · [[Catálogo - Rhino#Text Entity (Text)|Text Entity]] · [[Catálogo - Rhino#Display Attributes (Display)|Display Attributes]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (45)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Annotation Text | [[Add Annotation Text\|Py]] · [[Add Annotation Text (cs)\|C#]] | Agrega un texto en un punto del plano de construcción | `doc.Objects.AddText(texto, plano, altura, fuente, ...)` |
| Add Arrowheads to Curves | [[Add Arrowheads to Curves\|Py]] · [[Add Arrowheads to Curves (cs)\|C#]] | Pone puntas de flecha a una línea con los atributos del objeto | `ObjectAttributes.ObjectDecoration` |
| Add Background Bitmap | [[Add Background Bitmap\|Py]] · [[Add Background Bitmap (cs)\|C#]] | Pone una imagen de fondo para calcar en la vista | `Viewport.SetTraceImage(archivo, plano, ancho, alto, ...)` |
| Add Clipping Plane | [[Add Clipping Plane\|Py]] · [[Add Clipping Plane (cs)\|C#]] | Agrega un plano de corte desde un rectángulo | `doc.Objects.AddClippingPlane(plano, ancho, alto, viewportId)` |
| Add Layout | [[Add Layout (cs)\|C#]] | Crea un layout A0 con una ventana de detalle a escala | `doc.Views.AddPageView, AddDetailView, DetailGeometry.SetScale` |
| Add Leader | [[Add Leader\|Py]] · [[Add Leader (cs)\|C#]] | Agrega una directriz desde una lista de puntos | `rs.AddLeader(puntos)` |
| Add Linear Dimension | [[Add Linear Dimension\|Py]] · [[Add Linear Dimension (cs)\|C#]] | Agrega una cota lineal pidiéndola al usuario | `RhinoGet.GetLinearDimension → doc.Objects.AddLinearDimension` |
| Add Linear Dimension2 | [[Add Linear Dimension2 (py)\|Py]] · [[Add Linear Dimension2 (cs)\|C#]] | Cota lineal desde dos puntos y la posición de la línea de cota | `LinearDimension(plano, ext1, ext2, ptLinea)` |
| Add Material | [[Add Material\|Py]] · [[Add Material (cs)\|C#]] | Crea un material y lo asigna a una esfera | `Material → RenderMaterial.CreateBasicMaterial → doc.RenderMaterials.Add` |
| Add Named View | [[Add Named View\|Py]] · [[Add Named View (cs)\|C#]] | Guarda una vista con nombre (posición de cámara y objetivo) | `Viewport.SetCameraLocation / SetCameraDirection → doc.NamedViews.Add` |
| Add Radial Dimension | [[Add Radial Dimension (py)\|Py]] · [[Add Radial Dimension (cs)\|C#]] | Agrega una cota de radio a una curva | `Curve.CurvatureAt → RadialDimension → doc.Objects.AddRadialDimension` |
| Add Texture | [[Add Texture\|Py]] · [[Add Texture (cs)\|C#]] | Aplica una imagen como textura al material de un objeto | `Texture.FileName → Material.SetTexture → RenderMaterial` |
| Advanced Display Settings | [[Advanced Display Settings\|Py]] · [[Advanced Display Settings (cs)\|C#]] | Cambia un atributo de un modo de visualización (grosor del alambre de mallas) | `DisplayModeDescription.GetDisplayModes / UpdateDisplayMode` |
| Change Dimension Style | [[Change Dimension Style\|Py]] · [[Change Dimension Style (cs)\|C#]] | Aplica el estilo de cota actual a todas las anotaciones | `doc.DimStyles.CurrentDimensionStyleIndex → CommitChanges` |
| Conduit Draw Shaded Mesh | [[Conduit Draw Shaded Mesh (cs)\|C#]] | Dibuja una malla sombreada con un display conduit, sin agregarla al documento | `DisplayConduit.PostDrawObjects → DrawMeshShaded` |
| Determine Active Viewport | [[Determine Active Viewport\|Py]] · [[Determine Active Viewport (cs)\|C#]] | Nombre de la vista activa, también dentro de un layout | `doc.Views.ActiveView, RhinoPageView.PageIsActive` |
| Display Conduit | [[Display Conduit (cs)\|C#]] | Conduit básico: dibuja los ejes del plano de construcción | `DisplayConduit.CalculateBoundingBox / PreDrawObjects` |
| Display Conduit Arrowheads | [[Display Conduit Arrowheads\|Py]] · [[Display Conduit Arrowheads (cs)\|C#]] | Dibuja flechas con un display conduit (tamaño en pantalla o en el modelo) | `DisplayConduit → e.Display.DrawArrow` |
| Display Order | [[Display Order\|Py]] · [[Display Order (cs)\|C#]] | Orden de dibujo de los objetos (adelante o atrás) | `Attributes.DisplayOrder → CommitChanges` |
| Draw Mesh | [[Draw Mesh\|Py]] · [[Draw Mesh (cs)\|C#]] | Malla desde una esfera, dibujada en azul con un conduit | `Mesh.CreateFromSphere → DisplayConduit (DrawMeshShaded)` |
| Dynamically Draw Geometry when Picking Points | [[Dynamically Draw Geometry when Picking Points\|Py]] · [[Dynamically Draw Geometry when Picking Points (cs)\|C#]] | Vista previa de un círculo mientras se elige el radio | `clase GetPoint propia con OnDynamicDraw` |
| Dynamically Drawing Text Strings | [[Dynamically Drawing Text Strings\|Py]] · [[Dynamically Drawing Text Strings (cs)\|C#]] | Texto en pantalla que sigue al cursor (coordenadas de pantalla) | `Viewport.GetTransform(World, Screen), e.Display.Draw2dText` |
| Edit Text | [[Edit Text\|Py]] · [[Edit Text (cs)\|C#]] | Cambia el contenido de un texto | `TextObject.Geometry.Text → CommitChanges` |
| Explode Hatch | [[Explode Hatch\|Py]] · [[Explode Hatch (cs)\|C#]] | Explota un sombreado en sus curvas y superficies | `Hatch.Explode()` |
| Get and Set the Active View | [[Get and Set the Active View\|Py]] · [[Get and Set the Active View (cs)\|C#]] | Cambia la vista activa por nombre | `doc.Views.ActiveView = vista` |
| Hatch Curve | [[Hatch Curve\|Py]] · [[Hatch Curve (cs)\|C#]] | Crea un sombreado dentro de una curva cerrada y plana | `Hatch.Create(curva, patron, rotacion, escala)` |
| Isocurve Density | [[Isocurve Density\|Py]] · [[Isocurve Density (cs)\|C#]] | Cambia la densidad de isocurvas de un objeto | `Attributes.WireDensity` |
| Modify Light Color | [[Modify Light Color\|Py]] · [[Modify Light Color (cs)\|C#]] | Cambia el color de una luz | `doc.Lights.Modify(id, luz)` |
| Modify Object Color | [[Modify Object Color\|Py]] · [[Modify Object Color (cs)\|C#]] | Cambia el color de un objeto | `Attributes.ObjectColor + ColorSource.ColorFromObject` |
| Move CPlane | [[Move CPlane\|Py]] · [[Move CPlane (cs)\|C#]] | Mueve el plano de construcción con vista previa | `Viewport.GetConstructionPlane / SetConstructionPlane` |
| Object Color | [[Object Color (cs)\|C#]] | Cambia el color de varios objetos con el diálogo de color | `Dialogs.ShowColorDialog, Attributes.ColorSource` |
| Object Display Mode | [[Object Display Mode\|Py]] · [[Object Display Mode (cs)\|C#]] | Modo de visualización propio de un objeto en una vista | `Attributes.SetDisplayModeOverride(modo, viewportId)` |
| Overlay Text Display Conduit | [[Overlay Text Display Conduit\|Py]] · [[Overlay Text Display Conduit (cs)\|C#]] | Texto fijo en una esquina de la vista con un conduit | `DisplayConduit → e.Display.Draw2dText` |
| Pick Points | [[Pick Points (cs)\|C#]] | Puntos temporales dibujados con un conduit y seleccionables | `DisplayConduit + clase GetPoint propia` |
| Read Dimension Text | [[Read Dimension Text (cs)\|C#]] | Lee el texto que muestra una cota | `AnnotationObjectBase.DisplayText` |
| Replace Hatch Pattern | [[Replace Hatch Pattern\|Py]] · [[Replace Hatch Pattern (cs)\|C#]] | Cambia el patrón de los sombreados seleccionados | `HatchGeometry.PatternIndex → CommitChanges` |
| Set RhinoPageView Width and Height | [[Set RhinoPageView Width and Height (cs)\|C#]] | Cambia el tamaño de la hoja de un layout | `RhinoPageView.PageWidth / PageHeight` |
| Set Viewport Name | [[Set Viewport Name\|Py]] · [[Set Viewport Name (cs)\|C#]] | Cambia el nombre de una vista | `view.MainViewport.Name` |
| Show Surface Direction | [[Show Surface Direction (cs)\|C#]] | Muestra las normales de una superficie con flechas (conduit) | `BrepFace.NormalAt → e.Display.DrawDirectionArrow` |
| Single Color Back Faces | [[Single Color Back Faces (cs)\|C#]] | Lee los colores de las caras traseras en cada modo de visualización | `DisplayModeDescription.DisplayAttributes` |
| Sprite Drawing | [[Sprite Drawing (cs)\|C#]] | Dibuja imágenes pequeñas (sprites) en la vista | `DisplayPipeline.PostDrawObjects → DrawSprite` |
| Text Justify | [[Text Justify\|Py]] · [[Text Justify (cs)\|C#]] | Texto centrado con una fuente dada | `TextEntity.Justification, doc.Fonts.FindOrCreate` |
| Viewport Resolution | [[Viewport Resolution\|Py]] · [[Viewport Resolution (cs)\|C#]] | Tamaño en píxeles de la vista activa | `ActiveViewport.Size` |
| Visual Analysis Modes | [[Visual Analysis Modes (cs)\|C#]] | Modo de análisis propio: colores según la altura Z | `VisualAnalysisMode.Register → EnableVisualAnalysisMode` |
| Zoom to Object | [[Zoom to Object\|Py]] · [[Zoom to Object (cs)\|C#]] | Encuadra un objeto en la vista | `Viewport.ZoomBoundingBox(caja)` |

## Componentes de Grasshopper (156)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (9)

- [[Catálogo - Params#Angular Dimension (parámetro)|Angular Dimension (parámetro)]] — Contiene una colección de cotas angulares
- [[Catálogo - Params#Annotation Dot (parámetro)|Annotation Dot (parámetro)]] — Contiene una colección de puntos de anotación (dots)
- [[Catálogo - Params#Centermark (parámetro)|Centermark (parámetro)]] — Contiene una colección de marcas de centro
- [[Catálogo - Params#Hatch (parámetro)|Hatch (parámetro)]] — Contiene una colección de sombreados (hatches)
- [[Catálogo - Params#Leader (parámetro)|Leader (parámetro)]] — Contiene una colección de directrices (leaders)
- [[Catálogo - Params#Linear Dimension (parámetro)|Linear Dimension (parámetro)]] — Contiene una colección de cotas lineales
- [[Catálogo - Params#Ordinate Dimension (parámetro)|Ordinate Dimension (parámetro)]] — Contiene una colección de cotas por coordenadas
- [[Catálogo - Params#Radial Dimension (parámetro)|Radial Dimension (parámetro)]] — Contiene una colección de cotas radiales
- [[Catálogo - Params#Text Entity (parámetro)|Text Entity (parámetro)]] — Contiene una colección de entidades de texto

### Params › Primitive (3)

- [[Catálogo - Params#Colour (Col, parámetro)|Colour (Col, parámetro)]] — Contiene una colección de colores RGB
- [[Catálogo - Params#Font (parámetro)|Font (parámetro)]] — Contiene una colección de fuentes
- [[Catálogo - Params#Shader (parámetro)|Shader (parámetro)]] — Contiene una colección de materiales de visualización

### Display › Colour (11)

- [[Catálogo - Display#Colour CMYK (CMYK)|Colour CMYK (CMYK)]] — Crea un color a partir de canales {CMYK} en coma flotante
- [[Catálogo - Display#Colour HSL (HSL)|Colour HSL (HSL)]] — Crea un color a partir de canales {HSL} en coma flotante
- [[Catálogo - Display#Colour HSV (HSV)|Colour HSV (HSV)]] — Crea un color a partir de canales {HSV} en coma flotante
- [[Catálogo - Display#Colour L*ab (L*AB)|Colour L*ab (L*AB)]] — Crea un color a partir de canales {CIE L*ab} en coma flotante
- [[Catálogo - Display#Colour LCH (LCH)|Colour LCH (LCH)]] — Crea un color a partir de canales {CIE LCH} en coma flotante
- [[Catálogo - Display#Colour RGB (f) (fRGB)|Colour RGB (f) (fRGB)]] — Crea un color a partir de canales {RGB} en coma flotante
- [[Catálogo - Display#Colour RGB (RGB)|Colour RGB (RGB)]] — Crea un color a partir de canales {RGB}
- [[Catálogo - Display#Colour XYZ (XYZ)|Colour XYZ (XYZ)]] — Crea un color a partir de canales {XYZ} en coma flotante (especificación CIE 1931)
- [[Catálogo - Display#Split AHSL (AHSL)|Split AHSL (AHSL)]] — Separa un color en canales {AHSL} en coma flotante
- [[Catálogo - Display#Split AHSV (AHSV)|Split AHSV (AHSV)]] — Separa un color en canales {AHSV} en coma flotante
- [[Catálogo - Display#Split ARGB (ARGB)|Split ARGB (ARGB)]] — Separa un color en canales {ARGB} en coma flotante

### Display › Dimensions (16)

- [[Catálogo - Display#Aligned Dimension (AlignDim)|Aligned Dimension (AlignDim)]] — Crea una cota de distancia entre dos puntos
- [[Catálogo - Display#Angular Dimension (AngleDim)|Angular Dimension (AngleDim)]] — Crea una cota de ángulo entre puntos
- [[Catálogo - Display#Angular Dimensions (Mesh) (AngleDimMesh)|Angular Dimensions (Mesh) (AngleDimMesh)]] — Crea cotas de ángulo en todas las esquinas de una malla
- [[Catálogo - Display#Arc Dimension (ArcDim)|Arc Dimension (ArcDim)]] — Crea una cota de ángulo a partir de un arco
- [[Catálogo - Display#Circular Dimension (CircleDim)|Circular Dimension (CircleDim)]] — Crea una cota de ángulo proyectada sobre un círculo
- [[Catálogo - Display#Gradient Hatch (GHatch)|Gradient Hatch (GHatch)]] — Crea un sombreado (hatch) de degradado
- [[Catálogo - Display#Line Dimension (LineDim)|Line Dimension (LineDim)]] — Crea una cota de distancia a lo largo de una línea
- [[Catálogo - Display#Linear Dimension (LinearDim)|Linear Dimension (LinearDim)]] — Crea una cota de distancia entre puntos, proyectada sobre una línea
- [[Catálogo - Display#Make2D|Make2D]] — Crea un dibujo de líneas ocultas a partir de la geometría
- [[Catálogo - Display#Make2D Parallel View (M2D Parallel)|Make2D Parallel View (M2D Parallel)]] — Define una vista paralela para una solución Make2D
- [[Catálogo - Display#Make2D Perspective View (M2D Perspective)|Make2D Perspective View (M2D Perspective)]] — Define una vista en perspectiva para una solución Make2D
- [[Catálogo - Display#Marker Dimension (MarkDim)|Marker Dimension (MarkDim)]] — Crea una anotación de texto en un punto
- [[Catálogo - Display#Pattern Hatch (PHatch)|Pattern Hatch (PHatch)]] — Crea un sombreado (hatch) con patrón
- [[Catálogo - Display#Serial Dimension (SerialDim)|Serial Dimension (SerialDim)]] — Crea una cota de distancia entre varios puntos, proyectada sobre una línea
- [[Catálogo - Display#Text Tag (Tag)|Text Tag (Tag)]] — Representa una lista de etiquetas de texto en una vista de Rhino
- [[Catálogo - Display#Text Tag 3D (Tag)|Text Tag 3D (Tag)]] — Representa una lista de etiquetas de texto 3D en una vista de Rhino

### Display › Graphs (6)

- [[Catálogo - Display#Bar Graph (parámetro)|Bar Graph (parámetro)]] — Representación en gráfico de barras de un conjunto de números
- [[Catálogo - Display#Image Gallery (Gallery, objeto especial)|Image Gallery (Gallery, objeto especial)]] — Muestra una secuencia de imágenes
- [[Catálogo - Display#Legend|Legend]] — Muestra una leyenda formada por etiquetas y colores
- [[Catálogo - Display#Pie Chart (Pie, parámetro)|Pie Chart (Pie, parámetro)]] — Muestra un conjunto de fragmentos de texto como gráfico de torta
- [[Catálogo - Display#Quick Graph (Graph, parámetro)|Quick Graph (Graph, parámetro)]] — Muestra un conjunto de valores Y como gráfico
- [[Catálogo - Display#Value Tracker (Tracker, parámetro)|Value Tracker (Tracker, parámetro)]] — Registra una colección de valores numéricos a lo largo del tiempo

### Display › Preview (9)

- [[Catálogo - Display#Cloud Display (Cloud)|Cloud Display (Cloud)]] — Dibuja una colección de puntos como una nube difusa
- [[Catálogo - Display#Create Material (Material)|Create Material (Material)]] — Crea un material OpenGL
- [[Catálogo - Display#Custom Curve Preview (Curve Preview)|Custom Curve Preview (Curve Preview)]] — Vista previa personalizada de curvas
- [[Catálogo - Display#Custom Preview (Preview)|Custom Preview (Preview)]] — Permite vistas previas personalizadas de la geometría
- [[Catálogo - Display#Deconstruct Material (DMaterial)|Deconstruct Material (DMaterial)]] — Descompone un material de visualización (sombreador) en sus distintos atributos
- [[Catálogo - Display#Dot Display (Dots)|Dot Display (Dots)]] — Dibuja una colección de puntos de colores
- [[Catálogo - Display#Symbol (Advanced) (SymAdv)|Symbol (Advanced) (SymAdv)]] — Propiedades avanzadas de visualización de símbolos
- [[Catálogo - Display#Symbol (Simple) (SymSim)|Symbol (Simple) (SymSim)]] — Propiedades simples de visualización del símbolo
- [[Catálogo - Display#Symbol Display (Symbol)|Symbol Display (Symbol)]] — Muestra símbolos

### Display › Vector (4)

- [[Catálogo - Display#Point List (Points)|Point List (Points)]] — Muestra detalles de listas de puntos
- [[Catálogo - Display#Point Order (Order)|Point Order (Order)]] — Muestra el orden de una lista de puntos
- [[Catálogo - Display#Vector Display (VDis)|Vector Display (VDis)]] — Previsualiza vectores en la vista
- [[Catálogo - Display#Vector Display Ex (VDisEx)|Vector Display Ex (VDisEx)]] — Previsualiza vectores en la vista

### Rhino › Annotations (24)

- [[Catálogo - Rhino#Aligned Dimension (DimAligned)|Aligned Dimension (DimAligned)]] — Cota alineada
- [[Catálogo - Rhino#Angle Dimension (Arc) (DimAngle-A)|Angle Dimension (Arc) (DimAngle-A)]] — Cota angular a partir de arcos
- [[Catálogo - Rhino#Angle Dimension (Lines) (DimAngle-L)|Angle Dimension (Lines) (DimAngle-L)]] — Cota angular a partir de líneas
- [[Catálogo - Rhino#Angle Dimension (Points) (DimAngle-P)|Angle Dimension (Points) (DimAngle-P)]] — Cota angular
- [[Catálogo - Rhino#Annotation Arrow Settings (AS-Arrows)|Annotation Arrow Settings (AS-Arrows)]] — Ajustes de flechas del estilo de anotación
- [[Catálogo - Rhino#Annotation Dimension Settings (AS-Dimension)|Annotation Dimension Settings (AS-Dimension)]] — Ajustes de cotas del estilo de anotación
- [[Catálogo - Rhino#Annotation Dot (Dot)|Annotation Dot (Dot)]] — Punto de anotación (dot)
- [[Catálogo - Rhino#Annotation Leader Settings (AS-Leaders)|Annotation Leader Settings (AS-Leaders)]] — Ajustes de directrices del estilo de anotación
- [[Catálogo - Rhino#Annotation Style|Annotation Style]] — Estilo de anotación
- [[Catálogo - Rhino#Annotation Style Overrides (A-Style)|Annotation Style Overrides (A-Style)]] — Obtiene/define el estilo de anotación y los atributos reemplazados
- [[Catálogo - Rhino#Annotation Text Overrides (A-Text)|Annotation Text Overrides (A-Text)]] — Gestiona los atributos del texto de la anotación
- [[Catálogo - Rhino#Annotation Text Settings (AS-Text)|Annotation Text Settings (AS-Text)]] — Ajustes de texto del estilo de anotación
- [[Catálogo - Rhino#Annotation Tolerance Settings (AS-Tolerance)|Annotation Tolerance Settings (AS-Tolerance)]] — Ajustes de tolerancia del estilo de anotación
- [[Catálogo - Rhino#Annotation Units Settings (AS-Units)|Annotation Units Settings (AS-Units)]] — Ajustes de unidades del estilo de anotación
- [[Catálogo - Rhino#Centermark|Centermark]] — Marca de centro
- [[Catálogo - Rhino#Evaluate Annotation Text (Evaluate)|Evaluate Annotation Text (Evaluate)]] — Obtiene el texto de la anotación con las expresiones de campos de texto evaluadas
- [[Catálogo - Rhino#Leader|Leader]] — Directriz (leader)
- [[Catálogo - Rhino#Linear Dimension (DimLinear)|Linear Dimension (DimLinear)]] — Cota lineal
- [[Catálogo - Rhino#Model Font (Font)|Model Font (Font)]] — Fuente tipográfica
- [[Catálogo - Rhino#Ordinate Dimension (DimOrdinate)|Ordinate Dimension (DimOrdinate)]] — Cota por coordenadas
- [[Catálogo - Rhino#Query Annotation Styles (Styles)|Query Annotation Styles (Styles)]] — Consulta un documento de Rhino para obtener todos los estilos de anotación disponibles
- [[Catálogo - Rhino#Query Installed Fonts (Fonts)|Query Installed Fonts (Fonts)]] — Consulta todas las fuentes disponibles
- [[Catálogo - Rhino#Radial Dimension (DimRadial)|Radial Dimension (DimRadial)]] — Cota radial
- [[Catálogo - Rhino#Text Entity (Text)|Text Entity (Text)]] — Entidad de texto

### Rhino › Drafting (11)

- [[Catálogo - Rhino#Colour Gradient|Colour Gradient]] — Degradado de color
- [[Catálogo - Rhino#Drafting Scale|Drafting Scale]] — Obtiene o define el factor de escala de anotaciones, tipos de línea y/o patrones de sombreado
- [[Catálogo - Rhino#Export Hatch Pattern (E-Hatch)|Export Hatch Pattern (E-Hatch)]] — Exporta patrones de sombreado a un archivo
- [[Catálogo - Rhino#Gradient Colour Stop (Colour Stop)|Gradient Colour Stop (Colour Stop)]] — Punto de color del degradado
- [[Catálogo - Rhino#Import Hatch Pattern (I-Hatch)|Import Hatch Pattern (I-Hatch)]] — Importa un patrón de sombreado
- [[Catálogo - Rhino#Model Hatch (Hatch)|Model Hatch (Hatch)]] — Sombreado del modelo
- [[Catálogo - Rhino#Model Hatch Line (Hatch Line)|Model Hatch Line (Hatch Line)]] — Línea de sombreado
- [[Catálogo - Rhino#Model Hatch Pattern (Hatch Pattern)|Model Hatch Pattern (Hatch Pattern)]] — Patrón de sombreado del modelo
- [[Catálogo - Rhino#Model Linetype (Linetype)|Model Linetype (Linetype)]] — Tipo de línea del modelo
- [[Catálogo - Rhino#Query Model Hatch Patterns (Hatches)|Query Model Hatch Patterns (Hatches)]] — Consulta un documento de Rhino para obtener todos los patrones de sombreado disponibles
- [[Catálogo - Rhino#Query Model Linetypes (Linetypes)|Query Model Linetypes (Linetypes)]] — Consulta un documento de Rhino para obtener todos los tipos de línea disponibles

### Rhino › Render (18)

- [[Catálogo - Rhino#Directional Light (D-Light)|Directional Light (D-Light)]] — Luz direccional
- [[Catálogo - Rhino#Import Model Environment (I-Environment)|Import Model Environment (I-Environment)]] — Importa un entorno del modelo
- [[Catálogo - Rhino#Import Model Material (I-Material)|Import Model Material (I-Material)]] — Importa un material del modelo
- [[Catálogo - Rhino#Light Attributes (Light)|Light Attributes (Light)]] — Modifica o inspecciona los atributos de una luz
- [[Catálogo - Rhino#Linear Light|Linear Light]] — Luz lineal
- [[Catálogo - Rhino#Model Basic Environment (Basic Environment)|Model Basic Environment (Basic Environment)]] — Entorno básico del modelo
- [[Catálogo - Rhino#Model Material (Material)|Model Material (Material)]] — Material del modelo
- [[Catálogo - Rhino#Point Light|Point Light]] — Luz puntual
- [[Catálogo - Rhino#Query Model Environments (Environments)|Query Model Environments (Environments)]] — Consulta un documento de Rhino para obtener todos los entornos de render disponibles
- [[Catálogo - Rhino#Query Model Lights (Lights)|Query Model Lights (Lights)]] — Consulta un documento de Rhino para obtener todas las luces disponibles
- [[Catálogo - Rhino#Query Model Materials (Materials)|Query Model Materials (Materials)]] — Consulta un documento de Rhino para obtener todos los materiales de render disponibles
- [[Catálogo - Rhino#Query Render Options (Render)|Query Render Options (Render)]] — Consulta un documento de Rhino para obtener sus opciones de render
- [[Catálogo - Rhino#Rectangular Light|Rectangular Light]] — Luz rectangular
- [[Catálogo - Rhino#Skylight|Skylight]] — La luz de cielo (skylight) de Rhino
- [[Catálogo - Rhino#Spotlight|Spotlight]] — Foco (spotlight)
- [[Catálogo - Rhino#Sun|Sun]] — Sol a partir de un punto de anclaje terrestre y una fecha/hora
- [[Catálogo - Rhino#Sun (Manual Control) (Sun)|Sun (Manual Control) (Sun)]] — Sol a partir del ángulo del norte y los valores de azimut y altitud
- [[Catálogo - Rhino#Sun Preview (S-Preview)|Sun Preview (S-Preview)]] — Previsualiza un sol o su luna asociada

### Rhino › Viewports (6)

- [[Catálogo - Rhino#Model View (View)|Model View (View)]] — Vista del modelo
- [[Catálogo - Rhino#Model Viewport|Model Viewport]] — Vista (viewport) del modelo
- [[Catálogo - Rhino#Query Layouts (Layouts)|Query Layouts (Layouts)]] — Consulta un documento de Rhino para obtener todas las vistas de layout disponibles
- [[Catálogo - Rhino#Query Named Views (Named Views)|Query Named Views (Named Views)]] — Consulta un documento de Rhino para obtener todas las vistas guardadas disponibles
- [[Catálogo - Rhino#Query Viewports (Viewports)|Query Viewports (Viewports)]] — Consulta un documento de Rhino para obtener todas las vistas (viewports) disponibles
- [[Catálogo - Rhino#Zoom Extents (Zoom Ext)|Zoom Extents (Zoom Ext)]] — Hace zoom en la vista para mostrar todos los objetos

### eleFront › 04 Annotations (10)

- [[Catálogo - eleFront#Deconstruct Dimension (DeDim)|Deconstruct Dimension (DeDim)]] — Descompone un objeto cota
- [[Catálogo - eleFront#Deconstruct Hatch (DeHatch)|Deconstruct Hatch (DeHatch)]] — Descompone un sombreado (hatch)
- [[Catálogo - eleFront#Deconstruct Text (DeText)|Deconstruct Text (DeText)]] — Descompone un objeto texto
- [[Catálogo - eleFront#Define Angular Dimension (AngularDim)|Define Angular Dimension (AngularDim)]] — Define un objeto cota angular
- [[Catálogo - eleFront#Define Hatch (Hatch)|Define Hatch (Hatch)]] — Define un objeto sombreado para enviarlo al componente de bake de eleFront
- [[Catálogo - eleFront#Define Leader (Leader)|Define Leader (Leader)]] — Define un objeto directriz (leader)
- [[Catálogo - eleFront#Define Linear Dimension (Linear Dim)|Define Linear Dimension (Linear Dim)]] — Define una cota lineal
- [[Catálogo - eleFront#Define Radial Dimension (RadialDim)|Define Radial Dimension (RadialDim)]] — Define un objeto cota radial
- [[Catálogo - eleFront#Define Text Dot (TextDot)|Define Text Dot (TextDot)]] — Define un objeto punto de texto (text dot)
- [[Catálogo - eleFront#Define Text Object (Text)|Define Text Object (Text)]] — Define un objeto texto

### Human › Display (9)

- [[Catálogo - Human#Custom Preview Lineweights (PreviewLW)|Custom Preview Lineweights (PreviewLW)]] — Vista previa personalizada con grosores de línea
- [[Catálogo - Human#Custom Preview Materials (PreviewMat)|Custom Preview Materials (PreviewMat)]] — Vista previa personalizada con materiales
- [[Catálogo - Human#Render Curve to Screen (CrvToScreen)|Render Curve to Screen (CrvToScreen)]] — Muestra un objeto curva en una posición fija de la pantalla
- [[Catálogo - Human#Render Mesh to Screen (MeshToScreen)|Render Mesh to Screen (MeshToScreen)]] — Muestra un objeto malla en una posición fija de la pantalla
- [[Catálogo - Human#Render Point to Screen (PtToScreen)|Render Point to Screen (PtToScreen)]] — Muestra un objeto punto en una posición fija de la pantalla
- [[Catálogo - Human#Render Text to Screen (TextToScreen)|Render Text to Screen (TextToScreen)]] — Muestra un objeto texto en una posición fija de la pantalla
- [[Catálogo - Human#Screen-Oriented Mesh (ScreenMesh)|Screen-Oriented Mesh (ScreenMesh)]] — Muestra un objeto malla que mantiene siempre la misma orientación respecto de la pantalla
- [[Catálogo - Human#Screen-Oriented Text (ScreenText)|Screen-Oriented Text (ScreenText)]] — Muestra texto que mantiene siempre la misma orientación respecto de la pantalla
- [[Catálogo - Human#Screen-To-World Tag (S2WTag)|Screen-To-World Tag (S2WTag)]] — Crea una etiqueta especial anclada a una ubicación de la pantalla y a una ubicación del modelo

### Human › Image (5)

- [[Catálogo - Human#Bitmap from File (Bitmap)|Bitmap from File (Bitmap)]] — Carga una imagen desde una ruta de archivo
- [[Catálogo - Human#Deserialize Image from String (Str2Img)|Deserialize Image from String (Str2Img)]] — Convierte un texto codificado en Base-64 que representa una imagen en un archivo de imagen temporal y…
- [[Catálogo - Human#Picture Source (PicSrc)|Picture Source (PicSrc)]] — Obtiene la ruta del mapa de bits de una superficie de Rhino referenciada, creada con el comando Picture o…
- [[Catálogo - Human#Sample Bitmap (SampleBMP)|Sample Bitmap (SampleBMP)]] — Este componente permite muestrear el color y el brillo de los píxeles de un mapa de bits. Las coordenadas…
- [[Catálogo - Human#Serialize Image to String (Img2Str)|Serialize Image to String (Img2Str)]] — Convierte un archivo de imagen en un texto que se puede incrustar en tu archivo. ¡No lo uses con imágenes…

### Human › Texture Mapping (6)

- [[Catálogo - Human#BoxMapping (BoxMap)|BoxMapping (BoxMap)]] — Aplica un mapeo de textura de caja a una malla
- [[Catálogo - Human#Custom Mapping (Custom Map)|Custom Mapping (Custom Map)]] — Aplica coordenadas de textura por vértice a una malla
- [[Catálogo - Human#CylinderMapping (CylinderMap)|CylinderMapping (CylinderMap)]] — Aplica un mapeo de textura cilíndrico a una malla
- [[Catálogo - Human#PlanarMapping (PlanarMap)|PlanarMapping (PlanarMap)]] — Aplica un mapeo de textura plano a una malla
- [[Catálogo - Human#SphericalMapping (SphericalMap)|SphericalMapping (SphericalMap)]] — Aplica un mapeo de textura esférico a una malla
- [[Catálogo - Human#SurfaceMapping (SurfaceMap)|SurfaceMapping (SurfaceMap)]] — Aplica un mapeo de textura UV de superficie a una malla

### Pufferfish › Color (9)

- [[Catálogo - Pufferfish#Color To Point (Col2Pt)|Color To Point (Col2Pt)]] — Convierte un color en un punto usando los valores RGB del color como valores XYZ del punto
- [[Catálogo - Pufferfish#Grayscale Color (GrayCol)|Grayscale Color (GrayCol)]] — Convierte un color a escala de grises con distintos esquemas comunes de ponderación de luminosidad
- [[Catálogo - Pufferfish#Invert Color (InvCol)|Invert Color (InvCol)]] — Invierte un color
- [[Catálogo - Pufferfish#Mirror Combine Colors (MirComCols)|Mirror Combine Colors (MirComCols)]] — Refleja un conjunto de colores desde su final o su inicio y lo combina con el conjunto original
- [[Catálogo - Pufferfish#Mirror Cut Colors (MirCutCols)|Mirror Cut Colors (MirCutCols)]] — Corta un conjunto de colores en un índice, refleja el lado conservado del corte respecto de ese índice y lo…
- [[Catálogo - Pufferfish#Point To Color (Pt2Col)|Point To Color (Pt2Col)]] — Convierte un punto en un color usando los valores XYZ del punto como valores RGB del color
- [[Catálogo - Pufferfish#Tween Consecutive Colors (TwnConCols)|Tween Consecutive Colors (TwnConCols)]] — Interpola (tween) consecutivamente entre un conjunto de colores
- [[Catálogo - Pufferfish#Tween Through Colors (TwnThruCols)|Tween Through Colors (TwnThruCols)]] — Interpola (tween) a través de un conjunto de colores
- [[Catálogo - Pufferfish#Tween Two Colors (Twn2Cols)|Tween Two Colors (Twn2Cols)]] — Interpola (tween) entre dos colores

<!-- AUTO:fin -->
