---
title: "Essential Mathematics Ch.2 — Matrices y Transformaciones"
type: source
tags: [tipo/fuente, matematicas/matrices, geometria/transformaciones]
palabras-clave: [matrices, transformaciones, geometria-computacional]
sources: [raw/rhinocommon/2 Matrices y transformaciones.md]
created: 2026-05-03
updated: 2026-10-13
---

Capítulo 2 de *Essential Mathematics for Computational Design* (McNeel). Cubre la representación matricial de transformaciones geométricas en programación 3D.

**URL original:** https://developer.rhino3d.com/guides/general/essential-mathematics/matrices-transformations/

## Temas cubiertos

- Por qué matrices 4×4: coordenadas homogéneas permiten representar todas las transformaciones (incluyendo traslación) en un formato unificado
- Multiplicación de matrices: eficiencia de combinar transformaciones antes de aplicarlas a miles de puntos
- Matriz identidad
- Las 6 transformaciones fundamentales:
  - **Traslación**: columna derecha `[a1, a2, a3]`
  - **Rotación**: matrices para eje X, Y y Z usando seno/coseno
  - **Escalado**: diagonal `[Sx, Sy, Sz, 1]`
  - **Sesgado (Shear)**: elementos fuera de diagonal
  - **Reflejo/Espejo**: invierte la dirección normal de caras
  - **Proyección plana**: anula una coordenada (proyección ortogonal)

## Connections

- Mapas: [[Mapa - Transformaciones]]
- [[wiki/concepts/transformaciones-geometricas]] — síntesis de los conceptos de este capítulo
- [[wiki/entities/essential-mathematics-computational-design]] — libro fuente
- [[wiki/entities/rhinocommon]] — SDK donde `Rhino.Geometry.Transform` implementa estas matrices

## Fuentes

- Archivo original: [[2 Matrices y transformaciones]]
