---
title: "Catálogo Grasshopper — eleFront"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "eleFront"
libraries: ["eleFront 5.4.1"]
components: 74
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/elefront, rhino/documento, rhino/vista, datos/arboles, programacion/scripts]
---

# eleFront

74 objetos · librería: eleFront 5.4.1 · autor: eleFront

Mapas: [[Mapa - Documento de Rhino]] (65) · [[Mapa - Visualización y anotaciones]] (10) · [[Mapa - Data trees y listas]] (9) · [[Mapa - Scripts, interfaz y archivos]] (9)

## 01 Reference

### Deconstruct Ghost (DeGho)

Separa el Guid y los atributos de la geometría fantasma (Ghost Geometry)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ghost Geometry | `G` | Geometry | item | Objetos de geometría fantasma de eleFront a restituir como geometría. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guids | `G` | Text | item | El Guid de la geometría original. |
| Source File | `F` | Text | item | Ruta del archivo que contiene el objeto original. |
| Attributes | `A` | Generic Data | item | Atributos del objeto. |

### Interact with Rhino Object (IntObj)

Interactúa con objetos del documento de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object Guid | `ID` | Guid | árbol | Guid de los objetos |
| Activate *(opcional)* | `A` | Boolean | item | Activar el componente |

### Manifest Ghost Geometry (Man)

Importa la geometría real de un objeto fantasma.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ghost Geometry | `G` | Geometry | item | Objetos de geometría fantasma de eleFront a restituir como geometría. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Objeto(s) referenciado(s) |

### Reference Block by Name (RefBlock)

Referencia instancias de bloque por nombre de bloque

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Name | `[]BN` | Text | item | Nombres de los bloques a referenciar. Conecta una Value List para cargar los nombres de los bloques del documento activo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Instances | `B` | Generic Data | lista | Bloque(s) referenciado(s) |

### Reference by BakeName (RefBake)

Referencia objetos según el nombre de bake y los atributos de usuario

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| BakeName | `[]N` | Text | item | Nombre con el que se hizo bake de los objetos. Conecta una ValueList para ver los nombres de bake posibles. |
| Key | `[]K` | Text | lista | Clave a buscar en los objetos referenciados. |
| Val | `[]V` | Text | lista | Valor a buscar en los objetos referenciados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | lista | Objeto(s) referenciado(s) |

### Reference by Key/Value (RefKV)

Referencia objetos según pares clave/valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Key | `[]K` | Text | lista | Clave a buscar en los objetos referenciados. |
| Val | `[]V` | Text | lista | Valor a buscar en los objetos referenciados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | lista | Objeto(s) referenciado(s) |

### Reference by Layer (RefLay)

Referencia objetos de Rhino por capa.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer name | `[]L` | Text | item | Nombre de la capa de la que referenciar objetos. Conecta una ValueList para ver las capas activas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | lista | Objeto(s) referenciado(s) |

### Reference by Name (RefName)

Referencia objetos de Rhino por nombre.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object Name | `N` | Text | item | Nombres de los objetos a referenciar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | lista | Objeto(s) referenciado(s) |

### Reference by Type (refType)

Referencia objetos de Rhino por tipo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object Type | `[]T` | Text | item | Tipo de objeto a referenciar. Conecta una ValueList para ver los filtros de tipo disponibles. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | lista | Objeto(s) referenciado(s) |

### Update All Reference Components (Update Refs - All, parámetro)

Actualiza todos los componentes de referencia de eleFront con este botón

Tipo de dato: **Boolean**

### Update Group (parámetro)

Activa todos los componentes de eleFront que comparten el grupo de este botón

Tipo de dato: **Boolean**

## 02 Filter

### Filter By Layer (FilterLay)

Filtra objetos según su capa

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer | `[]L` | Text | item | Capa a buscar en los objetos referenciados. Conecta una ValueList para ver las capas activas. |
| Geometry | `G` | Extended Geometry | lista | Geometría a filtrar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Excluded Geometry | `Ex` | Generic Data | lista | Objetos que no cumplieron el criterio del filtro. |
| Included Geometry | `G` | Generic Data | lista | Objetos que cumplen el criterio del filtro |

### Filter By Name (FilterName)

Filtra objetos según su nombre

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `[]N` | Text | item | Nombre a buscar en los objetos referenciados |
| Geometry | `G` | Extended Geometry | lista | Geometría a filtrar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Excluded Geometry | `Ex` | Generic Data | lista | Objetos que no cumplieron el criterio del filtro. |
| Included Geometry | `G` | Generic Data | lista | Objetos que cumplen el criterio del filtro |

### Filter by Type (FilterType)

Filtra objetos según su tipo de objeto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object Type | `[]T` | Text | item | Tipo de objeto a buscar. Conecta una ValueList para ver los tipos posibles. |
| Geometry | `G` | Extended Geometry | lista | Geometría a filtrar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Excluded Geometry | `Ex` | Generic Data | lista | Objetos que no cumplieron el criterio del filtro. |
| Included Geometry | `G` | Generic Data | lista | Objetos que cumplen el criterio del filtro |

### Filter by User Attributes (FilterAtt)

Filtra objetos según sus atributos de usuario. También permite filtrado en paralelo opcional.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Key | `[]K` | Text | lista | Clave a buscar en los objetos referenciados. Conecta una ValueList para ver las claves posibles. |
| Val | `[]V` | Text | lista | Valor a buscar en los objetos referenciados. |
| Attributes | `A` | Generic Data | lista | Atributos/geometría referenciada a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | árbol | Objeto(s) filtrado(s) |

### Sort By Key (SortKey)

Injerta (graft) un árbol según las claves de texto de usuario. Crea una rama nueva por cada clave única.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Attributes | `A` | Generic Data | árbol | Atributos/geometría referenciada a evaluar |
| Key 1 | `[]K1` | Text | item | Clave a buscar en los objetos referenciados. Conecta una ValueList para ver las claves posibles. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sorted Objects | `O` | Generic Data | árbol | Objetos ordenados |
| Values | `V1` | Text | árbol | Valores encontrados |

## 03 Attributes

### Attach Attributes (AttAtt)

Adjunta atributos a la geometría, creando un objeto completo con atributos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a la que hacer bake |
| Attributes | `A` | Generic Data | item | Atributos a asignar a la geometría al hacer bake |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Attributed Geometry | `AG` | Generic Data | item | Geometría con los atributos adjuntos |

### AttributesFromJSON (AttFromJSON)

Deserializa un objeto JSON a atributos de eleFront.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| JSON String | `J` | Text | item | Texto del objeto JSON |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| eleFront Attributes | `A` | Generic Data | item | Si funciona, el atributo de eleFront |

### AttributesToJSON (AttToJSON)

Serializa EleFrontAttributes a formato JSON

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría o atributos a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| JSON | `J` | Text | item | Formato JSON |

### Define Color (Color)

Define el color

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color *(opcional)* | `C` | Colour | item | Color de la capa |
| Source *(opcional)* | `[]S` | Text | item | Fuente del color (objeto, capa, padre o material). Conecta una ValueList para ver las fuentes de color. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Color | `C` | Generic Data | item | Color con la información de su fuente |

### Detach Attributes (DetAtt)

Separa un objeto en su geometría y sus atributos de eleFront

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría a separar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría sin atributos |
| Attributes | `A` | Generic Data | item | Atributos de objeto de eleFront |

### EleFront Attributes (EF Att)

Crea, modifica o descompone atributos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Attributes *(opcional)* | `A` | Generic Data | item | Atributos u objeto con atributos |
| Keys *(opcional)* | `K` | Text | lista | Claves de los atributos de usuario |
| Values *(opcional)* | `V` | Text | lista | Valores de los atributos de usuario |
| Name *(opcional)* | `N` | Text | item | Nombre |
| Layer *(opcional)* | `[]L` | Layer | item | Capa |
| Colour Source *(opcional)* | `[]CS` | Text | item | Fuente del color (objeto, capa, padre o material). Conecta una ValueList para ver las fuentes de color. |
| Object Colour *(opcional)* | `Oc` | Colour | item | Color del objeto |
| Material Source *(opcional)* | `[]Ms` | Text | item | Fuente del material (objeto, capa, padre). Conecta una ValueList para ver las fuentes de material. |
| Material Name *(opcional)* | `[]Mn` | Text | item | Nombre del material |
| Linetype *(opcional)* | `[]Lt` | Text | item | Tipo de línea |
| Print Colour *(opcional)* | `Pc` | Colour | item | Color de impresión |
| Print Width *(opcional)* | `Pw` | Number | item | Grosor de impresión |
| Print Colour Source *(opcional)* | `[]Pcs` | Text | item | Fuente del color de impresión (objeto, capa, padre o material). Conecta una ValueList para ver las fuentes de color. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Attributes | `A` | Generic Data | item | Atributos u objeto con atributos |
| Keys | `K` | Text | lista | Claves de los atributos de usuario |
| Values | `V` | Text | lista | Valores de los atributos de usuario |
| Name | `N` | Text | item | Nombre |
| Layer | `L` | Layer | item | Capa |
| Colour Source | `CS` | Text | item | Fuente del color (objeto, capa, padre o material). Conecta una ValueList para ver las fuentes de color. |
| Display Colour | `Dc` | Colour | item | Color de visualización |
| Material Source | `Ms` | Text | item | Fuente del material (objeto, capa, padre). Conecta una ValueList para ver las fuentes de material. |
| Material Name | `Mn` | Text | item | Nombre del material |
| Linetype | `Lt` | Text | item | Tipo de línea |
| Print Colour | `Pc` | Colour | item | Color de impresión |
| Print Width | `Pw` | Number | item | Grosor de impresión |
| Print Colour Source | `Pcs` | Text | item | Fuente del color de impresión (objeto, capa, padre o material). Conecta una ValueList para ver las fuentes de color. |

### EleFront Layer (EF Layer)

Crea, modifica o descompone una capa. Se puede asignar a los atributos de un objeto o hacer bake con "Bake Layer"

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer *(opcional)* | `[]L` | Layer | item | Capa |
| Layer Names *(opcional)* | `Ln` | Text | lista | Nombres de las capas |
| Hidden *(opcional)* | `H` | Boolean | item | Oculta |
| Locked *(opcional)* | `Lk` | Boolean | item | Bloqueada |
| Display Colour *(opcional)* | `Dc` | Colour | item | Color de visualización |
| Material Name *(opcional)* | `[]Mn` | Text | item | Nombre del material |
| Linetype *(opcional)* | `[]Lt` | Text | item | Tipo de línea |
| Print Colour *(opcional)* | `Pc` | Colour | item | Color de impresión |
| Print Width *(opcional)* | `Pw` | Number | item | Grosor de impresión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layer | `L` | Layer | item | Capa |
| Layer Names | `Ln` | Text | lista | Nombres de las capas |
| Hidden | `H` | Boolean | item | Oculta |
| Locked | `Lk` | Boolean | item | Bloqueada |
| Display Colour | `Dc` | Colour | item | Color de visualización |
| Material Name | `Mn` | Text | item | Nombre del material |
| Linetype | `Lt` | Text | item | Tipo de línea |
| Print Colour | `Pc` | Colour | item | Color de impresión |
| Print Width | `Pw` | Number | item | Grosor de impresión |

### Get All Keys/Values (GetKV)

Obtiene todas las claves, valores y el nombre de bake de los atributos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Attributes or Attributed Geometry | `A` | Generic Data | item | Atributos o geometría con atributos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Keys | `K` | Text | lista | Claves |
| Values | `V` | Text | lista | Valores |
| BakeName | `B` | Text | lista | Nombre de bake |

### Get Rhino Attributes (RhAtt)

Obtiene los atributos de Rhino de un objeto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría a la que hacer bake |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `N` | Text | item | Nombre |
| Layer | `L` | Layer | item | Capa |
| Color | `C` | Generic Data | item | Color |
| Material Name | `Mn` | Text | item | Nombre del material asignado |
| Source File | `F` | Text | item | Si es geometría de una worksession, entrega el archivo del que vino el objeto. |

### Get User Value (GetUV)

Devuelve el valor de atributo de usuario que corresponde a una clave. Funciona con geometría referenciada o con atributos de EleFront

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría o atributos a evaluar |
| Key | `[]K` | Text | lista | Clave(s) de las que devolver el valor. Conecta una ValueList para ver las claves posibles. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `V` | Generic Data | item | Valores asociados a las claves |

### Inherit Attributes by Key (Inherit)

Hereda atributos indicando la clave

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Target Object | `T` | Generic Data | item | Objeto al que adjuntar los datos clave/valor |
| Source Object | `S` | Generic Data | item | Objeto con atributos del que se heredan los datos clave/valor |
| Keys *(opcional)* | `[]K` | Text | lista | Claves que pasan del objeto de origen al objeto destino. Admite comodines (* y ?). Por defecto es * (todas las claves). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Updated Attribute Object | `AO` | Generic Data | item | Objeto con atributos con los datos clave/valor heredados |
| Found Keys | `K` | Text | lista | Claves que se copiaron del destino al origen |

### Modify Rhino Object Attributes (ModRAtt)

Modifica los atributos de un objeto de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Referenced Object | `O` | Generic Data | item | Objeto de Rhino a modificar |
| Attributes | `A` | Generic Data | item | Atributos a asignar a la geometría al hacer bake |
| Activate *(opcional)* | `A` | Boolean | item | Activa el cambio en el documento activo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Message | `S` | Text | item | Mensaje de estado |

### Remove User Text (RemUT)

Quita claves y valores de usuario de objetos del documento de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | item | Geometría a la que hacer bake |
| Activate *(opcional)* | `A` | Boolean | item | Activar los componentes |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Success | `S` | Boolean | item | Valor booleano que indica si la operación funcionó |

### Set User String (Set US)

Define pares clave/valor de texto de usuario en un objeto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object | `O` | Generic Data | item | Objeto a modificar (geometría o datos de EleFront) |
| Keys | `K` | Text | lista | Claves de texto de usuario a definir |
| Values | `V` | Text | lista | Valores de texto de usuario a definir. Un valor vacío quita la clave. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object | `O` | Generic Data | item | Objeto con los textos de usuario actualizados |

## 04 Annotations

### Deconstruct Dimension (DeDim)

Descompone un objeto cota

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dimension | `D` | Geometry | item | Objeto cota |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `V` | Number | lista | Valor medido |
| Text | `T` | Text | lista | Texto que reemplaza al medido |
| Plane | `P` | Plane | lista | Plano base del objeto texto |
| Points | `C` | Point | lista | Puntos de control de la cota |
| Style | `S` | Text | lista | Estilo de cota |

### Deconstruct Hatch (DeHatch)

Descompone un sombreado (hatch)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch | `H` | Geometry | item | Objeto sombreado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch Geometry | `C` | Geometry | lista | Geometría del sombreado explotada |
| Boundary | `B` | Curve | lista | Borde del sombreado |
| Name | `N` | Text | lista | Nombre del patrón de sombreado |
| Scale | `S` | Number | lista | Escala del sombreado |
| Rotation | `R` | Number | lista | Rotación del patrón |

### Deconstruct Text (DeText)

Descompone un objeto texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Object | `T` | Generic Data | item | Objeto texto a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto |
| Plane | `P` | Plane | item | Plano base del objeto texto |
| Height | `H` | Number | item | Altura del texto |
| Justification | `J` | Generic Data | item | Justificación del texto |

### Define Angular Dimension (AngularDim)

Define un objeto cota angular

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Origin | `PO` | Point | item | Centro de la cota angular |
| Point 1 | `P1` | Point | item | Primer punto de la cota |
| Point 2 | `P2` | Point | item | Segundo punto de la cota |
| Offset *(opcional)* | `O` | Number | item | Desfase de la cota respecto del origen del plano |
| Flip *(opcional)* | `F` | Boolean | item | Invierte la cota para que muestre el ángulo mayor |
| Dimension style *(opcional)* | `[]DS` | Text | item | Estilo de cota. Si no se entrega, se usa el estilo activo. |
| Overwrite Text *(opcional)* | `T` | Text | item | Reemplaza el texto de la cota |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angular Dimension | `AD` | Generic Data | item | Cota angular |

### Define Hatch (Hatch)

Define un objeto sombreado para enviarlo al componente de bake de eleFront

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curva plana que representa el borde del sombreado |
| Pattern *(opcional)* | `[]P` | Text | item | Nombre del patrón de sombreado. Conecta una ValueList para ver los patrones activos. |
| Rotation *(opcional)* | `R` | Number | item | Rotación del patrón en grados |
| Scale *(opcional)* | `S` | Number | item | Escala del patrón |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hatch | `H` | Generic Data | item | Objeto sombreado |

### Define Leader (Leader)

Define un objeto directriz (leader)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto de la directriz |
| Points | `P` | Point | lista | Puntos que definen la geometría de la directriz |
| Plane *(opcional)* | `Pl` | Plane | item | Plano para ubicar la directriz. Si se omite, se usa el plano XY del mundo. |
| Dimension Style *(opcional)* | `[]DS` | Text | item | Estilo de cota. Si no se entrega, se usa el estilo activo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Leaders | `L` | Generic Data | item | Directrices definidas |

### Define Linear Dimension (Linear Dim)

Define una cota lineal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point 1 | `P1` | Point | item | Primer punto de la cota |
| Point 2 | `P2` | Point | item | Segundo punto de la cota |
| Plane *(opcional)* | `Pl` | Plane | item | Plano de la cota. Si se omite, la cota será alineada. |
| Offset *(opcional)* | `O` | Number | item | Desfase de la cota desde P1 |
| Dimension style *(opcional)* | `[]DS` | Text | item | Estilo de cota. Si no se entrega, se usa el estilo activo. |
| Overwrite Text *(opcional)* | `T` | Text | item | Reemplaza el texto de la cota |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Linear Dimension | `LD` | Generic Data | item | Cota lineal |

### Define Radial Dimension (RadialDim)

Define un objeto cota radial

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center | `C` | Point | item | Centro |
| Tip | `T` | Point | item | Punto para la punta de la cota sobre el círculo |
| Dimension Point | `D` | Point | item | Ubicación de la cota |
| Dimension Plane | `P` | Plane | item | Plano de la cota. Si se omite, se usa XY. |
| Dimension Style *(opcional)* | `[]DS` | Text | item | Estilo de cota. Si no se entrega, se usa el estilo activo. |
| Overwrite Text *(opcional)* | `T` | Text | item | Reemplaza el texto de la cota |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Radial Dimension | `RD` | Generic Data | item | Cota radial |

### Define Text Dot (TextDot)

Define un objeto punto de texto (text dot)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto |
| Location | `P` | Point | item | Ubicación del TextDot |
| Font *(opcional)* | `F` | Text | item | Fuente del texto |
| Size *(opcional)* | `S` | Integer | item | Tamaño del texto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| TextDot | `T` | Generic Data | item | Objeto punto de texto |

### Define Text Object (Text)

Define un objeto texto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto |
| Plane *(opcional)* | `P` | Plane | item | Plano para ubicar el texto |
| Dimension Style *(opcional)* | `[]DS` | Text | item | Estilo de cota. Si no se entrega, se usa el estilo activo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Generic Data | item | Objeto texto |

## 05 Blocks

### Define Embedded Block (DefEmbed)

Define un bloque incrustado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Generic Data | lista | Geometría de cada definición de bloque. Cada rama se convierte en una definición de bloque. |
| Attributes *(opcional)* | `A` | Generic Data | lista | Atributos a asignar a la geometría de la definición de bloque |
| Block Name | `N` | Text | item | Nombre de bloque de cada definición. Cada rama necesita su propio nombre. Si ya existe en el documento una definición con el mismo nombre, se sobrescribe. |
| Base Plane | `P` | Plane | item | Plano base de cada definición de bloque. Cada rama necesita su propio plano base. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definition | `BD` | Generic Data | item | Definición de bloque |

### Define Linked Block (DefLnkBlock)

Crea una definición de bloque vinculada. La definición se puede instanciar como bloque.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Path of Folder | `F` | Text | item | Indica la ruta de la carpeta |
| Block Name (File Name) | `N` | Text | item | Indica el nombre del bloque |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Definition | `D` | Generic Data | lista | Definición de bloque creada |

### Explode Block (ExpBlock)

Explota un bloque para obtener su geometría.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block | `B` | Block | item | Bloque o definición de bloque a consultar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `N` | Text | item | Nombre del bloque |
| Transform | `X` | Transform | item | La transformación del bloque |
| Geometry | `G` | Geometry | lista | Geometría del bloque |

### Get Block Info (Block Info)

Devuelve información de una instancia de bloque

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block | `B` | Block | item | Bloque o definición de bloque a consultar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `N` | Text | item | Nombre del bloque |
| Plane | `P` | Plane | item | Plano base transformado |
| Transform | `X` | Transform | item | La transformación del bloque |
| Block Type | `T` | Text | item | Tipo de bloque |
| FilePath | `F` | Text | item | Ruta del archivo si el bloque está vinculado; si no, devuelve nulo |
| Active | `D` | Boolean | item | True si la definición del bloque existe y está actualizada en el documento activo. |

### Insert Block (Insert)

Inserta un bloque del documento activo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block Name | `N` | Text | item | Nombre del bloque |
| Plane | `P` | Plane | item | Plano de inserción |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Block | `B` | Generic Data | item | Bloque |

### List Blocks In Document (ListBlockD)

Lista todos los nombres de bloques del documento de Rhino

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Name | `N` | Text | item | Nombres de los bloques |

### Push Block Definitions (PushBlk)

Envía definiciones de bloque al documento de Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `O` | Generic Data | árbol | Bloques a definir |
| Activate *(opcional)* | `A` | Boolean | item | Enviar las definiciones a Rhino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `O` | Generic Data | árbol | Paso directo de los objetos de entrada. Si el componente se activó, los bloques de este flujo ya se habrán enviado. |
| Message | `S` | Text | lista | Mensaje de estado |

### Reload Linked Block Definitions (ReloadBlk)

Recarga desde el disco las definiciones de bloques vinculados. Los objetos que no son bloques y los bloques incrustados pasan sin cambios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `O` | Generic Data | árbol | Árbol de objetos con instancias de bloque a recargar. Los que no son bloques y los bloques incrustados pasan sin cambios. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Objects | `O` | Generic Data | árbol | Objetos con las definiciones de bloques vinculados recargadas desde el disco |
| Definitions | `D` | Generic Data | item | Definiciones de bloque únicas que se recargaron |

## 06 Bake

### Bake All eleFront (Bake All, parámetro)

Hace bake de todos los objetos de eleFront con este botón

Tipo de dato: **Boolean**

### Bake Group (parámetro)

Activa todos los componentes de bake que comparten el grupo de este botón

Tipo de dato: **Boolean**

### Bake Layers (BkLay)

Hace bake de capas en Rhino

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Layers | `L` | Layer | item | Capas de los objetos. |
| Bake *(opcional)* | `B` | Boolean | item | Hacer bake de las capas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Message | `S` | Text | lista | Mensaje de estado |

### Bake Objects (Bake)

Hace bake de objetos en Rhino con atributos de Rhino y atributos de usuario

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | árbol | Geometría a la que hacer bake |
| Attributes *(opcional)* | `A` | Generic Data | árbol | Atributos a asignar a la geometría al hacer bake |
| BakeName *(opcional)* | `N` | Text | item | Si se indica, ¡se eliminan todos los objetos a los que antes se les hizo bake con el mismo nombre de bake! Solo admite una entrada. No asignes nombres de bake distintos a ramas distintas; usa pares clave/valor para asignar atributos distintos a cada rama. |
| Bake Settings *(opcional)* | `S` | Generic Data | item | Entrega aquí los ajustes de bake para tener más control sobre su comportamiento. Reemplazan cualquier preajuste seleccionado en el componente. |
| Bake *(opcional)* | `B` | Boolean | item | Entrada opcional de interruptor para disparar el bake. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Message | `S` | Text | lista | Mensaje de estado |
| Ghosts | `G` | Generic Data | lista | Objetos fantasma de la geometría a la que se hizo bake |

### Bake Objects To File (BakeToFile)

Hace bake de objetos en un archivo de Rhino externo, con atributos de Rhino y atributos de usuario

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| FilePath | `F` | Text | item | Ruta del archivo de Rhino en el que hacer bake de la geometría |
| Geometry | `G` | Geometry | lista | Geometría a la que hacer bake |
| Attributes *(opcional)* | `A` | Generic Data | lista | Atributos a asignar a la geometría al hacer bake |
| BakeName *(opcional)* | `N` | Text | item | Si se indica, ¡se eliminan todos los objetos a los que antes se les hizo bake con el mismo nombre de bake! Solo admite una entrada. No asignes nombres de bake distintos a ramas distintas; usa pares clave/valor para asignar atributos distintos a cada rama. |
| Bake Settings *(opcional)* | `S` | Generic Data | item | Entrega aquí los ajustes de bake para tener más control sobre su comportamiento. Reemplazan cualquier preajuste seleccionado en el componente. |
| Bake *(opcional)* | `B` | Boolean | item | Entrada opcional de interruptor para disparar el bake. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guids | `G` | Generic Data | lista | Guids de la geometría a la que se hizo bake |

### Bake Settings (BkSettings)

Selecciona ajustes de bake predefinidos, con opciones para reemplazarlos por ajustes personalizados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Auto-Push Block Definition *(opcional)* | `AP` | Boolean | item | Poner en True para enviar automáticamente las definiciones que no están en el documento. |
| Auto-Manifest Ghost Geometry *(opcional)* | `AM` | Boolean | item | Poner en True para volver a leer automáticamente la geometría de la geometría fantasma. Ojo: esto puede volver todo más lento si los archivos de origen son grandes. |
| Block Names Handling *(opcional)* | `[]BN` | Text | item | Elige cómo manejar los nombres de bloque duplicados. Conecta una ValueList para ver las opciones. |
| DimStyle Name Handling *(opcional)* | `[]DS` | Text | item | Elige cómo manejar los estilos de cota duplicados. Conecta una ValueList para ver las opciones. |
| Material Name Handling *(opcional)* | `[]MN` | Text | item | Elige cómo manejar los nombres de material duplicados. Conecta una ValueList para ver las opciones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bake Settings | `BS` | Generic Data | item | Ajustes de bake |

## 07 Trees

### Clean Parallel (CleanP)

Limpia el árbol de datos principal y entrega todos los objetos secundarios respectivos por elemento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Data | `P` | Generic Data | árbol | Árbol de datos principal a injertar |
| Secondary Data 1 *(opcional)* | `1` | Generic Data | árbol | Lista opcional de ramas a filtrar en sincronía |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Data | `P` | Generic Data | árbol | Flujo de datos principal limpio |
| Secondary Data 1 | `1` | Generic Data | árbol | Datos sincronizados en 1 |

### Create Tree (Tree)

Crea un árbol indicando una ruta de rama para cada elemento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Datos a agregar al árbol |
| Path | `P` | Path | árbol | Ruta de cada dato |
| Ensure *(opcional)* | `E` | Path | árbol | Rutas que se deben crear independientemente de los datos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Datos en la nueva estructura de árbol |

### Duplicate Data Match (Dup)

Duplica datos según un árbol de datos de origen

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Source Data Tree | `S` | Generic Data | lista | Árbol de datos de origen con el que coincidir |
| Secondary Data 1 *(opcional)* | `1` | Generic Data | lista | Lista opcional de datos a duplicar en sincronía |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Source Data | `S` | Generic Data | lista | Flujo de datos principal |
| Secondary Data 1 | `1` | Generic Data | lista | Datos sincronizados en 1 |

### Get Matching Branches (GetBrn)

Toma las ramas de un árbol paralelo con las mismas rutas. Puede quitar las vacías.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Data | `P` | Generic Data | árbol | Árbol de datos principal a injertar |
| Secondary Data 1 *(opcional)* | `1` | Generic Data | árbol | Lista opcional de ramas a filtrar en sincronía |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Data | `P` | Generic Data | árbol | Flujo de datos principal limpio |
| Secondary Data 1 | `1` | Generic Data | árbol | Datos sincronizados en 1 |

### Graft By Index (GraftI)

Injerta (graft) elementos en ramas nuevas usando un índice para la rama de destino. Cada elemento del árbol se asigna a una ruta nueva según su índice correspondiente.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Árbol de datos a reestructurar |
| Indices | `I` | Integer | árbol | Árbol de índices a agregar a las rutas. Debe tener las mismas ramas y cantidades de elementos que el árbol de datos. El índice de cada elemento determina su nueva rama. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Árbol de datos reestructurado con los índices agregados a las rutas |

### Graft Match (GraftM)

Hace coincidir árboles secundarios con un árbol guía por prefijo de ruta. Una rama secundaria coincide cuando las rutas de la guía empiezan con su ruta.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guide Tree | `G` | Generic Data | árbol | Árbol principal con rutas de profundidad completa |
| Secondary Data 1 *(opcional)* | `1` | Generic Data | árbol | Árbol secundario opcional a comparar con la guía |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guide Tree | `G` | Generic Data | árbol | Árbol guía (filtrado si Matching Only está activo) |
| Secondary Data 1 | `1` | Generic Data | árbol | Datos coincidentes de la entrada 1 |

### Graft Parallel (GraftP)

Injerta (graft) el árbol de datos principal y entrega todos los objetos secundarios respectivos por elemento

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Data | `P` | Generic Data | árbol | Árbol de datos principal a injertar |
| Secondary Data 1 *(opcional)* | `1` | Generic Data | árbol | Lista opcional de ramas a filtrar en sincronía |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Data | `P` | Generic Data | árbol | Flujo de datos principal injertado |
| Secondary Data 1 | `1` | Generic Data | árbol | Datos sincronizados en 1 |

### Shift To Depth (ShfDep)

Desplaza un árbol de datos a una profundidad indicada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol a desplazar |
| Depth | `D` | Integer | item | Profundidad de la rama |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shifted Tree | `S` | Generic Data | árbol | Árbol desplazado |

### ShiftMatch (ShiftM)

Desplaza un árbol de datos para que coincida con la estructura de un árbol guía

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guide Tree | `G` | Generic Data | árbol | Árbol que determina la profundidad del desplazamiento |
| Secondary Data 1 *(opcional)* | `1` | Generic Data | árbol | Lista opcional de ramas a desplazar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Guide Tree | `G` | Generic Data | árbol | Árbol guía |
| Secondary Data 1 | `1` | Generic Data | árbol | Datos sincronizados en 1 |

## 08 Params

### eleFront Data Description (Description, parámetro)

Usa este componente para guiar tus flujos de datos en el lienzo de forma ordenada. Usa una descripción con sentido

Tipo de dato: **eleFrontDataDescription**

### Extended Geometry (ExtGeo, parámetro)

Parámetro para todos los tipos de geometría, incluidos los que no son nativos de Grasshopper

Tipo de dato: **Extended Geometry**

## 09 Files

### Construct FilePath (ConPath)

Construye una ruta de archivo a partir de carpetas, nombre de archivo y extensión

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Folders | `Fo` | Text | lista | Lista de nombres de carpetas a combinar en una ruta |
| File Name | `Fn` | Text | item | Nombre de archivo sin extensión |
| Extension *(opcional)* | `Ex` | Text | item | Extensión del archivo (con o sin el punto inicial) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| FilePath | `F` | Text | item | Ruta de archivo construida |

### Deconstruct FilePath (DecPath)

Divide una ruta de archivo en carpeta y nombre de archivo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| FilePath | `F` | Text | item | Ruta del archivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Folder | `Fo` | Text | item | Carpeta |
| File Name | `Fn` | Text | item | Nombre del archivo sin extensión |
| File Name with Extension | `Fn+` | Text | item | Nombre del archivo con extensión |

### Export Generic (ExpGen)

Exporta a cualquier tipo de archivo que admita Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Folder Path | `F` | Text | item | Carpeta donde guardar los objetos exportados |
| File Name | `N` | Text | item | Nombre del archivo exportado. |
| File Extension | `E` | Text | item | La extensión del archivo determina el formato de salida |
| Rhino Objects *(opcional)* | `ID` | Guid | lista | Objetos de Rhino a exportar |
| Axis System *(opcional)* | `P` | Plane | item | Plano que define el sistema de ejes. Si se omite, se usa el plano XY del mundo |
| Export Scheme *(opcional)* | `S` | Text | item | Esquema de exportación. Si se omite, se usa el último esquema usado |
| Export | `A` | Boolean | item | Activa el componente. Para esta entrada no uses un botón, sino un interruptor (toggle) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Messages | `O` | Text | item | Mensajes de salida |

### Export to Rhino File (Exp3dm)

Exporta objetos a un archivo 3dm

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Destination | `D` | Text | item | Ruta donde guardar el archivo. Solo una ruta por rama. |
| Rhino Object | `ID` | Guid | lista | Objetos de Rhino a exportar |
| Base Plane *(opcional)* | `P` | Plane | item | Plano base para la exportación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Messages | `O` | Text | item | Mensajes de salida |

### Get Current File (File)

Devuelve el nombre y la carpeta del archivo actual.

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Folder | `Fo` | Text | item | Carpeta contenedora |
| File Name | `Fi` | Text | item | Nombre del archivo |
| Worksession | `W` | Text | item | Ruta del archivo de la worksession, si existe. |
| Grasshopper Folder | `GHF` | Text | item | Carpeta que contiene el archivo de Grasshopper actual, si existe |
| Grasshopper File Name | `GHFi` | Text | item | Nombre del archivo de Grasshopper actual, si existe |

### List Files (Files)

Lista todos los archivos de una carpeta que coinciden con una máscara de búsqueda

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Folder | `F` | Text | item | Carpeta en la que buscar |
| Search Mask *(opcional)* | `S` | Text | item | Máscara de búsqueda para los resultados. Admite patrones con comodines. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Files | `F` | Text | lista | Rutas completas de los archivos |

### Merge Rhino Files (MergeF)

Fusiona archivos de Rhino en uno solo, con distintos ajustes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Source Files | `S` | Text | lista | Rutas de los archivos a fusionar. Se fusiona la lista de cada rama. |
| Destination | `D` | Text | lista | Ruta donde guardar el archivo. Solo una ruta por rama. |
| Block Name Handling *(opcional)* | `[]BN` | Text | item | Elige cómo manejar los nombres de bloque duplicados. Conecta una ValueList para ver las opciones. |
| DimStyle Name Handling *(opcional)* | `[]DS` | Text | item | Elige cómo manejar los estilos de cota duplicados. Conecta una ValueList para ver las opciones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Messages | `O` | Text | item | Mensajes de salida |

### Modify Rhino File (Modify3dm)

Agrega o quita objetos de un archivo de Rhino externo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File to Modify | `F` | Text | item | Ruta del archivo a modificar. |
| Objects to Add *(opcional)* | `A` | Generic Data | lista | Objetos a agregar al archivo. Deben ser geometría de referencia, geometría fantasma o un Guid |
| Objects to Delete *(opcional)* | `D` | Generic Data | lista | Objetos a eliminar del archivo. Deben ser geometría fantasma (del mismo modelo) o un Guid |
| Block Name Handling *(opcional)* | `[]BN` | Text | item | Elige cómo manejar los nombres de bloque duplicados. Conecta una ValueList para ver las opciones. |
| DimStyle Name Handling *(opcional)* | `[]DS` | Text | item | Elige cómo manejar los estilos de cota duplicados. Conecta una ValueList para ver las opciones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Messages | `O` | Text | item | Mensajes de salida |

### Select Folder (SelFolder)

Selecciona de forma interactiva una ruta de carpeta usando listas de valores autocompletadas. Conecta una Value List a la entrada Root para las carpetas superiores y luego agrega entradas Subfolder para bajar de nivel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Root | `[]R` | Text | item | Ruta de la carpeta raíz. Conecta una Value List para ver las carpetas superiores del archivo actual. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Path | `P` | Text | item | Ruta de carpeta o archivo construida |
| Valid | `V` | Boolean | item | True si la ruta existe |
