---
tags: [tipo/mapa, matematicas, matematicas/numeros, software/grasshopper, lenguaje/python]
---

# Matemáticas

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Números, dominios (intervalos), operadores, trigonometría, lógica booleana, matrices y expresiones. En Grasshopper, muchas cadenas de 5 componentes matemáticos se reemplazan por una sola [[Catálogo - Maths#Expression|Expression]] o unas líneas de Python.

## Teoría y código
- [[wiki/concepts/vector-mathematics]] · [[wiki/concepts/transformaciones-geometricas]] (matrices)
- [[wiki/concepts/curvatura]] · [[wiki/entities/essential-mathematics-computational-design]]

## Equivalencias con Python

| Tarea | Grasshopper | Python |
|---|---|---|
| Remapear a otro rango | [[Catálogo - Maths#Remap Numbers (ReMap)\|Remap Numbers]] | `b0 + (x - a0) * (b1 - b0) / (a1 - a0)` |
| Dominio (intervalo) | [[Catálogo - Maths#Construct Domain (Dom)\|Construct Domain]] | `rg.Interval(a, b)` |
| Dividir un dominio | [[Catálogo - Maths#Divide Domain (Div)\|Divide Domain]] | `[rg.Interval(a + d * i, a + d * (i + 1)) for i in range(n)]` con `d = (b - a) / n` |
| Limitar | [[Catálogo - Maths#Clamp\|Clamp]] | `max(lo, min(hi, x))` |
| Redondear | [[Catálogo - Maths#Round\|Round]] | `round(x)`, `math.floor(x)`, `math.ceil(x)` |
| Seno (radianes) | [[Catálogo - Maths#Sine (Sin)\|Sine]] | `math.sin(math.radians(grados))` |
| Promedio | [[Catálogo - Maths#Average (Avr)\|Average]] | `sum(xs) / len(xs)` |
| Comparar | [[Catálogo - Maths#Larger Than (Larger)\|Larger Than]] | `a > b`, `a >= b` |
| Lógica | [[Catálogo - Maths#Gate And (And)\|Gate And]] / [[Catálogo - Maths#Gate Or (Or)\|Gate Or]] / [[Catálogo - Maths#Gate Not (Not)\|Gate Not]] | `and`, `or`, `not` |
| Fórmula libre | [[Catálogo - Maths#Expression\|Expression]] | cualquier expresión de Python |

## Para empezar
[[Catálogo - Maths#Expression|Expression]] · [[Catálogo - Maths#Remap Numbers (ReMap)|Remap Numbers]] · [[Catálogo - Maths#Construct Domain (Dom)|Construct Domain]] · [[Catálogo - Maths#Bounds (Bnd)|Bounds]] · [[Catálogo - Sets#Series|Series]] · [[Catálogo - Sets#Range|Range]] · [[Catálogo - Params#Graph Mapper (Graph, parámetro)|Graph Mapper]] · [[Catálogo - Maths#Mass Addition (MA)|Mass Addition]]

<!-- AUTO:inicio -->

## Componentes de Grasshopper (174)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Primitive (8)

- [[Catálogo - Params#Complex (C, parámetro)|Complex (C, parámetro)]] — Contiene una colección de números complejos
- [[Catálogo - Params#Domain (parámetro)|Domain (parámetro)]] — Contiene una colección de dominios numéricos
- [[Catálogo - Params#Domain² (parámetro)|Domain² (parámetro)]] — Contiene una colección de dominios numéricos 2D
- [[Catálogo - Params#Integer (Int, parámetro)|Integer (Int, parámetro)]] — Contiene una colección de números enteros
- [[Catálogo - Params#Matrix (parámetro)|Matrix (parámetro)]] — Contiene una colección de matrices numéricas
- [[Catálogo - Params#Number (Num, parámetro)|Number (Num, parámetro)]] — Contiene una colección de números de coma flotante
- [[Catálogo - Params#Time (parámetro)|Time (parámetro)]] — Contiene una colección de horas y fechas
- [[Catálogo - Params#Unit System (parámetro)|Unit System (parámetro)]] — Contiene una colección de sistemas de unidades del modelo

### Maths › Domain (14)

- [[Catálogo - Maths#Bounds (Bnd)|Bounds (Bnd)]] — Crea un dominio numérico que abarca una lista de números
- [[Catálogo - Maths#Bounds 2D (Bnd)|Bounds 2D (Bnd)]] — Crea un dominio numérico bidimensional que abarca una lista de coordenadas
- [[Catálogo - Maths#Consecutive Domains (Consec)|Consecutive Domains (Consec)]] — Crea dominios consecutivos a partir de una lista de números
- [[Catálogo - Maths#Construct Domain (Dom)|Construct Domain (Dom)]] — Crea un dominio numérico a partir de dos extremos numéricos
- [[Catálogo - Maths#Construct Domain² (Dom²)|Construct Domain² (Dom²)]] — Crea un dominio bidimensional a partir de dos dominios simples
- [[Catálogo - Maths#Construct Domain² (Dom²Num)|Construct Domain² (Dom²Num)]] — Crea un dominio bidimensional a partir de cuatro números
- [[Catálogo - Maths#Deconstruct Domain (DeDomain)|Deconstruct Domain (DeDomain)]] — Descompone un dominio numérico en sus partes
- [[Catálogo - Maths#Deconstruct Domain² (DeDom2)|Deconstruct Domain² (DeDom2)]] — Descompone un dominio bidimensional en sus partes
- [[Catálogo - Maths#Deconstruct Domain² (DeDom2Num)|Deconstruct Domain² (DeDom2Num)]] — Descompone un dominio bidimensional en cuatro números
- [[Catálogo - Maths#Divide Domain (Div)|Divide Domain (Div)]] — Divide un dominio en segmentos iguales
- [[Catálogo - Maths#Divide Domain² (Divide)|Divide Domain² (Divide)]] — Divide un dominio bidimensional en segmentos iguales
- [[Catálogo - Maths#Find Domain (FDom)|Find Domain (FDom)]] — Busca el primer dominio que contiene un valor específico
- [[Catálogo - Maths#Includes (Inc)|Includes (Inc)]] — Prueba si un valor numérico está incluido en el dominio
- [[Catálogo - Maths#Remap Numbers (ReMap)|Remap Numbers (ReMap)]] — Reasigna números a un nuevo dominio numérico (remap)

### Maths › Matrix (7)

- [[Catálogo - Maths#Construct Matrix (Matrix)|Construct Matrix (Matrix)]] — Construye una matriz a partir de valores iniciales
- [[Catálogo - Maths#Deconstruct Matrix (DeMatrix)|Deconstruct Matrix (DeMatrix)]] — Descompone una matriz en sus partes
- [[Catálogo - Maths#Display Matrix (Matrix, parámetro)|Display Matrix (Matrix, parámetro)]] — Muestra una matriz
- [[Catálogo - Maths#Invert Matrix (MInvert)|Invert Matrix (MInvert)]] — Invierte una matriz
- [[Catálogo - Maths#Swap Columns (SwapC)|Swap Columns (SwapC)]] — Intercambia dos columnas de una matriz
- [[Catálogo - Maths#Swap Rows (SwapR)|Swap Rows (SwapR)]] — Intercambia dos filas de una matriz
- [[Catálogo - Maths#Transpose Matrix (Transpose)|Transpose Matrix (Transpose)]] — Transpone una matriz (intercambia filas y columnas)

### Maths › Operators (25)

- [[Catálogo - Maths#Absolute (Abs)|Absolute (Abs)]] — Calcula el valor absoluto de un valor
- [[Catálogo - Maths#Addition (A+B)|Addition (A+B)]] — Suma matemática
- [[Catálogo - Maths#Division (A/B)|Division (A/B)]] — División matemática
- [[Catálogo - Maths#Equality (Equals)|Equality (Equals)]] — Prueba la igualdad (o desigualdad) de dos números
- [[Catálogo - Maths#Factorial (Fac)|Factorial (Fac)]] — Devuelve el factorial de un entero
- [[Catálogo - Maths#Gate And (And)|Gate And (And)]] — Realiza la conjunción booleana (compuerta AND)
- [[Catálogo - Maths#Gate Majority (Vote)|Gate Majority (Vote)]] — Calcula el voto de mayoría entre tres booleanos
- [[Catálogo - Maths#Gate Nand (Nand)|Gate Nand (Nand)]] — Realiza la negación alternativa booleana (compuerta NAND)
- [[Catálogo - Maths#Gate Nor (Nor)|Gate Nor (Nor)]] — Realiza la negación conjunta booleana (compuerta NOR)
- [[Catálogo - Maths#Gate Not (Not)|Gate Not (Not)]] — Realiza la negación booleana (compuerta NOT)
- [[Catálogo - Maths#Gate Or (Or)|Gate Or (Or)]] — Realiza la disyunción booleana (compuerta OR)
- [[Catálogo - Maths#Gate Xnor (Xnor)|Gate Xnor (Xnor)]] — Realiza el bicondicional booleano (compuerta XNOR)
- [[Catálogo - Maths#Gate Xor (Xor)|Gate Xor (Xor)]] — Realiza la disyunción exclusiva booleana (compuerta XOR)
- [[Catálogo - Maths#Integer Division (A∖B)|Integer Division (A∖B)]] — División entera matemática
- [[Catálogo - Maths#Larger Than (Larger)|Larger Than (Larger)]] — Mayor que (o igual a)
- [[Catálogo - Maths#Mass Addition (MA)|Mass Addition (MA)]] — Realiza la suma de todos los elementos de una lista
- [[Catálogo - Maths#Mass Multiplication (MM)|Mass Multiplication (MM)]] — Realiza la multiplicación de todos los elementos de una lista
- [[Catálogo - Maths#Modulus (Mod)|Modulus (Mod)]] — Divide dos números y devuelve solo el resto
- [[Catálogo - Maths#Multiplication (A×B)|Multiplication (A×B)]] — Multiplicación matemática
- [[Catálogo - Maths#Negative (Neg)|Negative (Neg)]] — Calcula el negativo de un valor
- [[Catálogo - Maths#Power (Pow)|Power (Pow)]] — Eleva un valor a una potencia
- [[Catálogo - Maths#Relative Differences (RelDif)|Relative Differences (RelDif)]] — Calcula las diferencias relativas de una lista de datos
- [[Catálogo - Maths#Similarity (Similar)|Similarity (Similar)]] — Prueba la similitud de dos números
- [[Catálogo - Maths#Smaller Than (Smaller)|Smaller Than (Smaller)]] — Menor que (o igual a)
- [[Catálogo - Maths#Subtraction (A-B)|Subtraction (A-B)]] — Resta matemática

### Maths › Polynomials (11)

- [[Catálogo - Maths#Cube|Cube]] — Calcula el cubo de un valor
- [[Catálogo - Maths#Cube Root (Cbrt)|Cube Root (Cbrt)]] — Calcula la raíz cúbica de un valor
- [[Catálogo - Maths#Log N (LogN)|Log N (LogN)]] — Devuelve el logaritmo en base N de un número
- [[Catálogo - Maths#Logarithm (Log)|Logarithm (Log)]] — Calcula el logaritmo en base 10 de un valor
- [[Catálogo - Maths#Natural logarithm (Ln)|Natural logarithm (Ln)]] — Calcula el logaritmo natural de un valor
- [[Catálogo - Maths#One Over X (1/x)|One Over X (1/x)]] — Calcula uno dividido por x
- [[Catálogo - Maths#Power of 10 (10º)|Power of 10 (10º)]] — Eleva 10 a la potencia N
- [[Catálogo - Maths#Power of 2 (2º)|Power of 2 (2º)]] — Eleva 2 a la potencia N
- [[Catálogo - Maths#Power of E (Eº)|Power of E (Eº)]] — Eleva E a la potencia N
- [[Catálogo - Maths#Square (Sqr)|Square (Sqr)]] — Calcula el cuadrado de un valor
- [[Catálogo - Maths#Square Root (Sqrt)|Square Root (Sqrt)]] — Calcula la raíz cuadrada de un valor

### Maths › Time (8)

- [[Catálogo - Maths#Combine Date & Time (CDate)|Combine Date & Time (CDate)]] — Combina una fecha y una hora en una sola fecha
- [[Catálogo - Maths#Construct Date (Date)|Construct Date (Date)]] — Construye una instancia de fecha y hora
- [[Catálogo - Maths#Construct Exotic Date (DateEx)|Construct Exotic Date (DateEx)]] — Construye una fecha usando un calendario específico
- [[Catálogo - Maths#Construct Smooth Time (SmTime)|Construct Smooth Time (SmTime)]] — Construye una instancia de tiempo a partir de componentes continuos
- [[Catálogo - Maths#Construct Time (Time)|Construct Time (Time)]] — Construye una instancia de tiempo
- [[Catálogo - Maths#Date Range (RDate)|Date Range (RDate)]] — Crea un rango de fechas u horas sucesivas
- [[Catálogo - Maths#Deconstruct Date (DDate)|Deconstruct Date (DDate)]] — Descompone una fecha en años, meses, días, horas, minutos y segundos
- [[Catálogo - Maths#Interpolate Date (IntDate)|Interpolate Date (IntDate)]] — Interpola entre dos fechas u horas

### Maths › Trig (18)

- [[Catálogo - Maths#ArcCosine (ACos)|ArcCosine (ACos)]] — Calcula el ángulo cuyo coseno es el valor indicado
- [[Catálogo - Maths#ArcSine (ASin)|ArcSine (ASin)]] — Calcula el ángulo cuyo seno es el valor indicado
- [[Catálogo - Maths#ArcTangent (ATan)|ArcTangent (ATan)]] — Calcula el ángulo cuya tangente es el valor indicado
- [[Catálogo - Maths#Centroid|Centroid]] — Genera el centroide de un triángulo a partir de sus medianas
- [[Catálogo - Maths#Circumcentre (CCentre)|Circumcentre (CCentre)]] — Genera el circuncentro de un triángulo a partir de las mediatrices
- [[Catálogo - Maths#CoSecant (Csc)|CoSecant (Csc)]] — Calcula la cosecante (recíproco del seno) de un ángulo
- [[Catálogo - Maths#Cosine (Cos)|Cosine (Cos)]] — Calcula el coseno de un valor
- [[Catálogo - Maths#CoTangent (Cot)|CoTangent (Cot)]] — Calcula la cotangente (recíproco de la tangente) de un ángulo
- [[Catálogo - Maths#Degrees (Deg)|Degrees (Deg)]] — Convierte un ángulo en radianes a grados
- [[Catálogo - Maths#Incentre (ICentre)|Incentre (ICentre)]] — Genera el incentro de un triángulo a partir de las bisectrices
- [[Catálogo - Maths#Orthocentre (OCentre)|Orthocentre (OCentre)]] — Genera el ortocentro de un triángulo a partir de sus alturas
- [[Catálogo - Maths#Radians (Rad)|Radians (Rad)]] — Convierte un ángulo en grados a radianes
- [[Catálogo - Maths#Right Trigonometry (RTrig)|Right Trigonometry (RTrig)]] — Trigonometría del triángulo rectángulo
- [[Catálogo - Maths#Secant (Sec)|Secant (Sec)]] — Calcula la secante (recíproco del coseno) de un ángulo
- [[Catálogo - Maths#Sinc|Sinc]] — Calcula el seno cardinal (sinc) de un valor
- [[Catálogo - Maths#Sine (Sin)|Sine (Sin)]] — Calcula el seno de un valor
- [[Catálogo - Maths#Tangent (Tan)|Tangent (Tan)]] — Calcula la tangente de un valor
- [[Catálogo - Maths#Triangle Trigonometry (Trig)|Triangle Trigonometry (Trig)]] — Trigonometría de un triángulo cualquiera

### Maths › Util (20)

- [[Catálogo - Maths#Average (Avr)|Average (Avr)]] — Calcula el promedio aritmético de un conjunto de elementos
- [[Catálogo - Maths#Blur Numbers (NBlur)|Blur Numbers (NBlur)]] — Difumina una lista de números promediando sus vecinos
- [[Catálogo - Maths#Clamp|Clamp]] — Restringe un número entre dos extremos numéricos
- [[Catálogo - Maths#Complex Argument (Arg)|Complex Argument (Arg)]] — Obtiene el argumento de un número complejo
- [[Catálogo - Maths#Complex Components (Complex)|Complex Components (Complex)]] — Extrae las partes real e imaginaria de un número complejo
- [[Catálogo - Maths#Complex Conjugate (z*)|Complex Conjugate (z*)]] — Crea el conjugado de un número complejo
- [[Catálogo - Maths#Complex Modulus (CMod)|Complex Modulus (CMod)]] — Obtiene el módulo de un número complejo
- [[Catálogo - Maths#Create Complex (Complex)|Create Complex (Complex)]] — Crea un número complejo a partir de una parte real y una imaginaria
- [[Catálogo - Maths#Epsilon (Eps)|Epsilon (Eps)]] — Devuelve un múltiplo del épsilon de coma flotante de doble precisión
- [[Catálogo - Maths#Extremes (Extrz)|Extremes (Extrz)]] — Busca los extremos de una lista de valores
- [[Catálogo - Maths#Golden Ratio (Phi)|Golden Ratio (Phi)]] — Devuelve un múltiplo de la razón áurea (Phi)
- [[Catálogo - Maths#Interpolate data (Interp)|Interpolate data (Interp)]] — Interpola una colección de datos
- [[Catálogo - Maths#Maximum (Max)|Maximum (Max)]] — Devuelve el mayor de dos elementos
- [[Catálogo - Maths#Minimum (Min)|Minimum (Min)]] — Devuelve el menor de dos elementos
- [[Catálogo - Maths#Natural logarithm (E)|Natural logarithm (E)]] — Devuelve un múltiplo del número natural (e)
- [[Catálogo - Maths#Pi|Pi]] — Devuelve un múltiplo de Pi
- [[Catálogo - Maths#Round|Round]] — Redondea un valor de coma flotante
- [[Catálogo - Maths#Smooth Numbers (Smooth)|Smooth Numbers (Smooth)]] — Suaviza números que cambian en el tiempo
- [[Catálogo - Maths#Truncate (Trunc)|Truncate (Trunc)]] — Recorta los extremos numéricos de un conjunto
- [[Catálogo - Maths#Weighted Average (Wav)|Weighted Average (Wav)]] — Calcula el promedio ponderado de un conjunto de elementos

### Sets › Sequence (14)

- [[Catálogo - Sets#Char Sequence (CharSeq)|Char Sequence (CharSeq)]] — Crea una secuencia de caracteres de texto
- [[Catálogo - Sets#Cull Index (Cull i)|Cull Index (Cull i)]] — Elimina (cull) elementos indexados de una lista
- [[Catálogo - Sets#Cull Nth (CullN)|Cull Nth (CullN)]] — Elimina (cull) cada N-ésimo elemento de una lista
- [[Catálogo - Sets#Cull Pattern (Cull)|Cull Pattern (Cull)]] — Elimina (cull) elementos de una lista usando una máscara de bits que se repite
- [[Catálogo - Sets#Duplicate Data (Dup)|Duplicate Data (Dup)]] — Duplica datos una cantidad predefinida de veces
- [[Catálogo - Sets#Fibonacci (Fib)|Fibonacci (Fib)]] — Crea una sucesión de Fibonacci
- [[Catálogo - Sets#Jitter|Jitter]] — Mezcla al azar una lista de valores
- [[Catálogo - Sets#Random|Random]] — Genera una lista de números pseudoaleatorios
- [[Catálogo - Sets#Random Reduce (Reduce)|Random Reduce (Reduce)]] — Quita al azar N elementos de una lista
- [[Catálogo - Sets#Range|Range]] — Crea un rango de números
- [[Catálogo - Sets#Repeat Data (Repeat)|Repeat Data (Repeat)]] — Repite un patrón hasta alcanzar cierto largo
- [[Catálogo - Sets#Sequence (Seq)|Sequence (Seq)]] — Genera una secuencia de números
- [[Catálogo - Sets#Series|Series]] — Crea una serie de números
- [[Catálogo - Sets#Stack Data (Stack)|Stack Data (Stack)]] — Duplica elementos individuales de una lista de datos

### Pufferfish › Domain (20)

- [[Catálogo - Pufferfish#Average Domain (AvrDom)|Average Domain (AvrDom)]] — Calcula el promedio aritmético de un conjunto de dominios
- [[Catálogo - Pufferfish#Average Domain² (AvrDom²)|Average Domain² (AvrDom²)]] — Calcula el promedio aritmético de un conjunto de dominios²
- [[Catálogo - Pufferfish#Mirror Combine Domains (MirComDoms)|Mirror Combine Domains (MirComDoms)]] — Refleja un conjunto de dominios desde su final o su inicio y lo combina con el conjunto original
- [[Catálogo - Pufferfish#Mirror Combine Domains² (MirComDoms²)|Mirror Combine Domains² (MirComDoms²)]] — Refleja un conjunto de dominios² desde su final o su inicio y lo combina con el conjunto original
- [[Catálogo - Pufferfish#Mirror Cut Domains (MirCutDoms)|Mirror Cut Domains (MirCutDoms)]] — Corta un conjunto de dominios en un índice, refleja el lado conservado del corte respecto de ese índice y lo…
- [[Catálogo - Pufferfish#Mirror Cut Domains² (MirCutDoms²)|Mirror Cut Domains² (MirCutDoms²)]] — Corta un conjunto de dominios² en un índice, refleja el lado conservado del corte respecto de ese índice y lo…
- [[Catálogo - Pufferfish#Reparameterize Domains (ReparamDoms)|Reparameterize Domains (ReparamDoms)]] — Reparametriza un conjunto de dominios para que sus valores de inicio y final vayan de 0 a 1, o de forma…
- [[Catálogo - Pufferfish#Reparameterize Domains² (ReparamDoms²)|Reparameterize Domains² (ReparamDoms²)]] — Reparametriza un conjunto de dominios² para que los valores de inicio y final de sus dominios {u} y {v} vayan…
- [[Catálogo - Pufferfish#Slide Within Domain (SlideInDom)|Slide Within Domain (SlideInDom)]] — Se desliza entre el inicio y el final de un dominio para obtener un número dentro de él
- [[Catálogo - Pufferfish#Slide Within Domain² (SlideInDom²)|Slide Within Domain² (SlideInDom²)]] — Se desliza entre el inicio y el final de un dominio² para obtener un número de dominio {u} y {v} dentro de él
- [[Catálogo - Pufferfish#Tween Consecutive Domains (TwnConDoms)|Tween Consecutive Domains (TwnConDoms)]] — Interpola (tween) consecutivamente entre un conjunto de dominios
- [[Catálogo - Pufferfish#Tween Consecutive Domains² (TwnConDoms²)|Tween Consecutive Domains² (TwnConDoms²)]] — Interpola (tween) consecutivamente entre un conjunto de dominios²
- [[Catálogo - Pufferfish#Tween Through Domains (TwnThruDoms)|Tween Through Domains (TwnThruDoms)]] — Interpola (tween) a través de un conjunto de dominios
- [[Catálogo - Pufferfish#Tween Through Domains² (TwnThruDoms²)|Tween Through Domains² (TwnThruDoms²)]] — Interpola (tween) a través de un conjunto de dominios²
- [[Catálogo - Pufferfish#Tween Two Domains (Twn2Doms)|Tween Two Domains (Twn2Doms)]] — Interpola (tween) entre dos dominios
- [[Catálogo - Pufferfish#Tween Two Domains² (Twn2Doms²)|Tween Two Domains² (Twn2Doms²)]] — Interpola (tween) entre dos dominios²
- [[Catálogo - Pufferfish#Two Way Domain (2WayDom)|Two Way Domain (2WayDom)]] — Construye un dominio a partir de un número que pasa a ser los extremos negativo y positivo del dominio desde…
- [[Catálogo - Pufferfish#Two Way Domain² (2WayDom²)|Two Way Domain² (2WayDom²)]] — Construye un dominio² a partir de un número {u} y un número {v} que pasan a ser los extremos negativo y…
- [[Catálogo - Pufferfish#Weighted Average Domain (WavDom)|Weighted Average Domain (WavDom)]] — Calcula el promedio aritmético ponderado de un conjunto de dominios
- [[Catálogo - Pufferfish#Weighted Average Domain² (WavDom²)|Weighted Average Domain² (WavDom²)]] — Calcula el promedio aritmético ponderado de un conjunto de dominios²

### Pufferfish › Number (29)

- [[Catálogo - Pufferfish#Curve Graph Mapper (CrvGraphMap)|Curve Graph Mapper (CrvGraphMap)]] — Reasigna valores con un gráfico personalizado usando curvas de entrada
- [[Catálogo - Pufferfish#Deconstruct Number (DeNum)|Deconstruct Number (DeNum)]] — Descompone un número en su parte entera y su resto decimal
- [[Catálogo - Pufferfish#Default Angle Tolerance (DefAt)|Default Angle Tolerance (DefAt)]] — Entrega el valor por defecto de la tolerancia angular de RhinoMath (1 grado \| 0.017453 rad)
- [[Catálogo - Pufferfish#Document Angle Tolerance (DocAt)|Document Angle Tolerance (DocAt)]] — Entrega la tolerancia angular del documento de Rhino (Propiedades del documento > Unidades > Modelo >…
- [[Catálogo - Pufferfish#Document Distance Tolerance (DocDt)|Document Distance Tolerance (DocDt)]] — Entrega la tolerancia absoluta de distancia del documento de Rhino (Propiedades del documento > Unidades >…
- [[Catálogo - Pufferfish#Equality Within Tolerance (EqualsT)|Equality Within Tolerance (EqualsT)]] — Prueba la igualdad de dos números dentro de una tolerancia (\|A - B\| <= t)
- [[Catálogo - Pufferfish#Highest & Lowest Numbers (HiLoNums)|Highest & Lowest Numbers (HiLoNums)]] — Obtiene los valores mayor y menor de un conjunto de números
- [[Catálogo - Pufferfish#Invert Boolean (InvBool)|Invert Boolean (InvBool)]] — Invierte un booleano: True pasa a False y False pasa a True
- [[Catálogo - Pufferfish#Last Index Range (LastRange)|Last Index Range (LastRange)]] — Crea un rango de números entre 0 y el último índice de una lista (largo de la lista - 1)
- [[Catálogo - Pufferfish#Linearize Numbers (LinearNums)|Linearize Numbers (LinearNums)]] — Linealiza un conjunto de números: un conjunto que se repite como onda se reasigna a incrementos crecientes…
- [[Catálogo - Pufferfish#List Length Range (LengRange)|List Length Range (LengRange)]] — Crea un rango de números entre 0 y el largo de una lista
- [[Catálogo - Pufferfish#Mass Division (MDiv)|Mass Division (MDiv)]] — Realiza la división de todos los números de un conjunto
- [[Catálogo - Pufferfish#Mass Subtraction (MSub)|Mass Subtraction (MSub)]] — Realiza la resta de todos los números de un conjunto
- [[Catálogo - Pufferfish#Mirror Combine Numbers (MirComNums)|Mirror Combine Numbers (MirComNums)]] — Refleja un conjunto de números desde su final o su inicio y lo combina con el conjunto original
- [[Catálogo - Pufferfish#Mirror Cut Numbers (MirCutNums)|Mirror Cut Numbers (MirCutNums)]] — Corta un conjunto de números en un índice, refleja el lado conservado del corte respecto de ese índice y lo…
- [[Catálogo - Pufferfish#Odd & Even Numbers (OddEveNums)|Odd & Even Numbers (OddEveNums)]] — Separa un conjunto de números en impares y pares, con la opción de usar marcadores nulos en los conjuntos…
- [[Catálogo - Pufferfish#Partition Number (PartNum)|Partition Number (PartNum)]] — Reparte un número de la forma más pareja posible en una cantidad dada de partes
- [[Catálogo - Pufferfish#Percentage (Pcent)|Percentage (Pcent)]] — Calcula el porcentaje de un número
- [[Catálogo - Pufferfish#Reparameterize Numbers (ReparamNums)|Reparameterize Numbers (ReparamNums)]] — Reparametriza un conjunto de números para que su dominio vaya de 0 a 1, o de forma invertida de 1 a 0
- [[Catálogo - Pufferfish#Reparameterized Range (RepaRange)|Reparameterized Range (RepaRange)]] — Crea un rango de números entre 0 y 1
- [[Catálogo - Pufferfish#Round To Decimal Place (RoundD)|Round To Decimal Place (RoundD)]] — Redondea un número a una posición decimal o lo trunca en una posición decimal
- [[Catálogo - Pufferfish#Round To Factor (RoundF)|Round To Factor (RoundF)]] — Redondea un número a un múltiplo de un factor
- [[Catálogo - Pufferfish#Round To Nearest (RoundN)|Round To Nearest (RoundN)]] — Redondea los números de x a los números más cercanos de y, con la opción de reasignar el conjunto x a los…
- [[Catálogo - Pufferfish#Tween Consecutive Numbers (TwnConNums)|Tween Consecutive Numbers (TwnConNums)]] — Interpola (tween) consecutivamente entre un conjunto de números
- [[Catálogo - Pufferfish#Tween Through Numbers (TwnThruNums)|Tween Through Numbers (TwnThruNums)]] — Interpola (tween) a través de un conjunto de números
- [[Catálogo - Pufferfish#Tween Two Numbers (Twn2Nums)|Tween Two Numbers (Twn2Nums)]] — Interpola (tween) entre dos números
- [[Catálogo - Pufferfish#X Minus One (x-1)|X Minus One (x-1)]] — Resta uno a x
- [[Catálogo - Pufferfish#X Plus One (x+1)|X Plus One (x+1)]] — Suma uno a x
- [[Catálogo - Pufferfish#Zero Distance Tolerance (ZeroDt)|Zero Distance Tolerance (ZeroDt)]] — Entrega el valor de la tolerancia de distancia cero de RhinoMath (1.0e-12)

<!-- AUTO:fin -->
