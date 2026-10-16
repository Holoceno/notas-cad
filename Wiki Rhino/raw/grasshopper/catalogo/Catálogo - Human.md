---
title: "Catálogo Grasshopper — Human"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Human"
libraries: ["Human 1.3.1"]
components: 57
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/human, rhino/documento, rhino/vista]
---

# Human

57 objetos · librería: Human 1.3.1

Mapas: [[Mapa - Documento de Rhino]] (37) · [[Mapa - Visualización y anotaciones]] (20) · [[Mapa - Data trees y listas]] (3) · [[Mapa - Brep y sólidos]] (3)

## Creation

### Bake Geometry (Bake)

Hace bake de la geometría en el documento con los atributos indicados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bake? | `bake` | Boolean | item | Poner en True para hacer bake de los objetos en el documento con los atributos indicados. Este componente está pensado para geometría normal de Grasshopper; si tienes objetos especiales para bake, como luces, sombreados o bloques, usa sus componentes de creación específicos. |
| Geometry | `geo` | Geometry | item | La geometría de Grasshopper a la que hacer bake |
| Attributes *(opcional)* | `att` | Generic Data | item | Los atributos que se asignan a la geometría |

### CreateAttributes (CreateAtts)

Crea atributos de objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name *(opcional)* | `name` | Text | item | El nombre del objeto |
| Layer Name *(opcional)* | `lay` | Text | item | El nombre de la capa en la que está el objeto |
| Color *(opcional)* | `col` | Colour | item | El color de visualización del objeto |
| Material Name *(opcional)* | `mat` | Text | item | El nombre del material de render del objeto |
| Linetype Name *(opcional)* | `lt` | Text | item | El nombre del tipo de línea del objeto |
| Group Indices *(opcional)* | `grp` | Integer | lista | Los índices de los grupos a los que pertenece cada objeto |
| Plot Weight *(opcional)* | `PW` | Number | item | Grosor de impresión del objeto, en mm. |
| Plot Color *(opcional)* | `PC` | Colour | item | El color de impresión del objeto |
| Visibility *(opcional)* | `V` | Boolean | item | True si el objeto está visible, False si está oculto |
| UserData Keys *(opcional)* | `udk` | Text | lista | Las claves de los datos de usuario del objeto |
| UserData Values *(opcional)* | `udv` | Text | lista | Los valores de los datos de usuario del objeto. El largo de la lista debe coincidir con el de las claves |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object Attributes | `att` | Generic Data | item | Atributos de objeto |

### CreateHatch

Crea objetos de sombreado (hatch) con el patrón, la escala, la rotación y los atributos indicados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bake? | `B` | Boolean | item | Pon este valor en True para hacer bake de los sombreados en tu documento activo de Rhino. |
| Curves | `C` | Curve | lista | Los conjuntos de curvas a sombrear. Las curvas de una misma rama se procesan juntas, generando vacíos interiores cuando corresponde. |
| Hatch Pattern Name | `N` | Text | lista | El nombre del sombreado a buscar. Si se deja vacío o no se encuentra, se usa un sombreado sólido. |
| Hatch Scale | `S` | Number | lista | Escala del sombreado |
| Hatch Rotation | `R` | Number | lista | Rotación del sombreado en radianes |
| Attributes *(opcional)* | `att` | Generic Data | lista | Las propiedades de objeto del sombreado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Geometry | `HG` | Geometry | lista | Las superficies o curvas del sombreado indicado |
| Hatch Objects | `HO` | Generic Data | lista | El objeto sombreado nativo. |

### CreateLight

Crea un objeto luz. Por ahora funciona bien con luces puntuales y direccionales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bake? | `bake` | Boolean | item | Pon este valor en True para hacer bake de las luces en tu documento activo de Rhino. |
| Location | `L` | Point | item | La ubicación de la luz |
| Direction | `D` | Vector | item | La dirección de la luz (no aplica a todos los estilos de luz) |
| Light Style | `LS` | Text | item | El estilo de luz del objeto. Por ahora debe ser WorldPoint o WorldDirectional; en el futuro se admitirán WorldSpot, WorldRectangular y WorldLinear. |
| Intensity | `I` | Number | item | La intensidad de la luz, entre 0.0 y 1.0 |
| Color | `C` | Colour | item | El color difuso de la luz |
| Attributes *(opcional)* | `att` | Generic Data | item | Las propiedades de objeto de la luz |

### Define Block (DefBlock)

Este componente permite definir o reemplazar una definición de bloque.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Name | `BN` | Text | item | El nombre de la definición de bloque |
| Geometry | `G` | Geometry | lista | La geometría que forma el bloque. |
| Attributes *(opcional)* | `A` | Generic Data | lista | Los atributos opcionales de la geometría (como capa, color, etc.) |
| Block Origin | `BO` | Plane | item | El plano base de la definición de bloque |
| Overwrite | `O` | Boolean | item | Pon esto en True para sobrescribir la definición de bloque. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Name | `BN` | Text | item | Los nombres de los bloques definidos con éxito |

### JustifiedText3d (Justified Text)

Crea objetos de texto 3D con el tamaño, la ubicación, la alineación y la fuente indicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `L` | Plane | item | Ubicación y orientación del texto |
| Text | `T` | Text | item | Texto a mostrar |
| Size | `S` | Number | item | Tamaño del texto |
| Color *(opcional)* | `C` | Colour | item | Color de visualización del texto |
| Horizontal Alignment | `A` | Integer | item | La alineación horizontal del texto. 0 = izquierda, 1 = centro, 2 = derecha |
| Vertical Alginment | `VA` | Integer | item | La alineación vertical del texto. 0 = abajo, 1 = al medio, 2 = arriba |
| Font *(opcional)* | `F` | Text | item | La fuente a usar |
| Use Meshes | `M` | Boolean | item | ¿Convertir el texto en malla para mostrar transparencia? Ojo: esta función es experimental y no funciona bien con todas las fuentes. |
| Attributes *(opcional)* | `att` | Generic Data | item | Atributos opcionales que se asignan a la geometría al hacer bake. Reemplazan el color de visualización indicado. |
| Bake *(opcional)* | `B` | Boolean | item | Usa esta entrada como disparador automático de bake: ponla en True para hacer bake del texto en el documento de Rhino. |

### PlaceBlock

Coloca un bloque indicado con la transformación deseada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Name | `name` | Text | item | El nombre de la definición de bloque. |
| Transform | `xform` | Transform | item | La transformación a aplicar al bloque |
| Bake? | `bake` | Boolean | item | Pon esto en True para agregar los bloques al documento |
| Attributes *(opcional)* | `att` | Generic Data | item | Atributos de objeto |

## Display

### Custom Preview Lineweights (PreviewLW)

Vista previa personalizada con grosores de línea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a previsualizar |
| Shader | `S` | Shader | item | El sombreador que reemplaza la vista previa |
| Thickness *(opcional)* | `T` | Number | item | El grosor de la visualización en alambre |
| Absolute | `A` | Boolean | item | Poner en True para intentar dibujar las curvas con una dimensión absoluta. |

### Custom Preview Materials (PreviewMat)

Vista previa personalizada con materiales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a previsualizar |
| Diffuse Color *(opcional)* | `DC` | Colour | item | El color difuso base. |
| Transparency *(opcional)* | `T` | Number | item | La transparencia general, de 0 a 1. |
| Diffuse Bitmap *(opcional)* | `DB` | Text | item | La ruta del mapa de bits que se usa en el canal difuso. |
| Transparency Bitmap *(opcional)* | `TB` | Text | item | La ruta del mapa de bits que se usa en el canal de transparencia. |

### Render Curve to Screen (CrvToScreen)

Muestra un objeto curva en una posición fija de la pantalla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `Crv` | Curve | item | Curva a mostrar en pantalla. Asegúrate de que la curva esté en (o cerca de) el origen del mundo. |
| Location | `L` | Point | item | La ubicación donde se muestra el texto. Si "Scale With Viewport" está desmarcado, indica los puntos en coordenadas de píxeles: 100,100,0 queda 100 píxeles a la derecha y hacia abajo desde la esquina superior izquierda de la vista. |
| Scale Factor | `S` | Number | item | Un multiplicador de la escala. Úsalo para ajustar el tamaño de la curva en pantalla. |
| Color *(opcional)* | `C` | Colour | item | El color con que se muestra la curva. |
| Thickness | `T` | Integer | item | El grosor de línea con que se muestra la curva. |
| Depth | `D` | Number | item | Un valor entre 0 y 1 que controla la profundidad Z de la curva en pantalla. Un número alto aparece delante de la mayoría de los objetos y uno bajo, detrás. Evita valores exactamente iguales a 0 o 1: quédate un poco dentro de los límites para evitar artefactos |
| Fixed | `F` | Boolean | item | Si es True, los objetos quedan fijos y orientados al plano de la pantalla; si es False, los objetos rotan cuando rota la vista. |

### Render Mesh to Screen (MeshToScreen)

Muestra un objeto malla en una posición fija de la pantalla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a mostrar en pantalla. Asegúrate de que la malla esté en (o cerca de) el origen del mundo. |
| Location | `L` | Point | item | La ubicación donde se muestra la malla. Si "Scale With Viewport" está desmarcado, indica los puntos en coordenadas de píxeles: 100,100,0 queda 100 píxeles a la derecha y hacia abajo desde la esquina superior izquierda de la vista. |
| Scale Factor | `S` | Number | item | Un multiplicador de la escala. Úsalo para ajustar el tamaño de la malla en pantalla. |
| Color *(opcional)* | `C` | Colour | item | El color con que se muestra la malla. No reemplaza los colores por vértice de la malla. |
| Depth | `D` | Number | item | Un valor entre 0 y 1 que controla la profundidad Z de la malla en pantalla. Un número alto aparece delante de la mayoría de los objetos y uno bajo, detrás. Evita valores exactamente iguales a 0 o 1: quédate un poco dentro de los límites para evitar artefactos |
| Fixed | `F` | Boolean | item | Si es True, los objetos quedan fijos y orientados al plano de la pantalla; si es False, los objetos rotan cuando rota la vista. |
| Bitmap Texture *(opcional)* | `T` | Text | item | Si se entrega, una textura de mapa de bits para la malla. Usa los componentes de mapeo de texturas para alinearla. |

### Render Point to Screen (PtToScreen)

Muestra un objeto punto en una posición fija de la pantalla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto a mostrar en pantalla. Asegúrate de que el punto esté en (o cerca de) el origen del mundo. |
| Location | `L` | Point | item | La ubicación donde se muestra el punto. Si "Scale With Viewport" está desmarcado, indica los puntos en coordenadas de píxeles: 100,100,0 queda 100 píxeles a la derecha y hacia abajo desde la esquina superior izquierda de la vista. |
| Scale Factor | `S` | Number | item | Un multiplicador de la escala. Úsalo para ajustar el tamaño de la curva en pantalla. |
| Color *(opcional)* | `C` | Colour | item | El color con que se muestra el punto. |
| Radius | `R` | Integer | item | El tamaño con que se muestra el punto. |
| Depth | `D` | Number | item | Un valor entre 0 y 1 que controla la profundidad Z del punto en pantalla. Un número alto aparece delante de la mayoría de los objetos y uno bajo, detrás. Evita valores exactamente iguales a 0 o 1: quédate un poco dentro de los límites para evitar artefactos |
| Fixed | `F` | Boolean | item | Si es True, los objetos quedan fijos y orientados al plano de la pantalla; si es False, los objetos rotan cuando rota la vista. |

### Render Text to Screen (TextToScreen)

Muestra un objeto texto en una posición fija de la pantalla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | El texto a dibujar en pantalla |
| Location | `L` | Point | item | La ubicación donde se muestra el texto. Indica los puntos en coordenadas de píxeles: 100,100,0 queda 100 píxeles a la derecha y hacia abajo desde la esquina superior izquierda de la vista. |
| Size | `S` | Number | item | La altura del texto en píxeles. |
| Color | `C` | Colour | item | El color con que se muestra el texto |
| Font *(opcional)* | `F` | Text | item | La fuente a usar |

### Screen-Oriented Mesh (ScreenMesh)

Muestra un objeto malla que mantiene siempre la misma orientación respecto de la pantalla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a mostrar en pantalla. Asegúrate de que la malla esté en (o cerca de) el origen del mundo. |
| Location | `L` | Point | item | La ubicación donde se muestra la malla |
| Size Factor | `S` | Number | item | Un multiplicador de la escala. Úsalo para ajustar el tamaño de la malla en pantalla. |
| Color *(opcional)* | `C` | Colour | item | El color con que se muestra la malla. No reemplaza los colores por vértice de la malla. |
| Depth | `D` | Number | item | Un valor que controla la profundidad Z de la malla en pantalla. Los números altos aparecen delante de la mayoría de los objetos y los bajos, detrás. Valores demasiado altos pueden hacer que desaparezca por completo. |
| Absolute | `A` | Boolean | item | Si es True, los objetos mantienen un tamaño fijo respecto de las dimensiones del mundo; si es False, siempre tienen el mismo tamaño respecto de la pantalla |
| Bitmap Texture *(opcional)* | `T` | Text | item | Si se entrega, una textura de mapa de bits para la malla. Usa los componentes de mapeo de texturas para alinearla. |

### Screen-Oriented Text (ScreenText)

Muestra texto que mantiene siempre la misma orientación respecto de la pantalla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | El texto a dibujar en pantalla |
| Font *(opcional)* | `F` | Text | item | La fuente a usar |
| Justification *(opcional)* | `J` | Integer | item | Justificación del texto |
| Location | `L` | Point | item | La ubicación donde se muestra el texto |
| Size Factor | `S` | Number | item | Un multiplicador de la escala. Úsalo para ajustar el tamaño del texto en pantalla. |
| Color *(opcional)* | `C` | Colour | item | El color con que se muestra el texto. |
| Depth | `D` | Number | item | Un valor que controla la profundidad Z del texto en pantalla. Los números altos aparecen delante de la mayoría de los objetos y los bajos, detrás. Valores demasiado altos pueden hacer que desaparezca por completo. |
| Absolute | `A` | Boolean | item | Si es True, el texto mantiene un tamaño fijo respecto de las dimensiones del mundo; si es False, siempre tiene el mismo tamaño respecto de la pantalla |

### Screen-To-World Tag (S2WTag)

Crea una etiqueta especial anclada a una ubicación de la pantalla y a una ubicación del modelo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tag Text | `T` | Text | item | El texto a mostrar en la etiqueta |
| Tag Screen Location | `SL` | Point | item | La ubicación en coordenadas de pantalla (píxeles) donde va la etiqueta |
| Tag World Location | `WL` | Point | item | La ubicación en el espacio del mundo a la que debe apuntar la etiqueta |
| Tag Justification | `J` | Integer | item | La alineación de la etiqueta. Controla tanto la alineación del texto como la dirección hacia la que sale la línea de la etiqueta. Si eliges alineación a la izquierda, la línea sale hacia la derecha. |
| Font Name *(opcional)* | `F` | Text | item | El nombre de la fuente a usar |
| Font Size | `FS` | Number | item | El tamaño de la fuente |
| Color | `C` | Colour | item | El color del texto y de las líneas |
| Tag Extension | `TE` | Integer | item | La longitud de extensión (en píxeles) de la línea que sale de la etiqueta. Pon 0 para una línea recta simple. |
| Line Weight | `LW` | Integer | item | El grosor de la línea |

## Document Info

### Font Table (Fonts)

Obtiene la lista de fuentes del sistema.

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fonts | `F` | Text | lista | Una lista de las fuentes del sistema disponibles. |

### Hatch Table (HatchTable)

Obtiene los sombreados del documento activo de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Update | `U` | Boolean | árbol | Activa esto para actualizar el componente si se agregaron sombreados nuevos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatches | `H` | Text | lista | La lista de nombres de patrones de sombreado del documento activo |

### Layer Table (LayerTable)

Obtiene la lista de capas del documento activo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Update | `U` | Boolean | árbol | Pon este valor en True para actualizar la tabla de capas |
| Auto-Update | `AU` | Boolean | item | Si este valor está en True, el componente escucha los cambios de la tabla de capas y se actualiza solo cada vez que algo cambia. Úsalo con cuidado: puedes crear un bucle infinito si más adelante creas capas a partir de las salidas de este componente. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layers | `L` | Text | lista | La lista de nombres de capas del documento activo |
| Full Layer Paths | `LF` | Text | lista | La lista de nombres de capas del documento, con la información de anidación |
| Layer Colors | `C` | Colour | lista | Los colores de las capas del documento |
| Linetypes | `LT` | Text | lista | La lista de tipos de línea asociados a las capas del documento |
| Material Names | `M` | Text | lista | La lista de nombres de materiales asociados a las capas del documento |
| Visible | `V` | Boolean | lista | True si la capa está visible. |
| Print Width | `PW` | Number | lista | Los grosores de impresión asociados a las capas del documento |
| Print Color | `PC` | Colour | lista | El color de impresión de la capa |

### Linetype Table (LT Table)

Obtiene los tipos de línea del documento activo de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Update | `U` | Boolean | árbol | Activa esto para actualizar el componente si se agregaron tipos de línea nuevos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linetypes | `LT` | Text | árbol | La lista de nombres de tipos de línea del documento activo |
| Linetype Pattern | `pat` | Number | árbol | El patrón de longitudes de segmento asociado al tipo de línea |

### Material Table (MatTable)

Accede a los materiales de render del documento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| update | `U` | Boolean | árbol | Cambia este interruptor booleano para refrescar la lista de materiales del documento |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material Name | `MN` | Text | lista | Los nombres de los materiales del documento |
| Shader | `S` | Shader | lista | Un sombreador de Grasshopper que se aproxima lo más posible al material de render. |
| Diffuse | `Kd` | Colour | lista | Color del canal difuso |
| Specular | `Ks` | Colour | lista | Color del brillo especular |
| Emission | `Ke` | Colour | lista | Color emisivo del material |
| Alpha | `A` | Number | lista | Cantidad de transparencia (0.0 = transparente, 1.0 = opaco) |
| Gloss | `G` | Number | lista | Cantidad de brillo del material (0.0 = mate, 1.0 = brillo total) |

### Named Views and Display Modes (ViewsAndModes)

Obtiene una lista de las vistas guardadas y los modos de visualización de este documento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Update | `U` | Boolean | árbol | Activa esto para actualizar la lista de vistas guardadas y modos de visualización. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Named Views | `NV` | Text | lista | La lista de nombres de las vistas guardadas |
| Display Modes | `DM` | Text | lista | La lista de modos de visualización disponibles |

### Viewport Properties (Viewports)

Obtiene una lista de las vistas y sus propiedades

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Update | `U` | Boolean | árbol | Activa esto para forzar una actualización cuando la actualización automática no está activa. |
| Auto Update | `AU` | Boolean | item | Poner en True para escuchar ciertos cambios en las vistas. El componente se actualiza cuando cambia la vista activa o cuando se agregan, eliminan o renombran vistas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Viewport Names | `VP` | Text | lista | La lista de vistas |
| Active Viewport Index | `I` | Integer | item | El índice de la vista activa actual |
| Viewport Bounds | `B` | Rectangle | lista | Un rectángulo por cada vista |
| Viewport Display Mode | `DM` | Text | lista | El nombre en inglés del modo de visualización de cada vista |
| Camera Location | `CL` | Point | lista | La ubicación de la cámara en cada vista |
| Camera Target | `CT` | Point | lista | La ubicación del objetivo de la cámara en cada vista |
| Camera Plane | `CP` | Plane | lista | El plano de la cámara de cada vista |
| Camera Lens Length | `CLL` | Number | lista | La longitud focal (equivalente 35 mm) de la cámara en cada vista |
| Camera Projection | `CPr` | Boolean | lista | True si la cámara usa proyección en perspectiva |
| Camera Up | `CU` | Vector | lista | El vector "arriba" de la cámara en cada vista |

## Document Modifications

### Create/Modify Layers (Layers)

Crea y modifica capas de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer Name | `L` | Text | item | Capa a agregar o modificar |
| Layer Color *(opcional)* | `C` | Colour | item | Color de visualización de la capa |
| Layer Linetype *(opcional)* | `LT` | Text | item | El nombre del tipo de línea de la capa. La lista de tipos de línea disponibles se obtiene con el componente Linetype Table. |
| Layer Material *(opcional)* | `M` | Text | item | El nombre del material de render de la capa. Déjalo como texto vacío para el material por defecto. |
| Visibility *(opcional)* | `V` | Boolean | item | True si la capa está visible. |
| Print Width *(opcional)* | `PW` | Number | item | Grosor de impresión de la capa. 0.0 = por defecto |
| Print Color *(opcional)* | `PC` | Colour | item | Color de impresión de la capa. |
| Delete Layer | `D` | Boolean | item | Poner en True para eliminar la capa |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer Names | `L` | Text | item | Si funciona, el nombre de la capa creada/modificada. |
| Layer Full Path | `FP` | Text | item | Si funciona, la ruta completa de la capa creada/modificada. |

### Create/Modify Materials (Materials)

Crea o edita materiales de render del documento. Ojo: el componente solo puede modificar materiales que él mismo creó antes; no reconoce materiales agregados a mano al documento de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `MN` | Text | item | Nombre del material a agregar o modificar. |
| Diffuse *(opcional)* | `Kd` | Colour | item | Color del canal difuso |
| Specular *(opcional)* | `Ks` | Colour | item | Color del brillo especular |
| Emission *(opcional)* | `Ke` | Colour | item | Color emisivo del material |
| Alpha *(opcional)* | `A` | Number | item | Cantidad de transparencia (0.0 = transparente, 1.0 = opaco) |
| Gloss *(opcional)* | `G` | Number | item | Cantidad de brillo del material (0.0 = mate, 1.0 = brillo total) |
| Diffuse Bitmap *(opcional)* | `DB` | Text | item | Ruta de una imagen para el canal difuso |
| Transparency Bitmap *(opcional)* | `TB` | Text | item | Ruta de una imagen para el canal de transparencia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `MN` | Text | item | Nombre de los materiales agregados o modificados con éxito |

### Modify Object Attributes (ModAtts)

Usa este componente para modificar los atributos de objeto de geometría en Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `O` | Guid | item | Los objetos referenciados a modificar |
| Attributes | `A` | Generic Data | item | Los nuevos atributos de objeto a aplicar. |

### Modify Viewport (Mod Viewport)

Usa este componente para restaurar una vista guardada en una vista, definir su modo de visualización o su cámara.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Viewport Name *(opcional)* | `N` | Text | item | El nombre de la vista a modificar. Si se deja vacío, se usa la vista activa. |
| Named View to Restore *(opcional)* | `NV` | Text | item | El nombre opcional de una vista guardada a restaurar en esta vista. |
| Display Mode *(opcional)* | `DM` | Text | item | Modo de visualización opcional para esta vista. |
| Camera Location *(opcional)* | `CL` | Point | item | El punto opcional de ubicación de la cámara. Reemplaza a la vista guardada. |
| Camera Target *(opcional)* | `CT` | Point | item | El punto opcional de objetivo de la cámara. Reemplaza a la vista guardada. |
| Camera Projection *(opcional)* | `CPr` | Boolean | item | Un booleano opcional para la proyección de la cámara: False para paralela, True para perspectiva. |
| Camera Lens Length *(opcional)* | `CLL` | Number | item | Longitud focal opcional de la cámara en perspectiva |
| Camera Up *(opcional)* | `CU` | Vector | item | El vector "arriba" de la cámara |

## Image

### Bitmap from File (Bitmap)

Carga una imagen desde una ruta de archivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bitmap Path | `P` | Text | item | La ruta del archivo de la imagen (jpg, png, etc.) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bitmap | `B` | Generic Data | item | El objeto mapa de bits |
| Width | `W` | Integer | item | El ancho del mapa de bits en píxeles |
| Height | `H` | Integer | item | El alto del mapa de bits en píxeles |

### Deserialize Image from String (Str2Img)

Convierte un texto codificado en Base-64 que representa una imagen en un archivo de imagen temporal y devuelve su ruta.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Image String | `I` | Text | item | La imagen serializada como texto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Path | `P` | Text | item | Una ruta temporal que apunta a la imagen |

### Picture Source (PicSrc)

Obtiene la ruta del mapa de bits de una superficie de Rhino referenciada, creada con el comando Picture o PictureFrame.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Picture Surface | `P` | Surface | item | Una superficie referenciada creada con el comando Picture o PictureFrame de Rhino. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bitmap Path | `P` | Text | item | La ruta del mapa de bits de esta superficie. |

### Sample Bitmap (SampleBMP)

Este componente permite muestrear el color y el brillo de los píxeles de un mapa de bits. Las coordenadas deben estar en el rango de 0,0 a 1,1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bitmap | `B` | Generic Data | item | El mapa de bits a muestrear |
| Coordinates | `C` | Point | lista | Coordenadas tipo UV entre 0,0 y 1,1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colors | `C` | Colour | lista | Los valores de color RGB en cada punto de muestreo |
| Values | `V` | Number | lista | Los valores de brillo en cada punto de muestreo, en el rango de 0 a 1 |

### Serialize Image to String (Img2Str)

Convierte un archivo de imagen en un texto que se puede incrustar en tu archivo. ¡No lo uses con imágenes grandes!

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Image Path | `P` | Text | item | La ruta del archivo de imagen |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Image | `I` | Text | item | El mapa de bits codificado en Base64 como texto |

## Misc

### Clickable Mesh (ClickM)

Permite hacer clic en la vista de Rhino para seleccionar de una lista de mallas. ¡ADVERTENCIA! Captura TODOS los clics del mouse en Rhino: mientras esté activo no podrás usar Rhino con normalidad.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Enable | `E` | Boolean | item | Activa el modo de selección con clic. |
| Meshes | `M` | Mesh | lista | Las mallas sobre las que quieres poder hacer clic |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Selected Meshes | `M` | Mesh | lista | Las mallas en las que se hizo clic |
| Selected Indices | `I` | Integer | lista | Los índices de las mallas seleccionadas |
| Mouse Line | `ML` | Line | árbol | La línea que representa la ubicación del mouse |

### Convert To Document Units (DocUnits)

Interpreta un texto de distancia con formato (como 5'-10") y lo convierte a número en las unidades del documento activo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value string | `V` | Text | item | El texto de distancia con formato a interpretar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value in Document Units | `V` | Number | item | Un valor numérico que representa la distancia indicada en las unidades del documento activo. |

### DeleteOnLayer (DelOnLay)

Elimina todos los objetos de las capas indicadas y luego entrega True. Sirve para simular que se cambia un objeto directamente en un documento de Rhino y aprovechar las capacidades avanzadas de visualización. ADVERTENCIA: asegúrate de que ninguna parte de tu definición referencie objetos de esas capas, ni con parámetros estándar ni con componentes de Human. ¡SI NO RESPETAS ESTA ADVERTENCIA PUEDES HACER QUE GRASSHOPPER SE CAIGA!

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Run | `run` | Boolean | item | Si está en True, elimina los objetos de la capa o capas indicadas. |
| Layer | `lay` | Text | árbol | Capa cuyos objetos se eliminarán. ¡Atención: elimina todos los objetos de la capa indicada cuando run está en True! |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| run | `run` | Boolean | item | Entrega el valor de la entrada "run" cuando los objetos ya se eliminaron. |

### Directory Contents (Dir)

Lista los archivos de una carpeta indicada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Folder Path | `P` | Text | item | La carpeta a listar |
| Filter *(opcional)* | `F` | Text | item | Un filtro opcional, por ejemplo para limitar los tipos de archivo. |
| Include Subfolders | `S` | Boolean | item | Si está en True, también obtiene archivos de las subcarpetas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Paths | `F` | Text | lista | Los archivos de la carpeta indicada. |
| File Names | `N` | Text | lista | Solo los nombres de archivo, sin extensión. |

### Dispatch Multiple (MDispatch)

Reparte (dispatch) varias listas a la vez. Solo obtiene los valores True; usa invertir para obtener los otros.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dispatch Pattern | `DP` | Boolean | lista | Una lista de booleanos que controla el filtrado. Debe tener la misma cantidad de elementos que todas las listas a filtrar |
| List 0 *(opcional)* | `0` | Generic Data | lista | Lista a filtrar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List 0 | `0` | Generic Data | lista | Lista filtrada |

### Filter By Item (IFilter)

Filtra una o varias listas según una lista guía y un subconjunto de esa lista guía.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guide List | `G` | Text | lista | La lista de elementos en la que se basa el filtrado. Debe tener la misma cantidad de elementos que todas las listas a filtrar |
| Selected Items *(opcional)* | `S` | Text | lista | Los elementos que quieres incluir |
| List 0 *(opcional)* | `0` | Generic Data | lista | Lista a filtrar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List 0 | `0` | Generic Data | lista | Lista filtrada |

### Item Selector (List, parámetro)

Permite seleccionar uno o varios elementos de una lista de entrada

Tipo de dato: **Goo**

### Read 3dm File (3dm)

Lee objetos de un archivo .3dm externo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `FP` | Text | item | La ruta del o los archivos 3dm a leer |
| Layer Filter | `L` | Text | item | Un filtro para el nombre de capa |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `O` | Geometry | lista | La geometría de los objetos |
| Layer Names | `L` | Text | lista | Rutas completas de capa por objeto |
| Attributes | `A` | Generic Data | item | Los atributos de cada objeto |
| Units | `U` | Text | item | Las unidades del archivo |

### Save Viewport To File (SaveView)

Guarda una captura o un render de una vista en la ruta indicada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Run | `R` | Boolean | item | Poner en True para guardar la vista |
| Viewport Name *(opcional)* | `VP` | Text | item | El nombre de la vista a capturar. Si no se entrega, se usa la vista activa. |
| Render | `Rnd` | Boolean | item | Poner en True para renderizar con el motor de render actual. Si usas V-Ray, asegúrate de configurarlo en "Batch". |
| File Path | `FP` | Text | item | La ubicación donde se guarda la captura |
| Scale Factor | `Sc` | Number | item | Un factor de escala que multiplica las dimensiones actuales de la vista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Saved File Path | `P` | Text | item | La ruta del archivo de imagen guardado con éxito |

## Reference

### Dynamic Geometry Pipeline (DPipeline)

Define un pipeline de geometría de Rhino a Grasshopper, con filtros variables por nombre, tipo de objeto y capa.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer Filter | `lay` | Text | item | El filtro distingue mayúsculas y minúsculas. Se permiten estos comodines: ? (cualquier carácter), * (cero o más caracteres), # (cualquier dígito [0-9]), [chars] (cualquier carácter de chars), [!chars] (cualquier carácter que no esté en chars) |
| Type Filter *(opcional)* | `type` | Text | lista | El tipo se indica con una lista de textos: 'Point', 'Curve', 'Brep', 'Mesh', 'Hatch', 'Extrusion', 'Light', 'Text' y 'Block'. Además, 'All' acepta todos los tipos y 'Default' incluye solo los tipos que acepta el componente Pipeline nativo. |
| Name Filter | `name` | Text | item | El filtro distingue mayúsculas y minúsculas. Se permiten estos comodines: ? (cualquier carácter), * (cero o más caracteres), # (cualquier dígito [0-9]), [chars] (cualquier carácter de chars), [!chars] (cualquier carácter que no esté en chars) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry Out | `G` | Generic Data | lista | Geometría recolectada |

### Explode Blocks (BlockExplode)

Explota un conjunto de objetos de instancia (bloques) en su geometría

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Objects | `block` | Generic Data | item | Datos de tipo Rhino.DocObjects.InstanceObject |
| Block Name Filter *(opcional)* | `BNF` | Text | item | Un filtro opcional para el nombre del bloque. Solo se procesan/explotan los bloques que coinciden con el filtro (con comodines como *, ?). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `geo` | Generic Data | lista | Geometría del bloque |
| Attributes | `att` | Generic Data | lista | Atributos de objeto |
| Block Name | `name` | Text | lista | El nombre de la definición de bloque |
| BoundingBox | `bbox` | Box | lista | La caja contenedora de la definición de instancia |
| Block Transform | `xform` | Transform | lista | La transformación de esta instancia de bloque |
| Insertion Plane | `pln` | Plane | item | El punto de inserción de esta instancia de bloque. |
| Instance Count | `ct` | Integer | item | La cantidad de instancias de este bloque presentes en el documento de Rhino. |

### Explode Blocks Recursively (BlockExplode R)

Explota de forma recursiva un conjunto de objetos de instancia (bloques) en su geometría, estructurada en un árbol de datos según el anidamiento de los bloques.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Objects | `block` | Generic Data | árbol | Datos de tipo Rhino.DocObjects.InstanceObject |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `geo` | Generic Data | árbol | Geometría del bloque |
| Attributes | `att` | Generic Data | árbol | Atributos de objeto |
| Block Names | `name` | Text | árbol | Los nombres de las definiciones de bloque |
| BoundingBox | `bbox` | Box | árbol | La caja contenedora de la definición de instancia |
| Block Transforms | `xform` | Transform | árbol | La lista de transformaciones de esta instancia de bloque y de todos sus padres |

### Hatch Explode (HatchExp)

Obtiene la geometría y las propiedades de un objeto sombreado (hatch) referenciado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch | `hatch` | Generic Data | item | Un Rhino.DocObjects.HatchObject o un Rhino.Geometry.Hatch |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Boundary Curves | `curves` | Curve | lista | Curvas de contorno del sombreado |
| Hatch Pattern Name | `name` | Text | item | El nombre del patrón de sombreado |
| Hatch Scale | `scale` | Number | item | Escala del sombreado |
| Hatch Rotation | `rot` | Number | item | Rotación del sombreado en radianes |
| Exploded Hatch Geometry | `exp` | Geometry | lista | Geometría del sombreado explotada como curvas o superficies planas |

### LightProperties (LightProps)

Lee las propiedades de una luz desde un Rhino.DocObjects.LightObject

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Light | `light` | Generic Data | item | Un Rhino.DocObjects.LightObject |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Location | `L` | Point | item | La ubicación de la luz |
| Direction | `D` | Vector | item | La dirección de la luz (no aplica a todos los estilos de luz) |
| Light Style | `LS` | Text | item | El estilo de luz del objeto luz |
| Intensity | `I` | Number | item | La intensidad de la luz |
| Color | `C` | Colour | item | El color difuso de la luz |
| Attributes | `att` | Generic Data | item | Las propiedades de objeto de la luz |

### Object Attributes (ObjAtts)

Accede a los atributos individuales de un RhinoObject o de un tipo ObjectAttributes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object or Attributes | `A` | Generic Data | item | El RhinoObject u ObjectAttributes a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `name` | Text | item | El nombre del objeto |
| Layer Name | `lay` | Text | item | El nombre de la capa en la que está el objeto |
| Layer Full Path | `FP` | Text | item | La ruta completa de la capa en la que está el objeto |
| Color | `col` | Colour | item | El color de visualización del objeto |
| Material Name | `mat` | Text | item | El nombre del material de render del objeto |
| Linetype Name | `lt` | Text | item | El nombre del tipo de línea del objeto |
| Group Indices | `grp` | Integer | lista | Los índices de los grupos a los que pertenece cada objeto |
| Plot Weight | `PW` | Number | item | El grosor de impresión del objeto en mm |
| Plot Color | `PC` | Colour | item | El color de impresión del objeto |
| Visibility | `V` | Boolean | item | True si el objeto está visible, False si está oculto |
| UserData Keys | `udk` | Text | lista | Las claves de los datos de usuario de los atributos del objeto |
| UserData Values | `udv` | Text | lista | Los valores de los datos de usuario de los atributos del objeto |

### Objects By Selection (SelObj)

Obtiene los objetos seleccionados actualmente en Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reset | `reset` | Boolean | item | Pon este valor en True para obtener la geometría seleccionada actualmente en Rhino. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Selected Geometry | `G` | Generic Data | item | La geometría de Rhino seleccionada actualmente. |

### Reinstate Tree (ReTree)

Este componente recupera la estructura de árbol de datos de geometría referenciada a la que se hizo bake con "Bake Geometry" usando la opción "Preserve Trees".

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | árbol | Geometría referenciada desde Rhino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | árbol | Geometría con el árbol restablecido |

### Sort Objects By Type (SortByType)

Ordena un conjunto de objetos de Rhino por tipo y extrae la geometría de los tipos que ya existen en Grasshopper.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| RhinoObjects | `rhObj` | Generic Data | lista | Geometría normal de Grasshopper o datos de tipo Rhino.DocObjects.*, como los que salen del componente Dynamic Pipeline |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `pt` | Point | item | Puntos |
| Curves | `crv` | Curve | item | Curvas |
| Surfaces | `srf` | Surface | item | Superficies |
| Breps | `brep` | Brep | item | Breps |
| Meshes | `mesh` | Mesh | item | Mallas |
| Text Objects | `txt` | Generic Data | item | Objetos de texto y anotación |
| Hatch Objects | `hatch` | Generic Data | item | Objetos sombreado (hatch) |
| Light Objects | `light` | Generic Data | item | Objetos luz |
| Blocks | `block` | Generic Data | item | Instancias de bloque |
| Extrusions | `extr` | Brep | item | Objetos extrusión, convertidos a Breps |
| Other | `other` | Generic Data | item | Otros |
| Type Map | `type` | Integer | item | Un índice que corresponde al tipo de cada objeto. 0 = punto, 1 = curva, 2 = superficie, 3 = brep, 4 = malla, 5 = texto, 6 = sombreado, 7 = luz, 8 = bloque, 9 = extrusión, 10 = otro |

### Text Object Info (TxtObjInfo)

Obtiene la ubicación, el plano de orientación, la alineación y el texto de un objeto texto referenciado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Objects | `txtObj` | Generic Data | item | Objetos texto de tipo Rhino.DocObjects.TextObject |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `L` | Plane | item | El plano base del objeto texto |
| Text | `T` | Text | item | El texto |
| Size | `S` | Number | item | La altura del texto |
| Alignment | `A` | Integer | item | La alineación del texto |
| Vertical Alignment | `VA` | Integer | item | La alineación vertical del texto |

## Texture Mapping

### BoxMapping (BoxMap)

Aplica un mapeo de textura de caja a una malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a mapear |
| Box | `B` | Box | item | La caja en la que se basa el mapeo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Mesh | `M` | Mesh | item | La malla con el mapeo de textura aplicado. Para ver el efecto debe usarse junto con el componente Custom Preview with Materials. |

### Custom Mapping (Custom Map)

Aplica coordenadas de textura por vértice a una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a mapear |
| UV texture coordinates | `UV` | Point | lista | Una lista de coordenadas de textura, una por vértice de la malla; normalmente en el rango 0-1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Mesh | `M` | Mesh | item | La malla con el mapeo de textura aplicado. Para ver el efecto debe usarse junto con el componente Custom Preview with Materials. |

### CylinderMapping (CylinderMap)

Aplica un mapeo de textura cilíndrico a una malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a mapear |
| Base Circle | `C` | Circle | item | El círculo base del mapeo. |
| Height | `H` | Number | item | La altura del cilindro de mapeo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Mesh | `M` | Mesh | item | La malla con el mapeo de textura aplicado. Para ver el efecto debe usarse junto con el componente Custom Preview with Materials. |
| Mapping Cylinder | `C` | Brep | item | Un Brep que representa el cilindro de mapeo |

### PlanarMapping (PlanarMap)

Aplica un mapeo de textura plano a una malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a mapear |
| Plane | `P` | Plane | item | El plano base |
| X Extents | `X` | Domain | item | El dominio X |
| Y Extents | `Y` | Domain | item | El dominio Y |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Mesh | `M` | Mesh | item | La malla con el mapeo de textura aplicado. Para ver el efecto debe usarse junto con el componente Custom Preview with Materials. |
| Mapping Plane | `P` | Surface | item | Una superficie que representa el plano de mapeo |

### SphericalMapping (SphericalMap)

Aplica un mapeo de textura esférico a una malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a mapear |
| Base Plane | `P` | Plane | item | El plano base de la esfera de mapeo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Mesh | `M` | Mesh | item | La malla con el mapeo de textura aplicado. Para ver el efecto debe usarse junto con el componente Custom Preview with Materials. |
| Mapping Sphere | `S` | Brep | item | Una superficie que representa la esfera de mapeo |

### SurfaceMapping (SurfaceMap)

Aplica un mapeo de textura UV de superficie a una malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla a mapear |
| Surface | `S` | Surface | item | La superficie a usar para el mapeo. Se ignoran los recortes. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped Mesh | `M` | Mesh | item | La malla con el mapeo de textura aplicado. Para ver el efecto debe usarse junto con el componente Custom Preview with Materials. |
