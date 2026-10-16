---
title: "Catálogo Grasshopper — Anemone"
source: "Exportado del Grasshopper instalado (herramientas/exportar_catalogo_gh.py)"
type: catalogo
tab: "Anemone"
libraries: ["Anemone Classic"]
components: 3
rhino: "8.35.26251.13001"
grasshopper: "1.0.0008"
generated: 2026-10-12
tags: [tipo/catalogo, software/grasshopper, plugin/anemone, programacion/scripts]
---

# Anemone

3 objetos · librería: Anemone Classic · autor: Mateusz Zwierzycki

Mapas: [[Mapa - Scripts, interfaz y archivos]] (3)

## Classic

### Loop End

Termina el bucle con este componente. Doble clic para pausar el bucle.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| < | `<` | Text | item | Conectar a Loop Start |
| Exit *(opcional)* | `E` | Boolean | item | Poner en True para salir del bucle |
| Data | `D0` | Generic Data | árbol | Datos que recorren el bucle |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D0` | Generic Data | árbol | Datos después del bucle |

### Loop Start

Inicia el bucle con este componente. Doble clic para volver a ejecutar.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Repeat *(opcional)* | `N` | Integer | item | Número de repeticiones |
| Trigger *(opcional)* | `T` | Generic Data | árbol | Si quieres que el disparador reinicie el bucle |
| Data *(opcional)* | `D0` | Generic Data | árbol | Datos que recorren el bucle |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| > | `>` | Text | item | Conectar a Loop End |
| Counter | `C` | Integer | item | Contador |
| Data | `D0` | Generic Data | árbol | Datos que recorren el bucle |

## Util

### Time Buffer (Buffer)

Espera un tiempo determinado antes de pasar los datos.

| Entrada | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Datos a retener (buffer) |
| Time | `T` | Integer | item | Tiempo de espera en ms |

| Salida | Abrev. | Tipo | Acceso | Descripción |
|---|---|---|---|---|
| Data | `D` | Generic Data | árbol | Datos retenidos (buffer) |
