---
title: "Catálogo Grasshopper — Sets"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Sets"
libraries: ["Field Components 8.35.26251.13001", "Grasshopper 1.0.0008", "Math Components 8.35.26251.13001"]
components: 89
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, datos/arboles, matematicas]
---

# Sets

89 objetos · librería: Field Components 8.35.26251.13001, Grasshopper 1.0.0008, Math Components 8.35.26251.13001 · autor: Robert McNeel & Associates

Mapas: [[Mapa - Data trees y listas]] (89) · [[Mapa - Matemáticas]] (14) · [[Mapa - Brep y sólidos]] (1)

## List

### Combine Data (Combine)

Combina los elementos no nulos de varias entradas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Input 0 *(opcional)* | `0` | Generic Data | item | Datos a combinar |
| Input 1 *(opcional)* | `1` | Generic Data | item | Datos a combinar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Datos resultantes con la menor cantidad posible de nulos |
| Index | `I` | Integer | item | Índice de la entrada que se copió en el resultado |

### Cross Reference (CrossRef)

Referencia cruzada de datos de varias listas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List (A) *(opcional)* | `A` | Generic Data | lista | Lista (A) sobre la que operar |
| List (B) *(opcional)* | `B` | Generic Data | lista | Lista (B) sobre la que operar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List (A) | `A` | Generic Data | lista | Lista (A) ajustada |
| List (B) | `B` | Generic Data | lista | Lista (B) ajustada |

### Dispatch

Reparte (dispatch) los elementos de una lista en dos listas de destino.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a filtrar |
| Dispatch pattern | `P` | Boolean | lista | Patrón de reparto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List A | `A` | Generic Data | lista | Destino del reparto para los valores True |
| List B | `B` | Generic Data | lista | Destino del reparto para los valores False |

### Insert Items (Ins)

Inserta una colección de elementos en una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a modificar |
| Item *(opcional)* | `I` | Generic Data | lista | Elementos a insertar. Si no se entregan, se insertan nulos. |
| Indices | `i` | Integer | lista | Índice de inserción de cada elemento |
| Wrap | `W` | Boolean | item | Si es True, los índices se envuelven (wrap) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista con los valores insertados |

### Item Index (Index)

Obtiene el índice de un elemento en una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista en la que buscar |
| Item | `i` | Generic Data | item | Elemento a buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Index | `i` | Integer | item | El índice del elemento en la lista, o -1 si no se encontró. |

### List Item (Item)

Obtiene un elemento específico de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista base |
| Index | `i` | Integer | item | Índice del elemento |
| Wrap | `W` | Boolean | item | Envuelve (wrap) el índice dentro de los límites de la lista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Item | `i` | Generic Data | item | Elemento en {i'} |

### List Length (Lng)

Mide el largo de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L` | Integer | item | Cantidad de elementos en L |

### Longest List (Long)

Alarga una colección de listas hasta el largo de la más larga

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List (A) *(opcional)* | `A` | Generic Data | lista | Lista (A) sobre la que operar |
| List (B) *(opcional)* | `B` | Generic Data | lista | Lista (B) sobre la que operar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List (A) | `A` | Generic Data | lista | Lista (A) ajustada |
| List (B) | `B` | Generic Data | lista | Lista (B) ajustada |

### Null Item (Null)

Prueba si un dato es nulo o inválido

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Item *(opcional)* | `I` | Generic Data | item | Elemento a probar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Null Flags | `N` | Boolean | item | True si el elemento es nulo. |
| Invalid Flags | `X` | Boolean | item | True si el elemento es inválido o nulo. |
| Description | `D` | Text | item | Una descripción de texto del estado del objeto. |

### Partition List (Partition)

Parte una lista en sublistas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a partir |
| Size | `S` | Integer | lista | Tamaño de las partes |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Chunks | `C` | Generic Data | árbol | Partes de la lista |

### Pick'n'Choose (P'n'C)

Elige y selecciona de un conjunto de datos de entrada.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Integer | lista | Patrón de selección de los índices de entrada |
| Stream 0 *(opcional)* | `0` | Generic Data | lista | Flujo de entrada 0 |
| Stream 1 *(opcional)* | `1` | Generic Data | lista | Flujo de entrada 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | lista | Resultado seleccionado |

### Replace Items (Replace)

Reemplaza ciertos elementos de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a modificar |
| Item *(opcional)* | `I` | Generic Data | lista | Elementos con los que reemplazar. Si no se entregan, se insertan nulos. |
| Indices *(opcional)* | `i` | Integer | lista | Índice de reemplazo de cada elemento |
| Wrap | `W` | Boolean | item | Si es True, los índices se envuelven (wrap) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista con los valores reemplazados |

### Replace Nulls (NullRep)

Reemplaza datos nulos o inválidos por otros datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Items | `I` | Generic Data | lista | Elementos en los que buscar nulos |
| Replacements | `R` | Generic Data | lista | Elementos con los que reemplazar los nulos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Items | `I` | Generic Data | lista | Lista sin nulos |
| Count | `N` | Integer | item | Cantidad de elementos reemplazados |

### Reverse List (Rev)

Invierte el orden de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista invertida |

### Shift List (Shift)

Desplaza todos los elementos de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a desplazar |
| Shift | `S` | Integer | item | Desplazamiento |
| Wrap | `W` | Boolean | item | Envolver (wrap) los valores |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista desplazada |

### Shortest List (Short)

Acorta una colección de listas hasta el largo de la más corta

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List (A) *(opcional)* | `A` | Generic Data | lista | Lista (A) sobre la que operar |
| List (B) *(opcional)* | `B` | Generic Data | lista | Lista (B) sobre la que operar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List (A) | `A` | Generic Data | lista | Lista (A) ajustada |
| List (B) | `B` | Generic Data | lista | Lista (B) ajustada |

### Sift Pattern (Sift)

Separa (sift) los elementos de una lista usando un patrón de índices que se repite.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a separar |
| Sift Pattern | `P` | Integer | lista | Patrón de separación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output 0 | `0` | Generic Data | lista | Salida para el índice de separación 0 |
| Output 1 | `1` | Generic Data | lista | Salida para el índice de separación 1 |

### Sort List (Sort)

Ordena una lista de claves numéricas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Keys | `K` | Number | lista | Lista de claves ordenables |
| Values A *(opcional)* | `A` | Generic Data | lista | Lista opcional de valores a ordenar en sincronía |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Keys | `K` | Number | lista | Claves ordenadas |
| Values A | `A` | Generic Data | lista | Valores sincronizados en A |

### Split List (Split)

Divide una lista en partes separadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista base |
| Index | `i` | Integer | item | Índice de división |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List A | `A` | Generic Data | lista | Elementos a la izquierda de (i) |
| List B | `B` | Generic Data | lista | Elementos a la derecha de (i), incluido (i) |

### Sub List (SubSet)

Extrae un subconjunto de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista base |
| Domain | `D` | Domain | item | Dominio de índices a copiar |
| Wrap | `W` | Boolean | item | Reasigna los índices que se salen del dominio de la lista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Subconjunto de la lista base |
| Index | `I` | Integer | lista | Índices de los elementos del subconjunto |

### Weave

Entrelaza (weave) un conjunto de datos de entrada con un patrón personalizado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Pattern | `P` | Integer | lista | Patrón de entrelazado de los índices de entrada |
| Stream 0 | `0` | Generic Data | lista | Flujo de entrada 0 |
| Stream 1 | `1` | Generic Data | lista | Flujo de entrada 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Weave | `W` | Generic Data | lista | Resultado del entrelazado |

## Sequence

### Char Sequence (CharSeq)

Crea una secuencia de caracteres de texto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Count | `C` | Integer | item | Cantidad de elementos de la secuencia. |
| Char Pool | `P` | Text | item | Conjunto de caracteres disponibles para la secuencia. |
| Format *(opcional)* | `F` | Text | item | Máscara de formato opcional |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sequence | `S` | Text | lista | Secuencia de etiquetas de caracteres |

### Cull Index (Cull i)

Elimina (cull) elementos indexados de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a la que eliminar elementos |
| Indices | `I` | Integer | lista | Índices a eliminar |
| Wrap | `W` | Boolean | item | Envuelve (wrap) los índices dentro del rango de la lista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista con los elementos eliminados |

### Cull Nth (CullN)

Elimina (cull) cada N-ésimo elemento de una lista.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a la que eliminar elementos |
| Cull frequency | `N` | Integer | item | Frecuencia de eliminación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista con los elementos eliminados |

### Cull Pattern (Cull)

Elimina (cull) elementos de una lista usando una máscara de bits que se repite.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a la que eliminar elementos |
| Cull Pattern | `P` | Boolean | lista | Patrón de eliminación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista con los elementos eliminados |

### Duplicate Data (Dup)

Duplica datos una cantidad predefinida de veces.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | lista | Datos a duplicar |
| Number | `N` | Integer | item | Cantidad de duplicados |
| Order | `O` | Boolean | item | Conserva el orden de la lista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | lista | Datos duplicados |

### Fibonacci (Fib)

Crea una sucesión de Fibonacci.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Seed A | `A` | Number | item | Primer número semilla de la sucesión |
| Seed B | `B` | Number | item | Segundo número semilla de la sucesión |
| Number | `N` | Integer | item | Cantidad de valores de la sucesión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Series | `S` | Number | lista | Los primeros N números de esta sucesión de Fibonacci |

### Jitter

Mezcla al azar una lista de valores.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Valores a mezclar |
| Jitter | `J` | Number | item | Intensidad de la mezcla (0.0 = sin mezclar, 1.0 = mezcla completa) |
| Seed | `S` | Integer | item | Semilla del motor de mezcla |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `V` | Generic Data | lista | Valores mezclados |
| Indices | `I` | Integer | lista | Mapa de índices de los elementos mezclados |

### Random

Genera una lista de números pseudoaleatorios.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Range | `R` | Domain | item | Dominio del rango numérico aleatorio |
| Number | `N` | Integer | item | Cantidad de valores aleatorios |
| Seed | `S` | Integer | item | Semilla del motor aleatorio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Random | `R` | Generic Data | lista | Números aleatorios |

### Random Reduce (Reduce)

Quita al azar N elementos de una lista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista a reducir |
| Reduction | `R` | Integer | item | Cantidad de elementos a quitar |
| Seed | `S` | Integer | item | Valor semilla del generador aleatorio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista reducida |

### Range

Crea un rango de números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `D` | Domain | item | Dominio del rango numérico |
| Steps | `N` | Integer | item | Cantidad de pasos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Range | `R` | Number | lista | Rango de números |

### Repeat Data (Repeat)

Repite un patrón hasta alcanzar cierto largo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | lista | Patrón a repetir |
| Length | `L` | Integer | item | Largo del patrón final |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | lista | Datos repetidos |

### Sequence (Seq)

Genera una secuencia de números

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Notation | `N` | Text | item | Notación de la secuencia |
| Length | `L` | Integer | item | Largo final de la secuencia |
| Initial | `I` | Number | lista | Valores iniciales de la secuencia |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Sequence | `S` | Number | lista | Secuencia |

### Series

Crea una serie de números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start | `S` | Number | item | Primer número de la serie |
| Step | `N` | Number | item | Tamaño del paso de cada número sucesivo |
| Count | `C` | Integer | item | Cantidad de valores de la serie |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Series | `S` | Number | lista | Serie de números |

### Stack Data (Stack)

Duplica elementos individuales de una lista de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | lista | Datos a apilar |
| Stack | `S` | Integer | lista | Patrón de apilado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | lista | Datos apilados |

## Sets

### Carthesian Product (CProd)

Crea el producto cartesiano de dos conjuntos de igual cardinalidad.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A | `A` | Generic Data | lista | Primer conjunto para el producto cartesiano. |
| Set B | `B` | Generic Data | lista | Segundo conjunto para el producto cartesiano. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Product | `P` | Generic Data | árbol | Producto cartesiano de A y B. |

### Create Set (CSet)

Crea el conjunto válido a partir de una lista de elementos (un conjunto válido solo contiene elementos distintos).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| List | `L` | Generic Data | lista | Lista de datos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set | `S` | Generic Data | lista | Un conjunto con todos los valores distintos de L |
| Map | `M` | Integer | lista | Un mapa de índices de los índices originales a los índices del conjunto |

### Delete Consecutive (DCon)

Elimina miembros similares consecutivos de un conjunto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set | `S` | Generic Data | lista | Conjunto sobre el que operar. |
| Wrap | `W` | Boolean | item | Si es True, el último y el primer miembro se consideran adyacentes. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set | `S` | Generic Data | lista | Conjunto sin los miembros idénticos consecutivos. |
| Count | `N` | Integer | item | Cantidad de miembros eliminados. |

### Disjoint

Prueba si dos conjuntos son disjuntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A | `A` | Generic Data | lista | Primer conjunto. |
| Set B | `B` | Generic Data | lista | Segundo conjunto. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | True si ninguno de los elementos de A aparece en B. |

### Find similar member (FSim)

Busca el miembro más parecido en un conjunto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | item | Dato a buscar. |
| Set | `S` | Generic Data | lista | Conjunto en el que buscar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hit | `H` | Generic Data | item | Miembro de S más cercano a D. |
| Index | `i` | Integer | item | Índice de H en el conjunto. |

### Key/Value Search (KeySearch)

Extrae un elemento de una colección según una coincidencia clave-valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Keys | `K` | Generic Data | lista | Una lista de valores clave. |
| Values | `V` | Generic Data | lista | Una lista de datos de valor, uno por cada clave. |
| Search | `S` | Generic Data | item | Un valor clave a buscar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Elemento resultante de la lista de valores que coincide con la clave buscada |

### Member Index (MIndex)

Busca las apariciones de un miembro específico en un conjunto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set | `S` | Generic Data | lista | Conjunto sobre el que operar. |
| Member | `M` | Generic Data | item | Miembro a buscar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Index | `I` | Integer | lista | Índices del miembro. |
| Count | `N` | Integer | item | Cantidad de apariciones del miembro. |

### Replace Members (Replace)

Reemplaza miembros de un conjunto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set | `S` | Generic Data | lista | Conjunto sobre el que operar. |
| Find | `F` | Generic Data | lista | Elemento(s) a reemplazar. |
| Replace *(opcional)* | `R` | Generic Data | lista | Elemento(s) con los que reemplazar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | lista | Conjuntos con los miembros reemplazados. |

### Set Difference (Difference)

Crea la diferencia de dos conjuntos (los objetos presentes en A pero no en B).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A | `A` | Generic Data | lista | Conjunto del que restar. |
| Set B | `B` | Generic Data | lista | Conjunto a restar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Union | `U` | Generic Data | lista | La diferencia de conjuntos A menos B |

### Set Difference (S) (ExDiff)

Crea la diferencia simétrica de dos conjuntos (los objetos presentes en A o en B, pero no en ambos).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A | `A` | Generic Data | lista | Primer conjunto para la diferencia simétrica. |
| Set B | `B` | Generic Data | lista | Segundo conjunto para la diferencia simétrica. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| ExDifference | `X` | Generic Data | lista | La diferencia simétrica entre A y B. |

### Set Intersection (Intersection)

Crea la intersección de dos conjuntos (los objetos únicos presentes en ambos conjuntos).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A *(opcional)* | `A` | Generic Data | lista | Datos para la intersección de conjuntos |
| Set B *(opcional)* | `B` | Generic Data | lista | Datos para la intersección de conjuntos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Union | `U` | Generic Data | lista | La unión de todos los conjuntos de entrada |

### Set Majority (Majority)

Determina qué miembros aparecen en la mayoría de tres conjuntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A | `A` | Generic Data | lista | Primer conjunto. |
| Set B | `B` | Generic Data | lista | Segundo conjunto. |
| Set C | `C` | Generic Data | lista | Tercer conjunto. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | lista | Conjunto con todos los elementos únicos que aparecen en al menos dos de los conjuntos de entrada. |

### Set Union (SUnion)

Crea la unión de dos conjuntos (los objetos únicos presentes en cualquiera de los dos).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A *(opcional)* | `A` | Generic Data | lista | Datos para la unión de conjuntos. |
| Set B *(opcional)* | `B` | Generic Data | lista | Datos para la unión de conjuntos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Union | `U` | Generic Data | lista | La unión de los conjuntos A y B. |

### SubSet

Prueba la inclusión entre dos conjuntos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Set A | `A` | Generic Data | lista | Superconjunto. |
| Set B | `B` | Generic Data | lista | Subconjunto. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | True si todos los elementos de B están en A. |

## Text

### Characters (Chars)

Separa un texto en caracteres individuales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto a separar. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `C` | Text | lista | Caracteres resultantes |
| Unicode | `U` | Integer | lista | Valor Unicode del carácter |

### Concatenate (Concat)

Concatena fragmentos de texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fragment A *(opcional)* | `A` | Text | item | Primer fragmento de texto |
| Fragment B *(opcional)* | `B` | Text | item | Segundo fragmento de texto |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Text | item | Texto resultante formado por todos los fragmentos |

### Format

Da formato a datos usando marcadores de posición y etiquetas de formato

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Format | `F` | Text | item | Formato del texto |
| Culture | `C` | Culture | item | Cultura (idioma/región) del formato |
| Data 0 *(opcional)* | `0` | Generic Data | item | Datos a insertar en los marcadores {0} |
| Data 1 *(opcional)* | `1` | Generic Data | item | Datos a insertar en los marcadores {1} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto con formato |

### Match Text (TMatch)

Compara un texto con un patrón

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto a comparar |
| Pattern *(opcional)* | `P` | Text | item | Patrón opcional con comodines para la comparación |
| RegEx *(opcional)* | `R` | Text | item | Patrón RegEx opcional para la comparación |
| Case | `C` | Boolean | item | Compara distinguiendo mayúsculas y minúsculas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Match | `M` | Boolean | item | True si el texto cumple todos los patrones entregados |

### Replace Text (Rep)

Reemplaza todas las apariciones de un fragmento de texto por otro

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto sobre el que operar. |
| Find *(opcional)* | `F` | Text | item | Fragmento a reemplazar. |
| Replace *(opcional)* | `R` | Text | item | Fragmento opcional con el que reemplazar. Si se deja vacío, se quitan todas las apariciones de F. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Text | item | Resultado del reemplazo de texto |

### Sort Text (TSort)

Ordena una colección de fragmentos de texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Keys | `K` | Text | lista | Fragmentos de texto a ordenar (clave de orden) |
| Values *(opcional)* | `V` | Generic Data | lista | Valores opcionales a ordenar en sincronía |
| Culture | `C` | Culture | item | Reglas culturales de orden |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Keys | `K` | Text | lista | Fragmentos de texto ordenados |
| Values | `V` | Generic Data | lista | Valores ordenados |

### Text Case (Case)

Cambia las MaYúScUlAs de un texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto a modificar |
| Culture | `C` | Culture | item | Reglas culturales para mayúsculas y minúsculas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Upper Case | `U` | Text | item | Representación en mayúsculas de T |
| Lower Case | `L` | Text | item | Representación en minúsculas de T |

### Text Distance (TDist)

Calcula la distancia de Levenshtein entre dos fragmentos de texto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text A | `A` | Text | item | Primer fragmento de texto |
| Text B | `B` | Text | item | Segundo fragmento de texto |
| Case | `C` | Boolean | item | Compara distinguiendo mayúsculas y minúsculas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Distance | `D` | Integer | item | Distancia de Levenshtein entre los dos fragmentos |

### Text Fragment (Fragment)

Extrae un fragmento (subconjunto) de un texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto sobre el que operar. |
| Start | `i` | Integer | item | Índice, desde cero, del primer carácter a copiar. |
| Count *(opcional)* | `N` | Integer | item | Cantidad opcional de caracteres a copiar. Si se deja vacío, se copia todo el resto. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Fragment | `F` | Text | item | El fragmento de texto resultante |

### Text Join (Join)

Une una colección de fragmentos de texto en uno

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | lista | Fragmentos de texto a unir. |
| Join *(opcional)* | `J` | Text | item | Separador de fragmentos. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Text | item | Texto resultante |

### Text Length (Len)

Obtiene el largo (cantidad de caracteres) de un texto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto a medir. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Length | `L` | Integer | item | Cantidad de caracteres |

### Text On Surface (TextSrf)

Crea una colección de símbolos de texto alineados sobre una superficie.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto a crear. |
| Font | `F` | Text | item | Nombre de la fuente, con las etiquetas opcionales 'Bold' o 'Italic'. |
| Height | `H` | Number | item | Altura de las formas del texto. |
| Depth | `D` | Number | item | Profundidad de las formas del texto. |
| Base Line | `B` | Curve | item | Línea base del texto. |
| Base Surface *(opcional)* | `S` | Generic Data | item | Superficie base opcional para orientar el texto. Se permiten superficies, mallas y SubDs. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Symbols | `S` | Brep | lista | Símbolos que forman las formas del texto. |

### Text Split (Split)

Divide un texto en fragmentos usando separadores

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto a separar. |
| Separators | `C` | Text | item | Caracteres separadores. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Text | lista | Fragmentos de texto resultantes |

### Text Trim (Trim)

Quita los espacios en blanco al inicio y al final de un texto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Text | `T` | Text | item | Texto a separar. |
| Start | `S` | Boolean | item | Quitar los espacios al inicio. |
| End | `E` | Boolean | item | Quitar los espacios al final. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Text | item | Texto recortado. |

## Tree

### Clean Tree (Clean)

Quita todos los elementos nulos e inválidos de un árbol de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Remove Nulls | `N` | Boolean | item | Quita los elementos nulos del árbol. |
| Remove Invalid | `X` | Boolean | item | Quita los elementos inválidos del árbol. |
| Remove Empty | `E` | Boolean | item | Quita las ramas vacías del árbol. |
| Tree | `T` | Generic Data | árbol | Árbol de datos a limpiar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos impecable |

### Construct Path (Path)

Construye una ruta de rama de un árbol de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Indices | `I` | Integer | lista | Índices de la ruta de rama |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Branch | `B` | Path | item | Ruta de rama |

### Deconstruct Path (DPath)

Descompone una ruta de árbol de datos en enteros individuales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Branch | `B` | Path | item | Ruta de rama |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Indices | `I` | Integer | lista | Índices de la ruta de rama |

### Entwine

Aplana y combina una colección de flujos de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Branch {0;0} *(opcional)* | `{0;0}` | Generic Data | árbol | Datos a entrelazar |
| Branch {0;1} *(opcional)* | `{0;1}` | Generic Data | árbol | Datos a entrelazar |
| Branch {0;2} *(opcional)* | `{0;2}` | Generic Data | árbol | Datos a entrelazar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado entrelazado |

### Explode Tree (BANG!)

Extrae todas las ramas de un árbol

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data *(opcional)* | `D` | Generic Data | árbol | Datos a explotar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Branch 0 | `-` | Generic Data | árbol | Todos los datos dentro de la rama en el índice 0 |
| Branch 1 | `-` | Generic Data | árbol | Todos los datos dentro de la rama en el índice 1 |

### Flatten Tree (Flatten)

Aplana un árbol de datos quitando toda la información de ramas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a aplanar |
| Path | `P` | Path | item | Ruta del árbol aplanado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos aplanado |

### Flip Matrix (Flip)

Voltea un árbol de datos tipo matriz intercambiando filas y columnas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Matriz de datos a voltear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Matriz de datos volteada |

### Graft Tree (Graft)

Injerta (graft) un árbol de datos agregando una rama extra por cada elemento.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a injertar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos injertado |

### Match Tree (Match)

Hace coincidir un árbol de datos con otro.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a modificar |
| Guide | `G` | Generic Data | árbol | Árbol de datos con el que coincidir |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos coincidente, con los datos de T pero la estructura de G |

### Merge

Fusiona varios flujos de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data 1 *(opcional)* | `D1` | Generic Data | árbol | Flujo de datos 1 |
| Data 2 *(opcional)* | `D2` | Generic Data | árbol | Flujo de datos 2 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | árbol | Resultado de la fusión |

### Path Compare (Compare)

Compara una ruta con un patrón de máscara

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Path | `P` | Path | item | Ruta a comparar |
| Mask | `M` | Text | item | Máscara de comparación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Comparison | `C` | Boolean | item | Comparación (True = coincide, False = no coincide) |

### Path Mapper (parámetro)

Realiza operaciones léxicas sobre árboles de datos.

Tipo de dato: **Goo**

### Prune Tree (Prune)

Quita las ramas pequeñas de un árbol de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a podar |
| Minimum | `N0` | Integer | item | Quita las ramas con menos de N0 elementos. |
| Maximum | `N1` | Integer | item | Quita las ramas con más de N1 elementos (usa cero para ignorar el límite superior). |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol podado |

### Relative Item (RelItem)

Obtiene un par de elementos relativos de un árbol de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol sobre el que operar |
| Offset | `O` | Text | item | Desfase relativo del par de elementos |
| Wrap Paths | `Wp` | Boolean | item | Envuelve (wrap) las rutas cuando el desplazamiento se sale de los límites |
| Wrap Items | `Wi` | Boolean | item | Envuelve (wrap) los elementos cuando el desplazamiento se sale de los límites |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Item A | `A` | Generic Data | árbol | Elemento del árbol |
| Item B | `B` | Generic Data | árbol | Elemento del árbol relativo a A |

### Relative Items (RelItem2)

Obtiene un par de elementos relativos de dos árboles de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree A | `A` | Generic Data | árbol | Primer árbol de datos |
| Tree B | `B` | Generic Data | árbol | Segundo árbol de datos |
| Offset | `O` | Text | item | Desfase relativo del par de elementos |
| Wrap Paths | `Wp` | Boolean | item | Envuelve (wrap) las rutas cuando el desplazamiento se sale de los límites |
| Wrap Items | `Wi` | Boolean | item | Envuelve (wrap) los elementos cuando el desplazamiento se sale de los límites |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Item A | `A` | Generic Data | árbol | Elemento en el árbol A |
| Item B | `B` | Generic Data | árbol | Elemento relativo en el árbol B |

### Replace Paths (Replace)

Busca y reemplaza rutas en un árbol de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Flujo de datos a procesar |
| Search | `S` | Text | lista | Máscaras de búsqueda |
| Replace | `R` | Path | lista | Rutas de reemplazo respectivas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Datos del árbol procesados |

### Shift Paths (PShift)

Desplaza los índices de todas las rutas de un árbol de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Datos a modificar |
| Offset | `O` | Integer | item | Desfase a aplicar a cada rama |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Datos desplazados |

### Simplify Tree (Simplify)

Simplifica un árbol de datos quitando la parte de la ruta que comparten todas las ramas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a simplificar. |
| Front | `F` | Boolean | item | Limita el colapso de rutas solo a los índices del inicio de la ruta. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos simplificado. |

### Split Tree (Split)

Divide un árbol de datos en dos partes usando máscaras de ruta.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Árbol a dividir |
| Masks | `M` | Text | lista | Máscaras de división |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Positive | `P` | Generic Data | árbol | Conjunto positivo de datos (todas las ramas que coinciden con alguna máscara) |
| Negative | `N` | Generic Data | árbol | Conjunto negativo de datos (todas las ramas que no coinciden con ninguna máscara) |

### Stream Filter (Filter)

Filtra una colección de flujos de entrada

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Gate | `G` | Integer | item | Índice del flujo de compuerta (gate) |
| Stream 0 *(opcional)* | `0` | Generic Data | árbol | Flujo de entrada en el índice 0 |
| Stream 1 *(opcional)* | `1` | Generic Data | árbol | Flujo de entrada en el índice 1 |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Stream | `S` | Generic Data | árbol | Flujo filtrado |

### Stream Gate (Gate)

Redirige un flujo hacia salidas específicas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Stream | `S` | Generic Data | árbol | Flujo de entrada |
| Gate | `G` | Integer | item | Índice de compuerta del flujo de salida |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Target 0 | `0` | Generic Data | árbol | Salida para el índice de compuerta 0 |
| Target 1 | `1` | Generic Data | árbol | Salida para el índice de compuerta 1 |

### Tree Branch (Branch)

Obtiene una rama específica de un árbol de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos |
| Path | `P` | Path | item | Ruta de la rama del árbol de datos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Branch | `B` | Generic Data | árbol | Rama en {P} |

### Tree Item (Item)

Obtiene un elemento específico de un árbol de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos |
| Path | `P` | Path | item | Ruta de la rama del árbol de datos |
| Index | `i` | Integer | item | Índice del elemento |
| Wrap | `W` | Boolean | item | Envuelve (wrap) el índice dentro de los límites de la lista |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Element | `E` | Generic Data | item | Elemento en {P:i'} |

### Tree Statistics (TStat)

Obtiene estadísticas de un árbol de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a analizar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Paths | `P` | Path | lista | Todas las rutas del árbol |
| Length | `L` | Integer | lista | El largo de cada rama del árbol |
| Count | `C` | Integer | item | Cantidad de rutas y ramas del árbol |

### Trim Tree (Trim)

Reduce la complejidad de un árbol fusionando las ramas más externas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a aplanar |
| Depth | `D` | Integer | item | Cantidad de ramas externas a fusionar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos recortado |

### Unflatten Tree (Unflatten)

Desaplana un árbol de datos devolviendo los elementos a sus ramas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos a desaplanar |
| Guide | `G` | Generic Data | árbol | Árbol de datos guía que define la estructura de rutas |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Tree | `T` | Generic Data | árbol | Árbol de datos desaplanado |
