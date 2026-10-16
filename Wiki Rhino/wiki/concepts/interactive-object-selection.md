---
title: "Interactive Object Selection (Rhino)"
type: concept
tags: [tipo/concepto, software/rhinocommon, rhino/seleccion, programacion/interfaz]
palabras-clave: [selection, workflow, ux, command-design]
sources: [raw/rhinocommon/Object Selection with Options.md]
created: 2026-05-03
updated: 2026-10-13
---

In Rhino, interactive object selection is the mechanism by which a command asks the user to pick geometry from the viewport, optionally adjusting command parameters mid-selection. The challenge is that Rhino distinguishes between objects already selected when the command launches (pre-selected) and objects picked after the command starts (post-selected), and both must coexist cleanly.

## The Selection Loop

The standard pattern is a `for(;;)` loop driven by `GetObject.GetMultiple()`:

- `GetResult.Option` → user clicked a command-line option; update settings and continue
- `GetResult.Object` → user finished picking; break and proceed
- anything else → cancel

This loop allows seamless interleaving of picking and option adjustment without restarting the selection state.

## Pre-selection vs Post-selection

Rhino commands conventionally leave pre-selected objects highlighted at the end. Post-selected objects are normally deselected on exit. When both happen in the same command, the selections must be manually reconciled — typically by deselecting everything before exiting to ensure visual consistency.

## Geometry Filtering

Commands can restrict what types of objects are pickable using `ObjectType` flags:

```
ObjectType.Surface | ObjectType.PolysrfFilter | ObjectType.Mesh
```

This is a design decision about command scope — narrow filters improve precision, wide filters improve flexibility.

## Connections

- Mapas: [[Mapa - Documento de Rhino]] · [[Mapa - Scripts, interfaz y archivos]] · [[Mapa - Programación]]
- [[wiki/entities/rhinocommon]] — the SDK that implements this pattern
- [[wiki/sources/2026-05-03-object-selection-with-options]] — primary source
