# CHG-020 — Modelo de entidades, relaciones, eventos y auditoría de Core (ADR-005)

## Estado

Documentado y aplicado a la documentación operativa. No afecta a código de producto ni a los agentes de desarrollo definidos por ADR-003/ADR-004.

## Objetivo y alcance

Se cierra el bloque 2 de `docs/01-proyecto/decisiones-transversales-pendientes.md` — el modelo de entidades comunes, relaciones explícitas, eventos internos y auditoría mínima de Core —, identificado como el bloqueador transversal que más módulos condicionaba. La propuesta se desarrolló en `docs/03-arquitectura/propuesta-modelo-core.md`, fue revisada y acordada por ambos colaboradores, y se formaliza como `docs/13-adrs/ADR-005-modelo-core.md`.

## Impacto

- **Nuevo ADR:** `docs/13-adrs/ADR-005-modelo-core.md`, añadido a `docs/13-adrs/indice.md`.
- **Core:** `docs/12-modulos/00-core.md` actualizado — entidades, relaciones y eventos dejan de ser conceptos abiertos; la sección "Decisiones pendientes" se reduce a autorización concreta (bloque 1), tecnología de entrega de eventos y catálogo de tipos.
- **Decisiones transversales:** el bloque 2 de `docs/01-proyecto/decisiones-transversales-pendientes.md` se marca RESUELTO (ADR-005).
- **Roadmap:** `docs/01-proyecto/roadmap.md` actualizado — el ítem "resolver el contrato de Core" se marca alcanzado; el bloqueador transversal restante pasa a ser identidad, permisos y sesiones.
- **Relación con ADR-003/ADR-004:** sin conflicto de contenido. ADR-003 ya señalaba el contrato de eventos de Core como prerrequisito no resuelto para los agentes internos del producto; esta decisión lo resuelve. Hubo colisión de numeración (un primer borrador usó "ADR-003" antes de que ADR-003/ADR-004 se aprobaran en otra rama); se renumera a ADR-005 sin reabrir ninguna decisión ya tomada en esos dos.
- **Arquitectura técnica, datos, API, interfaz, requisitos, pruebas y operaciones:** no se decide tecnología concreta; sigue pendiente.

## Seguridad y privacidad

El modelo de auditoría mínima (tipo, entidad, actor, marca de tiempo) queda listo para que la autorización, cuando se resuelva el bloque 1, se aplique sobre la misma base sin rediseñar el registro. No se otorga a ningún módulo ni agente acceso directo a datos internos de otro; la separación Core/módulos declarada coincide con el principio de mínimo acceso ya aplicado a los agentes de desarrollo en ADR-003/ADR-004.

## Verificación y rollback

Comprobar que `00-core.md`, el índice de ADR y el roadmap son consistentes entre sí y no contradicen ADR-003/ADR-004. El rollback consiste en revertir los archivos de documentación cambiados; no altera datos, servicios ni infraestructura.

## Documentación relacionada

- `docs/03-arquitectura/propuesta-modelo-core.md`
- `docs/13-adrs/ADR-005-modelo-core.md`
- `docs/13-adrs/indice.md`
- `docs/12-modulos/00-core.md`
- `docs/01-proyecto/decisiones-transversales-pendientes.md`
- `docs/01-proyecto/roadmap.md`