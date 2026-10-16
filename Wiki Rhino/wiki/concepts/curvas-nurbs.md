---
title: "Curvas NURBS"
type: concept
tags: [tipo/concepto, geometria/curvas, geometria/nurbs]
palabras-clave: [nurbs, curvas, parametrico, bezier, grado, puntos-de-control, nodos, pesos]
sources: [raw/rhinocommon/3 Curvas y superficies paramétricas.md]
created: 2026-05-03
updated: 2026-10-13
---

NURBS (Non-Uniform Rational B-Splines) es la representación matemática principal que usa Rhino para curvas y superficies. Combina precisión matemática con edición intuitiva vía puntos de control.

## Curvas paramétricas: el concepto base

Una curva paramétrica mapea un parámetro `t` dentro de un dominio `[t0, t1]` a un punto `(x,y,z)` en el espacio. El parámetro no garantiza velocidad constante: intervalos iguales de `t` no producen distancias iguales en la curva 3D (salvo en líneas de grado 1).

## Los 4 atributos de una curva NURBS

### 1. Grado
Entero positivo que determina cuántos puntos de control afectan cada segmento (grado + 1 CPs por segmento):

| Grado | Geometría típica |
|-------|-----------------|
| 1 | Líneas, polilíneas |
| 2 | Círculos, elipses, cónicas |
| 3 | Curvas de forma libre (más común) |
| 5 | Curvas de forma libre de alta calidad |

### 2. Puntos de control (CPs)
Lista de puntos que definen la forma. En curvas **ancladas** (clamped), los extremos de la curva pasan por los CPs extremos. En curvas **periódicas** (cerradas suaves), la costura no pasa por ningún CP. Mover un CP afecta localmente la curva.

### 3. Pesos
Cada CP tiene un peso (número positivo). Cuando todos son iguales (generalmente 1) la curva es **no racional**. Pesos distintos crean curvas **racionales** necesarias para representar círculos y elipses exactos. Recomendación: no modificar pesos salvo para representar cónicas exactas.

### 4. Nodos (Knot vector)
Lista no decreciente de valores de parámetro. Número de nodos = número de CPs + grado - 1.

- **Multiplicidad**: cuántas veces aparece un nodo. Máximo = grado.
- **Multiplicidad total** (= grado): la curva pasa por ese CP → punto de torsión en nodos interiores.
- **Nodos uniformes**: espaciado constante entre nodos interiores.
- **Nodos no uniformes**: espaciado proporcional al espaciado de CPs → curvas más suaves.
- Escalar la lista de nodos no cambia la curva 3D.

## Curvas ancladas vs. periódicas

| | Anclada (abierta) | Periódica (cerrada suave) |
|-|-|-|
| Extremos | Pasan por CPs extremos | Costura no coincide con CPs |
| Nodos inicial/final | Multiplicidad total | Nodos simples |
| Punto de torsión | Posible con nodos interiores totales | No existe |

## Algoritmo de De Casteljau (Bézier)
Método iterativo para calcular un punto en `t`: interpolación lineal recursiva entre puntos de control hasta obtener un único punto.

## Algoritmo de De Boor (NURBS)
Generalización de De Casteljau para NURBS. Estable numéricamente; usado internamente por Rhino.

## Connections

- Mapas: [[Mapa - Curvas]] · [[Mapa - Superficies y NURBS]]
- [[wiki/concepts/continuidad-geometrica]] — cómo unir segmentos NURBS suavemente
- [[wiki/concepts/curvatura]] — análisis de la forma de la curva
- [[wiki/concepts/superficies-nurbs]] — extensión del concepto a dos dimensiones
- [[wiki/sources/2026-05-03-curvas-superficies-parametricas]] — fuente primaria
