---
title: "Catálogo Grasshopper — LunchBox"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "LunchBox"
libraries: ["LunchBox 2025.5.5.0"]
components: 99
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/lunchbox, programacion/scripts, geometria/patrones, datos/arboles, geometria/superficies, rhino/documento]
---

# LunchBox

99 objetos · librería: LunchBox 2025.5.5.0

Mapas: [[Mapa - Scripts, interfaz y archivos]] (28) · [[Mapa - Patrones y teselados]] (25) · [[Mapa - Data trees y listas]] (19) · [[Mapa - Superficies y NURBS]] (13) · [[Mapa - Documento de Rhino]] (11) · [[Mapa - Mallas y SubD]] (7) · [[Mapa - Brep y sólidos]] (4) · [[Mapa - Puntos, vectores y planos]] (2) · [[Mapa - Fabricación]] (1)

## Data

### Convert JSON to XML (JSON-XML)

Convierte un texto JSON a XML.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| JSON String | `JSON` | Text | item | Un texto JSON (JavaScript Object Notation). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| XML String | `XML` | Generic Data | item | Texto XML convertido. |

### Convert XML to JSON (XML-JSON)

Convierte un texto XML a JSON

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| XML String | `XML` | Text | item | Un texto XML. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| JSON String | `JSON` | Generic Data | item | Texto JSON convertido. |

### Create CSV (CSV)

Crea un texto CSV

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data Grid Headers | `Headers` | Text | lista | Una lista de nombres de encabezado para la grilla de datos. |
| Value Tree | `Values` | Text | árbol | Una estructura de árbol de valores numéricos. (Por defecto, las ramas se tratan como columnas.) |
| Delimiter | `Delimit` | Text | item | Un separador para el texto CSV (normalmente una coma). |
| Quote Items | `Quotes` | Boolean | item | Incluye comillas alrededor de los encabezados y valores del CSV. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CSV String | `CSV` | Generic Data | item | El texto CSV. |

### Create Data Grid (DataGrid)

Crea una vista de grilla de datos. Los datos se pueden guardar como archivo CSV.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data Grid Headers | `Headers` | Text | lista | Una lista de nombres de encabezado para la grilla de datos. |
| Value Tree | `Values` | Text | árbol | Un árbol de valores numéricos. El orden de las ramas debe corresponder a un encabezado de columna |

### Create DataSet (DataSet)

Crea un DataSet

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| DataSet Name | `Name` | Text | item | Nombre del DataSet. |
| DataTables | `Tables` | Generic Data | lista | Una lista de DataTables para el DataSet |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| DataSet | `DataSet` | Generic Data | item | El objeto DataSet. |

### Create DataTable (DataTable)

Crea un DataTable

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Table Name | `Name` | Text | item | Nombre de la tabla de datos. |
| Table Headers | `Headers` | Text | lista | Una lista de nombres de encabezado correspondientes a los datos. |
| Value Tree | `Values` | Text | árbol | Un árbol de valores numéricos o de texto. El orden de las ramas debe corresponder a la lista de encabezados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| DataTable | `DataTable` | Generic Data | item | El objeto DataTable. |

### Create JSON (JSON)

Crea JSON a partir de un DataSet

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Write JSON | `Write` | Boolean | item | Valor booleano para escribir el archivo JSON. |
| File Path | `Path` | Text | item | Ruta donde guardar el archivo XML. |
| DataSet | `DataSet` | Generic Data | item | El DataSet a serializar como JSON |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| JSON | `JSON` | Generic Data | item | JSON como texto. |

### Create XML from Tree (XML Tree)

Crea XML a partir de un árbol de Grasshopper con texto o números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Write XML | `Write` | Boolean | item | Valor booleano para escribir el archivo XML. |
| File Path | `Path` | Text | item | Ruta donde guardar el archivo XML. |
| DataTree | `Tree` | Text | árbol | El árbol de datos de Grasshopper |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| XML | `XML` | Generic Data | item | XML como texto. |

### Read CSV (CSV)

Lee un texto CSV (valores separados por comas).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| CSV String | `CSV` | Text | lista | Un texto CSV (valores separados por comas). |
| Delimiter | `Delimit` | Text | item | Un separador para el texto CSV (normalmente una coma). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Headers | `Headers` | Generic Data | item | Nombres de encabezado de cada columna. |
| Values | `Values` | Generic Data | item | Valores interpretados del CSV. |

### Read XML by Tag (XML)

Lee datos XML por etiqueta.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| XML | `XML` | Text | item | Los datos XML a interpretar. |
| XML Tag | `Tag` | Text | item | Etiqueta a buscar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| XML InnerText | `InnerText` | Generic Data | item | Obtiene los valores concatenados del nodo y de todos sus nodos hijos. |
| XML Inner XML | `InnerXML` | Generic Data | item | Obtiene el marcado de los nodos hijos. |

### Write XML File (Write XML)

Crea XML a partir de un DataSet

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Write XML | `Write` | Boolean | item | Valor booleano para escribir el archivo XML. |
| File Path | `Path` | Text | item | Ruta donde guardar el archivo XML. |
| DataSet | `DataSet` | Generic Data | item | El DataSet a serializar como XML |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| XML | `XML` | Generic Data | item | XML como texto. |

## Form

### 3D Supershape (3DSupershape)

Crea una superforma (supershape) 3D paramétrica

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| m Parameter | `m` | Number | item | Parámetro R de la forma. |
| a Parameter | `a` | Number | item | Parámetro T de la forma |
| b Parameter | `b` | Number | item | Parámetro de escala de la forma |
| n1 Parameter | `n1` | Number | item | Dominio en la dirección U |
| n2 Parameter | `n2` | Number | item | Dominio en la dirección V |
| n3 Parameter | `n3` | Number | item | Dominio en la dirección V |
| Scale Parameter | `S` | Number | item | Escala de la superforma |
| D1 Interval | `D1` | Domain | item | Dominio en la dirección U |
| D2 Interval | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

### Conoid Surface (Conoid)

Crea la superficie conoide de Plücker.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| R Parameter | `R` | Number | item | Parámetro R de la forma. |
| T Parameter | `T` | Number | item | Parámetro T de la forma |
| Scale | `S` | Number | item | Parámetro de escala de la forma |
| Domain 1 | `D1` | Domain | item | Dominio en la dirección U |
| Domain 2 | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

### Enneper Surface (Enneper)

Crea una superficie de Enneper paramétrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| R Parameter | `a` | Integer | item | Parámetro a de la forma. |
| Scale | `S` | Number | item | Parámetro de escala de la forma |
| Domain 1 | `D1` | Domain | item | Dominio en la dirección U |
| Domain 2 | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

### Helicoid Surface (Helicoid)

Crea una superficie helicoide paramétrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| R Parameter | `R` | Number | item | Parámetro R de la forma. |
| T Parameter | `T` | Number | item | Parámetro T de la forma |
| Scale | `S` | Number | item | Parámetro de escala de la forma |
| Domain 1 | `D1` | Domain | item | Dominio en la dirección U |
| Domain 2 | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

### Hyperbolic Paraboloid (Paraboloid)

Crea una superficie paraboloide paramétrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| R Parameter | `a` | Number | item | Parámetro a de la forma. |
| R Parameter | `b` | Number | item | Parámetro a de la forma. |
| Scale | `S` | Number | item | Parámetro de escala de la forma |
| Domain 1 | `D1` | Domain | item | Dominio en la dirección U |
| Domain 2 | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

### Klein Surface (Klein)

Crea una superficie de Klein paramétrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| R Parameter | `R` | Number | item | Parámetro R de la forma. |
| T Parameter | `T` | Number | item | Parámetro T de la forma |
| Scale | `S` | Number | item | Parámetro de escala de la forma |
| Domain 1 | `D1` | Domain | item | Dominio en la dirección U |
| Domain 2 | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

### Mobius Surface (Mobius)

Crea una superficie de Möbius paramétrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| R Parameter | `R` | Number | item | Parámetro R de la forma. |
| T Parameter | `T` | Number | item | Parámetro T de la forma |
| Scale | `S` | Number | item | Parámetro de escala de la forma |
| Domain 1 | `D1` | Domain | item | Dominio en la dirección U |
| Domain 2 | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

### Platonic Cube (PlatoCube)

Crea un cubo paramétrico con un parámetro de truncamiento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pln` | Plane | item | Plano de orientación. |
| Radius | `Rad` | Number | item | Radio esférico. |
| Truncation | `Trunc` | Number | item | El parámetro de truncamiento (un valor entre 0 y 1). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Platonic Solid | `Plato` | Generic Data | item | El sólido platónico |

### Platonic Dodecahedron (PlatoDodec)

Crea un dodecaedro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pln` | Plane | item | Plano de orientación. |
| Radius | `Rad` | Number | item | Radio esférico. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Platonic Solid | `Plato` | Generic Data | item | El sólido platónico |

### Platonic Icosahedron (PlatoIcosa)

Crea un icosaedro paramétrico con un parámetro de truncamiento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pln` | Plane | item | Plano de orientación. |
| Radius | `Rad` | Number | item | Radio esférico. |
| Truncation | `Trunc` | Number | item | El parámetro de truncamiento (un valor entre 0 y 1). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Platonic Solid | `Plato` | Generic Data | item | El sólido platónico |

### Platonic Octahedron (PlatoOcta)

Crea un octaedro paramétrico con un parámetro de truncamiento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pln` | Plane | item | Plano de orientación. |
| Radius | `Rad` | Number | item | Radio esférico. |
| Truncation | `Trunc` | Number | item | El parámetro de truncamiento (un valor entre 0 y 1). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Platonic Solid | `Plato` | Generic Data | item | El sólido platónico |

### Platonic Tetrahedron (PlatoTetra)

Crea un tetraedro paramétrico con un parámetro de truncamiento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pln` | Plane | item | Plano de orientación. |
| Radius | `Rad` | Number | item | Radio esférico. |
| Truncation | `Trunc` | Number | item | El parámetro de truncamiento (un valor entre 0 y 1). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Platonic Solid | `Plato` | Generic Data | item | El sólido platónico |

### Torus Surface (Torus)

Crea una superficie toroidal (toro) paramétrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| C Parameter | `C` | Number | item | Parámetro C de la forma. |
| R Parameter | `R` | Number | item | Parámetro R de la forma. |
| T Parameter | `T` | Number | item | Parámetro T de la forma |
| Scale | `S` | Number | item | Parámetro de escala de la forma |
| Domain 1 | `D1` | Domain | item | Dominio en la dirección U |
| Domain 2 | `D2` | Domain | item | Dominio en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Generic Data | item | La superficie matemática. |

## Generate

### Attractor (Attract)

Genera valores de atractor usando listas de atractores y objetivos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Attractor Points | `Attractors` | Point | lista | Una lista de uno o más puntos atractores. |
| Target Points | `Targets` | Point | lista | Una lista de uno o más objetivos. |
| Attractor Domain | `Domain` | Domain | item | Un dominio para los valores del atractor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `Values` | Generic Data | item | Valores del atractor escalados al dominio. |
| Vectors | `Vectors` | Generic Data | item | Vectores del atractor escalados al dominio. |
| Distances | `Distances` | Generic Data | item | Una lista de distancias. Si hay más de un atractor, es un promedio. |

### Attractor Wave (AttWave)

Genera un efecto de atractor en onda usando listas de atractores y objetivos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Attractor Points | `Attractors` | Point | lista | Una lista de uno o más puntos atractores. |
| Target Points | `Targets` | Point | lista | Una lista de uno o más objetivos. |
| Attractor Domain | `Domain` | Domain | item | Un dominio para los valores del atractor |
| Frequency | `Freq` | Number | item | Frecuencia del atractor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `Values` | Generic Data | item | Valores del atractor escalados al dominio. |
| Vectors | `Vectors` | Generic Data | item | Vectores del atractor escalados al dominio. |
| Distances | `Distances` | Generic Data | item | Una lista de distancias. Si hay más de un atractor, es un promedio. |

### Constant Quad Subdivide (ConstQuad)

Subdivide un panel triangular en celdas cuadrangulares

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Quad Surface | `Quad` | Surface | item | Una superficie cuadrangular sin recortar a subdividir |
| Subdivide | `N` | Integer | item | Cantidad de subdivisiones. |
| Recursion Toggle | `R` | Boolean | item | Alterna entre dos opciones de subdivisión recursiva |
| Wires | `Wires` | Boolean | item | Si es True, el componente devuelve polilíneas (más rápido); si es False, devuelve superficies (más lento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Quad Cells | `Quad` | Generic Data | item | Lista de celdas cuadrangulares. |

### Panel Frame (Frame)

Crea un marco con offset a partir de un panel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panel | `Panel` | Brep | item | El panel a enmarcar. |
| Scale Factor | `S` | Number | item | Un factor de escala entre 0 y 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panel Frame | `Frame` | Generic Data | item | El marco del panel. |
| Panel | `Panel` | Generic Data | item | El panel interior escalado |

### Subdivide Quad (QuadSub)

Subdivide un cuadrilátero en celdas autosemejantes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Quad Surface | `Quad` | Surface | item | Una superficie cuadrangular sin recortar a subdividir |
| Subdivide | `N` | Integer | item | Cantidad de subdivisiones. |
| Boolean 1 | `B1` | Boolean | item | El primer booleano. |
| Boolean 2 | `B2` | Boolean | item | El segundo booleano. |
| Boolean 3 | `B3` | Boolean | item | El tercer booleano. |
| Boolean 4 | `B4` | Boolean | item | El cuarto booleano. |
| Wires | `Wires` | Boolean | item | Si es True, el componente devuelve polilíneas (más rápido); si es False, devuelve superficies (más lento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Quad Cells A | `QuadA` | Generic Data | item | Lista de celdas cuadrangulares. |
| Quad Cells B | `QuadB` | Generic Data | item | Lista de celdas cuadrangulares. |

### Subdivide Triangle (TriSub)

Subdivide un triángulo en celdas autosemejantes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Triangular Curve | `Tri` | Curve | item | Una curva o superficie triangular cerrada a subdividir |
| Subdivide | `N` | Integer | item | Cantidad de subdivisiones. |
| Boolean 1 | `B1` | Boolean | item | El primer booleano. |
| Boolean 2 | `B2` | Boolean | item | El segundo booleano. |
| Boolean 3 | `B3` | Boolean | item | El tercer booleano. |
| Boolean 4 | `B4` | Boolean | item | El cuarto booleano. |
| Wires | `Wires` | Boolean | item | Si es True, el componente devuelve polilíneas (más rápido); si es False, devuelve superficies (más lento) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Triangle Cells A | `TriA` | Generic Data | item | Lista de celdas triangulares. |
| Triangle Cells B | `TriB` | Generic Data | item | Lista de celdas triangulares. |

## Mass

### Building Mass (Area Constrained) (Mass by Area)

Crea una masa de edificio rectangular restringida por un valor de área total.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `pln` | Plane | item | El plano base de la masa del edificio. |
| Total Area | `Area` | Number | item | Área total de la masa del edificio (suma del área de todos los pisos). |
| Footprint Width | `Width` | Number | item | El ancho de la planta de la masa del edificio. |
| Footprint Length | `Length` | Number | item | El largo de la planta de la masa del edificio. |
| Floor Height | `floorHeight` | Number | lista | La altura de piso a piso de la masa del edificio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Floors | `Floors` | Generic Data | item | Una lista de superficies de piso. |
| Mass | `Mass` | Generic Data | item | La envolvente extruida de la masa del edificio. |

### Building Mass (Boundary and Area) (Mass Boundary Area)

Crea una masa de edificio a partir de una forma de contorno, restringida por el área total.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundary Curve | `Boundary` | Curve | item | La curva de contorno de la planta de la masa del edificio. |
| Total Area | `Area` | Number | item | Área total de la masa del edificio (suma del área de todos los pisos). |
| Floor Height | `floorHeight` | Number | lista | La altura de piso a piso de la masa del edificio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Floors | `Floors` | Generic Data | item | Una lista de superficies de piso. |
| Mass | `Mass` | Generic Data | item | La envolvente extruida de la masa del edificio. |

### Building Mass (Boundary and Floors) (Mass Boundary Floors)

Crea una masa de edificio a partir de una forma de contorno, restringida por la cantidad de pisos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundary Curve | `Boundary` | Curve | item | La curva plana de contorno de la planta de la masa del edificio. |
| Number of Floors | `numOfFloors` | Integer | item | La cantidad de pisos del edificio. |
| Floor Height | `floorHeight` | Number | lista | La altura de piso a piso de la masa del edificio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Floors | `Floors` | Generic Data | item | Una lista de superficies de piso. |
| Mass | `Mass` | Generic Data | item | La envolvente extruida de la masa del edificio. |

### Building Mass (Floor Count) (Mass by Floor)

Crea una masa de edificio rectangular a partir de la cantidad de pisos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `pln` | Plane | item | El plano base de la masa del edificio. |
| Number of Floors | `numOfFloors` | Integer | item | La cantidad de pisos del edificio. |
| Footprint Width | `Width` | Number | item | El ancho de la planta de la masa del edificio. |
| Footprint Length | `Length` | Number | item | El largo de la planta de la masa del edificio. |
| Floor Height | `floorHeight` | Number | lista | La altura de piso a piso de la masa del edificio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Floors | `Floors` | Generic Data | item | Una lista de superficies de piso. |
| Mass | `Mass` | Generic Data | item | La envolvente extruida de la masa del edificio. |

## Mesh

### Mesh Edges (with Tolerance) (MshEdge)

Busca las aristas desnudas de una malla y las aristas entre caras con un ángulo mayor que el indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Un objeto malla. |
| Angle Threshold | `Angle` | Number | item | Se devuelven las aristas entre caras con un ángulo mayor que este. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Interior Edges | `IntEdges` | Generic Data | item | Aristas interiores. |
| Naked Edges | `NakedEdges` | Generic Data | item | Aristas desnudas. |

### Mesh Extrude (MshExtrude)

Extruye un objeto malla a lo largo de un vector dado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Una malla a la que aplicar offset (usa las normales de los vértices como dirección). |
| Direction | `Dir` | Vector | item | Dirección en la que extruir la malla. (La magnitud del vector determina la distancia.) |
| Solid Toggle | `Solid?` | Boolean | item | Si es True, cose la malla original con la malla extruida. |
| Extrude Both Sides Toggle | `Both Sides?` | Boolean | item | El resultado es una malla extruida a lo largo del vector dado y del vector opuesto. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extruded Mesh | `Mesh` | Generic Data | item | La malla extruida. |

### Mesh Offset (MshOffset)

Aplica offset a un objeto malla usando las normales de los vértices de la malla de origen.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Una malla a la que aplicar offset (usa las normales de los vértices como dirección). |
| Offset Distance | `Offset` | Number | item | Distancia de offset de la malla. |
| Solid Toggle | `Solid?` | Boolean | item | Si es True, cose la malla original con la malla con offset para intentar obtener una malla sólida. |
| Offset Both Sides Toggle | `Both Sides?` | Boolean | item | Si es True, se aplica offset a la malla en ambas direcciones desde la original. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset Mesh | `Mesh` | Generic Data | item | La malla con offset. |

### Mesh Reduce (MshReduce)

Reduce los polígonos de una malla para simplificarla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Una malla a reducir. |
| Target Size | `Size` | Integer | item | Reduce hasta la cantidad de caras objetivo. |
| Distort | `Dist` | Boolean | item | Deforma la malla después de reducirla. |
| Accuracy | `Accuracy` | Number | item | Precisión de la nueva malla (0 = menos precisa, 10 = más precisa). |
| Normalize Size | `Normalize` | Boolean | item | Normaliza la malla después de reducirla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reduced Mesh | `RedMsh` | Generic Data | item | La malla reducida. |

### Mesh to Nurbs (MeshNurbs)

Convierte las caras de una malla en superficies NURBS.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Mesh` | Mesh | item | Una malla cuyas caras se convierten en superficies NURBS. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Quadrangular Surfaces | `Quads` | Generic Data | item | Superficies obtenidas de las caras cuadrangulares de una malla. |
| Triangular Surfaces | `Tris` | Generic Data | item | Superficies obtenidas de las caras triangulares de una malla. |

### Quad Remesh (Remesh)

Rehace la malla de un Brep o malla usando la función Quad Remesh de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh or Brep | `Geo` | Geometry | item | Una malla o brep sobre el que hacer el remallado |
| Quad Remesh Parameters | `Parameters` | Generic Data | item | Ajustes usados en la operación Quad Remesh |
| Guide Curves *(opcional)* | `Guides` | Curve | lista | Curvas guía opcionales para el remallado. Deben estar sobre la superficie del objeto a remallar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Remeshed Mesh | `Mesh` | Generic Data | item | La malla de cuadriláteros resultante. |

### Quad Remesh Parameters (Parameters)

Parámetros para controlar la salida del componente Quad Remesh.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Target Quad Count | `QuadCount` | Integer | item | Si se calculan los cuadriláteros según una cantidad objetivo. |
| Use Adaptive Quads | `Adaptive?` | Boolean | item | Respeta lo más posible la cantidad objetivo de cuadriláteros. Si es True, se usan más cuadriláteros en zonas de alta curvatura. |
| Adaptive Quad Size | `AdaptiveSize` | Number | item | Tamaño objetivo de los cuadriláteros adaptativos usados en el remallado |
| Detect Hard Edges | `DetectEdges?` | Boolean | item | Si es True, intenta detectar y conservar las aristas duras del objeto. |
| Preserve Mesh Array Hard Edges | `PreserveEdges?` | Integer | item | 0=desactivado, 1=activado (inteligente), 2=activado (estricto): los conjuntos de mallas creados desde Breps conservan los bordes de las caras del brep. |
| Symmetry Axis | `Symmetry` | Integer | item | 0=ninguno, 1=X, 2=Y, 3=Z: eje de simetría a usar en el remallado. |
| Guide Curve Influence | `GuideInfuence` | Integer | item | 0=aproximar, 1=interpolar anillo de aristas, 2=interpolar bucle de aristas: este valor se ignora si no se entregan curvas guía |
| Target Edge Length | `Edge Length` | Number | item | Si es >0, los cuadriláteros se calculan según la longitud de arista (OJO: cuando se usa, reemplaza los parámetros de cantidad/tamaño adaptativo) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Remesh Parameters | `Parameters` | Generic Data | item | Parámetros de la operación Quad Remesh. |

## Panels

### Diamond Grid (DGrid)

Crea una grilla de puntos de esquina en diamante sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner Point 1 | `C1` | Generic Data | item | El primer punto de esquina |
| Corner Point 2 | `C2` | Generic Data | item | El segundo punto de esquina |
| Corner Point 3 | `C3` | Generic Data | item | El tercer punto de esquina |
| Corner Point 4 | `C4` | Generic Data | item | El cuarto punto de esquina |
| Mid Point | `MPt` | Generic Data | item | El punto medio del cuadrilátero. |
| Normals | `N` | Generic Data | item | Vector normal en el punto medio. |

### Diamond Panels (Diamond)

Crea paneles en diamante sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Diamond Panels | `Diamonds` | Generic Data | item | Paneles completos (cuadriláteros en diamante) |
| Tri Panels | `Triangles` | Generic Data | item | Paneles de borde (triangulares) |

### Hexagon Cells (Hex)

Crea celdas hexagonales sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| t Parameter | `t` | Number | item | Un valor de parámetro para transformar el ángulo del hexágono. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hexagon Cells | `Cells` | Generic Data | item | Celdas como polilíneas cerradas. |
| Centers | `Centers` | Generic Data | item | Centros de las celdas hexagonales |

### Quad Grid (QGrid)

Crea una grilla de puntos de esquina cuadrangular sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner Point 1 | `C1` | Generic Data | item | El primer punto de esquina |
| Corner Point 2 | `C2` | Generic Data | item | El segundo punto de esquina |
| Corner Point 3 | `C3` | Generic Data | item | El tercer punto de esquina |
| Corner Point 4 | `C4` | Generic Data | item | El cuarto punto de esquina |
| Mid Point | `MPt` | Generic Data | item | El punto medio del cuadrilátero. |
| Normals | `N` | Generic Data | item | Vector normal en el punto medio. |

### Quad Panels (Quads)

Crea paneles cuadrangulares sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Generic Data | item | Sistema de paneles. |

### Random Quad Panels (QuadRand)

Crea paneles cuadrangulares desfasados al azar sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| Random Seed | `S` | Integer | item | Valor semilla para la aleatoriedad. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Generic Data | item | Sistema de paneles. |

### Skewed Quads (SQuads)

Crea paneles cuadrangulares "sesgados" sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| t Parameter | `t` | Number | item | Un valor de parámetro para definir la cantidad de sesgo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Full Panels | `PanelsA` | Generic Data | item | Sistema de paneles. |
| Edge Panels | `PanelsB` | Generic Data | item | Sistema de paneles. |

### Staggered Quad Panels (QuadStag)

Crea paneles cuadrangulares desfasados (trabados) sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Generic Data | item | Sistema de paneles. |

### Triangle Panels B (TriB)

Crea paneles triangulares sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Generic Data | item | Sistema de paneles. |

### Triangle Panels C (TriC)

Crea paneles triangulares sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Generic Data | item | Sistema de paneles. |

### Triangular Panels A (TriA)

Crea paneles triangulares sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panels | `Panels` | Generic Data | item | Sistema de paneles. |

## Serialization

### Create GUID (GUID)

Crea un GUID (identificador único global) válido.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Guids | `count` | Integer | item | Cantidad de GUIDs a crear. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| GUID | `GUID` | Generic Data | item | GUID como texto. |

### Decrypt Text (Decrypt)

Descifra texto con una frase de contraseña.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Encrypted Text | `Text` | Text | item | Texto a descifrar. |
| Passphrase | `Pass` | Text | item | La frase de contraseña para descifrar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Decrypted Text | `Decrypt` | Generic Data | item | Texto descifrado. |

### Deserialize Geometry (Deserialize)

Deserializa un texto (JSON, XML o binario) a geometría de Grasshopper.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Serialized Text | `Text` | Text | item | Texto (binario, XML o JSON) a deserializar a geometría |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `Geo` | Generic Data | item | Geometría. |

### Encrypt Text (Encrypt)

Cifra texto con una frase de contraseña.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| String Cipher | `Text` | Text | item | Objeto texto a cifrar. |
| Passphrase | `Pass` | Text | item | La frase de contraseña para el cifrado. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Encrypted Text | `Encrypt` | Generic Data | item | Texto cifrado. |

### Hash Objects (Hash)

Usa un algoritmo de hash seguro (SHA) para obtener el hash de geometría o textos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Object | `obj` | Generic Data | item | Objeto de geometría o texto del que obtener el hash. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hash String | `Hash` | Generic Data | item | Texto del hash SHA. |

### Serialize Geometry (Serialize)

Serializa geometría de Grasshopper a formatos de texto (JSON, XML o binario).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `Geo` | Generic Data | item | Objeto de geometría a serializar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Serialized Text | `Text` | Generic Data | item | Texto (JSON, XML o binario) obtenido del objeto de Rhino. |

## Structure

### 2D Truss (Truss)

Crea una cercha 2D a partir de un conjunto de curvas de borde.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `CrvA` | Curve | item | Curva que define el borde superior de la cercha. |
| Curve B | `CrvB` | Curve | item | Curva que define el borde inferior de la cercha. |
| Divisions | `N` | Integer | item | Cantidad de divisiones |
| Truss Toggle | `T` | Integer | item | Alterna entre configuraciones del alma de la cercha. 0 = alma en dos direcciones, 1 = alma en una dirección, 2 = alma en una dirección invertida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Lines | `LinesA` | Generic Data | item | Ejes de la estructura principal. |
| Brace Lines | `LinesB` | Generic Data | item | Ejes de la estructura de arriostramiento. |
| Vertical Lines | `LinesC` | Generic Data | item | Ejes de la estructura vertical. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

### Braced Grid 1-D Structure (GridBraced1D)

Crea una estructura de grilla arriostrada en 1 dirección sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Lines | `LinesA` | Generic Data | item | Ejes de la estructura principal. |
| Brace Lines | `LinesB` | Generic Data | item | Ejes de la estructura de arriostramiento. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

### Braced Grid 2-D Structure (GridBraced2D)

Crea una estructura de grilla arriostrada en 2 direcciones sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Lines | `LinesA` | Generic Data | item | Ejes de la estructura principal. |
| Brace Lines | `LinesB` | Generic Data | item | Ejes de la estructura de arriostramiento. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

### Diagrid Structure (Diagrid)

Crea una estructura diagrid sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| Type | `T` | Boolean | item | Alterna el tipo de diagrid. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Structure Lines | `Lines` | Generic Data | item | Ejes de la estructura. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

### Grid Structure (Grid)

Crea una estructura de grilla simple sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Structure Lines | `Lines` | Generic Data | item | Ejes de la estructura. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

### Hexagonal Structure (Hex)

Crea una estructura hexagonal sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| Adjust Shape | `A` | Number | item | Ajusta la forma del hexágono. |
| Type | `T` | Boolean | item | Alterna el tipo de grilla hexagonal. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Structure Lines | `Lines` | Generic Data | item | Ejes de la estructura. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

### Space Truss Structure 1 (SpaceTruss 1)

Crea una estructura de cercha espacial sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a panelizar |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |
| Truss Depth | `D` | Number | item | La altura (peralte) de la cercha. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Lines | `LinesA` | Generic Data | item | Ejes de la estructura principal. |
| Primary Lines | `LinesB` | Generic Data | item | Ejes de la estructura principal. |
| Web Lines | `Web` | Generic Data | item | Ejes de la estructura del alma. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

### Space Truss Structure 2 (SpaceTruss 2)

Crea una estructura de cercha espacial a partir de dos superficies guía

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface A | `Srf-A` | Surface | item | La primera superficie de la cercha espacial. |
| Surface B | `Srf-B` | Surface | item | La segunda superficie de la cercha espacial. |
| U Divisions | `U` | Integer | item | Divisiones en la dirección U de la superficie. |
| V Divisions | `V` | Integer | item | Divisiones en la dirección V de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Primary Lines | `LinesA` | Generic Data | item | Ejes de la estructura principal. |
| Primary Lines | `LinesB` | Generic Data | item | Ejes de la estructura principal. |
| Web Lines | `Web` | Generic Data | item | Ejes de la estructura del alma. |
| Structure Nodes | `Nodes` | Generic Data | item | Nodos de conexión de la estructura. |

## Util

### Arc Divide (ArcDivide)

Divide una curva spline en segmentos de arco tangentes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Una curva spline a dividir en arcos. |
| t Parameters | `t` | Number | lista | Una lista de parámetros 't' |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arcs | `Arcs` | Generic Data | item | Segmentos de arco |
| Centers | `Centers` | Generic Data | item | Centros de los arcos. |

### Brep Join Progression (BrepJoin)

Une progresivamente caras de Brep con un valor de tolerancia. Las caras se unen progresivamente en el orden en que se entregan.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `Brep` | Brep | lista | Lista de Breps a unir. |
| Tolerance | `tol` | Number | item | Tolerancia de distancia 3D para detectar aristas superpuestas. |
| Compact | `compact` | Boolean | item | Si es True, define las marcas y tolerancias del brep y quita caras y aristas no usadas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `Brep` | Generic Data | item | Geometría Brep unida. |

### Brep Join with Tolerance (BrepJoin)

Une caras de Brep con un valor de tolerancia.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `Brep` | Brep | lista | Lista de Breps a unir. |
| Tolerance | `tol` | Number | item | Tolerancia de distancia 3D para detectar aristas superpuestas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `Brep` | Generic Data | item | Geometría Brep unida. |

### Create RTree (RTree)

Crea un RTree en el que se puede buscar

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Input geometry | `Geo` | Generic Data | lista | Geometría de entrada para crear el RTree (lista de puntos, malla o PointCloud) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| RTree | `RTree` | Generic Data | lista | El RTree calculado para búsquedas rápidas |

### Deconstruct Wireframe (DeWire)

Organiza una estructura de curvas en alambre en nodos y ejes

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Crvs` | Curve | lista | Red de curvas a organizar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Nodes | `Nodes` | Generic Data | item | Lista de nodos. |
| Curve Definition | `CrvDef` | Generic Data | item | Definición de cada curva por los índices de sus puntos extremos. |

### Flatness Check (Flat)

Revisa la planitud de un panel cuadrangular.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Panel List | `Panels` | Surface | lista | Una lista de paneles cuadrangulares a revisar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Flat Panels | `F` | Generic Data | item | Proyecciones planas de los paneles |
| Planes | `P` | Generic Data | item | Planos de proyección |
| Deviations | `D` | Generic Data | item | Cantidad de desviación de planitud. |

### Patch Surface (Patch)

Devuelve una superficie de parche (patch) a partir de una lista de curvas de borde. (Solo Rhino 5)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge Curves | `Crvs` | Curve | lista | Curvas de borde que definen el parche. |
| U | `U` | Integer | item | Tramos U del parche. |
| V | `V` | Integer | item | Tramos V del parche. |
| Tolerance | `t` | Number | item | Tolerancia del parche. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Patch Surface | `Patch` | Generic Data | item | Una superficie de parche. |

### Random Split List (RandomSplit)

Divide al azar una lista en dos listas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Master List | `L` | Generic Data | lista | Una lista a dividir al azar. |
| Seed | `R` | Integer | item | Valor semilla aleatorio. |
| Split | `S` | Number | item | Un valor entre 0 y 1. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List A | `A` | Generic Data | item | Lista A después de la división. |
| List B | `B` | Generic Data | item | Lista B después de la división. |

### Rebuild Surface (RebuildSrf)

Reconstruye una superficie sin recortar usando parámetros U y V.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a reconstruir. |
| U Degree | `uDeg` | Integer | item | Grado en la dirección U |
| V Degree | `vDeg` | Integer | item | Grado en la dirección V |
| U Number | `U` | Integer | item | Cantidad de puntos en la dirección U. |
| V Number | `V` | Integer | item | Cantidad de puntos en la dirección V. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rebuilt Surface | `RebSrf` | Generic Data | item | La superficie reconstruida resultante. |

### Relative Coordinates (Relative)

Devuelve las coordenadas de un punto respecto de un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pln` | Plane | item | Un plano respecto del cual medir la coordenada. |
| Point | `Pt` | Point | item | Un punto del que obtener las coordenadas relativas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Relative Point | `rPt` | Generic Data | item | El punto relativo usando el plano del mundo. |
| Relative X | `rX` | Generic Data | item | La ubicación X relativa. |
| Relative Y | `rY` | Generic Data | item | La ubicación Y relativa. |
| Relative Z | `rZ` | Generic Data | item | La ubicación Z relativa. |

### Reverse Surface Direction (RevSrf)

Invierte las direcciones UV de una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `Srf` | Surface | item | Una superficie a invertir. |
| Reverse Option | `R` | Integer | item | 0=no hacer nada, 1=invertir U, 2=invertir V, 3=invertir UV |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reversed Surface | `RevSrf` | Generic Data | item | La superficie invertida resultante. |

### RTree Closest Point (RTree CP)

Busca el punto más cercano en un RTree a partir de puntos de búsqueda

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Search Points | `SPoints` | Point | árbol | Puntos desde los que buscar |
| RTree | `RTree` | Generic Data | árbol | El RTree en el que buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closest Point | `CPoint` | Point | árbol | El punto más cercano del RTree |
| Closest Index | `Index` | Integer | árbol | El índice del punto más cercano del RTree |

### RTree Points in Range (RTree Range)

Busca los puntos de un RTree que están dentro de un rango de los puntos de búsqueda

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Search Points | `SPoints` | Point | árbol | Puntos desde los que buscar |
| Search Distance | `Distance` | Number | árbol | Distancias de búsqueda |
| RTree | `RTree` | Generic Data | árbol | El RTree en el que buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points within Range | `RPoints` | Point | árbol | Los puntos del RTree dentro del rango de los puntos de búsqueda |
| Indices within Range | `Indices` | Integer | árbol | Los índices de los puntos del RTree dentro del rango de los puntos de búsqueda |

### Shell Brep (Shell)

Crea un cascarón hueco a partir de un Brep sólido

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Solid Brep | `Brep` | Brep | item | Un Brep sólido al que hacer el vaciado (shell) |
| Face Indices | `FaceInd` | Integer | lista | Los índices de las caras a quitar. |
| Shell Thickness | `Thickness` | Number | item | El espesor del shell. |
| Tolerance | `tol` | Number | item | Tolerancia de distancia 3D para detectar aristas superpuestas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell Brep | `Shell` | Generic Data | item | El brep vaciado |

### Shortest Walk (Walk)

Busca el "camino más corto" (Shortest Walk) dentro de una red de curvas. Este nodo usa código actualizado escrito originalmente por Giulio Piacentino de McNeel and Associates. https://www.food4rhino.com/en/app/shortest-walk-gh

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve Network | `Crvs` | Curve | lista | Red de curvas a organizar. |
| Lengths | `Lengths` | Number | lista | Una lista de longitudes para cada segmento de curva. No tiene que ser la longitud real si quieres ponderar las curvas. |
| Path Lines | `Paths` | Line | lista | Una lista de líneas de recorrido que definen el inicio y el final del camino. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shortest Walk | `Walk` | Generic Data | item | El camino más corto. |
| Links | `Links` | Generic Data | item | Enlaces resultantes. |
| Directions | `Directions` | Generic Data | item | Direcciones resultantes. |
| Lengths | `Lengths` | Generic Data | item | Longitudes resultantes. |

### Sort Adjacent Brep Faces (Adjacent)

Devuelve una estructura ordenada de caras de Brep adyacentes a otras caras.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `Brep` | Brep | árbol | Un brep en el que analizar las caras adyacentes. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep Face | `Face` | Generic Data | item | Lista de caras del brep |
| Adjecent Faces | `Adjacent` | Generic Data | item | Una lista de caras adyacentes para cada cara del brep |
| Adjecent Faces Indeces | `AdjIndex` | Generic Data | item | Una lista de índices de caras adyacentes para cada cara del brep. |
| Adjecency Matrix | `Matrix` | Generic Data | item | Matriz de adyacencia cruzada True/False para cada cara del brep. |

### Sort Duplicate Breps (Sort Brep)

Ordena una lista de Breps según sus duplicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `Breps` | Brep | lista | Lista de Breps en la que buscar duplicados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unique Breps | `Unique` | Generic Data | item | Lista de Breps únicos. |
| Indices | `Indices` | Generic Data | item | Índices ordenados. |

### Sort Duplicate Curves (Sort Crv)

Ordena una lista de curvas según sus duplicados, usando las tolerancias del documento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Crvs` | Curve | lista | Lista de curvas en la que buscar duplicados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unique Curves | `Unique` | Generic Data | item | Lista de curvas únicas. |
| Indices | `Indices` | Generic Data | item | Índices ordenados. |

### Sort Duplicate Points (Sort Pts)

Ordena una lista de puntos según sus duplicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `Pts` | Point | lista | Lista de puntos en la que buscar duplicados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unique Points | `Unique` | Generic Data | item | Lista de puntos únicos. |
| Indices | `Indices` | Generic Data | item | Índices ordenados. |

### Sort Duplicate Values (Sort Val)

Ordena una lista de números o textos según sus duplicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value List | `Values` | Text | árbol | Lista de números o textos en la que buscar duplicados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unique Values | `Unique` | Generic Data | item | Valores únicos de una lista. |
| Indices | `Indices` | Generic Data | item | Índices ordenados. |

### String Distance (Str Dist)

Evalúa la "distancia" (diferencia) entre dos textos con el algoritmo de Levenshtein. Una distancia de 0 indica que los textos coinciden perfectamente. Valores más altos indican más diferencia entre los textos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| String A | `StrA` | Text | item | Un texto. |
| String B | `StrB` | Text | item | Un texto con el que comparar. |
| To Lowercase | `ToLower` | Boolean | item | Pasa los textos a minúsculas para calcular la distancia. |
| Remove Spaces | `removeSpaces` | Boolean | item | Quita los espacios de los textos para calcular la distancia. |
| Remove Substrings | `removeSubStrings` | Boolean | item | Quita subtextos de los textos para la comparación. |
| Substrings | `Substrings` | Text | lista | Una lista de subtextos a quitar de los textos de origen. Útil para quitar caracteres innecesarios al calcular la distancia. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Distance Score | `Score` | Generic Data | item | La distancia. 0 indica que los textos coinciden perfectamente. Cuanto más alto el número, mayor la distancia (diferencia) entre los textos |

### Unroll Brep (Unroll)

Desenrolla un brep o una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `Brep` | Brep | item | El Brep o la superficie a desenrollar. |
| Join Unrolled | `Join` | Boolean | item | ¿Unir las piezas desenrolladas del Brep? |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Unrolled Brep | `Unrolled` | Generic Data | item | La superficie o Brep desenrollado. |

## Workflow

### Create Layers (Layer)

Crea una lista de capas en Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Create Toggle | `Create` | Boolean | item | Activa la creación de capas. |
| Layer Names | `Names` | Text | item | Una lista de nombres de capas. |
| Layer Colors | `Colors` | Colour | item | Una lista de colores de capas. |

### Excel Reader (ExcelRead)

Lee un archivo de Excel abierto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Read Excel Data | `Read` | Boolean | item | Poner en 'True' para leer información de un archivo de Excel abierto. |
| Workbook Path | `Path` | Text | item | La ruta del libro de Excel. |
| Worksheet Name | `Worksheet` | Text | item | El nombre de la hoja en la que escribir. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Exceptions | `out` | Generic Data | item | Muestra los mensajes de error o de éxito. |
| Column Header Names | `Headers` | Generic Data | item | Nombres de los encabezados de columna. |
| Excel Data | `Data` | Generic Data | item | Datos de la planilla de Excel. |

### Excel Writer (ExcelWrite)

Escribe en un archivo de Excel abierto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Write Excel Data | `Write` | Boolean | item | Poner en 'True' para escribir información en un archivo de Excel abierto. |
| Workbook Path | `Path` | Text | item | La ruta del libro de Excel. |
| Worksheet Name | `Worksheet` | Text | item | El nombre de la hoja en la que escribir. |
| Column Headings | `Headings` | Text | lista | Los encabezados de columna. |
| Data | `Data` | Text | árbol | Datos organizados como ramas de un árbol de datos. (Por defecto, las ramas se tratan como columnas.) |
| Clear Sheet | `Clear` | Boolean | item | Poner en 'True' para borrar la información existente en la hoja. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Exceptions | `out` | Generic Data | item | Muestra los mensajes de error o de éxito. |

### Launch Application (LaunchApp)

Abre una aplicación o un archivo externo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Launch Toggle | `Launch` | Boolean | item | Poner en 'True' para leer información de un archivo de Excel abierto. |
| Application Path | `Path` | Text | item | La ruta de la aplicación o del archivo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Exceptions | `out` | Generic Data | item | Muestra los mensajes de error o de éxito. |

### Layer Information (Layer Info)

Obtiene información de las capas del documento actual.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reference Toggle | `Toggle` | Boolean | item | Activa la referencia de objetos por capa. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Names | `Names` | Generic Data | item | Nombre de las capas. |
| Display Colors | `Colors` | Generic Data | item | Color de visualización de la capa. |
| GUID | `ID` | Generic Data | item | Nombre de las capas. |

### Layer Reference (Layer Ref)

Referencia geometría de capas con sus GUID y nombres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Reference Toggle | `Toggle` | Boolean | item | Activa la referencia de objetos por capa. |
| Layer Name | `Layer` | Text | lista | El nombre de la capa a referenciar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `Geo` | Generic Data | item | Geometría de la capa |
| Name | `Name` | Generic Data | item | Nombre de la geometría |
| Color | `Color` | Generic Data | item | Color del objeto |
| User String Keys | `UserKeys` | Generic Data | item | Claves de texto de usuario asignadas al objeto. |
| User String Values | `UserValues` | Generic Data | item | Valores de texto de usuario asignados al objeto. |
| GUID | `ID` | Generic Data | item | El GUID de la geometría. |

### Object Bake (Bake)

Hace bake de objetos en una capa del documento activo de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bake Toggle | `Bake` | Boolean | item | Poner en 'True' para hacer bake de los objetos. |
| Geometry Objects | `Objects` | Generic Data | item | Geometría a la que hacer bake. |
| Layer | `Layer` | Text | item | Hace bake de la geometría en una capa. |
| Object Name | `ObjName` | Text | item | Nombre del objeto de geometría. |
| Object Color | `ObjColor` | Colour | item | Color del objeto de geometría. |
| Layer Color | `LayerColor` | Colour | item | Color de la capa de la geometría. |
| User String | `UserStrings` | Text | lista | Datos de texto de usuario del objeto. |
| User Keys | `UserKeys` | Text | lista | Claves únicas correspondientes a los textos de usuario. |

### Object Save (Save)

Guarda geometría en una ubicación de archivo indicada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bake Toggle | `Bake` | Boolean | item | Poner en 'True' para hacer bake de los objetos. |
| File Directory | `Dir` | Text | item | Carpeta de destino del archivo |
| File Name | `File` | Text | lista | Nombre del archivo con extensión (*.3dm, *.dwg, *.sat, *.stl, *.obj, etc.). |
| Geometry Objects | `Objects` | Generic Data | lista | Geometría a guardar. |
| Layer | `Layer` | Text | item | Hace bake de la geometría en una capa. |
| Object Name | `objName` | Text | item | Nombre del objeto de geometría. |
| Object Color | `objColor` | Colour | item | Color del objeto de geometría. |
| Layer Color | `layerColor` | Colour | item | Color de la capa de la geometría. |

### Rhino Command (RhCOM)

Envía un comando a la línea de comandos de Rhino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Send Command Toggle | `Send` | Boolean | item | Poner en 'True' para enviar un comando. |
| Command String | `Command` | Text | item | El comando a ejecutar. |

### Text Reader (Reader)

Lee un flujo de texto desde un archivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Read Toggle | `Read` | Boolean | item | Si está en 'True', lee desde el archivo. |
| File Path | `Path` | Text | item | La ruta de un archivo de texto a leer. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `Text` | Generic Data | item | Valores de texto del archivo. |

### Text Writer (Writer)

Escribe un flujo de texto en un archivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Write Toggle | `Write` | Boolean | item | Si está en 'True', escribe en el archivo. |
| File Path | `Path` | Text | item | La ruta donde guardar el flujo de texto. |
| Text Stream | `Text` | Text | árbol | Un flujo de texto a escribir en un archivo. Los elementos de listas y árboles se escriben como filas nuevas en el archivo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Exceptions | `out` | Generic Data | item | Muestra los mensajes de error o de éxito. |
