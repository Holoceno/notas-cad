---
title: "Superficies NURBS y Polisuperficies"
type: concept
tags: [tipo/concepto, geometria/superficies, geometria/nurbs, geometria/brep]
palabras-clave: [nurbs, superficies, parametrico, brep, polisuperficies, recortadas, singularidad]
sources: [raw/rhinocommon/3 Curvas y superficies paramétricas.md]
created: 2026-05-03
updated: 2026-10-13
---

Las superficies NURBS son la extensión de las curvas NURBS a dos dimensiones. Rhino las usa como representación principal de superficies de forma libre, junto con la estructura Brep para polisuperficies.

## Superficie paramétrica

Una superficie paramétrica mapea dos parámetros independientes `(u, v)` a un punto `(x, y, z)`:

```
x = x(u, v)
y = y(u, v)
z = z(u, v)
```

El dominio es un rectángulo `[u_min, u_max] × [v_min, v_max]`. Calcular en el centro del dominio no produce necesariamente el punto central en 3D.

## Superficie NURBS

Una red de curvas NURBS en dos direcciones. Tiene todos los atributos de las curvas NURBS (grado, CPs, pesos, nodos) pero **en cada dirección u y v por separado**.

- Puntos de control: grilla rectangular
- Grado en u y en v pueden ser distintos
- La reparametrización no cambia la forma 3D
- El plano tangente en un punto está definido por las derivadas parciales respecto a u y v

## Superficies recortadas vs. no recortadas

**No recortada**: el borde de la superficie coincide exactamente con el borde del rectángulo de parámetros subyacente.

**Recortada (trimmed)**: la superficie NURBS subyacente existe completa, pero se define una región activa mediante curvas de recorte 2D (en espacio de parámetros). Estas se proyectan como bordes 3D.
- Bucle exterior: define el borde exterior
- Bucles interiores: definen agujeros

## Singularidades

Ocurren cuando un borde del rectángulo de parámetros se contrae a un punto. Ejemplo: el polo de una esfera o la punta de un cono. Las isocurvas convergen en ese punto. Se pueden evitar usando superficies recortadas en su lugar.

## Polisuperficies y Brep (Boundary Representation)

Cuando dos o más superficies se unen por bordes comunes, forman una **polisuperficie** representada como **Brep**.

### Datos del Brep
**Geometría:**
- Superficies NURBS subyacentes (sin recortar)
- Curvas 3D: geometría de las aristas
- Curvas 2D: geometría de los recortes en espacio de parámetros

**Topología** (conectividad):
- **Faces**: referencian la superficie 3D subyacente + loops
- **Edges**: referencian la curva 3D + vertices extremos + trims
- **Vertices**: puntos de esquina compartidos entre aristas
- **Loops**: cadenas cerradas de trims (exterior/interior)
- **Trims**: curvas 2D en el espacio de parámetros que referencian una arista

Un **sólido** es un Brep cerrado (hermético). Las caras adyacentes comparten aristas y vértices.

### Riesgo de edición de polisuperficies
Modificar una cara puede crear huecos si los bordes compartidos no se mantienen coincidentes dentro de la tolerancia del modelo.

## Connections

- Mapas: [[Mapa - Superficies y NURBS]] · [[Mapa - Brep y sólidos]]
- [[wiki/concepts/curvas-nurbs]] — las isocurvas de la superficie son curvas NURBS
- [[wiki/concepts/continuidad-geometrica]] — continuidad entre parches de superficie
- [[wiki/concepts/curvatura]] — curvatura gaussiana y media de superficies
- [[wiki/concepts/brep-polisuperficies]] — estructura de datos del Brep en detalle
- [[wiki/sources/2026-05-03-curvas-superficies-parametricas]] — fuente primaria
