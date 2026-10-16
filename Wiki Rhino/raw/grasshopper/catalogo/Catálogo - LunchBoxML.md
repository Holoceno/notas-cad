---
title: "Catálogo Grasshopper — LunchBoxML"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "LunchBoxML"
libraries: ["LunchBoxML 2024.2.11.0"]
components: 68
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/lunchboxml, simulacion]
---

# LunchBoxML

68 objetos · librería: LunchBoxML 2024.2.11.0

Mapas: [[Mapa - Simulación, optimización y ML]] (68)

## Accord.net

### Codify Data

Codifica datos para usarlos en distintos modelos clasificadores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Label | `Label` | Text | item | Etiqueta usada para categorizar estos datos. |
| Data | `Data` | Text | lista | La lista de datos. |
| Data Type | `Type` | Integer | item | Tipo de dato: (0) ordinal (1) categórico (2) categórico con línea base (3) continuo (4) discreto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Codified Data | `Data` | Generic Data | item | Los datos codificados |

### Confusion Matrix Properties (Confusion Matrix)

Este componente expone las propiedades de una matriz de confusión general

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| General Confusion Matrix | `Confusion Matrix` | Generic Data | item | La matriz de confusión general. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Accuracy | `Accuracy` | Number | item | Exactitud (o concordancia global) |
| Error | `Error` | Number | item | Es lo mismo que 1.0 - exactitud |
| Precision | `Precision` | Number | lista | Precisión |
| Recall | `Recall` | Number | lista | Exhaustividad (recall) |
| Variance | `Variance` | Number | item | Varianza |
| Chance Agreement | `Chance Agreement` | Number | item | Concordancia por azar |
| Geometric Agreement | `Geometric Agreement` | Number | item | Concordancia geométrica |
| Cohen's Kappa Statistic | `Kappa` | Number | item | Estadístico Kappa de Cohen |
| Chi-Square | `Chi-Square` | Number | item | El estadístico chi-cuadrado de la tabla de contingencia. |

### Gaussian Mixture (GaussianMix)

Solver para modelos de mezcla gaussiana.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Inputs | `Inputs` | Number | árbol | La lista de entradas de entrenamiento. |
| Components | `Components` | Integer | item | Cantidad de clústeres |
| Random Seed | `seed` | Integer | item | Valor semilla para Accord. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Predicción resultante |
| Likelihood | `Likelihood` | Generic Data | item | Log-verosimilitud de que una entrada pertenezca a un clúster. |
| Probability | `Probability` | Generic Data | item | Probabilidad de que una entrada pertenezca a un clúster. |

### Hidden Markov Model (HiddenMark)

Solver para problemas de modelos ocultos de Markov.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Inputs | `Inputs` | Text | árbol | La lista de entradas de entrenamiento. |
| Generations | `Gen` | Integer | item | Cantidad de muestras nuevas a generar |
| Random Seed | `Seed` | Integer | item | Semilla aleatoria para iniciar la generación. |
| States | `States` | Integer | item | Cantidad de estados a usar en el modelo. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Generación predicha |

### K-Means Clustering (K-Means)

Solver para agrupamiento K-Means.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Inputs | `Inputs` | Number | árbol | La lista de entradas de entrenamiento. |
| # of Clusters | `Clusters` | Integer | item | Cantidad de clústeres |
| Random Seed | `seed` | Integer | item | Valor semilla para Accord. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Predicción resultante |
| Likelihood | `Likelihood` | Generic Data | item | Log-verosimilitud de que una entrada pertenezca a un clúster. |
| Centroids | `Centroids` | Generic Data | item | El centroide del clúster. |

### Kernel SVM Tester (SVM Tester)

Este componente prueba un clasificador de máquina de vectores de soporte (SVM) basado en kernel.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Support Vector Machine | `SVM` | Generic Data | item | La máquina de vectores de soporte a probar. |
| Test Input Data | `Input` | Generic Data | lista | Datos de entrada de prueba a clasificar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Classifications | `Classifications` | Generic Data | lista | Clasificaciones según los datos de entrada. |
| Probabilties | `Probabilties` | Number | árbol | Probabilidad de que un vector de entrada pertenezca a la clasificación predicha. |

### Kernel SVM Trainer (SVM Trainer)

Este componente entrena una máquina de vectores de soporte (SVM) basada en kernel con un conjunto de datos de entrenamiento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Inputs | `Inputs` | Generic Data | lista | Los datos de entrada de entrenamiento. |
| Training Classifications | `Classifications` | Generic Data | item | La lista de clasificaciones. |
| Kernel Type | `Kernel` | Integer | item | Tipo de kernel: (0) lineal (1) gaussiano (2) laplaciano (3) polinomial (4) sigmoide |
| K Folds | `K Folds` | Integer | item | La cantidad de particiones (folds) usadas en la validación cruzada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Support Vector Machine | `SVM` | Generic Data | item | Máquina de vectores de soporte (SVM) basada en kernel entrenada |
| Support Vectors | `Vectors` | Number | árbol | Vectores de soporte |
| Confusion Matrix | `Confusion Matrix` | Generic Data | item | La matriz de confusión general según las particiones de entrenamiento/prueba de la validación cruzada. |

### Linear Regression (LineReg)

Solver para problemas de regresión lineal.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Test Data | `Test` | Number | item | Datos para probar contra los datos de entrenamiento. |
| Training Inputs | `Inputs` | Number | lista | La lista de entradas de entrenamiento. |
| Training Output | `Output` | Number | lista | La lista de salidas de entrenamiento. |
| Random Seed | `seed` | Integer | item | Semilla aleatoria del algoritmo de aprendizaje. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Predicción resultante |

### Load Model

Deserializa un modelo desde un archivo guardado (*.bin)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | Ruta del modelo guardado (*.bin). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Loaded Model | `Model` | Generic Data | item | Modelo cargado |

### Logistic Regression (LogReg)

Solver para problemas de regresión logística.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Test Data | `Test` | Number | árbol | Datos para probar contra los datos de entrenamiento. |
| Training Inputs | `Inputs` | Number | árbol | La lista de entradas de entrenamiento. |
| Training Output | `Output` | Boolean | lista | La lista de salidas de entrenamiento. |
| Tolerance | `Tol` | Number | item | Valor de tolerancia para determinar si el algoritmo convergió. |
| Maximum Iterations | `MaxIter` | Integer | item | Cantidad máxima de iteraciones que hace el algoritmo |
| Regularization Value | `Regular` | Number | item | Valor de regularización que se suma a la función objetivo. |
| Random Seed | `seed` | Integer | item | Semilla aleatoria del algoritmo de aprendizaje |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Predicción resultante |
| Score | `Score` | Generic Data | item | Los puntajes predichos |

### Multivariate Linear Regression (MultiLineReg)

Solver para problemas de regresión lineal multivariada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Test Data | `Test` | Number | árbol | Datos para probar contra los datos de aprendizaje. |
| Inputs | `Inputs` | Number | árbol | La lista de entradas. |
| Output | `Output` | Number | árbol | La lista de salidas. |
| Random Seed | `seed` | Integer | item | Semilla aleatoria del algoritmo de aprendizaje |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Predicción resultante |

### Naive Bayes Classification Tester

Este componente prueba un clasificador bayesiano ingenuo (naive Bayes) adaptativo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Naive Bayes Classifier | `Classifier` | Generic Data | item | El clasificador naive Bayes a probar. |
| Test Input Data | `Input` | Generic Data | lista | Datos de entrada de prueba a clasificar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Classifications | `Classifications` | Generic Data | lista | Clasificaciones según los datos de entrada. |
| Probabilties | `Probabilties` | Number | árbol | Probabilidad de que un vector de entrada pertenezca a la clasificación predicha. |

### Naive Bayes Classification Trainer

Este componente entrena un algoritmo clasificador bayesiano ingenuo (naive Bayes) adaptativo con un conjunto de datos de entrenamiento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Inputs | `Inputs` | Generic Data | lista | Los datos de entrada de entrenamiento. |
| Training Classifications | `Classifications` | Generic Data | item | La lista de clasificaciones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trained Naive Bayes Classifier | `Classifier` | Generic Data | item | Clasificador naive Bayes entrenado |

### Neural Network Tester

Prueba una solución usando un solver de red neuronal entrenado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trained Neural Network | `Neural Network` | Generic Data | item | Una red neuronal entrenada. |
| Test Input Data | `Input` | Number | árbol | Datos de entrada de prueba. Se asume que los valores se reasignaron al dominio [-1 a 1]. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Neural Network Output | `Output` | Number | árbol | Salida de la red neuronal |

### Neural Network Trainer

Este componente usa el algoritmo de aprendizaje de retropropagación resiliente (RProp) para entrenar redes neuronales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Inputs | `Inputs` | Number | árbol | Los valores de entrada de entrenamiento |
| Training Outputs | `Outputs` | Number | árbol | Los valores de salida esperados |
| Hidden Neurons | `Hidden Neurons` | Integer | lista | Cantidad de neuronas en cada capa oculta. |
| Learning Algorithm | `Learning Algorithm` | Integer | item | Algoritmo de aprendizaje: (0) retropropagación (1) retropropagación resiliente (2) algoritmo evolutivo (genético) (3) Levenberg-Marquardt |
| Activation Function | `Activation Function` | Integer | item | Función de activación: (0) sigmoide (1) sigmoide bipolar (2) lineal (3) lineal rectificada (4) umbral (5) identidad |
| Alpha | `Alpha` | Number | item | Valor alfa. |
| Iterations | `Iterations` | Integer | item | Cantidad de iteraciones para entrenar la red. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trained Nueral Network | `Neural Network` | Generic Data | item | Red neuronal entrenada |
| Error's Dynamics | `Error` | Number | lista | Dinámica del error |

### Nonlinear Regression (NonlineReg)

Solver para problemas de regresión no lineal usando optimización mínima secuencial (SMO).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Test Data | `Test` | Number | árbol | Árbol de datos para probar contra los datos de entrenamiento. |
| Training Inputs | `Inputs` | Number | árbol | Árbol de entradas de entrenamiento. |
| Training Output | `Output` | Number | lista | La lista de salidas de entrenamiento. |
| Sigma | `Sigma` | Integer | item | Sigma de la curva de predicción |
| Complexity | `Complex` | Number | item | Complejidad de la predicción |
| Random Seed | `Seed` | Integer | item | Semilla del generador de números. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Predicción resultante |
| Score | `Score` | Generic Data | item | Los puntajes predichos |
| Error | `Error` | Generic Data | item | Error entre lo esperado y lo predicho |

### Restricted Boltzmann Machine (ResBoltz)

Solver para máquinas de Boltzmann restringidas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Test Data | `Test` | Number | lista | Datos para probar contra los datos de aprendizaje. |
| Training Inputs | `Inputs` | Number | árbol | La lista de entradas de entrenamiento. |
| Training Output | `Output` | Number | árbol | La lista de salidas de entrenamiento. |
| Momentum | `Momentum` | Number | item | Término de inercia (momentum) del algoritmo de aprendizaje. |
| Learning Rate | `Rate` | Number | item | Tasa de aprendizaje del algoritmo. |
| Decay | `Decay` | Number | item | Constante de decaimiento de pesos del algoritmo de aprendizaje. |
| Alpha | `Alpha` | Number | item | Valor alfa de la sigmoide. |
| Iterations | `Iterations` | Integer | item | Cantidad de iteraciones de aprendizaje |
| Random Seed | `seed` | Integer | item | Semilla aleatoria del algoritmo de aprendizaje |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `Result` | Generic Data | item | Predicción resultante |

## Data Sets

### Convert Column Type (Convert)

Convierte una columna a un nuevo tipo de dato. Esta transformación opera sobre tipos numéricos, booleanos, de texto, DateTime y clave.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a cambiar. |
| Column | `Column` | Text | item | El nombre de la columna del conjunto de datos a convertir. |
| Convert To Type | `Convert To` | Integer | item | Convertir al tipo: (0) número (1) booleano (2) texto (3) fecha y hora (4) clave |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos modificado. |

### Create Data Set (Create)

Crea un conjunto de datos que se puede usar para entrenar un algoritmo de aprendizaje automático.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Labels | `Labels` | Text | lista | Etiquetas usadas para nombrar cada columna de datos. |
| Data | `Data` | Generic Data | árbol | Los datos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | Los datos codificados. |

### Featurize Text (Featurize)

Transforma una columna de texto en un vector numérico de características que representa conteos normalizados de n-gramas y de n-gramas de caracteres.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a modificar. |
| Column | `Column` | Text | item | El nombre de la columna de texto del conjunto de datos a convertir en características. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos modificado. |

### Filter Data

Filtra datos según los valores de una columna.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data to Filter | `Data` | Generic Data | item | Los datos a filtrar |
| Column | `Column` | Text | item | El nombre de la columna del conjunto de datos a filtrar. |
| Lower Bound | `Lower Bound` | Number | item | El límite inferior (incluido) de los datos filtrados. |
| Upper Bound | `Upper Bound` | Number | item | El límite superior (excluido) de los datos filtrados. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos filtrado. |

### Get Column Label (Column Label)

Obtiene los nombres de las columnas de un conjunto de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a cambiar. |

### Load Data From Text File (Load Data)

Carga un conjunto de datos desde un archivo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | Ruta de un archivo. |
| Separator Character | `Separator` | Text | item | El carácter que separa los datos dentro de una fila. |
| Has Header | `Has Header` | Boolean | item | Si el archivo tiene una primera línea con los nombres de las características. Si es True, el cargador salta la primera línea al llamar al método Load. |
| Data Loader Options *(opcional)* | `Options` | Generic Data | item | Opciones adicionales para controlar cómo se carga un archivo de datos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos cargado. |

### Normalize Data (Normalize)

Normaliza los valores de una columna de un conjunto de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a cambiar. |
| Columns | `Columns` | Text | lista | Los nombres de las columnas del conjunto de datos a normalizar. |
| Fix Zero | `Fix Zero` | Boolean | item | Si se asigna el cero a cero, conservando la dispersión. Cuando fixZero es False, el intervalo normalizado es [0,1] y la distribución de los valores normalizados depende del modo de normalización. Cuando fixZero es True, el intervalo normalizado es [−1,1] y la distribución también depende del modo de normalización, pero el comportamiento es distinto: la distribución depende de qué tan lejos está cada número de 0, de modo que el número más lejano se asigna a 1 si es positivo o a -1 si es negativo. La distancia a 0 afecta la distribución: la mayoría de los números que están más juntos se normalizan hacia 0. |
| Normalization Mode | `Mode` | Integer | item | Modo de normalización: (0) Min Max: reescala la entrada según la diferencia entre los valores mínimo y máximo de los datos. (1) Mean Variance: resta la media (de los datos) y divide por la varianza (de los datos). (2) Log Mean Variance: normaliza según el logaritmo de los datos. (3) Normalize Binning: asigna el valor de entrada a un índice de intervalo (bin) y lo divide por la cantidad de intervalos, produciendo un valor entre 0 y 1. Los límites de los intervalos se calculan para repartir los datos de forma pareja. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos modificado. |

### One Hot Encoding (Encoding)

Convierte una o más columnas de texto en igual cantidad de columnas de vectores con codificación one-hot. La codificación one-hot se usa a menudo para convertir datos categóricos a una forma que se pueda entregar a un algoritmo de aprendizaje automático.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a cambiar. |
| Columns | `Columns` | Text | lista | Los nombres de las columnas del conjunto de datos a codificar. |
| Output Kind | `Output Kind` | Integer | item | Tipo de salida: (1) Bag: produce un vector en que cada posición guarda la cantidad de apariciones del valor correspondiente en el vector de entrada. Cada posición corresponde a un valor del diccionario, así que su largo es el tamaño del diccionario construido. Indicator y Bag solo difieren en cómo se agregan los vectores de bits generados por cada posición de la columna de entrada: en Indicator se concatenan y en Bag se suman. Cuando la columna de origen es un escalar, Indicator y Bag son idénticos. (2) Indicator: produce un vector indicador. Cada posición corresponde a una categoría del diccionario, así que su largo es el tamaño del diccionario construido. Si un valor no está en el diccionario, la salida es el vector cero. (3) Key: produce claves en una columna KeyDataViewType. Si la columna de entrada es un vector, la salida contiene un tipo de clave vectorial, en que cada posición corresponde a la posición respectiva del vector de entrada. Si una categoría no está en el diccionario construido, se le asigna el valor cero. (4) Binary: produce un vector con codificación binaria que representa los valores del diccionario presentes en la columna de entrada. Si un valor de la columna de entrada no está en el diccionario, la salida es el vector cero. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos modificado. |

### Peek At Data (Peek Data)

Muestra una pequeña muestra del contenido de un conjunto de datos de ML

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos cargado. |
| Number of Rows | `Rows` | Integer | item | Cantidad de filas del conjunto de datos a ver. Ojo: este componente devuelve como máximo 100 filas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `Values` | Text | árbol | Los valores de los datos. |
| Columns | `Columns` | Text | lista | Los nombres de cada columna del conjunto de datos. |

### Remove Columns

Quita columnas de un conjunto de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a cambiar. |
| Columns | `Columns` | Text | lista | Los nombres de las columnas del conjunto de datos a quitar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos modificado. |

### Replace Missing Data (Replace Data)

Reemplaza datos faltantes en una columna. Ojo: este componente solo funciona con datos numéricos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Incoming Data | `Data` | Generic Data | item | El conjunto de datos a modificar. |
| Column | `Column` | Text | item | El nombre de la columna del conjunto de datos donde reemplazar los elementos faltantes. |
| Replacement Mode | `Replacement Mode` | Integer | item | Modo de reemplazo: (0) Mean: reemplaza con el promedio de la columna (1) Minimum: reemplaza con el valor mínimo de la columna (2) Maximum: reemplaza con el valor máximo de la columna (3) Mode: reemplaza con el valor más frecuente de la columna |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos filtrado. |

### Select Columns

Selecciona columnas de un conjunto de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a cambiar. |
| Columns | `Columns` | Text | lista | Los nombres de las columnas del conjunto de datos a seleccionar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos modificado. |

### Split Data

Divide un conjunto de datos cargado en subconjuntos de entrenamiento y de prueba.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos cargado a dividir |
| Testing Fraction | `Fraction` | Number | item | La fracción del conjunto original que va al conjunto de prueba. |
| Seed | `Seed` | Integer | item | Semilla del generador aleatorio que elige las filas para la división entrenamiento/prueba. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Data Set | `Training Data` | Generic Data | item | El conjunto de datos de entrenamiento |
| Testing Data Set | `Testing Data` | Generic Data | item | El conjunto de datos de prueba |

### Text Loader Options (Options)

Opciones adicionales para controlar cómo se carga un archivo de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Columns *(opcional)* | `Columns` | Text | lista | Indica los nombres de las columnas de entrada que se asignan a las columnas del conjunto de datos. Si se entregan nombres de columna, reemplazan a la entrada de encabezado. |
| Trim Whitespace | `Trim Whitespace` | Boolean | item | Si se quitan los espacios en blanco al final de las líneas. |
| Allow Quoting | `Allow Quoting` | Boolean | item | Si la entrada puede incluir valores entre comillas dobles. Este parámetro sirve para distinguir los caracteres separadores dentro de un valor de los separadores reales. Si es True, los separadores dentro de comillas dobles se tratan como parte del valor. Si es False, todos los separadores, incluso los que están entre comillas, delimitan una columna nueva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text Loader Options | `Options` | Generic Data | item | Opciones del cargador de texto. |

### Tokenize Into Words (Tokenize)

Divide una o más columnas de texto en palabras individuales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos a modificar. |
| Column | `Column` | Text | item | El nombre de la columna de texto del conjunto de datos a tokenizar. |
| Separators *(opcional)* | `Separators` | Text | lista | Los caracteres separadores para dividir el texto en palabras. Si se deja vacío, se usa el espacio. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `Data` | Generic Data | item | El conjunto de datos modificado. |

## Models

### Binary Classifier Tester

Prueba un modelo para problemas de clasificación binaria.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Model | `Model` | Generic Data | item | Modelo de clasificación binaria entrenado. |
| Testing Data Set | `Testing Data` | Generic Data | item | El conjunto de datos de prueba. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Predictions | `Predictions` | Generic Data | árbol | Predicciones |
| Scores | `Scores` | Number | árbol | Los puntajes de todas las clases. Un valor más alto significa mayor probabilidad de pertenecer a la clase asociada. Si el elemento i tiene el mayor valor, el índice de etiqueta predicho es i. |

### Binary Classifier Trainer

Entrena un modelo para problemas de clasificación binaria.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Data Set | `Training Data` | Generic Data | item | El conjunto de datos de entrenamiento. |
| Feature Names | `Features` | Text | lista | Los nombres de las columnas del conjunto de datos que se usan como características. Las entradas de un modelo de aprendizaje automático se llaman características (features). |
| Label Name | `Label` | Text | item | El nombre de la columna del conjunto de datos que se usa como etiqueta. Los valores reales (a veces llamados salidas) que se usan para entrenar un modelo de aprendizaje automático se llaman etiquetas (labels). |
| Trainer Type | `Trainer Type` | Generic Data | item | El tipo de entrenador usado para el entrenamiento de regresión. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Model | `Model` | Generic Data | item | Modelo entrenado |

### Load Saved Model (Load Model)

Deserializa un modelo desde un archivo guardado (*.zip)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| File Path | `File Path` | Text | item | Ruta del modelo guardado (*.zip). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Loaded Model | `Model` | Generic Data | item | Modelo cargado |

### Multiclass Classifier Tester

Prueba un modelo para problemas de clasificación multiclase.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Model | `Model` | Generic Data | item | Modelo de clasificación binaria entrenado. |
| Testing Data Set | `Testing Data` | Generic Data | item | El conjunto de datos de prueba. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Predictions | `Predictions` | Generic Data | árbol | Predicciones |
| Scores | `Scores` | Number | árbol | Los puntajes de todas las clases. Un valor más alto significa mayor probabilidad de pertenecer a la clase asociada. Si el elemento i tiene el mayor valor, el índice de etiqueta predicho es i. |

### Multiclass Classifier Trainer

Entrena un modelo para problemas de clasificación multiclase.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Data Set | `Training Data` | Generic Data | item | El conjunto de datos de entrenamiento. |
| Feature Names | `Features` | Text | lista | Los nombres de las columnas del conjunto de datos que se usan como características. Las entradas de un modelo de aprendizaje automático se llaman características (features). |
| Label Name | `Label` | Text | item | El nombre de la columna del conjunto de datos que se usa como etiqueta. Los valores reales (a veces llamados salidas) que se usan para entrenar un modelo de aprendizaje automático se llaman etiquetas (labels). |
| Trainer Type | `Trainer Type` | Generic Data | item | El tipo de entrenador usado para la clasificación multiclase. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Model | `Model` | Generic Data | item | Modelo entrenado |

### Object Detection Using ONNX File (Image Classifier)

Usa un archivo de aprendizaje profundo preentrenado Open Neural Network Exchange (ONNX) para detección de objetos y segmentación de imágenes. Los modelos de detección de objetos detectan la presencia de varios objetos en una imagen y separan las zonas donde se detectan. Los modelos de segmentación semántica dividen una imagen de entrada etiquetando cada píxel en un conjunto de categorías predefinidas. Más información en https://onnx.ai/

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bitmap Path | `Bmp` | Text | item | La ruta completa de un archivo de imagen. |
| Model Path | `Model` | Text | item | La ruta del modelo ONNX preentrenado. Este componente funciona con el modelo YOLO (You Only Look Once) V4, que se puede descargar en https://github.com/onnx/models/tree/master/vision/object_detection_segmentation/yolov4. El modelo YOLO V4 es una red neuronal convolucional profunda preentrenada para detección de objetos en tiempo real que detecta 80 clases distintas. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Bitmap with Regions | `Bmp` | Generic Data | item | El mapa de bits con las cajas contenedoras dibujadas sobre la imagen. |
| Image Boundary | `Boundary` | Rectangle | item | Un rectángulo que representa el borde de la imagen. El borde está normalizado de modo que la dimensión máxima de la imagen (ancho o alto) quede dentro del dominio [0-1]. |
| Image Regions | `Regions` | Rectangle | lista | Regiones rectangulares que representan las zonas de interés clasificadas en la imagen. Los rectángulos están normalizados de modo que la dimensión máxima de la imagen (ancho o alto) quede dentro del dominio [0-1]. |
| Statistics | `Stats` | Generic Data | lista | Estadísticas de la clasificación de la imagen. |

### Regression Tester

Prueba un modelo para problemas de regresión.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Model | `Model` | Generic Data | item | Modelo de regresión entrenado. |
| Testing Data Set | `Testing Data` | Generic Data | item | El conjunto de datos de prueba. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Predictions | `Predictions` | Generic Data | árbol | Predicciones |
| R2 | `R2` | Number | item | R cuadrado (R2, también llamado coeficiente de determinación) representa el poder predictivo del modelo como un valor entre -inf y 1.00. 1.00 indica un ajuste perfecto, y el ajuste puede ser arbitrariamente malo, por lo que los puntajes pueden ser negativos. Un puntaje de 0.00 significa que el modelo adivina el valor esperado de la etiqueta. R2 mide qué tan cerca están los valores reales de prueba de los valores predichos. |
| Absolute Loss | `Abs Loss` | Number | item | La pérdida absoluta, también llamada error absoluto medio (MAE), mide qué tan cerca están las predicciones de los resultados reales. Es el promedio de todos los errores del modelo, donde el error del modelo es la distancia absoluta entre el valor de etiqueta predicho y el correcto. Este error de predicción se calcula para cada registro del conjunto de prueba y finalmente se promedia sobre todos los errores absolutos registrados. |
| Squared Loss | `Sq Loss` | Number | item | La pérdida cuadrática, también llamada error cuadrático medio (MSE) o desviación cuadrática media (MSD), indica qué tan cerca está una línea de regresión de un conjunto de valores de prueba, tomando las distancias de los puntos a la línea de regresión (esas distancias son los errores E) y elevándolas al cuadrado. El cuadrado da más peso a las diferencias grandes. |
| Root Mean Squared Loss | `RMS Loss` | Number | item | La raíz del error cuadrático medio (RMSE) mide la diferencia entre los valores que predice un modelo y los valores observados en el entorno modelado. La pérdida RMS es la raíz cuadrada de la pérdida cuadrática y tiene las mismas unidades que la etiqueta, similar a la pérdida absoluta pero dando más peso a las diferencias grandes. |

### Regression Trainer

Entrena un modelo para problemas de regresión.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Training Data Set | `Training Data` | Generic Data | item | El conjunto de datos de entrenamiento. |
| Feature Names | `Features` | Text | lista | Los nombres de las columnas del conjunto de datos que se usan como características. Las entradas de un modelo de aprendizaje automático se llaman características (features). |
| Label Name | `Label` | Text | item | El nombre de la columna del conjunto de datos que se usa como etiqueta. Los valores reales (a veces llamados salidas) que se usan para entrenar un modelo de aprendizaje automático se llaman etiquetas (labels). |
| Trainer Type | `Trainer Type` | Generic Data | item | El tipo de entrenador usado para el entrenamiento de regresión. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Model | `Model` | Generic Data | item | Modelo entrenado |

## Trainer Types

### Average Perceptron Binary Classifier (Avg Perceptron)

El clasificador binario Average Perceptron se usa para entrenar un modelo lineal de clasificación binaria con datos de etiqueta booleanos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Number of Iterations | `Iterations` | Integer | item | Cantidad de pasadas por el conjunto de entrenamiento. |
| Learning Rate | `Learning` | Number | item | La tasa de contracción de los árboles, usada para evitar el sobreajuste. |
| Decrease Learning Rate | `Decrease` | Boolean | item | Determina si se reduce o no la tasa de aprendizaje (LearningRate). Si es True, la tasa de aprendizaje se reduce con cada actualización de pesos, en proporción a la raíz cuadrada de la cantidad de actualizaciones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Fast Forest Binary Classifier (Fast Forest)

El entrenador Fast Forest se usa para entrenar un modelo de clasificación binaria con árboles de decisión, usando el método Fast Forest.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Leaves | `Leaves` | Integer | item | La cantidad máxima de hojas de cada árbol de regresión. |
| Number of Trees | `Trees` | Integer | item | Cantidad total de árboles de decisión a crear en el conjunto. |
| Minimum Example Count Per Leaf | `Count` | Integer | item | La cantidad mínima de datos necesaria para formar una hoja nueva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Fast Forest Regression (Fast Forest)

El entrenador Fast Forest se usa para entrenar un modelo de regresión con árboles de decisión, usando el método Fast Forest.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Leaves | `Leaves` | Integer | item | La cantidad máxima de hojas de cada árbol de regresión. |
| Number of Trees | `Trees` | Integer | item | Cantidad total de árboles de decisión a crear en el conjunto. |
| Minimum Example Count Per Leaf | `Count` | Integer | item | La cantidad mínima de datos necesaria para formar una hoja nueva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Fast Tree Binary Classifier (Fast Tree)

El entrenador Fast Tree se usa para entrenar un modelo de regresión con árboles de decisión, usando el método Fast Tree.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Leaves | `Leaves` | Integer | item | La cantidad máxima de hojas de cada árbol de regresión. |
| Number of Trees | `Trees` | Integer | item | Cantidad total de árboles de decisión a crear en el conjunto. |
| Minimum Example Count Per Leaf | `Count` | Integer | item | La cantidad mínima de datos necesaria para formar una hoja nueva. |
| Learning Rate | `Learning` | Number | item | La tasa de aprendizaje. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Fast Tree Regression (Fast Tree)

El entrenador Fast Tree se usa para entrenar un modelo de regresión con árboles de decisión, usando el método Fast Tree.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Leaves | `Leaves` | Integer | item | La cantidad máxima de hojas de cada árbol de regresión. |
| Number of Trees | `Trees` | Integer | item | Cantidad total de árboles de decisión a crear en el conjunto. |
| Minimum Example Count Per Leaf | `Count` | Integer | item | La cantidad mínima de datos necesaria para formar una hoja nueva. |
| Learning Rate | `Learning` | Number | item | La tasa de aprendizaje. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Fast Tree Tweedie Regression (Fast Tree Tweedie)

El entrenador Fast Tree Tweedie se usa para entrenar un modelo de regresión con árboles de decisión, usando el método Fast Tree Tweedie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Leaves | `Leaves` | Integer | item | La cantidad máxima de hojas de cada árbol de regresión. |
| Number of Trees | `Trees` | Integer | item | Cantidad total de árboles de decisión a crear en el conjunto. |
| Minimum Example Count Per Leaf | `Count` | Integer | item | La cantidad mínima de datos necesaria para formar una hoja nueva. |
| Learning Rate | `Learning` | Number | item | La tasa de aprendizaje. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Field Aware Factorization Machine Binary Classifier (Factorization)

El clasificador binario Field Aware Factorization Machine se usa para entrenar un modelo con un método de gradiente estocástico.

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Generalized Additive Models Binary Classifier (GAM)

El entrenador GAM se usa para entrenar un modelo de clasificación binaria con modelos aditivos generalizados (GAM).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Iterations | `Iterations` | Integer | item | La cantidad de iteraciones para aprender las características. |
| Maximum Bin Count Per Feature | `Bins` | Integer | item | La cantidad máxima de intervalos (bins) para aproximar las características. |
| Learning Rate | `Learning` | Number | item | La tasa de aprendizaje. Los GAM funcionan mejor con una tasa de aprendizaje pequeña. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Generalized Additive Models Regression (GAM)

El entrenador GAM se usa para entrenar un modelo de regresión con modelos aditivos generalizados (GAM).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Iterations | `Iterations` | Integer | item | La cantidad de iteraciones para aprender las características. |
| Maximum Bin Count Per Feature | `Bins` | Integer | item | La cantidad máxima de intervalos (bins) para aproximar las características. |
| Learning Rate | `Learning` | Number | item | La tasa de aprendizaje. Los GAM funcionan mejor con una tasa de aprendizaje pequeña. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Lbfgs Logistic Regression Binary Classifier (Lbfgs Logistic Regression)

El entrenador de clasificación binaria Lbfgs Logistic Regression se usa para entrenar modelos lineales de regresión logística con el método L-BFGS.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Enforce Non-Negativity | `Non-Negativity` | Boolean | item | Fuerza pesos no negativos. |
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| History Size | `History Size` | Integer | item | Cantidad de iteraciones anteriores que se recuerdan para estimar el hessiano. Valores más bajos dan estimaciones más rápidas pero menos precisas. |
| Optimization Tolerance | `Tolerance` | Number | item | Parámetro de tolerancia para la convergencia de la optimización. (Bajo = más lento y más preciso). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Lbfgs Maximum Entropy Multiclass Classifier (Lbfgs Maximum Entropy)

El modelo de máxima entropía Lbfgs es una generalización de la regresión lineal. La principal diferencia entre el modelo de máxima entropía y la regresión logística es la cantidad de clases que admite el problema de clasificación.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Enforce Non-Negativity | `Non-Negativity` | Boolean | item | Fuerza pesos no negativos. |
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| History Size | `History Size` | Integer | item | Cantidad de iteraciones anteriores que se recuerdan para estimar el hessiano. Valores más bajos dan estimaciones más rápidas pero menos precisas. |
| Optimization Tolerance | `Tolerance` | Number | item | Parámetro de tolerancia para la convergencia de la optimización. (Bajo = más lento y más preciso). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Lbfgs Poisson Regression (Lbfgs Poisson)

El entrenador Lbfgs Poisson se usa para entrenar modelos de regresión de Poisson.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Enforce Non-Negativity | `Non-Negativity` | Boolean | item | Fuerza pesos no negativos. |
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| History Size | `History Size` | Integer | item | Cantidad de iteraciones anteriores que se recuerdan para estimar el hessiano. Valores más bajos dan estimaciones más rápidas pero menos precisas. |
| Optimization Tolerance | `Tolerance` | Number | item | Parámetro de tolerancia para la convergencia de la optimización. (Bajo = más lento y más preciso). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Light GBM Binary Classifier (Light GBM)

El clasificador Light GBM entrena un modelo con un método de clasificación binaria por árboles de decisión con gradient boosting.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Leaves | `Leaves` | Integer | item | La cantidad máxima de hojas de cada árbol. |
| Number of Iterations | `Iterations` | Integer | item | La cantidad de iteraciones de boosting. En cada iteración se crea un árbol nuevo, así que equivale a la cantidad de árboles. |
| Minimum Example Count Per Leaf | `Count` | Integer | item | La cantidad mínima de datos necesaria para formar una hoja nueva. |
| Learning Rate | `Learning` | Number | item | La tasa de contracción de los árboles, usada para evitar el sobreajuste. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Light Gbm Multiclass Classifier (Light Gbm)

El entrenador LightGBM es una implementación de código abierto de árboles de decisión con gradient boosting.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Evaluation Metric | `Eval Metric` | Integer | item | Determina qué métrica de evaluación usar: 1) por defecto 2) error 3) log loss 4) ninguna |
| Learning Rate | `Learning Rate` | Number | item | La tasa de contracción de los árboles, usada para evitar el sobreajuste. El rango válido es [0,1]. |
| Sigmoid Parameter | `Sigmoid` | Number | item | Determina la pendiente de la función sigmoide |
| Use SoftMax | `Use Softmax` | Boolean | item | Determina si se usa la función de pérdida SoftMax. La función SoftMax es una generalización de la función logística a varias dimensiones. |
| Max Bins Per Feature | `Max Bins` | Integer | item | La cantidad máxima de intervalos (bins) en que se agrupan los valores de las características. Pocos intervalos pueden reducir la precisión del entrenamiento pero aumentar la capacidad de generalización (contra el sobreajuste). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Light GBM Regression (Light GBM)

Light GBM entrena un modelo con un método de regresión por árboles de decisión con gradient boosting.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Leaves | `Leaves` | Integer | item | La cantidad máxima de hojas de cada árbol. |
| Number of Iterations | `Iterations` | Integer | item | La cantidad de iteraciones de boosting. En cada iteración se crea un árbol nuevo, así que equivale a la cantidad de árboles. |
| Minimum Example Count Per Leaf | `Count` | Integer | item | La cantidad mínima de datos necesaria para formar una hoja nueva. |
| Learning Rate | `Learning` | Number | item | La tasa de contracción de los árboles, usada para evitar el sobreajuste. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Linear SVM Binary Classifier (Linear SVM)

El entrenador de clasificación binaria Linear SVM se usa para entrenar un modelo lineal de clasificación binaria con el método Linear SVM.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Iterations | `Iterations` | Integer | item | La cantidad de iteraciones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Local Deep SVM Binary Classifier (LDSVM)

El entrenador de clasificación binaria Local Deep SVM se usa para entrenar un modelo no lineal de clasificación binaria con el método Local Deep SVM.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Iterations | `Iterations` | Integer | item | La cantidad de iteraciones. |
| Tree Depth | `Depth` | Integer | item | La profundidad del árbol del Local Deep SVM. |
| Use Bias | `Bias` | Boolean | item | Indica si se usa o no el sesgo (bias). |
| Use Cached Data | `Cache` | Boolean | item | Indica si se usan o no datos en caché. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Naive Bayes Multiclass Classifier (Naive Bayes)

El entrenador Naive Bayes es un clasificador probabilístico que se puede usar en problemas multiclase. Con el teorema de Bayes, la probabilidad condicional de que una muestra pertenezca a una clase se calcula según la cantidad de muestras de cada combinación de características. Sin embargo, el clasificador Naive Bayes solo es viable si la cantidad de características y de valores que puede tomar cada una es relativamente pequeña. Asume independencia entre las características de una clase, aunque puedan depender unas de otras. Este entrenador multiclase acepta valores de características binarios de tipo float: los valores mayores que cero se tratan como verdaderos y los menores o iguales a 0, como falsos.

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Online Gradient Descent Regression (Online Gradient Descent)

El entrenador Online Gradient Descent se usa para entrenar un modelo de regresión lineal con el método de descenso de gradiente en línea para estimar sus parámetros.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Number of Iterations | `Iterations` | Integer | item | Cantidad de pasadas por el conjunto de entrenamiento. |
| Learning Rate | `Learning` | Number | item | La tasa de contracción de los árboles, usada para evitar el sobreajuste. |
| Decrease Learning Rate | `Decrease` | Boolean | item | Determina si se reduce o no la tasa de aprendizaje (LearningRate). Si es True, la tasa de aprendizaje se reduce con cada actualización de pesos, en proporción a la raíz cuadrada de la cantidad de actualizaciones. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Ordinary Least Squares Regression (OLS)

El entrenador Ordinary Least Squares se usa para entrenar un modelo de regresión lineal con el método de mínimos cuadrados ordinarios (OLS) para estimar sus parámetros.

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### SDCA Logistic Regression Binary Classifier (SDCA Logistic Regression)

El entrenador de clasificación binaria SDCA Logistic Regression se usa para entrenar modelos de clasificación por regresión logística con el método de ascenso de coordenadas dual estocástico.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Maximum Number of Iterations | `Iterations` | Integer | item | La cantidad máxima de pasadas sobre los datos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Sdca Maximum Entropy Multiclass Classifier (Sdca Maximum Entropy)

El modelo de máxima entropía Sdca se usa para predecir un objetivo con un modelo clasificador multiclase lineal entrenado con un método de descenso de coordenadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Convergence Tolerance | `Convergence` | Number | item | La tolerancia de la razón entre la brecha de dualidad y la pérdida primal para revisar la convergencia. |
| Bias Learning Rate | `Bias` | Number | item | La tasa de aprendizaje para ajustar el sesgo para que no se regularice. |
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Shuffle | `Shuffle` | Boolean | item | Determina si se mezclan los datos en cada iteración de entrenamiento. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### SDCA Noncalibrated Binary Classifier (SDCA Noncalibrated)

El entrenador de clasificación binaria SDCA Noncalibrated se usa para entrenar modelos de clasificación por regresión logística con el método de ascenso de coordenadas dual estocástico.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Maximum Number of Iterations | `Iterations` | Integer | item | La cantidad máxima de pasadas sobre los datos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Sdca Noncalibrated Multiclass Classifier (Sdca Noncalibrated)

El modelo Sdca no calibrado se usa para predecir un objetivo con un modelo clasificador multiclase lineal entrenado con un método de descenso de coordenadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Convergence Tolerance | `Convergence` | Number | item | La tolerancia de la razón entre la brecha de dualidad y la pérdida primal para revisar la convergencia. |
| Bias Learning Rate | `Bias` | Number | item | La tasa de aprendizaje para ajustar el sesgo para que no se regularice. |
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Shuffle | `Shuffle` | Boolean | item | Determina si se mezclan los datos en cada iteración de entrenamiento. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Sdca Regression (Sdca)

El entrenador Sdca se usa para entrenar un modelo de regresión con el método de ascenso de coordenadas dual estocástico.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L1 Regularization | `L1 Regularization` | Number | item | El peso de regularización L1. |
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Maximum Number of Iterations | `Iterations` | Integer | item | La cantidad máxima de pasadas sobre los datos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### SGD Calibrated Binary Classifier (SGD Calibrated)

SGD Calibrated entrena un modelo de clasificación lineal con el método de descenso de gradiente estocástico (SGD) en paralelo. El SGD es un algoritmo iterativo que optimiza una función objetivo diferenciable.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Number of Iterations | `Iterations` | Integer | item | La cantidad máxima de pasadas por el conjunto de entrenamiento; pon 1 para simular aprendizaje en línea. |
| Learning Rate | `Learning` | Number | item | La tasa de aprendizaje inicial que usa el SGD. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### SGD Noncalibrated Binary Classifier (SGD Noncalibrated)

SGD Noncalibrated entrena un modelo de clasificación lineal con el método de descenso de gradiente estocástico (SGD) en paralelo. El SGD es un algoritmo iterativo que optimiza una función objetivo diferenciable.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| L2 Regularization | `L2 Regularization` | Number | item | El peso de regularización L2. |
| Number of Iterations | `Iterations` | Integer | item | La cantidad máxima de pasadas por el conjunto de entrenamiento; pon 1 para simular aprendizaje en línea. |
| Learning Rate | `Learning` | Number | item | La tasa de aprendizaje inicial que usa el SGD. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |

### Symbolic SGD Logistic Regression Binary Classifier (Symbolic SGD)

El clasificador Symbolic SGD Logistic Regression entrena un modelo lineal de clasificación binaria con el método de descenso de gradiente estocástico (SGD) simbólico. El SGD es un algoritmo iterativo que optimiza una función objetivo diferenciable.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number of Iterations | `Iterations` | Integer | item | Cantidad de pasadas sobre los datos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Trainer Type | `Trainer Type` | Generic Data | item | El entrenador usado para problemas de aprendizaje automático. |
