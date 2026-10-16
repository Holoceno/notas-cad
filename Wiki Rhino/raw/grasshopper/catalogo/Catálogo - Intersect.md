---
title: "Catálogo Grasshopper — Intersect"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Intersect"
libraries: ["Curve Components 8.35.26251.13001", "IO Components 8.35.26251.13001", "Surface Components 8.35.26251.13001", "Transform Components 8.35.26251.13001", "Triangulation Components 8.35.26251.13001", "Vector Components 8.35.26251.13001"]
components: 52
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, geometria/intersecciones, geometria/brep]
---

# Intersect

52 objetos · librería: Curve Components 8.35.26251.13001, IO Components 8.35.26251.13001, Surface Components 8.35.26251.13001, Transform Components 8.35.26251.13001, Triangulation Components 8.35.26251.13001, Vector Components 8.35.26251.13001 · autor: Robert McNeel & Associates

Mapas: [[Mapa - Intersecciones y booleanos]] (52) · [[Mapa - Brep y sólidos]] (16)

## Mathematical

### Brep – Line (BLX)

Calcula las intersecciones entre un Brep y una línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep base |
| Line | `L` | Line | item | Línea de intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de superposición de la intersección |
| Points | `P` | Point | lista | Puntos de intersección |

### Brep – Plane (Sec)

Calcula las intersecciones entre un Brep y un plano (lo que también se conoce como sección).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep base |
| Plane | `P` | Plane | item | Plano de sección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de sección |
| Points | `P` | Point | lista | Puntos de sección |

### Contour

Crea un conjunto de contornos de un Brep o una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Geometry | item | Brep o malla a contornear |
| Point | `P` | Point | item | Punto inicial de los contornos |
| Direction | `N` | Vector | item | Dirección normal de los contornos |
| Distance | `D` | Number | item | Distancia entre contornos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Contours | `C` | Curve | árbol | Contornos resultantes (agrupados por sección) |

### Contour (ex) (Contour)

Crea un conjunto de contornos de un Brep o una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Geometry | item | Brep o malla a contornear |
| Plane | `P` | Plane | item | Plano base de los contornos |
| Offsets *(opcional)* | `O` | Number | lista | Desfases de los contornos desde el plano base (si se omiten, debes indicar distancias) |
| Distances *(opcional)* | `D` | Number | lista | Distancias entre contornos (si se omiten, debes indicar desfases) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Contours | `C` | Curve | árbol | Contornos resultantes (agrupados por sección) |

### Curve – Line (CLX)

Calcula las intersecciones entre una curva y una línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a intersectar |
| Line | `L` | Line | item | Línea con la que intersectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Eventos de intersección |
| Params | `t` | Number | lista | Parámetros en la curva |
| Count | `N` | Integer | item | Cantidad de eventos de intersección |

### Curve – Plane (PCX)

Calcula las intersecciones entre una curva y un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva base |
| Plane | `P` | Plane | item | Plano de intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Eventos de intersección |
| Params C | `t` | Number | lista | Parámetros {t} en la curva |
| Params P | `uv` | Point | lista | Parámetros {uv} en el plano |

### IsoVist (IVist)

Calcula un muestreo de isovista en una ubicación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano y origen del muestreo |
| Count | `N` | Integer | item | Cantidad de muestras |
| Radius | `R` | Number | item | Radio de muestreo |
| Obstacles | `O` | Geometry | lista | Contornos de los obstáculos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de intersección de los rayos de muestreo con los obstáculos |
| Distance | `D` | Number | lista | Lista de distancias de intersección |
| Index | `I` | Integer | lista | Lista de índices de obstáculo de cada impacto, o -1 si no se golpeó ningún obstáculo |

### IsoVist Ray (IVRay)

Calcula una sola muestra de isovista en una ubicación

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sample | `S` | Line | item | Rayo de muestreo |
| Radius | `R` | Number | item | Radio de muestreo |
| Obstacles | `O` | Geometry | lista | Contornos de los obstáculos (se permiten curvas, planos, mallas y breps) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto de intersección del rayo de muestreo con los obstáculos |
| Distance | `D` | Number | item | Distancia desde el inicio del rayo hasta el punto de intersección |
| Index | `I` | Integer | item | Índice del obstáculo golpeado, o -1 si no se golpeó ningún obstáculo |

### Line – Line (LLX)

Calcula las intersecciones entre dos líneas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line 1 | `A` | Line | item | Primera línea de la intersección |
| Line 2 | `B` | Line | item | Segunda línea de la intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Param A | `tA` | Number | item | Parámetro en la línea A |
| Param B | `tB` | Number | item | Parámetro en la línea B |
| Point A | `pA` | Point | item | Punto en la línea A |
| Point B | `pB` | Point | item | Punto en la línea B |

### Line – Plane (PLX)

Calcula la intersección entre una línea y un plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea base |
| Plane | `P` | Plane | item | Plano de intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Evento de intersección |
| Param L | `t` | Number | item | Parámetro {t} en la línea infinita |
| Param P | `uv` | Point | item | Parámetro {uv} en el plano |

### Mesh – Plane (Sec)

Calcula las intersecciones entre una malla y un plano (lo que también se conoce como sección).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla base |
| Plane | `P` | Plane | item | Plano de sección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Polilíneas de sección |

### Mesh – Ray (MeshRay)

Intersecta una malla con un rayo semi-infinito

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a intersectar |
| Point | `P` | Point | item | Punto inicial del rayo |
| Direction | `D` | Vector | item | Dirección del rayo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `X` | Point | item | Primer punto de intersección |
| Hit | `H` | Boolean | item | Booleano que indica si el rayo impacta o no |

### Plane Region (PlReg)

Crea una región acotada a partir de planos que se intersectan.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane | `P` | Plane | item | Plano y origen de la región |
| Bounds | `B` | Plane | lista | Planos que acotan la región |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Region | `R` | Curve | item | Región acotada |

### Plane – Plane (PPX)

Calcula la intersección de dos planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane A | `A` | Plane | item | Primer plano |
| Plane B | `B` | Plane | item | Segundo plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Line | `L` | Line | item | Línea de intersección |

### Plane – Plane – Plane (3PX)

Calcula las intersecciones de tres planos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane A | `A` | Plane | item | Primer plano |
| Plane B | `B` | Plane | item | Segundo plano |
| Plane C | `C` | Plane | item | Tercer plano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `Pt` | Point | item | Punto de intersección |
| Line AB | `AB` | Line | item | Línea de intersección entre A y B |
| Line AC | `AC` | Line | item | Línea de intersección entre A y C |
| Line BC | `BC` | Line | item | Línea de intersección entre B y C |

### Point Cloud Contour (PC Contour)

Crea una serie de curvas planas intersectando planos con una nube de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cloud | `Cloud` | Point Cloud | item | Nube de puntos |
| Start *(opcional)* | `Start` | Point | item | Punto inicial de los contornos |
| Direction *(opcional)* | `Direction` | Vector | item | Dirección normal de los contornos |
| Distance *(opcional)* | `Distance` | Number | item | Distancia entre contornos |
| Limit *(opcional)* | `Limit` | Boolean | item | Limita los contornos al rango indicado por el vector normal. Si es False, se generan contornos para toda la nube de puntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Curves` | Curve | lista | Las curvas de sección |

### Point Cloud Section (PC Section)

Crea una sección plana intersectando un plano con una nube de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cloud | `Cloud` | Point Cloud | item | Nube de puntos |
| Plane | `Plane` | Plane | item | El plano de intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `Curves` | Curve | lista | Las curvas de sección |

### Surface – Line (SLX)

Calcula las intersecciones entre una superficie y una línea.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Line | `L` | Line | item | Línea de intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de superposición de la intersección |
| Points | `P` | Point | lista | Puntos de intersección |
| UV Points | `uv` | Point | lista | Coordenadas {uv} de la superficie en los eventos de intersección |
| Normal | `N` | Vector | lista | Vector normal de la superficie en los eventos de intersección |

## Physical

### Brep – Brep (BBX)

Calcula las intersecciones entre dos Breps.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep A | `A` | Brep | item | Primer Brep |
| Brep B | `B` | Brep | item | Segundo Brep |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de intersección |
| Points | `P` | Point | lista | Puntos de intersección |

### Brep – Curve (BCX)

Calcula las intersecciones entre un Brep y una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep base |
| Curve | `C` | Curve | item | Curva de intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de superposición de la intersección |
| Points | `P` | Point | lista | Puntos de intersección |

### Clash

Realiza un análisis de colisiones (clash) en un conjunto de formas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First Set | `A` | Mesh | lista | Primer conjunto de formas |
| Second Set | `B` | Mesh | lista | Segundo conjunto de formas |
| Distance | `D` | Number | item | Tolerancia de distancia para detectar colisiones |
| Result Limit | `L` | Integer | item | Cantidad máxima de resultados a buscar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Clash Count | `N` | Integer | item | Cantidad de colisiones encontradas |
| Clash Points | `P` | Point | lista | Colección de puntos de colisión. |
| Clash Radii | `R` | Number | lista | Colección de radios de colisión (uno por punto). |
| First Index | `i` | Integer | lista | Índice de la malla en colisión del primer conjunto. |
| Second index | `j` | Integer | lista | Índice de la malla en colisión del segundo conjunto. |

### Collision Many–Many (ColMM)

Prueba colisiones muchos-con-muchos entre objetos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Colliders | `C` | Geometry | lista | Objetos para la colisión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Collision | `C` | Boolean | lista | True si el objeto de este índice colisiona con alguno de los otros objetos |
| Indices | `I` | Integer | lista | Índice del objeto del conjunto que colisionó con el objeto de este índice |

### Collision One–Many (ColOM)

Prueba colisiones uno-con-muchos entre objetos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Collider | `C` | Geometry | item | Objeto para la colisión |
| Obstacles | `O` | Geometry | lista | Obstáculos para la colisión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Collision | `C` | Boolean | item | True si el objeto colisiona con alguno de los obstáculos |
| Index | `I` | Integer | item | Índice del primer obstáculo que colisiona con el objeto |

### Curve – Curve (CCX)

Calcula las intersecciones entre dos curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve A | `A` | Curve | item | Primera curva |
| Curve B | `B` | Curve | item | Segunda curva |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Eventos de intersección |
| Params A | `tA` | Number | lista | Parámetros en la primera curva |
| Params B | `tB` | Number | lista | Parámetros en la segunda curva |

### Curve – Self (CX)

Calcula todas las autointersecciones de una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva para las autointersecciones |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Eventos de intersección |
| Params | `t` | Number | lista | Parámetros en la curva |

### Mesh – Curve (MCX)

Intersección malla-curva

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a intersectar |
| Curve | `C` | Curve | item | Curva con la que intersectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `X` | Point | lista | Puntos de intersección |
| Faces | `F` | Integer | lista | Índice de la cara de intersección de cada punto |

### Mesh – Mesh (MMX)

Intersección malla-malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh A | `A` | Mesh | item | Primera malla |
| Mesh B | `B` | Mesh | item | Segunda malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Intersections | `X` | Curve | lista | Polilíneas de intersección |

### Multiple Curves (MCX)

Calcula las intersecciones entre varias curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas a intersectar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Eventos de intersección |
| Index A | `iA` | Integer | lista | Índice de la primera curva de la intersección |
| Index B | `iB` | Integer | lista | Índice de la segunda curva de la intersección |
| Param A | `tA` | Number | lista | Parámetro en la primera curva |
| Param B | `tB` | Number | lista | Parámetro en la segunda curva |

### Surface Split (SrfSplit)

Divide una superficie con un grupo de curvas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Curves *(opcional)* | `C` | Curve | lista | Curvas de corte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fragments | `F` | Surface | lista | Fragmentos resultantes |

### Surface – Curve (SCX)

Calcula las intersecciones entre una superficie y una curva.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Superficie base |
| Curve | `C` | Curve | item | Curva de intersección |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas de superposición de la intersección |
| Points | `P` | Point | lista | Puntos de intersección |
| UV Points | `uv` | Point | lista | Coordenadas {uv} de la superficie en los eventos de intersección |
| Normals | `N` | Vector | lista | Vector normal de la superficie en los eventos de intersección |
| Parameters | `t` | Number | lista | Parámetro de la curva en los eventos de intersección |
| Tangents | `T` | Vector | lista | Vector tangente de la curva en los eventos de intersección |

## Region

### Split with Brep (Split)

Divide una curva con un Brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a dividir |
| Brep | `B` | Brep | item | Brep con el que dividir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curvas divididas |
| Points | `P` | Point | lista | Puntos de división |

### Split with Breps (Split)

Divide una curva con varios Breps.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Brep | `B` | Brep | lista | Brep con el que recortar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | lista | Curvas divididas |
| Points | `P` | Point | lista | Puntos de división |

### Trim with Brep (Trim)

Recorta una curva con un Brep.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Brep | `B` | Brep | item | Brep con el que recortar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inside | `Ci` | Curve | lista | Curvas divididas que quedan dentro del Brep |
| Outside | `Co` | Curve | lista | Curvas divididas que quedan fuera del Brep |

### Trim with Breps (Trim)

Recorta una curva con varios Breps.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Brep | `B` | Brep | lista | Breps con los que recortar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inside | `Ci` | Curve | lista | Curvas divididas que quedan dentro de los Breps de recorte |
| Outside | `Co` | Curve | lista | Curvas divididas que quedan fuera de los Breps de recorte |

### Trim with Region (Trim)

Recorta una curva con una región.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Region | `R` | Curve | item | Región con la que recortar |
| Plane *(opcional)* | `P` | Plane | item | Plano de solución opcional. Si se omite, se usa el plano que mejor se ajusta a la curva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inside | `Ci` | Curve | lista | Curvas divididas que quedan dentro de la región |
| Outside | `Co` | Curve | lista | Curvas divididas que quedan fuera de la región |

### Trim with Regions (Trim)

Recorta una curva con varias regiones.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Curva a recortar |
| Regions | `R` | Curve | lista | Regiones con las que recortar |
| Plane *(opcional)* | `P` | Plane | item | Plano de solución opcional. Si se omite, se usa el plano que mejor se ajusta a la curva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inside | `Ci` | Curve | lista | Curvas divididas que quedan dentro de las regiones |
| Outside | `Co` | Curve | lista | Curvas divididas que quedan fuera de las regiones |

## Shape

### Boundary Volume (BVol)

Crea una polisuperficie cerrada a partir de superficies de contorno

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundaries | `B` | Brep | lista | Superficies de contorno |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Solid | `S` | Brep | item | Volumen sólido |

### Box Slits (Slits)

Agrega ranuras (slits) a una colección de cajas que se intersectan

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boxes | `B` | Box | lista | Cajas a intersectar |
| Gap | `G` | Number | item | Ancho de holgura adicional |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | árbol | Cajas con ranuras |
| Topology | `T` | Integer | árbol | Topología de las ranuras |

### Mesh Difference (MDif)

Realiza una diferencia sólida entre dos conjuntos de mallas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes A | `A` | Mesh | lista | Primer conjunto de mallas |
| Meshes B | `B` | Mesh | lista | Segundo conjunto de mallas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | lista | Resultado de la diferencia A-B |

### Mesh Intersection (MInt)

Realiza una intersección sólida de un conjunto de mallas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes A | `A` | Mesh | lista | Primer conjunto de mallas |
| Meshes B | `B` | Mesh | lista | Segundo conjunto de mallas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | lista | Resultado de la intersección de A y B |

### Mesh Split (MSplit)

División malla-malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a dividir |
| Splitters | `S` | Mesh | lista | Mallas con las que dividir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | lista | Resultado de la división de la malla |

### Mesh Union (MUnion)

Realiza una unión sólida de un conjunto de mallas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Mallas a unir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | lista | Resultado de la unión sólida de mallas |

### Region Difference (RDiff)

Diferencia entre dos conjuntos de curvas planas cerradas (regiones)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves A | `A` | Curve | lista | Curvas de las que restar. |
| Curves B | `B` | Curve | lista | Curvas a restar. |
| Plane *(opcional)* | `P` | Plane | item | Plano opcional para la solución booleana |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Curve | lista | Contornos resultantes de la diferencia booleana (A - B) |

### Region Intersection (RInt)

Intersección entre dos conjuntos de curvas planas cerradas (regiones)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves A | `A` | Curve | lista | Primer conjunto de regiones. |
| Curves B | `B` | Curve | lista | Segundo conjunto de regiones. |
| Plane *(opcional)* | `P` | Plane | item | Plano opcional para la solución booleana |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Curve | lista | Contornos resultantes de la intersección booleana (A y B) |

### Region Slits (RSlits)

Agrega ranuras (slits) a una colección de regiones planas que se intersectan

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Regions | `R` | Curve | lista | Regiones planas a intersectar |
| Width | `W` | Number | item | Ancho de las ranuras |
| Gap | `G` | Number | item | Tamaño de holgura adicional en los puntos donde se encuentran las ranuras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Regions | `R` | Surface | árbol | Regiones con ranuras |
| Topology | `T` | Integer | árbol | Topología de las ranuras |

### Region Union (RUnion)

Unión de un conjunto de curvas planas cerradas (regiones)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curves | `C` | Curve | lista | Curvas para la operación de unión booleana |
| Plane *(opcional)* | `P` | Plane | item | Plano opcional para la solución booleana |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Curve | lista | Contornos resultantes de la unión booleana |

### Solid Difference (SDiff)

Realiza una diferencia sólida entre dos conjuntos de Breps.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps A | `A` | Brep | lista | Primer conjunto de Breps |
| Breps B | `B` | Brep | lista | Segundo conjunto de Breps |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Brep | lista | Resultado de la diferencia |

### Solid Intersection (SInt)

Realiza una intersección sólida entre dos conjuntos de Breps.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps A | `A` | Brep | lista | Primer conjunto de Breps |
| Breps B | `B` | Brep | lista | Segundo conjunto de Breps |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Brep | lista | Resultado de la intersección |

### Solid Union (SUnion)

Realiza una unión sólida de un conjunto de Breps.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | lista | Breps a unir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Brep | lista | Resultado de la unión |

### Split Brep (Split)

Divide un brep con otro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep a dividir |
| Cutter *(opcional)* | `C` | Brep | item | Forma de corte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Brep | lista | Fragmentos del brep |

### Split Brep Multiple (SplitMul)

Divide un brep con un grupo de otros breps.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep a dividir |
| Cutters *(opcional)* | `C` | Brep | lista | Formas de corte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Brep | lista | Fragmentos del brep |

### Trim Solid (Trim)

Abre perforaciones en una forma con un conjunto de cortadores sólidos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Brep | item | Forma a recortar |
| Cutters | `T` | Brep | lista | Formas de recorte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Brep | lista | Forma con perforaciones |
