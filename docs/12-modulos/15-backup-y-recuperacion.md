# Módulo 15 — Backup y Recuperación — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba una tecnología de copia de seguridad, un formato de backup ni una ubicación de almacenamiento concreta.

## Propósito

Garantizar que la información que el propietario ha ido registrando en todos los módulos pueda recuperarse ante pérdida, corrupción o error, y que exista un procedimiento claro para restaurarla, en vez de depender de que cada módulo resuelva esto por su cuenta.

## Problema que resuelve

Varios módulos ya han señalado explícitamente que su respaldo y recuperación quedan pendientes de decidir aquí (Documentos y Archivos, sobre todo, pero también Tareas, Calendario, Estudios y Finanzas dependen de que sus datos sobrevivan a un fallo). Sin un módulo propio, cada uno definiría su propia estrategia de copia, generando inconsistencia y, peor aún, el riesgo real de que algo no se respalde nunca porque "no era responsabilidad de nadie".

## Alcance funcional propuesto

El módulo trata el respaldo como una operación transversal sobre lo que cada módulo declara que debe conservarse:

- `Copia de seguridad`: snapshot de los datos del sistema en un momento dado, con un alcance definido (todo el sistema o un subconjunto).
- `Política de respaldo`: frecuencia y alcance con que se generan copias, aprobada explícitamente por el propietario.
- `Restauración`: operación de recuperar el sistema, o parte de él, a un estado previo a partir de una copia.
- `Verificación`: comprobación de que una copia es válida y restaurable, sin esperar a necesitarla realmente para descubrir que estaba corrupta.

Este módulo respalda datos y metadatos de los módulos funcionales; en el caso de Documentos y Archivos, según definió ese módulo, queda pendiente decidir si se respaldan los archivos físicos, solo sus metadatos y referencias, o ambos.

## Debe permitir

- Generar una copia de seguridad completa o parcial, según la política aprobada por el propietario.
- Restaurar el sistema, o un subconjunto de módulos, a partir de una copia concreta, con confirmación explícita antes de sobrescribir datos actuales.
- Verificar periódicamente que una copia existente es válida y restaurable.
- Informar al propietario, a través de Notificaciones, si una copia falla, no se genera según lo previsto, o falla su verificación.
- Consultar el historial de copias disponibles, con su fecha y alcance.

## No debe hacer

- No decide todavía la tecnología ni la ubicación física o en la nube de las copias.
- No restaura datos automáticamente sin confirmación explícita del propietario, dado el riesgo de sobrescribir información actual válida.
- No decide por sí mismo qué se considera "dato crítico" de cada módulo: cada módulo debe declarar qué necesita respaldarse; este módulo ejecuta la política, no la define en solitario.
- No sustituye al control de versiones de código del proyecto (eso es responsabilidad de las herramientas de desarrollo, no de este módulo de producto).
- No expone las copias de seguridad a integraciones externas sin que pase, si corresponde, por Integraciones y por la autorización de Identidad y Seguridad.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Copia de seguridad` | Snapshot de datos en un momento dado. | Cubre el alcance que la política de respaldo determine, a partir de lo que cada módulo declara conservable. |
| `Política de respaldo` | Frecuencia y alcance aprobados. | Configurada por el propietario, posiblemente a través de Configuración. |
| `Restauración` | Operación de recuperación desde una copia. | Requiere confirmación explícita y queda registrada para trazabilidad. |
| `Verificación` | Comprobación de validez de una copia. | Se ejecuta periódicamente o antes de confiar en una copia para restaurar. |

## Ciclo de vida y reglas iniciales

1. El propietario aprueba una política de respaldo: qué se incluye y con qué frecuencia.
2. El sistema genera copias según esa política, sin intervención manual salvo que el propietario decide forzar una copia puntual.
3. Cada copia puede verificarse; si la verificación falla, el propietario debe ser avisado para no descubrirlo solo en el momento de necesitar restaurar.
4. Ante una restauración, el propietario elige una copia del historial y confirma explícitamente antes de que el sistema sobrescriba el estado actual.
5. El historial de copias se conserva según una política de retención aún por definir, para no acumular copias indefinidamente sin control.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta el concepto transversal de qué constituye un dato del dominio a respaldar, y el registro de auditoría de restauraciones. |
| Identidad y Seguridad (1) | Autoriza quién puede configurar la política de respaldo o ejecutar una restauración, dado el riesgo de esta última. |
| Configuración (2) | Lugar natural donde alojar la política de respaldo (frecuencia, alcance). |
| Notificaciones (3) | Canal para avisar de fallos de copia, de verificación, o para confirmar que una restauración se completó. |
| Documentos y Archivos (5) | Módulo con la decisión pendiente más explícita sobre qué respaldar (metadatos, archivos físicos, o ambos). |
| Todos los módulos funcionales | Cada uno debe declarar qué datos considera críticos de conservar; este módulo ejecuta la política resultante. |
| Integraciones (13) | Si el almacenamiento de copias ocurre en un proveedor externo, esa conexión se gestionaría a través de Integraciones. |

## Seguridad, privacidad y límites de acceso

Una copia de seguridad contiene, por definición, una réplica de todos los datos sensibles del sistema (identidad, finanzas, documentos), por lo que merece al menos el mismo nivel de protección que los datos originales, y potencialmente uno mayor si se almacena fuera del sistema principal. Se proponen como principios de diseño: cifrado de las copias, acceso restringido a quien pueda configurar la política o ejecutar una restauración, y registro auditable de cada copia generada, verificada o restaurada. El mecanismo concreto de cifrado y la ubicación de almacenamiento quedan como decisión técnica pendiente.

## Automatizaciones

La generación periódica de copias según la política aprobada es, en sí misma, la automatización principal de este módulo, pero se ejecuta bajo una política explícitamente aprobada por el propietario, no bajo una regla arbitraria de Automatizaciones. La verificación periódica de copias podría plantearse como una automatización similar, con aviso ante fallo a través de Notificaciones.

## MVP propuesto

- Generación de una copia completa del sistema según una frecuencia mínima aprobada por el propietario.
- Verificación básica de que la copia generada es legible/restaurable.
- Restauración completa desde una copia, con confirmación explícita.
- Aviso al propietario si una copia falla o no se genera según lo previsto.

El respaldo parcial por módulo, la retención del historial de copias y la decisión sobre archivos físicos de Documentos y Archivos son decisiones pendientes; por ello no se presentan como requisitos aprobados.

## Futuro, no MVP

- Respaldo y restauración parcial por módulo, en vez de solo completo.
- Almacenamiento de copias en un proveedor externo a través de Integraciones.
- Política de retención configurable con expiración automática de copias antiguas.
- Restauración a un punto intermedio específico en vez de solo a la copia más reciente válida.

## Decisiones pendientes

- Frecuencia y alcance mínimo de la política de respaldo en el MVP.
- Si Documentos y Archivos respalda archivos físicos, solo metadatos, o ambos.
- Ubicación y tecnología de almacenamiento de las copias.
- Política de retención del historial de copias.
- Nivel de detalle y protección del registro de restauraciones.

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
- Automatizaciones: `docs/12-modulos/12-automatizaciones.md`.
- Integraciones: `docs/12-modulos/13-integraciones.md`.
- IA / Agentes: `docs/12-modulos/14-ia-agentes.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.