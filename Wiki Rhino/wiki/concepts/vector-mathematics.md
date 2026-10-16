---
title: "Vector Mathematics"
type: concept
tags: [tipo/concepto, matematicas/vectores, geometria/puntos-vectores]
palabras-clave: [vectores, matematicas, geometria-computacional, producto-escalar, producto-vectorial]
sources: [raw/rhinocommon/1 Matemáticas vectoriales.md]
created: 2026-05-03
updated: 2026-10-13
---

Un vector representa una cantidad con dirección y longitud: `v = <a1, a2, a3>`. A diferencia de un punto (ubicación), un vector es independiente de su punto de anclaje — todas las flechas con la misma dirección y longitud son el mismo vector.

## Representación y longitud

- **Vector de posición**: anclado en el origen; sus componentes coinciden con las coordenadas del extremo
- **Longitud**: `|v| = √(a1² + a2² + a3²)`
- **Vector unitario**: `u = v / |v|`, longitud = 1; usado para comparar direcciones puras

## Operaciones básicas

| Operación | Resultado | Uso |
|-----------|-----------|-----|
| Escalar: `t * v` | vector escalado | cambiar magnitud |
| Suma: `a + b` | nuevo vector | dirección media (con unitarios) |
| Resta: `a - b` | vector de b → a | encontrar dirección entre dos puntos |

## Producto escalar (Dot product)

`a · b = a1*b1 + a2*b2 + a3*b3` → escalar

- Equivale a `|a| * |b| * cos(θ)` — relación directa con el ángulo entre vectores
- Con unitarios: `a · b = cos(θ)`, rango [-1, 1]
- **Ortogonalidad**: `a · b = 0` ↔ vectores perpendiculares
- **Proyección**: `a · unit(b)` = longitud de proyección de `a` sobre `b`

## Producto vectorial (Cross product)

`a × b = <a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1>` → vector

- El resultado es **perpendicular a ambos** vectores de entrada
- Dirección: regla de la mano derecha (sistema diestro de Rhino)
- Longitud: `|a × b| = |a| * |b| * sin(θ)` — proporcional al seno del ángulo
- **Paralelismo**: `a × b = 0` ↔ vectores paralelos
- El orden importa: `a × b = -(b × a)`

## Ecuación vectorial de una línea

```
P = Q + t * v
```
Donde `Q` es un punto conocido, `v` la dirección, `t` un número real. Con `t ∈ [0,1]` recorre el segmento entre dos puntos. Punto medio: `M = Q + 0.5 * (P - Q)`.

## Ecuación vectorial de un plano

Un plano queda definido por un punto y su normal `n`. La ecuación escalar:
```
n · (b - a) = 0
```
La normal se obtiene como `n = (B - A) × (C - A)` dados tres puntos no colineales.

## Connections

- Mapas: [[Mapa - Puntos, vectores y planos]]
- [[wiki/concepts/transformaciones-geometricas]] — las matrices de transformación se construyen sobre estas operaciones
- [[wiki/concepts/curvas-nurbs]] — las tangentes a curvas NURBS son vectores
- [[wiki/sources/2026-05-03-matematicas-vectoriales]] — fuente primaria
