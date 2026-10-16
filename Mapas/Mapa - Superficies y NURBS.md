---
tags: [tipo/mapa, geometria/superficies, geometria/nurbs, software/grasshopper, software/rhinocommon, software/cadquery]
---

# Superficies y NURBS

↑ [[Mapa - Grasshopper|Todos los mapas]] · [[Inicio]]

Superficies de forma libre (loft, sweep, network) y su análisis en el dominio u-v. Una superficie es una "hoja" con parámetros (u, v); cuando se recorta o se une con otras pasa a ser un [[Mapa - Brep y sólidos|Brep]].

## Teoría y código
- [[wiki/concepts/superficies-nurbs]]: dominio u-v, recortadas, singularidades
- [[wiki/concepts/continuidad-geometrica]] · [[wiki/concepts/curvatura]] (gaussiana y media)
- [[wiki/sources/2026-05-03-curvas-superficies-parametricas]] · [[wiki/sources/2026-05-04-rhinopy-superficies]]

## Equivalencias

> En C# se usa el mismo método de RhinoCommon con otra sintaxis: [[wiki/concepts/python-csharp-rhinocommon|Python ↔ C#]]. Ejemplos oficiales en los dos lenguajes: tabla **Muestras de RhinoCommon**, más abajo.

| Tarea | Grasshopper | RhinoCommon (Python) | CadQuery |
|---|---|---|---|
| Loft | [[Catálogo - Surface#Loft\|Loft]] | `rg.Brep.CreateFromLoft(curvas, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)` | `.loft()` |
| Barrido por un riel | [[Catálogo - Surface#Sweep1 (Swp1)\|Sweep1]] | `rg.Brep.CreateFromSweep(riel, perfil, False, tol)` | `.sweep(camino)` |
| Extruir | [[Catálogo - Surface#Extrude (Extr)\|Extrude]] | `rg.Extrusion.Create(crv_plana, altura, True)` | `.extrude(h)` |
| Revolución | [[Catálogo - Surface#Revolution (RevSrf)\|Revolution]] | `rg.RevSurface.Create(perfil, eje)` | `.revolve(grados)` |
| Cara plana con agujeros | [[Catálogo - Surface#Boundary Surfaces (Boundary)\|Boundary Surfaces]] | `rg.Brep.CreatePlanarBreps(curvas, tol)` | `cq.Face.makeFromWires(borde, huecos)` |
| Punto y normal en (u, v) | [[Catálogo - Surface#Evaluate Surface (EvalSrf)\|Evaluate Surface]] | `srf.PointAt(u, v)`, `srf.NormalAt(u, v)` | `face.positionAt(u, v)`, `face.normalAt()` |
| Punto más cercano | [[Catálogo - Surface#Surface Closest Point (Srf CP)\|Surface Closest Point]] | `ok, u, v = srf.ClosestPoint(pt)` | — |
| Isocurva | [[Catálogo - Curve#Iso Curve (Iso)\|Iso Curve]] | `srf.IsoCurve(direccion, parametro)` | — |
| Offset | [[Catálogo - Surface#Offset Surface (Offset)\|Offset Surface]] | `srf.Offset(d, tol)` | — |

## Para empezar
[[Catálogo - Surface#Loft|Loft]] · [[Catálogo - Surface#Sweep1 (Swp1)|Sweep1]] · [[Catálogo - Surface#Sweep2 (Swp2)|Sweep2]] · [[Catálogo - Surface#Network Surface (NetSurf)|Network Surface]] · [[Catálogo - Surface#Divide Surface (SDivide)|Divide Surface]] · [[Catálogo - Surface#Surface Frames (SFrames)|Surface Frames]] · [[Catálogo - Surface#Isotrim (SubSrf)|Isotrim]] · [[Catálogo - Surface#Surface Curvature (Curvature)|Surface Curvature]] · plugins: LunchBox (superficies matemáticas), Pufferfish

<!-- AUTO:inicio -->

## Muestras de RhinoCommon (20)

> Ejemplos oficiales de McNeel, el mismo en **Python** y en **C#** para comparar línea a línea ([[wiki/sources/2026-10-13-muestras-rhinocommon-python-csharp|cómo leerlas]]). Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde `muestras_rhinocommon.json`.

| Muestra | Código | Qué hace | Mirar en RhinoCommon |
|---|---|---|---|
| Add Truncated Cone | [[Add Truncated Cone\|Py]] · [[Add Truncated Cone (cs)\|C#]] | Cono truncado por revolución entre dos círculos | `RevSurface.Create(perfil, eje) → Brep.CreateFromRevSurface` |
| Array Points on Surface | [[Array Points on Surface\|Py]] | Grilla de puntos sobre una superficie (filas × columnas) | `rs.SurfaceDomain, rs.EvaluateSurface` |
| Calculate Surface Curvature | [[Calculate Surface Curvature\|Py]] · [[Calculate Surface Curvature (cs)\|C#]] | Curvaturas principales, gaussiana y media en un punto | `rs.SurfaceCurvature(id, (u, v)) → Surface.CurvatureAt` |
| Create Surface From Points and Knots | [[Create Surface From Points and Knots\|Py]] · [[Create Surface From Points and Knots (cs)\|C#]] | Superficie NURBS desde cero: puntos de control y vectores de nodos | `NurbsSurface.Create, KnotsU / KnotsV, Points.SetControlPoint` |
| Determine Normal Direction of Brep Face | [[Determine Normal Direction of Brep Face\|Py]] · [[Determine Normal Direction of Brep Face (cs)\|C#]] | Normal de una cara en un punto, considerando si está invertida | `BrepFace.ClosestPoint → NormalAt(u, v), OrientationIsReversed` |
| Duplicate Surface Border | [[Duplicate Surface Border\|Py]] · [[Duplicate Surface Border (cs)\|C#]] | Borde de una superficie o polisuperficie como curvas | `Brep.DuplicateEdgeCurves(True) → Curve.JoinCurves` |
| Extend Surface | [[Extend Surface\|Py]] · [[Extend Surface (cs)\|C#]] | Extiende un borde de una superficie | `Surface.Extend(IsoStatus, largo, suave)` |
| Extract Isocurve | [[Extract Isocurve\|Py]] · [[Extract Isocurve (cs)\|C#]] | Extrae una isocurva U o V en un punto | `Surface.IsoCurve(direccion, parametro)` |
| Furthest Z on Surface given X Y | [[Furthest Z on Surface given X Y\|Py]] · [[Furthest Z on Surface given X Y (cs)\|C#]] | Z más alta de una superficie en una posición X, Y | `Intersection.ProjectPointsToBreps(breps, pts, dir, tol)` |
| Increase NURBS Surface Degree | [[Increase NURBS Surface Degree\|Py]] · [[Increase NURBS Surface Degree (cs)\|C#]] | Sube el grado U y V de una superficie NURBS | `ToNurbsSurface().IncreaseDegreeU / IncreaseDegreeV` |
| Is Planar Surface in Plane | [[Is Planar Surface in Plane\|Py]] · [[Is Planar Surface in Plane (cs)\|C#]] | Comprueba si una superficie plana está en un plano dado | `Surface.IsPlanar, BoundingBox.GetCorners, Plane.DistanceTo` |
| Loft Surfaces | [[Loft Surfaces\|Py]] · [[Loft Surfaces (cs)\|C#]] | Superficie de transición (loft) entre curvas | `rs.AddLoftSrf → Brep.CreateFromLoft` |
| Move Grip Objects | [[Move Grip Objects (cs)\|C#]] | Mueve los puntos de control de una superficie según su normal | `RhinoObject.GetGrips → GripObject.Move → doc.Objects.GripUpdate` |
| Orient On Surface | [[Orient On Surface\|Py]] · [[Orient On Surface (cs)\|C#]] | Orienta objetos sobre una superficie según su normal | `Surface.FrameAt(u, v) → Transform.PlaneToPlane` |
| Planar Surface | [[Planar Surface\|Py]] · [[Planar Surface (cs)\|C#]] | Superficie plana desde un rectángulo | `RhinoGet.GetRectangle → PlaneSurface(plano, intervaloU, intervaloV)` |
| Show Surface Direction | [[Show Surface Direction (cs)\|C#]] | Muestra las normales de una superficie con flechas (conduit) | `BrepFace.NormalAt → e.Display.DrawDirectionArrow` |
| Surface from Corner Points | [[Surface from Corner Points\|Py]] · [[Surface from Corner Points (cs)\|C#]] | Superficie desde 4 esquinas | `NurbsSurface.CreateFromCorners(a, b, c, d)` |
| Surface from Edge Curves | [[Surface from Edge Curves\|Py]] · [[Surface from Edge Curves (cs)\|C#]] | Superficie desde 2 a 4 curvas de borde | `Brep.CreateEdgeSurface(curvas)` |
| Sweep Surfaces with Sweep1 | [[Sweep Surfaces with Sweep1\|Py]] · [[Sweep Surfaces with Sweep1 (cs)\|C#]] | Barrido de secciones a lo largo de un riel | `SweepOneRail().PerformSweep(riel, secciones)` |
| Unroll Surface | [[Unroll Surface\|Py]] · [[Unroll Surface (cs)\|C#]] | Desarrolla una superficie desarrollable junto con curvas y puntos asociados | `Unroller(brep).PerformUnroll()` |

## Componentes de Grasshopper (158)

> Lista generada por `Wiki Rhino/herramientas/relacionar_catalogo.py` desde el catálogo exportado. No editar a mano entre las marcas AUTO: se reescribe al ejecutar el script.

### Params › Geometry (1)

- [[Catálogo - Params#Surface (Srf, parámetro)|Surface (Srf, parámetro)]] — Contiene una colección de superficies genéricas

### Surface › Analysis (25)

- [[Catálogo - Surface#Area|Area]] — Calcula las propiedades de área de breps, mallas y curvas planas cerradas
- [[Catálogo - Surface#Area Moments (AMoments)|Area Moments (AMoments)]] — Calcula los momentos de área de breps, mallas y curvas planas cerradas
- [[Catálogo - Surface#Box Corners|Box Corners]] — Extrae las 8 esquinas de una caja
- [[Catálogo - Surface#Box Properties (BoxProp)|Box Properties (BoxProp)]] — Obtiene algunas propiedades de una caja
- [[Catálogo - Surface#Brep Closest Point (Brep CP)|Brep Closest Point (Brep CP)]] — Busca el punto más cercano en un brep
- [[Catálogo - Surface#Brep Edges (Edges)|Brep Edges (Edges)]] — Extrae las curvas de arista de un brep
- [[Catálogo - Surface#Brep Topology (Topology)|Brep Topology (Topology)]] — Obtiene y muestra la topología de un brep
- [[Catálogo - Surface#Brep Wireframe (Wires)|Brep Wireframe (Wires)]] — Extrae las curvas de alambre (wireframe) de un brep
- [[Catálogo - Surface#Deconstruct Box (DeBox)|Deconstruct Box (DeBox)]] — Descompone una caja en sus partes
- [[Catálogo - Surface#Deconstruct Brep (DeBrep)|Deconstruct Brep (DeBrep)]] — Descompone un brep en sus partes
- [[Catálogo - Surface#Dimensions (Dim)|Dimensions (Dim)]] — Obtiene las dimensiones aproximadas de una superficie
- [[Catálogo - Surface#Evaluate Box (Box)|Evaluate Box (Box)]] — Evalúa una caja en el espacio normalizado {UVW}
- [[Catálogo - Surface#Evaluate Surface (EvalSrf)|Evaluate Surface (EvalSrf)]] — Evalúa las propiedades locales de una superficie en una coordenada {uv}
- [[Catálogo - Surface#Is Planar (Planar)|Is Planar (Planar)]] — Prueba si una superficie es plana
- [[Catálogo - Surface#Osculating Circles (Osc)|Osculating Circles (Osc)]] — Calcula los círculos osculadores principales de una superficie en una coordenada {uv}
- [[Catálogo - Surface#Point In Brep (BrepInc)|Point In Brep (BrepInc)]] — Prueba si un punto está dentro de un brep cerrado
- [[Catálogo - Surface#Point In Breps (BrepsInc)|Point In Breps (BrepsInc)]] — Prueba si un punto está dentro de una colección de breps cerrados
- [[Catálogo - Surface#Point In Trim (TrimInc)|Point In Trim (TrimInc)]] — Prueba si una coordenada {uv} está dentro de la parte recortada de una superficie
- [[Catálogo - Surface#Principal Curvature (Curvature)|Principal Curvature (Curvature)]] — Evalúa la curvatura principal de una superficie en una coordenada {uv}
- [[Catálogo - Surface#Shape In Brep (ShapeIn)|Shape In Brep (ShapeIn)]] — Prueba si una forma está dentro de un brep
- [[Catálogo - Surface#Surface Closest Point (Srf CP)|Surface Closest Point (Srf CP)]] — Busca el punto más cercano en una superficie
- [[Catálogo - Surface#Surface Curvature (Curvature)|Surface Curvature (Curvature)]] — Evalúa la curvatura de la superficie en una coordenada {uv}
- [[Catálogo - Surface#Surface Points (SrfPt)|Surface Points (SrfPt)]] — Obtiene los puntos de control de una superficie NURBS
- [[Catálogo - Surface#Volume|Volume]] — Calcula las propiedades de volumen de breps y mallas cerrados
- [[Catálogo - Surface#Volume Moments (VMoments)|Volume Moments (VMoments)]] — Calcula las propiedades de volumen de breps y mallas cerrados

### Surface › Freeform (23)

- [[Catálogo - Surface#4Point Surface (Srf4Pt)|4Point Surface (Srf4Pt)]] — Crea una superficie que une tres o cuatro puntos de esquina
- [[Catálogo - Surface#Boundary Surfaces (Boundary)|Boundary Surfaces (Boundary)]] — Crea superficies planas a partir de una colección de curvas de borde
- [[Catálogo - Surface#Control Point Loft (CPLoft)|Control Point Loft (CPLoft)]] — Crea un loft a través de los puntos de control de las curvas
- [[Catálogo - Surface#Edge Surface (EdgeSrf)|Edge Surface (EdgeSrf)]] — Crea una superficie a partir de dos, tres o cuatro curvas de borde
- [[Catálogo - Surface#Extrude (Extr)|Extrude (Extr)]] — Extruye puntos, curvas y superficies a lo largo de un vector
- [[Catálogo - Surface#Extrude Along (ExtrCrv)|Extrude Along (ExtrCrv)]] — Extruye curvas y superficies a lo largo de una curva
- [[Catálogo - Surface#Extrude Linear (Extrude)|Extrude Linear (Extrude)]] — Extruye curvas y superficies a lo largo de un camino recto
- [[Catálogo - Surface#Extrude Point (Extr)|Extrude Point (Extr)]] — Extruye curvas y superficies hasta un punto
- [[Catálogo - Surface#Fit Loft (FitLoft)|Fit Loft (FitLoft)]] — Crea un loft ajustado a un conjunto de curvas
- [[Catálogo - Surface#Fragment Patch (FPatch)|Fragment Patch (FPatch)]] — Crea un parche fragmentado a partir de un borde de polilínea
- [[Catálogo - Surface#Loft|Loft]] — Crea una superficie con loft a través de un conjunto de curvas de sección
- [[Catálogo - Surface#Loft Options (Loft Opt)|Loft Options (Loft Opt)]] — Crea opciones de loft a partir de entradas individuales
- [[Catálogo - Surface#Network Surface (NetSurf)|Network Surface (NetSurf)]] — Crea una superficie a partir de redes de curvas
- [[Catálogo - Surface#Patch|Patch]] — Crea una superficie de parche (patch)
- [[Catálogo - Surface#Pipe|Pipe]] — Crea una superficie de tubería alrededor de una curva de riel
- [[Catálogo - Surface#Pipe Variable (VPipe)|Pipe Variable (VPipe)]] — Crea una superficie de tubería con radios variables alrededor de una curva de riel
- [[Catálogo - Surface#Rail Revolution (RailRev)|Rail Revolution (RailRev)]] — Crea una superficie de revolución usando un riel de barrido
- [[Catálogo - Surface#Revolution (RevSrf)|Revolution (RevSrf)]] — Crea una superficie de revolución
- [[Catálogo - Surface#Ruled Surface (RuleSrf)|Ruled Surface (RuleSrf)]] — Crea una superficie entre dos curvas
- [[Catálogo - Surface#Sum Surface (SumSrf)|Sum Surface (SumSrf)]] — Crea una superficie de suma a partir de dos curvas de borde
- [[Catálogo - Surface#Surface From Points (SrfGrid)|Surface From Points (SrfGrid)]] — Crea una superficie NURBS a partir de una grilla de puntos
- [[Catálogo - Surface#Sweep1 (Swp1)|Sweep1 (Swp1)]] — Crea una superficie de barrido (sweep) con una curva de riel
- [[Catálogo - Surface#Sweep2 (Swp2)|Sweep2 (Swp2)]] — Crea una superficie de barrido (sweep) con dos curvas de riel

### Surface › Primitive (13)

- [[Catálogo - Surface#Bounding Box (BBox)|Bounding Box (BBox)]] — Calcula las cajas contenedoras orientadas de la geometría
- [[Catálogo - Surface#Box 2Pt (Box)|Box 2Pt (Box)]] — Crea una caja definida por dos puntos
- [[Catálogo - Surface#Box Rectangle (BoxRec)|Box Rectangle (BoxRec)]] — Crea una caja definida por un rectángulo y una altura
- [[Catálogo - Surface#Center Box (Box)|Center Box (Box)]] — Crea una caja centrada en un plano
- [[Catálogo - Surface#Cone|Cone]] — Crea una superficie cónica
- [[Catálogo - Surface#Cylinder (Cyl)|Cylinder (Cyl)]] — Crea una superficie cilíndrica
- [[Catálogo - Surface#Domain Box (Box)|Domain Box (Box)]] — Crea una caja definida por un plano base y dominios de tamaño
- [[Catálogo - Surface#Plane Surface (PlaneSrf)|Plane Surface (PlaneSrf)]] — Crea una superficie plana
- [[Catálogo - Surface#Plane Through Shape (PxS)|Plane Through Shape (PxS)]] — Crea una superficie rectangular más grande que una forma dada
- [[Catálogo - Surface#Quad Sphere (QSph)|Quad Sphere (QSph)]] — Crea un brep esférico formado por parches NURBS cuadrangulares
- [[Catálogo - Surface#Sphere (Sph)|Sphere (Sph)]] — Crea una superficie esférica
- [[Catálogo - Surface#Sphere 4Pt (Sph4Pt)|Sphere 4Pt (Sph4Pt)]] — Crea una superficie esférica a partir de 4 puntos
- [[Catálogo - Surface#Sphere Fit (SFit)|Sphere Fit (SFit)]] — Ajusta una esfera a una colección 3D de puntos

### Surface › Util (22)

- [[Catálogo - Surface#Brep Join (Join)|Brep Join (Join)]] — Une varios Breps
- [[Catálogo - Surface#Cap Holes (Cap)|Cap Holes (Cap)]] — Tapa todos los agujeros planos de un Brep
- [[Catálogo - Surface#Cap Holes Ex (CapEx)|Cap Holes Ex (CapEx)]] — Tapa la mayor cantidad posible de agujeros de un Brep
- [[Catálogo - Surface#Convex Edges (EdgesCvx)|Convex Edges (EdgesCvx)]] — Selecciona las aristas cóncavas o convexas de un brep
- [[Catálogo - Surface#Copy Trim (Trim)|Copy Trim (Trim)]] — Copia los datos de recorte UV de una superficie a otra
- [[Catálogo - Surface#Divide Surface (SDivide)|Divide Surface (SDivide)]] — Genera una grilla de puntos {uv} sobre una superficie
- [[Catálogo - Surface#Edges from Directions (EdgesDir)|Edges from Directions (EdgesDir)]] — Selecciona aristas de un brep según su dirección
- [[Catálogo - Surface#Edges from Faces (EdgesFaces)|Edges from Faces (EdgesFaces)]] — Selecciona todas las aristas del brep que delimitan ciertas caras
- [[Catálogo - Surface#Edges from Length (EdgesLen)|Edges from Length (EdgesLen)]] — Selecciona aristas de un brep según su longitud
- [[Catálogo - Surface#Edges from Linearity (EdgesLin)|Edges from Linearity (EdgesLin)]] — Selecciona aristas de un brep según su linealidad
- [[Catálogo - Surface#Edges from Points (EdgesPt)|Edges from Points (EdgesPt)]] — Selecciona aristas de un brep según su coincidencia con puntos
- [[Catálogo - Surface#Fillet Edge (FilEdge)|Fillet Edge (FilEdge)]] — Aplica fillet a algunas aristas de un brep
- [[Catálogo - Surface#Flip|Flip]] — Invierte las normales de una superficie según geometría local o remota
- [[Catálogo - Surface#Isotrim (SubSrf)|Isotrim (SubSrf)]] — Extrae un subconjunto isoparamétrico de una superficie
- [[Catálogo - Surface#Merge Faces (FMerge)|Merge Faces (FMerge)]] — Fusiona todas las caras coplanares adyacentes de un brep
- [[Catálogo - Surface#Offset Surface (Offset)|Offset Surface (Offset)]] — Aplica offset a una superficie con una distancia fija
- [[Catálogo - Surface#Offset Surface Loose (Offset (L))|Offset Surface Loose (Offset (L))]] — Aplica offset a una superficie moviendo sus puntos de control
- [[Catálogo - Surface#Retrim|Retrim]] — Vuelve a recortar una superficie según los datos de recorte 3D de otra superficie
- [[Catálogo - Surface#Reverse Surface (Reverse Srf)|Reverse Surface (Reverse Srf)]] — Invierte las direcciones de la parametrización de la superficie (U, V y W)
- [[Catálogo - Surface#Surface Frames (SFrames)|Surface Frames (SFrames)]] — Genera una grilla de marcos {uv} sobre una superficie
- [[Catálogo - Surface#Transpose Surface (Transpose)|Transpose Surface (Transpose)]] — Transpone la parametrización de la superficie (intercambia U y V)
- [[Catálogo - Surface#Untrim|Untrim]] — Quita todas las curvas de recorte de una superficie

### LunchBox › Form (13)

- [[Catálogo - LunchBox#3D Supershape (3DSupershape)|3D Supershape (3DSupershape)]] — Crea una superforma (supershape) 3D paramétrica
- [[Catálogo - LunchBox#Conoid Surface (Conoid)|Conoid Surface (Conoid)]] — Crea la superficie conoide de Plücker
- [[Catálogo - LunchBox#Enneper Surface (Enneper)|Enneper Surface (Enneper)]] — Crea una superficie de Enneper paramétrica
- [[Catálogo - LunchBox#Helicoid Surface (Helicoid)|Helicoid Surface (Helicoid)]] — Crea una superficie helicoide paramétrica
- [[Catálogo - LunchBox#Hyperbolic Paraboloid (Paraboloid)|Hyperbolic Paraboloid (Paraboloid)]] — Crea una superficie paraboloide paramétrica
- [[Catálogo - LunchBox#Klein Surface (Klein)|Klein Surface (Klein)]] — Crea una superficie de Klein paramétrica
- [[Catálogo - LunchBox#Mobius Surface (Mobius)|Mobius Surface (Mobius)]] — Crea una superficie de Möbius paramétrica
- [[Catálogo - LunchBox#Platonic Cube (PlatoCube)|Platonic Cube (PlatoCube)]] — Crea un cubo paramétrico con un parámetro de truncamiento
- [[Catálogo - LunchBox#Platonic Dodecahedron (PlatoDodec)|Platonic Dodecahedron (PlatoDodec)]] — Crea un dodecaedro
- [[Catálogo - LunchBox#Platonic Icosahedron (PlatoIcosa)|Platonic Icosahedron (PlatoIcosa)]] — Crea un icosaedro paramétrico con un parámetro de truncamiento
- [[Catálogo - LunchBox#Platonic Octahedron (PlatoOcta)|Platonic Octahedron (PlatoOcta)]] — Crea un octaedro paramétrico con un parámetro de truncamiento
- [[Catálogo - LunchBox#Platonic Tetrahedron (PlatoTetra)|Platonic Tetrahedron (PlatoTetra)]] — Crea un tetraedro paramétrico con un parámetro de truncamiento
- [[Catálogo - LunchBox#Torus Surface (Torus)|Torus Surface (Torus)]] — Crea una superficie toroidal (toro) paramétrica

### Parakeet › Primitive (5)

- [[Catálogo - Parakeet#Geodesic Dome|Geodesic Dome]] — Genera una cúpula geodésica a partir de un icosaedro
- [[Catálogo - Parakeet#Klein Bottle|Klein Bottle]] — Crea una botella de Klein como superficie NURBS
- [[Catálogo - Parakeet#Klein Surface|Klein Surface]] — Crea una superficie NURBS de Klein
- [[Catálogo - Parakeet#Mobius Surface (Mobius)|Mobius Surface (Mobius)]] — Crea una superficie de Möbius con parámetros variables
- [[Catálogo - Parakeet#PlukerSurface (PlukerSrf)|PlukerSurface (PlukerSrf)]] — Crea una superficie de Plücker con parámetros variables

### Parakeet › Surface (13)

- [[Catálogo - Parakeet#BooleanSplit|BooleanSplit]] — Divide un Brep con otro(s) Brep(s) [división Brep\|Brep]
- [[Catálogo - Parakeet#Brep join plus (Brep join +)|Brep join plus (Brep join +)]] — Une varios Breps que estén a menos de una distancia
- [[Catálogo - Parakeet#Brep Remove Holes (BrepRemoveHoles)|Brep Remove Holes (BrepRemoveHoles)]] — Quita los agujeros de un B-rep (funciona con superficies NURBS recortadas y sin recortar)
- [[Catálogo - Parakeet#Brep Topology|Brep Topology]] — Obtiene la topología completa de un Brep
- [[Catálogo - Parakeet#CreateSolid|CreateSolid]] — Crea un sólido (Brep cerrado) encerrado por superficies y polisuperficies que se intersectan
- [[Catálogo - Parakeet#Extend Surface (ExtendSrf)|Extend Surface (ExtendSrf)]] — Extiende una superficie desde una arista y una distancia dadas
- [[Catálogo - Parakeet#Map To Surface (MapToSrf)|Map To Surface (MapToSrf)]] — Mapea una curva sobre una superficie
- [[Catálogo - Parakeet#Offset Brep (BrepOffset)|Offset Brep (BrepOffset)]] — Aplica offset a un Brep con parámetros variables
- [[Catálogo - Parakeet#Panelized Sum Surface (PQSumSrf)|Panelized Sum Surface (PQSumSrf)]] — Crea una panelización de cuadriláteros planos sobre una superficie, generada por dos curvas de perfil (basado…
- [[Catálogo - Parakeet#RemoveDuplicateSurface (RemoveDupSrf)|RemoveDuplicateSurface (RemoveDupSrf)]] — Quita las superficies idénticas de una lista
- [[Catálogo - Parakeet#Reverse Surface (ReverseSrf)|Reverse Surface (ReverseSrf)]] — Invierte las direcciones U y V (dominio) de una superficie
- [[Catálogo - Parakeet#Unjoin Brep Faces (Unjoin Brep)|Unjoin Brep Faces (Unjoin Brep)]] — Explota un Brep desde algunas aristas específicas
- [[Catálogo - Parakeet#Voronoi On Surface (VoronoiSrf)|Voronoi On Surface (VoronoiSrf)]] — Genera un patrón de Voronoi sobre una superficie NURBS dada

### Pufferfish › Surface (43)

- [[Catálogo - Pufferfish#Append Polysurfaces (AppPsrfs)|Append Polysurfaces (AppPsrfs)]] — Agrega un conjunto de polisuperficies (Breps) desconectadas para formar una sola polisuperficie (Brep)…
- [[Catálogo - Pufferfish#Automatic Edge Surface (AutoEdgSrf)|Automatic Edge Surface (AutoEdgSrf)]] — Crea una superficie entre 2, 3 o 4 curvas de borde ordenadas automáticamente
- [[Catálogo - Pufferfish#Automatic Network Surface (AutoNetSrf)|Automatic Network Surface (AutoNetSrf)]] — Crea una superficie a partir de una red de curvas ordenada automáticamente
- [[Catálogo - Pufferfish#Average Surface (AvrSrf)|Average Surface (AvrSrf)]] — Calcula el promedio aritmético de un conjunto de superficies; las superficies recortadas se tratan como sin…
- [[Catálogo - Pufferfish#Constrained Volume Box (ConsVolBox)|Constrained Volume Box (ConsVolBox)]] — Crea una caja rectangular o regular del tamaño de un volumen dado, con factores de proporción {x}, {y} y {z}…
- [[Catálogo - Pufferfish#Constrained Volume Ellipsoid (ConsVolEli)|Constrained Volume Ellipsoid (ConsVolEli)]] — Crea un elipsoide o esfera del tamaño de un volumen dado, con factores de proporción {x}, {y} y {z}, centrado…
- [[Catálogo - Pufferfish#Extrude Tapered Polysurface (ExtrTaper)|Extrude Tapered Polysurface (ExtrTaper)]] — Extruye un perfil con conicidad según un ángulo de desmoldeo
- [[Catálogo - Pufferfish#Fit Surface (FitSrf)|Fit Surface (FitSrf)]] — Ajusta una nueva superficie a una superficie existente cuando es posible, sin cambiar la forma general…
- [[Catálogo - Pufferfish#Flip Polysurface (FlipPsrf)|Flip Polysurface (FlipPsrf)]] — Invierte las normales de una polisuperficie (Brep); las polisuperficies cerradas no se pueden invertir y…
- [[Catálogo - Pufferfish#Is Polysurface Closed (PsrfClsd)|Is Polysurface Closed (PsrfClsd)]] — Prueba si una polisuperficie (Brep) es cerrada
- [[Catálogo - Pufferfish#Is Surface Closed (SrfClsd)|Is Surface Closed (SrfClsd)]] — Prueba si una superficie es cerrada y si sus aristas se cierran en las direcciones {u} o {v}
- [[Catálogo - Pufferfish#Is Surface Collapsed (SrfCollapsed)|Is Surface Collapsed (SrfCollapsed)]] — Prueba si una superficie tiene aristas colapsadas en un punto (singularidades)
- [[Catálogo - Pufferfish#Is Surface Trimmed (SrfTrimd)|Is Surface Trimmed (SrfTrimd)]] — Prueba si una superficie está recortada; también puede buscar caras recortadas en una polisuperficie (Brep)
- [[Catálogo - Pufferfish#Mesh To Polysurface (Msh2Psrf)|Mesh To Polysurface (Msh2Psrf)]] — Convierte una malla en una polisuperficie NURBS (Brep)
- [[Catálogo - Pufferfish#Mirror Cut Polysurface (MirCutPsrf)|Mirror Cut Polysurface (MirCutPsrf)]] — Corta una polisuperficie (Brep) con un plano, refleja el lado conservado del corte respecto de un plano de…
- [[Catálogo - Pufferfish#Mirror Cut Surface (MirCutSrf)|Mirror Cut Surface (MirCutSrf)]] — Corta una superficie con un plano, refleja el lado conservado del corte respecto de un plano de reflejo y lo…
- [[Catálogo - Pufferfish#Offset Surface (OffSrf)|Offset Surface (OffSrf)]] — Aplica offset a una superficie, con la opción de hacerlo hacia ambos lados a distancias distintas y crear un…
- [[Catálogo - Pufferfish#Parameter Subdivide Surface (ParamSubDivSrf)|Parameter Subdivide Surface (ParamSubDivSrf)]] — Genera una grilla de superficies de subdivisión sobre una superficie, dividiendo su dominio con parámetros…
- [[Catálogo - Pufferfish#Plane Trim Surface (PlnTrimSrf)|Plane Trim Surface (PlnTrimSrf)]] — Recorta (quita) las partes de una superficie que están a un lado de un plano; también funciona con…
- [[Catálogo - Pufferfish#Rebuild Surface (RebSrf)|Rebuild Surface (RebSrf)]] — Reconstruye una superficie con una cantidad de puntos, un grado y un dominio dados en las direcciones {u} y…
- [[Catálogo - Pufferfish#Remap Surface Domain² (ReSrfDom²)|Remap Surface Domain² (ReSrfDom²)]] — Reasigna el rango del dominio² {uv} de una superficie a un rango de entrada, con la opción de igualar el…
- [[Catálogo - Pufferfish#Reparameterize Surface (ReparamSrf)|Reparameterize Surface (ReparamSrf)]] — Reparametriza una superficie para que su dominio² (uv) vaya de 0 a 1; también funciona con superficies…
- [[Catálogo - Pufferfish#Shell Polysurface (ShellPsrf)|Shell Polysurface (ShellPsrf)]] — Crea un cascarón hueco con espesor a partir de una polisuperficie cerrada (Brep)
- [[Catálogo - Pufferfish#Shrink Trimmed Surface (ShrinkTrimSrf)|Shrink Trimmed Surface (ShrinkTrimSrf)]] — Encoge la superficie sin recortar subyacente de una superficie recortada para que quede lo más cerca posible…
- [[Catálogo - Pufferfish#Split Kinky Surface (SplitKinkySrf)|Split Kinky Surface (SplitKinkySrf)]] — Divide en una polisuperficie (Brep) la superficie de salida de un componente de superficie sin dividir, si…
- [[Catálogo - Pufferfish#Superimpose Surface (SuperSrf)|Superimpose Surface (SuperSrf)]] — Superpone la cantidad de puntos de control {uv}, el grado {uv}, el dominio {uv} y los recortes de una…
- [[Catálogo - Pufferfish#Surface Degree (SrfDeg)|Surface Degree (SrfDeg)]] — Obtiene el valor del grado de una superficie en sus direcciones {u} y {v}
- [[Catálogo - Pufferfish#Surface Spans (Srfpans)|Surface Spans (Srfpans)]] — Obtiene los subdominios² de cada tramo (span) de una superficie e información de los tramos: subdominios de…
- [[Catálogo - Pufferfish#Surface Statistics (SrfStats)|Surface Statistics (SrfStats)]] — Obtiene estadísticas de una superficie o polisuperficie (Brep): cantidad de caras, de caras sin recortar, de…
- [[Catálogo - Pufferfish#Swap Surface Directions (SwapSrfDir)|Swap Surface Directions (SwapSrfDir)]] — Intercambia o invierte las direcciones {u} y {v} de una superficie; también funciona con superficies…
- [[Catálogo - Pufferfish#Tween Consecutive Surfaces (TwnConSrfs)|Tween Consecutive Surfaces (TwnConSrfs)]] — Interpola (tween) consecutivamente entre un conjunto de superficies; las superficies recortadas se tratan…
- [[Catálogo - Pufferfish#Tween Through Surfaces (TwnThruSrfs)|Tween Through Surfaces (TwnThruSrfs)]] — Interpola (tween) a través de un conjunto de superficies; las superficies recortadas se tratan como sin…
- [[Catálogo - Pufferfish#Tween Two Surfaces (Twn2Srfs)|Tween Two Surfaces (Twn2Srfs)]] — Interpola (tween) entre dos superficies; las superficies recortadas se tratan como sin recortar
- [[Catálogo - Pufferfish#Tween Two Surfaces Along Curve (Twn2SrfsCrv)|Tween Two Surfaces Along Curve (Twn2SrfsCrv)]] — Interpola (tween) entre dos superficies a lo largo de una curva guía (u opcionalmente de dos curvas guía)…
- [[Catálogo - Pufferfish#Unroll Polysurface (UnrollPsrf)|Unroll Polysurface (UnrollPsrf)]] — Desenrolla una polisuperficie (Brep) para que sus caras queden planas sobre un plano, con la opción de…
- [[Catálogo - Pufferfish#Unsplit Edge Surface (UnsplitEdge)|Unsplit Edge Surface (UnsplitEdge)]] — Crea una superficie de bordes sin recortar entre 2, 3 o 4 curvas de borde, que no se divide en una…
- [[Catálogo - Pufferfish#Unsplit Extrude Surface (UnsplitExtr)|Unsplit Extrude Surface (UnsplitExtr)]] — Crea una superficie extruida sin recortar a partir de una curva o superficie de perfil, a lo largo de un…
- [[Catálogo - Pufferfish#Unsplit Loft Surface (UnsplitLoft)|Unsplit Loft Surface (UnsplitLoft)]] — Crea una superficie con loft sin recortar a través de un conjunto de curvas o superficies de sección, que no…
- [[Catálogo - Pufferfish#Unsplit Rail Revolve Surface (UnsplitRailRev)|Unsplit Rail Revolve Surface (UnsplitRailRev)]] — Crea una superficie de revolución sin recortar a partir de una curva o superficie de perfil, guiada por una…
- [[Catálogo - Pufferfish#Unsplit Revolve Surface (UnsplitRev)|Unsplit Revolve Surface (UnsplitRev)]] — Crea una superficie de revolución sin recortar a partir de una curva o superficie de perfil alrededor de un…
- [[Catálogo - Pufferfish#Unsplit Sum Surface (UnsplitSum)|Unsplit Sum Surface (UnsplitSum)]] — Crea una superficie de suma sin recortar a partir de dos curvas de borde, que no se divide en una…
- [[Catálogo - Pufferfish#Unsplit Sweep Surface (UnsplitSwp)|Unsplit Sweep Surface (UnsplitSwp)]] — Crea una superficie de barrido (sweep) sin recortar a través de un conjunto de curvas o superficies de…
- [[Catálogo - Pufferfish#Weighted Average Surface (WavSrf)|Weighted Average Surface (WavSrf)]] — Calcula el promedio aritmético ponderado de un conjunto de superficies; las superficies recortadas se tratan…

<!-- AUTO:fin -->
