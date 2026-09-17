# Módulo 6 — Tareas — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un modelo de datos definitivo, un motor de recordatorios ni un mecanismo de sincronización con calendarios externos.

## Propósito

Permitir al propietario registrar, organizar y dar seguimiento a las cosas que tiene que hacer, con la información mínima necesaria para priorizarlas, relacionarlas con otros elementos del dominio (documentos, eventos, áreas personales) y saber en todo momento qué está pendiente, en curso o resuelto.

## Problema que resuelve

Las tareas cotidianas se dispersan entre notas, aplicaciones y recordatorios sueltos, sin relación con el resto de la información personal del propietario. Sin un módulo propio, no habría un lugar único donde ver qué queda pendiente, priorizarlo, ni vincular una tarea con el documento, evento o área a la que pertenece.

## Alcance funcional propuesto

El módulo tratará la tarea como una entidad de dominio con un ciclo de vida propio, distinta de un simple recordatorio de Notificaciones o de un evento de Calendario:

- `Tarea`: unidad de trabajo pendiente, con título, estado, prioridad y fechas relevantes.
- `Estado de tarea`: situación actual dentro de un ciclo de vida acotado (pendiente, en curso, completada, cancelada), sin asumir todavía un flujo más complejo tipo tablero.
- `Prioridad`: nivel orientativo de importancia u urgencia, sin un algoritmo de ordenación definido.
- `Subtarea`: unidad de trabajo dependiente de una tarea principal, si se aprueba para el MVP.

La relación entre una tarea y una fecha límite, un recordatorio o un evento de calendario se apoya en las relaciones explícitas de Core; este módulo no redefine esos conceptos.

## Debe permitir

- Crear, editar, completar, cancelar y eliminar una tarea.
- Asignar una prioridad y, opcionalmente, una fecha límite u objetivo.
- Consultar tareas filtradas por estado, prioridad o fecha.
- Relacionar una tarea con otros elementos del dominio mediante las relaciones explícitas de Core: un documento, un evento de calendario, un área personal o un ítem de otro módulo.
- Descomponer una tarea en subtareas, si se aprueba para el MVP, sin obligar a usarlas.
- Notificar, a través de Notificaciones, cambios relevantes como una fecha límite próxima o vencida.

## No debe hacer

- No sustituye a Calendario y Eventos: una tarea no es un evento con hora fija, aunque pueda relacionarse con uno.
- No decide todavía el mecanismo de recordatorio (eso corresponde a Notificaciones, que este módulo solo dispara).
- No implementa todavía vistas de tipo tablero, dependencias complejas entre tareas ni asignación a más de un actor, dado el alcance de un solo propietario.
- No interpreta ni prioriza automáticamente el contenido de una tarea en el MVP; cualquier sugerencia asistida por IA queda fuera de este módulo y corresponde, si se aprueba, a IA/Agentes.
- No borra ni modifica los elementos relacionados (documentos, eventos) como efecto colateral de cambiar el estado de una tarea.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Tarea` | Unidad de trabajo pendiente del propietario. | Puede relacionarse con documentos, eventos, áreas u otras tareas mediante relaciones explícitas de Core. |
| `Estado de tarea` | Situación dentro de un ciclo de vida acotado. | Pertenece a una tarea; su transición puede disparar eventos internos. |
| `Prioridad` | Orden orientativo de importancia. | Atributo de la tarea, sin efecto automático definido aún. |
| `Subtarea` | Trabajo dependiente de una tarea principal. | Se relaciona con su tarea principal; su alcance en el MVP está pendiente. |
| `Recordatorio de tarea` | Aviso asociado a una fecha relevante de la tarea. | Se apoya en Notificaciones; este módulo solo decide cuándo debería dispararse. |

## Ciclo de vida y reglas iniciales

1. El propietario crea una tarea con al menos un título; el resto de campos (prioridad, fecha, relaciones) son opcionales en el MVP.
2. La tarea nace en estado pendiente y avanza a en curso, completada o cancelada según la acción del propietario.
3. Cambiar el estado de una tarea puede emitir un evento interno de Core, que Notificaciones puede traducir en un aviso si corresponde.
4. Si la tarea tiene fecha límite y esta se acerca o se supera sin completarse, el módulo debe poder señalarlo, sin decidir aún el mecanismo exacto de aviso.
5. Eliminar una tarea retira su registro y sus relaciones; no afecta a los elementos relacionados (un documento o evento vinculado sigue existiendo).
6. Las subtareas, si se aprueban, siguen su propio estado pero no deberían permitir marcar la tarea principal como completada mientras queden subtareas pendientes; la regla exacta queda pendiente de diseño.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta entidades, relaciones explícitas, eventos internos y auditoría conceptual. |
| Identidad y Seguridad (1) | Autoriza quién puede crear, ver o modificar una tarea, relevante sobre todo si en el futuro hay más de un actor. |
| Configuración (2) | Puede alojar preferencias como el orden por defecto de las tareas o el horizonte de "próximas a vencer". |
| Notificaciones (3) | Recibe los eventos de tarea (creación, vencimiento próximo, completada) y decide cómo avisar, según las preferencias del propietario. |
| Documentos y Archivos (5) | Puede ser el destino de una relación explícita desde una tarea (p. ej. "revisar este documento"). |
| Calendario y Eventos | Relación previsible en ambos sentidos (una tarea con fecha puede reflejarse en el calendario), pendiente de estudiar cuando se aborde ese módulo. |
| Búsqueda, Automatizaciones, IA/Agentes | Consumirán tareas como datos de dominio cuando se estudien; sus reglas propias no pertenecen a este módulo. |

## Seguridad, privacidad y límites de acceso

El contenido de una tarea puede reflejar información personal, laboral o sensible (p. ej. el título de una tarea puede mencionar un documento financiero o un asunto médico), por lo que su acceso debería quedar sujeto a los mismos principios de autorización que el resto del sistema, aunque en el MVP de un solo propietario esto se simplifique. Los eventos internos generados por cambios de estado deberían quedar disponibles para auditoría conceptual, sin exponer contenido innecesario en notificaciones o registros cuando no sea preciso.

## Automatizaciones

No se propone automatización propia para el MVP más allá de disparar el evento interno que Notificaciones puede consumir. En el futuro podría estudiarse la creación automática de tareas a partir de otros módulos (p. ej. una tarea generada desde un evento de Calendario o desde una automatización de Documentos), pero esa integración corresponde al módulo de Automatizaciones y no se decide aquí.

## MVP propuesto

- Creación, edición, finalización, cancelación y eliminación de una tarea con título, estado y prioridad.
- Fecha límite opcional, con señalización básica de vencimiento próximo o superado.
- Relación explícita con otros elementos del dominio a través de Core.
- Listado y filtrado simple por estado y prioridad.

El soporte de subtareas, el algoritmo de ordenación por prioridad y el horizonte exacto de "próximo a vencer" son decisiones pendientes; por ello no se presentan como requisitos aprobados.

## Futuro, no MVP

- Subtareas con dependencias más ricas y bloqueo mutuo.
- Vistas de tipo tablero o agrupación por área/proyecto.
- Priorización o sugerencias asistidas por IA/Agentes.
- Tareas recurrentes.
- Asignación a más de un actor si el sistema pasa a ser multiusuario.

## Decisiones pendientes

- Si las subtareas forman parte del MVP o se posponen.
- Regla exacta de cuándo se considera una tarea "próxima a vencer".
- Si la prioridad es una escala fija o configurable.
- Qué relaciones con otros módulos se consideran parte del MVP frente a futuras.
- Si una tarea completada o cancelada se conserva indefinidamente o sigue alguna política de archivo.

## Trazabilidad

- Visión y alcance: `docs/01-proyecto/vision-y-alcance.md`.
- Core y relaciones: `docs/12-modulos/00-core.md`.
- Identidad y Seguridad: `docs/12-modulos/01-identidad-seguridad.md`.
- Configuración y Notificaciones: `docs/12-modulos/02-configuracion.md` y `docs/12-modulos/03-notificaciones.md`.
- Información Personal: `docs/12-modulos/04-informacion-personal.md`.
- Documentos y Archivos: `docs/12-modulos/05-documentos-y-archivos.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.