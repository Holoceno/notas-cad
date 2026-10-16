---
tags: [tipo/apunte, software/cadquery, software/cadcraft, fabricacion/planos]
---

# CadQuery → CADCraft (planos 2D)

CADCraft: AutoCAD libre (ArtCraft), solo 2D, **pre-alfa** — no usar para entregas a clientes todavía.

## Flujo
1. CadQuery exporta la cara/vista a DXF: `cq.exporters.export(pieza.faces("<Z"), "pieza.dxf")`
2. CADCraft acota y exporta a PDF (a mano, o un asistente vía MCP / `cadcraft-cli`).

## Ojo: unidades
Por defecto el estilo de cota está en pulgadas → números diminutos. Antes de acotar:
- `units {"lunits":2,"luprec":0,"insunits":4}` (decimal, mm)
- `dimstyle {"name":"MM","current":true,"DIMTXT":3.5,"DIMASZ":3,"DIMDEC":0,"DIMTAD":1}`

Ejemplo: `~/proyectos/cad-python/salida/panel_acotado.pdf`
Ver: [[CadQuery vs RhinoCommon]]
