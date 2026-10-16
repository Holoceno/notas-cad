---
title: "Essential Mathematics Ch.3 — Curvas y Superficies Paramétricas"
type: source
tags: [tipo/fuente, geometria/curvas, geometria/superficies, geometria/nurbs, geometria/brep]
palabras-clave: [nurbs, curvas, superficies, parametrico, continuidad, curvatura, brep]
sources: [raw/rhinocommon/3 Curvas y superficies paramétricas.md]
created: 2026-05-03
updated: 2026-10-13
---

Capítulo 3 de *Essential Mathematics for Computational Design* (McNeel). El capítulo más extenso: cubre la teoría completa de curvas y superficies NURBS que Rhino usa como representación matemática principal.

**URL original:** https://developer.rhino3d.com/guides/general/essential-mathematics/parametric-curves-surfaces/

## Temas cubiertos

**Curvas paramétricas:**
- Parámetro `t` y dominio de curva; reparametrización
- Parametrización uniforme vs no uniforme (velocidad constante vs variable)
- Vector tangente a una curva
- Curvas de Bézier cúbicas; algoritmo de De Casteljau

**NURBS — 4 atributos:**
1. **Grado**: 1=polilínea, 2=cónicas, 3/5=forma libre
2. **Puntos de control**: grado+1 puntos por segmento; ancladas pasan por extremos
3. **Pesos**: curvas racionales (círculos) vs no racionales (peso uniforme = 1)
4. **Nodos**: lista no decreciente; multiplicidad total = punto de torsión; nodos uniformes vs no uniformes; algoritmo de De Boor

**Continuidad geométrica:** G0 (posición), G1 (tangencia), G2 (curvatura)

**Curvatura:** señalada, radio de curvatura como inverso del círculo osculador

**Superficies paramétricas:** dominio u-v, plano tangente, normal de superficie

**Superficies NURBS:** red de curvas NURBS en dos direcciones, grado en u y v, singularidades, recortadas vs no recortadas

**Polisuperficies y Brep:** boundary representation, geometría + topología, sólidos = Breps cerrados

## Connections

- Mapas: [[Mapa - Curvas]] · [[Mapa - Superficies y NURBS]] · [[Mapa - Brep y sólidos]]
- [[wiki/concepts/curvas-nurbs]] — NURBS: grado, CPs, nodos, pesos
- [[wiki/concepts/continuidad-geometrica]] — G0/G1/G2
- [[wiki/concepts/curvatura]] — curvatura de curvas y superficies
- [[wiki/concepts/superficies-nurbs]] — superficies paramétricas y polisuperficies
- [[wiki/entities/essential-mathematics-computational-design]] — libro fuente

## Fuentes

- Archivo original: [[3 Curvas y superficies paramétricas]]
