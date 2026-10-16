---
title: "Curvatura (Curvas y Superficies)"
type: concept
tags: [tipo/concepto, geometria/curvatura, geometria/superficies, geometria/nurbs]
palabras-clave: [curvatura, gaussiana, media, principal, nurbs, analisis-de-forma]
sources: [raw/rhinocommon/3 Curvas y superficies paramétricas.md]
created: 2026-05-03
updated: 2026-10-13
---

La curvatura mide el cambio en la inclinación tangente de una curva o superficie por unidad de longitud. Es la herramienta analítica fundamental para evaluar la calidad de forma en modelado 3D.

## Curvatura de curvas

En cualquier punto de una curva, la curvatura `κ` es la inversa del radio del **círculo osculador** (el círculo que mejor aproxima la curva en ese punto):

```
κ = 1 / radio_osculador
```

- Para un círculo: curvatura constante = 1/R
- Para una línea: curvatura = 0
- La curvatura **señalada** distingue por qué lado está el círculo: positiva (izquierda) o negativa (derecha)

Los valores de curvatura en los puntos de unión entre curvas determinan la continuidad: igual curvatura señalada = G2.

## Curvatura de superficies

### Curvatura normal
En un punto de la superficie, para cada dirección del plano tangente existe una curvatura normal (la curvatura de la curva que se forma al cortar la superficie con un plano vertical en esa dirección).

### Curvaturas principales (k1, k2)
El **mínimo** y el **máximo** de todas las curvaturas normales en un punto. Las direcciones correspondientes son perpendiculares entre sí.

### Curvatura Gaussiana = k1 × k2
Producto de las dos curvaturas principales:

| Signo | Forma local | Ejemplo |
|-------|-------------|---------|
| **Positiva** | Cuenco (bowl) — el plano tangente toca la superficie en un solo punto | Esfera, domo |
| **Negativa** | Silla de montar — el plano tangente corta la superficie | Punto de silla, hiperboloide |
| **Cero** | Al menos una dirección es recta | Plano, cilindro, cono |

La curvatura gaussiana es invariante bajo doblado isométrico (una hoja de papel doblada mantiene curvatura gaussiana 0).

### Curvatura Media = (k1 + k2) / 2
- **Cero en todas partes**: superficie mínima (mínima área para su contorno) — ejemplo: película de jabón
- **Constante en todas partes**: superficie CMC (curvatura media constante) — ejemplo: burbuja de jabón

## Análisis en Rhino

- **Gráfico de curvatura de curvas**: "peine" de vectores perpendiculares proporcionales a la curvatura
- **Análisis de curvatura gaussiana**: mapa de colores sobre la superficie (útil para identificar puntos de silla o zonas planas no deseadas)
- **Análisis de curvatura media**: identifica zonas de cambio brusco en la forma

## Connections

- Mapas: [[Mapa - Superficies y NURBS]]
- [[wiki/concepts/continuidad-geometrica]] — G2 requiere curvatura coincidente
- [[wiki/concepts/curvas-nurbs]] — curvatura como atributo de las curvas NURBS
- [[wiki/concepts/superficies-nurbs]] — curvatura principal y gaussiana en superficies
- [[wiki/sources/2026-05-03-curvas-superficies-parametricas]] — fuente primaria
