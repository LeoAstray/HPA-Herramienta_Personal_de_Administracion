# Decisiones transversales pendientes

## Propósito

El roadmap documental fija como próximo objetivo "resolver decisiones de dominio que condicionan varios módulos", antes de diseñar la arquitectura global. Este documento reúne, a partir de la sección "Decisiones pendientes" de cada uno de los 16 estudios de módulo, las preguntas que no son específicas de un solo módulo sino que varias de sus respuestas obligarían a otros módulos a ajustarse. El objetivo es resolverlas una vez, no dieciséis veces.

No es un ADR: ninguna de estas preguntas está decidida aquí. Cuando se resuelva una, debe registrarse como ADR según `docs/00-gobierno/proceso-de-cambio.md` y reflejarse en los módulos afectados.

## Cómo leer este documento

Cada bloque agrupa una pregunta de fondo, qué módulos la plantearon (entre paréntesis, con su número) y qué se bloquea mientras no se resuelva. Al final se listan las decisiones que, tras revisar los 16 módulos, resultaron ser realmente específicas de un solo módulo y por tanto no transversales: esas se dejan para cuando se retome ese módulo, no para esta ronda.

## 1. Identidad, permisos y sesiones

**Pregunta de fondo:** ¿cómo se autentica el propietario, qué mecanismo de sesión/dispositivo se usa en la red local, y qué nivel de permiso exige cada acción sensible?

- Mecanismo concreto de autenticación, cifrado y descubrimiento de dispositivos en la red local (1).
- Modelo de sesiones: duración, expiración, revocación, renovación (1).
- Alcance mínimo de permisos en el MVP de un solo propietario (1), y alcance mínimo de auditoría/autorización en Core (0).
- Qué ajustes de Configuración se consideran sensibles y qué permiso exigen modificarlos (2).
- Quién puede configurar la política de respaldo o ejecutar una restauración (15).
- Nivel de acceso a información financiera y a rutas de Documentos y Archivos (9, 5) — dependen directamente de este modelo, no deciden uno propio.

**Bloquea:** el modelo de `Actor/Identidad` de Core, y cualquier decisión de permisos en Identidad y Seguridad, Configuración, Documentos, Finanzas y Backup queda provisional hasta resolver esto.

## 2. Modelo de eventos internos, relaciones y auditoría de Core — RESUELTO (ADR-005)

**Pregunta de fondo:** ¿qué hace que algo sea una "entidad común" de Core, cómo se tipan las relaciones explícitas entre módulos, y cómo se entregan los eventos internos (reintentos, idempotencia, orden)?

- Qué convierte a un concepto en entidad común; tipos y semántica de relaciones; modelo de eventos internos, entrega, reintentos e idempotencia; separación entre Core, servicios de aplicación y módulos (0).
- Política de reintentos e idempotencia cuando una acción de Automatizaciones falla; orden de ejecución cuando varias reglas reaccionan al mismo evento (12).
- Cómo se notifica a un módulo que uno de sus ajustes ha cambiado (2).
- Si el registro de auditoría de accesos vive en Identidad y Seguridad o se apoya enteramente en el concepto de Core (1).

**Bloquea:** literalmente todo lo demás. Notificaciones, Automatizaciones, Búsqueda e IA/Agentes están definidos como consumidores de "eventos internos" y "operaciones expuestas" de Core, pero ese contrato no existe todavía como decisión, solo como concepto. Es razonable tratar esta como la primera decisión de dominio a cerrar.

## 3. Sincronización de fechas relevantes externas con Calendario

**Pregunta de fondo:** cuando Tareas, Estudios o Finanzas exponen una fecha (vencimiento, convocatoria, vencimiento financiero) para que Calendario la refleje, ¿qué mecanismo garantiza que se actualice o desaparezca si el dato original cambia?

- Mecanismo de sincronización entre una fecha relevante externa y su reflejo en la vista temporal (7).
- Qué módulos de origen se reflejan en el MVP frente a más adelante (7).
- Regla exacta de cuándo una tarea se considera "próxima a vencer" (6), margen de aviso previo para una convocatoria (8) y nivel de detalle permitido en una notificación de vencimiento financiero (9) — son la misma pregunta de "margen y contenido de aviso previo" repetida en tres módulos.

**Bloquea:** el diseño concreto de Calendario y Eventos, y cualquier automatización que dependa de "algo está próximo a vencer".

## 4. Alcance ahora vs. esperar caso de uso: Integraciones e IA/Agentes

**Pregunta de fondo:** ambos módulos señalan que ningún otro módulo exige todavía una integración externa o una capacidad de IA concreta. ¿Se define su contrato ahora, en abstracto, o se pospone hasta que exista un primer caso de uso real?

- Si Integraciones se implementa antes de tener un proveedor concreto que lo necesite (13).
- Si IA/Agentes se implementa antes de tener un caso de uso concreto aprobado (14).

**Bloquea:** cuánto esfuerzo de diseño dedicarle a estos dos módulos en esta ronda frente a otros con necesidad más inmediata (Tareas, Documentos, Finanzas).

## 5. Retención y política de archivo de datos resueltos

**Pregunta de fondo:** varios módulos generan datos que, tras completarse, podrían conservarse indefinidamente o purgarse/archivarse según una política común.

- Si una tarea completada o cancelada se conserva indefinidamente o sigue una política de archivo (6).
- Cuánto tiempo y en qué forma se conserva el historial de notificaciones (3).
- Si existe historial de búsquedas y cómo se protege (11).
- Política de retención del historial de copias de seguridad (15).

**Bloquea:** poco a nivel de arquitectura inmediata, pero conviene fijar un criterio común de retención antes de diseñar el modelo de datos, para no resolverlo de forma distinta en cada módulo.

## Decisiones específicas, no transversales

Tras revisar los 16 módulos, estas quedaron como preguntas de un solo módulo, sin condicionar a otros de forma directa. Se dejan para cuando se retome ese módulo en detalle, no para esta ronda:

- Documentos y Archivos (5): identidad estable de archivo movido/renombrado externamente; política de referencias rotas y duplicados; criterios de contenido no confiable.
- Información Personal (4): campos concretos del perfil; historial de cambios propio.
- Tareas (6): si las subtareas entran en el MVP; escala de prioridad fija o configurable.
- Estudios (8): niveles obligatorios de la jerarquía; formato del resultado de una convocatoria.
- Finanzas (9): catálogo de categorías; soporte multimoneda.
- Guías (10): catálogo de categorías; formato mínimo de un paso.
- Búsqueda (11): campos buscables por módulo; frecuencia de actualización del índice.
- Backup (15): si Documentos respalda archivos físicos, solo metadatos, o ambos.

## Siguiente paso

Resolver los bloques 1 y 2 primero — son los que condicionan literalmente al resto —, después el 3, y decidir el 4 como una elección de alcance/tiempo más que de diseño. El bloque 5 puede resolverse en paralelo, como un criterio corto y común. Cada resolución debe registrarse como ADR y reflejarse en los módulos listados en su bloque.