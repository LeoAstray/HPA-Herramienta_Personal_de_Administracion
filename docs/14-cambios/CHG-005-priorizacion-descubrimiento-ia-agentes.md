# CHG-005 — Priorización del descubrimiento de IA y Agentes

## Estado

Documentado y aplicado a la documentación operativa. No se añade código de producto, proveedor, modelo, credencial ni integración externa.

## Objetivo y alcance

Reflejar la decisión del propietario de hacer del descubrimiento y diseño de IA/Agentes el siguiente objetivo del proyecto. La prioridad consiste en investigar casos de uso, agentes necesarios, modelos y controles; no autoriza implementar agentes antes de disponer de los prerrequisitos de Core e Identidad y Seguridad.

## Impacto

- **Gobierno y roadmap:** el descubrimiento de IA/Agentes pasa a ser la actividad inmediata.
- **Decisión:** ADR-003 registra el alcance y los límites de esta prioridad.
- **Módulo IA/Agentes:** incorpora los entregables que deben existir antes de recomendar una implementación.
- **Arquitectura, datos, API, interfaz, infraestructura, pruebas y operaciones:** continúan sin decisiones técnicas aprobadas.
- **Asana:** no se actualiza; no se proporcionó una referencia o autorización para crear tareas externas.

## Seguridad y privacidad

No se conectan modelos, agentes ni servicios externos, y no se envían datos del producto. El descubrimiento deberá aplicar mínimo privilegio y evaluar expresamente el tratamiento de datos, permisos, confirmación humana, revocación y auditoría antes de proponer un agente implementable.

## Verificación y rollback

Se comprueba que el roadmap, el estado, la documentación de IA y el índice ADR enlazan con ADR-003 y presentan la misma prioridad. El rollback consiste en revertir estos documentos y CHG-005; no afecta a datos, servicios ni infraestructura.

## Documentación relacionada

- `docs/13-adrs/ADR-003-priorizacion-descubrimiento-ia-agentes.md`
- `docs/01-proyecto/roadmap.md`
- `docs/10-ia/`
- `docs/12-modulos/14-ia-agentes.md`
