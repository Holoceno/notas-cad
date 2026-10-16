---
tags: [tipo/apunte, fabricacion/nesting, fabricacion/cnc, programacion/algoritmos, software/grasshopper, lenguaje/python]
palabras-clave: [nesting, bin packing, franjas, strip packing, mochila, knapsack, cota inferior, placas, OpenNest]
---

# Nesting por franjas

Cuando **todas las piezas tienen el mismo alto**, el nesting 2D se vuelve un problema 1D: la placa se corta en franjas de ese alto y cada franja es una "caja" de largo fijo que hay que llenar. Es más simple, más rápido y se puede **demostrar** que el resultado es el mínimo, cosa que OpenNest no da.

Caso real: baffles de 300 de alto en placas de 2780×1200 → 4 franjas justas por placa.

## Cómo funciona
1. **Medir cada pieza en su propio plano** (largo × alto): marco local con X a lo largo de la pieza; caja contenedora en ese plano.
2. **Armar placa por placa**: cada franja parte con la pieza más larga que cabe y el resto del largo se llena con el **mejor subconjunto** de piezas restantes (problema de la mochila, por programación dinámica en mm enteros).
3. **Piezas paradas (opcional)**: una pieza más corta que el alto de la placa puede ir girada 90° en una **columna** al costado; la columna exige que *todas* las franjas de esa placa dejen libre ese ancho.
4. Elegir el número de columnas que más largo coloca; cada pieza parada tiene una **penalización**, así solo se gira cuando ahorra una placa.

```python
def mejor_relleno(largos, espacio):
    """Índices de los largos que mejor llenan 'espacio' (mochila 0/1)."""
    mejor = {0: ()}
    for i, l in enumerate(largos):
        for suma, sel in list(mejor.items()):
            t = suma + int(math.ceil(l))
            if t <= espacio and t not in mejor:
                mejor[t] = sel + (i,)
    return mejor[max(mejor)]
```

## ¿Cómo sé que es el mínimo? (cota inferior)
- **Por área**: `ceil(área de piezas / área de placa)`. Siempre válida, pero a veces optimista.
- **Por piezas de más de media placa**: dos piezas de más de la mitad del largo nunca comparten franja, y en cualquier vertical de la placa caben solo 4 → como máximo 4 por placa. Si además no pueden ir paradas (largo > alto de placa), cada placa admite como máximo 4 de ellas.
- Si el resultado iguala la cota, **no hay nada mejor**. Ejemplo: 77 piezas largas en Mármol → `ceil(77/4) = 20` placas, y el nesting dio 20.
- La cota por área puede mentir: Negro daba "1 placa" por área, pero 6 piezas no caben en 4 franjas.

## Lo que aprendí
- Primero mirar si el problema tiene una **simplificación** (alto constante, piezas rectangulares) antes de ir al nesting genérico.
- Un algoritmo simple (agrupar las largas de a 4) fue óptimo en un cielo, pero en el otro, con largos muy variados, gastaba una placa de más. Llenar con mochila lo resolvió.
- Girar piezas puede ahorrar placas, pero **preguntar si el material tiene veta o dirección**.
- Sin separación entre piezas sirve si el cuchillo es delgado; si no, sumar el ancho de corte al largo de cada pieza.

## Conexiones
- Mapas: [[Mapa - Fabricación]] · [[Mapa - Data trees y listas]]
- Alternativa genérica: [[wiki/entities/opennest|OpenNest]] (formas libres, rotaciones, separación)
- Para que contorno, rótulo, pliegue y flocks viajen juntos a la placa: [[Ramas paralelas por pieza]]
