---
title: "Object Selection with Options"
type: source
tags: [tipo/fuente, software/rhinocommon, rhino/seleccion]
palabras-clave: [selection, getobject, command-options, workflow]
sources: [raw/rhinocommon/Object Selection with Options.md]
created: 2026-05-03
updated: 2026-10-13
---

Guide from Robert McNeel & Associates on how to build Rhino commands that let the user pick objects, adjust command-line options, and keep picking — all maintaining a coherent selection set throughout.

**Original URL:** https://developer.rhino3d.com/guides/rhinocommon/object-selection-options/

## Key Takeaways

- `GetObject` manages the full lifecycle of interactive selection in a Rhino command
- Pre-selected objects (before the command starts) and post-selected objects (picked during the command) must be reconciled manually to keep the viewport state consistent
- The `for(;;)` loop is the canonical pattern: branch on `GetResult.Option` (re-enter loop) vs `GetResult.Object` (break) vs anything else (cancel)
- After a user clicks a command-line option, `EnablePreSelect(false, true)` must be called to avoid a false early exit from `GetMultiple`
- Geometry filtering uses `ObjectType` bitflags — combinable with `|` to accept multiple geometry types

## Key Properties & Methods

| Member | Purpose |
|--------|---------|
| `EnableClearObjectsOnEntry(false)` | Preserves the selection set when re-entering the loop |
| `EnableUnselectObjectsOnExit(false)` | Keeps objects highlighted after loop exits |
| `DeselectAllBeforePostSelect = false` | Prevents wiping pre-selected objects on post-select |
| `EnablePreSelect(false, true)` | Disables pre-selection after an option is clicked |
| `go.ObjectsWerePreselected` | Detects the mixed pre/post case |

## Connections

- Mapas: [[Mapa - Documento de Rhino]] · [[Mapa - Programación]]
- [[wiki/concepts/interactive-object-selection]] — workflow pattern this guide implements
- [[wiki/entities/rhinocommon]] — SDK this guide belongs to

## Fuentes

- Archivo original: [[Object Selection with Options]]
