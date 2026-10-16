---
title: "Catálogo Grasshopper — Wb"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Wb"
libraries: ["Weaverbird 0.9.0.1"]
components: 36
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/weaverbird, geometria/mallas, geometria/patrones]
---

# Wb

36 objetos · librería: Weaverbird 0.9.0.1 · autor: Piacentino

Mapas: [[Mapa - Mallas y SubD]] (36) · [[Mapa - Patrones y teselados]] (8)

## Create

### Weaverbird's Mesh From Lines (Weave Back) (wbWeave)

Transforma una lista de líneas en una malla. (Componente experimental que permite probar funciones futuras.) Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | lista | Las líneas de las que obtener la malla |
| Maximum valence | `V` | Integer | item | Valencia máxima de las caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `O` | Mesh | item | La nueva malla |

### Weaverbird's Tile (wbTile)

Tesela algunas caras de una malla según sus propiedades laterales y una regla elegida. (Componente experimental que permite probar funciones futuras.) Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| FillStrategy | `F` | TessellationEnum | item | La estrategia de relleno. 0: Skip, sin inserciones en las caras objetivo. 1: Best, usa la mejor combinación disponible hoy. 2: Triangle Fan, un abanico de triángulos con un punto central adicional. 3: Triangle Hand, una serie de triángulos que apuntan todos al vértice cero. 4: Triangle Knit, los triángulos parten del vértice 0 y siguen en forma rectangular. 5: Triangle Zigzag, los triángulos parten del vértice 0 y se alternan. 6: Quad Stitch, coloca cuadriláteros salvo en el último segmento si es impar. 7: Quad Fan, agrega un punto central y coloca cuadriláteros cada dos aristas. |
| Opt-in | `O` | TessellationApplyToEnum | item | Aplica el teselado a estas caras. 0: All Faces, todas las caras. 1: Quads And More, todas excepto triángulos. 2: Penta And More, todas excepto triángulos y cuadriláteros. 9: Tris, solo triángulos. 16: Quads, solo cuadriláteros. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

## Define

### Weaverbird's Mesh Antiprism (wbAntiprism)

Construye una forma sólida (antiprisma). Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane *(opcional)* | `P` | Plane | item | Un plano usado para formar la base del sólido |
| Width *(opcional)* | `W` | Number | item | El ancho del círculo base |
| NumberOfSides *(opcional)* | `S` | Integer | item | La cantidad de lados del polígono base |
| TopPoint *(opcional)* | `T` | Point | item | El punto que define la parte superior del sólido |
| BasePolygonMethod *(opcional)* | `C` | Boolean | item | True: el ancho se refiere al radio de la circunferencia circunscrita. False: se refiere a la circunferencia inscrita |
| FillStrategy *(opcional)* | `F` | TessellationEnum | item | La estrategia de relleno. 0: Skip, sin inserciones en las caras objetivo. 1: Best, usa la mejor combinación disponible hoy. 2: Triangle Fan, un abanico de triángulos con un punto central adicional. 3: Triangle Hand, una serie de triángulos que apuntan todos al vértice cero. 4: Triangle Knit, los triángulos parten del vértice 0 y siguen en forma rectangular. 5: Triangle Zigzag, los triángulos parten del vértice 0 y se alternan. 6: Quad Stitch, coloca cuadriláteros salvo en el último segmento si es impar. 7: Quad Fan, agrega un punto central y coloca cuadriláteros cada dos aristas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Mesh | item | La malla resultante |

### Weaverbird's Mesh Dipyramid (wbDipyramid)

Construye una forma sólida (bipirámide). Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane *(opcional)* | `P` | Plane | item | Un plano usado para formar la base del sólido |
| Width *(opcional)* | `W` | Number | item | El ancho del círculo base |
| NumberOfSides *(opcional)* | `S` | Integer | item | La cantidad de lados del polígono base |
| TopPoint *(opcional)* | `T` | Point | item | El punto que define la parte superior del sólido |
| BasePolygonMethod *(opcional)* | `C` | Boolean | item | True: el ancho se refiere al radio de la circunferencia circunscrita. False: se refiere a la circunferencia inscrita |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Mesh | item | La malla resultante |

### Weaverbird's Mesh Mesh Icosahedron (wbIcosahedron)

Construye una malla (icosaedro de malla). Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane *(opcional)* | `P` | Plane | item | Un plano usado para formar la base del prisma |
| Radius *(opcional)* | `W` | Number | item | El radio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Mesh | item | La malla resultante |

### Weaverbird's Mesh Prism (wbPrism)

Construye una forma sólida (prisma). Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane *(opcional)* | `P` | Plane | item | Un plano usado para formar la base del sólido |
| Width *(opcional)* | `W` | Number | item | El ancho del círculo base |
| NumberOfSides *(opcional)* | `S` | Integer | item | La cantidad de lados del polígono base |
| TopPoint *(opcional)* | `T` | Point | item | El punto que define la parte superior del sólido |
| BasePolygonMethod *(opcional)* | `C` | Boolean | item | True: el ancho se refiere al radio de la circunferencia circunscrita. False: se refiere a la circunferencia inscrita |
| FillStrategy *(opcional)* | `F` | TessellationEnum | item | La estrategia de relleno. 0: Skip, sin inserciones en las caras objetivo. 1: Best, usa la mejor combinación disponible hoy. 2: Triangle Fan, un abanico de triángulos con un punto central adicional. 3: Triangle Hand, una serie de triángulos que apuntan todos al vértice cero. 4: Triangle Knit, los triángulos parten del vértice 0 y siguen en forma rectangular. 5: Triangle Zigzag, los triángulos parten del vértice 0 y se alternan. 6: Quad Stitch, coloca cuadriláteros salvo en el último segmento si es impar. 7: Quad Fan, agrega un punto central y coloca cuadriláteros cada dos aristas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Mesh | item | La malla resultante |

### Weaverbird's Mesh Pyramid (wbPyramid)

Construye una forma sólida (pirámide). Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane *(opcional)* | `P` | Plane | item | Un plano usado para formar la base del sólido |
| Width *(opcional)* | `W` | Number | item | El ancho del círculo base |
| NumberOfSides *(opcional)* | `S` | Integer | item | La cantidad de lados del polígono base |
| TopPoint *(opcional)* | `T` | Point | item | El punto que define la parte superior del sólido |
| BasePolygonMethod *(opcional)* | `C` | Boolean | item | True: el ancho se refiere al radio de la circunferencia circunscrita. False: se refiere a la circunferencia inscrita |
| FillStrategy *(opcional)* | `F` | TessellationEnum | item | La estrategia de relleno. 0: Skip, sin inserciones en las caras objetivo. 1: Best, usa la mejor combinación disponible hoy. 2: Triangle Fan, un abanico de triángulos con un punto central adicional. 3: Triangle Hand, una serie de triángulos que apuntan todos al vértice cero. 4: Triangle Knit, los triángulos parten del vértice 0 y siguen en forma rectangular. 5: Triangle Zigzag, los triángulos parten del vértice 0 y se alternan. 6: Quad Stitch, coloca cuadriláteros salvo en el último segmento si es impar. 7: Quad Fan, agrega un punto central y coloca cuadriláteros cada dos aristas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Mesh | item | La malla resultante |

### Weaverbird's Polylines Dodecahedron (wbDodecahedron)

Construye una malla (dodecaedro de polilíneas). Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Plane *(opcional)* | `P` | Plane | item | Un plano usado para formar la base del prisma |
| Radius *(opcional)* | `W` | Number | item | El radio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutPolylines | `P` | Curve | item | El conjunto de polilíneas resultante |

## Extract

### Weaverbird's Dual graph (wbDual)

Este componente calcula el dual débil de la malla. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Dual Mode | `M` | DualModeEnum | item | El método usado para construir los puntos de las caras. 0: Vertex Average, modo dual por promedio de vértices. 1: Keep Size, modo dual que conserva el tamaño. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Face Polylines (wbFacePolys)

Devuelve la representación poligonal de una malla, como si cada cara fuera un circuito cerrado de polilínea. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla abierta o cerrada de la que extraer las caras. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygons | `P` | Curve | item | La lista de polígonos cerrados que forman la malla |

### Weaverbird's Join Meshes and Weld (wbJoin)

Devuelve un único objeto malla formado a partir de una lista de mallas. La malla nueva es más liviana: ocupa menos que la suma de las originales. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M+` | Mesh | lista | Una lista de mallas abiertas o cerradas |
| Weld | `W` | Boolean | item | Indica si se unen los puntos coincidentes de las caras después de la unión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla construida |

### Weaverbird's Mesh Edges (wbEdges)

Devuelve la representación en alambre (wireframe) de una malla. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh or Polylines | `G` | Geometry | lista | La malla abierta o cerrada, o el grupo de polilíneas cerradas, del que extraer el wireframe. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Lines | `L` | Line | item | La lista de alambres (líneas de arista) que forman la malla |

### Weaverbird's Naked boundary (wbNaked)

Busca la policurva desnuda (cubierta por una sola cara) como la unión de varias aristas desnudas. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Closed Polylines | `M` | Geometry | lista | La malla o polilínea cerrada en la que buscar lados desnudos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Naked curves | `C` | Curve | item | Las curvas que forman el borde desnudo |

### Weaverbird's Reroute Faces (wbReroute)

Devuelve una malla nueva formada por una sublista de caras. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla abierta o cerrada |
| Index | `N+` | Integer | lista | Los índices de las caras nuevas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh0 | `R0` | Mesh | item | La malla positiva |
| Mesh1 | `R1` | Mesh | item | La malla negativa |

### Weaverbird's Reroute Faces by Pattern (wbReroutePattern)

Devuelve una malla nueva formada por una sublista de caras: las caras 'True' van a una salida y las 'False' a la otra. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla abierta o cerrada |
| Index | `P+` | Boolean | lista | El patrón con el que comparar las caras |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh0, containing 'true' values | `T` | Mesh | item | La malla positiva |
| Mesh1, containing 'false' values | `F` | Mesh | item | La malla negativa |

### Weaverbird's Unify face windings (wbUnify)

Se asegura de que el sentido de giro de las caras sea uno solo, cuando es posible. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Vertices Component (wbVertices)

Devuelve la representación en puntos de una malla. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Closed polylines group | `G` | Geometry | lista | La malla abierta o cerrada, o el grupo de polilíneas cerradas, del que extraer los puntos. |
| Weld *(opcional)* | `W` | Boolean | item | ¿Se eliminan todos los puntos coincidentes? |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Points | `P` | Point | item | La lista de puntos que forman la malla |

## Smoothen

### Weaverbird's Blur Mesh (wbBlur)

Calcula una representación suavizada de una malla original, pero solo en cuanto a colores y coordenadas de vértices. No aumenta la cantidad de caras. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Thin | `T` | Number | item | El adelgazamiento final, de una sola vez, con la malla original |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Laplacian Smoothing (wbLaplace)

Calcula una representación suavizada de una malla original. No aumenta la cantidad de caras. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Smooth Naked Edges *(opcional)* | `S` | NakedEdgeEnum | item | Define cómo tratar las aristas desnudas. 0: Fixed, no se mueven ni se modifican. 1: Smooth, tienden a una spline. 2: Corner Fixed, las esquinas (vértices con 2 lados) quedan fijas y los demás vértices desnudos tienden a una spline. |
| Thin | `T` | Number | item | El adelgazamiento final, de una sola vez, con la malla original |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's LaplacianHC Smoothing (wbLaplaceHC)

Calcula una representación suavizada de una malla original. No aumenta la cantidad de caras. Permite indicar un aumento de volumen. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Smooth Naked Edges *(opcional)* | `S` | NakedEdgeEnum | item | Define cómo tratar las aristas desnudas. 0: Fixed, no se mueven ni se modifican. 1: Smooth, tienden a una spline. 2: Corner Fixed, las esquinas (vértices con 2 lados) quedan fijas y los demás vértices desnudos tienden a una spline. |
| Partial-Original | `P` | Number | item | La parte de la malla original a usar de forma incremental después de la primera operación de suavizado. Solo afecta niveles mayores que 1. Permite transiciones con menos ruido en niveles altos |
| Orientation | `O` | Number | item | La orientación e intensidad del vector que conserva el volumen. La mayoría de las veces se puede dejar en 0 |
| Volume-Saving activation | `A` | Number | item | La activación, de 0 a 1, del vector que conserva el volumen. En 0, la operación pasa a ser un suavizado laplaciano normal |
| Thin | `T` | Number | item | El adelgazamiento final, de una sola vez, con la malla original |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

## SubD

### Weaverbird's Catmull-Clark Subdivision (wbCatmullClark)

Calcula la subdivisión recursiva de mallas descrita por Edwin Catmull y Jim Clark, en su paper de 1978. La malla resultante siempre está formada por caras cuadrangulares. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Smooth Naked Edges *(opcional)* | `S` | NakedEdgeEnum | item | Define cómo tratar las aristas desnudas. 0: Fixed, no se mueven ni se modifican. 1: Smooth, tienden a una spline. 2: Corner Fixed, las esquinas (vértices con 2 lados) quedan fijas y los demás vértices desnudos tienden a una spline. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Constant Quads Split Subdivision (wbSplitQuads)

Calcula una malla de solo cuadriláteros y de aspecto similar, que se obtiene agregando una cara por cada arista de la malla original. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Smooth Naked Edges *(opcional)* | `S` | NakedEdgeEnum | item | Define cómo tratar las aristas desnudas. 0: Fixed, no se mueven ni se modifican. 1: Smooth, tienden a una spline. 2: Corner Fixed, las esquinas (vértices con 2 lados) quedan fijas y los demás vértices desnudos tienden a una spline. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Inner Polygons Subdivision (wbInnerPolygons)

Coloca una cara nueva que parte del punto medio de cada arista de cada cara original. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Loop Subdivision (wbLoop)

Calcula la subdivisión recursiva de mallas descrita por Charles Loop en su tesis de matemáticas de 1987. Funciona mejor si la malla de entrada es completamente de triángulos; la resultante también tiene siempre caras triangulares. Usa wbOptions para cambiar la fórmula. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Smooth Naked Edges *(opcional)* | `S` | NakedEdgeEnum | item | Define cómo tratar las aristas desnudas. 0: Fixed, no se mueven ni se modifican. 1: Smooth, tienden a una spline. 2: Corner Fixed, las esquinas (vértices con 2 lados) quedan fijas y los demás vértices desnudos tienden a una spline. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Midedge Subdivision (wbMidedge)

Calcula la subdivisión recursiva de mallas que se obtiene dividiendo las aristas en su punto medio. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Smooth Naked Edges *(opcional)* | `S` | NakedEdgeEnum | item | Define cómo tratar las aristas desnudas. 0: Fixed, no se mueven ni se modifican. 1: Smooth, tienden a una spline. 2: Corner Fixed, las esquinas (vértices con 2 lados) quedan fijas y los demás vértices desnudos tienden a una spline. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Sierpinski Triangles Subdivision (wbSierpinski)

Coloca un triángulo en cada esquina de una cara de la malla. La malla tendrá un agujero más por cara. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Split Polygons Subdivision (wbSplitPolygons)

Coloca una cara nueva que parte del punto medio de cada arista de cada cara original y tapa el agujero con triángulos de Sierpinski. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |
| Smooth Naked Edges *(opcional)* | `S` | NakedEdgeEnum | item | Define cómo tratar las aristas desnudas. 0: Fixed, no se mueven ni se modifican. 1: Smooth, tienden a una spline. 2: Corner Fixed, las esquinas (vértices con 2 lados) quedan fijas y los demás vértices desnudos tienden a una spline. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

### Weaverbird's Split Triangles Subdivision (wbTriangles)

Coloca varios triángulos en cada cara. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a subdividir |
| Level *(opcional)* | `L` | Integer | item | La cantidad de iteraciones de subdivisión de cada cara |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del proceso de subdivisión |

## Transform

### Weaverbird's Bevel Edges (wbBevelEdges)

Reemplaza cada arista de la malla original por una cara nueva que conecta los dos vértices y, por el lado largo, las dos caras. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Polylines | `M` | Geometry | lista | La malla, o lista de polilíneas, a procesar. |
| Distance *(opcional)* | `D` | Number | lista | El valor escalar usado para construir los nuevos vértices interiores. La distancia puede darse como lista, donde cada valor se aplica al elemento correspondiente de la malla de entrada. |
| InsetType *(opcional)* | `T` | InsetTypeEnum | item | Definición de la distancia de los vértices nuevos. 0: Percent, porcentaje de la longitud de la arista (debe ser < 50). 1: Parallelogram, regla del paralelogramo (valor menor que la arista más corta / 2). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Geometry | item | La malla después del proceso |

### Weaverbird's Bevel Vertices (wbBevelVertices)

Reemplaza cada vértice de la malla original por una cara nueva que conecta todas las aristas. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Polylines | `M` | Geometry | lista | La malla, o lista de polilíneas, a procesar. |
| Distance *(opcional)* | `D` | Number | lista | El valor escalar usado para construir los nuevos vértices interiores. La distancia puede darse como lista, donde cada valor se aplica al elemento correspondiente de la malla de entrada. |
| InsetType *(opcional)* | `T` | InsetTypeEnum | item | Definición de la distancia de los vértices nuevos. 0: Percent, porcentaje de la longitud de la arista (debe ser < 50). 1: Parallelogram, regla del paralelogramo (valor menor que la arista más corta / 2). |
| Output geometry as mesh | `M` | Boolean | item | True si quieres mallas como resultado; False en otro caso. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Geometry | item | La malla después del proceso |

### Weaverbird's Mesh Thicken (wbThicken)

Calcula una malla nueva que es un sólido cerrado, siempre que a la malla original se le pueda aplicar offset y esté orientada. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a modificar |
| Distance *(opcional)* | `D` | Number | lista | La lista de distancias a usar para construir los nuevos vértices interiores. Una distancia por vértice |
| OffsetType *(opcional)* | `T` | OffsetTypeEnum | item | Definición de la distancia de los vértices nuevos. 0: Distance On Diagonals, la medida sobre la diagonal decide el offset. 1: Hypotenuse Average, trigonométrico (experimental). 2: Planes Intersections, intersección de planos; funciona mejor con vértices de valencia tres (experimental). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del offset |

### Weaverbird's Mesh Window (wbWindow)

Reemplaza cada cara de la malla original por una nueva, reconstruida hacia adentro. Cada cara tiene la misma cantidad de lados que la original. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Polylines | `M` | Geometry | lista | La malla, o lista de polilíneas, a procesar. |
| Distance *(opcional)* | `D` | Number | lista | El valor escalar usado para construir los nuevos vértices interiores. La distancia puede darse como lista, donde cada valor se aplica al elemento correspondiente de la malla de entrada. |
| InsetType *(opcional)* | `T` | InsetTypeEnum | item | Definición de la distancia de los vértices nuevos. 0: Percent, porcentaje de la longitud de la arista (debe ser < 50). 1: Parallelogram, regla del paralelogramo (valor menor que la arista más corta / 2). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Geometry | item | La malla después del proceso |

### Weaverbird's Offset Mesh (wbOffset)

Calcula un offset de mallas. El resultado es abierto si la entrada es abierta. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Curves | `M` | Geometry | lista | La malla abierta o cerrada, o la lista de curvas cerradas, a modificar |
| Distance *(opcional)* | `D` | Number | lista | La lista de distancias a usar para construir los nuevos vértices interiores. Una distancia por vértice |
| OffsetType *(opcional)* | `T` | OffsetTypeEnum | item | Definición de la distancia de los vértices nuevos. 0: Distance On Diagonals, la medida sobre la diagonal decide el offset. 1: Hypotenuse Average, trigonométrico (experimental). 2: Planes Intersections, intersección de planos; funciona mejor con vértices de valencia tres (experimental). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output Mesh/Curves | `O` | Geometry | item | La malla después del offset |

### Weaverbird's Picture Frame (wbFrame)

Calcula una malla nueva de género mayor, donde cada cara tiene un agujero nuevo al centro y parece un marco de cuadro. La malla resultante siempre está formada por caras cuadrangulares. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Polylines | `M` | Geometry | lista | La malla, o lista de polilíneas, a procesar. |
| Distance *(opcional)* | `D` | Number | lista | El valor escalar usado para construir los nuevos vértices interiores. La distancia puede darse como lista, donde cada valor se aplica al elemento correspondiente de la malla de entrada. |
| InsetType *(opcional)* | `T` | InsetTypeEnum | item | Definición de la distancia de los vértices nuevos. 0: Percent, porcentaje de la longitud de la arista (debe ser < 50). 1: Parallelogram, regla del paralelogramo (valor menor que la arista más corta / 2). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Geometry | item | La malla después del proceso |

### Weaverbird's Sierpinski Carpet (wbCarpet)

Calcula una malla nueva de género mayor, donde cada cara tiene un agujero nuevo al centro. La malla resultante siempre está formada por caras cuadrangulares. Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Polylines | `M` | Geometry | lista | La malla, o lista de polilíneas, a procesar. |
| Distance *(opcional)* | `D` | Number | lista | El valor escalar usado para construir los nuevos vértices interiores. La distancia puede darse como lista, donde cada valor se aplica al elemento correspondiente de la malla de entrada. |
| InsetType *(opcional)* | `T` | InsetTypeEnum | item | Definición de la distancia de los vértices nuevos. 0: Percent, porcentaje de la longitud de la arista (debe ser < 50). 1: Parallelogram, regla del paralelogramo (valor menor que la arista más corta / 2). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Geometry | item | La malla después del proceso |

### Weaverbird's Stellate/Cumulation (wbStellate)

Agrega una pirámide sobre cada cara (a veces llamado kis). (Componente experimental que permite probar funciones futuras.) Provisto por Weaverbird 0.9.0.1.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh/Polylines | `M` | Geometry | lista | La malla, o lista de polilíneas, a procesar. |
| Distance *(opcional)* | `D` | Number | lista | El valor escalar usado para construir los nuevos vértices interiores. La distancia puede darse como lista, donde cada valor se aplica al elemento correspondiente de la malla de entrada. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| OutMesh | `O` | Geometry | item | La malla después del proceso |
