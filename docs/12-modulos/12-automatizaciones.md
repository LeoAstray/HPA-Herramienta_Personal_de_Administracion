# Módulo 12 — Automatizaciones — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un motor de reglas, un lenguaje de condiciones ni un mecanismo de ejecución concreto.

## Propósito

Permitir que ocurran acciones dentro del sistema en reacción a eventos de otros módulos, sin que cada módulo tenga que implementar su propia lógica de "si pasa esto, entonces haz aquello".

## Problema que resuelve

Varios módulos ya insinúan comportamientos reactivos (una tarea generada desde una guía, un aviso escalado si no se atiende, una tarea de repaso antes de un examen), pero ninguno de ellos debería implementar esa lógica por sí mismo: acoplaría módulos entre sí de forma rígida y duplicaría reglas similares en distintos sitios. Sin un módulo de Automatizaciones, cada caso quedaría resuelto de forma ad-hoc dentro del módulo que lo necesita.

## Alcance funcional propuesto

El módulo trata la automatización como una regla declarada, no como código arbitrario:

- `Regla de automatización`: relación entre un evento interno de origen (definido por Core) y una acción resultante en un módulo destino.
- `Condición`: criterio simple que decide si la regla se activa ante un evento (p. ej. "solo si la prioridad es alta"), sin asumir un lenguaje de condiciones complejo en el MVP.
- `Acción`: efecto concreto que produce la regla al activarse (crear una tarea, disparar una notificación), siempre expresado como una operación ya expuesta por el módulo destino, nunca como acceso directo a sus datos internos.
- `Ejecución de regla`: registro de que una regla se activó, con su resultado, para trazabilidad.

Automatizaciones no inventa capacidades nuevas: orquesta capacidades que los módulos destino ya exponen (crear una tarea, enviar una notificación), respetando sus propias reglas y permisos.

## Debe permitir

- Declarar una regla que reaccione a un evento interno de un módulo de origen y ejecute una acción en un módulo destino.
- Aplicar una condición simple antes de ejecutar la acción.
- Registrar cada ejecución de una regla, con éxito o fallo, para que el propietario pueda revisar qué automatización actuó y cuándo.
- Activar o desactivar una regla sin eliminarla.
- Notificar, a través de Notificaciones, si una automatización falla de forma repetida.

## No debe hacer

- No accede directamente a los datos internos de otro módulo: solo consume sus eventos internos y llama a sus operaciones expuestas, ambos definidos por Core.
- No implementa un lenguaje de condiciones ni un motor de scripting genérico en el MVP; las condiciones son simples y acotadas.
- No decide por sí mismo qué constituye una buena práctica de automatización para cada módulo: esa responsabilidad es de cada módulo destino, que expone solo las acciones que considera seguras de automatizar.
- No ejecuta acciones irreversibles sin que el módulo destino las trate como tales (por ejemplo, nunca fuerza el borrado físico de un archivo como efecto de una regla).
- No sustituye ni compite con IA/Agentes: Automatizaciones ejecuta reglas declaradas explícitamente, no genera comportamiento nuevo por inferencia.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Regla de automatización` | Vínculo entre un evento de origen y una acción destino. | Se apoya en los eventos internos y operaciones expuestas definidos por Core. |
| `Condición` | Criterio simple de activación. | Pertenece a una regla; evalúa datos del evento, no del módulo completo. |
| `Acción` | Efecto ejecutado en el módulo destino. | Debe ser una operación ya expuesta por ese módulo, nunca acceso directo a sus datos. |
| `Ejecución de regla` | Registro histórico de una activación. | Pertenece a una regla; alimenta la trazabilidad y la auditoría conceptual de Core. |

## Ciclo de vida y reglas iniciales

1. Un módulo origen emite un evento interno definido por Core (p. ej. "convocatoria próxima" en Estudios).
2. Si existe una regla de automatización activa para ese evento y su condición se cumple, Automatizaciones invoca la acción correspondiente en el módulo destino (p. ej. crear una tarea de repaso en Tareas).
3. La ejecución, exitosa o fallida, se registra con su resultado.
4. Si una regla falla repetidamente, el propietario debe poder enterarse mediante una notificación, sin que el fallo silencioso se acumule sin control.
5. Desactivar una regla detiene su ejecución futura sin borrar su historial ni su definición.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Define el contrato de eventos internos y operaciones expuestas sobre el que se apoya toda regla. |
| Identidad y Seguridad (1) | Autoriza que una acción se ejecute dentro del alcance de permisos del actor que originó el evento, no con privilegios ampliados. |
| Notificaciones (3) | Canal para avisar de fallos repetidos de una regla, y a menudo también acción destino habitual (p. ej. "enviar una notificación" como efecto de una regla). |
| Tareas (6), Calendario (7), Estudios (8), Finanzas (9), Guías (10) | Fuentes previsibles de eventos de origen y, a la vez, destinos habituales de acciones (crear una tarea, marcar algo). |
| Búsqueda | No interactúa directamente con Automatizaciones en el MVP. |
| Integraciones, IA/Agentes | Extensiones futuras previsibles: eventos o acciones que cruzan hacia sistemas externos o hacia comportamiento asistido, no decididas en este módulo. |

## Seguridad, privacidad y límites de acceso

Toda automatización debe ejecutarse dentro del alcance de permisos del actor cuyo evento la originó, nunca con privilegios superiores a los que ese actor tendría actuando manualmente. Las acciones irreversibles o sensibles (borrar, mover archivos, ejecutar pagos) no deberían ser automatizables en el MVP salvo que el módulo destino las module explícitamente como seguras y reversibles. El registro de ejecuciones debe permitir auditar qué reglas actuaron sobre qué datos, sin exponer contenido innecesario del evento original.

## Automatizaciones (alcance de este propio módulo)

Este módulo es, en sí mismo, la capa de automatización del sistema; no tiene un submódulo separado de automatizaciones sobre sí mismo. Su propia fiabilidad (reintentos, idempotencia, orden de ejecución cuando varias reglas reaccionan al mismo evento) queda como decisión pendiente de diseño técnico, no funcional.

## MVP propuesto

- Declaración de una regla simple: evento de origen, condición básica, acción destino.
- Activación y desactivación de una regla sin eliminarla.
- Registro de ejecuciones con éxito/fallo.
- Aviso al propietario ante fallos repetidos de una misma regla.

El número y tipo de eventos/acciones disponibles en el MVP, y el lenguaje exacto de condiciones, son decisiones pendientes; por ello no se presentan como requisitos aprobados.

## Futuro, no MVP

- Condiciones compuestas o encadenamiento de varias reglas.
- Automatizaciones sugeridas o generadas asistidas por IA/Agentes.
- Automatizaciones que involucren integraciones externas.
- Panel de revisión y ajuste fino de reglas con métricas de uso.

## Decisiones pendientes

- Catálogo inicial de eventos y acciones disponibles para automatizar en el MVP.
- Lenguaje o formato de las condiciones simples permitidas.
- Política de reintentos e idempotencia cuando una acción falla.
- Orden de ejecución cuando varias reglas reaccionan al mismo evento.
- Qué acciones se consideran demasiado sensibles para automatizar en el MVP.

## Trazabilidad

- Visión y alcance: `docs/01-proyecto/vision-y-alcance.md`.
- Core y relaciones: `docs/12-modulos/00-core.md`.
- Identidad y Seguridad: `docs/12-modulos/01-identidad-seguridad.md`.
- Configuración y Notificaciones: `docs/12-modulos/02-configuracion.md` y `docs/12-modulos/03-notificaciones.md`.
- Información Personal: `docs/12-modulos/04-informacion-personal.md`.
- Documentos y Archivos: `docs/12-modulos/05-documentos-y-archivos.md`.
- Tareas: `docs/12-modulos/06-tareas.md`.
- Calendario y Eventos: `docs/12-modulos/07-calendario-y-eventos.md`.
- Estudios: `docs/12-modulos/08-estudios.md`.
- Finanzas / Planificación Salarial: `docs/12-modulos/09-finanzas.md`.
- Guías y Procedimientos: `docs/12-modulos/10-guias-y-procedimientos.md`.
- Búsqueda: `docs/12-modulos/11-busqueda.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.