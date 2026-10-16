---
title: "Transformaciones Geométricas (Matrices 4×4)"
type: concept
tags: [tipo/concepto, geometria/transformaciones, matematicas/matrices]
palabras-clave: [matrices, transformaciones, traslacion, rotacion, escala, sesgado, reflejo, proyeccion]
sources: [raw/rhinocommon/2 Matrices y transformaciones.md]
created: 2026-05-03
updated: 2026-10-13
---

Las transformaciones geométricas (mover, rotar, escalar) se representan en programación 3D como matrices 4×4 usando coordenadas homogéneas. Un sistema unificado permite combinar múltiples transformaciones en una sola multiplicación antes de aplicarlas a la geometría.

## Por qué 4×4 (coordenadas homogéneas)

Con una matriz 3×3 no se puede representar la traslación. Al añadir una cuarta coordenada `w=1` a los puntos `[x, y, z, 1]`, todas las transformaciones —incluyendo traslación— caben en una misma matriz 4×4.

**Eficiencia:** combinar dos transformaciones antes de aplicarlas a 1000 puntos = 1001 operaciones vs 2000 por separado.

## Las 6 transformaciones fundamentales

### Traslación
```
[1  0  0  a1]   [x]   [x + a1]
[0  1  0  a2] · [y] = [y + a2]
[0  0  1  a3]   [z]   [z + a3]
[0  0  0   1]   [1]   [  1   ]
```

### Rotación
- Eje Z: `[cos b, -sin b, 0, 0 / sin b, cos b, 0, 0 / 0, 0, 1, 0 / 0, 0, 0, 1]`
- Eje X: cos/sin en el bloque Y-Z
- Eje Y: cos/sin en el bloque X-Z

### Escalado
Diagonal principal: `[Sx, 0, 0, 0 / 0, Sy, 0, 0 / 0, 0, Sz, 0 / 0, 0, 0, 1]`. Centro de escala = origen.

### Sesgado (Shear)
Elementos fuera de diagonal afectan los ejes en función de los otros. Ejemplo: sesgado en X manteniendo Y fijo tiene un `0.5` en la posición [0,1].

### Reflejo/Espejo
Refleja sobre un plano. **Efecto secundario importante:** invierte la dirección de las normales de las caras de la geometría.

### Proyección plana (Ortogonal)
Anula la coordenada del eje perpendicular al plano de proyección. Proyección al plano XY: posición `[2,2]` = 0 en la diagonal.

## Matriz identidad

Todos los elementos diagonales = 1, resto = 0. Aplicarla no cambia la geometría. Es el equivalente del "neutro" para transformaciones.

## Connections

- Mapas: [[Mapa - Transformaciones]]
- [[wiki/concepts/vector-mathematics]] — las columnas de la matriz de rotación son vectores unitarios
- [[wiki/concepts/tipos-geometria-rhinocommon]] — `Transform` en RhinoCommon implementa estas matrices
- [[wiki/sources/2026-05-03-matrices-y-transformaciones]] — fuente primaria
