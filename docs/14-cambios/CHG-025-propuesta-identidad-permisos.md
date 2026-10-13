# CHG-025 — Propuesta de identidad, permisos y sesiones

## Estado y alcance

Aplicado el 2026-10-11. Cambio documental que redacta la propuesta del bloque 1 de [decisiones transversales pendientes](../01-proyecto/decisiones-transversales-pendientes.md): identidad, permisos y sesiones. Es una propuesta; no aprueba ninguna decisión ni modifica ADR existentes.

## Cambio documental

Se añade la [propuesta de identidad, permisos y sesiones](../03-arquitectura/propuesta-identidad-permisos.md). Cubre actores, autenticación del propietario, autorización de dispositivos, sesiones, acciones sensibles, política de autorización, auditoría y avisos, transporte, y recuperación ante pérdida de la credencial. Termina con cinco decisiones que ambos colaboradores deben confirmar.

Se enlaza desde el [README de arquitectura](../03-arquitectura/README.md) y se actualiza el [roadmap](../01-proyecto/roadmap.md) con el avance, los pendientes y el siguiente paso. No cambia [ADR-005](../13-adrs/ADR-005-modelo-core.md), ADR-003 ni ADR-004, ni los contratos de los agentes de desarrollo; no requiere una nueva ADR hasta que se acuerde la propuesta.

## Verificación

Comprobaciones locales sobre los cuatro archivos del cambio: sin espacios finales y con salto de línea final; todos los enlaces relativos y anclas resueltos. No se consultan enlaces web.

## Pendientes, siguiente paso y recuperación

Los pendientes y el siguiente paso se consultan en el [roadmap](../01-proyecto/roadmap.md): revisión y acuerdo de ambos colaboradores; después, ADR-006 y actualización de `docs/12-modulos/01-identidad-seguridad.md`, de los módulos afectados y del bloque 1 de decisiones transversales. GitHub y Asana se gestionan manualmente.

La recuperación, si se solicita, consiste en retirar la propuesta y este registro y revertir las modificaciones del roadmap y del README de arquitectura, preservando cambios ajenos.