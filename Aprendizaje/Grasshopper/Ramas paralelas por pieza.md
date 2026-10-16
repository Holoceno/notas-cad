---
tags: [tipo/apunte, datos/arboles, datos/texto, software/grasshopper, fabricacion/nesting]
palabras-clave: [data tree, ruta, path, Replace Paths, Path Mapper, Construct Path, Unflatten Tree, Duplicate Data, Member Index, rótulos]
---

# Ramas paralelas por pieza

**Una pieza = una ruta.** Si el contorno, el rótulo, el pliegue y los flocks de cada pieza viven en árboles distintos pero con la **misma ruta**, se pueden reordenar todos a la vez (por color, por placa) sin perder qué va con qué. Es lo que permite hornear cada tipo en su capa y seguir sabiendo a qué pieza pertenece.

## La ruta como dirección
| Etapa | Ruta | Significa |
|---|---|---|
| Geometría | `{tipo;fila;pieza}` | tipo A=0 / B=1, fila dentro del tipo, pieza este=0 / oeste=1 |
| Por color | `{color;línea;pieza}` | línea global de abajo hacia arriba = `2·fila + tipo` |
| En placa | `{color;placa;línea;pieza}` | resultado del nesting |

## Componentes que lo hacen posible
- **Path Mapper** `{a;b;c;d;e;f;g} → {a;b;c}`: limpiar rutas largas para que todos los árboles hablen igual.
- **Tree Statistics** (rutas) → **Deconstruct Path** → **List Item** 0/1/2: sacar tipo, fila y pieza como números.
- **Format** `L1-{0}{1}`: rótulo con letra (`List Item` sobre `B, A, D, C` con índice `2·tipo + pieza`) y número.
- **Duplicate Data** con *Graft* en las dos entradas: expandir un patrón "3 Mármol, 1 Bruma, 6 Mármol…" a una lista por línea. Sin graft duplica la lista entera por cada número.
- **Member Index**: nombre de color → índice de rama.
- **Merge** (entradas con Graft) + **Construct Path**: armar la ruta nueva `{color;línea;pieza}`.
- **Replace Paths** (buscar = rutas viejas, reemplazar = rutas nuevas): aplicar el mismo cambio a los 4 árboles.
- **Unflatten Tree** con guía: devolver una lista plana (los rótulos) a la forma del árbol de piezas.

## Errores típicos
- **Entwine** aplana las ramas: para juntar árboles A y B sin chocar, mejor *Path Mapper* (`{0;…}` y `{1;…}`) + *Merge*.
- Una lista plana contra un árbol de muchas ramas: Grasshopper usa el **primer** elemento en cada rama. Siempre llevar la lista a la forma del árbol.
- *Stream Filter* elige para todo el árbol; para elegir por pieza, *Pick'n'Choose*.

## Conexiones
- Mapas: [[Mapa - Data trees y listas]] · [[Mapa - Fabricación]]
- [[wiki/concepts/data-trees]]
- Uso real: [[Nesting por franjas]]
