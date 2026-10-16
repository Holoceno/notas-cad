# notas-cad

Apuntes de Rhino, Grasshopper, RhinoCommon, Python y fabricación digital que he ido juntando mientras aprendo. Es una bóveda de Obsidian: se abre la carpeta como bóveda y se navega desde `Inicio.md`.

No es documentación oficial ni está terminada. Lo armé para no tener que resolver dos veces lo mismo, y lo comparto por si a alguien más le sirve.

## Qué hay

| Carpeta | Contenido |
|---|---|
| `Inicio.md` | La portada, con los mapas por tema. |
| `Mapas/` | Mapas por tema (curvas, brep, mallas, data trees, fabricación, programación...). Cada uno junta apuntes, páginas de la wiki y la lista de componentes de Grasshopper del tema. |
| `Aprendizaje/` | Apuntes cortos, un concepto por nota, con ejemplos de casos reales. |
| `Wiki Rhino/` | Una wiki de Rhino armada a partir de fuentes: `raw/` son las fuentes originales tal cual (documentación y muestras de McNeel, catálogo de componentes de Grasshopper), `wiki/` son los resúmenes y conceptos, y `herramientas/` los scripts que mantienen el catálogo. |
| `Plantillas/` | Plantilla para anotar una sesión de trabajo. |

## La wiki y sus fuentes

La wiki sigue un método que tomé de otro repo de "segundo cerebro": las fuentes se guardan sin tocar en `raw/` (por ejemplo con Web Clipper) y desde ahí se escriben las páginas de `wiki/`, siempre citando de dónde sale cada cosa. Las reglas están en `Wiki Rhino/CLAUDE.md`, pensadas para trabajar la wiki con un asistente de IA, pero se pueden seguir a mano.

Las muestras y guías de `raw/` son de McNeel (developer.rhino3d.com), copiadas de su repositorio público. Los créditos son suyos.

## Etiquetas

Cada nota tiene etiquetas en el frontmatter (`tipo/` + tema). El vocabulario y cómo buscar está en `Mapas/Etiquetas y navegación.md`.

## Si quieres aportar

Si encuentras un error o tienes un apunte que sume, avísame o abre un issue.
