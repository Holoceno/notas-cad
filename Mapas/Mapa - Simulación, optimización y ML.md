---
tags: [tipo/mapa, simulacion, simulacion/fisica, simulacion/optimizacion, simulacion/ml, software/grasshopper, plugin/kangaroo, plugin/lunchboxml]
---

# Simulación, optimización y ML

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

- **Kangaroo2**: física y form-finding. Se definen *goals* (largo, ancla, planaridad, colisión) y un *solver* busca la forma que mejor los cumple.
- **Galapagos**: optimización evolutiva de un número (minimizar material, maximizar área...).
- **Biber**: optimización para estructuras de placas.
- **LunchBoxML**: machine learning (regresión, clasificación, clustering).

Todavía no hay teoría ingestada en la wiki para este mapa (pendiente: K2Goals y Kangaroo-examples en `raw/grasshopper/guias/`).

## Conceptos clave de Kangaroo
| Concepto | Componente | Idea |
|---|---|---|
| Solver | [[Catálogo - Kangaroo2#Solver\|Solver]] | Itera hasta que los goals se equilibran (o el umbral) |
| Ancla | [[Catálogo - Kangaroo2#Anchor\|Anchor]] | Fija puntos (apoyos) |
| Largo | [[Catálogo - Kangaroo2#Length(Line)\|Length(Line)]] | Resortes: cada línea quiere un largo |
| Ver resultado | [[Catálogo - Kangaroo2#Show\|Show]] | Muestra la geometría durante la simulación |
| Interactivo | [[Catálogo - Kangaroo2#Grab\|Grab]] | Tirar puntos con el mouse |

## Para empezar
[[Catálogo - Kangaroo2#Solver|Solver]] · [[Catálogo - Kangaroo2#Anchor|Anchor]] · [[Catálogo - Kangaroo2#Length(Line)|Length(Line)]] · [[Catálogo - Kangaroo2#Show|Show]] · [[Catálogo - Params#Galapagos (objeto especial)|Galapagos]] · [[Catálogo - LunchBoxML|LunchBoxML (pestaña completa)]]

<!-- AUTO:inicio -->

## Componentes de Grasshopper (179)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Util (3)

- [[Catálogo - Params#Fitness Landscape (LScape)|Fitness Landscape (LScape)]] — Muestra un paisaje de aptitud (fitness) 2.5D
- [[Catálogo - Params#Galapagos (objeto especial)|Galapagos (objeto especial)]] — Interfaz con el solver evolutivo Galapagos
- [[Catálogo - Params#Gene Pool (Genes, parámetro)|Gene Pool (Genes, parámetro)]] — Contiene una colección de genes (es decir, variables)

### Biber › Optimization (7)

- [[Catálogo - Biber#Check Size (CS)|Check Size (CS)]] — Revisa el tamaño de los shells de un ensamble e informa si algún shell no se puede obtener de la plancha de…
- [[Catálogo - Biber#Fixed Constrain (FC)|Fixed Constrain (FC)]] — Fija los vértices de la malla en su lugar durante la optimización de planaridad
- [[Catálogo - Biber#Linear Constrain (LC)|Linear Constrain (LC)]] — Fija los vértices de la malla sobre una línea durante la optimización de planaridad
- [[Catálogo - Biber#Optimize for Planarity (Solver)|Optimize for Planarity (Solver)]] — Mueve los vértices de la malla para que todas las celdas queden planas
- [[Catálogo - Biber#Plane Constrain (PC)|Plane Constrain (PC)]] — Fija los vértices de la malla sobre un plano durante la optimización de planaridad
- [[Catálogo - Biber#Simplify Mesh (SM)|Simplify Mesh (SM)]] — Toma una malla de entrada y la simplifica soldando sus vértices, fusionando las caras coplanares y eliminando…
- [[Catálogo - Biber#Split Polygon by Angle (SPA)|Split Polygon by Angle (SPA)]] — Divide los polígonos en los vértices con un ángulo mayor que el umbral de entrada. El polígono se divide…

### Kangaroo2 › Goals-6dof (8)

- [[Catálogo - Kangaroo2#AlignFaces|AlignFaces]] — Alinea caras de un par de cuerpos rígidos
- [[Catálogo - Kangaroo2#Beam|Beam]] — Viga que resiste flexión y torsión
- [[Catálogo - Kangaroo2#Concentric|Concentric]] — Alinea los ejes de un par de cuerpos rígidos
- [[Catálogo - Kangaroo2#RigidBody|RigidBody]] — Cuerpo rígido (RigidBody)
- [[Catálogo - Kangaroo2#RigidBodyCollide|RigidBodyCollide]] — Colisión entre un par de cuerpos rígidos
- [[Catálogo - Kangaroo2#RigidPointSet|RigidPointSet]] — Un conjunto de puntos que mantienen sus posiciones relativas
- [[Catálogo - Kangaroo2#SolidPlaneCollide|SolidPlaneCollide]] — Colisión entre un plano y un sólido
- [[Catálogo - Kangaroo2#Support|Support]] — Define las condiciones de apoyo de un extremo de viga o de un cuerpo rígido

### Kangaroo2 › Goals-Angle (6)

- [[Catálogo - Kangaroo2#Angle|Angle]] — Ángulo
- [[Catálogo - Kangaroo2#AngleSnap (AS)|AngleSnap (AS)]] — Ajusta el ángulo entre 2 líneas al múltiplo entero más cercano de un valor dado
- [[Catálogo - Kangaroo2#ClampAngle|ClampAngle]] — Mantiene el ángulo entre 2 líneas dentro de un rango dado
- [[Catálogo - Kangaroo2#EqualAngle (EA)|EqualAngle (EA)]] — Iguala los ángulos entre varios pares de líneas
- [[Catálogo - Kangaroo2#G2|G2]] — Mantiene la continuidad de curvatura entre 2 curvas NURBS
- [[Catálogo - Kangaroo2#Rod|Rod]] — Varilla que resiste flexión y estiramiento

### Kangaroo2 › Goals-Co (4)

- [[Catálogo - Kangaroo2#CoCircular|CoCircular]] — CoCircular
- [[Catálogo - Kangaroo2#CoLinear|CoLinear]] — CoLinear
- [[Catálogo - Kangaroo2#CoPlanar|CoPlanar]] — CoPlanar
- [[Catálogo - Kangaroo2#CoSpherical|CoSpherical]] — CoSpherical

### Kangaroo2 › Goals-Col (7)

- [[Catálogo - Kangaroo2#Collider|Collider]] — Colisiones entre segmentos de línea con grosor y esferas
- [[Catálogo - Kangaroo2#CurveCollide (CC)|CurveCollide (CC)]] — Colisiones entre curvas cerradas en un plano dado
- [[Catálogo - Kangaroo2#CurvePointCollide (CPC)|CurvePointCollide (CPC)]] — Mantiene un conjunto de puntos fuera o dentro de una curva 2D dada
- [[Catálogo - Kangaroo2#ImageCircles (ImgCircles)|ImageCircles (ImgCircles)]] — Empaquetado de círculos con tamaños según los colores de una imagen
- [[Catálogo - Kangaroo2#SoftBodyCollide|SoftBodyCollide]] — Colisiones entre una colección de mallas deformables
- [[Catálogo - Kangaroo2#SolidPointCollide (SPC)|SolidPointCollide (SPC)]] — Mantiene un conjunto de puntos fuera o dentro de una malla dada
- [[Catálogo - Kangaroo2#SphereCollide (SC)|SphereCollide (SC)]] — Colisiones entre grandes cantidades de esferas del mismo tamaño

### Kangaroo2 › Goals-Lin (9)

- [[Catálogo - Kangaroo2#ClampLength|ClampLength]] — Mantiene la longitud dentro de límites dados
- [[Catálogo - Kangaroo2#ConstantTension (CT)|ConstantTension (CT)]] — Un elemento que adapta su rigidez para mantener una fuerza constante
- [[Catálogo - Kangaroo2#Direction|Direction]] — Alinea un segmento de línea con un vector dado o, si no se entrega, con el más cercano de los vectores XYZ…
- [[Catálogo - Kangaroo2#DynamicWeight1d (DW)|DynamicWeight1d (DW)]] — Una carga en la dirección Z negativa, cuya magnitud se actualiza según la longitud de la línea
- [[Catálogo - Kangaroo2#EqualLength|EqualLength]] — EqualLength
- [[Catálogo - Kangaroo2#Length(Line)|Length(Line)]] — Length(Line)
- [[Catálogo - Kangaroo2#LengthRatio|LengthRatio]] — Mantiene una proporción fija entre las longitudes de un par de líneas
- [[Catálogo - Kangaroo2#LengthSnap|LengthSnap]] — Ajusta la longitud a múltiplos enteros de un número dado
- [[Catálogo - Kangaroo2#PlasticLength (PL)|PlasticLength (PL)]] — Intenta conservar la longitud de la línea de forma elástica hasta que se deforma más allá del límite…

### Kangaroo2 › Goals-Mesh (19)

- [[Catálogo - Kangaroo2#Conicalize (Conical)|Conicalize (Conical)]] — Ajusta una malla de cuadriláteros para que sus vértices sean cónicos, de modo que la malla tenga un offset…
- [[Catálogo - Kangaroo2#CyclicQuad|CyclicQuad]] — Hace que un cuadrilátero tenga una circunferencia circunscrita
- [[Catálogo - Kangaroo2#Developablize|Developablize]] — Convierte una malla triangular en parches desarrollables con pliegues. Basado en el paper 'Developability of…
- [[Catálogo - Kangaroo2#EdgeLengths|EdgeLengths]] — Define las longitudes de las aristas de una malla
- [[Catálogo - Kangaroo2#Hinge|Hinge]] — Bisagra (Hinge)
- [[Catálogo - Kangaroo2#Isothermic (Iso)|Isothermic (Iso)]] — Hace que una malla de cuadriláteros sea S-isotérmica, como se describe en el paper 'Quasiisothermic Mesh…
- [[Catálogo - Kangaroo2#LiveSoap (LS)|LiveSoap (LS)]] — Para generar mallas mínimas y CMC (curvatura media nula y constante, respectivamente) que adaptan su…
- [[Catálogo - Kangaroo2#NoFoldThrough|NoFoldThrough]] — Evita que los lados de una bisagra se atraviesen entre sí
- [[Catálogo - Kangaroo2#Planarize|Planarize]] — Planarize
- [[Catálogo - Kangaroo2#PlasticHinge (PH)|PlasticHinge (PH)]] — Como Hinge, pero plegar más allá del umbral plástico/elástico cambia el ángulo de reposo
- [[Catálogo - Kangaroo2#PolygonArea|PolygonArea]] — PolygonArea
- [[Catálogo - Kangaroo2#Pressure|Pressure]] — Una fuerza normal a cada triángulo, proporcional a su área
- [[Catálogo - Kangaroo2#Smooth|Smooth]] — Smooth
- [[Catálogo - Kangaroo2#SoapFilm (SG)|SoapFilm (SG)]] — Para generar mallas de curvatura media nula
- [[Catálogo - Kangaroo2#TangentialSmooth (TSmooth)|TangentialSmooth (TSmooth)]] — Suaviza una malla solo en los planos tangentes locales. Se usa junto con SoapFilm
- [[Catálogo - Kangaroo2#TangentIncircles|TangentIncircles]] — TangentIncircles
- [[Catálogo - Kangaroo2#VertexLoads|VertexLoads]] — Aplica cargas verticales iguales a todos los vértices de una malla
- [[Catálogo - Kangaroo2#Volume|Volume]] — Define el volumen total de una malla
- [[Catálogo - Kangaroo2#Wind|Wind]] — Viento

### Kangaroo2 › Goals-On (3)

- [[Catálogo - Kangaroo2#OnCurve|OnCurve]] — Mantiene un punto sobre una curva dada
- [[Catálogo - Kangaroo2#OnMesh|OnMesh]] — Mantiene un punto sobre una malla dada
- [[Catálogo - Kangaroo2#OnPlane|OnPlane]] — Mantiene un punto sobre un plano dado

### Kangaroo2 › Goals-Pt (10)

- [[Catálogo - Kangaroo2#Anchor|Anchor]] — Ancla (Anchor)
- [[Catálogo - Kangaroo2#AnchorXYZ|AnchorXYZ]] — Fija un punto solo en los ejes del mundo elegidos. Si necesitas reiniciar la posición inicial, desconecta y…
- [[Catálogo - Kangaroo2#Bomb (B)|Bomb (B)]] — Provoca una explosión después de una cantidad dada de iteraciones
- [[Catálogo - Kangaroo2#Coincident (C)|Coincident (C)]] — Equivale a una restricción de longitud cero entre un par de puntos
- [[Catálogo - Kangaroo2#Floor|Floor]] — Piso (Floor)
- [[Catálogo - Kangaroo2#FloorFriction (Floor)|FloorFriction (Floor)]] — Piso con fricción estática
- [[Catálogo - Kangaroo2#Load|Load]] — Carga (Load)
- [[Catálogo - Kangaroo2#MagnetSnap (MS)|MagnetSnap (MS)]] — Une puntos entre sí según su proximidad
- [[Catálogo - Kangaroo2#PlasticAnchor|PlasticAnchor]] — PlasticAnchor
- [[Catálogo - Kangaroo2#Transform|Transform]] — Mantiene una transformación dada entre 2 puntos

### Kangaroo2 › Main (7)

- [[Catálogo - Kangaroo2#BouncySolver|BouncySolver]] — Solver con inercia (momentum)
- [[Catálogo - Kangaroo2#Grab|Grab]] — Permite arrastrar partículas de Kangaroo en las vistas de Rhino
- [[Catálogo - Kangaroo2#Show|Show]] — Mostrar
- [[Catálogo - Kangaroo2#Soft & Hard Solver (Soft&HardSolver)|Soft & Hard Solver (Soft&HardSolver)]] — Solver con entradas separadas para goals blandos y goals de restricción dura
- [[Catálogo - Kangaroo2#Solver|Solver]] — El componente principal donde se combinan y aplican los goals
- [[Catálogo - Kangaroo2#StepSolver|StepSolver]] — Solver que avanza solo cuando se refresca la entrada. Útil para hacer animaciones
- [[Catálogo - Kangaroo2#ZombieSolver|ZombieSolver]] — Una versión del componente solver que hace todas las iteraciones internamente y entrega el resultado final

### Kangaroo2 › Mesh (22)

- [[Catálogo - Kangaroo2#Bipartite|Bipartite]] — Intenta asignar un booleano a cada vértice de una malla de modo que ningún par de vértices conectados tenga…
- [[Catálogo - Kangaroo2#ByParent|ByParent]] — Refina una malla, separando las salidas por cara de origen
- [[Catálogo - Kangaroo2#Checkerboard|Checkerboard]] — Intenta asignar un booleano a cada cara de una malla de modo que ningún par de caras adyacentes tenga el…
- [[Catálogo - Kangaroo2#Combine&Clean (Clean)|Combine&Clean (Clean)]] — Combina y limpia una lista de mallas, quitando vértices no usados y duplicados
- [[Catálogo - Kangaroo2#Diagonalize (Diag)|Diagonalize (Diag)]] — Reemplaza cada arista por una cara nueva
- [[Catálogo - Kangaroo2#FaceFaceOffset (FaceFace)|FaceFaceOffset (FaceFace)]] — Aplica offset a una malla cónica de modo que las caras correspondientes queden a distancia constante
- [[Catálogo - Kangaroo2#FoldAngle|FoldAngle]] — Mide el ángulo actual entre dos triángulos alrededor de su arista común
- [[Catálogo - Kangaroo2#HingePoints|HingePoints]] — Obtiene los 4 puntos de cada arista interior para usar en una fuerza Hinge
- [[Catálogo - Kangaroo2#MeshCorners (MC)|MeshCorners (MC)]] — Extrae las esquinas más agudas que cierto ángulo
- [[Catálogo - Kangaroo2#MeshDirection (MD)|MeshDirection (MD)]] — Ordena las direcciones de las caras de una malla
- [[Catálogo - Kangaroo2#MeshMap|MeshMap]] — Mapea puntos de una malla a otra
- [[Catálogo - Kangaroo2#MeshTurn (Turn)|MeshTurn (Turn)]] — Rota el orden de los vértices de cada cara
- [[Catálogo - Kangaroo2#NakedVertices (NV)|NakedVertices (NV)]] — Ordena los vértices de una malla en 2 listas según estén o no rodeados por caras
- [[Catálogo - Kangaroo2#PlanarityAnalysis (PA)|PlanarityAnalysis (PA)]] — Muestra la planaridad de las caras como una malla coloreada
- [[Catálogo - Kangaroo2#Refine|Refine]] — Divide cada cuadrilátero en 4 cuadriláteros y cada triángulo en 4 triángulos
- [[Catálogo - Kangaroo2#RefineStrips (Strips)|RefineStrips (Strips)]] — Subdivisión direccional: refina los cuadriláteros en una sola dirección
- [[Catálogo - Kangaroo2#RemeshByColour|RemeshByColour]] — Rehace la malla con longitudes de arista que dependen de los colores de los vértices de la malla de entrada
- [[Catálogo - Kangaroo2#Stripper|Stripper]] — Divide una malla en franjas
- [[Catálogo - Kangaroo2#TangentCircles (TC)|TangentCircles (TC)]] — Genera círculos inscritos en las caras, un empaquetado de círculos centrado en los vértices, o el dual por…
- [[Catálogo - Kangaroo2#Unroller|Unroller]] — Desenrolla una franja de cuadriláteros
- [[Catálogo - Kangaroo2#VertexNeighbours (VN)|VertexNeighbours (VN)]] — Devuelve las posiciones de los vértices conectados por una arista al vértice dado
- [[Catálogo - Kangaroo2#WarpWeft|WarpWeft]] — Separa las aristas de una malla en 2 listas según la dirección de urdimbre y trama

### Kangaroo2 › Utility (6)

- [[Catálogo - Kangaroo2#DotDisplay (Dot)|DotDisplay (Dot)]] — Muestra los puntos como círculos rellenos
- [[Catálogo - Kangaroo2#interconnectPoints (inter)|interconnectPoints (inter)]] — Dibuja una línea entre cada par de puntos de una lista
- [[Catálogo - Kangaroo2#Möbius Transformation (MB)|Möbius Transformation (MB)]] — Transformaciones de Möbius 3D de cualquier geometría mediante rotación 4D
- [[Catálogo - Kangaroo2#removeDuplicateLines (dupLn)|removeDuplicateLines (dupLn)]] — Quita líneas similares de una lista
- [[Catálogo - Kangaroo2#removeDuplicatePts (dupPt)|removeDuplicatePts (dupPt)]] — Quita puntos similares de una lista
- [[Catálogo - Kangaroo2#SplitAtCorners|SplitAtCorners]] — Divide una polilínea en varias partes según el ángulo

### LunchBoxML › Accord.net (17)

- [[Catálogo - LunchBoxML#Codify Data|Codify Data]] — Codifica datos para usarlos en distintos modelos clasificadores
- [[Catálogo - LunchBoxML#Confusion Matrix Properties (Confusion Matrix)|Confusion Matrix Properties (Confusion Matrix)]] — Este componente expone las propiedades de una matriz de confusión general
- [[Catálogo - LunchBoxML#Gaussian Mixture (GaussianMix)|Gaussian Mixture (GaussianMix)]] — Solver para modelos de mezcla gaussiana
- [[Catálogo - LunchBoxML#Hidden Markov Model (HiddenMark)|Hidden Markov Model (HiddenMark)]] — Solver para problemas de modelos ocultos de Markov
- [[Catálogo - LunchBoxML#K-Means Clustering (K-Means)|K-Means Clustering (K-Means)]] — Solver para agrupamiento K-Means
- [[Catálogo - LunchBoxML#Kernel SVM Tester (SVM Tester)|Kernel SVM Tester (SVM Tester)]] — Este componente prueba un clasificador de máquina de vectores de soporte (SVM) basado en kernel
- [[Catálogo - LunchBoxML#Kernel SVM Trainer (SVM Trainer)|Kernel SVM Trainer (SVM Trainer)]] — Este componente entrena una máquina de vectores de soporte (SVM) basada en kernel con un conjunto de datos de…
- [[Catálogo - LunchBoxML#Linear Regression (LineReg)|Linear Regression (LineReg)]] — Solver para problemas de regresión lineal
- [[Catálogo - LunchBoxML#Load Model|Load Model]] — Deserializa un modelo desde un archivo guardado (*.bin)
- [[Catálogo - LunchBoxML#Logistic Regression (LogReg)|Logistic Regression (LogReg)]] — Solver para problemas de regresión logística
- [[Catálogo - LunchBoxML#Multivariate Linear Regression (MultiLineReg)|Multivariate Linear Regression (MultiLineReg)]] — Solver para problemas de regresión lineal multivariada
- [[Catálogo - LunchBoxML#Naive Bayes Classification Tester|Naive Bayes Classification Tester]] — Este componente prueba un clasificador bayesiano ingenuo (naive Bayes) adaptativo
- [[Catálogo - LunchBoxML#Naive Bayes Classification Trainer|Naive Bayes Classification Trainer]] — Este componente entrena un algoritmo clasificador bayesiano ingenuo (naive Bayes) adaptativo con un conjunto…
- [[Catálogo - LunchBoxML#Neural Network Tester|Neural Network Tester]] — Prueba una solución usando un solver de red neuronal entrenado
- [[Catálogo - LunchBoxML#Neural Network Trainer|Neural Network Trainer]] — Este componente usa el algoritmo de aprendizaje de retropropagación resiliente (RProp) para entrenar redes…
- [[Catálogo - LunchBoxML#Nonlinear Regression (NonlineReg)|Nonlinear Regression (NonlineReg)]] — Solver para problemas de regresión no lineal usando optimización mínima secuencial (SMO)
- [[Catálogo - LunchBoxML#Restricted Boltzmann Machine (ResBoltz)|Restricted Boltzmann Machine (ResBoltz)]] — Solver para máquinas de Boltzmann restringidas

### LunchBoxML › Data Sets (15)

- [[Catálogo - LunchBoxML#Convert Column Type (Convert)|Convert Column Type (Convert)]] — Convierte una columna a un nuevo tipo de dato. Esta transformación opera sobre tipos numéricos, booleanos, de…
- [[Catálogo - LunchBoxML#Create Data Set (Create)|Create Data Set (Create)]] — Crea un conjunto de datos que se puede usar para entrenar un algoritmo de aprendizaje automático
- [[Catálogo - LunchBoxML#Featurize Text (Featurize)|Featurize Text (Featurize)]] — Transforma una columna de texto en un vector numérico de características que representa conteos normalizados…
- [[Catálogo - LunchBoxML#Filter Data|Filter Data]] — Filtra datos según los valores de una columna
- [[Catálogo - LunchBoxML#Get Column Label (Column Label)|Get Column Label (Column Label)]] — Obtiene los nombres de las columnas de un conjunto de datos
- [[Catálogo - LunchBoxML#Load Data From Text File (Load Data)|Load Data From Text File (Load Data)]] — Carga un conjunto de datos desde un archivo
- [[Catálogo - LunchBoxML#Normalize Data (Normalize)|Normalize Data (Normalize)]] — Normaliza los valores de una columna de un conjunto de datos
- [[Catálogo - LunchBoxML#One Hot Encoding (Encoding)|One Hot Encoding (Encoding)]] — Convierte una o más columnas de texto en igual cantidad de columnas de vectores con codificación one-hot. La…
- [[Catálogo - LunchBoxML#Peek At Data (Peek Data)|Peek At Data (Peek Data)]] — Muestra una pequeña muestra del contenido de un conjunto de datos de ML
- [[Catálogo - LunchBoxML#Remove Columns|Remove Columns]] — Quita columnas de un conjunto de datos
- [[Catálogo - LunchBoxML#Replace Missing Data (Replace Data)|Replace Missing Data (Replace Data)]] — Reemplaza datos faltantes en una columna. Ojo: este componente solo funciona con datos numéricos
- [[Catálogo - LunchBoxML#Select Columns|Select Columns]] — Selecciona columnas de un conjunto de datos
- [[Catálogo - LunchBoxML#Split Data|Split Data]] — Divide un conjunto de datos cargado en subconjuntos de entrenamiento y de prueba
- [[Catálogo - LunchBoxML#Text Loader Options (Options)|Text Loader Options (Options)]] — Opciones adicionales para controlar cómo se carga un archivo de datos
- [[Catálogo - LunchBoxML#Tokenize Into Words (Tokenize)|Tokenize Into Words (Tokenize)]] — Divide una o más columnas de texto en palabras individuales

### LunchBoxML › Models (8)

- [[Catálogo - LunchBoxML#Binary Classifier Tester|Binary Classifier Tester]] — Prueba un modelo para problemas de clasificación binaria
- [[Catálogo - LunchBoxML#Binary Classifier Trainer|Binary Classifier Trainer]] — Entrena un modelo para problemas de clasificación binaria
- [[Catálogo - LunchBoxML#Load Saved Model (Load Model)|Load Saved Model (Load Model)]] — Deserializa un modelo desde un archivo guardado (*.zip)
- [[Catálogo - LunchBoxML#Multiclass Classifier Tester|Multiclass Classifier Tester]] — Prueba un modelo para problemas de clasificación multiclase
- [[Catálogo - LunchBoxML#Multiclass Classifier Trainer|Multiclass Classifier Trainer]] — Entrena un modelo para problemas de clasificación multiclase
- [[Catálogo - LunchBoxML#Object Detection Using ONNX File (Image Classifier)|Object Detection Using ONNX File (Image Classifier)]] — Usa un archivo de aprendizaje profundo preentrenado Open Neural Network Exchange (ONNX) para detección de…
- [[Catálogo - LunchBoxML#Regression Tester|Regression Tester]] — Prueba un modelo para problemas de regresión
- [[Catálogo - LunchBoxML#Regression Trainer|Regression Trainer]] — Entrena un modelo para problemas de regresión

### LunchBoxML › Trainer Types (28)

- [[Catálogo - LunchBoxML#Average Perceptron Binary Classifier (Avg Perceptron)|Average Perceptron Binary Classifier (Avg Perceptron)]] — El clasificador binario Average Perceptron se usa para entrenar un modelo lineal de clasificación binaria con…
- [[Catálogo - LunchBoxML#Fast Forest Binary Classifier (Fast Forest)|Fast Forest Binary Classifier (Fast Forest)]] — El entrenador Fast Forest se usa para entrenar un modelo de clasificación binaria con árboles de decisión…
- [[Catálogo - LunchBoxML#Fast Forest Regression (Fast Forest)|Fast Forest Regression (Fast Forest)]] — El entrenador Fast Forest se usa para entrenar un modelo de regresión con árboles de decisión, usando el…
- [[Catálogo - LunchBoxML#Fast Tree Binary Classifier (Fast Tree)|Fast Tree Binary Classifier (Fast Tree)]] — El entrenador Fast Tree se usa para entrenar un modelo de regresión con árboles de decisión, usando el método…
- [[Catálogo - LunchBoxML#Fast Tree Regression (Fast Tree)|Fast Tree Regression (Fast Tree)]] — El entrenador Fast Tree se usa para entrenar un modelo de regresión con árboles de decisión, usando el método…
- [[Catálogo - LunchBoxML#Fast Tree Tweedie Regression (Fast Tree Tweedie)|Fast Tree Tweedie Regression (Fast Tree Tweedie)]] — El entrenador Fast Tree Tweedie se usa para entrenar un modelo de regresión con árboles de decisión, usando…
- [[Catálogo - LunchBoxML#Field Aware Factorization Machine Binary Classifier (Factorization)|Field Aware Factorization Machine Binary Classifier (Factorization)]] — El clasificador binario Field Aware Factorization Machine se usa para entrenar un modelo con un método de…
- [[Catálogo - LunchBoxML#Generalized Additive Models Binary Classifier (GAM)|Generalized Additive Models Binary Classifier (GAM)]] — El entrenador GAM se usa para entrenar un modelo de clasificación binaria con modelos aditivos generalizados…
- [[Catálogo - LunchBoxML#Generalized Additive Models Regression (GAM)|Generalized Additive Models Regression (GAM)]] — El entrenador GAM se usa para entrenar un modelo de regresión con modelos aditivos generalizados (GAM)
- [[Catálogo - LunchBoxML#Lbfgs Logistic Regression Binary Classifier (Lbfgs Logistic Regression)|Lbfgs Logistic Regression Binary Classifier (Lbfgs Logistic Regression)]] — El entrenador de clasificación binaria Lbfgs Logistic Regression se usa para entrenar modelos lineales de…
- [[Catálogo - LunchBoxML#Lbfgs Maximum Entropy Multiclass Classifier (Lbfgs Maximum Entropy)|Lbfgs Maximum Entropy Multiclass Classifier (Lbfgs Maximum Entropy)]] — El modelo de máxima entropía Lbfgs es una generalización de la regresión lineal. La principal diferencia…
- [[Catálogo - LunchBoxML#Lbfgs Poisson Regression (Lbfgs Poisson)|Lbfgs Poisson Regression (Lbfgs Poisson)]] — El entrenador Lbfgs Poisson se usa para entrenar modelos de regresión de Poisson
- [[Catálogo - LunchBoxML#Light GBM Binary Classifier (Light GBM)|Light GBM Binary Classifier (Light GBM)]] — El clasificador Light GBM entrena un modelo con un método de clasificación binaria por árboles de decisión…
- [[Catálogo - LunchBoxML#Light Gbm Multiclass Classifier (Light Gbm)|Light Gbm Multiclass Classifier (Light Gbm)]] — El entrenador LightGBM es una implementación de código abierto de árboles de decisión con gradient boosting
- [[Catálogo - LunchBoxML#Light GBM Regression (Light GBM)|Light GBM Regression (Light GBM)]] — Light GBM entrena un modelo con un método de regresión por árboles de decisión con gradient boosting
- [[Catálogo - LunchBoxML#Linear SVM Binary Classifier (Linear SVM)|Linear SVM Binary Classifier (Linear SVM)]] — El entrenador de clasificación binaria Linear SVM se usa para entrenar un modelo lineal de clasificación…
- [[Catálogo - LunchBoxML#Local Deep SVM Binary Classifier (LDSVM)|Local Deep SVM Binary Classifier (LDSVM)]] — El entrenador de clasificación binaria Local Deep SVM se usa para entrenar un modelo no lineal de…
- [[Catálogo - LunchBoxML#Naive Bayes Multiclass Classifier (Naive Bayes)|Naive Bayes Multiclass Classifier (Naive Bayes)]] — El entrenador Naive Bayes es un clasificador probabilístico que se puede usar en problemas multiclase. Con el…
- [[Catálogo - LunchBoxML#Online Gradient Descent Regression (Online Gradient Descent)|Online Gradient Descent Regression (Online Gradient Descent)]] — El entrenador Online Gradient Descent se usa para entrenar un modelo de regresión lineal con el método de…
- [[Catálogo - LunchBoxML#Ordinary Least Squares Regression (OLS)|Ordinary Least Squares Regression (OLS)]] — El entrenador Ordinary Least Squares se usa para entrenar un modelo de regresión lineal con el método de…
- [[Catálogo - LunchBoxML#SDCA Logistic Regression Binary Classifier (SDCA Logistic Regression)|SDCA Logistic Regression Binary Classifier (SDCA Logistic Regression)]] — El entrenador de clasificación binaria SDCA Logistic Regression se usa para entrenar modelos de clasificación…
- [[Catálogo - LunchBoxML#Sdca Maximum Entropy Multiclass Classifier (Sdca Maximum Entropy)|Sdca Maximum Entropy Multiclass Classifier (Sdca Maximum Entropy)]] — El modelo de máxima entropía Sdca se usa para predecir un objetivo con un modelo clasificador multiclase…
- [[Catálogo - LunchBoxML#SDCA Noncalibrated Binary Classifier (SDCA Noncalibrated)|SDCA Noncalibrated Binary Classifier (SDCA Noncalibrated)]] — El entrenador de clasificación binaria SDCA Noncalibrated se usa para entrenar modelos de clasificación por…
- [[Catálogo - LunchBoxML#Sdca Noncalibrated Multiclass Classifier (Sdca Noncalibrated)|Sdca Noncalibrated Multiclass Classifier (Sdca Noncalibrated)]] — El modelo Sdca no calibrado se usa para predecir un objetivo con un modelo clasificador multiclase lineal…
- [[Catálogo - LunchBoxML#Sdca Regression (Sdca)|Sdca Regression (Sdca)]] — El entrenador Sdca se usa para entrenar un modelo de regresión con el método de ascenso de coordenadas dual…
- [[Catálogo - LunchBoxML#SGD Calibrated Binary Classifier (SGD Calibrated)|SGD Calibrated Binary Classifier (SGD Calibrated)]] — SGD Calibrated entrena un modelo de clasificación lineal con el método de descenso de gradiente estocástico…
- [[Catálogo - LunchBoxML#SGD Noncalibrated Binary Classifier (SGD Noncalibrated)|SGD Noncalibrated Binary Classifier (SGD Noncalibrated)]] — SGD Noncalibrated entrena un modelo de clasificación lineal con el método de descenso de gradiente…
- [[Catálogo - LunchBoxML#Symbolic SGD Logistic Regression Binary Classifier (Symbolic SGD)|Symbolic SGD Logistic Regression Binary Classifier (Symbolic SGD)]] — El clasificador Symbolic SGD Logistic Regression entrena un modelo lineal de clasificación binaria con el…

<!-- AUTO:fin -->
