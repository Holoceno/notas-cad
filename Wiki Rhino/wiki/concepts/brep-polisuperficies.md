---
title: "Brep y Polisuperficies — Estructura de Datos"
type: concept
tags: [tipo/concepto, geometria/brep, software/rhinocommon]
palabras-clave: [brep, polisuperficies, topologia, faces, edges, trims, loops]
sources: [raw/rhinocommon/3 Curvas y superficies paramétricas.md, raw/rhinocommon/Chapter 3 RhinoCommon Geometry.md]
created: 2026-05-03
updated: 2026-10-13
---

El Brep (Boundary Representation) es la estructura de datos que Rhino usa para representar superficies recortadas y polisuperficies. Combina geometría (ubicaciones en 3D y 2D) con topología (conectividad entre las partes).

## Dos capas de datos

### Geometría
| Elemento | Espacio | Descripción |
|----------|---------|-------------|
| Superficies NURBS | 3D | Las superficies subyacentes sin recortar |
| Curvas 3D | 3D | Geometría de las aristas en el espacio de modelado |
| Curvas 2D | 2D (parámetros) | Geometría de los recortes en el espacio u-v |

### Topología
| Elemento | Referencia geométrica | Descripción |
|----------|----------------------|-------------|
| **Vertices** | Punto 3D | Esquinas del Brep; compartidos entre aristas adyacentes |
| **Edges** | Curva 3D | Bordes; referencian curva, 2 vértices y lista de trims |
| **Faces** | Superficie 3D | Referencian la superficie subyacente y al menos 1 loop |
| **Loops** | Cadena cerrada 2D | Bucle exterior (borde) o interior (agujero) de una cara |
| **Trims** | Curva 2D | Una curva en el espacio de parámetros por cada arista; referencia 1 edge |

## Navegación del grafo

```
Brep
 ├── Faces → [ underlying surface, loops ]
 │    └── Loops → [ trims ]
 │         └── Trims → [ edge, 2D curve ]
 │              └── Edges → [ 3D curve, start/end vertices ]
 └── Vertices → [ edge indices ]
```

Las aristas compartidas entre caras adyacentes tienen **múltiples trims** (uno por cara). Una arista con un solo trim = arista desnuda (naked edge) = borde del Brep.

## Casos especiales

- **Trim singular**: trim sin arista asociada (`trim.Edge == null`) — indica singularidad (polo de esfera, punta de cono)
- **Sólido**: Brep cerrado donde todas las aristas tienen exactamente 2 trims
- **Cara Normal vs. superficie normal**: pueden tener sentidos opuestos; la orientación se almacena en la cara

## Convención de orientación de trims

- Bucles exteriores: corren en sentido **antihorario** en el espacio 2D de parámetros
- Bucles interiores (agujeros): corren en sentido **horario**

## En RhinoCommon

```csharp
// Navegación básica
brep.Faces        // BrepFaceList
brep.Edges        // BrepEdgeList
brep.Vertices     // BrepVertexList
brep.Loops        // BrepLoopList
brep.Trims        // BrepTrimList

// Detectar aristas desnudas (naked edges)
foreach (var edge in brep.Edges)
    if (edge.TrimCount == 1) // naked edge
```

## Connections

- Mapas: [[Mapa - Brep y sólidos]] · [[Mapa - Programación]]
- [[wiki/concepts/superficies-nurbs]] — las faces del Brep son superficies NURBS (posiblemente recortadas)
- [[wiki/concepts/continuidad-geometrica]] — la continuidad entre faces determina la suavidad del Brep
- [[wiki/concepts/tipos-geometria-rhinocommon]] — `Brep` como clase en el SDK
- [[wiki/sources/2026-05-03-curvas-superficies-parametricas]] — teoría del Brep
- [[wiki/sources/2026-05-03-rhinocommon-geometry-cap3]] — implementación en C#
