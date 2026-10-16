---
title: "1 Matemáticas vectoriales"
source: "https://developer.rhino3d.com/guides/general/essential-mathematics/vector-mathematics/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-03
description: "Rhinoceros 3D: Esta guía trata las matemáticas vectoriales, incluida la representación de vectores, las operaciones vectoriales y las ecuaciones de líneas y planos."
tags:
  - "clippings"
---
Un vector representa un parámetro, como la velocidad o la fuerza, que tiene dirección y longitud. Los vectores en sistemas de coordenadas 3D se representan con un conjunto ordenado de tres números reales de la forma:

$$
\overset{\rightarrow}{\mathbf{v}} =< a_{1} , a_{2} , a_{3} >
$$
![](https://www.youtube.com/watch?v=NU34_aCoN3E)

## 1.1 Representación vectorial

En este documento, las letras minúsculas en negrita representarán los vectores. Los componentes de un vector también se representarán entre paréntesis angulares. Las letras mayúsculas representarán los puntos. Las coordenadas de los puntos siempre se representarán entre paréntesis.

Utilizando un sistema de coordenadas y cualquier conjunto de puntos de anclaje en ese sistema, podemos representar o visualizar estos vectores dibujándolos como el segmento de una línea. Dibujamos también la punta de una flecha para representar la dirección de los vectores.

Por ejemplo, si tenemos un vector que tiene una dirección paralela al eje x de un sistema de coordenadas dado y una magnitud de 5 unidades, podemos escribir el vector de la siguiente manera:

$$
\overset{\rightarrow}{\mathbf{v}} =< 5 , 0 , 0 >
$$

Para representar ese vector, necesitamos un punto de anclaje en el sistema de coordenadas. Por ejemplo, todas las flechas de la siguiente figura son representaciones iguales del mismo vector a pesar de que están ancladas en diferentes ubicaciones.

![](https://developer.rhino3d.com/images/math-image169.png)

Figura (1): Representación de vectores en el sistema de coordenadas 3D.

Note

Dado un vector 3D 
$$
\overset{\rightarrow}{v} =< a_{1} , a_{2} , a_{3} >
$$
, todos los componentes de los vectores 
$$
a_{1}
$$
, $a\_2
$$
, \$ a_{3}
$$
 son números reales. Además, todos los segmentos de línea desde un punto 
$$
A \left(\right. x , y , z \left.\right)
$$
 hasta otro punto 
$$
B \left(\right. x + a_{1} , y + a_{2} , z + a_{3} \left.\right)
$$
 son representaciones equivalentes del vector 
$$
\overset{\rightarrow}{v}
$$
.

Entonces, ¿cómo definimos los puntos finales de un segmento de línea que representa un vector dado? Definamos un punto de anclaje (A) de modo que:

$$
A = \left(\right. 1 , 2 , 3 \left.\right)
$$

Y un vector:

$$
\overset{\rightarrow}{\mathbf{v}} =< 5 , 6 , 7 >
$$

El punto extremo 
$$
\left(\right. B \left.\right)
$$
 del vector se calcula sumando los componentes correspondientes del punto de anclaje y el vector 
$$
\overset{\rightarrow}{v}
$$
:

$$
B = A + \overset{\rightarrow}{\mathbf{v}}
$$
  
$$
B = \left(\right. 1 + 5 , 2 + 6 , 3 + 7 \left.\right)
$$
  
$$
B = \left(\right. 6 , 8 , 10 \left.\right)
$$

![](https://developer.rhino3d.com/images/math-image172.png)

Figura (2): La relación entre un vector, el punto de anclaje del vector y el punto que coincide con la ubicación del extremo del vector.

![](https://www.youtube.com/watch?v=ELQ8NgENhJY)
![](https://www.youtube.com/watch?v=INtNgczxyWg)

### Vector de posición

Existe una representación especial de vectores que utiliza el 
$$
\text{punto de origen} \left(\right. 0 , 0 , 0 \left.\right)
$$
 como punto de anclaje del vector. El vector de posición 
$$
\overset{\rightarrow}{\mathbf{v}} =< a_{1} , a_{2} , a_{3} >
$$
 se representa con un segmento de línea entre dos puntos, el origen y B, de modo que:

$$
\text{Punto de origen} = \left(\right. 0 , 0 , 0 \left.\right)
$$
  
$$
B = \left(\right. a_{1} , a_{2} , a_{3} \left.\right)
$$

![](https://developer.rhino3d.com/images/math-image171.png)

Figura (3): Vector de posición. Las coordenadas del punto extremo son iguales a los componentes del vector correspondiente.

Note

Un *vector de posición* de un vector dado 
$$
\overset{\rightarrow}{v} =< a_{1} , a_{2} , a_{3} >
$$
 es una representación especial del segmento de línea desde el punto de origen 
$$
\left(\right. 0 , 0 , 0 \left.\right)
$$
 al punto 
$$
\left(\right. a_{1} , a_{2} , a_{3} \left.\right)
$$
.

![](https://www.youtube.com/watch?v=8BNyMC4EBcw)
![](https://www.youtube.com/watch?v=Ft2edI4g1qY)

### Vectores y puntos

Es importante no confundir vectores con puntos. Son conceptos muy diferentes. Los vectores, como mencionamos, representan una cantidad que tiene dirección y longitud, mientras que los puntos indican una ubicación. Por ejemplo, la dirección norte es un vector, mientras que el polo norte es una ubicación (punto). Si tenemos un vector y un punto que tienen los mismos componentes, como por ejemplo:

$$
\overset{\rightarrow}{\mathbf{v}} =< 3 , 1 , 0 >
$$
  
$$
P = \left(\right. 3 , 1 , 0 \left.\right)
$$

Podemos dibujar el vector y el punto de la siguiente manera:

![](https://developer.rhino3d.com/images/math-image174.png)

Figura (4): Un vector define una dirección y una longitud. Un punto define una ubicación.

![](https://www.youtube.com/watch?v=RRrTz_QO_rA)

### Longitud vectorial

Como se ha mencionado anteriormente, los vectores tienen longitud. Usaremos 
$$
\left|\right. a \left|\right.
$$
 para representar la longitud de un vector dado 
$$
a
$$
. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 4 , 3 , 0 >
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. = \sqrt{4^{2} + 3^{2} + 0^{2}}
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. = 5
$$

En general, la longitud de un vector 
$$
\overset{\rightarrow}{\mathbf{a}} < a_{1} , a_{2} , a_{3} >
$$
 se calcula de la siguiente manera:

$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. = \sqrt{\left(\right. a_{1} \left.\right)^{2} + \left(\right. a_{2} \left.\right)^{2} + \left(\right. a_{3} \left.\right)^{2}}
$$
![](https://developer.rhino3d.com/images/math-image173.png)

Figura (5): Longitud del vector.

### Vector unitario

Un vector unitario es un vector con una longitud igual a una unidad. Los vectores unitarios se utilizan comúnmente para comparar las direcciones de los vectores.

Note

Un vector unitario es un vector cuya longitud es igual a una unidad.

Para calcular un vector unitario, necesitamos encontrar la longitud del vector dado y luego dividir los componentes del vector por la longitud. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 4 , 3 , 0 >
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. = \sqrt{4^{2} + 3^{2} + 0^{2}}
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. = 5 \text{unidades de longitud}
$$

Si 
$$
\overset{\rightarrow}{\mathbf{b}} = \text{vector unitario}
$$
 de 
$$
a
$$
, entonces:  
$$
\overset{\rightarrow}{\mathbf{b}} =< 4 / 5 , 3 / 5 , 0 / 5 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 0.8 , 0.6 , 0 >
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{b}} \left|\right. = \sqrt{0.8^{2} + 0.6^{2} + 0^{2}}
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{b}} \left|\right. = \sqrt{0.64 + 0.36 + 0}
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{b}} \left|\right. = \sqrt{\left(\right. 1 \left.\right)} = 1 \text{unidad de longitud}
$$

En general:

$$
\overset{\rightarrow}{\mathbf{a}} =< a_{1} , a_{2} , a_{3} >
$$

El vector unitario de 
$$
\overset{\rightarrow}{\mathbf{a}} =< a_{1} / \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. , a_{2} / \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. , a_{3} / \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. >
$$

![](https://developer.rhino3d.com/images/math-image176.png)

Figura (6): El vector unitario es igual a una unidad de longitud del vector.

![](https://www.youtube.com/watch?v=yVSigpl3EUo)

## 1.2 Operaciones vectoriales

![](https://www.youtube.com/watch?v=uInxocphhxI)

### Operación escalar de vectores

La operación escalar de vectores implica multiplicar un vector por un número. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 4 , 3 , 0 >
$$
  
$$2\* \\mathbf{\\vec a} = <2 *4, 2* 3, 2\*0> 2\*\\mathbf{\\vec a} = <8, 6, 0>$$

![](https://developer.rhino3d.com/images/math-image175.png)

Figura (7): Operación escalar de vectores

En general, dado el vector 
$$
\overset{\rightarrow}{\mathbf{a}} =< a_{1} , a_{2} , a_{3} >
$$
 y un número real 
$$
t
$$

$$
t * \overset{\rightarrow}{\mathbf{a}} =< t * a_{1} , t * a_{2} , t * a_{3} >
$$
![](https://www.youtube.com/watch?v=S59M8BnDYAQ)

### Suma de vectores

La suma de vectores toma dos vectores y se obtiene un tercer vector. Sumamos vectores añadiendo sus componentes.

Note

Los vectores se suman añadiendo sus componentes.

Por ejemplo, si tenemos dos vectores:

$$
\overset{\rightarrow}{\mathbf{a}} =< 1 , 2 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 4 , 1 , 3 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} + \overset{\rightarrow}{\mathbf{b}} =< 1 + 4 , 2 + 1 , 0 + 3 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} + \overset{\rightarrow}{\mathbf{b}} =< 5 , 3 , 3 >
$$

![](https://developer.rhino3d.com/images/math-image179.png)

Figura (8): Adición de vectores.

En general, la suma de vectores de los dos vectores a y b se calcula de la siguiente manera:

$$
\overset{\rightarrow}{\mathbf{a}} =< a_{1} , a_{2} , a_{3} >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< b_{1} , b_{2} , b_{3} >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} + \overset{\rightarrow}{\mathbf{b}} =< a_{1} + b_{1} , a_{2} + b_{2} , a_{3} + b_{3} >
$$

La suma de vectores es útil para hallar la dirección media de dos o más vectores. En estos casos, solemos usar vectores de la misma longitud. Este es un ejemplo que muestra la diferencia entre emplear vectores de iguales o de diferentes longitudes en la resultante de la suma de dichos vectores:

![](https://developer.rhino3d.com/images/math-image177.png)

Figura (9): Suma de varios vectores de longitud (izquierda). Suma de vectores de la misma longitud (derecha) para obtener la dirección media.

Es probable que los vectores de entrada no tengan la misma longitud. Para encontrar la dirección media, tiene que utilizar el vector unitario de los vectores de entrada. Como se ha mencionado anteriormente, el vector unitario es un vector de que tiene una longitud igual a 1.

![](https://www.youtube.com/watch?v=VTVk3t3WeAY)

### Resta de vectores

La resta de vectores toma dos vectores y se obtiene un tercer vector. Restamos dos vectores restando los componentes correspondientes. Por ejemplo, si tenemos dos vectores 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
 and 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 y restamos 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 de 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
, entonces:

$$
\overset{\rightarrow}{\mathbf{a}} =< 1 , 2 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 4 , 1 , 4 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} - \overset{\rightarrow}{\mathbf{b}} =< 1 - 4 , 2 - 1 , 0 - 4 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} - \overset{\rightarrow}{\mathbf{b}} =< - 3 , 1 , - 4 >= \overset{\rightarrow}{\mathbf{b}} \mathbf{a}
$$

Si restamos 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 de 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
, obtenemos un resultado diferente:

$$
\overset{\rightarrow}{\mathbf{b}} - \overset{\rightarrow}{\mathbf{a}} =< 4 - 1 , 1 - 2 , 4 - 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} - \overset{\rightarrow}{\mathbf{a}} =< 3 , - 1 , 4 >= \overset{\rightarrow}{\mathbf{a}} \mathbf{b}
$$

Observe que el vector 
$$
\overset{\rightarrow}{\mathbf{b}} - \overset{\rightarrow}{\mathbf{a}}
$$
 tiene la misma longitud que el vector 
$$
\$ \overset{\rightarrow}{\mathbf{a}} - \overset{\rightarrow}{\mathbf{b}}
$$
, pero va en sentido contrario.

![](https://developer.rhino3d.com/images/math-image178.png)

Figura (10): Resta de vectores.

En general, si tenemos dos vectores, 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
 y 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
, entonces 
$$
\$ \overset{\rightarrow}{\mathbf{a}} - \overset{\rightarrow}{\mathbf{b}}
$$
 es un vector que se calcula de la siguiente manera:

$$
\overset{\rightarrow}{\mathbf{a}} =< a_{1} , a_{2} , a_{3} >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< b_{1} , b_{2} , b_{3} >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} - \overset{\rightarrow}{\mathbf{b}} =< a_{1} - b_{1} , a_{2} - b_{2} , a_{3} - b_{3} >= \overset{\rightarrow}{\mathbf{b}} \mathbf{a}
$$

La resta de vectores se suele usar para hallar vectores entre puntos. Por lo tanto, si necesitamos hallar un vector que vaya desde el punto extremo del vector de posición 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 al punto extremo del vector de posición 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
, usamos la resta de vectores 
$$
\left(\right. \overset{\rightarrow}{\mathbf{a}} - \overset{\rightarrow}{\mathbf{b}} \left.\right)
$$
 como se muestra en la Figura (11).

![](https://developer.rhino3d.com/images/math-image180.png)

Figura (11): Utilice la resta de vectores para hallar un vector entre dos puntos.

![](https://www.youtube.com/watch?v=RQK8pCIWKNY)

### Propiedades de los vectores

Los vectores tienen ocho propiedades fundamentales. Si a, b y c son vectores, y s y t son números, entonces:

$$
\overset{\rightarrow}{\mathbf{a}} + \overset{\rightarrow}{\mathbf{b}} = \overset{\rightarrow}{\mathbf{b}} + \overset{\rightarrow}{\mathbf{a}}
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} + 0 = a
$$
  
$$
s * \left(\right. \overset{\rightarrow}{\mathbf{a}} + \overset{\rightarrow}{\mathbf{b}} \left.\right) = s * a + s * \overset{\rightarrow}{\mathbf{b}}
$$
  
$$
s * t * \left(\right. \overset{\rightarrow}{\mathbf{a}} \left.\right) = s * \left(\right. t * \overset{\rightarrow}{\mathbf{a}} \left.\right)
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} + \left(\right. \overset{\rightarrow}{\mathbf{b}} + \overset{\rightarrow}{\mathbf{c}} \left.\right) = \left(\right. \overset{\rightarrow}{\mathbf{a}} + \overset{\rightarrow}{\mathbf{b}} \left.\right) + \overset{\rightarrow}{\mathbf{c}}
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} + \left(\right. - \overset{\rightarrow}{\mathbf{a}} \left.\right) = 0
$$
  
$$
\left(\right. s + t \left.\right) * \overset{\rightarrow}{\mathbf{a}} = s * \overset{\rightarrow}{\mathbf{a}} + t * \overset{\rightarrow}{\mathbf{a}}
$$
  
$$
1 * \overset{\rightarrow}{\mathbf{a}} = \overset{\rightarrow}{\mathbf{a}}
$$

### Producto escalar de vectores

El producto escalar toma dos vectores y se obtiene un número. Por ejemplo, si tenemos los dos vectores a y b de modo que:

$$
\overset{\rightarrow}{\mathbf{a}} =< 1 , 2 , 3 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 5 , 6 , 7 >
$$

Entonces el producto escalar es la suma de multiplicar los componentes de la siguiente manera:

$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} = 1 * 5 + 2 * 6 + 3 * 7
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} = 38
$$

En general, dados los dos vectores a y b:

$$
\overset{\rightarrow}{\mathbf{a}} =< a_{1} , a_{2} , a_{3} >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< b_{1} , b_{2} , b_{3} >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} = a_{1} * b_{1} + a_{2} * b_{2} + a_{3} * b_{3}
$$

Siempre obtenemos un número positivo del producto escalar entre dos vectores cuando van en la misma dirección general. Un producto escalar negativo entre dos vectores significa que los dos vectores van en la dirección general opuesta.

![](https://developer.rhino3d.com/images/math-image181.png)

Figura (12): Cuando los dos vectores van en la misma dirección (izquierda), el resultado es un producto escalar positivo. Cuando los dos vectores van en la dirección opuesta (derecha), el resultado es un producto escalar negativo.

Al calcular el producto escalar de dos vectores unitarios, el resultado siempre está entre 1 y +1. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 1 , 0 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 0 , 6 , 0 , 8 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} = \left(\right. 1 * 0.6 , 0 * 0.8 , 0 * 0 \left.\right) = 0.6
$$

Además, el producto escalar de un vector consigo mismo es igual a la longitud de ese vector elevado a dos. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 0 , 3 , 4 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{a}} = 0 * 0 + 3 * 3 + 4 * 4
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{a}} = 25
$$

Cálculo de la longitud cuadrada del vector 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
:

$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. = \sqrt{4^{2} + 3^{2} + 0^{2}}
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. = 5
$$
  
$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. 2 = 25
$$

### Producto escalar de vectores, longitudes y ángulos

Existe una relación entre el producto escalar de dos vectores y el ángulo entre ellos.

Note

El producto escalar de dos vectores unitarios distintos a cero es igual al coseno del ángulo entre ellos.

En general:

$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} = \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. * \left|\right. \overset{\rightarrow}{\mathbf{b}} \left|\right. * c o s \left(\right. ө \left.\right)
$$
, o bien  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} / \left(\right. \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. * \left|\right. \overset{\rightarrow}{\mathbf{b}} \left|\right. \left.\right) = c o s \left(\right. ө \left.\right)
$$

Donde:

$$
ө
$$
 es el ángulo incluido entre los vectores.

Si los vectores a y b son vectores unitarios, podemos decir que:

$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} = c o s \left(\right. ө \left.\right)
$$

Y dado que el coseno de un ángulo de 90 grados es igual a 0, podemos decir que:

Note

Los vectores 
$$
\overset{\rightarrow}{a}
$$
 y 
$$
\overset{\rightarrow}{b}
$$
 son ortogonales si, y solo si, 
$$
\overset{\rightarrow}{a} \cdot \overset{\rightarrow}{b} = 0
$$
.

Por ejemplo, si calculamos el producto escalar de los dos vectores ortogonales, el eje x y el eje y universales, el resultado será igual a cero.

$$
\overset{\rightarrow}{\mathbf{x}} =< 1 , 0 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{y}} =< 0 , 1 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{x}} \cdot \overset{\rightarrow}{\mathbf{y}} = \left(\right. 1 * 0 \left.\right) + \left(\right. 0 * 1 \left.\right) + \left(\right. 0 * 0 \left.\right)
$$
  
$$
\overset{\rightarrow}{\mathbf{x}} \cdot \overset{\rightarrow}{\mathbf{y}} = 0
$$

También existe una relación entre el producto escalar y la longitud de proyección de un vector sobre otro. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 5 , 2 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 9 , 0 , 0 >
$$
  
$$
u n i d a d \left(\right. \overset{\rightarrow}{\mathbf{b}} \left.\right) =< 1 , 0 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot u n i d a d \left(\right. \overset{\rightarrow}{\mathbf{b}} \left.\right) = \left(\right. 5 * 1 \left.\right) + \left(\right. 2 * 0 \left.\right) + \left(\right. 0 * 0 \left.\right)
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} - u n i d a d \left(\right. \overset{\rightarrow}{\mathbf{b}} \left.\right) = 2 \left(\right. \text{que es igual a la longitud de proyecci}\acute{o}\text{n de mathbf}{\backslash\text{vec a}}\text{ sobre mathbf}{\backslash\text{vec b}} \left.\right)
$$

![](https://developer.rhino3d.com/images/math-image182.png)

Figura (13): El producto escalar es igual a la longitud de proyección de un vector sobre un vector unitario distinto a cero.

En general, dado un vector a y un vector distinto a cero b, podemos calcular la longitud de proyección pL del vector a sobre el vector b utilizando el producto escalar.

$$
p L = \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. * c o s \left(\right. ө \left.\right)
$$
  
$$
p L = \overset{\rightarrow}{\mathbf{a}} \cdot u n i d a d \left(\right. \overset{\rightarrow}{\mathbf{b}} \left.\right)
$$

![](https://www.youtube.com/watch?v=ZsM2RQbVDf4)

### Propiedades del producto escalar

Si 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
, 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 y 
$$
\overset{\rightarrow}{\mathbf{c}}
$$
 son vectores y s es un número, entonces:

$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{a}} = \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right.^{2}
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \left(\right. \overset{\rightarrow}{\mathbf{b}} + \overset{\rightarrow}{\mathbf{c}} \left.\right) = \overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} + \overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{c}}
$$
  
$$
0 \cdot \overset{\rightarrow}{\mathbf{a}} = 0
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} = \overset{\rightarrow}{\mathbf{b}} \cdot \overset{\rightarrow}{\mathbf{a}}
$$
  
$$
\left(\right. s * \overset{\rightarrow}{\mathbf{a}} \left.\right) \cdot \overset{\rightarrow}{\mathbf{b}} = s * \left(\right. \overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} \left.\right) = \overset{\rightarrow}{\mathbf{a}} \cdot \left(\right. s * \overset{\rightarrow}{\mathbf{b}} \left.\right)
$$

### Producto vectorial

El producto vectorial toma dos vectores y se obtiene un tercer vector que es ortogonal a ambos.

![](https://developer.rhino3d.com/images/math-image183.png)

Figura (14): Cálculo del producto vectorial de dos vectores.

Por ejemplo, si tiene dos vectores que se encuentran en el plano xy universal, entonces su producto vectorial es un vector perpendicular al plano xy que va en la dirección del eje z universal positivo o negativo. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 3 , 1 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 1 , 2 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} =< \left(\right. 1 * 0 – 0 * 2 \left.\right) , \left(\right. 0 * 1 - 3 * 0 \left.\right) , \left(\right. 3 * 2 - 1 * 1 \left.\right) >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} =< 0 , 0 , 5 >
$$

Note

El vector 
$$
\overset{\rightarrow}{a} \times \overset{\rightarrow}{b}
$$
 es ortogonal tanto a 
$$
\overset{\rightarrow}{a}
$$
 como a 
$$
\overset{\rightarrow}{b}
$$
.

Probablemente nunca tenga que calcular manualmente un producto vectorial de dos vectores, pero si tiene curiosidad sobre cómo se hace, continúe leyendo; si no, puede omitir esta sección. El producto vectorial 
$$
a \times b
$$
 se resuelve utilizando determinantes. Esta ilustración simple muestra cómo calcular un determinante utilizando los vectores base estándar:

$$
i =< 1 , 0 , 0 >
$$
  
$$
j =< 0 , 1 , 0 >
$$
  
$$
k =< 0 , 0 , 1 >
$$

![](https://developer.rhino3d.com/images/math-image184.png)

El producto vectorial de los dos vectores 
$$
\overset{\rightarrow}{\mathbf{a}} =< a 1 , a 2 , a 3 >
$$
 y 
$$
\overset{\rightarrow}{\mathbf{b}} =< b 1 , b 2 , b 3 >
$$
 se calcula de la siguiente manera utilizando el diagrama anterior:

$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} = i \left(\right. a_{2} * b_{3} \left.\right) + j \left(\right. a_{3} * b_{1} \left.\right) + k \left(\right. a_{1} * b_{2} \left.\right) - k \left(\right. a_{2} * b_{1} \left.\right) - i \left(\right. a_{3} * b_{2} \left.\right) - j \left(\right. a_{1} * b_{3} \left.\right)
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} = i \left(\right. a_{2} * b_{3} - a_{3} * b_{2} \left.\right) + j \left(\right. a_{3} * b_{1} - a_{1} * b_{3} \left.\right) + k \left(\right. a_{1} * b_{2} - a_{2} * b_{1} \left.\right)
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} =< a_{2} * b_{3} – a_{3} * b_{2} , a_{3} * b_{1} - a_{1} * b_{3} , a_{1} * b_{2} - a_{2} * b_{1} >
$$

![](https://www.youtube.com/watch?v=I5WkhSo4p6o)

### Producto vectorial y ángulo entre vectores

Existe una relación entre el ángulo entre dos vectores y la longitud de su producto vectorial. Cuanto menor sea el ángulo (seno más pequeño), más corto será el producto vectorial. El orden de los operandos es importante en los productos vectoriales. Por ejemplo:

$$
\overset{\rightarrow}{\mathbf{a}} =< 1 , 0 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< 0 , 1 , 0 >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} =< 0 , 0 , 1 >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} \times \overset{\rightarrow}{\mathbf{a}} =< 0 , 0 , - 1 >
$$

![](https://developer.rhino3d.com/images/math-image185.png)

Figura (15): Existe una relación entre el ángulo entre dos vectores y la longitud de su producto vectorial.

En el sistema diestro de Rhino, la dirección de 
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}}
$$
 viene dada por la regla de la mano derecha (donde 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
 = dedo índice, 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 = dedo corazón y 
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}}
$$
 = pulgar).

![](https://developer.rhino3d.com/images/math-image186.png)

En general, para cualquier par de vectores 3D 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
 y 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
:

$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} \left|\right. = \left|\right. \overset{\rightarrow}{\mathbf{a}} \left|\right. \left|\right. \overset{\rightarrow}{\mathbf{b}} \left|\right. s i n \left(\right. ө \left.\right)
$$

Donde:

$$
ө
$$
 es el ángulo incluido entre los vectores de posición de 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
 y 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 $

Si a y b son vectores unitarios, entonces podemos decir que la longitud de su producto vectorial es igual al seno del ángulo entre ellos. En otras palabras:

$$
\left|\right. \overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} \left|\right. = s i n \left(\right. ө \left.\right)
$$

El producto vectorial entre dos vectores nos ayuda a determinar si dos vectores son paralelos. Esto se debe a que el resultado es siempre un vector cero.

Note

Los vectores 
$$
\overset{\rightarrow}{a}
$$
 y 
$$
\overset{\rightarrow}{b}
$$
 son paralelos si, y solo si, 
$$
a \times b = 0
$$
.

### Propiedades del producto vectorial

Si 
$$
\overset{\rightarrow}{\mathbf{a}}
$$
, 
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 y 
$$
\overset{\rightarrow}{\mathbf{c}}
$$
 son vectores, y 
$$
s
$$
 es un número, entonces:  
$$
\overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} = - \overset{\rightarrow}{\mathbf{b}} \times \overset{\rightarrow}{\mathbf{a}}
$$
  
$$
\left(\right. s * \overset{\rightarrow}{\mathbf{a}} \left.\right) \times \overset{\rightarrow}{\mathbf{b}} = s * \left(\right. \overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} \left.\right) = \overset{\rightarrow}{\mathbf{a}} \times \left(\right. s * \overset{\rightarrow}{\mathbf{b}} \left.\right)
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \times \left(\right. \overset{\rightarrow}{\mathbf{b}} + \overset{\rightarrow}{\mathbf{c}} \left.\right) = \overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} + \overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{c}}
$$
  
$$
\left(\right. \overset{\rightarrow}{\mathbf{a}} + \overset{\rightarrow}{\mathbf{b}} \left.\right) \times \overset{\rightarrow}{\mathbf{c}} = \overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{c}} + \overset{\rightarrow}{\mathbf{b}} \times \overset{\rightarrow}{\mathbf{c}}
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \cdot \left(\right. \overset{\rightarrow}{\mathbf{b}} \times \overset{\rightarrow}{\mathbf{c}} \left.\right) = \left(\right. \overset{\rightarrow}{\mathbf{a}} \times \overset{\rightarrow}{\mathbf{b}} \left.\right) \cdot \overset{\rightarrow}{\mathbf{c}}
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} \times \left(\right. \overset{\rightarrow}{\mathbf{b}} \times \overset{\rightarrow}{\mathbf{c}} \left.\right) = \left(\right. \overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{c}} \left.\right) * \overset{\rightarrow}{\mathbf{b}} – \left(\right. \overset{\rightarrow}{\mathbf{a}} \cdot \overset{\rightarrow}{\mathbf{b}} \left.\right) * \overset{\rightarrow}{\mathbf{c}}
$$

## 1.3 Ecuación vectorial de una línea

La ecuación vectorial de una línea se utiliza en aplicaciones de modelado 3D y diseño gráfico por ordenador.

![](https://developer.rhino3d.com/images/math-image187.png)

Figura (16): Ecuación vectorial de una línea.

Por ejemplo, si sabemos la dirección de una línea y un punto en esa línea, podemos hallar cualquier otro punto en la línea utilizando vectores, como se muestra a continuación:

$$
\overset{―}{L} = l i n e
$$
  
$$
\overset{\rightarrow}{\mathbf{v}} =< a , b , c >
$$
 vector unitario de dirección de la línea  
$$
Q = \left(\right. x_{0} , y_{0} , z_{0} \left.\right)
$$
 punto de posición de la línea  
$$
P = \left(\right. x , y , z \left.\right)
$$
 cualquier punto en la línea

Sabemos que:

$$
\overset{\rightarrow}{\mathbf{a}} = t * \overset{\rightarrow}{\mathbf{v}}
$$
 (2)  
$$
\overset{\rightarrow}{\mathbf{p}} = \overset{\rightarrow}{\mathbf{q}} + \overset{\rightarrow}{\mathbf{a}}
$$
 (1)

A partir de 1 y 2:

$$
\overset{\rightarrow}{\mathbf{p}} = \overset{\rightarrow}{\mathbf{q}} + t * \overset{\rightarrow}{\mathbf{v}}
$$
 (3)

Sin embargo, también podemos expresar (3) de la siguiente manera:

$$
< x , y , z >=< x_{0} , y_{0} , z_{0} > + < t * a , t * b , t * c >
$$
  
$$
< x , y , z >=< x_{0} + t * a , y_{0} + t * b , z_{0} + t * c >
$$

Por tanto:

$$
x = x_{0} + t * a
$$
  
$$
y = y_{0} + t * b
$$
  
$$
z = z_{0} + t * c
$$

Que es lo mismo que:

$$
P = Q + t * \overset{\rightarrow}{\mathbf{v}}
$$

Note

Dado un punto 
$$
Q
$$
 y una dirección 
$$
\overset{\rightarrow}{v}
$$
 en una línea, cualquier punto 
$$
P
$$
 de esa línea se puede calcular utilizando la ecuación vectorial de una línea 
$$
P = Q + t * \overset{\rightarrow}{v}
$$
 donde 
$$
t
$$
 es un número.

Otro ejemplo común es hallar el punto medio entre dos puntos. A continuación, se muestra cómo encontrar el punto medio utilizando la ecuación vectorial de una línea:

$$
\overset{\rightarrow}{\mathbf{q}}
$$
 es el vector de posición del punto $Q\\mathbf{\\vec p} 
$$
e s e l v e c t o r d e p o s i c i \acute{o} n d e l p u n t o
$$
 P\\mathbf{\\vec a} 
$$
e s e l v e c t o r q u e v a d e s d e
$$
 Q \\rightarrow P$$

De la resta de vectores se obtiene que:

$$
\overset{\rightarrow}{\mathbf{a}} = \overset{\rightarrow}{\mathbf{p}} - \overset{\rightarrow}{\mathbf{q}}
$$

De la ecuación lineal se obtiene que:

$$
M = Q + t * \overset{\rightarrow}{\mathbf{a}}
$$

Y como necesitamos hallar el punto medio, entonces:

$$
t = 0.5
$$

Por tanto, podemos decir que:

$$
M = Q + 0.5 * \overset{\rightarrow}{\mathbf{a}}
$$
![](https://developer.rhino3d.com/images/math-image159.png)

Figura (17): Búsqueda del punto medio entre dos puntos de entrada.

En general, puede hallar cualquier punto entre 
$$
Q
$$
 y 
$$
P
$$
 cambiando el valor 
$$
t
$$
 entre 0 y 1 utilizando la ecuación general:

$$
M = Q + t * \left(\right. P - Q \left.\right)
$$

Note

Dados dos puntos 
$$
Q
$$
 y 
$$
P
$$
, cualquier punto 
$$
M
$$
 entre los dos puntos se calcula utilizando la ecuación 
$$
M = Q + t * \left(\right. P - Q \left.\right)
$$
 donde t es un número entre 0 y 1.

## 1.4 Ecuación vectorial de un plano

Una forma de definir un plano es cuando hay un punto y un vector que es perpendicular al plano. Ese vector generalmente se conoce como normal al plano. La normal apunta en la dirección por encima del plano.

Un ejemplo de cómo calcular la normal de un plano es cuando hay tres puntos no lineales en el plano.

En la Figura (16), dados:

$$
A
$$
 = el primer punto del plano  
$$
B
$$
 = el segundo punto del plano  
$$
C
$$
 = el tercer punto del plano

Y:

$$
\overset{\rightarrow}{\mathbf{a}}
$$
 = un vector de posición del punto 
$$
A
$$
  
$$
\overset{\rightarrow}{\mathbf{b}}
$$
 = un vector de posición del punto 
$$
B
$$
  
$$
\overset{\rightarrow}{\mathbf{c}}
$$
 = un vector de posición del punto 
$$
C
$$

Podemos encontrar el vector de la normal 
$$
\overset{\rightarrow}{\mathbf{n}}
$$
 de la siguiente manera:

$$
\overset{\rightarrow}{\mathbf{n}} = \left(\right. \overset{\rightarrow}{\mathbf{b}} - \overset{\rightarrow}{\mathbf{a}} \left.\right) \times \left(\right. \overset{\rightarrow}{\mathbf{c}} - \overset{\rightarrow}{\mathbf{a}} \left.\right)
$$
![](https://developer.rhino3d.com/images/math-image160.png)

Figura (18): Vectores y planos

También podemos derivar la ecuación escalar del plano utilizando el producto escalar del vector:

$$
\overset{\rightarrow}{\mathbf{n}} \cdot \left(\right. \overset{\rightarrow}{\mathbf{b}} - \overset{\rightarrow}{\mathbf{a}} \left.\right) = 0
$$

Si:

$$
\overset{\rightarrow}{\mathbf{n}} =< a , b , c >
$$
  
$$
\overset{\rightarrow}{\mathbf{b}} =< x , y , z >
$$
  
$$
\overset{\rightarrow}{\mathbf{a}} =< x_{0} , y_{0} , z_{0} >
$$

Entonces podemos ampliar lo anterior:

$$
< a , b , c > \cdot < x - x_{0} , y - y_{0} , z - z_{0} >= 0
$$

Resolver el producto escalar da la ecuación escalar general de un plano:

$$
a * \left(\right. x - x_{0} \left.\right) + b * \left(\right. y - y_{0} \left.\right) + c * \left(\right. z - z_{0} \left.\right) = 0
$$

## 1.5 Tutoriales

Todos los conceptos tratados en este capítulo tienen una aplicación directa para resolver problemas geométricos comunes que se encuentran durante el modelado. Los siguientes tutoriales paso a paso emplean los conceptos aprendidos en este capítulo utilizando Rhinoceros y Grasshopper (GH).

### 1.5.1 Dirección de cara

Dados un punto y una superficie, ¿cómo podemos determinar si el punto está orientado hacia la parte frontal o posterior de esa superficie?

**Entrada:**

1. Una superficie
2. Un punto
![](https://developer.rhino3d.com/images/math-image161.png)

**Parámetros:**

La dirección de la cara está definida por la dirección normal de la superficie. Necesitaremos la siguiente información:

- La dirección normal de la superficie en una ubicación de superficie más cercana al punto de entrada.
- Una dirección de vector desde el punto más cercano al punto de entrada.

Compare las dos direcciones anteriores. Si van en la misma dirección, el punto está orientado hacia la parte frontal; de lo contrario, está orientado hacia la parte posterior.

**Solución:**

1\. Encuentre la ubicación del punto más cercano en la superficie en relación con el punto de entrada utilizando el componente Pull. Esto nos dará la ubicación uv del punto más cercano, que luego podemos usar para evaluar la superficie y hallar su dirección normal.

![](https://developer.rhino3d.com/images/math-image162.png)

2\. Ahora podemos usar el punto más cercano para dibujar un vector orientado hacia el punto de entrada. También podemos dibujar:

![](https://developer.rhino3d.com/images/math-image163.png)

3\. Podemos comparar los dos vectores utilizando el producto escalar. Si el resultado es positivo, el punto está delante de la superficie. Si el resultado es negativo, el punto está detrás de la superficie.

![](https://developer.rhino3d.com/images/math-image164.png)

Los pasos anteriores también se pueden resolver utilizando otros lenguajes de scripting. Uso del componente VB de Grasshopper:

![](https://developer.rhino3d.com/images/math-image165.png)
```vb
Private Sub RunScript(ByVal pt As Point3d, ByVal srf As Surface, ByRef A As Object)

 

  'Declare variables

  Dim u, v As Double

  Dim closest_pt As Point3d

 

  'get closest point u, v

  srf.ClosestPoint(pt, u, v)

 

  'get closest point

  closest_pt = srf.PointAt(u, v)

 

  'calculate direction from closest point to test point

  Dim dir As New Vector3d(pt - closest_pt)

 

  'calculate surface normal

  Dim normal = srf.NormalAt(u, v)

 

  'compare the two directions using the dot product

  A = dir * normal

End Sub
```

Uso del componente Python de Grasshopper con RhinoScriptSyntax:

![](https://developer.rhino3d.com/images/math-image14.png)
```python
import rhinoscriptsyntax as rs #import RhinoScript library

 

#find the closest point

u, v = rs.SurfaceClosestPoint(srf, pt)

 

#get closest point

closest_pt = rs.EvaluateSurface(srf, u, v)

 

#calculate direction from closest point to test point

dir = rs.PointCoordinates(pt) - closest_pt

 

#calculate surface normal

normal = rs.SurfaceNormal(srf, [u, v])

 

#compare the two directions using the dot product

A = dir * normal
```

Uso del componente Python de Grasshopper solo con RhinoCommon:

![](https://developer.rhino3d.com/images/math-image13.png)
```python
#find the closest point

found, u, v = srf.ClosestPoint(pt)

 

if found:

 

    #get closest point

    closest_pt = srf.PointAt(u, v)

 

    #calculate direction from closest point to test point

    dir = pt - closest_pt

 

    #calculate surface normal

    normal = srf.NormalAt(u, v)

 

    #compare the two directions using the dot product

    A = dir * normal
```

Uso del componente C# de Grasshopper:

![](https://developer.rhino3d.com/images/math-image165.png)
```cs
private void RunScript(Point3d pt, Surface srf, ref object A)

{

  //Declare variables

  double u, v;

  Point3d closest_pt;

 

  //get closest point u, v

  srf.ClosestPoint(pt, out u, out v);

 

  //get closest point

  closest_pt = srf.PointAt(u, v);

 

  //calculate direction from closest point to test point

  Vector3d dir = pt - closest_pt;

 

  //calculate surface normal

  Vector3d normal = srf.NormalAt(u, v);

 

  //compare the two directions using the dot product

  A = dir * normal;

}
```

### 1.5.2 Caja descompuesta

El siguiente tutorial muestra cómo descomponer una polisuperficie. Así es como queda la caja descompuesta al final:

![](https://developer.rhino3d.com/images/math-image15.jpg)

**Entrada:**

Identifique la entrada, que es una caja.

![](https://developer.rhino3d.com/images/math-image17.jpg)

**Parámetros:**

- Piense en todos los parámetros que tenemos que conocer para este tutorial.
- El centro de la descomposición.
- Las caras de la caja que estamos descomponiendo.
- La dirección hacia la que se mueve cada cara.
![](https://developer.rhino3d.com/images/math-image19.jpg)

Una vez identificados los parámetros, es cuestión de juntarlos en una solución uniendo los pasos lógicos para lograr una respuesta.

**Solución:**

1\. Encuentre el centro de la caja utilizando el componente **Box Properties** en GH:

![](https://developer.rhino3d.com/images/math-image21.png)

2\. Extraiga las caras de la caja con el componente **Deconstruct Brep**:

![](https://developer.rhino3d.com/images/math-image23.png)

3\. La dirección hacia la que movemos las caras es la parte complicada. Primero debemos encontrar el centro de cada cara y luego definir la dirección desde el centro de la caja hacia el centro de cada cara de la siguiente manera:

![](https://developer.rhino3d.com/images/math-image25.png)

4\. Una vez tengamos todos los parámetros listos, podemos usar el componente **Move** para mover las caras en la dirección adecuada. Asegúrese de configurar la amplitud deseada de los vectores y ya podrá empezar.

![](https://developer.rhino3d.com/images/math-image27.png)

Los pasos anteriores también se pueden resolver mediante VB script, C# o Python. A continuación se muestra la solución con estos lenguajes de scripting.

Uso del componente VB de Grasshopper:

![](https://developer.rhino3d.com/images/math-image29.png)
```vb
Private Sub RunScript(ByVal box As Brep, ByVal dis As Double, ByRef A As Object)

 

    'get the brep center

    Dim area As Rhino.Geometry.AreaMassProperties

    area = Rhino.Geometry.AreaMassProperties.Compute(box)

 

    Dim box_center As Point3d

    box_center = area.Centroid

 

    'get a list of faces

    Dim faces As Rhino.Geometry.Collections.BrepFaceList = box.Faces

 

    'decalre variables

    Dim center As Point3d

    Dim dir As Vector3d

    Dim exploded_faces As New List( Of Rhino.Geometry.Brep )

    Dim i As Int32

    'loop through all faces

 

    For i = 0 To faces.Count() - 1

      'extract each of the face

      Dim extracted_face As Rhino.Geometry.Brep = box.Faces.ExtractFace(i)

 

      'get the center of each face

      area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face)

      center = area.Centroid

 

      'calculate move direction (from box centroid to face center)

      dir = center - box_center

      dir.Unitize()

      dir *= dis

 

      'move the extracted face

      extracted_face.Transform(Transform.Translation(dir))

 

      'add to exploded_faces list

      exploded_faces.Add(extracted_face)

    Next

 

    'assign exploded list of faces to output

    A = exploded_faces

  End Sub
```

Uso del componente Python de Grasshopper con RhinoCommon:

![](https://developer.rhino3d.com/images/math-image4.png)
```python
import Rhino

 

#get the brep center

area = Rhino.Geometry.AreaMassProperties.Compute(box)

box_center = area.Centroid

 

#get a list of faces

faces = box.Faces

 

#decalre variables

exploded_faces = []

 

#loop through all faces

for i, face in enumerate(faces):

 

    #get a duplicate of the face

    extracted_face = faces.ExtractFace(i)

    

    #get the center of each face

    area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face)

    center = area.Centroid

    

    #calculate move direction (from box centroid to face center)

    dir = center - box_center

    dir.Unitize()

    dir *= dis

    

    #move the extracted face

    move = Rhino.Geometry.Transform.Translation(dir)

    extracted_face.Transform(move)

    

    #add to exploded_faces list

    exploded_faces.append(extracted_face)

 

#assign exploded list of faces to output

A = exploded_faces
```

Uso del componente C# de Grasshopper:

![](https://developer.rhino3d.com/images/math-image2.png)
```cs
private void RunScript(Brep box, double dis, ref object A)

{

 

    //get the brep center

  Rhino.Geometry.AreaMassProperties area =        Rhino.Geometry.AreaMassProperties.Compute(box);

  Point3d box_center = area.Centroid;

 

  //get a list of faces

  Rhino.Geometry.Collections.BrepFaceList faces = box.Faces;

 

  //decalre variables

  Point3d center;   Vector3d dir;

  List<Rhino.Geometry.Brep> exploded_faces = new List<Rhino.Geometry.Brep>();

 

  //loop through all faces   for( int i = 0; i < faces.Count(); i++ )

  {

    //extract each of the face

    Rhino.Geometry.Brep extracted_face = box.Faces.ExtractFace(i);

 

    //get the center of each face

    area = Rhino.Geometry.AreaMassProperties.Compute(extracted_face);

    center = area.Centroid;

 

    //calculate move direction (from box centroid to face center)

    dir = center - box_center;

    dir.Unitize();

    dir *= dis;

 

    //move the extracted face

    extracted_face.Transform(Transform.Translation(dir));

 

    //add to exploded_faces list

    exploded_faces.Add(extracted_face);

  }

 

  //assign exploded list of faces to output

  A = exploded_faces;

}
```

### 1.5.3 Esferas tangentes

Este tutorial muestra cómo crear dos esferas tangentes entre dos puntos de entrada. El resultado será el siguiente:

![](https://developer.rhino3d.com/images/math-image5.png)

**Entrada:**  
Dos puntos ( 
$$
A
$$
 y 
$$
B
$$
) en el sistema de coordenadas 3D.

![](https://developer.rhino3d.com/images/math-image6.png)

Parámetros: A continuación, se muestra un diagrama de los parámetros que necesitaremos para resolver el problema: 
$$
A
$$
 punto tangente 
$$
D
$$
 entre las dos esferas, en algún parámetro 
$$
t
$$
 (0-1) entre los puntos 
$$
A
$$
 y 
$$
B
$$
.

- El centro de la primera esfera o el punto medio 
	$$
	C 1
	$$
	 entre 
	$$
	A
	$$
	 y 
	$$
	D
	$$
	.
- El centro de la segunda esfera o el punto medio 
	$$
	C 2
	$$
	 entre 
	$$
	D
	$$
	 y 
	$$
	B
	$$
	.
- El radio de la primera esfera 
	$$
	\left(\right. r 1 \left.\right)
	$$
	 o la distancia entre 
	$$
	A
	$$
	 y 
	$$
	C 1
	$$
	.
- El radio de la segunda esfera 
	$$
	\left(\right. r 2 \left.\right)
	$$
	 o la distancia entre 
	$$
	D
	$$
	 y 
	$$
	C 2
	$$
	.

**Solución:**

1\. Utilice el componente **Expression** para definir el punto 
$$
D
$$
 entre 
$$
A
$$
 y 
$$
B
$$
 como parámetro 
$$
t
$$
. La expresión que usaremos se basa en la ecuación vectorial de una línea:

$$
D = A + t * \left(\right. B - A \left.\right)
$$

$$
B - A
$$
: es el vector que va de 
$$
B
$$
 a

$$A (\\vec{BA}) mediante la operación de resta de vectores.

$$

t\*(B-A) 
$$
: d o n d e
$$
 t

$$ está entre 0 y 1 para obtener una ubicación en el vector.

$$

A+t\*(B-A)

$$: obtiene un punto en el vector entre A y B.

![](https://developer.rhino3d.com/images/math-image8.png)

2\. Utilice el componente Expression para definir también los puntos medios $$

C1 
$$
y
$$
 C2

$$.

![](https://developer.rhino3d.com/images/math-image9.png)

3\. El radio de la primera esfera $$

(r1) 
$$
y e l r a d i o d e l a s e g u n d a e s f e r a
$$
 (r2)

$$ se pueden calcular utilizando el componente **Distance**.

![](https://developer.rhino3d.com/images/math-image10.png)

4\. El último paso consiste en crear la esfera a partir de un plano base y un radio. Debemos asegurarnos de que los orígenes estén conectados a $$

C1 
$$
y
$$
 C2 
$$
y a l r a d i o d e
$$
 r1 
$$
y
$$
 r2$$. ![](https://developer.rhino3d.com/images/math-image54.png)

**Uso del componente VB de Grasshopper:**

![](https://developer.rhino3d.com/images/math-image56.png)
```vb
Private Sub RunScript(ByVal A As Point3d, ByVal B As Point3d, ByVal t As Double, ByRef S1 As Object, ByRef S2 As Object)

 

  'declare variables

  Dim D, C1, C2 As Rhino.Geometry.Point3d

  Dim r1, r2 As Double

 

  'find a point between A and B

  D = A + t * (B - A)

 

  'find mid point between A and D

  C1 = A + 0.5 * (D - A)

 

  'find mid point between D and B

  C2 = D + 0.5 * (B - D)

  'find spheres radius

  r1 = A.DistanceTo(C1)

  r2 = B.DistanceTo(C2)

 

  'create spheres and assign to output

  S1 = New Rhino.Geometry.Sphere(C1, r1)

  S2 = New Rhino.Geometry.Sphere(C2, r2)

 

End Sub
```

Uso del componente Python:

![](https://developer.rhino3d.com/images/math-image62.png)
```python
import Rhino

 

#find a point between A and B

D = A + t * (B - A)

 

#find mid point between A and D

C1 = A + 0.5 * (D - A)

 

#find mid point between D and B

C2 = D + 0.5 * (B - D)

 

#find spheres radius

r1 = A.DistanceTo(C1)

r2 = B.DistanceTo(C2)

 

#create spheres and assign to output

S1 = Rhino.Geometry.Sphere(C1, r1)

S2 = Rhino.Geometry.Sphere(C2, r2)
```

Uso del componente C# de Grasshopper:

![](https://developer.rhino3d.com/images/math-image58.png)
```cs
private void RunScript(Point3d A, Point3d B, double t, ref object S1, ref object S2)

{

  //declare variables

  Rhino.Geometry.Point3d D, C1, C2;

  double r1, r2;

 

  //find a point between A and B

  D = A + t * (B - A);

 

  //find mid point between A and D

  C1 = A + 0.5 * (D - A);

 

  //find mid point between D and B

  C2 = D + 0.5 * (B - D);

 

  //find spheres radius

  r1 = A.DistanceTo(C1);

  r2 = B.DistanceTo(C2);

 

  //create spheres and assign to output

  S1 = new Rhino.Geometry.Sphere(C1, r1);

  S2 = new Rhino.Geometry.Sphere(C2, r2);

}
```

## Descargar archivos de muestra

Descargue el archivo [math-samplesandtutorials.zip](https://developer.rhino3d.com/files/math-samplesandtutorials.zip), que contiene todos los archivos de ejemplo de Grasshopper y de código de esta guía.

## Próximos pasos

Ahora que ya conoce las matemáticas vectoriales, consulte la guía [Matrices y transformaciones](https://developer.rhino3d.com/guides/general/essential-mathematics/matrices-transformations/) para aprender más sobre mover, rotar y escalar objetos….