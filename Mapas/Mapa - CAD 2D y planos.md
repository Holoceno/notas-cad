---
tags: [tipo/mapa, fabricacion/planos, software/cadquery, software/cadcraft, rhino/anotaciones, tipo/indice]
---

# CAD 2D y planos

↑ [[Inicio]]

Planos para fabricar o presentar: vistas 2D, cotas, limpieza de dibujos y formatos DXF/PDF. Herramientas: Rhino (Make2D, cotas), CadQuery (exportar caras a DXF), CADCraft (CAD 2D libre, controlable vía MCP) y el flujo tipo AutoCAD.

- [[Aprendizaje/CadQuery/CadQuery a CADCraft (planos 2D)]]: CadQuery → DXF → CADCraft → PDF
- [[Aprendizaje/Algoritmos/OVERKILL (CADCraft)]] · overkill-rhino: limpiar líneas duplicadas y superpuestas
- [[Mapa - Visualización y anotaciones]]: cotas, textos, hatches y Make2D en Grasshopper
- [[wiki/concepts/rhinocommon-anotaciones-api]]: cotas y textos por código
- Láminas por código: muestras **Add Layout** y **Set RhinoPageView Width and Height** (tabla de abajo)
- [[wiki/entities/rhino3dm]]: escribir `.3dm` con capas desde Python, sin Rhino (alternativa al DXF)
- [[Mapa - Fabricación]]: los planos como entrada al CNC

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (14)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Annotation Text | [[Add Annotation Text\|Py]] · [[Add Annotation Text (cs)\|C#]] | Agrega un texto en un punto del plano de construcción | `doc.Objects.AddText(texto, plano, altura, fuente, ...)` |
| Add Layout | [[Add Layout (cs)\|C#]] | Crea un layout A0 con una ventana de detalle a escala | `doc.Views.AddPageView, AddDetailView, DetailGeometry.SetScale` |
| Add Leader | [[Add Leader\|Py]] · [[Add Leader (cs)\|C#]] | Agrega una directriz desde una lista de puntos | `rs.AddLeader(puntos)` |
| Add Linear Dimension | [[Add Linear Dimension\|Py]] · [[Add Linear Dimension (cs)\|C#]] | Agrega una cota lineal pidiéndola al usuario | `RhinoGet.GetLinearDimension → doc.Objects.AddLinearDimension` |
| Add Linear Dimension2 | [[Add Linear Dimension2 (py)\|Py]] · [[Add Linear Dimension2 (cs)\|C#]] | Cota lineal desde dos puntos y la posición de la línea de cota | `LinearDimension(plano, ext1, ext2, ptLinea)` |
| Add Radial Dimension | [[Add Radial Dimension (py)\|Py]] · [[Add Radial Dimension (cs)\|C#]] | Agrega una cota de radio a una curva | `Curve.CurvatureAt → RadialDimension → doc.Objects.AddRadialDimension` |
| Change Dimension Style | [[Change Dimension Style\|Py]] · [[Change Dimension Style (cs)\|C#]] | Aplica el estilo de cota actual a todas las anotaciones | `doc.DimStyles.CurrentDimensionStyleIndex → CommitChanges` |
| Edit Text | [[Edit Text\|Py]] · [[Edit Text (cs)\|C#]] | Cambia el contenido de un texto | `TextObject.Geometry.Text → CommitChanges` |
| Explode Hatch | [[Explode Hatch\|Py]] · [[Explode Hatch (cs)\|C#]] | Explota un sombreado en sus curvas y superficies | `Hatch.Explode()` |
| Hatch Curve | [[Hatch Curve\|Py]] · [[Hatch Curve (cs)\|C#]] | Crea un sombreado dentro de una curva cerrada y plana | `Hatch.Create(curva, patron, rotacion, escala)` |
| Read Dimension Text | [[Read Dimension Text (cs)\|C#]] | Lee el texto que muestra una cota | `AnnotationObjectBase.DisplayText` |
| Replace Hatch Pattern | [[Replace Hatch Pattern\|Py]] · [[Replace Hatch Pattern (cs)\|C#]] | Cambia el patrón de los sombreados seleccionados | `HatchGeometry.PatternIndex → CommitChanges` |
| Set RhinoPageView Width and Height | [[Set RhinoPageView Width and Height (cs)\|C#]] | Cambia el tamaño de la hoja de un layout | `RhinoPageView.PageWidth / PageHeight` |
| Text Justify | [[Text Justify\|Py]] · [[Text Justify (cs)\|C#]] | Texto centrado con una fuente dada | `TextEntity.Justification, doc.Fonts.FindOrCreate` |

<!-- AUTO:fin -->
