---
title: "Catálogo Grasshopper — Mesh"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Mesh"
libraries: ["Curve Components 8.35.26251.13001", "Grasshopper 1.0.0008", "Kangaroo2 Components 2.5.3", "Surface Components 8.35.26251.13001", "Transform Components 8.35.26251.13001", "Triangulation Components 8.35.26251.13001"]
components: 64
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/kangaroo, geometria/mallas]
---

# Mesh

64 objetos · librería: Curve Components 8.35.26251.13001, Grasshopper 1.0.0008, Kangaroo2 Components 2.5.3, Surface Components 8.35.26251.13001, Transform Components 8.35.26251.13001, Triangulation Components 8.35.26251.13001 · autor: Daniel Piker, Robert McNeel & Associates

Mapas: [[Mapa - Mallas y SubD]] (64) · [[Mapa - Brep y sólidos]] (4)

## Analysis

### Deconstruct Face (DeFace)

Descompone una cara de malla en sus cuatro índices de esquina.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Face | `F` | Mesh face | item | Cara de malla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Integer | item | Índice del primer vértice de la cara |
| Corner B | `B` | Integer | item | Índice del segundo vértice de la cara |
| Corner C | `C` | Integer | item | Índice del tercer vértice de la cara |
| Corner D | `D` | Integer | item | Índice del cuarto vértice de la cara (igual a C si la cara es un triángulo) |

### Deconstruct Mesh (DeMesh)

Descompone una malla en sus partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Vértices de la malla |
| Faces | `F` | Mesh face | lista | Caras de la malla |
| Colours | `C` | Colour | lista | Colores de los vértices de la malla |
| Normals | `N` | Vector | lista | Normales de la malla |

### Face Boundaries (FaceB)

Convierte todas las caras de la malla en polilíneas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de la que extraer los bordes de las caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundaries | `B` | Curve | lista | Polilíneas de borde de cada cara de la malla |

### Face Circles (FaceC)

Calcula los círculos circunscritos de todas las caras de la malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de la que extraer normales y puntos centrales |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centers | `C` | Circle | lista | Círculos circunscritos de todos los triángulos de la malla (se omiten los cuadriláteros) |
| Ratio | `R` | Number | lista | Proporción de los triángulos: altura / arista más larga (se omiten los cuadriláteros) |

### Face Normals (FaceN)

Extrae las normales y los puntos centrales de todas las caras de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de la que extraer normales y puntos centrales |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centers | `C` | Point | lista | Puntos centrales de todas las caras |
| Normals | `N` | Vector | lista | Vectores normales de todas las caras |

### Mesh Closest Point (MeshCP)

Busca el punto más cercano en una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto desde el que buscar |
| Mesh | `M` | Mesh | item | Malla en la que buscar el punto más cercano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Ubicación en la malla más cercana al punto de búsqueda |
| Index | `I` | Integer | item | Índice de la cara del punto más cercano |
| Parameter | `P` | Mesh Parameter | item | Parámetro de malla del punto más cercano |

### Mesh Edges (MEdges)

Obtiene todas las aristas de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de la que extraer las aristas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Naked Edges | `E1` | Line | lista | Aristas con valencia 1 (una sola cara adyacente) |
| Interior Edges | `E2` | Line | lista | Aristas con valencia 2 (dos caras adyacentes) |
| Non-Manifold Edges | `E3` | Line | lista | Aristas con valencia 3 o mayor |

### Mesh Eval (MEval)

Evalúa una malla en un parámetro dado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a evaluar |
| Parameter | `P` | Mesh Parameter | item | Parámetro de malla para la evaluación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto en el parámetro de malla |
| Normal | `N` | Vector | item | Vector normal en el parámetro de malla |
| Colour | `C` | Colour | item | Color en el parámetro de malla |

### Mesh Inclusion (MInc)

Prueba si un punto está contenido en una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla para la prueba de inclusión (solo se consideran mallas cerradas) |
| Point | `P` | Point | item | Punto para la prueba de inclusión |
| Strict | `S` | Boolean | item | Si es True, la inclusión es estricta |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Inside | `I` | Boolean | item | Indicador de si el punto está dentro |

## Primitive

### Construct Mesh (ConMesh)

Construye una malla a partir de vértices, caras y colores opcionales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices | `V` | Point | lista | Vértices del objeto malla |
| Faces | `F` | Mesh face | lista | Caras del objeto malla |
| Colours *(opcional)* | `C` | Colour | lista | Colores de los vértices (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla construida |

### Mesh Box (MBox)

Crea una caja de malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Box | item | Caja base |
| X Count | `X` | Integer | item | Cantidad de caras en la dirección {x} |
| Y Count | `Y` | Integer | item | Cantidad de caras en la dirección {y} |
| Z Count | `Z` | Integer | item | Cantidad de caras en la dirección {z} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La caja de malla 3D |

### Mesh Colours (MCol)

Asigna un patrón de color repetitivo a un objeto malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla base |
| Colours | `C` | Colour | lista | Patrón de color |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla coloreada |

### Mesh Plane (MPlane)

Crea un plano de malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundary | `B` | Rectangle | item | Rectángulo que describe el borde del plano |
| Width count | `W` | Integer | item | Cantidad de caras en la dirección {x} |
| Height count | `H` | Integer | item | Cantidad de caras en la dirección {y} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Plano de malla |
| Area | `A` | Number | item | Área del plano de malla |

### Mesh Quad (Quad)

Crea un cuadrilátero de malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Integer | item | Índice de la primera esquina de la cara |
| Corner B | `B` | Integer | item | Índice de la segunda esquina de la cara |
| Corner C | `C` | Integer | item | Índice de la tercera esquina de la cara |
| Corner D | `D` | Integer | item | Índice de la cuarta esquina de la cara |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Face | `F` | Mesh face | item | Cara de malla cuadrangular |

### Mesh Sphere (MSphere)

Crea una esfera de malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| Radius | `R` | Number | item | Radio de la esfera de malla |
| U Count | `U` | Integer | item | Cantidad de caras alrededor de la esfera |
| V Count | `V` | Integer | item | Cantidad de caras de polo a polo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Esfera de malla |

### Mesh Sphere Ex (MSphereEx)

Crea una esfera de malla a partir de parches cuadrados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base | `B` | Plane | item | Plano base |
| Radius | `R` | Number | item | Radio de la esfera de malla |
| Count | `C` | Integer | item | Cantidad de caras a lo largo de cada arista del parche |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Esfera de malla |

### Mesh Spray (MSpray)

Asigna colores a una malla según puntos de rociado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla base |
| Points | `P` | Point | lista | Puntos de rociado |
| Colours | `C` | Colour | lista | Colores de los puntos de rociado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla rociada |

### Mesh Triangle (Triangle)

Crea un triángulo de malla.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Corner A | `A` | Integer | item | Índice de la primera esquina de la cara |
| Corner B | `B` | Integer | item | Índice de la segunda esquina de la cara |
| Corner C | `C` | Integer | item | Índice de la tercera esquina de la cara |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Face | `F` | Mesh face | item | Cara de malla triangular |

## Triangulation

### Convex Hull (Hull2D)

Calcula la envolvente convexa plana de una colección de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos para calcular la envolvente convexa |
| Plane *(opcional)* | `Pl` | Plane | item | Plano base opcional. Si no se entrega, se usa el plano que mejor se ajusta. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hull | `H` | Curve | item | Envolvente convexa en el espacio del plano base |
| Hull(z) | `Hz` | Curve | item | Envolvente convexa en el espacio del mundo |
| Indices | `I` | Integer | lista | Índices de los puntos que están en la envolvente convexa |

### Convex Hull 3D (Hull3D)

Calcula la envolvente convexa no plana (3D) de una colección de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos para calcular la envolvente convexa |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hull | `H` | Mesh | item | Envolvente convexa en coordenadas del mundo |
| Indices | `I` | Integer | lista | Índices de los puntos que están en la envolvente convexa |

### Delaunay Edges (Con)

Conectividad de Delaunay

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a triangular |
| Plane *(opcional)* | `Pl` | Plane | item | Plano base opcional. Si no se entrega, se usa el plano que mejor se ajusta. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Connectivity | `C` | Integer | árbol | Diagrama de conectividad topológica |
| Edges | `E` | Line | lista | Aristas del diagrama de conectividad |

### Delaunay Mesh (Del)

Triangulación de Delaunay

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos a triangular |
| Plane *(opcional)* | `Pl` | Plane | item | Plano base opcional. Si no se entrega, se usa el plano que mejor se ajusta. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Facet Dome (Facet)

Crea una cúpula facetada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos sobre la cúpula que describen los centros de las facetas |
| Box *(opcional)* | `B` | Box | item | Caja contenedora opcional para el borde de las facetas |
| Radius *(opcional)* | `R` | Number | item | Radio opcional de las facetas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Curve | lista | Patrón de facetas completo |
| Dome | `D` | Surface | item | Superficie de la cúpula |

### MetaBall

Isocurva metaball 2D que pasa por un punto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Ubicaciones de las cargas puntuales |
| Plane | `Pl` | Plane | item | Plano de sección del metaball |
| Point | `X` | Point | item | Intersección de la isocurva |
| Accuracy *(opcional)* | `A` | Number | item | Precisión de muestreo de la isocurva (déjalo vacío para precisión adaptativa) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Isocurve | `I` | Curve | lista | Isocurva metaball |

### MetaBall(t)

Isosuperficie metaball 2D por umbral

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Ubicaciones de las cargas puntuales |
| Plane | `Pl` | Plane | item | Plano de sección del metaball |
| Threshold | `T` | Number | item | Valor umbral de la isocurva |
| Accuracy *(opcional)* | `A` | Number | item | Precisión de muestreo de la isocurva (déjalo vacío para la precisión por defecto) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Isocurve | `I` | Curve | lista | Isocurvas metaball |

### MetaBall(t) Custom (MetaBall(t))

Isosuperficie metaball 2D por umbral y valores de carga personalizados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Ubicaciones de las cargas puntuales |
| Charge | `C` | Number | lista | Cargas puntuales (solo valores positivos) |
| Plane | `Pl` | Plane | item | Plano de sección del metaball |
| Threshold | `T` | Number | item | Valor umbral de la isocurva |
| Accuracy *(opcional)* | `A` | Number | item | Precisión de muestreo de la isocurva (déjalo vacío para la precisión por defecto) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Isocurve | `I` | Curve | lista | Isocurvas metaball |

### OcTree (OcT)

Una estructura oc-tree tridimensional

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de entrada |
| Square | `S` | Boolean | item | Hojas cuadradas |
| Group | `G` | Integer | item | Contenido permitido por hoja |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boxes | `B` | Box | árbol | Cajas de las hojas del oc-tree |
| Points | `P` | Point | árbol | Puntos por caja |

### Proximity 2D (Prox)

Busca proximidad bidimensional dentro de una lista de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de entrada |
| Plane | `Pl` | Plane | item | Plano base opcional. Si es nulo, se usa el plano que mejor se ajusta |
| Group | `G` | Integer | item | Cantidad máxima de puntos más cercanos a buscar |
| Min Radius *(opcional)* | `R-` | Number | item | Radio mínimo de búsqueda (opcional). |
| Max Radius *(opcional)* | `R+` | Number | item | Radio máximo de búsqueda (opcional). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Links | `L` | Line | árbol | Enlaces de proximidad |
| Topology | `T` | Integer | árbol | Topología de proximidad |

### Proximity 3D (Prox)

Busca proximidad tridimensional dentro de una lista de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de entrada |
| Group | `G` | Integer | item | Cantidad máxima de puntos más cercanos a buscar |
| Min Radius *(opcional)* | `R-` | Number | item | Radio mínimo de búsqueda (opcional). |
| Max Radius *(opcional)* | `R+` | Number | item | Radio máximo de búsqueda (opcional). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Links | `L` | Line | árbol | Enlaces de proximidad |
| Topology | `T` | Integer | árbol | Topología de proximidad |

### Quad Remesh (QRMesh)

Rehace la malla de una forma con cuadriláteros (quad remesh).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | item | Geometría sobre la que operar |
| Guides *(opcional)* | `C` | Curve | lista | Curvas guía |
| Settings | `S` | Quad meshing settings | item | Ajustes del remallado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla resultante solo con caras cuadrangulares. |

### Quad Remesh Settings (QRSettings)

Crea ajustes para el remallado con cuadriláteros.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Target Count | `Tc` | Integer | item | Cantidad de cuadriláteros que se busca obtener en el resultado. |
| Adaptive Size | `As` | Number | item | Un número en el rango [0, 100] que controla cómo cambia el tamaño de los cuadriláteros según la curvatura. |
| Adaptive Count | `Ac` | Boolean | item | True si se permite más cuadriláteros en zonas de alta curvatura. |
| Target Edge Length *(opcional)* | `Te` | Number | item | Longitud de arista objetivo (opcional). Si se define, se ignora 'Target Count'. |
| Hard Edges | `He` | Boolean | item | Detecta y conserva las aristas duras de la malla de entrada. |
| Seam Edges | `Se` | Integer | item | Detecta y conserva las aristas de borde de las caras del brep (0=desactivado, 1=inteligente, 2=estricto). |
| Symmetry | `Sy` | Integer | item | Eje de simetría (0=ninguno, 1=X, 2=Y, 3=Z). |
| Guide Curves | `Gc` | Integer | item | Influencia de las curvas guía (0=aproximar, 1=anillo de aristas, 2=bucle de aristas). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Settings | `S` | Quad meshing settings | item | Ajustes del remallado con cuadriláteros |

### QuadTree (QT)

Una estructura quadtree bidimensional

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos de entrada |
| Plane *(opcional)* | `Pl` | Plane | item | Plano base opcional. Si se omite, se usa el plano que mejor se ajusta |
| Square | `S` | Boolean | item | Hojas cuadradas |
| Group | `G` | Integer | item | Contenido permitido por hoja |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Quads | `Q` | Curve | árbol | Hojas del quadtree |
| Points | `P` | Point | árbol | Puntos por cuadrante |

### ShrinkWrap (Wrap)

Envuelve (ShrinkWrap) una malla o una nube de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Geometry | lista | Geometría a envolver con ShrinkWrap |
| Edge Length *(opcional)* | `E` | Number | item | La longitud de arista objetivo en unidades del documento. Valores más pequeños dan más resolución a costa de mallas más pesadas. Si no se entrega, se calcula un valor según heurísticas para obtener una envoltura holgada. |
| Offset | `O` | Number | item | Distancia de offset hacia afuera o hacia adentro |
| Smoothing | `S` | Integer | item | La cantidad de veces que se aplica el suavizado |
| Optimization | `P` | Integer | item | Porcentaje [0-100%] de optimización de polígonos deseado. Los polígonos se reducen en las zonas de menor curvatura. Valores más bajos conservan mejor los detalles a costa de más polígonos. |
| Fill Holes | `F` | Boolean | item | Si se rellenan los agujeros de las mallas de entrada antes de envolverlas. Se ignora cuando las entradas son nubes de puntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla ShrinkWrap resultante |

### Substrate

Algoritmo Substrate inspirado en Jared Tarbell (Complexification.net)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Border | `B` | Rectangle | item | Borde del substrate |
| Count | `N` | Integer | item | Cantidad de líneas del substrate |
| Angles | `A` | Number | lista | Ángulos base (en radianes) del substrate |
| Deviation | `D` | Number | item | Desviación angular (en radianes) de las líneas nuevas |
| Seed | `S` | Integer | item | Semilla aleatoria de la solución |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Substrate | `S` | Line | lista | Diagrama substrate |

### TriRemesh

Convierte un Brep o una malla en una malla de triángulos casi equiláteros

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `Geometry` | Geometry | item | Malla, Brep, superficie o curva inicial a remallar |
| Target *(opcional)* | `Target` | Mesh | item | Malla objetivo distinta opcional hacia la que tirar. Si no se entrega, se usa la malla inicial. |
| Sharp *(opcional)* | `Sharp` | Boolean | item | Conserva los detalles agudos |
| Features *(opcional)* | `Features` | Generic Data | lista | Curvas o puntos adicionales opcionales a conservar |
| Length *(opcional)* | `Length` | Number | item | Longitud de arista objetivo |
| Iterations | `Iters` | Integer | item | Cantidad de pasos de remallado a realizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Triangulation | `T` | Mesh | item | Resultado del remallado |
| Dual | `D` | Mesh | item | Malla dual de Ngons |
| Creases | `C` | Line | lista | Líneas de arista de los detalles agudos |

### Voronoi

Diagrama de Voronoi plano de una colección de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos del diagrama de Voronoi |
| Radius *(opcional)* | `R` | Number | item | Radio de celda opcional |
| Boundary *(opcional)* | `B` | Rectangle | item | Borde de contención opcional del diagrama. |
| Plane *(opcional)* | `Pl` | Plane | item | Plano base opcional. Si no se entrega, se usa el plano que mejor se ajusta. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Curve | lista | Celdas del diagrama de Voronoi. |

### Voronoi 3D (Voronoi³)

Diagrama de Voronoi volumétrico de una colección de puntos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | lista | Puntos del diagrama de Voronoi |
| Box *(opcional)* | `B` | Box | item | Borde opcional del diagrama |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cells | `C` | Brep | lista | Celdas del diagrama de Voronoi 3D |
| Boundary | `B` | Boolean | lista | Lista de booleanos que indica para cada celda si forma parte del borde original |

### Voronoi Cell (VCell)

Calcula una sola celda de Voronoi 3D

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Punto semilla de la celda de Voronoi |
| Neighbours | `N` | Point | lista | Puntos vecinos |
| Box *(opcional)* | `B` | Box | item | Borde opcional de la celda |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Cell | `C` | Brep | item | Celda de Voronoi 3D |

### Voronoi Groups (VorGroup)

Calcula un conjunto personalizado de diagramas de Voronoi anidados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundary | `B` | Rectangle | item | Borde del diagrama |
| Generation 1 *(opcional)* | `G1` | Point | lista | Puntos de la generación 1 |
| Generation 2 *(opcional)* | `G2` | Point | lista | Puntos de la generación 2 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Diagram 1 | `D1` | Curve | lista | Diagrama de Voronoi de la generación 1 |
| Diagram 2 | `D2` | Curve | lista | Diagrama de Voronoi de la generación 2 |

## Util

### Align Vertices (AlignVert)

Alinea los vértices cercanos de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a alinear |
| Tolerance | `T` | Number | item | Tolerancia de alineación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | item | Malla alineada |
| Count | `N` | Integer | item | Cantidad de vértices alineados |

### Blur Mesh (MBlur)

Difumina los colores de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a difuminar |
| Iterations | `I` | Integer | item | Cantidad de iteraciones consecutivas de difuminado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla con los colores de los vértices difuminados |

### Cull Faces (CullF)

Elimina (cull) caras de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que eliminar caras |
| Pattern | `P` | Boolean | lista | Patrón de eliminación de caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla sin todas las caras indicadas |

### Cull Vertices (CullV)

Elimina (cull) vértices de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que eliminar vértices |
| Pattern | `P` | Boolean | lista | Patrón de eliminación de vértices |
| Shrink | `S` | Boolean | item | Reducir cuadriláteros: si es True, los cuadriláteros se convierten en triángulos cuando es posible |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla sin todos los vértices indicados |

### Delete Faces (DeleteF)

Borra caras de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que borrar caras |
| Indices | `I` | Integer | lista | Lista de todos los índices de caras a borrar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla sin todas las caras indexadas |

### Delete Vertices (DeleteV)

Borra vértices de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a la que borrar vértices |
| Indices | `I` | Integer | lista | Lista de todos los índices de vértices a borrar |
| Shrink | `S` | Boolean | item | Reducir cuadriláteros: si es True, los cuadriláteros se convierten en triángulos cuando es posible |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla sin todos los vértices indexados |

### Disjoint Mesh (Disjoint)

Separa una malla en piezas desconectadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a dividir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Piezas desconectadas |

### Exposure

Calcula la exposición de una malla a una colección de rayos de energía y obstáculos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Mesh | item | Malla para la solución de exposición |
| Obstructions *(opcional)* | `O` | Mesh | lista | Geometría obstaculizadora adicional opcional |
| Rays | `R` | Vector | lista | Direcciones de los rayos de luz |
| Energy *(opcional)* | `E` | Number | lista | Valores de energía opcionales para cada rayo |
| Lambert | `L` | Boolean | item | Si es True, se aplica sombreado lambertiano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Exposure | `E` | Number | lista | Exposición combinada de cada vértice de la malla. |
| Range | `R` | Domain | item | Rango de exposición de toda la malla. |

### Flip Mesh (FlipM)

Invierte los vectores normales de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a invertir |
| Vertex Normals | `Vn` | Boolean | item | Invierte todas las normales de los vértices |
| Face Normals | `Fn` | Boolean | item | Invierte todas las normales de las caras |
| Face Orientation | `Fo` | Boolean | item | Invierte la orientación de todas las caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | item | Malla invertida |

### Mesh Brep (Mesh)

Crea una malla que aproxima la geometría de un Brep

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Geometría Brep |
| Settings | `S` | MeshParameters | item | Ajustes que usa el algoritmo de mallado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla aproximada |

### Mesh Join (MJoin)

Une un conjunto de mallas en una sola malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Meshes | `M` | Mesh | lista | Mallas a unir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Resultado de la unión de mallas |

### Mesh Shadow (MShadow)

Calcula el contorno de la sombra de un objeto malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla que proyecta la sombra |
| Light | `L` | Vector | item | Dirección de los rayos de luz |
| Plane | `P` | Plane | item | Plano que recibe las sombras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Outlines | `O` | Curve | lista | Contornos de la sombra |

### Mesh Split Plane (MSplit)

Divide una malla con un plano infinito.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a dividir |
| Plane | `P` | Plane | item | Plano de corte |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Above | `A` | Mesh | lista | Piezas sobre el plano. |
| Below | `B` | Mesh | lista | Piezas bajo el plano. |

### Mesh Surface (Mesh UV)

Crea una malla UV de superficie

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Surface | `S` | Surface | item | Geometría de la superficie |
| U Count | `U` | Integer | item | Cantidad de cuadriláteros en la dirección U |
| V Count | `V` | Integer | item | Cantidad de cuadriláteros en la dirección V |
| Overhang | `H` | Boolean | item | Permite que las caras sobresalgan de los recortes |
| Equalize | `Q` | Boolean | item | Igualar la longitud de los tramos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla UV |

### Occlusion (Occ)

Calcula la oclusión para una colección de rayos de visión y obstáculos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Samples | `S` | Point | lista | Puntos de muestreo para la prueba de oclusión |
| Obstructions | `O` | Mesh | lista | Geometría que obstruye |
| Rays | `R` | Vector | lista | Rayos de visión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hits | `H` | Integer | lista | Cantidad de rayos ocluidos por muestra. |
| Occlusion | `O` | Boolean | árbol | Topología de oclusión de cada muestra. |

### Quadrangulate (Quad)

Convierte en cuadriláteros la mayor cantidad posible de triángulos de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a cuadrangular |
| Angle | `A` | Number | item | Umbral de ángulo. Los triángulos que superen este ángulo de quiebre no se fusionan. |
| Ratio | `R` | Number | item | Umbral de proporción. No se consideran los cuadriláteros cuya proporción (diagonal más corta/diagonal más larga) supere el umbral. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla cuadrangulada (no se garantiza que se conviertan todos los triángulos). |
| Count | `N` | Integer | item | Cantidad de triángulos que se convirtieron en cuadriláteros |

### Settings (Custom) (Custom Mesh Settings)

Representa ajustes de malla personalizados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Stitch Seams | `Stitch` | Boolean | item | Si es True, las aristas de caras adyacentes se hacen coincidir. |
| Simple Planes | `Planes` | Boolean | item | Las caras planas se mallan con la menor cantidad posible de triángulos. |
| Refine | `Refine` | Boolean | item | Refina la grilla inicial si supera la tolerancia de precisión. |
| Min Count | `Min` | Integer | item | Cantidad mínima de cuadriláteros de la grilla inicial por cara. |
| Max Count | `Max` | Integer | item | Cantidad máxima de cuadriláteros de la grilla inicial por cara. |
| Aspect Ratio | `Aspect` | Number | item | Proporción máxima de los cuadriláteros de la grilla inicial. |
| Max Distance | `Max Dist` | Number | item | Distancia máxima permitida entre el centro de las aristas y la superficie de base. |
| Max Angle | `Max Angle` | Number | item | Ángulo máximo permitido (en grados) entre las normales de dos cuadriláteros adyacentes. |
| Min Edge | `Min Edge` | Number | item | Longitud de arista mínima permitida. |
| Max Edge | `Max Edge` | Number | item | Longitud de arista máxima permitida. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Settings | `S` | MeshParameters | item | Ajustes de malla suave |

### Settings (Quality) (Smooth)

Representa los ajustes de malla "suave y más lenta".

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Settings | `S` | MeshParameters | item | Ajustes de malla suave |

### Settings (Speed) (Jagged)

Representa los ajustes de malla "irregular y más rápida".

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Settings | `S` | MeshParameters | item | Ajustes de malla gruesa |

### Simple Mesh (SMesh)

Crea una malla que representa un Brep de la forma más simple posible

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Brep | `B` | Brep | item | Brep a mallar; solo se admiten breps con caras triangulares o cuadrangulares. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla |

### Smooth Mesh (MSmooth)

Suaviza los vértices de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a suavizar |
| Strength | `S` | Number | item | Intensidad del suavizado (0.0=nada, 1.0=máximo) |
| Skip Naked | `N` | Boolean | item | Omitir los vértices desnudos |
| Iterations | `I` | Integer | item | Cantidad de pasos sucesivos de suavizado |
| Limit *(opcional)* | `L` | Number | item | Desplazamiento máximo opcional por punto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla suavizada |

### Triangulate (Tri)

Triangula todos los cuadriláteros de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a triangular |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla solo con caras triangulares |
| Count | `N` | Integer | item | Cantidad de cuadriláteros que se triangularon |

### Unify Mesh (UniM)

Unifica las normales de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a unificar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | item | Malla unificada |
| Count | `N` | Integer | item | Cantidad de caras que se invirtieron |

### Unweld Mesh (Unweld)

Separa (desuelda) los pliegues de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a desoldar |
| Angle | `A` | Number | item | Ángulo de desoldadura |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | item | Malla desoldada |

### Weld Mesh (Weld)

Suelda (fusiona) los pliegues de una malla

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla a soldar |
| Angle | `A` | Number | item | Ángulo de soldadura |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Mesh | item | Malla soldada |
