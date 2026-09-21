# CHG-004 — Finalización del catálogo de módulos (Fase 1)

## Estado

Documentado y aplicado a la documentación operativa. No afecta a código de producto: el repositorio no contiene implementación de producto, arquitectura técnica aprobada ni esquema de datos.

## Objetivo y alcance

Se completa el estudio funcional inicial (Fase 1) de los módulos 6 a 15 — Tareas, Calendario y Eventos, Estudios, Finanzas / Planificación Salarial, Guías y Procedimientos, Búsqueda, Automatizaciones, Integraciones, IA / Agentes y Backup y Recuperación — siguiendo el método común definido en `docs/12-modulos/README.md` y, a partir del módulo 5, la plantilla ampliada (conceptos y relaciones, ciclo de vida, dependencias e interacción, seguridad/privacidad, automatizaciones, MVP, futuro, decisiones pendientes, trazabilidad).

Con esto, los 16 módulos del catálogo (0 a 15) cuentan con documentación de análisis Fase 1, cerrando el primer objetivo del roadmap documental.

## Impacto

- **Catálogo:** `docs/12-modulos/README.md` marca los 16 módulos como "Iniciado".
- **Documentos de módulo:** se añaden `06-tareas.md` a `15-backup-y-recuperacion.md`.
- **Roadmap:** `docs/01-proyecto/roadmap.md` actualizado — el objetivo "completar el análisis conceptual de los 16 módulos" se marca alcanzado y el próximo objetivo pasa a ser "resolver decisiones de dominio que condicionan varios módulos".
- **Decisiones pendientes:** cada módulo nuevo deja su propia lista de decisiones abiertas; varias son transversales (autenticación y permisos, sincronización de fechas relevantes externas con Calendario, si Integraciones e IA/Agentes se desarrollan ahora sin caso de uso concreto o se posponen) y quedan señaladas para el siguiente objetivo del roadmap, no resueltas en este cambio.
- **Arquitectura, datos, API, interfaz, requisitos, pruebas y operaciones:** no se toma ninguna decisión ni se crea un artefacto técnico; siguen pendientes tras la Fase 1.
- **ADR y Asana:** no procede ADR ni actualización de Asana. No se ha tomado una decisión técnica o de amplio impacto y no se proporcionó una referencia de Asana.

## Seguridad y privacidad

Las definiciones de los módulos añadidos mantienen los principios ya establecidos: mínimo privilegio, separación entre registro lógico y dato sensible, y ausencia de operaciones automáticas irreversibles sin confirmación explícita. Los módulos con mayor sensibilidad (Finanzas, Identidad y Seguridad, Backup y Recuperación) señalan explícitamente principios de diseño de seguridad propios, sin fijar aún mecanismo técnico. No se incluyen secretos ni datos personales reales.

## Verificación y rollback

Se debe comprobar que la secuencia `00`–`15`, el catálogo y los enlaces internos coinciden, y que el roadmap refleja el estado real del catálogo. Las fuentes históricas bajo `docs/general-docs/fuentes/` conservan su redacción original y no se alteran. El rollback consiste en revertir los archivos de documentación cambiados; no altera datos, servicios ni infraestructura.

## Documentación relacionada

- `docs/12-modulos/README.md`
- `docs/12-modulos/06-tareas.md` a `docs/12-modulos/15-backup-y-recuperacion.md`
- `docs/01-proyecto/roadmap.md`
- `docs/00-gobierno/estado-proyecto.md`