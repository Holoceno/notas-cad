---
title: "Catálogo Grasshopper — Surface"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Surface"
libraries: ["Curve Components 8.35.26251.13001", "Kangaroo2 Components 2.5.3", "Surface Components 8.35.26251.13001", "Transform Components 8.35.26251.13001", "Triangulation Components 8.35.26251.13001", "Vector Components 8.35.26251.13001"]
components: 93
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/kangaroo, geometria/superficies, geometria/brep, geometria/mallas]
---

# Surface

93 objetos · librería: Curve Components 8.35.26251.13001, Kangaroo2 Components 2.5.3, Surface Components 8.35.26251.13001, Transform Components 8.35.26251.13001, Triangulation Components 8.35.26251.13001, Vector Components 8.35.26251.13001 · autor: Daniel Piker, Robert McNeel & Associates

Mapas: [[Mapa - Superficies y NURBS]] (83) · [[Mapa - Brep y sólidos]] (34) · [[Mapa - Mallas y SubD]] (10)

## Analysis

### Area

Calcula las propiedades de área de breps, mallas y curvas planas cerradas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Brep, malla o curva plana cerrada para calcular el área |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Area | `A` | Number | item | Área de la geometría |
| Centroid | `C` | Point | item | Centroide del área de la geometría |

### Area Moments (AMoments)

Calcula los momentos de área de breps, mallas y curvas planas cerradas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Brep, malla o curva plana cerrada para calcular el área |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Area | `A` | Number | item | Área de la geometría |
| Centroid | `C` | Point | item | Centroide del volumen de la geometría |
| Inertia | `I` | Vector | item | Momentos de inercia respecto del centroide |
| Secondary | `S` | Vector | item | Momentos de inercia secundarios respecto del centroide |
| Gyration | `G` | Vector | item | Radios de giro |

### Box Corners

Extrae las 8 esquinas de una caja.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Point | item | Esquina en {x=mín, y=mín, z=mín} |
| Corner B | `B` | Point | item | Esquina en {x=máx, y=mín, z=mín} |
| Corner C | `C` | Point | item | Esquina en {x=máx, y=máx, z=mín} |
| Corner D | `D` | Point | item | Esquina en {x=mín, y=máx, z=mín} |
| Corner E | `E` | Point | item | Esquina en {x=mín, y=mín, z=máx} |
| Corner F | `F` | Point | item | Esquina en {x=máx, y=mín, z=máx} |
| Corner G | `G` | Point | item | Esquina en {x=máx, y=máx, z=máx} |
| Corner H | `H` | Point | item | Esquina en {x=mín, y=máx, z=máx} |

### Box Properties (BoxProp)

Obtiene algunas propiedades de una caja

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja a analizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center | `C` | Point | item | Punto central de la caja |
| Diagonal | `D` | Vector | item | Vector diagonal de la caja |
| Area | `A` | Number | item | Área de la caja |
| Volume | `V` | Number | item | Volumen de la caja |
| Degeneracy | `d` | Integer | item | Degeneración de la caja |

### Brep Closest Point (Brep CP)

Busca el punto más cercano en un brep

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de muestra |
| Brep | `B` | Brep | item | Brep base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto más cercano |
| Normal | `N` | Vector | item | Dirección normal en el punto más cercano |
| Distance | `D` | Number | item | Distancia entre el punto de muestra y el Brep |

### Brep Edges (Edges)

Extrae las curvas de arista de un brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Naked | `En` | Curve | lista | Curvas de arista desnudas |
| Interior | `Ei` | Curve | lista | Curvas de arista interiores |
| Non-Manifold | `Em` | Curve | lista | Curvas de arista no manifold |

### Brep Topology (Topology)

Obtiene y muestra la topología de un brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Face\|Face Adjacency | `FF` | Integer | árbol | Para cada cara, lista todas las caras que la rodean. |
| Face\|Edge Adjacency | `FE` | Integer | árbol | Para cada cara, lista todas las aristas que la rodean. |
| Edge\|Face Adjacency | `EF` | Integer | árbol | Para cada arista, lista todas las caras que la rodean. |

### Brep Wireframe (Wires)

Extrae las curvas de alambre (wireframe) de un brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep base |
| Density | `D` | Integer | item | Densidad de isocurvas del wireframe |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Wireframe | `W` | Curve | lista | Curvas del wireframe |

### Deconstruct Box (DeBox)

Descompone una caja en sus partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano de la caja |
| X | `X` | Domain | item | Dimensión {x} de la caja |
| Y | `Y` | Domain | item | Dimensión {y} de la caja |
| Z | `Z` | Domain | item | Dimensión {z} de la caja |

### Deconstruct Brep (DeBrep)

Descompone un brep en sus partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Faces | `F` | Surface | lista | Caras del Brep |
| Edges | `E` | Curve | lista | Aristas del Brep |
| Vertices | `V` | Point | lista | Vértices del Brep |

### Dimensions (Dim)

Obtiene las dimensiones aproximadas de una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a medir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U dimension | `U` | Number | item | Dimensión aproximada en la dirección U |
| V dimension | `V` | Number | item | Dimensión aproximada en la dirección V |

### Evaluate Box (Box)

Evalúa una caja en el espacio normalizado {UVW}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja base |
| U parameter | `U` | Number | item | Parámetro {u} (los valores entre 0.0 y 1.0 están dentro de la caja) |
| V parameter | `V` | Number | item | Parámetro {v} (los valores entre 0.0 y 1.0 están dentro de la caja) |
| W parameter | `W` | Number | item | Parámetro {w} (los valores entre 0.0 y 1.0 están dentro de la caja) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `Pl` | Plane | item | Plano en la coordenada {uvw} |
| Point | `Pt` | Point | item | Punto en la coordenada {uvw} |
| Include | `I` | Boolean | item | True si el punto está dentro o sobre la caja |

### Evaluate Surface (EvalSrf)

Evalúa las propiedades locales de una superficie en una coordenada {uv}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Point | `uv` | Point | item | Coordenada {uv} a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en {uv} |
| Normal | `N` | Vector | item | Normal en {uv} |
| U direction | `U` | Vector | item | Dirección U en {uv} |
| V direction | `V` | Vector | item | Dirección V en {uv} |
| Frame | `F` | Plane | item | Marco en {uv} |

### Is Planar (Planar)

Prueba si una superficie es plana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a probar si es plana |
| Interior | `I` | Boolean | item | Limita la prueba de planaridad al interior de las superficies recortadas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar | `F` | Boolean | item | Indicador de planaridad de la superficie |
| Plane | `P` | Plane | item | Plano de la superficie |

### Osculating Circles (Osc)

Calcula los círculos osculadores principales de una superficie en una coordenada {uv}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Point | `uv` | Point | item | Coordenada {uv} a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de la superficie en la coordenada {uv} |
| First circle | `C1` | Curve | item | Primer círculo osculador |
| Second circle | `C2` | Curve | item | Segundo círculo osculador |

### Point In Brep (BrepInc)

Prueba si un punto está dentro de un brep cerrado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep para la prueba de inclusión |
| Point | `P` | Point | item | Punto para la prueba de inclusión |
| Strict | `S` | Boolean | item | Si es True, la inclusión es estricta |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inside | `I` | Boolean | item | True si el punto está dentro del Brep. |

### Point In Breps (BrepsInc)

Prueba si un punto está dentro de una colección de breps cerrados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | lista | Breps para la prueba de inclusión |
| Point | `P` | Point | item | Punto para la prueba de inclusión |
| Strict | `S` | Boolean | item | Si es True, la inclusión es estricta |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inside | `I` | Boolean | item | True si el punto está dentro de al menos uno de los Breps. |
| Index | `i` | Integer | item | Índice del primer brep que contiene el punto, o -1 |

### Point In Trim (TrimInc)

Prueba si una coordenada {uv} está dentro de la parte recortada de una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| UV Point | `P` | Point | item | Punto UV a probar si está dentro del recorte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inclusion | `I` | Boolean | item | Indicador de inclusión. True si el punto está dentro de los bordes de recorte. |

### Principal Curvature (Curvature)

Evalúa la curvatura principal de una superficie en una coordenada {uv}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Point | `uv` | Point | item | Coordenada {uv} a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame | `F` | Plane | item | Marco de la superficie en la coordenada (uv) |
| Maximum | `C¹` | Number | item | Curvatura principal máxima (absoluta) |
| Minimum | `C²` | Number | item | Curvatura principal mínima (absoluta) |
| Max direction | `K¹` | Vector | item | Dirección de curvatura principal correspondiente a C¹. |
| Min direction | `K²` | Vector | item | Dirección de curvatura principal correspondiente a C². |

### Shape In Brep (ShapeIn)

Prueba si una forma está dentro de un brep

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep cerrado para la prueba dentro/fuera |
| Shape | `S` | Geometry | item | Forma para la prueba dentro/fuera |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Relation | `R` | Integer | item | Relación de la forma con el brep (0=dentro, 1=intersecta, 2=fuera) |

### Surface Closest Point (Srf CP)

Busca el punto más cercano en una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de muestra |
| Surface | `S` | Surface | item | Superficie base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto más cercano |
| UV Point | `uvP` | Point | item | Coordenadas {uv} del punto más cercano |
| Distance | `D` | Number | item | Distancia entre el punto de muestra y la superficie |

### Surface Curvature (Curvature)

Evalúa la curvatura de la superficie en una coordenada {uv}.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Point | `uv` | Point | item | Coordenada {uv} a evaluar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame | `F` | Plane | item | Marco de la superficie en la coordenada {uv} |
| Gaussian | `G` | Number | item | Curvatura gaussiana |
| Mean | `M` | Number | item | Curvatura media |

### Surface Points (SrfPt)

Obtiene los puntos de control de una superficie NURBS

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie de la que extraer los puntos de control |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Ubicaciones de los puntos de control |
| Weights | `W` | Number | lista | Pesos de los puntos de control |
| Greville | `G` | Point | lista | Puntos uv de Greville |
| U Count | `U` | Integer | item | Cantidad de puntos en la dirección U |
| V Count | `V` | Integer | item | Cantidad de puntos en la dirección V |

### Volume

Calcula las propiedades de volumen de breps y mallas cerrados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Brep o malla cerrados para calcular el volumen |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Volume | `V` | Number | item | Volumen de la geometría |
| Centroid | `C` | Point | item | Centroide del volumen de la geometría |

### Volume Moments (VMoments)

Calcula las propiedades de volumen de breps y mallas cerrados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Brep o malla cerrados para calcular el volumen |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Volume | `V` | Number | item | Volumen de la geometría |
| Centroid | `C` | Point | item | Centroide del volumen de la geometría |
| Inertia | `I` | Vector | item | Momentos de inercia respecto del centroide |
| Secondary | `S` | Vector | item | Momentos de inercia secundarios respecto del centroide |
| Gyration | `G` | Vector | item | Radios de giro |

## Freeform

### 4Point Surface (Srf4Pt)

Crea una superficie que une tres o cuatro puntos de esquina.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Point | item | Primera esquina |
| Corner B | `B` | Point | item | Segunda esquina |
| Corner C | `C` | Point | item | Tercera esquina |
| Corner D *(opcional)* | `D` | Point | item | Cuarta esquina (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie resultante |

### Boundary Surfaces (Boundary)

Crea superficies planas a partir de una colección de curvas de borde.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Curvas de borde |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surfaces | `S` | Surface | lista | Superficies de borde resultantes |

### Control Point Loft (CPLoft)

Crea un loft a través de los puntos de control de las curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de sección |
| Degree | `D` | Integer | item | Grado perpendicular a la dirección de las curvas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Resultado del loft |

### Edge Surface (EdgeSrf)

Crea una superficie a partir de dos, tres o cuatro curvas de borde.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva |
| Curve B | `B` | Curve | item | Segunda curva |
| Curve C *(opcional)* | `C` | Curve | item | Tercera curva (opcional) |
| Curve D *(opcional)* | `D` | Curve | item | Cuarta curva (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Brep que representa la superficie de bordes |

### Extrude (Extr)

Extruye puntos, curvas y superficies a lo largo de un vector.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Geometry | item | Superficie de perfil |
| Direction | `D` | Vector | item | Dirección de extrusión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extrusion | `E` | Geometry | item | Resultado de la extrusión |

### Extrude Along (ExtrCrv)

Extruye curvas y superficies a lo largo de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Geometry | item | Curva o superficie de perfil |
| Curve | `C` | Curve | item | Curva de extrusión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extrusion | `E` | Brep | item | Resultado de la extrusión |

### Extrude Linear (Extrude)

Extruye curvas y superficies a lo largo de un camino recto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Profile | `P` | Geometry | item | Curva o superficie de perfil |
| Orientation (P) | `Po` | Plane | item | Plano que indica la orientación del perfil |
| Axis | `A` | Line | item | Eje de extrusión |
| Orientation (A) *(opcional)* | `Ao` | Plane | item | Plano de orientación opcional para el eje |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extrusion | `E` | Brep | item | Resultado de la extrusión |

### Extrude Point (Extr)

Extruye curvas y superficies hasta un punto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Geometry | item | Curva o superficie de perfil |
| Point | `P` | Point | item | Punta de la extrusión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Extrusion | `E` | Brep | item | Resultado de la extrusión |

### Fit Loft (FitLoft)

Crea un loft ajustado a un conjunto de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de sección |
| Count U | `Nu` | Integer | item | Cantidad de puntos en la dirección de las curvas |
| Degree U | `Du` | Integer | item | Grado en la dirección de las curvas |
| Degree V | `Dv` | Integer | item | Grado perpendicular a la dirección de las curvas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Resultado del loft |

### Fragment Patch (FPatch)

Crea un parche fragmentado a partir de un borde de polilínea

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundary | `B` | Curve | item | Borde de polilínea del fragmento |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Patch | `P` | Brep | item | Parche fragmentado |

### Loft

Crea una superficie con loft a través de un conjunto de curvas de sección.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de sección |
| Options | `O` | Loft Options | item | Opciones de loft |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Loft | `L` | Brep | item | Superficies de loft resultantes |

### Loft Options (Loft Opt)

Crea opciones de loft a partir de entradas individuales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Closed | `Cls` | Boolean | item | Loft cerrado |
| Adjust | `Adj` | Boolean | item | Ajustar costuras |
| Rebuild | `Rbd` | Integer | item | Cantidad de reconstrucción (cero = sin reconstruir) |
| Refit | `Rft` | Number | item | Tolerancia de reajuste (cero = sin reajustar) |
| Type | `T` | Integer | item | Tipo de loft (0=normal, 1=holgado, 2=ajustado, 3=recto, 5=uniforme) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Options | `O` | Loft Options | item | Opciones de loft |

### Network Surface (NetSurf)

Crea una superficie a partir de redes de curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves U | `U` | Curve | lista | Curvas en la dirección U |
| Curves V | `V` | Curve | lista | Curvas en la dirección V |
| Continuity | `C` | Integer | item | Continuidad de la superficie (0=holgada, 1=posición, 2=tangencia, 3=curvatura) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie de red |

### Patch

Crea una superficie de parche (patch)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves *(opcional)* | `C` | Curve | lista | Curvas para el parche |
| Points *(opcional)* | `P` | Point | lista | Puntos para el parche |
| Spans | `S` | Integer | item | Cantidad de tramos |
| Flexibility | `F` | Number | item | Flexibilidad del parche (número bajo = menos flexibilidad) |
| Trim | `T` | Boolean | item | Intenta recortar el resultado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Patch | `P` | Surface | item | Resultado del parche |

### Pipe

Crea una superficie de tubería alrededor de una curva de riel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva base |
| Radius | `R` | Number | item | Radio de la tubería |
| Caps | `E` | Integer | item | Indica el tipo de tapas (0=ninguna, 1=plana, 2=redonda) |
| Fit Rail | `Fr` | Boolean | item | Si la curva de riel es una policurva de líneas y arcos, la curva se ajusta y se crea una sola superficie; si no, el resultado es un Brep de superficies unidas creadas a partir de los segmentos de la policurva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pipe | `P` | Brep | lista | Tubería resultante |

### Pipe Variable (VPipe)

Crea una superficie de tubería con radios variables alrededor de una curva de riel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva base |
| Parameters | `t` | Number | lista | Parámetros de la curva para los radios |
| Radii | `R` | Number | lista | Una lista de radios para cada parámetro definido |
| Caps | `E` | Integer | item | Indica el tipo de tapas (0=ninguna, 1=plana, 2=redonda) |
| Fit Rail | `Fr` | Boolean | item | Si la curva de riel es una policurva de líneas y arcos, la curva se ajusta y se crea una sola superficie; si no, el resultado es un Brep de superficies unidas creadas a partir de los segmentos de la policurva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pipe | `P` | Brep | lista | Tubería resultante |

### Rail Revolution (RailRev)

Crea una superficie de revolución usando un riel de barrido.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `P` | Curve | item | Curva de perfil |
| Rail | `R` | Curve | item | Curva de riel |
| Axis | `A` | Line | item | Eje de revolución |
| Scale | `S` | Boolean | item | Escala la altura de la curva de perfil |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Brep que representa el resultado de Rail-Revolve. |

### Revolution (RevSrf)

Crea una superficie de revolución.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `P` | Curve | item | Curva de perfil |
| Axis | `A` | Line | item | Eje de revolución |
| Domain | `D` | Domain | item | Dominio angular (en radianes) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | Brep que representa el resultado de la revolución. |

### Ruled Surface (RuleSrf)

Crea una superficie entre dos curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva |
| Curve B | `B` | Curve | item | Segunda curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie reglada entre A y B |

### Sum Surface (SumSrf)

Crea una superficie de suma a partir de dos curvas de borde.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva |
| Curve B | `B` | Curve | item | Segunda curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Brep | item | BRep que representa la superficie de suma |

### Surface From Points (SrfGrid)

Crea una superficie NURBS a partir de una grilla de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Grilla de puntos |
| U Count | `U` | Integer | item | Cantidad de puntos en la dirección {u} |
| Interpolate | `I` | Boolean | item | Interpolar las muestras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie resultante |

### Sweep1 (Swp1)

Crea una superficie de barrido (sweep) con una curva de riel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rail | `R` | Curve | item | Curva de riel |
| Sections | `S` | Curve | lista | Curvas de sección |
| Miter | `M` | Integer | item | Tipo de inglete en los quiebres (0=ninguno, 1=recortar, 2=rotar) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `S` | Brep | lista | Brep resultante |

### Sweep2 (Swp2)

Crea una superficie de barrido (sweep) con dos curvas de riel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rail 1 | `R¹` | Curve | item | Primera curva de riel |
| Rail 2 | `R²` | Curve | item | Segunda curva de riel |
| Sections | `S` | Curve | lista | Curvas de sección |
| Same Height | `H` | Boolean | item | Crea un barrido (sweep) que mantiene la misma altura. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `S` | Brep | lista | Brep resultante |

## Primitive

### Bounding Box (BBox)

Calcula las cajas contenedoras orientadas de la geometría.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Content | `C` | Geometry | lista | Geometría a contener |
| Plane | `P` | Plane | item | Plano de orientación de la caja contenedora |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | lista | Caja contenedora alineada, en coordenadas del mundo |
| Box | `B` | Box | lista | Caja contenedora en coordenadas del plano de orientación |

### Box 2Pt (Box)

Crea una caja definida por dos puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primera esquina |
| Point B | `B` | Point | item | Segunda esquina |
| Plane | `P` | Plane | item | Plano base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja resultante |

### Box Rectangle (BoxRec)

Crea una caja definida por un rectángulo y una altura.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rectangle | `R` | Rectangle | item | Rectángulo base |
| Height | `H` | Domain | item | Altura de la caja |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja resultante |

### Center Box (Box)

Crea una caja centrada en un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| X | `X` | Number | item | Tamaño de la caja en la dirección {x}. |
| Y | `Y` | Number | item | Tamaño de la caja en la dirección {y}. |
| Z | `Z` | Number | item | Tamaño de la caja en la dirección {z}. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja resultante |

### Cone

Crea una superficie cónica

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| Radius | `R` | Number | item | Radio en la base del cono |
| Length | `L` | Number | item | Altura del cono |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cone | `C` | Surface | item | Cono resultante |
| Tip | `T` | Point | item | Punta del cono |

### Cylinder (Cyl)

Crea una superficie cilíndrica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| Radius | `R` | Number | item | Radio del cilindro |
| Length | `L` | Number | item | Altura del cilindro |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cylinder | `C` | Surface | item | Cilindro resultante |

### Domain Box (Box)

Crea una caja definida por un plano base y dominios de tamaño.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| X | `X` | Domain | item | Dominio de la caja en la dirección {x}. |
| Y | `Y` | Domain | item | Dominio de la caja en la dirección {y}. |
| Z | `Z` | Domain | item | Dominio de la caja en la dirección {z}. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `B` | Box | item | Caja resultante |

### Plane Surface (PlaneSrf)

Crea una superficie plana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano base de la superficie |
| X Size | `X` | Domain | item | Dimensiones en la dirección X |
| Y Size | `Y` | Domain | item | Dimensiones en la dirección Y |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Surface | item | Superficie plana resultante |

### Plane Through Shape (PxS)

Crea una superficie rectangular más grande que una forma dada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano de la superficie |
| Shape | `S` | Geometry | item | Forma a superar |
| Inflate | `I` | Number | item | Cantidad de ampliación del borde |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie plana resultante |

### Quad Sphere (QSph)

Crea un brep esférico formado por parches NURBS cuadrangulares.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| Radius | `R` | Number | item | Radio de la esfera |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sphere | `S` | Brep | item | Esfera de cuadriláteros resultante |

### Sphere (Sph)

Crea una superficie esférica.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| Radius | `R` | Number | item | Radio de la esfera |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sphere | `S` | Surface | item | Esfera resultante |

### Sphere 4Pt (Sph4Pt)

Crea una superficie esférica a partir de 4 puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point 1 | `P1` | Point | item | Primer punto |
| Point 2 | `P2` | Point | item | Segundo punto (no puede coincidir con P1) |
| Point 3 | `P3` | Point | item | Tercer punto (no puede ser colineal con P1 y P2) |
| Point 4 | `P4` | Point | item | Cuarto punto (no puede ser coplanar con P1, P2 y P3) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center | `C` | Point | item | Centro de la esfera |
| Radius | `R` | Number | item | Radio de la esfera |
| Sphere | `S` | Surface | item | Esfera ajustada a P1~P4 |

### Sphere Fit (SFit)

Ajusta una esfera a una colección 3D de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a ajustar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Center | `C` | Point | item | Centro de la esfera ajustada |
| Radius | `R` | Number | item | Radio de la esfera ajustada |
| Sphere | `S` | Surface | item | Superficie esférica |

## SubD

### Mesh from SubD (MeshSubD)

Obtiene la malla de aproximación de una SubD.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD |
| Density | `D` | Integer | item | Densidad de subdivisión [0-5] |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla aproximada |

### MultiPipe (MP)

Crea una tubería ramificada alrededor de una red de líneas/curvas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Curves` | Generic Data | lista | Las curvas para la tubería. También acepta mallas |
| NodeSize | `NodeSize` | Number | lista | Radio de la tubería. Si se entrega un valor, se aplica a todo. También puedes entregar una lista de radios, uno por cada punto de SizePoints |
| SizePoints *(opcional)* | `SizePoints` | Point | lista | Si entregas varios radios en NodeSize, estos puntos identifican qué nodo recibe qué radio. Si solo algunos nodos tienen su radio definido así, los valores se interpolan a lo largo de la forma |
| EndOffset | `EndOffset` | Number | item | La distancia del primer bucle de aristas respecto del nodo, como multiplicador de NodeSize. Si es cero, no se agrega un bucle intermedio, para dar una forma más suave. |
| StrutSize | `StrutSize` | Number | item | El tamaño de los puntales entre nodos como multiplicador de NodeSize. <1 da puntales que se afinan, >1 da puntales abombados |
| Segment | `Segment` | Number | item | Separación aproximada de los bucles de aristas a lo largo de cada puntal. Si es cero, no se agregan bucles adicionales |
| KinkAngle | `KinkAngle` | Number | item | Cuando la entrada 'Curves' son curvas suaves, define el ángulo máximo entre segmentos consecutivos al discretizarlas |
| CubeFit | `CubeFit` | Number | item | Si es >0, intenta ajustar un cubo en cada nodo. Debe ser un valor entre 0 y 1, donde 0 = nunca y 1 = siempre, según qué tan ortogonales sean las líneas conectadas. |
| Caps *(opcional)* | `Caps` | Integer | item | Opción de tapa: 0 = ninguna, 1 = redonda, 2 = plana |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pipe | `P` | SubD | item | SubD de tubería resultante |

### SubD Control Polygon (SubDPoly)

Extrae el polígono de control de una SubD.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de control |

### SubD Edge Tags (SubDTags)

Define las etiquetas de arista de una forma SubD.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD a modificar. |
| Tag | `T` | Text | item | Descriptor de etiqueta de arista. |
| Ids | `Ei` | Integer | lista | Identificadores de las aristas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | Forma SubD modificada. |

### SubD Edges (SubDEdges)

Extrae todos los datos de aristas de una SubD.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | lista | Líneas de las aristas |
| Edges | `E` | Curve | lista | Curvas de las aristas |
| Tags | `T` | Text | lista | Etiquetas de las aristas |
| Ids | `Ei` | Text | lista | Identificadores de las aristas |

### SubD from Mesh (SubDMesh)

Crea una SubD a partir de una malla de control

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de control |
| Creases | `Cr` | Integer | item | Opción de pliegues de la subdivisión |
| Corners | `Co` | Integer | item | Opción de esquinas de la subdivisión |
| Interpolate | `I` | Boolean | item | Interpolar los vértices de la malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD |

### SubD Fuse (Fuse)

Combina 2 objetos SubD

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD A | `A` | Mesh | item | Primer objeto SubD o malla a fusionar |
| SubD B | `B` | Mesh | item | Segundo objeto SubD o malla a fusionar |
| Boolean Option | `O` | Integer | item | Tipo de booleano: 0=unión, 1=intersección, 2=A-B, 3=B-A |
| Smoothing | `S` | Integer | item | Cantidad de pasos de suavizado a aplicar en la unión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fuse | `F` | SubD | item | Resultado fusionado |

### SubD To Brep (ToBrep)

Convierte una superficie de subdivisión en una polisuperficie equivalente formada por caras NURBS.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD |
| Packing | `P` | Boolean | item | Si es True, los parches NURBS adyacentes compatibles se empaquetan en uno. |
| Continuity | `Gx` | Integer | item | Manejo de la continuidad en los vértices extraordinarios: 0) Ninguno: los parches NURBS se usan tal cual. 1) G1: los parches se modifican para ser G1 en el vértice extraordinario. 2) G2: los parches se modifican para ser G2 en el vértice extraordinario. 3) G1x: los parches se modifican para ser G1 en el vértice extraordinario y tienden a acercarse a G1 en las aristas cercanas a él. 4) G1xx: los parches se modifican para ser G1 en el vértice extraordinario y G1 a lo largo de las aristas cercanas a él. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `Br` | Brep | item | Polisuperficie formada por parches NURBS. |

### SubD Vertex Tags (SubDVTags)

Define las etiquetas de vértice de una forma SubD.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD a modificar. |
| Tag | `T` | Text | item | Descriptor de etiqueta de vértice (S=suave, C=pliegue, L=esquina, D=dardo). |
| Ids | `Vi` | Integer | lista | Identificadores de los vértices. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | Forma SubD modificada. |

### SubD Vertices (SubDVerts)

Extrae todos los datos de vértices de una SubD.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| SubD | `S` | SubD | item | SubD |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Ubicaciones de los vértices en la red de control. |
| Ids | `Vi` | Text | lista | Identificadores de los vértices. |
| Tags | `T` | Text | lista | Tipo de etiquetas de vértice. |

## Util

### Brep Join (Join)

Une varios Breps

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | lista | Breps a unir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | lista | Breps unidos |
| Closed | `C` | Boolean | lista | Indicador de cerrado de cada Brep resultante |

### Cap Holes (Cap)

Tapa todos los agujeros planos de un Brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep a tapar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep tapado |

### Cap Holes Ex (CapEx)

Tapa la mayor cantidad posible de agujeros de un Brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep a tapar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep tapado |
| Caps | `C` | Integer | item | Cantidad de tapas agregadas |
| Solid | `S` | Boolean | item | Valor que indica si el brep tapado es sólido |

### Convex Edges (EdgesCvx)

Selecciona las aristas cóncavas o convexas de un brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep del que extraer las aristas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Convex | `Cv` | Integer | lista | Índices de las aristas completamente convexas |
| Concave | `Cc` | Integer | lista | Índices de las aristas completamente cóncavas |
| Mixed | `Mx` | Integer | lista | Índices de las aristas de concavidad mixta |

### Copy Trim (Trim)

Copia los datos de recorte UV de una superficie a otra.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Source | `S` | Surface | item | Superficie de origen |
| Target | `T` | Surface | item | Superficie objetivo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie recortada de nuevo |

### Divide Surface (SDivide)

Genera una grilla de puntos {uv} sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir |
| U Count | `U` | Integer | item | Cantidad de segmentos en la dirección {u} |
| V Count | `V` | Integer | item | Cantidad de segmentos en la dirección {v} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | árbol | Puntos de división |
| Normals | `N` | Vector | árbol | Vectores normales en los puntos de división |
| Parameters | `uv` | Point | árbol | Coordenadas de parámetro en los puntos de división |

### Edges from Directions (EdgesDir)

Selecciona aristas de un brep según su dirección

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep del que extraer las aristas |
| Directions | `D` | Vector | lista | Direcciones por las que filtrar |
| Reflex | `R` | Boolean | item | Si es True, la prueba de ángulo incluye el ángulo reflejo |
| Angle | `A` | Number | item | Tolerancia angular de la dirección. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Aristas encontradas |
| Indices | `I` | Integer | lista | Índices de las aristas |
| Map | `M` | Text | lista | Mapa de direcciones por arista |

### Edges from Faces (EdgesFaces)

Selecciona todas las aristas del brep que delimitan ciertas caras

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep del que extraer las aristas |
| Points | `P` | Point | lista | Puntos para comprobar la coincidencia con las caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Aristas encontradas |
| Indices | `I` | Integer | lista | Índices de las aristas |

### Edges from Length (EdgesLen)

Selecciona aristas de un brep según su longitud

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep del que extraer las aristas |
| Minimum | `L-` | Number | item | Longitud mínima de arista para incluirla. |
| Maximum | `L+` | Number | item | Longitud máxima de arista para incluirla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Aristas encontradas |
| Indices | `I` | Integer | lista | Índices de las aristas |

### Edges from Linearity (EdgesLin)

Selecciona aristas de un brep según su linealidad

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep del que extraer las aristas |
| Minimum | `L-` | Number | item | Desviación mínima de linealidad para incluir la arista. |
| Maximum | `L+` | Number | item | Desviación máxima de linealidad para incluir la arista. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Aristas encontradas |
| Indices | `I` | Integer | lista | Índices de las aristas |

### Edges from Points (EdgesPt)

Selecciona aristas de un brep según su coincidencia con puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep del que extraer las aristas |
| Points | `P` | Point | lista | Puntos para comprobar la coincidencia |
| Valence | `V` | Integer | item | Valencia mínima de puntos por arista |
| Tolerance *(opcional)* | `T` | Number | item | Tolerancia de coincidencia opcional. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges | `E` | Curve | lista | Aristas encontradas |
| Indices | `I` | Integer | lista | Índices de las aristas |
| Map | `M` | Text | lista | Mapa de puntos por arista |

### Fillet Edge (FilEdge)

Aplica fillet a algunas aristas de un brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Brep | item | Forma a la que aplicar fillet |
| Blend | `B` | Integer | item | Tipo de mezcla del fillet |
| Metric | `M` | Integer | item | Tipo de medida del fillet |
| Edges *(opcional)* | `E` | Integer | lista | Índices de las aristas a las que aplicar fillet |
| Radii *(opcional)* | `R` | Number | lista | Radios/medidas del fillet por arista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `B` | Brep | item | Brep con fillet |

### Flip

Invierte las normales de una superficie según geometría local o remota

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a invertir |
| Guide *(opcional)* | `G` | Surface | item | Superficie guía opcional con la que coincidir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie invertida |
| Result | `R` | Boolean | item | Resultado: True si la superficie se invirtió |

### Isotrim (SubSrf)

Extrae un subconjunto isoparamétrico de una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Domain | `D` | Domain² | item | Dominio del subconjunto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Subconjunto de la superficie base |

### Merge Faces (FMerge)

Fusiona todas las caras coplanares adyacentes de un brep

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep a simplificar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | item | Brep simplificado |
| Before | `N0` | Integer | item | Cantidad de caras antes de simplificar |
| After | `N1` | Integer | item | Cantidad de caras después de simplificar |

### Offset Surface (Offset)

Aplica offset a una superficie con una distancia fija.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Distance | `D` | Number | item | Distancia de offset |
| Retrim | `T` | Boolean | item | Volver a recortar el offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Resultado del offset |

### Offset Surface Loose (Offset (L))

Aplica offset a una superficie moviendo sus puntos de control.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Distance | `D` | Number | item | Distancia de offset |
| Retrim | `T` | Boolean | item | Volver a recortar el offset |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Resultado del offset |

### Retrim

Vuelve a recortar una superficie según los datos de recorte 3D de otra superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Source | `S` | Surface | item | Superficie de origen que entrega los datos de recorte UV. |
| Target | `T` | Surface | item | Superficie objetivo a recortar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie recortada de nuevo |

### Reverse Surface (Reverse Srf)

Invierte las direcciones de la parametrización de la superficie (U, V y W)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a invertir |
| U | `U` | Boolean | item | Invierte la dirección {u} de la parametrización de la superficie. |
| V | `V` | Boolean | item | Invierte la dirección {v} de la parametrización de la superficie. |
| W | `W` | Boolean | item | Invierte la dirección {w} (también llamada normal) de la parametrización de la superficie. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie invertida |

### Surface Frames (SFrames)

Genera una grilla de marcos {uv} sobre una superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a dividir |
| U Count | `U` | Integer | item | Cantidad de segmentos en la dirección U |
| V Count | `V` | Integer | item | Cantidad de segmentos en la dirección V |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frames | `F` | Plane | árbol | Marcos de la superficie |
| Parameters | `uv` | Point | árbol | Coordenadas de parámetro en los puntos de división |

### Transpose Surface (Transpose)

Transpone la parametrización de la superficie (intercambia U y V)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie a transponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie transpuesta |
| U | `U` | Domain | item | Dominio {u} de la superficie transpuesta |
| V | `V` | Domain | item | Dominio {v} de la superficie transpuesta |

### Untrim

Quita todas las curvas de recorte de una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie sin recortar |
