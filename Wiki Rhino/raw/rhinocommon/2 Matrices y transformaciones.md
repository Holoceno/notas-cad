---
title: "2 Matrices y transformaciones"
source: "https://developer.rhino3d.com/guides/general/essential-mathematics/matrices-transformations/"
author:
  - "[[Robert McNeel & Associates]]"
published:
created: 2026-05-03
description: "Rhinoceros 3D: Esta guía estudia las operaciones y transformaciones de matrices."
tags:
  - "clippings"
---
*Transformaciones* hace referencia a operaciones como mover (denominado también *traslación*), rotar y escalar objetos. En programación 3D se almacenan utilizando matrices, que son series rectangulares de números. Se pueden realizar múltiples transformaciones rápidamente utilizando matrices. Una matriz \[\[4x4\]\] puede representar todas las transformaciones. Tener una dimensión de matriz unificada para todas las transformaciones ahorra tiempo de cálculo.

$$
\text{matrix} & \begin{matrix}c 1 & c 2 & c 3 & c 4\end{matrix} \\ \begin{matrix}r o w \left(\right. 1 \left.\right) \\ r o w \left(\right. 2 \left.\right) \\ r o w \left(\right. 3 \left.\right) \\ r o w \left(\right. 4 \left.\right)\end{matrix} & \left[\right. \begin{matrix}+ & + & + & + \\ + & + & + & + \\ + & + & + & + \\ + & + & + & +\end{matrix} \left]\right.
$$

## 2.1 Operaciones con matrices

La operación más relevante en el diseño gráfico por ordenador es la multiplicación de matrices. Ahora lo explicamos con más detalle.

### Multiplicación de matrices

La multiplicación de matrices se utiliza para aplicar transformaciones a la geometría. Por ejemplo, si tenemos un punto y queremos rotarlo alrededor de un eje, usamos una matriz de rotación y la multiplicamos por el punto para obtener la nueva ubicación rotada.

$$
\text{rotate matrix} & \text{input point} & \text{rotate point} \\ \left[\right. \begin{matrix}a & b & c & d \\ e & f & g & h \\ i & j & k & l \\ 0 & 0 & 0 & 1\end{matrix} \left]\right. & \cdot \left[\right. \begin{matrix}x \\ y \\ z \\ 1\end{matrix} \left]\right. & = \left[\right. \begin{matrix}x^{'} \\ y^{'} \\ z^{'} \\ 1\end{matrix} \left]\right.
$$

La mayoría de las veces, necesitamos realizar múltiples transformaciones en la misma geometría. Por ejemplo, si necesitamos mover y rotar mil puntos, podemos usar cualquiera de los siguientes métodos.

**Método 1**

1. Multiplique la matriz de movimiento por 1000 puntos para mover los puntos.
2. Multiplique la matriz de rotación por los 1000 puntos resultantes para rotar los puntos movidos.

Número de operaciones = **2000**.

**Método 2**

1. Multiplique las matrices de rotación y movimiento para crear una matriz de transformación combinada.
2. Multiplique la matriz combinada por 1000 puntos para mover y rotar en un solo paso.

Número de operaciones = **1001**.

Observe que el método 1 requiere casi el doble de operaciones para lograr el mismo resultado. Si bien el método 2 es muy eficaz, solo es posible si las matrices de movimiento y rotación son 
$$
\left[\right. 4 \times 4 \left]\right.
$$
. Por este motivo, en el diseño gráfico por ordenador se usa una matriz 
$$
\left[\right. 4 \times 4 \left]\right.
$$
 para representar todas las transformaciones, y una matriz 
$$
\left[\right. 4 \times 1 \left]\right.
$$
 para representar puntos.

Las aplicaciones de modelado tridimensional proporcionan herramientas para aplicar transformaciones y multiplicar matrices, pero si tiene curiosidad sobre cómo multiplicar matrices matemáticamente, le explicaremos un ejemplo sencillo. Para multiplicar dos matrices, éstas tienen que coincidir. En otras palabras, el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz. La matriz resultante tiene un tamaño igual al número de filas de la primera matriz y al número de columnas de la segunda matriz. Por ejemplo, si tenemos dos matrices, 
$$
M
$$
 y 
$$
P
$$
, con tamaños igual a 
$$
\left[\right. 4 \times 4 \left]\right.
$$
 and 
$$
\left[\right. 4 \times 1 \left]\right.
$$
 respectivamente, la matriz de multiplicación resultante 
$$
M \cdot P
$$
 tiene un tamaño igual a 
$$
\left[\right. 4 \times 1 \left]\right.
$$
, como se muestra en la siguiente ilustración:

$$
M & P & P^{'} \\ \left[\right. \begin{matrix}a & b & c & d \\ e & f & g & h \\ i & j & k & l \\ 0 & 0 & 0 & 1\end{matrix} \left]\right. & \cdot \left[\right. \begin{matrix}x \\ y \\ z \\ 1\end{matrix} \left]\right. & = \left[\right. \begin{matrix}x^{'} = a * x + b * y + c * z + d * 1 \\ y^{'} = e * x + f * y + g * z + h * 1 \\ z^{'} = i * x + j * y + k * z + l * 1 \\ 1 = 0 * x + 0 * y + 0 * z + 1 * 1\end{matrix} \left]\right.
$$

### Matriz de identidad

La matriz de identidad es una matriz especial donde todos los componentes diagonales son iguales a 1 y el resto igual a 0.

![](https://developer.rhino3d.com/images/math-image68.png)

La propiedad principal de la matriz identidad es que si se multiplica por cualquier otra matriz, los valores multiplicados por cero no cambian.

![](https://developer.rhino3d.com/images/math-image52.png)

## 2.2 Operaciones de transformación

La mayoría de las transformaciones conservan la relación paralela entre las partes de la geometría. Por ejemplo, los puntos colineales permanecen colineales después de la transformación. También los puntos de un plano permanecen coplanares después de la transformación. Este tipo de transformación se denomina transformacion *afin*.

### Traslación (mover)

Mover un punto desde una posición inicial a lo largo de un vector determinado se calcula de la siguiente manera:

$$
P^{'} = P + \overset{\rightarrow}{\mathbf{v}}
$$
 ![https://developer.rhino3d.com/images/math-image35.png](https://developer.rhino3d.com/images/math-image35.png)

Supongamos que:  
$$
P \left(\right. x , y , z \left.\right)
$$
 es un punto dado  
$$
\overset{\rightarrow}{\mathbf{v}} =< a , b , c >
$$
 es un vector de traslación  
Entonces:  
$$
P^{'} \left(\right. x \left.\right) = x + a
$$
  
$$
P^{'} \left(\right. y \left.\right) = y + b
$$
  
$$
P^{'} \left(\right. z \left.\right) = z + c
$$

Los puntos se representan en un formato de matriz utilizando una matriz \[4x1\] con un 1 insertado en la última fila. Por ejemplo, el punto P (x,y,z) se representa de la siguiente manera:

$$
\left[\right. x \\ y \\ z \\ 1 \left]\right.
$$

El uso de una matriz 
$$
\left[\right. 4 \times 4 \left]\right.
$$
 para las transformaciones (lo que se denomina un sistema de coordenadas homogéneo) en lugar una matriz 
$$
\left[\right. 3 \times 3 \left]\right.
$$
, permite representar todas las transformaciones, incluida la traslación. El formato general de una matriz de traslación es:

$$
\left[\right. 1 & 0 & 0 & a 1 \\ 0 & 1 & 0 & a 2 \\ 0 & 0 & 1 & a 3 \\ 0 & 0 & 0 & 1 \left]\right.
$$

Por ejemplo, para mover el punto 
$$
P \left(\right. 2 , 3 , 1 \left.\right)
$$
 por el vector 
$$
\overset{\rightarrow}{v} < 2 , 2 , 2 >
$$
, la nueva ubicación del punto es:

$$
P^{'} = P + \overset{\rightarrow}{\mathbf{v}} = \left(\right. 2 + 2 , 3 + 2 , 1 + 2 \left.\right) = \left(\right. 4 , 5 , 3 \left.\right)
$$

Si empleamos las matrices y multiplicamos la matriz de traslación por el punto de entrada, obtenemos la nueva ubicación del punto como se muestra a continuación:

$$
\left[\right. 1 & 0 & 0 & 2 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 1 \left]\right. \cdot \left[\right. 2 \\ 3 \\ 1 \\ 1 \left]\right. = \left[\right. \left(\right. 1 * 2 + 0 * 3 + 0 * 1 + 2 * 1 \left.\right) \\ \left(\right. 0 * 2 + 1 * 3 + 0 * 1 + 2 * 1 \left.\right) \\ \left(\right. 0 * 2 + 0 * 3 + 1 * 1 + 2 * 1 \left.\right) \\ \left(\right. 0 * 2 + 0 * 3 + 0 * 1 + 1 * 1 \left.\right) \left]\right. = \left[\right. 4 \\ 5 \\ 3 \\ 1 \left]\right.
$$

De manera similar, cualquier geometría se traslada multiplicando sus puntos de construcción por la matriz de traslación. Por ejemplo, si tenemos una caja definida por ocho puntos de esquina y queremos moverla 4 unidades en la dirección x, 5 unidades en la dirección y, y 3 unidades en la dirección z, debemos multiplicar cada uno de los ocho puntos de esquina de la caja por la siguiente matriz de traslación para obtener la nueva caja.

$$
\left[\right. 1 & 0 & 0 & 4 \\ 0 & 1 & 0 & 5 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \left]\right.
$$
![](https://developer.rhino3d.com/images/math-image37.png)

Figura (19): Traslación de todos los puntos de esquina de la caja.

### Rotación

Esta sección muestra cómo calcular la rotación alrededor del eje z y el punto de origen utilizando la trigonometría, y luego deducir el formato general de la matriz para la rotación.

![https://developer.rhino3d.com/images/math-image39.png](https://developer.rhino3d.com/images/math-image39.png)

Tome un punto en el plano 
$$
x , y
$$
 
$$
P \left(\right. x , y \left.\right)
$$
 y gírelo un ángulo ( 
$$
b
$$
). Del resultado, podemos deducir lo siguiente:

$$
x = d c o s \left(\right. a \left.\right)
$$
 (1)  
$$
y = d s i n \left(\right. a \left.\right)
$$
 (2)  
$$
x^{'} = d c o s \left(\right. b + a \left.\right)
$$
 (3)  
$$
y^{'} = d s i n \left(\right. b + a \left.\right)
$$
 (4)  
Podemos expandir 
$$
x
$$
 ’ e 
$$
y^{'}
$$
 usando las identidades trigonométricas del seno y el coseno de la suma de ángulos:  
$$
x^{'} = d c o s \left(\right. a \left.\right) c o s \left(\right. b \left.\right) - d s i n \left(\right. a \left.\right) s i n \left(\right. b \left.\right)
$$
 (5)  
$$
y^{'} = d c o s \left(\right. a \left.\right) s i n \left(\right. b \left.\right) + d s i n \left(\right. a \left.\right) c o s \left(\right. b \left.\right)
$$
 (6)  
Usando las ecuaciones 1 y 2:  
$$
x^{'} = x c o s \left(\right. b \left.\right) - y s i n \left(\right. b \left.\right)
$$
  
y’ = x sin(b) + y cos(b)

La matriz de rotación alrededor del **eje z** quedaría así:

$$
\left[\right. cos ⁡ b & - sin ⁡ b & 0 & 0 \\ sin ⁡ b & cos ⁡ b & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \left]\right.
$$

La matriz de rotación alrededor del **eje x** por el ángulo 
$$
b
$$
 quedaría así:

$$
\left[\right. 1 & 0 & 0 & 0 \\ 0 & cos ⁡ b & - sin ⁡ b & 0 \\ 0 & sin ⁡ b & cos ⁡ b & 0 \\ 0 & 0 & 0 & 1 \left]\right.
$$

La matriz de rotación alrededor del **eje y** por el ángulo 
$$
b
$$
 quedaría así:

$$
\left[\right. cos ⁡ b & 0 & sin ⁡ b & 0 \\ 0 & 1 & 0 & 0 \\ - sin ⁡ b & 0 & cos ⁡ b & 0 \\ 0 & 0 & 0 & 1 \left]\right.
$$

Por ejemplo, si tenemos una caja y queremos rotarla 30 grados, necesitamos lo siguiente:

1\. Construya la matriz de rotación de 30 grados. Utilizando la forma genérica y los valores de coseno y seno del ángulo de 30 grados, la matriz de rotación quedaría así:

$$
\left[\right. 0.87 & - 0.5 & 0 & 0 \\ 0.5 & 0.87 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \left]\right.
$$

2\. Multiplique la matriz de rotación por la geometría de entrada o, en el caso de una caja, multípliquela por cada uno de los puntos de esquina para hallar la nueva ubicación de la caja.

![](https://developer.rhino3d.com/images/math-image41.png)

Figura (20): Rotar geometría.

### Escalado

Para escalar la geometría, necesitamos un factor de escala y un centro de escala. El factor de escala puede ser uniforme por igual en las direcciones x,y,z, o puede ser único para cada dimensión.

Para escalar un punto, se puede usar la siguiente ecuación:

$$
P^{'} = S c a l e F a c t o r \left(\right. S \left.\right) * P
$$

O bien:

$$
P^{'} . x = S x * P . x
$$
  
$$
P^{'} . y = S y * P . y
$$
  
$$
P^{'} . z = S z * P . z
$$

Este es el formato de la matriz de escalado, teniendo en cuenta que el centro del escalado es el punto de origen universal (0,0,0).

$$
\left[\right. S c a l e - x & 0 & 0 & 0 \\ 0 & S c a l e - y & 0 & 0 \\ 0 & 0 & S c a l e - z & 0 \\ 0 & 0 & 0 & 1 \left]\right.
$$

Por ejemplo, si quisiéramos escalar una caja 0.25 unidades en relación con el origen universal, la matriz de escalado quedaría así:

![](https://developer.rhino3d.com/images/math-image43.png)

Figura (21): Geometría a escala

### Sesgado

El sesgado en tres dimensiones se mide a lo largo de un par de ejes en relación con el tercero. Por ejemplo, el sesgado en el eje z no va a cambiar la geometría a lo largo de ese eje, sino que altera los valores en x e y. Estos son algunos ejemplos de matrices de sesgado:

1\. Sesgado en x y z, manteniendo fija la coordenada y:

![https://developer.rhino3d.com/images/math-image45.png](https://developer.rhino3d.com/images/math-image45.png) 
$$
\left[\right. 1.0 & 0.5 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$
 ![https://developer.rhino3d.com/images/math-image47.png](https://developer.rhino3d.com/images/math-image47.png) 
$$
\left[\right. 1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.5 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$

2\. Sesgado en y y z, manteniendo fija la coordenada x:

![https://developer.rhino3d.com/images/math-image49.png](https://developer.rhino3d.com/images/math-image49.png) 
$$
\left[\right. 1.0 & 0.5 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$
 ![https://developer.rhino3d.com/images/math-image50.png](https://developer.rhino3d.com/images/math-image50.png) 
$$
\left[\right. 1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.5 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$

3\. Sesgado en x e y, manteniendo fija la coordenada z:

![https://developer.rhino3d.com/images/math-image32.png](https://developer.rhino3d.com/images/math-image32.png) 
$$
\left[\right. 1.0 & 0.0 & 0.5 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$
 ![https://developer.rhino3d.com/images/math-image33.png](https://developer.rhino3d.com/images/math-image33.png) 
$$
\left[\right. 1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.5 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$

### Reflejo o espejo

El reflejo o espejo crea un reflejo de un objeto a través de una línea o un plano. Los objetos 2D se reflejan a través de una línea, mientras que los objetos 3D se reflejan en un plano. Tenga en cuenta que la transformación de reflejo cambia la dirección normal de las caras de la geometría.

![](https://developer.rhino3d.com/images/math-image98.png)

Figura (23): Matriz de reflejo en el plano xy universal. Las direcciones de las caras se invierten.

### Proyección plana

Intuitivamente, el punto de proyección de un punto 3D dado 
$$
P \left(\right. x , y , z \left.\right)
$$
 sobre el plano xy universal es igual a 
$$
P_{x y} \left(\right. x , y , 0 \left.\right)
$$
 estableciendo el valor z en cero. De forma similar, la proyección de un punto P en el plano xz es 
$$
P_{x z} \left(\right. x , 0 , z \left.\right)
$$
. Al proyectar sobre el plano, 
$$
P_{x z} = \left(\right. 0 , y , z \left.\right)
$$
. Estas proyecciones se denominan proyecciones ortogonales.

Si tenemos una curva como entrada y aplicamos la transformación de proyección plana, obtenemos una curva proyectada sobre ese plano. A continuación se muestra un ejemplo de una curva proyectada sobre el plano xy con el formato de matriz.

Nota: las curvas NURBS (que se explican en el siguiente capítulo) utilizan puntos de control para definir las curvas. La proyección de una curva pasa por la proyección de sus puntos de control.

![https://developer.rhino3d.com/images/math-image100.png](https://developer.rhino3d.com/images/math-image100.png) 
$$
\left[\right. 1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$
 ![https://developer.rhino3d.com/images/math-image102.png](https://developer.rhino3d.com/images/math-image102.png) 
$$
\left[\right. 1.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$
 ![https://developer.rhino3d.com/images/math-image104.png](https://developer.rhino3d.com/images/math-image104.png) 
$$
\left[\right. 0.0 & 0.0 & 0.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 0.0 & 0.0 & 1.0 \left]\right.
$$

## Descargar archivos de muestra

Descargue [este archivo](https://www.rhino3d.com/download/rhino/6/essentialmathematics/), que contiene todos los archivos de ejemplo de Grasshopper y de código de esta guía.

## Próximos pasos

Ahora que tiene más conocimientos sobre matrices y transformaciones, eche un vistazo a la guía [Curvas y superficies paramétricas](https://developer.rhino3d.com/guides/general/essential-mathematics/parametric-curves-surfaces/) para aprender más sobre la estructura detallada de las curvas y superficies NURBS.