# Módulo 7 — Calendario y Eventos — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un motor de calendario, un formato de recurrencia, ni una integración con calendarios externos.

## Propósito

Permitir al propietario ver y organizar en el tiempo los momentos que le importan —citas, compromisos, fechas relevantes de otros módulos— en una vista temporal única, sin obligar a cada módulo a construir su propia noción de fecha u hora.

## Problema que resuelve

Las fechas relevantes de la vida del propietario (una cita, la fecha límite de una tarea, un examen de Estudios, un vencimiento de Finanzas) surgen de módulos distintos. Sin un módulo de Calendario, no habría una vista temporal única donde verlas juntas, ni una noción común de "evento en el tiempo" que el resto de módulos pudiera reutilizar en vez de reinventar su propio concepto de fecha.

## Alcance funcional propuesto

El módulo distingue el evento propio del calendario de las fechas que otros módulos ya gestionan:

- `Evento`: bloque de tiempo con título, fecha/hora de inicio y, opcionalmente, fin, propio del calendario.
- `Fecha relevante externa`: fecha que pertenece conceptualmente a otro módulo (una fecha límite de Tareas, un examen de Estudios) y que el calendario solo refleja mediante una relación explícita de Core, sin duplicar ni tomar posesión del dato original.
- `Recurrencia`: patrón de repetición de un evento, sin definir aún su formato exacto.
- `Vista temporal`: agrupación de eventos y fechas relevantes externas por día, semana o mes, como concepto de consulta, no de almacenamiento.

La regla de fondo es que Calendario no se convierte en la fuente de verdad de fechas que ya pertenecen a otro módulo: las refleja mediante relación, y si la fecha original cambia, la reflejada debe cambiar con ella según una regla de sincronización aún por diseñar.

## Debe permitir

- Crear, editar y eliminar un evento propio del calendario, con título, fecha/hora de inicio y fin opcional.
- Consultar una vista temporal (día, semana, mes) que combine eventos propios y fechas relevantes de otros módulos mediante relación explícita.
- Relacionar un evento con otros elementos del dominio (una tarea, un documento, una persona registrada en Información Personal).
- Definir eventos recurrentes, si se aprueba para el MVP, con un patrón simple.
- Disparar, a través de Notificaciones, un aviso previo a un evento próximo.

## No debe hacer

- No gestiona el ciclo de vida de una tarea, un vencimiento financiero o una fecha de estudios: eso pertenece a su módulo de origen; Calendario solo la refleja.
- No decide todavía el mecanismo ni el formato de recurrencia (diaria, semanal, reglas tipo iCal, etc.).
- No implementa todavía sincronización con calendarios externos (Google Calendar, CalDAV u otros); queda como integración futura y requiere autorización específica.
- No asume disponibilidad de más de un actor ni gestiona invitaciones o confirmaciones de terceros, dado el alcance de un solo propietario.
- No interpreta ni sugiere eventos automáticamente en el MVP; cualquier sugerencia asistida por IA queda fuera de este módulo.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Evento` | Bloque de tiempo propio del calendario. | Puede relacionarse con tareas, documentos o personas mediante relaciones explícitas de Core. |
| `Fecha relevante externa` | Fecha que pertenece a otro módulo. | Se refleja en la vista temporal por relación, no por copia; el origen sigue siendo dueño del dato. |
| `Recurrencia` | Patrón de repetición de un evento. | Atributo del evento; su alcance en el MVP está pendiente. |
| `Vista temporal` | Agrupación de eventos y fechas por periodo. | Concepto de consulta que combina datos propios y reflejados, sin almacenamiento propio. |
| `Recordatorio de evento` | Aviso previo asociado a un evento. | Se apoya en Notificaciones; este módulo solo decide cuándo debería dispararse. |

## Ciclo de vida y reglas iniciales

1. El propietario crea un evento propio con al menos título y fecha/hora de inicio; el resto de campos son opcionales en el MVP.
2. Un módulo de origen (Tareas, Estudios, Finanzas) puede exponer una fecha relevante que Calendario refleja en su vista temporal mediante una relación explícita, sin crear un evento duplicado.
3. Si la fecha original cambia o se elimina en su módulo de origen, la reflexión en Calendario debe actualizarse o desaparecer; el mecanismo exacto de sincronización queda pendiente de diseño.
4. Antes de un evento (propio o reflejado), el módulo puede solicitar a Notificaciones que emita un aviso previo, según la preferencia del propietario.
5. Eliminar un evento propio retira su registro y sus relaciones; no afecta a los elementos relacionados de otros módulos.
6. Un evento recurrente, si se aprueba, genera ocurrencias visibles en la vista temporal; la forma de editar o cancelar una sola ocurrencia frente a toda la serie queda pendiente de diseño.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta entidades, relaciones explícitas, eventos internos y auditoría conceptual. |
| Identidad y Seguridad (1) | Autoriza quién puede ver o modificar un evento, relevante sobre todo si en el futuro hay más de un actor. |
| Configuración (2) | Aloja preferencias como la vista por defecto (día/semana/mes) o el margen de aviso previo. |
| Notificaciones (3) | Recibe los eventos de calendario (creación, próximo a ocurrir) y decide cómo avisar. |
| Tareas (6) | Fuente habitual de fechas relevantes externas reflejadas en la vista temporal. |
| Información Personal (4) | Puede ser referenciada cuando un evento involucra a una persona registrada. |
| Estudios, Finanzas, Guías | Fuentes previsibles de fechas relevantes externas cuando se estudien esos módulos. |
| Integraciones | Responsable futuro de cualquier sincronización con calendarios externos; no se decide en este módulo. |

## Seguridad, privacidad y límites de acceso

Un evento puede revelar información sensible por su sola existencia (una cita médica, una reunión laboral concreta), por lo que su acceso debería quedar sujeto a los mismos principios de autorización que el resto del sistema, aunque en el MVP de un solo propietario esto se simplifique. Las fechas relevantes externas reflejadas no deberían exponer más detalle del que el módulo de origen autoriza a mostrar en una vista temporal compartida.

## Automatizaciones

No se propone automatización propia para el MVP más allá de disparar el evento interno que Notificaciones puede consumir para el aviso previo. En el futuro podría estudiarse la creación automática de eventos a partir de otros módulos (p. ej. bloquear tiempo para una tarea), pero esa lógica corresponde a Automatizaciones y no se decide aquí.

## MVP propuesto

- Creación, edición y eliminación de un evento propio con título, inicio y fin opcional.
- Vista temporal básica (al menos una de día/semana/mes) que combine eventos propios y fechas relevantes reflejadas desde Tareas.
- Relación explícita con otros elementos del dominio a través de Core.
- Aviso previo simple a través de Notificaciones.

El soporte de recurrencia, el número de módulos de origen reflejados en el MVP y el mecanismo exacto de sincronización son decisiones pendientes; por ello no se presentan como requisitos aprobados.

## Futuro, no MVP

- Recurrencia completa con edición de ocurrencia única frente a serie.
- Sincronización con calendarios externos (Google Calendar, CalDAV u otros) a través de Integraciones.
- Invitaciones, confirmaciones o disponibilidad compartida si el sistema pasa a ser multiusuario.
- Sugerencias de programación asistidas por IA/Agentes.

## Decisiones pendientes

- Formato y alcance de la recurrencia en el MVP.
- Mecanismo de sincronización entre una fecha relevante externa y su reflejo en la vista temporal cuando el origen cambia.
- Qué módulos de origen se reflejan en el MVP frente a más adelante.
- Margen de aviso previo por defecto y si es configurable por tipo de evento.
- Cómo se distingue visualmente un evento propio de una fecha reflejada, si es relevante a nivel funcional.

## Trazabilidad

- Visión y alcance: `docs/01-proyecto/vision-y-alcance.md`.
- Core y relaciones: `docs/12-modulos/00-core.md`.
- Identidad y Seguridad: `docs/12-modulos/01-identidad-seguridad.md`.
- Configuración y Notificaciones: `docs/12-modulos/02-configuracion.md` y `docs/12-modulos/03-notificaciones.md`.
- Información Personal: `docs/12-modulos/04-informacion-personal.md`.
- Documentos y Archivos: `docs/12-modulos/05-documentos-y-archivos.md`.
- Tareas: `docs/12-modulos/06-tareas.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.