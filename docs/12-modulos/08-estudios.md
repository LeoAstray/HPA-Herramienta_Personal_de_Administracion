# Módulo 8 — Estudios — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un modelo de datos definitivo ni una integración con plataformas educativas externas.

## Propósito

Permitir al propietario organizar su trayectoria formativa (cursos, asignaturas, exámenes, certificaciones) y las fechas y documentos asociados a ella, como un dominio propio y no como una colección suelta de tareas y archivos.

## Problema que resuelve

La vida formativa de una persona —cursos en marcha, exámenes próximos, certificados obtenidos— no encaja bien como una simple tarea o un documento aislado: tiene su propia estructura (asignatura, convocatoria, calificación) y su propio ciclo temporal. Sin un módulo dedicado, esta información quedaría dispersa entre Tareas, Documentos y Calendario sin una vista propia que responda a "¿qué estoy estudiando y cómo me va?".

## Alcance funcional propuesto

El módulo trata la actividad formativa como una jerarquía simple de conceptos:

- `Programa o curso`: unidad formativa de nivel superior (un grado, un curso online, una certificación).
- `Asignatura o módulo formativo`: unidad dentro de un programa, si aplica.
- `Convocatoria o evaluación`: fecha o periodo en el que se evalúa una asignatura (examen, entrega, presentación).
- `Resultado`: calificación o estado obtenido en una convocatoria, si el propietario decide registrarlo.

No todo uso del módulo requiere la jerarquía completa: un curso suelto sin asignaturas, o una certificación única, deben poder registrarse sin forzar niveles innecesarios.

## Debe permitir

- Registrar un programa o curso, con o sin asignaturas dentro de él.
- Registrar convocatorias o evaluaciones asociadas a una asignatura o a un curso, con su fecha.
- Registrar el resultado de una convocatoria, si el propietario lo desea, sin obligarlo.
- Relacionar un curso, asignatura o convocatoria con documentos (apuntes, certificados) y con eventos de Calendario mediante relaciones explícitas de Core.
- Consultar el estado general de la actividad formativa: qué está en curso, qué convocatorias quedan próximas.
- Disparar, a través de Notificaciones, un aviso previo a una convocatoria próxima, de forma similar a como lo hacen Tareas y Calendario.

## No debe hacer

- No sustituye a Documentos y Archivos para guardar el contenido de apuntes o certificados: los referencia mediante relación.
- No sustituye a Calendario para la vista temporal general; expone sus fechas relevantes para que Calendario las refleje, igual que hace Tareas.
- No decide todavía si existe un cálculo automático de nota media o progreso, ni su fórmula.
- No integra plataformas educativas externas (LMS, portales universitarios) en el MVP; queda como integración futura.
- No asume más de un propietario ni comparte información formativa con terceros.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Programa o curso` | Unidad formativa de nivel superior. | Puede contener asignaturas; se relaciona con documentos y eventos mediante Core. |
| `Asignatura o módulo formativo` | Unidad dentro de un programa. | Pertenece a un programa; puede tener convocatorias propias. |
| `Convocatoria o evaluación` | Fecha o periodo de evaluación. | Pertenece a una asignatura o directamente a un curso; es la fecha relevante externa que Calendario puede reflejar. |
| `Resultado` | Calificación o estado obtenido. | Pertenece a una convocatoria; su registro es opcional para el propietario. |

## Ciclo de vida y reglas iniciales

1. El propietario registra un programa o curso, con o sin asignaturas, según lo que necesite representar.
2. Dentro de una asignatura o curso, puede registrar una o varias convocatorias con su fecha.
3. Una convocatoria puede exponerse como fecha relevante externa para que Calendario la refleje, siguiendo la misma regla que Tareas.
4. Tras la convocatoria, el propietario puede registrar un resultado; si no lo hace, la convocatoria queda simplemente como pasada, sin estado forzado de aprobado/suspenso.
5. Eliminar un programa, asignatura o convocatoria retira su registro y sus relaciones; los documentos relacionados no se eliminan, solo se desvincula la relación.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta entidades, relaciones explícitas, eventos internos y auditoría conceptual. |
| Identidad y Seguridad (1) | Autoriza quién puede ver o modificar información formativa, relevante si en el futuro hay más de un actor. |
| Configuración (2) | Puede alojar preferencias como el margen de aviso previo a una convocatoria. |
| Notificaciones (3) | Recibe los eventos de convocatoria próxima y decide cómo avisar. |
| Documentos y Archivos (5) | Destino habitual de relaciones desde un curso, asignatura o convocatoria (apuntes, certificados). |
| Calendario y Eventos (7) | Refleja las convocatorias como fechas relevantes externas, igual que hace con Tareas. |
| Búsqueda, Automatizaciones, IA/Agentes | Consumirán la información formativa como datos de dominio cuando se estudien esos módulos. |

## Seguridad, privacidad y límites de acceso

Los resultados académicos y los certificados pueden ser información sensible, por lo que su acceso debería quedar sujeto a los mismos principios de autorización que el resto del sistema, aunque en el MVP de un solo propietario esto se simplifique. Este módulo no expone resultados ni convocatorias a terceros ni a integraciones externas sin autorización explícita.

## Automatizaciones

No se propone automatización propia para el MVP más allá de disparar el evento interno que Notificaciones puede consumir para el aviso previo a una convocatoria. En el futuro podría estudiarse el cálculo automático de progreso o nota media, o la creación automática de una tarea de repaso antes de una convocatoria, pero esa lógica corresponde a Automatizaciones y no se decide aquí.

## MVP propuesto

- Registro de un programa o curso, con asignaturas opcionales.
- Registro de convocatorias con fecha y, opcionalmente, resultado.
- Relación explícita con documentos y con la vista temporal de Calendario.
- Aviso previo simple a través de Notificaciones.

Si existe cálculo automático de progreso o nota media en el MVP, y el nivel exacto de la jerarquía (programa/asignatura/convocatoria) que es obligatorio frente a opcional, son decisiones pendientes.

## Futuro, no MVP

- Cálculo automático de progreso, nota media o estadísticas de rendimiento.
- Integración con plataformas educativas externas (LMS, portales universitarios).
- Recordatorios de repaso generados automáticamente antes de una convocatoria.
- Planes de estudio o rutas formativas sugeridas.

## Decisiones pendientes

- Qué niveles de la jerarquía (programa, asignatura, convocatoria) son obligatorios en el MVP.
- Si se calcula algún indicador agregado (progreso, nota media) desde el principio o se deja para el futuro.
- Formato del resultado de una convocatoria (numérico, apto/no apto, texto libre).
- Margen de aviso previo por defecto para una convocatoria próxima.

## Trazabilidad

- Visión y alcance: `docs/01-proyecto/vision-y-alcance.md`.
- Core y relaciones: `docs/12-modulos/00-core.md`.
- Identidad y Seguridad: `docs/12-modulos/01-identidad-seguridad.md`.
- Configuración y Notificaciones: `docs/12-modulos/02-configuracion.md` y `docs/12-modulos/03-notificaciones.md`.
- Información Personal: `docs/12-modulos/04-informacion-personal.md`.
- Documentos y Archivos: `docs/12-modulos/05-documentos-y-archivos.md`.
- Tareas: `docs/12-modulos/06-tareas.md`.
- Calendario y Eventos: `docs/12-modulos/07-calendario-y-eventos.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.