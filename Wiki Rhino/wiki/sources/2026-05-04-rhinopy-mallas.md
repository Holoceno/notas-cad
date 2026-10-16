---
title: "RhinoCommon Samples — Mallas (rhinopy)"
type: source
tags: [tipo/fuente, software/rhinocommon, lenguaje/python, geometria/mallas]
palabras-clave: [rhinopython, mallas, mesh, vertices, faces, display]
sources: [raw/rhinopy/Add Mesh.md, raw/rhinopy/Draw Mesh.md, raw/rhinopy/Create Mesh from Brep.md, raw/rhinopy/Duplicate Mesh Boundary.md]
created: 2026-05-04
updated: 2026-10-13
---

4 samples de RhinoCommon sobre construcción, visualización y extracción de bordes de mallas poligonales.

## Add Mesh — construcción desde cero

```python
import Rhino, scriptcontext

mesh = Rhino.Geometry.Mesh()

# Vértices (Point3f — precisión simple)
mesh.Vertices.Add(0.0, 0.0, 1.0)  # índice 0
mesh.Vertices.Add(1.0, 0.0, 1.0)  # índice 1
mesh.Vertices.Add(2.0, 0.0, 1.0)  # índice 2
# ...

# Caras cuadrilaterales (4 índices) o triangulares (3 índices)
mesh.Faces.AddFace(0, 1, 5, 4)
mesh.Faces.AddFace(1, 2, 6, 5)

# Post-proceso
mesh.Normals.ComputeNormals()
mesh.Compact()  # liberar memoria no usada

if scriptcontext.doc.Objects.AddMesh(mesh) != System.Guid.Empty:
    scriptcontext.doc.Views.Redraw()
```

## Draw Mesh — Display Conduit

Crea malla desde esfera y la dibuja en viewport via conduit:

```python
mesh = Rhino.Geometry.Mesh.CreateFromSphere(sphere, uCount=10, vCount=10)

class MeshConduit(Rhino.Display.DisplayConduit):
    def DrawOverlay(self, e):
        e.Display.DrawMeshShaded(self.mesh, material)
        e.Display.DrawMeshWires(self.mesh, System.Drawing.Color.Black)

conduit = MeshConduit()
conduit.mesh = mesh
conduit.Enabled = True
# ... interacción con usuario ...
conduit.Enabled = False
```

## Create Mesh from Brep

```python
brep = obj_ref.Brep()
meshes = Rhino.Geometry.Mesh.CreateFromBrep(brep, Rhino.Geometry.MeshingParameters.Default)
joined = Rhino.Geometry.Mesh()
for m in meshes:
    joined.Append(m)
scriptcontext.doc.Objects.AddMesh(joined)
```

## Duplicate Mesh Boundary

Extrae bordes desnudos (aristas sin cara adyacente) de una malla abierta:

```python
mesh = obj_ref.Mesh()
naked_edges = mesh.GetNakedEdges()  # retorna Polyline[]
for polyline in naked_edges:
    scriptcontext.doc.Objects.AddPolyline(polyline)
```

## Conexiones

- Mapas: [[Mapa - Mallas y SubD]] · [[Mapa - Programación]]
- [[wiki/concepts/rhinocommon-mesh-api]] — API de mallas detallada
- [[wiki/concepts/tipos-geometria-rhinocommon]] — Mesh en la jerarquía GeometryBase
- [[wiki/concepts/brep-polisuperficies]] — relación Brep ↔ Mesh
- [[wiki/entities/rhinocommon]] — SDK fuente

## Fuentes

Archivos originales de cada muestra (Python y C#; las muestras también están en su mapa):

- Add Mesh: [[Add Mesh|Python]] · [[Add Mesh (cs)|C#]]
- Draw Mesh: [[Draw Mesh|Python]] · [[Draw Mesh (cs)|C#]]
- Create Mesh from Brep: [[Create Mesh from Brep|Python]] · [[Create Mesh from Brep (cs)|C#]]
- Duplicate Mesh Boundary: [[Duplicate Mesh Boundary|Python]] · [[Duplicate Mesh Boundary (cs)|C#]]
