# Módulo 13 — Integraciones — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un proveedor externo concreto, un protocolo de autenticación ni un mecanismo de sincronización.

## Propósito

Definir cómo y bajo qué condiciones el sistema se comunica con servicios externos (calendarios, almacenamiento en la nube, banca, mensajería), de forma centralizada y controlada, sin que cada módulo funcional implemente su propia conexión a servicios de terceros.

## Problema que resuelve

Varios módulos han dejado explícitamente fuera de su alcance conexiones externas (Calendario con calendarios externos, Documentos con almacenamiento en la nube, Finanzas con bancos), señalando que esas integraciones son futuras y "corresponden a Integraciones". Sin este módulo, cada conexión externa se implementaría de forma aislada, con sus propias credenciales, permisos y riesgos, sin un punto único de control ni de revocación.

## Alcance funcional propuesto

El módulo trata cada conexión externa como una entidad gestionada, no como código embebido en el módulo que la usa:

- `Proveedor externo`: servicio de terceros con el que el sistema puede conectarse (un calendario externo, un proveedor de almacenamiento, una entidad bancaria), sin definir aún cuáles se soportan.
- `Conexión`: vínculo autorizado entre el propietario y un proveedor externo concreto, con sus credenciales o token, gestionado de forma centralizada.
- `Sincronización`: operación concreta de traer o llevar datos entre el sistema y un proveedor externo, siempre iniciada de forma explícita o según una política que el propietario aprueba.
- `Alcance de integración`: qué módulo y qué tipo de dato puede fluir a través de una conexión concreta.

Integraciones no decide qué proveedores se soportarán primero ni el orden: eso depende de qué módulos alcancen ese punto de madurez y de qué decida el propietario.

## Debe permitir

- Registrar una conexión con un proveedor externo, asociada a las credenciales necesarias, gestionadas de forma centralizada.
- Delimitar qué módulo y qué tipo de dato puede usar una conexión concreta (p. ej. una conexión a un calendario externo solo la usa Calendario y Eventos).
- Revocar una conexión en cualquier momento, deteniendo cualquier sincronización futura asociada a ella.
- Registrar cuándo se ejecutó una sincronización y su resultado, para trazabilidad.
- Avisar, a través de Notificaciones, si una conexión falla o su autorización expira.

## No debe hacer

- No decide todavía qué proveedores externos concretos se soportan en el MVP; puede que ninguno, dado que los módulos funcionales aún no lo requieren de forma aprobada.
- No otorga a un módulo acceso directo a las credenciales de una conexión: el módulo solicita una operación (leer, escribir) y este módulo la ejecuta contra el proveedor externo.
- No sincroniza datos de forma continua o en segundo plano sin que el propietario haya aprobado esa política explícitamente.
- No sustituye la lógica de negocio de cada módulo: una integración trae o lleva datos, pero el módulo destino sigue decidiendo qué hacer con ellos.
- No comparte credenciales ni datos entre distintas conexiones o proveedores.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Proveedor externo` | Servicio de terceros soportable. | Catálogo abierto, sin miembros aprobados aún. |
| `Conexión` | Vínculo autorizado con un proveedor concreto. | Se relaciona con el `Actor/Identidad` de Core que la autorizó. |
| `Sincronización` | Operación de intercambio de datos. | Pertenece a una conexión y a un alcance de integración concretos. |
| `Alcance de integración` | Delimitación de módulo y tipo de dato permitido. | Restringe qué puede fluir a través de una conexión. |

## Ciclo de vida y reglas iniciales

1. El propietario autoriza una conexión con un proveedor externo, aceptando explícitamente el alcance de integración propuesto (qué módulo, qué tipo de dato).
2. Un módulo funcional solicita una sincronización a través de este módulo, sin acceder directamente a las credenciales del proveedor.
3. Cada sincronización se registra con su resultado, éxito o fallo.
4. Si la autorización de una conexión expira o el proveedor la revoca externamente, el sistema debe detectarlo y avisar al propietario mediante Notificaciones.
5. Revocar una conexión desde el sistema detiene cualquier sincronización futura y no elimina los datos ya sincronizados, que pasan a ser gestionados por su módulo destino como cualquier otro dato.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta entidades, relaciones explícitas, eventos internos y auditoría conceptual. |
| Identidad y Seguridad (1) | Autoriza quién puede crear, usar o revocar una conexión, y protege las credenciales asociadas. |
| Notificaciones (3) | Canal para avisar de fallos de sincronización o expiración de autorización. |
| Calendario y Eventos (7), Documentos y Archivos (5), Finanzas (9) | Destinos habituales previsibles de una integración futura (calendario externo, almacenamiento en la nube, banca), aunque ninguno la requiere en su propio MVP. |
| IA/Agentes | Consumidor futuro previsible si se aprueban integraciones con asistentes o canales de voz externos. |

## Seguridad, privacidad y límites de acceso

Este módulo concentra un riesgo particular: gestiona credenciales de acceso a servicios externos. Se proponen como principios de diseño: almacenamiento centralizado y protegido de credenciales, alcance mínimo por conexión (un módulo y un tipo de dato, no acceso genérico), revocación inmediata y verificable, y registro auditable de cada sincronización. El cifrado concreto de credenciales y el protocolo de autenticación con cada proveedor quedan como decisión técnica pendiente.

## Automatizaciones

No se propone automatización propia para el MVP: toda sincronización parte de una acción explícita del propietario o de una solicitud puntual de un módulo, nunca de un proceso en segundo plano sin aprobación. En el futuro podría estudiarse la sincronización periódica automática bajo una política aprobada, coordinada con Automatizaciones, pero no se decide aquí.

## MVP propuesto

Dado que ningún módulo funcional exige aún una integración externa concreta, el MVP de este módulo podría limitarse a definir el contrato (conexión, alcance de integración, sincronización) sin implementar ningún proveedor real todavía, o bien esperar a que un módulo funcional lo requiera explícitamente. Esta decisión de alcance queda pendiente.

## Futuro, no MVP

- Soporte de un primer proveedor externo concreto (a decidir según necesidad real de un módulo, p. ej. un calendario externo).
- Sincronización periódica automática bajo política aprobada.
- Soporte de múltiples conexiones simultáneas al mismo tipo de proveedor.
- Panel centralizado de conexiones activas, su alcance y su estado.

## Decisiones pendientes

- Si este módulo se implementa antes de tener un proveedor concreto que lo necesite, o se pospone hasta entonces.
- Primer proveedor externo a soportar, si se decide avanzar.
- Protocolo de autenticación y almacenamiento de credenciales.
- Política de sincronización automática frente a manual en el futuro.
- Qué ocurre con los datos ya sincronizados cuando se revoca una conexión.

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
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.