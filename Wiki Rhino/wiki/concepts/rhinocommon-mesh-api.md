---
title: "RhinoCommon — API de Mallas"
type: concept
tags: [tipo/concepto, software/rhinocommon, lenguaje/python, geometria/mallas]
palabras-clave: [rhinopython, mallas, mesh, vertices, faces, normales, display]
sources: [raw/rhinopy/Add Mesh.md, raw/rhinopy/Draw Mesh.md, raw/rhinopy/Create Mesh from Brep.md, raw/rhinopy/Duplicate Mesh Boundary.md]
created: 2026-05-04
updated: 2026-10-13
---

`Rhino.Geometry.Mesh` es la clase de malla poligonal de RhinoCommon. No es paramétrica: se define directamente por vértices indexados y caras (triángulos o cuadriláteros).

## Construcción desde cero

```python
import Rhino, scriptcontext

mesh = Rhino.Geometry.Mesh()

# 1. Vértices — Point3f (precisión simple, diferente a Point3d)
mesh.Vertices.Add(0.0, 0.0, 0.0)   # índice 0
mesh.Vertices.Add(1.0, 0.0, 0.0)   # índice 1
mesh.Vertices.Add(1.0, 1.0, 0.0)   # índice 2
mesh.Vertices.Add(0.0, 1.0, 0.0)   # índice 3

# 2. Caras por índice de vértice
mesh.Faces.AddFace(0, 1, 2, 3)     # cuadrilateral
mesh.Faces.AddFace(0, 1, 2)        # triángulo (3 índices)

# 3. Calcular normales automáticamente
mesh.Normals.ComputeNormals()

# 4. Liberar huecos internos
mesh.Compact()

scriptcontext.doc.Objects.AddMesh(mesh)
scriptcontext.doc.Views.Redraw()
```

## Construcción desde geometría existente

```python
# Desde Brep
params = Rhino.Geometry.MeshingParameters.Default
meshes = Rhino.Geometry.Mesh.CreateFromBrep(brep, params)
joined = Rhino.Geometry.Mesh()
for m in meshes:
    joined.Append(m)

# Desde primitivas
sphere_mesh = Rhino.Geometry.Mesh.CreateFromSphere(sphere, uCount=10, vCount=10)
```

## Propiedades y consulta

| Propiedad/Método | Descripción |
|-----------------|-------------|
| `mesh.Vertices` | colección de `Point3f` |
| `mesh.Faces` | colección de `MeshFace` (v0, v1, v2[, v3]) |
| `mesh.Normals` | normales por vértice |
| `mesh.FaceNormals` | normales por cara |
| `mesh.TopologyEdges` | aristas con conectividad |
| `mesh.GetNakedEdges()` | aristas sin cara adyacente → `Polyline[]` |
| `mesh.IsValid` | valida la malla |
| `mesh.IsClosed` | True si no tiene bordes desnudos |

## Display Conduit — visualización sin añadir al doc

```python
class MeshConduit(Rhino.Display.DisplayConduit):
    def DrawOverlay(self, e):
        if self.mesh:
            material = Rhino.Display.DisplayMaterial(System.Drawing.Color.Blue)
            e.Display.DrawMeshShaded(self.mesh, material)
            e.Display.DrawMeshWires(self.mesh, System.Drawing.Color.Black)

conduit = MeshConduit()
conduit.mesh = my_mesh
conduit.Enabled = True   # activar: subscribe a eventos de drawing
# ... interacción con usuario ...
conduit.Enabled = False  # desactivar
```

## Diferencias clave con NurbsSurface

| Aspecto | Mesh | NurbsSurface |
|---------|------|-------------|
| Representación | Vértices + faces discretas | Ecuación paramétrica continua |
| Precisión | Aproximada (depende de densidad) | Exacta matemáticamente |
| Render | Directo (GPU triangle lists) | Requiere tesselación previa |
| Edición | Por vértice | Por puntos de control |
| Conversión | `NurbsSurface` → `Mesh` (tesselación) | No directo |

## Conexiones

- Mapas: [[Mapa - Mallas y SubD]] · [[Mapa - Programación]]
- [[wiki/sources/2026-05-04-rhinopy-mallas]] — samples de mallas
- [[wiki/concepts/tipos-geometria-rhinocommon]] — Mesh en jerarquía GeometryBase
- [[wiki/concepts/brep-polisuperficies]] — relación Brep ↔ Mesh
- [[wiki/concepts/rhinocommon-document-api]] — doc.Objects.AddMesh
- [[wiki/entities/rhinocommon]] — SDK fuente
