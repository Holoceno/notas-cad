---
title: "Continuidad Geométrica (G0, G1, G2)"
type: concept
tags: [tipo/concepto, geometria/continuidad, geometria/curvas, geometria/superficies, geometria/nurbs]
palabras-clave: [continuidad, suavidad, curvas, superficies, tangencia, curvatura, nurbs]
sources: [raw/rhinocommon/3 Curvas y superficies paramétricas.md]
created: 2026-05-03
updated: 2026-10-13
---

La continuidad describe el grado de suavidad en la unión entre dos segmentos de curva o dos parches de superficie. Es fundamental para lograr suavidad visual, reflejos de luz correctos y flujo de aire uniforme en diseño industrial y arquitectónico.

## Niveles de continuidad

| Nivel | Nombre | Condición |
|-------|--------|-----------|
| **G0** | Posición | Los segmentos se tocan (mismo punto de unión) |
| **G1** | Tangencia | El vector tangente tiene la misma **dirección** en la unión |
| **G2** | Curvatura | Tangentes **y curvatura** coinciden en la unión |
| **GN** | Orden superior | Coincidencia hasta derivada N-ésima |

Cada nivel implica el anterior: G2 requiere G1, que requiere G0.

## Para curvas

- **G0**: los puntos finales coinciden
- **G1**: los vectores tangentes al punto de unión son paralelos (mismo ángulo, no necesariamente misma longitud)
- **G2**: además, los radios de curvatura son iguales — el "círculo osculador" es el mismo en ambos lados

### Detección en Grasshopper
```
G0: end_c1.DistanceTo(start_c2) == 0
G1: unitize(tangent_c1) · unitize(tangent_c2) == 1.0
G2: unitize(curvature_c1) · unitize(curvature_c2) == 1.0
```

## Para superficies

- **G0**: las superficies comparten borde (unidas)
- **G1**: las tangentes correspondientes a lo largo del borde son paralelas en ambas direcciones u y v
- **G2**: curvaturas y tangentes coinciden en el borde común

### Análisis en Rhino
El análisis de cebra (zebra stripes) es la herramienta visual principal: rayas continuas sin quiebre = G1 mínimo; rayas de mismo ancho y curvatura = G2.

## En NURBS: cómo lograr continuidad

- **G0**: simplemente unir los puntos extremos de los CPs
- **G1**: alinear los CPs vecinos al punto de unión (colineales)
- **G2**: controlar también la distancia de los CPs vecinos al punto de unión

Un nodo de multiplicidad total en un nodo interior rompe la continuidad a G0 (punto de torsión).

## Connections

- Mapas: [[Mapa - Curvas]] · [[Mapa - Superficies y NURBS]]
- [[wiki/concepts/curvas-nurbs]] — la estructura de nodos controla la continuidad
- [[wiki/concepts/curvatura]] — curvatura coincidente = G2
- [[wiki/concepts/superficies-nurbs]] — continuidad entre parches de superficie
- [[wiki/sources/2026-05-03-curvas-superficies-parametricas]] — fuente primaria
