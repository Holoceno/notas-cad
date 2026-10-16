---
tags: [tipo/apunte, geometria/brep, geometria/curvas, fabricacion/cnc, software/rhinocommon, software/grasshopper, lenguaje/python]
palabras-clave: [Split Brep, recortar, contorno, región, centroide, fillet, CreateFilletCurves, piezas pequeñas, astillas]
---

# Recortar piezas con un contorno

Al cortar piezas con el borde de un cielo (o de cualquier región), la regla "**quedarse con el trozo más grande**" funciona solo mientras la pieza es mucho más larga que lo que sobra. En filas cortas falla: el trozo de afuera puede ser el más grande, o una mitad completa puede quedar fuera sin que el corte la toque. La regla correcta es **quedarse con lo de adentro**.

## Receta (RhinoCommon, Python 3)
```python
srf = rg.Brep.CreatePlanarBreps(contorno, tol)[0]
trozos = list(srf.Split(muros, tol)) or [srf]      # sin cruce → la pieza entera
adentro = []
for t in trozos:
    amp = rg.AreaMassProperties.Compute(t)
    p = rg.Point3d(amp.Centroid.X, amp.Centroid.Y, 0)   # a planta
    if region.Contains(p, rg.Plane.WorldXY, 0.5) == rg.PointContainment.Inside:
        adentro.append(t)
```
- El **centroide** decide, no el área. Un trozo sin cruce con los muros también se prueba: puede estar entero fuera.
- En Grasshopper: *Split Brep* → *Area* (centroide) → *Point in Curve* → *Dispatch*, en vez de *Sort* + *List Item*.

## Piezas que "no son ni una ni otra"
- Si la línea completa mide menos que el máximo de fabricación, **una sola pieza** es mejor que dos con una astilla.
- Para el plano de instalación conviene que la pieza única tome la **primera letra de su línea** (A o C), aunque técnicamente sea la "larga": el instalador espera ver una A.

## Fillet solo en algunas esquinas
`Curve.CreateFilletCornersCurve` redondea **todas** las esquinas. Para una sola esquina:
1. Buscar los vértices que tocan el muro (distancia < 0,1) y tomar el más bajo de cada extremo.
2. `rg.Curve.CreateFilletCurves(c0, punto0, c1, punto1, R, False, True, False, tol, tolAng)` con los dos tramos que llegan a esa esquina; devuelve los dos tramos recortados + el arco.
3. Volver a unir todo con `Curve.JoinCurves`.

Trampas encontradas:
- Los calados tenían **tramos curvos (grado 2)**: no son polilíneas, así que `TryGetPolyline` no sirve. Trabajar con los segmentos tal cual.
- Si el corte cae justo junto a un calado, el tramo plano mide menos que R: unir los tramos siguientes y hacer el fillet contra esa cadena.
- La esquina puede caer en la **costura** del contorno cerrado (último segmento → primero): rotar la lista de segmentos antes de buscar.
- Con el fillet ya hecho, apagar el fillet antiguo para no redondear dos veces.

## Conexiones
- Mapas: [[Mapa - Fabricación]] · [[Mapa - Intersecciones y booleanos]] · [[Mapa - Brep y sólidos]]
- [[wiki/concepts/rhinocommon-interseccion-api]] · muestra oficial: [[Split BReps with Planes]]
