---
tags: [tipo/mapa, rhino/documento, rhino/capas, software/rhinocommon, software/grasshopper, lenguaje/python]
---

# Documento de Rhino

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Leer y escribir el archivo de Rhino: referenciar objetos, hornear (*bake*) con atributos, capas, grupos, bloques, user text y archivos. Aquí se cruza Grasshopper con los scripts de Rhino: OVERKILL vive de esta API (atributos, grupos, `Replace`).

## Teoría y código
- [[wiki/concepts/rhinocommon-document-api]]: `doc.Objects`, `doc.Layers`, `scriptcontext`
- [[wiki/concepts/rhinocommon-capas-api]] · [[wiki/sources/2026-05-04-rhinopy-capas]]
- [[wiki/concepts/interactive-object-selection]] · [[wiki/concepts/getobject-loop-pattern]] (pendiente)
- Datos propios dentro de cada pieza (material, veta, mueble): muestra **User Data**, en la tabla de abajo; base para el [[wiki/concepts/plugins-rhino-grasshopper|plugin de muebles]]

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) |
|---|---|---|
| Agregar al documento | [[Catálogo - Params#Context Bake (C-Bake)\|Context Bake]] / [[Catálogo - eleFront#Bake Objects (Bake)\|eleFront Bake]] | `doc.Objects.AddCurve(crv, atributos)` |
| Buscar capa | [[Catálogo - Rhino#Query Model Layers (Layers)\|Query Model Layers]] | `doc.Layers.FindName("Corte")` |
| Crear capa | [[Catálogo - Rhino#Model Layer (Layer)\|Model Layer]] | `capa = Rhino.DocObjects.Layer(); capa.Name = "Corte"; doc.Layers.Add(capa)` |
| Objetos de una capa | [[Catálogo - Rhino#Query Model Objects (M-Objects)\|Query Model Objects]] / [[Catálogo - eleFront#Reference by Layer (RefLay)\|Reference by Layer]] | `doc.Objects.FindByLayer(capa)` |
| Cambiar atributos | [[Catálogo - eleFront#Modify Rhino Object Attributes (ModRAtt)\|Modify Rhino Object Attributes]] | `att = obj.Attributes.Duplicate(); ...; doc.Objects.ModifyAttributes(obj, att, True)` |
| Reemplazar geometría sin perder atributos | — | `doc.Objects.Replace(id, nueva)` |
| User text | [[Catálogo - eleFront#Set User String (Set US)\|Set User String]] | `att.SetUserString("material", "MDF 15")` |
| Grupos | [[Catálogo - Transform#Group\|Group]] | `i = doc.Groups.Add(); att.AddToGroup(i)` |

Dentro de Grasshopper el documento es `Rhino.RhinoDoc.ActiveDoc`. Para usar `rhinoscriptsyntax`, primero `scriptcontext.doc = Rhino.RhinoDoc.ActiveDoc`.

## Para empezar
[[Catálogo - Rhino#Query Model Objects (M-Objects)|Query Model Objects]] · [[Catálogo - Rhino#Model Object (Object)|Model Object]] · [[Catálogo - Rhino#Model Layer (Layer)|Model Layer]] · [[Catálogo - eleFront#Reference by Layer (RefLay)|Reference by Layer]] · [[Catálogo - eleFront#Bake Objects (Bake)|Bake Objects]] · [[Catálogo - Params#Context Bake (C-Bake)|Context Bake]] · [[Catálogo - LunchBox#Object Bake (Bake)|Object Bake]]

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (30)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Child Layer | [[Add Child Layer\|Py]] · [[Add Child Layer (cs)\|C#]] | Crea una subcapa dentro de otra capa | `Layer.ParentLayerId → doc.Layers.Add(capa)` |
| Add Layer | [[Add Layer\|Py]] · [[Add Layer (cs)\|C#]] | Crea una capa validando el nombre | `Layer.IsValidName, doc.Layers.Find, doc.Layers.Add` |
| Add Material | [[Add Material\|Py]] · [[Add Material (cs)\|C#]] | Crea un material y lo asigna a una esfera | `Material → RenderMaterial.CreateBasicMaterial → doc.RenderMaterials.Add` |
| Add Nested Block | [[Add Nested Block (cs)\|C#]] | Crea un bloque que contiene otro bloque | `doc.InstanceDefinitions.Add, InstanceReferenceGeometry` |
| Add Objects to Group | [[Add Objects to Group\|Py]] · [[Add Objects to Group (cs)\|C#]] | Agrupa los objetos seleccionados | `doc.Groups.Add(ids)` |
| Block Insertion Point | [[Block Insertion Point\|Py]] · [[Block Insertion Point (cs)\|C#]] | Muestra el punto de inserción de un bloque | `InstanceObject.InsertionPoint` |
| Copy Groups | [[Copy Groups\|Py]] · [[Copy Groups (cs)\|C#]] | Duplica objetos manteniendo sus grupos | `Attributes.GetGroupList, doc.Groups.Add` |
| Create Block Definition | [[Create Block Definition\|Py]] · [[Create Block Definition (cs)\|C#]] | Crea un bloque desde los objetos seleccionados | `doc.InstanceDefinitions.Add(nombre, desc, base, geometrias, atributos)` |
| Custom Undo | [[Custom Undo\|Py]] · [[Custom Undo (cs)\|C#]] | Registra acciones propias en Deshacer y Rehacer | `doc.AddCustomUndoEvent(nombre, funcion, dato)` |
| Delete Block Instance Definition | [[Delete Block Instance Definition\|Py]] · [[Delete Block Instance Definition (cs)\|C#]] | Borra una definición de bloque por nombre | `doc.InstanceDefinitions.Find → Delete` |
| Determine Object Layer | [[Determine Object Layer\|Py]] · [[Determine Object Layer (cs)\|C#]] | Capa de un objeto seleccionado | `Attributes.LayerIndex → doc.Layers[i].Name` |
| Display Precision | [[Display Precision\|Py]] · [[Display Precision (cs)\|C#]] | Cambia cuántos decimales muestra Rhino en las distancias | `doc.ModelDistanceDisplayPrecision` |
| Duplicate Object | [[Duplicate Object\|Py]] · [[Duplicate Object (cs)\|C#]] | Copia un objeto del documento | `RhinoObject.DuplicateGeometry → doc.Objects.Add` |
| Find Objects by Name | [[Find Objects by Name\|Py]] · [[Find Objects by Name (cs)\|C#]] | Busca objetos por su nombre | `ObjectEnumeratorSettings.NameFilter → doc.Objects.GetObjectList` |
| Get Object UUID | [[Get Object UUID\|Py]] · [[Get Object UUID (cs)\|C#]] | Lee el identificador único (Guid) de un objeto | `rs.GetObject → Guid (RhinoObject.Id)` |
| Instance Archive File Status | [[Instance Archive File Status (cs)\|C#]] | Estado de los bloques vinculados a archivos externos | `InstanceDefinition.ArchiveFileStatus` |
| Instance Definition Names | [[Instance Definition Names\|Py]] · [[Instance Definition Names (cs)\|C#]] | Lista los nombres de los bloques | `doc.InstanceDefinitions` |
| Instance Definition Objects | [[Instance Definition Objects\|Py]] · [[Instance Definition Objects (cs)\|C#]] | Lista los objetos que forman un bloque | `InstanceDefinition.GetObjects()` |
| Instance Definition Tree | [[Instance Definition Tree\|Py]] · [[Instance Definition Tree (cs)\|C#]] | Árbol de bloques anidados | `InstanceDefinition.Object(i), TextLog` |
| Lock Layer | [[Lock Layer\|Py]] · [[Lock Layer (cs)\|C#]] | Bloquea una capa por nombre | `Layer.IsLocked = True → CommitChanges` |
| Modify Object Color | [[Modify Object Color\|Py]] · [[Modify Object Color (cs)\|C#]] | Cambia el color de un objeto | `Attributes.ObjectColor + ColorSource.ColorFromObject` |
| Move Objects to Current Layer | [[Move Objects to Current Layer\|Py]] · [[Move Objects to Current Layer (cs)\|C#]] | Pasa los objetos seleccionados a la capa actual | `Attributes.LayerIndex = doc.Layers.CurrentLayerIndex` |
| Object Color | [[Object Color (cs)\|C#]] | Cambia el color de varios objetos con el diálogo de color | `Dialogs.ShowColorDialog, Attributes.ColorSource` |
| Object Iterator | [[Object Iterator\|Py]] · [[Object Iterator (cs)\|C#]] | Recorre todos los objetos del documento | `ObjectEnumeratorSettings → doc.Objects.GetObjectList` |
| Rename Block | [[Rename Block\|Py]] · [[Rename Block (cs)\|C#]] | Renombra un bloque | `doc.InstanceDefinitions.Find → Modify (rs.RenameBlock)` |
| Rename Layer | [[Rename Layer\|Py]] · [[Rename Layer (cs)\|C#]] | Renombra una capa | `Layer.Name → CommitChanges` |
| Rename Object | [[Rename Object\|Py]] · [[Rename Object (cs)\|C#]] | Cambia el nombre de un objeto | `rs.ObjectName(id, nombre) → Attributes.Name` |
| Select Objects in Object Groups | [[Select Objects in Object Groups\|Py]] · [[Select Objects in Object Groups (cs)\|C#]] | Selecciona todo el grupo de un objeto | `Attributes.GetGroupList → Select(True)` |
| Select Objects on Layer | [[Select Objects on Layer\|Py]] · [[Select Objects on Layer (cs)\|C#]] | Selecciona los objetos de una capa | `doc.Objects.FindByLayer(nombre)` |
| User Data | [[User Data (cs)\|C#]] | Guarda datos propios dentro de un objeto (viajan en el .3dm) | `clase UserData con Read / Write (ArchivableDictionary)` |

## Componentes de Grasshopper (180)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (7)

- [[Catálogo - Params#Block Instance (parámetro)|Block Instance (parámetro)]] — Contiene una colección de instancias de bloque
- [[Catálogo - Params#Geometry (Geo, parámetro)|Geometry (Geo, parámetro)]] — Contiene una colección de geometría genérica
- [[Catálogo - Params#Geometry Cache (parámetro)|Geometry Cache (parámetro)]] — Empuja geometría hacia el documento de Rhino o la trae desde él
- [[Catálogo - Params#Geometry Pipeline (Pipeline, parámetro)|Geometry Pipeline (Pipeline, parámetro)]] — Define un pipeline de geometría de Rhino a Grasshopper
- [[Catálogo - Params#Group (Grp, parámetro)|Group (Grp, parámetro)]] — Contiene una colección de grupos geométricos
- [[Catálogo - Params#Light (parámetro)|Light (parámetro)]] — Contiene una colección de luces
- [[Catálogo - Params#View (parámetro)|View (parámetro)]] — Contiene una colección de marcos de vista

### Params › Primitive (1)

- [[Catálogo - Params#Earth Anchor Point (Anchor, parámetro)|Earth Anchor Point (Anchor, parámetro)]] — Contiene un punto de anclaje terrestre que asocia un punto y una orientación del modelo con una latitud…

### Params › Rhino (13)

- [[Catálogo - Params#Display Mode (parámetro)|Display Mode (parámetro)]] — Contiene una colección de modos de visualización
- [[Catálogo - Params#Layout Viewport (Layout, parámetro)|Layout Viewport (Layout, parámetro)]] — Contiene una colección de diseños de página (layouts) de Rhino
- [[Catálogo - Params#Model Annotation Style (Style, parámetro)|Model Annotation Style (Style, parámetro)]] — Contiene una colección de estilos de anotación del modelo
- [[Catálogo - Params#Model Attribute Key (Key, parámetro)|Model Attribute Key (Key, parámetro)]] — Contiene una colección de claves de atributos
- [[Catálogo - Params#Model Block Definition (Block Definition, parámetro)|Model Block Definition (Block Definition, parámetro)]] — Contiene una colección de definiciones de bloque del modelo
- [[Catálogo - Params#Model Environment (Environment, parámetro)|Model Environment (Environment, parámetro)]] — Contiene una colección de entornos del modelo
- [[Catálogo - Params#Model Hatch Pattern (Hatch Pattern, parámetro)|Model Hatch Pattern (Hatch Pattern, parámetro)]] — Contiene una colección de patrones de sombreado del modelo
- [[Catálogo - Params#Model Layer (Layer, parámetro)|Model Layer (Layer, parámetro)]] — Contiene una colección de capas del modelo
- [[Catálogo - Params#Model Linetype (Linetype, parámetro)|Model Linetype (Linetype, parámetro)]] — Contiene una colección de tipos de línea del modelo
- [[Catálogo - Params#Model Material (Material, parámetro)|Model Material (Material, parámetro)]] — Contiene una colección de materiales del modelo
- [[Catálogo - Params#Model Object (Object, parámetro)|Model Object (Object, parámetro)]] — Contiene una colección de objetos del modelo
- [[Catálogo - Params#Model Print Width (Print Width, parámetro)|Model Print Width (Print Width, parámetro)]] — Contiene una colección de grosores de impresión del modelo
- [[Catálogo - Params#Model Viewport (Viewport, parámetro)|Model Viewport (Viewport, parámetro)]] — Contiene una colección de vistas de Rhino

### Rhino › Content (24)

- [[Catálogo - Rhino#Contains Text Filter (Contains)|Contains Text Filter (Contains)]] — Crea un filtro que determina si un texto aparece dentro de otro texto
- [[Catálogo - Rhino#Content Cache (Cache)|Content Cache (Cache)]] — Empuja contenido hacia un modelo de Rhino o lo trae desde él
- [[Catálogo - Rhino#Content Identity (Identity)|Content Identity (Identity)]] — Obtiene algunos detalles sobre la identidad del contenido del modelo
- [[Catálogo - Rhino#Content Information (Information)|Content Information (Information)]] — Obtiene o define información de los elementos de contenido de Rhino
- [[Catálogo - Rhino#Convert Units (C-Units)|Convert Units (C-Units)]] — Realiza una conversión de unidades sobre los datos de entrada
- [[Catálogo - Rhino#Duplicate Content (C-Duplicate)|Duplicate Content (C-Duplicate)]] — Duplica el contenido de entrada con una nueva identidad. Borra el Id del contenido actual y opcionalmente…
- [[Catálogo - Rhino#Equality Filter (Equals)|Equality Filter (Equals)]] — Crea un filtro que determina si un valor es igual a otro
- [[Catálogo - Rhino#Evaluate Text Fields (Evaluate)|Evaluate Text Fields (Evaluate)]] — Evalúa las expresiones de campos de un texto
- [[Catálogo - Rhino#Filter Content (Filter)|Filter Content (Filter)]] — Separa contenido según una condición de filtro
- [[Catálogo - Rhino#Greater Than Filter (Greater)|Greater Than Filter (Greater)]] — Crea un filtro que determina si un valor es mayor que otro
- [[Catálogo - Rhino#Group Content (Group)|Group Content (Group)]] — Agrupa contenido por clave
- [[Catálogo - Rhino#Import Content (Import)|Import Content (Import)]] — Importa un modelo desde un archivo
- [[Catálogo - Rhino#Intersection Filter (Intersection)|Intersection Filter (Intersection)]] — Combina varios filtros en una intersección, que devuelve True solo si todos los filtros de entrada se cumplen
- [[Catálogo - Rhino#Less Than Filter (Less)|Less Than Filter (Less)]] — Crea un filtro que determina si un valor es menor que otro
- [[Catálogo - Rhino#Logical And Filter (And)|Logical And Filter (And)]] — Combina dos filtros con un operador lógico AND
- [[Catálogo - Rhino#Logical Not Filter (Not)|Logical Not Filter (Not)]] — Crea un filtro como el NOT lógico de otro
- [[Catálogo - Rhino#Logical Or Filter (Or)|Logical Or Filter (Or)]] — Combina dos filtros con un operador lógico OR
- [[Catálogo - Rhino#Match Text Filter (Match)|Match Text Filter (Match)]] — Crea un filtro que determina si un valor de texto coincide con un patrón
- [[Catálogo - Rhino#Order Content (Order)|Order Content (Order)]] — Ordena contenido por clave
- [[Catálogo - Rhino#Query Directory (Directory)|Query Directory (Directory)]] — Consulta el sistema de archivos bajo la ruta de carpeta indicada
- [[Catálogo - Rhino#Text Field Expression (Field Expression)|Text Field Expression (Field Expression)]] — Construye una expresión de campo que se puede usar como campo de texto en anotaciones o como valor de texto…
- [[Catálogo - Rhino#Union Filter (Union)|Union Filter (Union)]] — Combina varios filtros en una unión, que devuelve True si al menos un filtro de entrada se cumple
- [[Catálogo - Rhino#Unit System (U-System)|Unit System (U-System)]] — Sistema de unidades
- [[Catálogo - Rhino#User Text (U-Text)|User Text (U-Text)]] — Modifica la colección de textos clave/valor de un elemento del modelo

### Rhino › Model (11)

- [[Catálogo - Rhino#Explode Object (Explode)|Explode Object (Explode)]] — Explota un objeto
- [[Catálogo - Rhino#Export Model Block Definition (E-Block)|Export Model Block Definition (E-Block)]] — Exporta una definición de bloque como archivo
- [[Catálogo - Rhino#Hide Model Layer (L-Hide)|Hide Model Layer (L-Hide)]] — Define la visibilidad de capas para las vistas del modelo y los detalles nuevos
- [[Catálogo - Rhino#Import Model Block Definition (I-Block)|Import Model Block Definition (I-Block)]] — Importa un archivo y crea una nueva definición de bloque
- [[Catálogo - Rhino#Model Block Definition (Block Definition)|Model Block Definition (Block Definition)]] — Definición de bloque
- [[Catálogo - Rhino#Model Block Instance (Block Instance)|Model Block Instance (Block Instance)]] — Instancia de bloque
- [[Catálogo - Rhino#Model Earth Location (Earth Location)|Model Earth Location (Earth Location)]] — Asocia una ubicación y orientación del modelo con valores de latitud, longitud y elevación en la Tierra
- [[Catálogo - Rhino#Model Layer (Layer)|Model Layer (Layer)]] — Capa del modelo
- [[Catálogo - Rhino#Query Model Block Definitions (Block Definitions)|Query Model Block Definitions (Block Definitions)]] — Consulta un documento de Rhino para obtener todas las definiciones de bloque disponibles
- [[Catálogo - Rhino#Query Model Layers (Layers)|Query Model Layers (Layers)]] — Consulta un documento de Rhino para obtener todas las capas disponibles
- [[Catálogo - Rhino#Query Model Location (Model Location)|Query Model Location (Model Location)]] — Consulta un documento de Rhino para obtener su ubicación terrestre

### Rhino › Objects (11)

- [[Catálogo - Rhino#Display Attributes (Display)|Display Attributes (Display)]] — Atributos de visualización del objeto
- [[Catálogo - Rhino#Display Colour|Display Colour]] — Atributos de color de visualización del objeto
- [[Catálogo - Rhino#Drafting Attributes (Drafting)|Drafting Attributes (Drafting)]] — Atributos de dibujo del objeto
- [[Catálogo - Rhino#Model Object (Object)|Model Object (Object)]] — Objeto del modelo
- [[Catálogo - Rhino#Object Linetype|Object Linetype]] — Atributos de tipo de línea del objeto
- [[Catálogo - Rhino#Print Colour|Print Colour]] — Atributos de color de impresión del objeto
- [[Catálogo - Rhino#Print Width|Print Width]] — Atributos de grosor de impresión del objeto
- [[Catálogo - Rhino#Query Model Objects (M-Objects)|Query Model Objects (M-Objects)]] — Consulta un documento de Rhino para obtener todos los objetos del modelo disponibles
- [[Catálogo - Rhino#Render Attributes (Render)|Render Attributes (Render)]] — Atributos de render del objeto
- [[Catálogo - Rhino#Render Material (Object Material)|Render Material (Object Material)]] — Atributos de material de render del objeto
- [[Catálogo - Rhino#Visibility Attributes (Visibility)|Visibility Attributes (Visibility)]] — Atributos de visibilidad del objeto

### eleFront › 01 Reference (11)

- [[Catálogo - eleFront#Deconstruct Ghost (DeGho)|Deconstruct Ghost (DeGho)]] — Separa el Guid y los atributos de la geometría fantasma (Ghost Geometry)
- [[Catálogo - eleFront#Interact with Rhino Object (IntObj)|Interact with Rhino Object (IntObj)]] — Interactúa con objetos del documento de Rhino
- [[Catálogo - eleFront#Manifest Ghost Geometry (Man)|Manifest Ghost Geometry (Man)]] — Importa la geometría real de un objeto fantasma
- [[Catálogo - eleFront#Reference Block by Name (RefBlock)|Reference Block by Name (RefBlock)]] — Referencia instancias de bloque por nombre de bloque
- [[Catálogo - eleFront#Reference by BakeName (RefBake)|Reference by BakeName (RefBake)]] — Referencia objetos según el nombre de bake y los atributos de usuario
- [[Catálogo - eleFront#Reference by Key/Value (RefKV)|Reference by Key/Value (RefKV)]] — Referencia objetos según pares clave/valor
- [[Catálogo - eleFront#Reference by Layer (RefLay)|Reference by Layer (RefLay)]] — Referencia objetos de Rhino por capa
- [[Catálogo - eleFront#Reference by Name (RefName)|Reference by Name (RefName)]] — Referencia objetos de Rhino por nombre
- [[Catálogo - eleFront#Reference by Type (refType)|Reference by Type (refType)]] — Referencia objetos de Rhino por tipo
- [[Catálogo - eleFront#Update All Reference Components (Update Refs - All, parámetro)|Update All Reference Components (Update Refs - All, parámetro)]] — Actualiza todos los componentes de referencia de eleFront con este botón
- [[Catálogo - eleFront#Update Group (parámetro)|Update Group (parámetro)]] — Activa todos los componentes de eleFront que comparten el grupo de este botón

### eleFront › 02 Filter (5)

- [[Catálogo - eleFront#Filter By Layer (FilterLay)|Filter By Layer (FilterLay)]] — Filtra objetos según su capa
- [[Catálogo - eleFront#Filter By Name (FilterName)|Filter By Name (FilterName)]] — Filtra objetos según su nombre
- [[Catálogo - eleFront#Filter by Type (FilterType)|Filter by Type (FilterType)]] — Filtra objetos según su tipo de objeto
- [[Catálogo - eleFront#Filter by User Attributes (FilterAtt)|Filter by User Attributes (FilterAtt)]] — Filtra objetos según sus atributos de usuario. También permite filtrado en paralelo opcional
- [[Catálogo - eleFront#Sort By Key (SortKey)|Sort By Key (SortKey)]] — Injerta (graft) un árbol según las claves de texto de usuario. Crea una rama nueva por cada clave única

### eleFront › 03 Attributes (14)

- [[Catálogo - eleFront#Attach Attributes (AttAtt)|Attach Attributes (AttAtt)]] — Adjunta atributos a la geometría, creando un objeto completo con atributos
- [[Catálogo - eleFront#AttributesFromJSON (AttFromJSON)|AttributesFromJSON (AttFromJSON)]] — Deserializa un objeto JSON a atributos de eleFront
- [[Catálogo - eleFront#AttributesToJSON (AttToJSON)|AttributesToJSON (AttToJSON)]] — Serializa EleFrontAttributes a formato JSON
- [[Catálogo - eleFront#Define Color (Color)|Define Color (Color)]] — Define el color
- [[Catálogo - eleFront#Detach Attributes (DetAtt)|Detach Attributes (DetAtt)]] — Separa un objeto en su geometría y sus atributos de eleFront
- [[Catálogo - eleFront#EleFront Attributes (EF Att)|EleFront Attributes (EF Att)]] — Crea, modifica o descompone atributos
- [[Catálogo - eleFront#EleFront Layer (EF Layer)|EleFront Layer (EF Layer)]] — Crea, modifica o descompone una capa. Se puede asignar a los atributos de un objeto o hacer bake con "Bake…
- [[Catálogo - eleFront#Get All Keys/Values (GetKV)|Get All Keys/Values (GetKV)]] — Obtiene todas las claves, valores y el nombre de bake de los atributos
- [[Catálogo - eleFront#Get Rhino Attributes (RhAtt)|Get Rhino Attributes (RhAtt)]] — Obtiene los atributos de Rhino de un objeto
- [[Catálogo - eleFront#Get User Value (GetUV)|Get User Value (GetUV)]] — Devuelve el valor de atributo de usuario que corresponde a una clave. Funciona con geometría referenciada o…
- [[Catálogo - eleFront#Inherit Attributes by Key (Inherit)|Inherit Attributes by Key (Inherit)]] — Hereda atributos indicando la clave
- [[Catálogo - eleFront#Modify Rhino Object Attributes (ModRAtt)|Modify Rhino Object Attributes (ModRAtt)]] — Modifica los atributos de un objeto de Rhino
- [[Catálogo - eleFront#Remove User Text (RemUT)|Remove User Text (RemUT)]] — Quita claves y valores de usuario de objetos del documento de Rhino
- [[Catálogo - eleFront#Set User String (Set US)|Set User String (Set US)]] — Define pares clave/valor de texto de usuario en un objeto

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

### eleFront › 05 Blocks (8)

- [[Catálogo - eleFront#Define Embedded Block (DefEmbed)|Define Embedded Block (DefEmbed)]] — Define un bloque incrustado
- [[Catálogo - eleFront#Define Linked Block (DefLnkBlock)|Define Linked Block (DefLnkBlock)]] — Crea una definición de bloque vinculada. La definición se puede instanciar como bloque
- [[Catálogo - eleFront#Explode Block (ExpBlock)|Explode Block (ExpBlock)]] — Explota un bloque para obtener su geometría
- [[Catálogo - eleFront#Get Block Info (Block Info)|Get Block Info (Block Info)]] — Devuelve información de una instancia de bloque
- [[Catálogo - eleFront#Insert Block (Insert)|Insert Block (Insert)]] — Inserta un bloque del documento activo
- [[Catálogo - eleFront#List Blocks In Document (ListBlockD)|List Blocks In Document (ListBlockD)]] — Lista todos los nombres de bloques del documento de Rhino
- [[Catálogo - eleFront#Push Block Definitions (PushBlk)|Push Block Definitions (PushBlk)]] — Envía definiciones de bloque al documento de Rhino
- [[Catálogo - eleFront#Reload Linked Block Definitions (ReloadBlk)|Reload Linked Block Definitions (ReloadBlk)]] — Recarga desde el disco las definiciones de bloques vinculados. Los objetos que no son bloques y los bloques…

### eleFront › 06 Bake (6)

- [[Catálogo - eleFront#Bake All eleFront (Bake All, parámetro)|Bake All eleFront (Bake All, parámetro)]] — Hace bake de todos los objetos de eleFront con este botón
- [[Catálogo - eleFront#Bake Group (parámetro)|Bake Group (parámetro)]] — Activa todos los componentes de bake que comparten el grupo de este botón
- [[Catálogo - eleFront#Bake Layers (BkLay)|Bake Layers (BkLay)]] — Hace bake de capas en Rhino
- [[Catálogo - eleFront#Bake Objects (Bake)|Bake Objects (Bake)]] — Hace bake de objetos en Rhino con atributos de Rhino y atributos de usuario
- [[Catálogo - eleFront#Bake Objects To File (BakeToFile)|Bake Objects To File (BakeToFile)]] — Hace bake de objetos en un archivo de Rhino externo, con atributos de Rhino y atributos de usuario
- [[Catálogo - eleFront#Bake Settings (BkSettings)|Bake Settings (BkSettings)]] — Selecciona ajustes de bake predefinidos, con opciones para reemplazarlos por ajustes personalizados

### eleFront › 08 Params (2)

- [[Catálogo - eleFront#eleFront Data Description (Description, parámetro)|eleFront Data Description (Description, parámetro)]] — Usa este componente para guiar tus flujos de datos en el lienzo de forma ordenada. Usa una descripción con…
- [[Catálogo - eleFront#Extended Geometry (ExtGeo, parámetro)|Extended Geometry (ExtGeo, parámetro)]] — Parámetro para todos los tipos de geometría, incluidos los que no son nativos de Grasshopper

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

### Human › Creation (7)

- [[Catálogo - Human#Bake Geometry (Bake)|Bake Geometry (Bake)]] — Hace bake de la geometría en el documento con los atributos indicados
- [[Catálogo - Human#CreateAttributes (CreateAtts)|CreateAttributes (CreateAtts)]] — Crea atributos de objeto
- [[Catálogo - Human#CreateHatch|CreateHatch]] — Crea objetos de sombreado (hatch) con el patrón, la escala, la rotación y los atributos indicados
- [[Catálogo - Human#CreateLight|CreateLight]] — Crea un objeto luz. Por ahora funciona bien con luces puntuales y direccionales
- [[Catálogo - Human#Define Block (DefBlock)|Define Block (DefBlock)]] — Este componente permite definir o reemplazar una definición de bloque
- [[Catálogo - Human#JustifiedText3d (Justified Text)|JustifiedText3d (Justified Text)]] — Crea objetos de texto 3D con el tamaño, la ubicación, la alineación y la fuente indicados
- [[Catálogo - Human#PlaceBlock|PlaceBlock]] — Coloca un bloque indicado con la transformación deseada

### Human › Document Info (7)

- [[Catálogo - Human#Font Table (Fonts)|Font Table (Fonts)]] — Obtiene la lista de fuentes del sistema
- [[Catálogo - Human#Hatch Table (HatchTable)|Hatch Table (HatchTable)]] — Obtiene los sombreados del documento activo de Rhino
- [[Catálogo - Human#Layer Table (LayerTable)|Layer Table (LayerTable)]] — Obtiene la lista de capas del documento activo
- [[Catálogo - Human#Linetype Table (LT Table)|Linetype Table (LT Table)]] — Obtiene los tipos de línea del documento activo de Rhino
- [[Catálogo - Human#Material Table (MatTable)|Material Table (MatTable)]] — Accede a los materiales de render del documento
- [[Catálogo - Human#Named Views and Display Modes (ViewsAndModes)|Named Views and Display Modes (ViewsAndModes)]] — Obtiene una lista de las vistas guardadas y los modos de visualización de este documento
- [[Catálogo - Human#Viewport Properties (Viewports)|Viewport Properties (Viewports)]] — Obtiene una lista de las vistas y sus propiedades

### Human › Document Modifications (4)

- [[Catálogo - Human#Create/Modify Layers (Layers)|Create/Modify Layers (Layers)]] — Crea y modifica capas de Rhino
- [[Catálogo - Human#Create/Modify Materials (Materials)|Create/Modify Materials (Materials)]] — Crea o edita materiales de render del documento. Ojo: el componente solo puede modificar materiales que él…
- [[Catálogo - Human#Modify Object Attributes (ModAtts)|Modify Object Attributes (ModAtts)]] — Usa este componente para modificar los atributos de objeto de geometría en Rhino
- [[Catálogo - Human#Modify Viewport (Mod Viewport)|Modify Viewport (Mod Viewport)]] — Usa este componente para restaurar una vista guardada en una vista, definir su modo de visualización o su…

### Human › Misc (9)

- [[Catálogo - Human#Clickable Mesh (ClickM)|Clickable Mesh (ClickM)]] — Permite hacer clic en la vista de Rhino para seleccionar de una lista de mallas. ¡ADVERTENCIA! Captura TODOS…
- [[Catálogo - Human#Convert To Document Units (DocUnits)|Convert To Document Units (DocUnits)]] — Interpreta un texto de distancia con formato (como 5'-10") y lo convierte a número en las unidades del…
- [[Catálogo - Human#DeleteOnLayer (DelOnLay)|DeleteOnLayer (DelOnLay)]] — Elimina todos los objetos de las capas indicadas y luego entrega True. Sirve para simular que se cambia un…
- [[Catálogo - Human#Directory Contents (Dir)|Directory Contents (Dir)]] — Lista los archivos de una carpeta indicada
- [[Catálogo - Human#Dispatch Multiple (MDispatch)|Dispatch Multiple (MDispatch)]] — Reparte (dispatch) varias listas a la vez. Solo obtiene los valores True; usa invertir para obtener los otros
- [[Catálogo - Human#Filter By Item (IFilter)|Filter By Item (IFilter)]] — Filtra una o varias listas según una lista guía y un subconjunto de esa lista guía
- [[Catálogo - Human#Item Selector (List, parámetro)|Item Selector (List, parámetro)]] — Permite seleccionar uno o varios elementos de una lista de entrada
- [[Catálogo - Human#Read 3dm File (3dm)|Read 3dm File (3dm)]] — Lee objetos de un archivo .3dm externo
- [[Catálogo - Human#Save Viewport To File (SaveView)|Save Viewport To File (SaveView)]] — Guarda una captura o un render de una vista en la ruta indicada

### Human › Reference (10)

- [[Catálogo - Human#Dynamic Geometry Pipeline (DPipeline)|Dynamic Geometry Pipeline (DPipeline)]] — Define un pipeline de geometría de Rhino a Grasshopper, con filtros variables por nombre, tipo de objeto y…
- [[Catálogo - Human#Explode Blocks (BlockExplode)|Explode Blocks (BlockExplode)]] — Explota un conjunto de objetos de instancia (bloques) en su geometría
- [[Catálogo - Human#Explode Blocks Recursively (BlockExplode R)|Explode Blocks Recursively (BlockExplode R)]] — Explota de forma recursiva un conjunto de objetos de instancia (bloques) en su geometría, estructurada en un…
- [[Catálogo - Human#Hatch Explode (HatchExp)|Hatch Explode (HatchExp)]] — Obtiene la geometría y las propiedades de un objeto sombreado (hatch) referenciado
- [[Catálogo - Human#LightProperties (LightProps)|LightProperties (LightProps)]] — Lee las propiedades de una luz desde un Rhino.DocObjects.LightObject
- [[Catálogo - Human#Object Attributes (ObjAtts)|Object Attributes (ObjAtts)]] — Accede a los atributos individuales de un RhinoObject o de un tipo ObjectAttributes
- [[Catálogo - Human#Objects By Selection (SelObj)|Objects By Selection (SelObj)]] — Obtiene los objetos seleccionados actualmente en Rhino
- [[Catálogo - Human#Reinstate Tree (ReTree)|Reinstate Tree (ReTree)]] — Este componente recupera la estructura de árbol de datos de geometría referenciada a la que se hizo bake con…
- [[Catálogo - Human#Sort Objects By Type (SortByType)|Sort Objects By Type (SortByType)]] — Ordena un conjunto de objetos de Rhino por tipo y extrae la geometría de los tipos que ya existen en…
- [[Catálogo - Human#Text Object Info (TxtObjInfo)|Text Object Info (TxtObjInfo)]] — Obtiene la ubicación, el plano de orientación, la alineación y el texto de un objeto texto referenciado

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

<!-- AUTO:fin -->
