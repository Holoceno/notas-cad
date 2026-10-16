---
tags: [tipo/apunte, programacion/algoritmos, software/cadcraft, fabricacion/planos]
---

# OVERKILL — cómo lo hace CADCraft

Fuente: `crates/engine/src/cmd/overkill.rs` (v0.6.2, ~780 líneas Rust).

## Idea clave
No compara todos contra todos (O(n²)). **Agrupa primero** (hash / ordenar) y solo compara dentro de cada grupo → ~O(n log n).

## 4 pasadas
1. **Duplicados exactos** → serializa cada objeto, redondea números a la tolerancia, usa el texto como clave de diccionario. Mismo texto = duplicado.
2. **Líneas colineales** → (a) dirección sin sentido (θ y θ+180° son la misma), (b) ordenar por ángulo y agrupar, (c) dentro, agrupar por distancia perpendicular (offset), (d) proyectar cada línea a un intervalo 1D `[t0, t1]` y **fusionar intervalos** como en un calendario.
3. **Arcos** → agrupar por (centro, radio); si hay un círculo, se come los arcos; si no, fusionar intervalos angulares (con el caso que cruza 360°).
4. **Polilíneas** → quitar segmentos de largo cero y vértices colineales.

## Trucos
- "Costura" de ángulos en −70,7° (−1,2346 rad): un ángulo raro, así líneas a 0°/90° nunca quedan partidas en el borde.
- No borra objetos de capas bloqueadas ni los que tienen cotas asociativas.

## Limitaciones encontradas
- Redondear a grilla puede fallar justo en el borde de una celda (dos valores a 0,1 × tol de distancia pueden caer en celdas distintas).
- No compara segmentos de polilínea contra líneas sueltas (documentado en docs/gaps.md).

Ver: [[CadQuery a CADCraft (planos 2D)]]

## En la Wiki Rhino
- [[vector-mathematics|Matemáticas vectoriales]]: producto punto (proyectar a 1D) y producto cruz (distancia a la recta), la base del algoritmo
- [[rhinocommon-interseccion-api|API de intersecciones]] · [[rhinocommon-capas-api|API de capas]]
