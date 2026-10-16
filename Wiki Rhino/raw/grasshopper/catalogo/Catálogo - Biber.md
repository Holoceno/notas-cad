---
title: "Catálogo Grasshopper — Biber"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Biber"
libraries: ["Biber 1.4.0.3", "Endoframe 1.2.0.0"]
components: 118
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/biber, fabricacion, geometria/brep]
---

# Biber

118 objetos · librería: Biber 1.4.0.3, Endoframe 1.2.0.0

Mapas: [[Mapa - Fabricación]] (118) · [[Mapa - Brep y sólidos]] (15) · [[Mapa - Simulación, optimización y ML]] (7)

## Assemble Tools

### Assemble (DM)

Toma una polisuperficie poligonal de entrada y crea un ensamble a partir de sus polígonos planos. Las caras y polígonos se convierten en Shells 3D, las aristas en Joints y los vértices en elementos Node

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Shell type *(opcional)* | `St` | Shell type | lista | Define cómo se crea una pieza a partir de una superficie plana. Una pieza puede ubicarse arriba, al medio o arriba de la cara. |
| Joint type *(opcional)* | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |
| Node type *(opcional)* | `Nt` | Node type | lista | Define cómo se tratan varias piezas alrededor de un nodo común. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |

### Breps to PPS (BTPPS)

Convierte un conjunto de breps planos que se intersectan en una PPS (Planar Poly-Surface) que se puede usar para crear un ensamble

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Breps | `PB` | Brep | lista | Un conjunto de breps planos. |
| Planarity tolerance *(opcional)* | `PlTol` | Number | item | La desviación de la superficie del polígono respecto de un plano. Este valor debe ser consistente en todos los componentes de EndoFrame. |
| Proximity tolerance *(opcional)* | `PrTol` | Number | item | La distancia mínima a la que dos puntos se consideran distintos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

### Disassemble (D)

Explota un ensamble en sus componentes (Shells, Joints y Node). Cada uno de estos subcomponentes puede tener o no una representación como polisuperficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Part | `P` | Part | lista | Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional útil para el anidado (nesting) y el etiquetado de las piezas. |
| Joint | `J` | Joint | lista | Un joint contiene la geometría creada a lo largo de las aristas de las piezas (si existe), además de información adicional útil para etiquetar y crear subestructuras que sostienen las piezas a lo largo de las aristas. |
| Node | `N` | Node | lista | Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos. |

### Disassemble Joint (Joint)

Obtiene la información de los elementos Shell, como objetos sólidos, superficies, etc.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint | `J` | Joint | item | Un joint contiene la geometría creada a lo largo de las aristas de las piezas (si existe), además de información adicional útil para etiquetar y crear subestructuras que sostienen las piezas a lo largo de las aristas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell index | `SI` | Integer | lista | Índice de los shells asociados a este joint |
| Node index | `NI` | Integer | lista | Índice de los nodos asociados a este joint |
| Joint index | `JI` | Integer | item | Índice de los elementos joint asociados a este elemento |
| Geometries | `Geom` | Geometry | lista | Según el elemento joint, entrega geometrías adicionales para sumar o restar del shell. |
| Surface | `Srf` | Brep | árbol | Superficies que se eliminan de los elementos shell a lo largo de las aristas. |
| Joint angle | `JA` | Number | lista | El ángulo entre dos shells consecutivos en el joint. Para joints manifold solo se entrega el ángulo interior. |

### Disassemble Node (Node)

Obtiene la información de los elementos Node, como objetos sólidos, superficies, índices, etc.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Node | `N` | Node | item | Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell index | `SI` | Integer | lista | Índice de los elementos shell asociados a este elemento |
| Joint index | `JI` | Integer | lista | Índice de los elementos joint asociados a este elemento |
| Node index | `NI` | Integer | item | Índice de los elementos nodo asociados a este elemento |
| Breps | `B` | Brep | árbol | Según el elemento nodo, puede entregar geometría sólida para fabricarse por separado. |
| Surface | `Srf` | Brep | árbol | Superficies que se eliminan de los elementos shell alrededor de las esquinas. |
| Node Plane | `NPln` | Plane | item | Plano en el nodo |
| Node Vertex | `Pt` | Point | item | La ubicación del vértice |

### Disassemble Shell (Shell)

Obtiene la información de los elementos Shell: índice del shell e índices de aristas y nodos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Part | `P` | Part | item | Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional útil para el anidado (nesting) y el etiquetado de las piezas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell index | `SI` | Integer | item | Índice de los elementos shell asociados a este elemento |
| Node index | `NI` | Integer | lista | Índice de los elementos nodo asociados a este elemento |
| Joint index | `JI` | Integer | lista | Índice de los elementos joint asociados a este elemento |
| Edge Labels (Top) | `E.L.T` | Plane | lista | Planos en el punto medio de las aristas de la cara superior de la pieza. |
| Edge Labels (Bottom) | `E.L.B` | Plane | lista | Planos en el punto medio de las aristas de la cara inferior de la pieza. |

### Fillet Shell Edges (FSE)

Aplica fillet a las aristas del shell según su tipo. Las aristas convexas/cóncavas y de superficie se pueden redondear por separado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Part | `P` | Part | item | Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional útil para el anidado (nesting) y el etiquetado de las piezas. |
| Fillet concave corners | `ConcE` | Number | item | Permite redondear las esquinas cóncavas. |
| Fillet convex corners | `ConvE` | Number | item | Permite redondear las esquinas convexas. |
| Fillet surface edges | `SurfE` | Number | item | Permite redondear las aristas que están en la superficie superior o inferior del shell. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | lista | Polisuperficie cerrada creada a partir del polígono de la malla |

### Merge PPS (M.P.P.S)

Fusiona varias PPS (Planar Poly-Surface) en una sola PPS

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | lista | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

### Mesh to PPS (MTPPS)

Convierte una malla en una PPS (Planar Poly-Surface) que se puede usar para crear un ensamble

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla de entrada |
| Planarity tolerance *(opcional)* | `PlTol` | Number | item | La desviación de la superficie del polígono respecto de un plano. Este valor debe ser consistente en todos los componentes de EndoFrame. |
| Proximity tolerance *(opcional)* | `PrTol` | Number | item | La distancia mínima a la que dos puntos se consideran distintos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

### Shell Geometry (SG)

Construye la geometría del shell y algunos objetos auxiliares para el proceso de fresado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Part | `P` | Part | item | Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional útil para el anidado (nesting) y el etiquetado de las piezas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell index | `SI` | Integer | item | Índice de los elementos shell asociados a este elemento |
| Convex edges | `CE` | Line | lista | Extrae las aristas convexas del shell sólido |
| Convex faces | `ConvF` | Brep | lista | Extrae las caras que no tienen esquinas convexas |
| Solid | `S` | Brep | item | La geometría sólida de la pieza, si existe |
| Top plane | `PL` | Plane | item | El plano superior orientado hacia donde apunta la mayoría de las caras |
| Raw part | `RP` | Curve | item | La polilínea que rodea la pieza en el plano superior. Puedes usarla para el anidado (nesting). |

### Sub-PPS (SPPS)

Crea una PPS (Planar Poly-Surface) parcial a partir de los componentes de otra PPS

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Polygon keys *(opcional)* | `P` | Integer | lista | Los índices de los polígonos que se incluyen en esta Polygon-Surface parcial |
| Edge keys *(opcional)* | `E` | Integer | lista | Los índices de las aristas que se incluyen en esta Polygon-Surface parcial |
| Vertex keys *(opcional)* | `V` | Integer | lista | Los índices de los vértices que se incluyen en esta Polygon-Surface parcial |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

## Joints

### Add feature (A.F.)

Agrega una serie de elementos (features) en la pieza objetivo a lo largo del joint, transformando la geometría de entrada desde el plano base hasta la cara superior o inferior de la pieza de referencia. Puedes elegir entre distintos métodos de arreglo (Count o Spacing) y controlar la posición y profundidad de los elementos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Obj | `Obj.` | Brep | item | La geometría se orienta desde el plano base hasta la cara superior o inferior de la pieza de referencia. |
| Base plane | `Base.` | Plane | item | La geometría se reubica en el joint respecto del plano de referencia. El plano de referencia es el plano XY por defecto. |
| Count | `Cnt.` | Integer | item | Si Spacing es cero (por defecto), Count define la cantidad de copias que se crean a lo largo del joint; si no, la cantidad de elementos se calcula según Spacing y Count solo define la cantidad mínima de elementos. |
| Spacing | `Spc.` | Number | item | Define la distancia de centro a centro entre copias a lo largo del joint, mientras Count define la cantidad mínima de elementos a crear. |
| Start | `St.` | Number | item | Desfase desde el inicio del joint. |
| End | `St.` | Number | item | Desfase desde el final del joint. |
| Target | `T.` | Integer | item | Identifica la pieza que se va a cortar. |
| Reference | `R.` | Integer | item | Selecciona otra pieza para orientar el vacío. |
| Flip | `Fl.` | Boolean | item | Invierte el vacío hacia la cara inferior. |
| Propotional | `Prop.` | Boolean | item | Si es True, la geometría se escala para caber en el espesor de la pieza objetivo. Si no, se usa la geometría real. |
| Open joints | `O.J.` | Boolean | item | Incluye los joints abiertos |
| Joint type | `jt` | Joint type | item | Define cómo se tratan varias piezas a lo largo de una arista común. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | item | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Add feature (A.F.) · 2

Agrega elementos (features) al joint. Un elemento puede ser una cavidad, una adición o un accesorio.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Base joint | `jt` | Joint type | item | El joint base que se modifica agregando elementos nuevos |
| Joint feature | `J.F.` | Joint feature | lista | Elementos (features) que se agregan al joint |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | item | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Barefaced Housing Joint (BHJ)

Crea un joint de alojamiento a cara vista (barefaced housing) a lo largo de la arista, en aristas manifold y no manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Tongue width | `W` | Number | item | Controla el ancho de la lengüeta. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. Valor por defecto: 0.33 |
| Groove depth | `D` | Number | item | Controla la profundidad de la ranura. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. Valor por defecto: 0.4 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Blind Finger Joint (BFJ)

Crea una unión de dedos ciega (blind finger joint)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Spacing | `S` | Number | item | Espacio entre los dedos |
| Depth | `D` | Number | item | Controla cuánto se extiende una pieza dentro de la otra. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. El valor óptimo (por defecto) es ¼, es decir, un cuarto del espesor del shell. |
| Reverse *(opcional)* | `R` | Boolean | item | Invierte el tratamiento del joint a lo largo de la arista. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Butt Joint (BJ)

Crea una unión a tope (butt joint) a lo largo de la arista, en aristas manifold y no manifold. La unión a tope se crea correctamente si el ángulo entre las normales de las dos caras adyacentes es mayor que la tolerancia angular del documento de Rhino; si no, las dos caras se consideran coplanares y se crea una unión a inglete en su lugar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Butt Rub Joint (BRJ)

Crea una unión a tope con refuerzo (butt rub joint) a lo largo de la arista, en aristas manifold y no manifold. Este joint crea soportes adicionales a lo largo de las aristas. Usa el componente Joint para extraer la geometría de los soportes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Size | `S` | Number | item | Controla el tamaño de la cuña en las esquinas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Custom Profile Joint (CPJ)

Ofrece opciones para crear un perfil personalizado a lo largo de las aristas manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Profile segment | `Pseg` | Generic Data | lista | Un segmento de un perfil |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Dovetail Joint (DVTJ)

Crea una unión de cola de milano (dovetail) a lo largo de la arista. Este joint solo se puede usar en aristas manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Dovetail joint setting *(opcional)* | `DTS` | Generic Data | item | Controla la geometría de la unión de cola de milano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Dovetail Joint Settings (DTS)

Entrega todos los ajustes de la unión de cola de milano

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Angle | `TA` | Number | item | Ángulo de las colas de milano en grados |
| Fillet radius | `FR` | Number | item | Radio del fillet |
| Length | `TL` | Number | item | La longitud de las colas en una unión de cola de milano. |
| Spacing | `PS` | Number | item | El espacio entre las colas o el tamaño de los pasadores. |
| Offset | `O` | Number | item | Desfase desde ambos extremos de la arista. Si ingresas cero, el componente busca el desfase automáticamente. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Dovetail joint setting | `DTS` | Generic Data | item | Controla la geometría de la unión de cola de milano |

### Dowel Butt Joint (DBJ)

La unión con tarugos se arma igual que una unión atornillada, solo que en vez de tornillos se pegan trozos de tarugo dentro de perforaciones. Al usar tarugos en vez de tornillos la unión queda mucho más resistente y puede convertirse en un detalle atractivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Depth | `De` | Number | item | Profundidad del tarugo dentro de cada pieza. |
| Diameter | `Di` | Number | item | Diámetro del tarugo. |
| Spacing | `S` | Number | item | Separación entre tarugos. Este valor solo se usa cuando el parámetro de cantidad es cero. |
| Number | `N` | Integer | item | Cantidad de tarugos. Si es cero, la cantidad de tarugos se calcula según el parámetro de separación. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Feature (F.)

Define un elemento (feature) de un joint. Un elemento puede ser aditivo, sustractivo o un accesorio. Un joint puede tener uno o varios elementos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Obj | `Obj.` | Brep | item | La geometría se orienta desde el plano base hasta la cara superior o inferior de la pieza de referencia. |
| Base plane | `Base.` | Plane | item | La geometría se reubica en el joint respecto del plano de referencia. El plano de referencia es el plano XY por defecto. |
| Count | `Cnt.` | Integer | item | Si Spacing es cero (por defecto), Count define la cantidad de copias que se crean a lo largo del joint; si no, la cantidad de elementos se calcula según Spacing y Count solo define la cantidad mínima de elementos. |
| Spacing | `Spc.` | Number | item | Define la distancia de centro a centro entre copias a lo largo del joint, mientras Count define la cantidad mínima de elementos a crear. |
| Start | `St.` | Number | item | Desfase desde el inicio del joint. |
| End | `St.` | Number | item | Desfase desde el final del joint. |
| Target | `T.` | Integer | item | Identifica la pieza que se va a cortar. |
| Reference | `R.` | Integer | item | Selecciona otra pieza para orientar el vacío. |
| Flip | `Fl.` | Boolean | item | Invierte el vacío hacia la cara inferior. |
| Propotional | `Prop.` | Boolean | item | Si es True, la geometría se escala para caber en el espesor de la pieza objetivo. Si no, se usa la geometría real. |
| Open joints | `O.J.` | Boolean | item | Incluye los joints abiertos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint feature | `J.F.` | Joint feature | item | Un elemento (feature) representa una adición, sustracción o accesorio en un joint. |

### Finger Joint (FJ)

Crea una unión de dedos (finger joint)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Count *(opcional)* | `C` | Integer | item | Cantidad de dedos |
| Spacing *(opcional)* | `S` | Number | item | Espacio entre los dedos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Half-lap Joint (HLJ)

Crea una unión a media madera (half-lap) a lo largo de la arista, en aristas manifold y no manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Depth | `D` | Number | item | Controla la profundidad de la ranura. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. El valor óptimo (por defecto) es 0.5. |
| Width | `W` | Number | item | Controla el ancho de la lengüeta. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. El valor óptimo (por defecto) es 0.5. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Keyed Mitered Joint (KMJ)

Crea una unión a inglete con llave (keyed miter) a lo largo de la arista. Este joint solo se puede usar en aristas manifold donde el ángulo entre las caras es menor que 180 grados (caras no coplanares).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Depth | `D` | Number | item | Controla la profundidad real de la ranura. |
| Length | `L` | Number | item | Controla la longitud real de la ranura. |
| Size | `Si` | Number | item | Si es mayor que cero, crea una extensión a la forma en V. |
| Thickness | `T` | Number | item | Controla el espesor de la llave o el ancho de la ranura. |
| Spacing | `Sp` | Number | item | El espacio entre las llaves. |
| On Top | `OnT` | Boolean | item | Si es True, la llave se coloca desde el lado superior (por defecto es False). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Lap Joint (LJ)

Crea una unión a solape (lap joint) a lo largo de la arista, en aristas manifold y no manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Depth | `D` | Number | item | Controla cuánto se extiende una pieza dentro de la otra. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. El valor óptimo (por defecto) es ¼, es decir, un cuarto del espesor del shell. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Lap Mitered Joint (LMJ)

Crea una unión a solape con inglete (lap-mitered) a lo largo de la arista. Este joint solo se puede usar en aristas manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Depth | `D` | Number | item | Controla cuánto se extiende una pieza dentro de la otra. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. El valor óptimo (por defecto) es 0.5, es decir, la mitad del espesor del shell. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Lock Mitered Joint (LMJ)

Crea una unión a inglete con traba (lock miter) a lo largo de la arista. Este joint solo se puede usar en aristas manifold donde el ángulo entre las caras es menor que 180 grados (caras no coplanares).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Depth | `D` | Number | item | Controla la profundidad de la ranura. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. |
| Width | `W` | Number | item | Controla el ancho de la ranura. Es una proporción, no la medida real. El valor debe estar entre 0 y 0.5. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Mitered Joint (MJ)

Unión a inglete.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Chamfer *(opcional)* | `CH` | Number | item | Aplica chamfer a las aristas de los shells opuestos. Es útil en una unión en cruz cuando los shells opuestos son coplanares. El valor debe estar entre 0 y 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Mitered Lap Joint (MLJ)

Crea una unión a inglete con solape (mitered lap) a lo largo de la arista. Este joint solo se puede usar en aristas manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Depth | `D` | Number | item | Controla cuánto se extiende una pieza dentro de la otra. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. El valor óptimo (por defecto) es 0.5, es decir, la mitad del espesor del shell. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Null Shape (Nseg)

Crea una forma nula

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Segment length *(opcional)* | `Len` | Number | item | Longitud del segmento |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint profile segment | `JPS` | Joint profile segment | item | Define un único segmento de perfil en un perfil de joint personalizado. |

### Open Joint (OJ)

Alinea la cara de las aristas abiertas con el plano de entrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Alignment plane | `PL` | Plane | item | El plano con el que se debe alinear la cara. Por defecto es el plano XY del mundo |
| Angle threshold | `A` | Number | item | El umbral de ángulo en grados. Si el ángulo de la cara con el plano de entrada es menor que este umbral, la cara se alinea con el plano. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Simplified Mitered Joint (default) (SMJ)

Una versión simple de la unión a inglete, sin variaciones. Todos los shells se encuentran en el centro de la intersección.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Splined Miter Joint (SMJ)

Unión a inglete con lengüeta (splined miter).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Width | `L` | Number | item | La longitud del pasador. |
| Depth | `TH` | Number | item | Espesor del pasador. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### Tongue & Groove Joint (TAGJ)

Crea una unión machihembrada (tongue & groove) a lo largo de la arista, en aristas manifold y no manifold.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |
| Extension | `E` | Number | item | Cuánto debe sobresalir el joint más allá de la pieza opuesta. Usa un valor mayor que cero si quieres esmerilar o lijar las superficies después del ensamble. |
| Angle threshold | `AT` | Number | item | Umbral de ángulo en grados. Optimiza la geometría del joint cuando el ángulo entre las caras es menor que este valor. |
| Tongue width | `TW` | Number | item | Controla el ancho de la lengüeta respecto del espesor del shell. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. |
| Groove depth | `GD` | Number | item | Controla la longitud de la lengüeta dentro del otro shell. Es una proporción, no la medida real. El valor debe estar entre 0 y 1. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

### U Shape (Useg)

Crea una forma de U con esquinas redondeadas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Segment length *(opcional)* | `Len` | Number | item | Longitud del segmento |
| Height | `H` | Number | item | Altura del segmento. |
| Angle1 | `Ang1` | Number | item | Ángulo (en grados) de la arista izquierda respecto de la línea perpendicular al joint. |
| Angle2 | `Ang2` | Number | item | Ángulo (en grados) de la arista derecha respecto de la línea perpendicular al joint. |
| Radius | `Rad` | Number | item | El radio del fillet |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint profile segment | `JPS` | Joint profile segment | item | Define un único segmento de perfil en un perfil de joint personalizado. |

### User defined profile segment (UDPS)

Un segmento de perfil personalizado definido por una curva plana en el plano XY. La curva de entrada debe empezar y terminar sobre el eje X.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Curve | `C` | Curve | item | Una curva plana en el plano XY que intersecta el eje X |
| Depth | `D` | Number | item | Controla cuánto corta el perfil de las piezas a lo largo del joint. Normalmente es 1.0, que equivale al espesor del material: el perfil se estira para cubrir todo el espesor de la pieza. Los valores mayores que 1.0 solo deben usarse con joints híbridos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint profile segment | `JPS` | Joint profile segment | lista | Define un único segmento de perfil en un perfil de joint personalizado. |

### Waffle Joint (WJ)

Crea una unión tipo waffle entre shells coplanares que se intersectan

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edges *(opcional)* | `I` | Integer | lista | Los índices de las aristas de la malla que se tratarán con este joint. Esta entrada es opcional; si se deja vacía, todas las aristas se tratan con este joint. |
| Gap | `G` | Number | item | Separación entre los shells en el joint. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint type | `jt` | Joint type | lista | Define cómo se tratan varias piezas a lo largo de una arista común. |

## Material Library

### Birch Multiplex

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Material sheet | `MS` | Rectangle | lista | Un objeto rectángulo que representa la plancha de material |

### Blockboard light-core

Bla bla bla

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Material sheet | `MS` | Rectangle | lista | Un objeto rectángulo que representa la plancha de material |

### Maritime Pine Plywood

Bla bla bla

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Material sheet | `MS` | Rectangle | lista | Un objeto rectángulo que representa la plancha de material |

### Poplar Plywood

Bla bla bla

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Material sheet | `MS` | Rectangle | lista | Un objeto rectángulo que representa la plancha de material |

### Tischlerplatte Pappel

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Material | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Material sheet | `MS` | Rectangle | lista | Un objeto rectángulo que representa la plancha de material |

## Nodes

### Coarse Node (CN)

Resuelve la intersección de los elementos shell recortando cada pieza con la opuesta. Esto puede dejar algunos nodos sin resolver; los nodos sin resolver se pueden limpiar con un nodo de recorte simple o múltiple.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices *(opcional)* | `I` | Integer | lista | Los índices de los vértices de la malla que se tratarán con este nodo. Esta entrada es opcional; si se deja vacía, todos los vértices se tratan con este nodo. |
| Offset *(opcional)* | `O` | Number | item | El tratamiento del joint empieza con un desfase desde la ubicación del vértice. |
| Gap | `G` | Number | item | Separación creada entre los elementos shell en la ubicación del nodo. No se recomiendan valores menores que la tolerancia absoluta del modelo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Node | `N` | Node | lista | Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos. |

### Multi-trims Node (MTN)

Resuelve la intersección de los elementos shell con varias operaciones de recorte entre cada par de shells que se intersectan.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices *(opcional)* | `I` | Integer | lista | Los índices de los vértices de la malla que se tratarán con este nodo. Esta entrada es opcional; si se deja vacía, todos los vértices se tratan con este nodo. |
| Offset *(opcional)* | `O` | Number | item | El tratamiento del joint empieza con un desfase desde la ubicación del vértice. |
| Gap | `G` | Number | item | Separación creada entre los elementos shell en la ubicación del nodo. No se recomiendan valores menores que la tolerancia absoluta del modelo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Node | `N` | Node | lista | Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos. |

### Null Node (default) (NN)

Un nodo nulo no hace nada y deja el vértice sin tratar. Usa este componente en los vértices con menos de 3 caras.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices *(opcional)* | `I` | Integer | lista | Los índices de los vértices de la malla que se tratarán con este nodo. Esta entrada es opcional; si se deja vacía, todos los vértices se tratan con este nodo. |
| Offset *(opcional)* | `O` | Number | item | El tratamiento del joint empieza con un desfase desde la ubicación del vértice. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Node | `N` | Node | lista | Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos. |

### Overlap Killer Node (O.K.N.)

Solo resuelve las esquinas superpuestas cuando una de las piezas tiene un ángulo llano o reflejo en la esquina.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices *(opcional)* | `I` | Integer | lista | Los índices de los vértices de la malla que se tratarán con este nodo. Esta entrada es opcional; si se deja vacía, todos los vértices se tratan con este nodo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Node | `N` | Node | lista | Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos. |

### Single-trim Node (STN)

Resuelve la intersección de los elementos shell con una sola operación de recorte en cada shell que se intersecta.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertices *(opcional)* | `I` | Integer | lista | Los índices de los vértices de la malla que se tratarán con este nodo. Esta entrada es opcional; si se deja vacía, todos los vértices se tratan con este nodo. |
| Offset *(opcional)* | `O` | Number | item | El tratamiento del joint empieza con un desfase desde la ubicación del vértice. |
| Gap | `G` | Number | item | Separación creada entre los elementos shell en la ubicación del nodo. No se recomiendan valores menores que la tolerancia absoluta del modelo. Puede que debas aumentar la separación si el solver no logra recortar una pieza en la ubicación del vértice. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Node | `N` | Node | lista | Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos. |

## Optimization

### Check Size (CS)

Revisa el tamaño de los shells de un ensamble e informa si algún shell no se puede obtener de la plancha de material

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar curve | `C` | Curve | item | La curva plana que se va a probar |
| Curve plane | `PL` | Plane | item | El plano de la curva |
| Material sheet | `MS` | Rectangle | item | Un objeto rectángulo que representa la plancha de material |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bounding rectangle | `BR` | Rectangle | item | El rectángulo más pequeño que contiene el polígono plano |
| Size check | `Fit` | Boolean | item | Devuelve True si la curva cabe en el rectángulo |

### Fixed Constrain (FC)

Fija los vértices de la malla en su lugar durante la optimización de planaridad.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Puntos cerca del vértice de la malla donde se aplica la restricción |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh Constrain | `Constrain` | Material | item | Una restricción usada en la optimización de mallas. Con restricciones puedes fijar vértices en su lugar mientras otros se mueven para lograr planaridad |

### Linear Constrain (LC)

Fija los vértices de la malla sobre una línea durante la optimización de planaridad.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Puntos cerca del vértice de la malla donde se aplica la restricción |
| Direction | `D` | Vector | item | La dirección en la que se puede mover el vértice. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh Constrain | `Constrain` | Material | item | Una restricción usada en la optimización de mallas. Con restricciones puedes fijar vértices en su lugar mientras otros se mueven para lograr planaridad |

### Optimize for Planarity (Solver)

Mueve los vértices de la malla para que todas las celdas queden planas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | Malla cuyas caras se fusionan |
| Mesh Constrain *(opcional)* | `Constrain` | Material | lista | Una restricción usada en la optimización de mallas. Con restricciones puedes fijar vértices en su lugar mientras otros se mueven para lograr planaridad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla poligonal que se usa para el análisis. |
| Report | `R` | Text | item | Resumen del resultado de la optimización. |

### Plane Constrain (PC)

Fija los vértices de la malla sobre un plano durante la optimización de planaridad.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point | `P` | Point | item | Puntos cerca del vértice de la malla donde se aplica la restricción |
| Plane | `PL` | Plane | item | El plano en el que se puede mover el vértice. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh Constrain | `Constrain` | Material | item | Una restricción usada en la optimización de mallas. Con restricciones puedes fijar vértices en su lugar mientras otros se mueven para lograr planaridad |

### Simplify Mesh (SM)

Toma una malla de entrada y la simplifica soldando sus vértices, fusionando las caras coplanares y eliminando los vértices colineales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `Ms` | Mesh | item | La malla de entrada que se va a simplificar. |
| Weld vertices | `Wv` | Boolean | item | Suelda los vértices que están dentro del umbral de soldadura. Ojo: soldar vértices puede generar aristas no manifold (aristas con más de 2 caras en común). Por defecto es True. |
| Weld edges | `We` | Boolean | item | Intenta soldar aristas. Si la distancia entre un vértice y una arista cercana es menor que esta tolerancia de arista, se sueldan las aristas desnudas alrededor del vértice y se crean aristas nuevas que conectan con el vértice. Por defecto es True |
| Merge coplanar faces | `Mf` | Boolean | item | Fusiona todas las caras que son planas dentro de la tolerancia de planaridad indicada. Ojo: se ignoran todos los polígonos creados antes en la malla. |
| Remove collinear vertices. | `Rv` | Boolean | item | Elimina los vértices que están sobre una misma línea solo si comparten hasta dos caras. La colinealidad se mide con la tolerancia angular. Por defecto es True. |
| Vertex threshold | `Vt` | Number | item | Tolerancia de distancia para soldar los vértices. |
| Edge threshold. | `Et` | Number | item | Tolerancia de distancia para soldar las aristas |
| Planarity tolerance | `Pt` | Number | item | Tolerancia para fusionar caras coplanares. |
| Angle threshold | `At` | Number | item | Umbral de ángulo para fusionar aristas colineales. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mesh | `M` | Mesh | item | La malla simplificada. Según las opciones de la sección de entradas, la malla puede ser manifold o no manifold. |

### Split Polygon by Angle (SPA)

Divide los polígonos en los vértices con un ángulo mayor que el umbral de entrada. El polígono se divide creando aristas nuevas desde el vértice problemático (con ángulo mayor que el umbral) hasta el vértice cercano. Este componente sirve para eliminar los ángulos reflejos de una Polygon-Surface con polígonos cóncavos y generar una nueva Polygon-Surface solo con polígonos convexos, porque normalmente es más fácil trabajar con polígonos convexos que con cóncavos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Angle threshold | `Ang` | Number | item | El ángulo interior máximo de cada polígono, en grados. Los vértices con un ángulo mayor que este valor se dividen. El valor por defecto es un poco menor que 180 grados, lo que permite dividir los polígonos cóncavos y los vértices con ángulos llanos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Breps | `B` | Brep | lista | Las superficies planas |
| New edges | `E` | Integer | lista | Los índices de las aristas recién creadas. Esta lista sirve si quieres unir los shells divididos. Ver 'Joint coplanar shells' para más información. |

## Parameters

### Assembly (parámetro)

Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital.

Tipo de dato: **Assembly**

### Joint (J, parámetro)

Un joint contiene la geometría creada a lo largo de las aristas de las piezas (si existe), además de información adicional útil para etiquetar y crear subestructuras que sostienen las piezas a lo largo de las aristas.

Tipo de dato: **Joint**

### Joint type (jt, parámetro)

Define cómo se tratan varias piezas a lo largo de una arista común.

Tipo de dato: **Joint type**

### Material (M, parámetro)

Un conjunto de propiedades que definen el material de una pieza.

Tipo de dato: **Material**

### Mesh Constrain (Constrain, parámetro)

Una restricción usada en la optimización de mallas. Con restricciones puedes fijar vértices en su lugar mientras otros se mueven para lograr planaridad

Tipo de dato: **Material**

### Node (N, parámetro)

Un nodo contiene la geometría creada en cada nodo (si existe), además de información adicional útil para crear subestructuras que sostienen las piezas en la ubicación de los nodos.

Tipo de dato: **Node**

### Node type (Nt, parámetro)

Define cómo se tratan varias piezas alrededor de un nodo común.

Tipo de dato: **Node type**

### Part (P, parámetro)

Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional útil para el anidado (nesting) y el etiquetado de las piezas.

Tipo de dato: **Part**

### Planar Polysurface (PPS, parámetro)

Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble.

Tipo de dato: **Planar Polysurface**

### Shell type (St, parámetro)

Define cómo se crea una pieza a partir de una superficie plana. Una pieza puede ubicarse arriba, al medio o arriba de la cara.

Tipo de dato: **Shell type**

## PPS Tools

### Edge Labeling (EL)

Etiqueta las aristas de una malla poligonal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Index *(opcional)* | `I` | Integer | lista | Índice de los componentes de la malla a etiquetar. |
| Size | `S` | Number | item | Tamaño de la etiqueta |
| Color | `C` | Colour | item | Color de la etiqueta |

### Edge Selection (ES)

Selecciona aristas de una PPS desde la vista previa de Grasshopper

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Selected Indices | `I` | Integer | lista | El índice de los elementos seleccionados |

### Filter Edge by Number of Connected Polgons (FEBNP)

Devuelve los números de las aristas de la malla poligonal donde la cantidad de polígonos conectados está dentro del rango indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Minimum | `Min` | Integer | item | La cantidad mínima de polígonos que comparten esta arista. |
| Maximum | `Max` | Integer | item | La cantidad máxima de polígonos que comparten esta arista. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Edges by Angle (FEBA)

Devuelve los números de las aristas de la malla donde el ángulo entre las dos caras conectadas está dentro del rango indicado. Este filtro solo se aplica a aristas con dos caras conectadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Minimum | `Min` | Number | item | El ángulo mínimo entre las dos caras, en grados. |
| Maximum | `Max` | Number | item | El ángulo máximo entre las dos caras, en grados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |
| Angle | `A` | Number | lista | El ángulo entre las dos piezas que comparten la arista. |

### Filter Edges by Attributes (FEBA)

Busca las aristas usando el par clave-valor definido en los atributos de usuario de los objetos brep

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Key | `K` | Text | item | La clave del texto de usuario de los atributos |
| Value | `V` | Text | item | El valor del texto de usuario de los atributos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Edges by Box (F.E.Box.)

Entrega los índices de las aristas que están dentro de la caja contenedora

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Box | `bx` | Box | item | Caja que encierra las aristas |
| Intersecting | `Intr.` | Boolean | item | Incluye las aristas que se intersectan si es True |
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Edges by Length (FEBL)

Devuelve los números de las aristas de la PPS cuya longitud está dentro del rango indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Minimum | `Min` | Number | item | La longitud mínima de arista. |
| Maximum | `Max` | Number | item | La longitud máxima de arista. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |
| Length | `L` | Number | lista | La longitud de la arista |

### Filter Edges by Polygons (FEBP)

Devuelve los números de las aristas de la malla poligonal que se comparten con alguno de los polígonos indicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Polygon index | `P` | Integer | lista | El índice o los índices de los polígonos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Edges by Vertex (FEBV)

Devuelve los números de las aristas de la malla poligonal que se comparten con alguno de los vértices indicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Vertex index | `V` | Integer | lista | El índice o los índices de los vértices. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Edges within a Plane (FEBP)

Filtra las aristas que están dentro de un plano dado. Se usa la tolerancia de proximidad de la PPS para determinar si las aristas están en el plano.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Plane | `Pl` | Plane | item | El plano que contiene las aristas dentro del umbral indicado |
| Threshold | `Th` | Number | item | El valor del umbral |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Manifold Edges (FME)

Filtra las aristas con dos caras conectadas en que ambas caras están orientadas en la misma dirección.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Open Edges (FOE)

Filtra las aristas que tienen una sola cara.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Edge indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Edge indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Planar Polygons (FPP)

Busca los polígonos coplanares con los polígonos indicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Ngon indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Polygon | `P` | Integer | item | Índices de polígonos como lista de enteros |
| Angle tolerance | `A` | Number | item | Los polígonos cuyas normales forman un ángulo menor que este valor se consideran coplanares. El ángulo se mide en grados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ngon indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Polygons by Area (FPBA)

Filtra los Ngons planos cuya área está dentro del rango indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Ngon indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Minimum area | `Min` | Number | item | El área del Ngon debe ser mayor que este valor. |
| Maximum area | `Max` | Number | item | El área del Ngon debe ser menor que este valor. |
| Ignore holes | `IH` | Boolean | item | Si es True, el área se calcula sin los agujeros dentro de los Ngons. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ngon indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Polygons by Attributes (FPBA)

Busca los polígonos usando el par clave-valor definido en los atributos de usuario

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Ngon indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Key | `K` | Text | item | La clave del texto de usuario de los atributos |
| Value | `V` | Text | item | El valor del texto de usuario de los atributos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ngon indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Polygons by Box (F.P.Box.)

Filtra los polígonos que están dentro de la caja contenedora indicada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bounding Box | `bbx` | Box | item | Caja contenedora que cubre los polígonos |
| Intersecting | `Intr.` | Boolean | item | Permite intersección: se consideran los polígonos que intersectan la caja |
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Ngon indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ngon indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Polygons by Edge (FPBE)

Busca los polígonos que contienen al menos una de las aristas indicadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Ngon indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Edges | `E` | Integer | lista | Índices de aristas como lista de enteros. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ngon indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Polygons by Plane (FPBP)

Calcula los ángulos entre el plano del polígono de la malla y un plano dado. El filtro deja pasar el índice del Ngon si la diferencia está dentro del umbral indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Ngon indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Reference plane *(opcional)* | `Pln` | Plane | item | El plano de referencia |
| Angle threshold *(opcional)* | `Ang` | Number | item | El umbral de ángulo en grados |
| Proximity tolerance *(opcional)* | `PrTol` | Number | item | La distancia mínima a la que dos puntos se consideran distintos. |
| Ignore face direction | `IFD` | Boolean | item | Poner en False si la normal de la cara debe apuntar en la misma dirección que el plano de referencia. |
| Ignore face location | `IFL` | Boolean | item | Poner en False si la cara debe contener el origen del plano. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ngon indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Polygons by Vertices (FPBV)

Busca los polígonos que contienen al menos un vértice de la lista de vértices de entrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Ngon indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Vertices | `V` | Integer | lista | Índices de vértices como lista de enteros |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Ngon indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Vertices by Box (F.V.Box.)

Filtra los vértices que están dentro de una caja contenedora dada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Vertex indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Bounding Box | `bbx` | Box | item | Una caja contenedora que contiene algunos vértices de la PPS |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertex indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Vertices by Edges (FVBE)

Filtra los vértices de la arista indicada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Vertex indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Edge index | `Edge` | Integer | lista | Los índices de las aristas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertex indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Vertices by Polygon (FVBP)

Filtra los vértices de los polígonos indicados.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Vertex indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Polygon index | `Polygons` | Integer | lista | Los índices de los polígonos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertex indices | `I` | Integer | lista | Los que pasan el filtro. |

### Filter Vertices by Proximity (FVP)

Filtra los vértices que están dentro de una tolerancia dada respecto de un conjunto de puntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Vertex indices *(opcional)* | `I` | Integer | lista | Argumento opcional para pasar el . Si no se define este valor, el filtro se aplica a toda la malla. |
| Reference point | `P` | Point | lista | Un conjunto de puntos donde buscar vértices cercanos. |
| Threshold | `T` | Number | item | Distancia máxima desde los puntos de referencia hasta un vértice. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Vertex indices | `I` | Integer | lista | Los que pasan el filtro. |

### Invert Filter (INV)

Invierte los elementos filtrados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Generic Data | item | Un objeto topológico formado por vértices, aristas y formas planas, que se usa para crear ensambles. |
| Indices | `I` | Integer | lista | Los índices de los componentes de la malla que se invierten (Vertex, Edge, Ngon) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Indices | `I` | Integer | lista | La lista invertida de componentes de la malla (Vertex, Edge, Ngon) |

### Polygon Labeling (PL)

Etiqueta los polígonos planos de una malla poligonal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Index *(opcional)* | `I` | Integer | lista | Índice de los componentes de la malla a etiquetar. |
| Size | `S` | Number | item | Tamaño de la etiqueta |
| Color | `C` | Colour | item | Color de la etiqueta |
| Only planar polygons | `P` | Boolean | item | Etiquetar solo los polígonos planos |
| Planarity tolerance | `T` | Number | item | Tolerancia de planaridad. |

### Polygon Selection (PS)

Selecciona polígonos de una PPS desde la vista previa de Grasshopper

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Selected Indices | `I` | Integer | lista | El índice de los elementos seleccionados |

### PPS Edge (E)

Extrae información de las aristas de una polisuperficie plana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Joint index | `JI` | Integer | lista | Índice de los elementos joint asociados a este elemento |
| Curve | `C` | Curve | lista | Arista como curva |

### PPS Polygon (V)

Extrae información de los polígonos de una polisuperficie plana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell index | `SI` | Integer | lista | Índice de los elementos shell asociados a este elemento |
| Polygon | `P` | Brep | lista | El polígono plano |
| Plane | `Plane` | Plane | lista | El plano del polígono |

### PPS Vertex (V)

Extrae información de los vértices de una polisuperficie plana

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Node index | `NI` | Integer | lista | Índice de los elementos nodo asociados a este elemento |
| Location | `L` | Point | lista | Ubicación del vértice |

### Vertex Labeling (VL)

Etiqueta los vértices de una malla poligonal

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Index *(opcional)* | `I` | Integer | lista | Índice de los componentes de la malla a etiquetar. |
| Size | `S` | Number | item | Tamaño de la etiqueta |
| Color | `C` | Colour | item | Color de la etiqueta |

### Vertex Selection (VS)

Selecciona vértices de una PPS desde la vista previa de Grasshopper

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Selected Indices | `I` | Integer | lista | El índice de los elementos seleccionados |

## Shells

### Negative Shell (default) (NS)

Todo el shell se crea en el lado negativo de la cara (polígono). El lado negativo de la cara es el opuesto a su normal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon index *(opcional)* | `I` | Integer | lista | Los índices de los polígonos de la malla con los que se debe crear este shell. Esta entrada es opcional; si se deja vacía, se crea el mismo shell en todos los polígonos de la malla. |
| Thickness | `T` | Number | item | El espesor del shell. |
| Material *(opcional)* | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Fitting direction | `FD` | Vector | item | La dirección en la que el shell se puede mover hacia su posición. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell type | `St` | Shell type | lista | Define cómo se crea una pieza a partir de una superficie plana. Una pieza puede ubicarse arriba, al medio o arriba de la cara. |

### Positive Shell (PS)

Todo el shell se crea en el lado positivo de la cara (polígono). El lado positivo de la cara es hacia donde apunta su normal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon index *(opcional)* | `I` | Integer | lista | Los índices de los polígonos de la malla con los que se debe crear este shell. Esta entrada es opcional; si se deja vacía, se crea el mismo shell en todos los polígonos de la malla. |
| Thickness | `T` | Number | item | El espesor del shell. |
| Material *(opcional)* | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Fitting direction | `FD` | Vector | item | La dirección en la que el shell se puede mover hacia su posición. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell type | `St` | Shell type | lista | Define cómo se crea una pieza a partir de una superficie plana. Una pieza puede ubicarse arriba, al medio o arriba de la cara. |

### Symmetric Shell (SS)

El shell se crea de forma simétrica a ambos lados de la cara de la malla (polígono).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Polygon index *(opcional)* | `I` | Integer | lista | Los índices de los polígonos de la malla con los que se debe crear este shell. Esta entrada es opcional; si se deja vacía, se crea el mismo shell en todos los polígonos de la malla. |
| Thickness | `T` | Number | item | El espesor del shell. |
| Material *(opcional)* | `M` | Material | item | Un conjunto de propiedades que definen el material de una pieza. |
| Fitting direction | `FD` | Vector | item | La dirección en la que el shell se puede mover hacia su posición. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell type | `St` | Shell type | lista | Define cómo se crea una pieza a partir de una superficie plana. Una pieza puede ubicarse arriba, al medio o arriba de la cara. |

## Simulation

### Assembly Sequence Generator (ASG)

Entrega la primera secuencia posible, a partir del índice de shell indicado, en la que se puede armar el ensamble. ¡Este componente no revisa colisiones!

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |
| Seed | `S` | Integer | item | El valor semilla del motor de búsqueda. Explora distintas variantes de ensamble cambiando este valor. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sequence | `S` | Generic Data | lista | Conjunto de listas ordenadas de índices de piezas a ensamblar. |

### Assembly Simulation (AS)

Muestra la secuencia de un ensamble colocando cada pieza en su posición en el orden y la dirección correctos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shell index | `SI` | Integer | lista | Índice de los elementos shell asociados a este elemento |
| Sequence | `S` | Generic Data | lista | Conjunto de listas ordenadas de índices de piezas a ensamblar. |
| Breps | `B` | Brep | lista | Las geometrías sólidas correspondientes a la lista anterior. |
| Simulation Parameter | `SP` | Number | item | Un valor entre 0 y 100 que indica el porcentaje de avance de la simulación. |
| Magnitude | `M` | Number | item | El desfase inicial de las piezas respecto de su ubicación final en el ensamble. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Breps | `B` | Brep | lista | Breps |

## Sub-Structure

### Construct (Type 4) 3D Connector (3DC)

Este conector crea una geometría guía a lo largo de las aristas para ayudar a colocar los marcos a ambos lados de la arista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Offset | `Of` | Number | item | Distancia entre los marcos a ambos lados de la arista. |
| D1 | `D1` | Number | item | Espesor de la escuadra |
| D2 | `D2` | Number | item | La extensión de la escuadra dentro del conector |
| D3 | `D3` | Number | item | El retorno de la escuadra dentro del conector |
| D4 | `D4` | Number | item | El espesor del retorno de la escuadra bajo el marco. |
| D5 | `D5` | Number | item | El retorno de la escuadra bajo el marco. |
| A | `A` | Number | item | Ángulo de la extensión de la escuadra respecto del eje vertical, en radianes |
| B | `B` | Number | item | Ángulo de conicidad de la pared de la escuadra, en radianes. |
| R1 | `R1` | Number | item | El radio de fillet grande. |
| R2 | `R2` | Number | item | El radio de fillet pequeño. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 3d Connector | `3d Con.` | 3d connector | item | Este componente crea una geometría guía a lo largo de las aristas para ayudar a colocar los marcos a ambos lados de la arista. |

### Construct 2D Connector (2DC)

Construye un conector 2D: una geometría guía en cada esquina de la pieza que conecta dos marcos adyacentes. La geometría siempre es plana y se puede cortar con láser; por eso se llama conector 2D.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Thickness | `Th` | Number | item | El espesor del conector 2D |
| Size | `S` | Number | item | Controla el tamaño del conector 2D |
| Diameter | `D` | Number | item | El diámetro de las perforaciones del conector 2D |
| Max Distance | `MD` | Number | item | Si la distancia del conector a la esquina del shell es mayor que este valor, el conector se extiende hasta el borde del shell |
| Angle Tolerance | `AT` | Number | item | Si el ángulo entre dos marcos es menor que este valor, la geometría del conector cambia para acomodar las perforaciones en el ángulo cerrado. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 2d Connector | `2d Con.` | 2d connector | item | Una geometría guía en cada esquina de la pieza que conecta dos marcos adyacentes. La geometría siempre es plana y se puede cortar con láser; por eso se llama conector 2D. |

### Construct Edge Support (CES)

Define los ajustes de un soporte en forma de "V" perpendicular a la arista del ensamble, que sostiene los shells adyacentes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L` | Number | item | Longitud del soporte perpendicular a la arista. |
| Depth | `D` | Number | item | Profundidad del soporte perpendicular a los shells adyacentes |
| Thickness | `Th` | Number | item | Espesor del material usado para crear el soporte |
| Groove Depth | `GD` | Number | item | La profundidad de la ranura hecha en los shells adyacentes para alojar el soporte. Es una proporción del espesor del shell, entre 0 y 1. Cero significa sin ranura y uno significa que el soporte atraviesa completamente el shell. |
| Groove Length | `GL` | Number | item | La longitud de la ranura en los shells adyacentes. Es una proporción de la longitud del soporte, entre 0 y 1. Cero significa sin ranura y uno significa que todo el largo del soporte encaja en los shells. |
| Gap1 | `G1` | Number | item | Holgura dentro de la ranura en la dirección del soporte |
| Gap2 | `G2` | Number | item | Holgura dentro de la ranura en la dirección perpendicular al soporte |
| Align Tongues | `AT` | Boolean | item | Alinea las lengüetas con la bisectriz de la arista, para que el soporte se pueda insertar en el joint en la dirección de la bisectriz. Por defecto (False) las lengüetas son perpendiculares a los shells. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 2d edge support | `2ES` | 2D Edge Connector | item | Una cuña bidimensional que sostiene las piezas a lo largo de una arista común. El soporte sirve para alinear las piezas a ambos lados de la arista o incluso para dar soporte estructural al encajar con las piezas. |

### Construct Frame (F)

Un marco que sostiene los shells a lo largo de las aristas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Width | `W` | Number | item | Ancho de la sección transversal. |
| Height | `H` | Number | item | Alto de la sección transversal. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame | `Fr.` | Frame | item | Un marco sostiene las piezas a lo largo de las aristas. |

### Deconstruct 2D Connector (2DC)

Conecta dos shells adyacentes cerca de la ubicación del nodo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 2d Connector | `2d Con.` | 2d connector | item | Una geometría guía en cada esquina de la pieza que conecta dos marcos adyacentes. La geometría siempre es plana y se puede cortar con láser; por eso se llama conector 2D. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Brep | lista | La geometría del conector nodal |
| Exterior Boundary | `EB` | Curve | item | El contorno exterior del conector nodal para corte láser |
| Interior Boundary | `IB` | Curve | item | El contorno interior del conector nodal |
| Holes | `C` | Circle | lista | Marcadores de las perforaciones que se harán en el elemento shell para conectarlo al conector 2D |
| Base plane | `BPl` | Plane | lista | El plano en el que se dibuja la geometría. Úsalo para dejar las geometrías sobre el plano XY. |
| Label location | `LL` | Plane | lista | El plano en el que se dibuja la etiqueta sobre las escuadras. |
| Label | `Lbl` | Text | lista | Id único del conector. |
| Part Index | `PI` | Integer | item | El índice de la pieza del ensamble a la que pertenece el conector. |

### Deconstruct 3D Connector (3DC)

Conecta dos shells adyacentes cerca de la ubicación del nodo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 3d Connector | `3d Con.` | 3d connector | item | Este componente crea una geometría guía a lo largo de las aristas para ayudar a colocar los marcos a ambos lados de la arista. |
| Thickness | `Th` | Number | item | El espesor del joint impreso en 3D |
| Spacing | `S` | Number | item | Separación máxima entre los conectores 3D |
| Depth | `D` | Number | item | La profundidad del conector y de la escuadra |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Connector Geometry | `C` | Brep | árbol | La geometría del conector 3D |
| Bracket Geometry | `B` | Brep | árbol | La geometría de las escuadras |
| Base plane | `BPl` | Plane | árbol | El plano en el que se dibuja la geometría. Úsalo para dejar las geometrías sobre el plano XY. |
| Label plane | `LPl` | Plane | árbol | El plano en el que se dibuja la etiqueta. |
| Label | `Lbl` | Text | árbol | Id único del conector, a partir de 1. |

### Deconstruct Edge Support (DCES)

Descompone los soportes de arista generados por el Edge Support System en sus subcomponentes (geometría, etiquetas y planos)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 2d edge support | `2ES` | 2D Edge Connector | item | Una cuña bidimensional que sostiene las piezas a lo largo de una arista común. El soporte sirve para alinear las piezas a ambos lados de la arista o incluso para dar soporte estructural al encajar con las piezas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Left Shell Index | `LSI` | Integer | item | El índice del shell izquierdo. |
| Right Shell Index | `RSI` | Integer | item | El índice del shell derecho. |
| Left Plane | `LP` | Plane | item | Un plano perpendicular al shell izquierdo en la ubicación del soporte. |
| Right Plane | `RP` | Plane | item | Un plano perpendicular al shell derecho en la ubicación del soporte. |
| Solid | `S` | Brep | item | Geometría sólida del soporte |
| 2D Curves | `C` | Curve | lista | Lista de todas las curvas 2D. Estas curvas se pueden usar para corte láser. |
| 2D Boundary | `B` | Curve | item | La curva más exterior. Esta curva se puede usar para el anidado (nesting). |

### Deconstruct Frame (F)

Un marco que sostiene los shells a lo largo de las aristas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Frame | `Fr.` | Frame | item | Un marco sostiene las piezas a lo largo de las aristas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Geometry | `G` | Brep | árbol | La geometría del perfil |
| Base plane | `BPl` | Plane | item | El plano en el que se dibuja la geometría. Úsalo para dejar las geometrías sobre el plano XY. |
| Label plane | `LPl` | Plane | item | El plano en el que se dibuja la etiqueta. |
| Label | `Lbl` | Text | item | Id único del conector, a partir de 1. |
| Length | `L` | Number | item | Longitud del marco. |
| Part Index | `PI` | Integer | item | El índice de la pieza del ensamble que sostiene este marco. |

### Edge Support System (ESS)

Da soporte a las piezas a lo largo de las aristas del ensamble

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |
| Joint index *(opcional)* | `JI` | Integer | lista | Índice de los elementos joint asociados a este elemento |
| 2d edge support | `2ES` | 2D Edge Connector | item | Una cuña bidimensional que sostiene las piezas a lo largo de una arista común. El soporte sirve para alinear las piezas a ambos lados de la arista o incluso para dar soporte estructural al encajar con las piezas. |
| Flip | `F` | Boolean | item | Pasa los soportes al otro lado del shell |
| Count | `C` | Integer | item | Cantidad de soportes a lo largo de la arista. |
| Spacing | `S` | Number | item | Espacio entre los soportes a lo largo de la arista. Este parámetro solo tiene efecto si el parámetro Count es cero. |
| Offset | `O` | Number | item | Desfase desde ambos lados de la arista. En algunos casos se puede usar un valor mayor que el de entrada para evitar colisiones. |
| Cleanup | `Cl` | Boolean | item | Poner en True para limpiar la intersección entre el soporte de arista y los shells, si la hay. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |
| 2d edge support | `2ES` | 2D Edge Connector | lista | Una cuña bidimensional que sostiene las piezas a lo largo de una arista común. El soporte sirve para alinear las piezas a ambos lados de la arista o incluso para dar soporte estructural al encajar con las piezas. |
| Unsupported Edges | `UsE` | Integer | lista | Si el programa no logra generar soporte para algunos joints del ensamble, aquí se registran los índices de esas aristas. Puedes crear otro Edge Support System con otros ajustes para generar soporte para esas aristas. |

### Nodal Support Structure (NSS)

Da soporte a los shells en los elementos joint.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |
| Flip | `F` | Boolean | item | Invierte la estructura. Por defecto todos los soportes se colocan bajo los shells. |
| Check for intersections | `C` | Boolean | item | Revisa la intersección de los elementos de la subestructura alrededor de los vértices. Si dos conectores 2D se intersectan, los marcos se empujan hacia dentro de la pieza para evitar la intersección |
| 3d Connector | `3d Con.` | 3d connector | item | Este componente crea una geometría guía a lo largo de las aristas para ayudar a colocar los marcos a ambos lados de la arista. |
| 2d Connector | `2d Con.` | 2d connector | item | Una geometría guía en cada esquina de la pieza que conecta dos marcos adyacentes. La geometría siempre es plana y se puede cortar con láser; por eso se llama conector 2D. |
| Frame | `Fr.` | Frame | item | Un marco sostiene las piezas a lo largo de las aristas. |
| Hole Depth | `D` | Number | item | Profundidad de las perforaciones en las piezas. |
| Ignore Edges *(opcional)* | `IE` | Integer | lista | No crea subestructura a lo largo de las aristas indicadas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |
| 3d Connector | `3d Con.` | 3d connector | lista | Este componente crea una geometría guía a lo largo de las aristas para ayudar a colocar los marcos a ambos lados de la arista. |
| 2d Connector | `2d Con.` | 2d connector | lista | Una geometría guía en cada esquina de la pieza que conecta dos marcos adyacentes. La geometría siempre es plana y se puede cortar con láser; por eso se llama conector 2D. |
| Frame | `Fr.` | Frame | lista | Un marco sostiene las piezas a lo largo de las aristas. |

### Tongue And Groove System (TGS)

Crea una serie de soportes machihembrados a lo largo de los conjuntos de planos dados. Normalmente se usa para revestimiento de muros.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `Assembly` | Assembly | item | Un ensamble es la combinación de una geometría (polisuperficie plana) y otra información necesaria (tipos de shell, joints y nodos) para producir piezas para fabricación digital. |
| Support planes | `SP` | Plane | lista | Los planos en los que se crean los soportes |
| Wall plane *(opcional)* | `WP` | Plane | item | El plano del muro donde se fijan todos los soportes. |
| Support Depth | `SD` | Number | item | Si no se entrega el plano del muro, el perfil se desfasa esta cantidad para crear la geometría del soporte. Si se entrega el plano del muro, este valor no tiene efecto. |
| Shell type | `St` | Shell type | item | Define cómo se crea una pieza a partir de una superficie plana. Una pieza puede ubicarse arriba, al medio o arriba de la cara. |
| Offset | `O` | Number | item | Desfase inicial y final de la ranura respecto de las aristas de la pieza |
| Depth | `N` | Number | item | Profundidad de la ranura dentro de la pieza |
| Gap | `G` | Number | item | La holgura entre el inicio y el final de la lengüeta dentro de la ranura |
| Width | `W` | Number | item | El ancho de la ranura y el espesor de la lengüeta |
| Overlap | `Ov.` | Number | item | Define cuánto se superpone la lengüeta con el montante. |
| MinLength | `M` | Number | item | No se crean lengüetas si la longitud disponible es menor que este umbral. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Assembly | `AM` | Generic Data | item | El ensamble representa la malla o polisuperficie con planchas planas y la demás información necesaria para producir las piezas de fabricación. |
| Support Boundary | `SB` | Curve | árbol | Las curvas 2D que representan los contornos de los soportes |
| Support Geometry | `SG` | Brep | árbol | La geometría de los soportes |
| Tongue Geometry | `TG` | Brep | árbol | La geometría de la lengüeta |
| Guid lines | `GL` | Line | árbol | Las líneas guía sobre la geometría del montante que ubican las lengüetas |
| Tongues Length | `TL` | Number | árbol | La longitud de las lengüetas |

### Waffle Grid 1 (WG1)

Crea una estructura tipo waffle a partir de un conjunto de superficies planas que se intersectan

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Regions | `S` | Brep | lista | Conjunto de superficies planas que se intersectan |
| Width | `W` | Number | item | Ancho de la ranura (slit) |
| Flip | `F` | Boolean | item | Invierte las ranuras |
| Shift | `Sh` | Number | item | Desplaza las ranuras a lo largo de la línea de intersección |
| Planarity tolerance *(opcional)* | `PlTol` | Number | item | La desviación de la superficie del polígono respecto de un plano. Este valor debe ser consistente en todos los componentes de EndoFrame. |
| Proximity tolerance *(opcional)* | `PrTol` | Number | item | La distancia mínima a la que dos puntos se consideran distintos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |

## Utilities

### Add Shape (AS)

Extrae la porción de la forma plana que queda dentro de la superficie superior del shell.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Part | `P` | Part | item | Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional útil para el anidado (nesting) y el etiquetado de las piezas. |
| Shape | `S` | Curve | lista | Forma 2D que se incluye en la pieza. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Shape | `S` | Curve | lista | Forma transformada |

### Edge marker (E.M.)

Marca las aristas en su punto medio para que las piezas se puedan alinear al ensamblarlas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Part | `P` | Part | item | Una pieza contiene la geometría que se usará en el proceso de fabricación, además de información adicional útil para el anidado (nesting) y el etiquetado de las piezas. |
| Length | `L` | Number | item | Longitud del marcador. Por defecto 10 mm |
| Offset | `O` | Number | item | Mueve el marcador a lo largo de la arista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Marks | `M` | Curve | lista | Marca todas las aristas de la pieza. |

### Furring Strips in Rectangle (FSR)

Genera listones paralelos (furring strips) dentro del rectángulo indicado

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundary | `B` | Rectangle | item | El área rectangular que se llena con listones paralelos a lo largo de su largo. |
| Spacing | `S` | Number | item | Separación entre los listones. |
| Width | `W` | Number | item | El ancho de los listones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Strips | `S` | Brep | lista | Los listones paralelos como superficies planas |

### Futting Strips in Boundary (FSB)

Genera listones paralelos (furring strips) dentro de una curva plana cerrada dada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Boundary | `B` | Curve | lista | La región o regiones planas cerradas que se llenan con listones paralelos a lo largo de su largo. |
| Spacing | `S` | Number | item | Separación entre los listones. |
| Width | `W` | Number | item | El ancho de los listones. |
| Edge index | `Ei` | Integer | item | El índice de la arista de la primera curva que se usa como dirección para generar los listones. Si se define un vector de dirección, se ignora la dirección de la arista. |
| Direction | `D` | Vector | item | Define la dirección de los listones. El vector debe estar dentro del plano de los contornos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Strips | `S` | Brep | lista | Los listones paralelos como superficies planas |

### Slicer

Genera un conjunto de planos paralelos copiando un plano de referencia a lo largo de una polisuperficie plana (PPS). Estos planos se usan para seccionar la PPS.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planar Polysurface | `PPS` | Planar Polysurface | item | Una polisuperficie con solo caras planas. Este tipo de objeto contiene la información geométrica y tipológica del ensamble. |
| Reference Plane | `RP` | Plane | item | Plano de corte de referencia |
| Maximum Spacing | `Smax` | Number | item | La distancia máxima entre secciones. |
| Minimum Spacing | `Smin` | Number | item | La distancia mínima entre secciones. |
| Distance to vertices | `VD` | Number | item | Distancia mínima del plano de corte a los vértices de la PPS. Normalmente se usa el espesor máximo del material |
| Start Offset | `SO` | Number | item | Distancia del primer plano respecto de su posición original |
| End Offset | `EO` | Number | item | Distancia del último plano respecto de su posición original |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Planes | `Pl` | Plane | lista | Los planos de corte como planos. |
| Slices | `S` | Brep | lista | Vista previa de la estructura. |
