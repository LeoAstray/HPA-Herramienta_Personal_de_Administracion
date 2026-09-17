# Módulo 10 — Guías y Procedimientos — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un formato de contenido, un motor de plantillas ni un mecanismo de versionado de texto.

## Propósito

Permitir al propietario registrar procedimientos propios —pasos a seguir para tareas que se repiten o que no quiere memorizar (cómo renovar un documento, cómo configurar algo, un checklist recurrente)— como conocimiento reutilizable, distinto de una tarea puntual o de un documento adjunto.

## Problema que resuelve

Ciertas actividades no son ni una tarea de una sola vez ni un archivo que se consulta pasivamente: son procedimientos con pasos que se repiten (renovar el DNI, hacer una copia de seguridad, dar de alta un servicio) y que, sin un lugar propio, se vuelven a investigar o recordar cada vez. Sin este módulo, esa información quedaría como notas sueltas dentro de Documentos, sin estructura de pasos ni relación clara con cuándo se usó por última vez.

## Alcance funcional propuesto

El módulo trata una guía como una secuencia de pasos reutilizable:

- `Guía o procedimiento`: conjunto de pasos para completar una actividad recurrente o poco frecuente, con un título y una categoría.
- `Paso`: instrucción individual dentro de una guía, con un orden y un texto descriptivo.
- `Ejecución de guía`: registro opcional de que el propietario siguió una guía en una fecha concreta, sin llegar a ser una tarea con su propio ciclo de vida.

Una guía no es una plantilla de tarea automática en el MVP: seguirla es una acción manual del propietario, aunque pueda, si se aprueba, generar una tarea o un conjunto de tareas a partir de sus pasos.

## Debe permitir

- Crear, editar y eliminar una guía con un título, una categoría y una lista ordenada de pasos.
- Consultar guías por categoría o por búsqueda simple de texto.
- Relacionar una guía con documentos de referencia (a través de Documentos y Archivos) o con otros elementos del dominio.
- Registrar, si el propietario lo desea, que ejecutó una guía en una fecha determinada, sin obligar a llevar ese historial.
- Marcar una guía como desactualizada o pendiente de revisión.

## No debe hacer

- No sustituye a Tareas como gestor de trabajo pendiente: una guía describe cómo hacer algo, no si está pendiente de hacerse, aunque pueda relacionarse con una tarea.
- No decide todavía si genera tareas automáticamente a partir de sus pasos; eso, si se aprueba, correspondería a una relación con Tareas o a Automatizaciones.
- No interpreta ni valida el contenido de los pasos: son texto libre en el MVP, sin lógica condicional ni ramas.
- No versiona formalmente el historial de cambios de una guía en el MVP, más allá de la marca de "desactualizada".
- No comparte guías con terceros ni las expone públicamente, dado el alcance de un solo propietario.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Guía o procedimiento` | Conjunto reutilizable de pasos. | Puede relacionarse con documentos de referencia y con tareas mediante Core. |
| `Paso` | Instrucción individual dentro de una guía. | Pertenece a una guía; tiene un orden dentro de ella. |
| `Categoría` | Clasificación temática de la guía. | Atributo de la guía; catálogo inicial abierto a definición. |
| `Ejecución de guía` | Registro opcional de uso en una fecha. | Pertenece a una guía; su registro es opcional para el propietario. |

## Ciclo de vida y reglas iniciales

1. El propietario crea una guía con un título y añade pasos en el orden que considere.
2. La guía puede reordenarse, editarse o marcarse como desactualizada en cualquier momento.
3. Al seguir una guía, el propietario puede, opcionalmente, registrar una ejecución con la fecha en que la usó.
4. Eliminar una guía retira su registro, sus pasos y sus relaciones; los documentos relacionados no se eliminan, solo se desvincula la relación.
5. Marcar una guía como desactualizada no la elimina ni impide consultarla; solo señala que puede necesitar revisión.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta entidades, relaciones explícitas, eventos internos y auditoría conceptual. |
| Identidad y Seguridad (1) | Autoriza quién puede ver o modificar una guía, relevante si en el futuro hay más de un actor. |
| Documentos y Archivos (5) | Destino habitual de relaciones desde una guía (manuales, capturas, referencias). |
| Tareas (6) | Relación previsible cuando el propietario decide convertir un paso o una guía completa en una tarea concreta. |
| Búsqueda | Consumirá las guías como contenido consultable cuando se estudie ese módulo. |
| Automatizaciones | Responsable futuro de cualquier generación automática de tareas a partir de una guía; no se decide en este módulo. |

## Seguridad, privacidad y límites de acceso

El contenido de una guía suele ser de menor sensibilidad que otros módulos, pero puede incluir referencias a información personal o financiera (p. ej. los pasos para renovar un documento pueden mencionar números o procedimientos concretos). Su acceso debería quedar sujeto a los mismos principios de autorización que el resto del sistema, aunque en el MVP de un solo propietario esto se simplifique. Este módulo no expone guías a terceros ni a integraciones externas sin autorización explícita.

## Automatizaciones

No se propone automatización propia para el MVP. En el futuro podría estudiarse la generación automática de una tarea o un conjunto de tareas a partir de los pasos de una guía, o un aviso periódico de revisión para guías marcadas como desactualizadas, pero esa lógica corresponde a Automatizaciones y no se decide aquí.

## MVP propuesto

- Creación, edición y eliminación de una guía con título, categoría y pasos ordenados.
- Consulta por categoría o búsqueda simple.
- Relación explícita con documentos de referencia.
- Marca manual de "desactualizada" y registro opcional de ejecución.

Si la generación de tareas a partir de una guía forma parte del MVP, y el nivel de detalle exigido en cada paso, son decisiones pendientes.

## Futuro, no MVP

- Generación automática de tareas a partir de los pasos de una guía.
- Recordatorios periódicos de revisión para guías desactualizadas.
- Plantillas de guía sugeridas o compartidas si el sistema pasa a ser multiusuario.
- Contenido enriquecido en los pasos (imágenes, enlaces estructurados) más allá de texto libre.

## Decisiones pendientes

- Catálogo inicial de categorías de guía.
- Si el registro de ejecución forma parte del MVP o se pospone.
- Nivel de detalle o formato mínimo exigido a un paso.
- Regla para marcar una guía como desactualizada (manual únicamente, o con algún aviso automático futuro).

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
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.