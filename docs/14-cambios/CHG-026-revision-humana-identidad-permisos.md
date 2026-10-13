# CHG-026 — Revisión humana de la propuesta de identidad, permisos y sesiones

## Estado y fuente

Registrado el 2026-10-13 a partir de la comunicación del colaborador: «el #42 lo voy a cerrar porque ambos hemos revisado la propuesta».

La declaración acredita la revisión humana de ambos colaboradores. No comunica el acuerdo sobre las cinco decisiones ni autoriza formalizar ADR-006. El cierre del issue es una acción anunciada por el colaborador; no se consulta ni se modifica GitHub.

Referencia local al registrar la comunicación: rama `dev`, HEAD `627896830b707704a8991fabc7cb626f924d0804`; blob de la [propuesta](../03-arquitectura/propuesta-identidad-permisos.md) anterior a este cambio `79fe3cf1c779a4f259c195c4a544cdf38e620683`. Es la versión local de referencia, no una identificación independiente de la versión revisada por las personas.

## Cambio documental

Se registra la revisión en el [seguimiento de identidad, permisos y sesiones del roadmap](../01-proyecto/roadmap.md#seguimiento-de-identidad-permisos-y-sesiones), con avance, pendientes y siguiente paso. El [README de arquitectura](../03-arquitectura/README.md) y la propuesta sustituyen las indicaciones de revisión pendiente por enlaces a ese seguimiento.

El contenido de la propuesta y las cinco decisiones a confirmar se conservan. CHG-025 permanece como registro histórico de su redacción. No se crea ADR-006 ni se cambian los permisos de los módulos, el workflow, la configuración o la implementación del producto.

## Verificación

Comprobaciones locales sobre los cuatro documentos afectados: `git --no-optional-locks diff --check` sin incidencias en los archivos rastreados; sin espacios finales y con salto final en los cuatro archivos, incluido CHG-026 sin rastrear. Se resuelven 30 enlaces locales, ocho de ellos con ancla, sin fallos. No son una revisión adicional del modelo ni pruebas del producto.

## Seguimiento y recuperación

La continuación se consulta en el [roadmap](../01-proyecto/roadmap.md#seguimiento-de-identidad-permisos-y-sesiones). Las operaciones Git y de publicación pertenecen al colaborador.

La recuperación, si se solicita, consiste en revertir únicamente las modificaciones de este paso y retirar CHG-026, preservando cambios ajenos.
