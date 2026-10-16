---
title: "OpenNest 2 (nesting en Grasshopper)"
type: entity
tags: [tipo/entidad, software/grasshopper, plugin/opennest, fabricacion/nesting, fabricacion/cnc, datos/arboles]
palabras-clave: [nesting, anidado, planchas, no-fit polygon, NFP, algoritmo genético, colisión, batch, rotaciones, veta, separación, offset, Petras Vestartas]
sources: [raw/grasshopper/catalogo/Catálogo - Params.md]
created: 2026-10-13
updated: 2026-10-13
---

**OpenNest** es un plugin de Grasshopper de Petras Vestartas que acomoda piezas planas sobre planchas aprovechando el material (*nesting*), pensado para corte CNC y láser. La versión instalada (**opennest_2 2.12**) tiene núcleo en C++ y aparece en la pestaña **Params › OpenNest2** (23 componentes). Además del anidado 2D trae utilidades de fabricación: simplificar contornos, cajas orientadas, ranuras de encaje, texto para grabar, desenrollar y empaquetado 3D.

## Detalles

### Flujo básico (4 pasos)

```
Planchas ─► Sheets ──────────┐
                             ├─► OpenNest2 (u OpenNestCollision) ─► piezas ubicadas + Transforms
Piezas ──► Geometry ─────────┤
              NestOptions ───┘ (opcional)
```

1. **Planchas** con [[Catálogo - Params#Sheets|Sheets]]: polilíneas cerradas, con agujeros opcionales. *Copies* = cantidad de planchas iguales, *Offset* = **margen** interior respecto del borde. Con superficies: [[Catálogo - Params#Sheets (Surfaces) (Sheets Srf)|Sheets (Surfaces)]].
2. **Piezas** con [[Catálogo - Params#Geometry|Geometry]]: curvas cerradas o superficies planas (entrada *Outlines*, acceso árbol).
   - *Offset* = **separación entre piezas**, solo para calcular: lo que sale son las curvas **originales**.
   - *Copies* = copias por pieza.
   - *Rotations* = restricción **por pieza**: `1` deja la pieza fija (veta de la madera); vacío o `0` usa el valor global.
   - *Attributes* = geometría que acompaña a cada pieza (textos, perforaciones), una rama por pieza.
   - Variantes: [[Catálogo - Params#Geometry (Rhino) (Geometry Rhino)|Geometry (Rhino)]] (lee objetos de Rhino por capa o GUID y ordena contornos y atributos solo) y [[Catálogo - Params#Geometry (Surfaces) (Geometry Srf)|Geometry (Surfaces)]].
3. **Opciones** con [[Catálogo - Params#NestOptions|NestOptions]] → entrada *Options* del solver (ver tabla abajo).
4. **Solver** (con un *Boolean Toggle* en *Run*; ESC detiene y conserva el mejor resultado):
   - [[Catálogo - Params#OpenNest2|OpenNest2]]: *no-fit polygon* + algoritmo genético. *Iterations* típico 10–40.
   - [[Catálogo - Params#OpenNestCollision|OpenNestCollision]]: colisión física. Empaqueta más apretado y rellena cavidades. *Iterations* ~4000 para el resultado final.
   - [[Catálogo - Params#OpenNest1|OpenNest1]]: recibe curvas sin procesar (sin Geometry ni atributos), con *Spacing* directo y **sin Batch**.

**Salidas** (árbol por plancha): *Sheets*, *Borders* (contornos ubicados), *All Geo*, *Transforms* (movimiento + rotación de cada pieza), *Sheet Id*, *Sheet Txt* (número de plancha como curvas) y *Attributes*.

### Opciones (NestOptions)

| Opción | Valores | Por defecto | Para qué |
|---|---|---|---|
| Solver | -1 auto · 0 OpenNest2 · 1 Collision | -1 | Qué juego de opciones usar |
| Rotations | 1–3600 (pasos de 360/n) | 4 | Más = más apretado y más lento (prueba 8) |
| Packing | 0 Box · 1 Gravity · 2 Squeeze · 3 Bottom Left | 1 | Estrategia de ubicación |
| Seed | 0–100000 | 30 | Misma semilla = mismo resultado |
| Mutation / Population | 0–100 / 1–100000 | 10 / 10 | Algoritmo genético |
| All Rotations | 0 / 1 | 1 | Prueba todas las orientaciones (motor C++, máx. 8) |
| Element Holes | 0 / 1 | 1 | Anida piezas chicas **dentro de los agujeros** de las grandes |
| Batch | 0 / 1 | 1 | **Cada rama = un lote en su propia plancha** (ver abajo) |
| Sheet Font | "fuente tamaño" | `MecSoft_Font-1 1` | Etiqueta del número de plancha |

### Batch y data trees (lo más importante)

Con **Batch = 1** cada **rama** del árbol de *Geometry* se anida como un bloque compacto: rama 0 → plancha 0, rama 1 → plancha 1. Si hay más ramas que planchas, se reparten en ronda. Una lista plana (una sola rama) da un único anidado combinado. Con **Batch = 0** se anida todo junto en la menor cantidad de planchas, que es lo más denso.

- Agrupar con [[Catálogo - Sets#Partition List (Partition)|Partition List]] o con una ruta por mueble → cada mueble en sus planchas, fácil de armar y etiquetar.
- Piezas **con agujeros**: cada pieza (contorno + agujeros) en su propia rama; si no, el componente intenta adivinar qué polilínea es agujero de cuál.
- *Attributes*: rama *i* ↔ pieza *i*. Ver [[wiki/concepts/data-trees]].

### Herramientas de fabricación incluidas

| Componente | Qué hace | Uso típico |
|---|---|---|
| [[Catálogo - Params#Simplify\|Simplify]] | Reduce vértices (Douglas-Peucker) y agranda lo justo para que la original quede **dentro** | Acelerar el anidado de contornos con muchas curvas |
| [[Catálogo - Params#Transform Object (TGuid)\|Transform Object]] | Aplica una transformación a un objeto de Rhino **conservando sus propiedades** | Mover los originales de Rhino a su lugar en la plancha |
| [[Catálogo - Params#Text\|Text]] | Texto como curvas | Grabar nombre de pieza (láser/fresa) |
| [[Catálogo - Params#Region Slits (RSlits)\|Region Slits]] | Ranuras de encaje entre regiones planas (versión corregida de la nativa) | Muebles y maquetas encastrables |
| [[Catálogo - Params#Unroll\|Unroll]] | Desenrolla Brep o malla llevando curvas, puntos y textos | Piezas curvas a plano |
| [[Catálogo - Params#Principal Component Analysis (PCA)\|PCA]] / [[Catálogo - Params#Bounding Box Edges (BBoxEdges)\|Bounding Box Edges]] | Caja orientada mínima, plano alineado y largos | Orientar piezas, medir el material bruto |
| [[Catálogo - Params#Inscribed Circle (InscribeCircle)\|Inscribed Circle]] | Mayor círculo dentro de una polilínea | Ubicar etiquetas, revisar anchos mínimos |
| [[Catálogo - Params#Pack Objects (Pack)\|Pack Objects]] | Dispone objetos 3D en fila, orientados a 2D | Revisión rápida, plano de piezas |
| [[Catálogo - Params#OpenNest3D\|OpenNest3D]] | Empaquetado 3D de mallas en una caja (vóxeles) | Llenar la cama de la impresora 3D |
| [[Catálogo - Params#Box Packing (PackBox)\|Box Packing]] | Empaqueta cajas 3D en un contenedor | Embalaje, logística |

### Consejos para CNC (por verificar en la primera prueba)

- *Offset* de Geometry = diámetro de la fresa + holgura. La descripción dice que es la separación que mantienen las piezas: **medir en la primera prueba** que no sea el doble.
- *Offset* de Sheets = margen de sujeción o borde dañado de la plancha.
- Veta: `Rotations = 1` en las piezas que la tienen y `4` u `8` en las demás. Pueden convivir en un mismo anidado.
- Para iterar rápido: Collision con pocas iteraciones o OpenNest2 con *Iterations* bajo. Para el corte final, subir.

### Relación con el plugin de muebles CNC


### Instalación y equipos

- Instalado en el Rhino 8.35 desde el que se exportó el catálogo (Package Manager o food4Rhino).
- El núcleo es C++ nativo: en el **MacBook** verificar que la versión publicada tenga soporte para Mac antes de depender de ella.

## Conexiones

- [[wiki/concepts/data-trees]]: Batch, Attributes y agujeros dependen de la estructura de ramas
- [[wiki/entities/grasshopper]]: el resto de los plugins instalados
- [[Mapa - Fabricación]]: OpenNest junto a Biber (uniones), NGon y la teoría de CNC

## Fuentes

- [[wiki/sources/2026-10-12-catalogo-grasshopper|Catálogo exportado]], sección [[Catálogo - Params#OpenNest2|Params › OpenNest2]]: descripciones oficiales de los 23 componentes (traducidas). Las opciones, valores por defecto y el comportamiento de Batch salen textualmente de ahí.
- Los consejos de CNC son recomendaciones propias, pendientes de validar en un corte real.
