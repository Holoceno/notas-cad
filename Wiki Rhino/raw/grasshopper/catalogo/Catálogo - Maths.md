---
title: "Catálogo Grasshopper — Maths"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Maths"
libraries: ["Curve Components 8.35.26251.13001", "Grasshopper 1.0.0008", "Math Components 8.35.26251.13001", "RhinoCodePluginGH", "Script Components 1.0.0.0", "Transform Components 8.35.26251.13001"]
components: 110
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, matematicas]
---

# Maths

110 objetos · librería: Curve Components 8.35.26251.13001, Grasshopper 1.0.0008, Math Components 8.35.26251.13001, RhinoCodePluginGH, Script Components 1.0.0.0, Transform Components 8.35.26251.13001 · autor: Robert McNeel & Associates

Mapas: [[Mapa - Matemáticas]] (103) · [[Mapa - Scripts, interfaz y archivos]] (7)

## Domain

### Bounds (Bnd)

Crea un dominio numérico que abarca una lista de números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Números a incluir en los límites |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain | item | Dominio numérico entre el número menor y el mayor de {N} |

### Bounds 2D (Bnd)

Crea un dominio numérico bidimensional que abarca una lista de coordenadas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Coordinates | `C` | Point | lista | Coordenadas bidimensionales a incluir en los límites |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain² | item | Dominio numérico bidimensional entre los números menor y mayor de {N.x ; N.y} |

### Consecutive Domains (Consec)

Crea dominios consecutivos a partir de una lista de números

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Números para los dominios consecutivos |
| Additive | `A` | Boolean | item | Si es True, los valores se suman a un total acumulado |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `D` | Domain | lista | Dominios que describen los espacios entre los números |

### Construct Domain (Dom)

Crea un dominio numérico a partir de dos extremos numéricos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain start | `A` | Number | item | Valor inicial del dominio numérico |
| Domain end | `B` | Number | item | Valor final del dominio numérico |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain | item | Dominio numérico entre {A} y {B} |

### Construct Domain² (Dom²)

Crea un dominio bidimensional a partir de dos dominios simples.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain U | `U` | Domain | item | Dominio en la dirección {u} |
| Domain V | `V` | Domain | item | Dominio en la dirección {v} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 2D Domain | `I²` | Domain² | item | Dominio numérico bidimensional de {u} y {v} |

### Construct Domain² (Dom²Num)

Crea un dominio bidimensional a partir de cuatro números.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U min | `U0` | Number | item | Límite inferior del dominio en la dirección {u} |
| U max | `U1` | Number | item | Límite superior del dominio en la dirección {u} |
| V min | `V0` | Number | item | Límite inferior del dominio en la dirección {v} |
| V max | `V1` | Number | item | Límite superior del dominio en la dirección {v} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| 2D Domain | `I²` | Domain² | item | Dominio numérico bidimensional de {u} y {v} |

### Deconstruct Domain (DeDomain)

Descompone un dominio numérico en sus partes.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain | item | Dominio base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Start | `S` | Number | item | Inicio del dominio |
| End | `E` | Number | item | Final del dominio |

### Deconstruct Domain² (DeDom2Num)

Descompone un dominio bidimensional en cuatro números

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain² | item | Dominio base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U min | `U0` | Number | item | Límite inferior del dominio en la dirección {u} |
| U max | `U1` | Number | item | Límite superior del dominio en la dirección {u} |
| V min | `V0` | Number | item | Límite inferior del dominio en la dirección {v} |
| V max | `V1` | Number | item | Límite superior del dominio en la dirección {v} |

### Deconstruct Domain² (DeDom2)

Descompone un dominio bidimensional en sus partes

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain² | item | Dominio base |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| U component | `U` | Domain | item | Componente {u} del dominio |
| V component | `V` | Domain | item | Componente {v} del dominio |

### Divide Domain (Div)

Divide un dominio en segmentos iguales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain | item | Dominio base |
| Count | `C` | Integer | item | Cantidad de segmentos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Segments | `S` | Domain | lista | Segmentos de la división |

### Divide Domain² (Divide)

Divide un dominio bidimensional en segmentos iguales.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domain | `I` | Domain² | item | Dominio base |
| U Count | `U` | Integer | item | Cantidad de segmentos en la dirección {u} |
| V Count | `V` | Integer | item | Cantidad de segmentos en la dirección {v} |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Segments | `S` | Domain² | lista | Segmentos individuales |

### Find Domain (FDom)

Busca el primer dominio que contiene un valor específico

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Domains | `D` | Domain | lista | Colección de dominios en la que buscar |
| Number | `N` | Number | item | Número a probar |
| Strict | `S` | Boolean | item | Comparación estricta: si es True, el valor debe estar en el interior de un dominio |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Index | `I` | Integer | item | Índice del primer dominio que incluye el valor indicado |
| Neighbour | `N` | Integer | item | Índice del dominio más cercano al valor indicado |

### Includes (Inc)

Prueba si un valor numérico está incluido en el dominio

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `V` | Number | item | Valor cuya inclusión se prueba |
| Domain | `D` | Domain | item | Dominio con el que probar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Includes | `I` | Boolean | item | True si el valor está incluido en el dominio |
| Deviation | `D` | Number | item | Distancia entre el valor y el valor más cercano dentro del dominio |

### Remap Numbers (ReMap)

Reasigna números a un nuevo dominio numérico (remap)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `V` | Number | item | Valor a reasignar |
| Source | `S` | Domain | item | Dominio de origen |
| Target | `T` | Domain | item | Dominio de destino |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mapped | `R` | Number | item | Número reasignado |
| Clipped | `C` | Number | item | Número reasignado y recortado al dominio |

## Matrix

### Construct Matrix (Matrix)

Construye una matriz a partir de valores iniciales

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rows | `R` | Integer | item | Cantidad de filas de la matriz |
| Columns | `C` | Integer | item | Cantidad de columnas de la matriz |
| Values *(opcional)* | `V` | Number | lista | Valores opcionales de la matriz; si se omiten, se crea una matriz identidad |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Una matriz recién creada |

### Deconstruct Matrix (DeMatrix)

Descompone una matriz en sus partes

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Rows | `R` | Integer | item | Cantidad de filas de la matriz |
| Columns | `C` | Integer | item | Cantidad de columnas de la matriz |
| Values | `V` | Number | lista | Valores de la matriz |

### Display Matrix (Matrix, parámetro)

Muestra una matriz

Tipo de dato: **Matrix**

### Invert Matrix (MInvert)

Invierte una matriz

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz a invertir |
| Tolerance | `t` | Number | item | Tolerancia de cero para la inversión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz invertida |
| Success | `S` | Boolean | item | Booleano que indica si la inversión funcionó |

### Swap Columns (SwapC)

Intercambia dos columnas de una matriz

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz para el intercambio de columnas |
| Column A | `A` | Integer | item | Índice de la primera columna |
| Column B | `B` | Integer | item | Índice de la segunda columna |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz con las filas intercambiadas |

### Swap Rows (SwapR)

Intercambia dos filas de una matriz

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz para el intercambio de filas |
| Row A | `A` | Integer | item | Índice de la primera fila |
| Row B | `B` | Integer | item | Índice de la segunda fila |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz con las filas intercambiadas |

### Transpose Matrix (Transpose)

Transpone una matriz (intercambia filas y columnas)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Una matriz recién creada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Matrix | `M` | Matrix | item | Matriz transpuesta |

## Operators

### Absolute (Abs)

Calcula el valor absoluto de un valor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Addition (A+B)

Suma matemática

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A *(opcional)* | `A` | Generic Data | item | Primer elemento de la suma |
| B *(opcional)* | `B` | Generic Data | item | Segundo elemento de la suma |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado de la suma |

### Division (A/B)

División matemática

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | Elemento a dividir (dividendo) |
| B | `B` | Generic Data | item | Elemento por el que dividir (divisor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | El resultado de la división |

### Equality (Equals)

Prueba la igualdad (o desigualdad) de dos números

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First Number | `A` | Number | item | Número a comparar |
| Second Number | `B` | Number | item | Número con el que comparar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Equality | `=` | Boolean | item | True si A = B |
| Inequality | `≠` | Boolean | item | True si A ≠ B |

### Factorial (Fac)

Devuelve el factorial de un entero.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `N` | Integer | item | Entero de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factorial | `F` | Generic Data | item | Factorial de {N} |

### Gate And (And)

Realiza la conjunción booleana (compuerta AND).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A *(opcional)* | `A` | Boolean | item | Primer booleano de la operación AND |
| B *(opcional)* | `B` | Boolean | item | Segundo booleano de la operación AND |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Valor resultante |

### Gate Majority (Vote)

Calcula el voto de mayoría entre tres booleanos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Boolean | item | Primer booleano |
| B | `B` | Boolean | item | Segundo booleano |
| C | `C` | Boolean | item | Tercer booleano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Valor promedio |

### Gate Nand (Nand)

Realiza la negación alternativa booleana (compuerta NAND).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Boolean | item | Booleano de la izquierda |
| B | `B` | Boolean | item | Booleano de la derecha |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Valor resultante |

### Gate Nor (Nor)

Realiza la negación conjunta booleana (compuerta NOR).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Boolean | item | Booleano de la izquierda |
| B | `B` | Boolean | item | Booleano de la derecha |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Valor resultante |

### Gate Not (Not)

Realiza la negación booleana (compuerta NOT).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Boolean | item | Valor booleano |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Inverso de {A} |

### Gate Or (Or)

Realiza la disyunción booleana (compuerta OR).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A *(opcional)* | `A` | Boolean | item | Primer booleano de la operación OR |
| B *(opcional)* | `B` | Boolean | item | Segundo booleano de la operación OR |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Valor resultante |

### Gate Xnor (Xnor)

Realiza el bicondicional booleano (compuerta XNOR).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Boolean | item | Booleano de la izquierda |
| B | `B` | Boolean | item | Booleano de la derecha |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Valor resultante |

### Gate Xor (Xor)

Realiza la disyunción exclusiva booleana (compuerta XOR).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Boolean | item | Booleano de la izquierda |
| B | `B` | Boolean | item | Booleano de la derecha |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Boolean | item | Valor resultante |

### Integer Division (A∖B)

División entera matemática

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Integer | item | Elemento a dividir (dividendo) |
| B | `B` | Integer | item | Elemento por el que dividir (divisor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Integer | item | Resultado de la división entera |

### Larger Than (Larger)

Mayor que (o igual a)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First Number | `A` | Number | item | Número a probar |
| Second Number | `B` | Number | item | Número contra el que probar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Larger than | `>` | Boolean | item | True si A > B |
| … or Equal to | `>=` | Boolean | item | True si A >= B |

### Mass Addition (MA)

Realiza la suma de todos los elementos de una lista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Input | `I` | Generic Data | lista | Valores de entrada para la suma masiva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado de la suma masiva |
| Partial Results | `Pr` | Generic Data | lista | Lista de resultados parciales |

### Mass Multiplication (MM)

Realiza la multiplicación de todos los elementos de una lista

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Input | `I` | Generic Data | lista | Valores de entrada para la multiplicación masiva. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado de la multiplicación masiva |
| Partial Results | `Pr` | Generic Data | lista | Lista de resultados parciales |

### Modulus (Mod)

Divide dos números y devuelve solo el resto.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | Primer número del módulo (dividendo) |
| B | `B` | Generic Data | item | Segundo número del módulo (divisor) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | El resto de A/B |

### Multiplication (A×B)

Multiplicación matemática

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A *(opcional)* | `A` | Generic Data | item | Primer elemento de la multiplicación |
| B *(opcional)* | `B` | Generic Data | item | Segundo elemento de la multiplicación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado de la multiplicación |

### Negative (Neg)

Calcula el negativo de un valor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Power (Pow)

Eleva un valor a una potencia.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | El elemento a elevar |
| B | `B` | Generic Data | item | El exponente |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | A elevado a la potencia B |

### Relative Differences (RelDif)

Calcula las diferencias relativas de una lista de datos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Values | `V` | Generic Data | lista | Lista de datos sobre la que operar (se permiten números, puntos o vectores) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Differenced | `D` | Generic Data | lista | Diferencias entre elementos consecutivos |

### Similarity (Similar)

Prueba la similitud de dos números

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First Number | `A` | Number | item | Número a comparar |
| Second Number | `B` | Number | item | Número con el que comparar |
| Threshold | `T%` | Number | item | Porcentaje (0% ~ 100%) de A y B bajo el cual se asume que son similares |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Similarity | `=` | Boolean | item | True si A ≈ B |
| Absolute difference | `dt` | Number | item | La diferencia absoluta entre A y B |

### Smaller Than (Smaller)

Menor que (o igual a)

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| First Number | `A` | Number | item | Número a probar |
| Second Number | `B` | Number | item | Número contra el que probar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Smaller than | `<` | Boolean | item | True si A < B |
| … or Equal to | `<=` | Boolean | item | True si A <= B |

### Subtraction (A-B)

Resta matemática

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A *(opcional)* | `A` | Generic Data | item | Primer operando de la resta |
| B *(opcional)* | `B` | Generic Data | item | Segundo operando de la resta |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado de la resta |

## Polynomials

### Cube

Calcula el cubo de un valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Cube Root (Cbrt)

Calcula la raíz cúbica de un valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Log N (LogN)

Devuelve el logaritmo en base N de un número.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `V` | Number | item | Valor |
| Base | `B` | Number | item | Base del logaritmo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Number | item | Resultado |

### Logarithm (Log)

Calcula el logaritmo en base 10 de un valor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Natural logarithm (Ln)

Calcula el logaritmo natural de un valor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### One Over X (1/x)

Calcula uno dividido por x.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Power of 10 (10º)

Eleva 10 a la potencia N.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Power of 2 (2º)

Eleva 2 a la potencia N.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Power of E (Eº)

Eleva E a la potencia N.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Square (Sqr)

Calcula el cuadrado de un valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Square Root (Sqrt)

Calcula la raíz cuadrada de un valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

## Script

### C♯ Script (C♯)

Componente de script C#

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Generic Data | item | Sin conversión |
| y *(opcional)* | `y` | Generic Data | item | Sin conversión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| out | `out` | Text | item | Contenido de la salida estándar y de errores recolectado durante la ejecución del script |
| a | `a` | Generic Data | item | Sin conversión |

### Evaluate (Eval)

Evalúa una expresión con una cantidad flexible de variables.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Expression | `E` | Expression | item | Expresión a evaluar |
| x *(opcional)* | `x` | Expression Variant | item | Valor 'x' usado para evaluar la expresión |
| y *(opcional)* | `y` | Expression Variant | item | Valor 'y' usado para evaluar la expresión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado de la expresión |

### Expression

Evalúa una expresión

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Expression Variant | item | Valor 'x' usado para evaluar '' |
| y *(opcional)* | `y` | Expression Variant | item | Valor 'y' usado para evaluar '' |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | Resultado de la expresión |

### IronPython 2 Script (IPy2)

Componente de script IronPython 2

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Generic Data | item | Sin conversión |
| y *(opcional)* | `y` | Generic Data | item | Sin conversión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| out | `out` | Text | item | Contenido de la salida estándar y de errores recolectado durante la ejecución del script |
| a | `a` | Generic Data | item | Sin conversión |

### Python 3 Script (Py3)

Componente de script Python 3

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Generic Data | item | Sin conversión |
| y *(opcional)* | `y` | Generic Data | item | Sin conversión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| out | `out` | Text | item | Contenido de la salida estándar y de errores recolectado durante la ejecución del script |
| a | `a` | Generic Data | item | Sin conversión |

### Script (S)

Componente de script

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Generic Data | item | Sin conversión |
| y *(opcional)* | `y` | Generic Data | item | Sin conversión |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| out | `out` | Text | item | Contenido de la salida estándar y de errores recolectado durante la ejecución del script |
| a | `a` | Generic Data | item | Sin conversión |

### VB Script (VB)

Un componente con script VB.NET

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| x *(opcional)* | `x` | Generic Data | item | Variable de script x |
| y *(opcional)* | `y` | Generic Data | item | Variable de script y |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| out | `out` | Text | lista | Flujos de impresión, reflexión y error |
| A | `A` | Generic Data | item | Parámetro de salida A |

## Time

### Combine Date & Time (CDate)

Combina una fecha y una hora en una sola fecha

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Date | `D` | Time | item | Parte de la fecha |
| Time | `T` | Time | item | Parte de la hora |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Time | item | Combinación resultante de fecha y hora. |

### Construct Date (Date)

Construye una instancia de fecha y hora.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Year | `Y` | Integer | item | Número de año (debe estar entre 1 y 9999) |
| Month | `M` | Integer | item | Número de mes (debe estar entre 1 y 12) |
| Day | `D` | Integer | item | Día del mes (debe estar entre 1 y 31) |
| Hour | `h` | Integer | item | Hora del día (debe estar entre 0 y 23) |
| Minute | `m` | Integer | item | Minuto de la hora (debe estar entre 0 y 59) |
| Second | `s` | Integer | item | Segundo del minuto (debe estar entre 0 y 59) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Date | `D` | Time | item | Datos de fecha y hora |

### Construct Exotic Date (DateEx)

Construye una fecha usando un calendario específico

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Year | `Y` | Integer | item | Número de año (debe estar entre 1 y 9999) |
| Month | `M` | Integer | item | Número de mes (debe estar entre 1 y 12) |
| Day | `D` | Integer | item | Día del mes (debe estar entre 1 y 31) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Time | `T` | Time | item | Representación gregoriana de la fecha. |

### Construct Smooth Time (SmTime)

Construye una instancia de tiempo a partir de componentes continuos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Days | `D` | Number | item | Cantidad de días |
| Hours | `H` | Number | item | Cantidad de horas |
| Minutes | `M` | Number | item | Cantidad de minutos |
| Seconds | `S` | Number | item | Cantidad de segundos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Time | `T` | Time | item | Tiempo construido |

### Construct Time (Time)

Construye una instancia de tiempo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Hour | `H` | Integer | item | Cantidad de horas |
| Minute | `M` | Integer | item | Cantidad de minutos |
| Second | `S` | Integer | item | Cantidad de segundos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Time | `T` | Time | item | Tiempo construido |

### Date Range (RDate)

Crea un rango de fechas u horas sucesivas

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Time A | `A` | Time | item | Primer tiempo |
| Time B | `B` | Time | item | Segundo tiempo |
| Count | `N` | Integer | item | Cantidad de tiempos a crear entre A y B |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Range | `R` | Time | lista | Rango de tiempos variables entre A y B. |

### Deconstruct Date (DDate)

Descompone una fecha en años, meses, días, horas, minutos y segundos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Date | `D` | Time | item | Datos de fecha y hora |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Year | `Y` | Integer | item | Número de año |
| Month | `M` | Integer | item | Número de mes |
| Day | `D` | Integer | item | Día del mes |
| Hour | `h` | Integer | item | Hora del día |
| Minute | `m` | Integer | item | Minuto de la hora |
| Second | `s` | Integer | item | Segundo del minuto |

### Interpolate Date (IntDate)

Interpola entre dos fechas u horas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Date A | `A` | Time | item | Primera fecha |
| Date B | `B` | Time | item | Segunda fecha |
| Interpolation | `t` | Number | item | Factor de interpolación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Date | `D` | Time | item | Fecha y hora interpolada |

## Trig

### ArcCosine (ACos)

Calcula el ángulo cuyo coseno es el valor indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### ArcSine (ASin)

Calcula el ángulo cuyo seno es el valor indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### ArcTangent (ATan)

Calcula el ángulo cuya tangente es el valor indicado.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Centroid

Genera el centroide de un triángulo a partir de sus medianas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primera esquina del triángulo |
| Point B | `B` | Point | item | Segunda esquina del triángulo |
| Point C | `C` | Point | item | Tercera esquina del triángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Centroid | `C` | Point | item | Punto centroide del triángulo |
| Median AB | `AB` | Line | item | Mediana que conecta el lado AB con la esquina C |
| Median BC | `BC` | Line | item | Mediana que conecta el lado BC con la esquina A |
| Median CA | `CA` | Line | item | Mediana que conecta el lado CA con la esquina B |

### Circumcentre (CCentre)

Genera el circuncentro de un triángulo a partir de las mediatrices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primera esquina del triángulo |
| Point B | `B` | Point | item | Segunda esquina del triángulo |
| Point C | `C` | Point | item | Tercera esquina del triángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Circumcentre | `C` | Point | item | Punto circuncentro del triángulo |
| Bisector AB | `AB` | Line | item | Mediatriz que sale del lado AB |
| Bisector BC | `BC` | Line | item | Mediatriz que sale del lado AB |
| Bisector CA | `CA` | Line | item | Mediatriz que sale del lado AB |

### CoSecant (Csc)

Calcula la cosecante (recíproco del seno) de un ángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Cosine (Cos)

Calcula el coseno de un valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### CoTangent (Cot)

Calcula la cotangente (recíproco de la tangente) de un ángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Degrees (Deg)

Convierte un ángulo en radianes a grados

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Radians | `R` | Number | item | Ángulo en radianes |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Degrees | `D` | Number | item | Ángulo en grados |

### Incentre (ICentre)

Genera el incentro de un triángulo a partir de las bisectrices.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primera esquina del triángulo |
| Point B | `B` | Point | item | Segunda esquina del triángulo |
| Point C | `C` | Point | item | Tercera esquina del triángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Incentre | `I` | Point | item | Punto incentro del triángulo |
| Bisector A | `A` | Line | item | Bisectriz que sale de la esquina A |
| Bisector B | `B` | Line | item | Bisectriz que sale de la esquina B |
| Bisector C | `C` | Line | item | Bisectriz que sale de la esquina C |

### Orthocentre (OCentre)

Genera el ortocentro de un triángulo a partir de sus alturas.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Point A | `A` | Point | item | Primera esquina del triángulo |
| Point B | `B` | Point | item | Segunda esquina del triángulo |
| Point C | `C` | Point | item | Tercera esquina del triángulo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Orthocentre | `C` | Point | item | Punto ortocentro del triángulo |
| Altitude AB | `AB` | Line | item | Altura que conecta el lado AB con la esquina C |
| Altitude BC | `BC` | Line | item | Altura que conecta el lado BC con la esquina A |
| Altitude CA | `CA` | Line | item | Altura que conecta el lado CA con la esquina B |

### Radians (Rad)

Convierte un ángulo en grados a radianes

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Degrees | `D` | Number | item | Ángulo en grados |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Radians | `R` | Number | item | Ángulo en radianes |

### Right Trigonometry (RTrig)

Trigonometría del triángulo rectángulo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha *(opcional)* | `α` | Number | item | Ángulo alfa (opcional) |
| Beta *(opcional)* | `β` | Number | item | Ángulo beta (opcional) |
| P length *(opcional)* | `P` | Number | item | Longitud del lado P (opcional) |
| Q length *(opcional)* | `Q` | Number | item | Longitud del lado Q (opcional) |
| R length *(opcional)* | `R` | Number | item | Longitud del lado R (opcional) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `α` | Number | item | Ángulo alfa calculado |
| Beta | `β` | Number | item | Ángulo beta calculado |
| P length | `P` | Number | item | Longitud calculada del lado P |
| Q length | `Q` | Number | item | Longitud calculada del lado Q |
| R length | `R` | Number | item | Longitud calculada del lado R |

### Secant (Sec)

Calcula la secante (recíproco del coseno) de un ángulo.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Sinc

Calcula el seno cardinal (sinc) de un valor.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Sine (Sin)

Calcula el seno de un valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Tangent (Tan)

Calcula la tangente de un valor

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `x` | Generic Data | item | Valor de entrada |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `y` | Generic Data | item | Valor de salida |

### Triangle Trigonometry (Trig)

Trigonometría de un triángulo cualquiera

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha *(opcional)* | `α` | Number | item | Ángulo alfa (opcional) |
| Beta *(opcional)* | `β` | Number | item | Ángulo beta (opcional) |
| Gamma *(opcional)* | `γ` | Number | item | Ángulo gamma (opcional) |
| A length *(opcional)* | `A` | Number | item | Longitud del lado A (opuesto a alfa), opcional |
| B length *(opcional)* | `B` | Number | item | Longitud del lado B (opuesto a beta), opcional |
| C length *(opcional)* | `C` | Number | item | Longitud del lado C (opuesto a gamma), opcional |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Alpha | `α` | Number | item | Ángulo alfa calculado |
| Beta | `β` | Number | item | Ángulo beta calculado |
| Gamma | `γ` | Number | item | Ángulo gamma calculado |
| A length | `A` | Number | item | Longitud calculada del lado A |
| B length | `B` | Number | item | Longitud calculada del lado B |
| C length | `C` | Number | item | Longitud calculada del lado C |

## Util

### Average (Avr)

Calcula el promedio aritmético de un conjunto de elementos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Input | `I` | Generic Data | lista | Valores de entrada a promediar |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Generic Data | item | Media aritmética (promedio) de todos los valores de entrada |

### Blur Numbers (NBlur)

Difumina una lista de números promediando sus vecinos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Números a difuminar |
| Strength | `S` | Number | item | Intensidad del difuminado (0=nada, 1=total) |
| Iterations | `I` | Integer | item | Cantidad de iteraciones sucesivas de difuminado |
| Lock | `L` | Boolean | item | Fija el primer y el último valor |
| Wrap | `W` | Boolean | item | Trata la lista como una colección cíclica |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | lista | Números difuminados |

### Clamp

Restringe un número entre dos extremos numéricos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `V` | Generic Data | item | Elemento a restringir entre dos extremos numéricos |
| Domain | `D` | Domain | item | Dominio entre dos extremos numéricos |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Clamped | `C` | Generic Data | item | Valor restringido |

### Complex Argument (Arg)

Obtiene el argumento de un número complejo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Complex | `C` | Complex | item | Número complejo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Argument | `A` | Number | item | Argumento del número complejo [C] |

### Complex Components (Complex)

Extrae las partes real e imaginaria de un número complejo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Complex | `C` | Complex | item | Número complejo a descomponer |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Real | `R` | Number | item | Parte real del número complejo |
| Imaginary | `i` | Number | item | Parte imaginaria del número complejo |

### Complex Conjugate (z*)

Crea el conjugado de un número complejo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Complex | `C` | Complex | item | Número complejo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Conjugate | `C` | Complex | item | Conjugado del número complejo [C] |

### Complex Modulus (CMod)

Obtiene el módulo de un número complejo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Complex | `C` | Complex | item | Número complejo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Modulus | `M` | Number | item | Módulo del número complejo [C] |

### Create Complex (Complex)

Crea un número complejo a partir de una parte real y una imaginaria

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Real | `R` | Number | item | Parte real del número complejo |
| Imaginary | `i` | Number | item | Parte imaginaria del número complejo |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Complex | `C` | Complex | item | Número complejo |

### Epsilon (Eps)

Devuelve un múltiplo del épsilon de coma flotante de doble precisión.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factor | `N` | Number | item | Factor por el que multiplicar épsilon |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output | `y` | Number | item | Valor de salida |

### Extremes (Extrz)

Busca los extremos de una lista de valores

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A *(opcional)* | `A` | Generic Data | item | Valor para la comparación |
| B *(opcional)* | `B` | Generic Data | item | Valor para la comparación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Mininum | `V-` | Generic Data | item | El menor de todos los valores |
| Maximum | `V+` | Generic Data | item | El mayor de todos los valores |

### Golden Ratio (Phi)

Devuelve un múltiplo de la razón áurea (Phi).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factor | `N` | Number | item | Factor por el que multiplicar Phi |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output | `y` | Number | item | Valor de salida |

### Interpolate data (Interp)

Interpola una colección de datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | lista | Datos a interpolar (solo tipos de datos simples). |
| Parameter | `t` | Number | item | Parámetro de interpolación normalizado. |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Value | `V` | Generic Data | item | Valor interpolado. |

### Maximum (Max)

Devuelve el mayor de dos elementos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | Primer elemento de la comparación |
| B | `B` | Generic Data | item | Segundo elemento de la comparación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | El mayor entre A y B |

### Minimum (Min)

Devuelve el menor de dos elementos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| A | `A` | Generic Data | item | Primer elemento de la comparación |
| B | `B` | Generic Data | item | Segundo elemento de la comparación |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `R` | Generic Data | item | El menor entre A y B |

### Natural logarithm (E)

Devuelve un múltiplo del número natural (e).

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factor | `N` | Number | item | Factor por el que multiplicar e |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output | `y` | Number | item | Valor de salida |

### Pi

Devuelve un múltiplo de Pi.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Factor | `N` | Number | item | Factor por el que multiplicar Pi |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Output | `y` | Number | item | Valor de salida |

### Round

Redondea un valor de coma flotante.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Number | `x` | Number | item | Número a redondear |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Nearest | `N` | Integer | item | Entero más cercano a x |
| Floor | `F` | Integer | item | Primer entero menor o igual que x |
| Ceiling | `C` | Integer | item | Primer entero mayor o igual que x |

### Smooth Numbers (Smooth)

Suaviza números que cambian en el tiempo

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers *(opcional)* | `N` | Number | árbol | Números que cambian |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Numbers | `N` | Number | árbol | Números suavizados |

### Truncate (Trunc)

Recorta los extremos numéricos de un conjunto

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Input | `I` | Generic Data | lista | Valores de entrada a recortar |
| Truncation factor | `t` | Number | item | Factor de recorte. Debe estar entre 0.0 (sin recorte) y 1.0 (recorte total) |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Result | `T` | Generic Data | lista | Conjunto recortado |

### Weighted Average (Wav)

Calcula el promedio ponderado de un conjunto de elementos

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Input | `I` | Generic Data | lista | Valores de entrada a promediar |
| Weights | `W` | Number | lista | Colección de pesos de cada valor |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Arithmetic mean | `AM` | Generic Data | item | Media aritmética (promedio) de todos los valores de entrada |
