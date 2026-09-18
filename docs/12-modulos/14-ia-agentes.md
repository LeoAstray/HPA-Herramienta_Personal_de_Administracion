# Módulo 14 — IA / Agentes — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un proveedor de modelo de IA, un mecanismo de orquestación ni un formato de contrato técnico.

## Propósito

Definir cómo un agente de IA puede consultar y operar sobre el sistema en nombre del propietario —respondiendo preguntas, sugiriendo acciones, ejecutando operaciones autorizadas— dentro de límites explícitos, sin que cada módulo tenga que exponer su propia interfaz ad-hoc para IA.

## Problema que resuelve

Varios módulos ya prevén que un agente de IA pueda, en el futuro, sugerir o generar contenido (priorización de tareas, búsqueda semántica, generación de tareas desde una guía), pero ninguno debería decidir por sí mismo cómo se comunica con un agente. Sin este módulo, cada integración de IA se construiría de forma distinta según el módulo, con riesgos de seguridad y de coherencia difíciles de controlar.

## Alcance funcional propuesto

El módulo trata la interacción con IA como un cliente autorizado más, sujeto a las mismas reglas que cualquier otro:

- `Agente`: proceso de IA (interno o externo) que puede consultar o actuar sobre el sistema en nombre del propietario, dentro de un alcance autorizado.
- `Contexto`: información que se entrega a un agente para que pueda responder o actuar, compuesta a partir de lo que los módulos exponen, nunca de acceso directo a sus datos internos.
- `Contrato de agente`: conjunto de operaciones y datos que un agente concreto puede usar, análogo al alcance de integración de Integraciones pero pensado para IA.
- `Sugerencia o acción propuesta`: resultado que produce un agente, que puede requerir confirmación explícita del propietario antes de aplicarse, según su nivel de riesgo.

Este módulo no es el agente en sí ni el modelo de IA: es la capa que decide qué puede ver y hacer un agente, y cómo se registra y confirma lo que produce.

## Debe permitir

- Definir el contrato de un agente: qué operaciones expuestas por otros módulos puede invocar y qué contexto puede recibir.
- Componer el contexto que se entrega a un agente a partir de lo que cada módulo expone, sin acceso directo a almacenamiento interno.
- Distinguir entre una consulta de solo lectura (responder una pregunta) y una acción que modifica datos, exigiendo confirmación explícita del propietario para la segunda salvo que se apruebe lo contrario para casos concretos.
- Registrar cada interacción relevante de un agente (qué se le mostró, qué propuso, qué se confirmó) para trazabilidad.
- Revocar o limitar el contrato de un agente en cualquier momento.

## No debe hacer

- No decide todavía qué proveedor o modelo de IA se usará, ni si el procesamiento ocurre localmente o en un servicio externo.
- No otorga a un agente acceso irrestricto a los datos del sistema: todo pasa por el contrato de agente y las operaciones ya expuestas por Core y los módulos funcionales.
- No ejecuta acciones sensibles o irreversibles sin confirmación explícita del propietario en el MVP.
- No sustituye a Automatizaciones: Automatizaciones ejecuta reglas declaradas explícitamente por el propietario, mientras que este módulo permite que un agente proponga o actúe de forma más flexible, siempre dentro de su contrato.
- No comparte el contexto compuesto para un agente con otros agentes o servicios sin autorización específica.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Agente` | Proceso de IA autorizado a consultar o actuar. | Se relaciona con el `Actor/Identidad` de Core que lo autorizó y con su propio contrato. |
| `Contexto` | Información entregada a un agente. | Se compone a partir de lo que los módulos exponen como consultable, análogo a lo que hace Búsqueda pero orientado a IA. |
| `Contrato de agente` | Alcance de operaciones y datos permitido. | Restringe qué puede ver y hacer un agente concreto. |
| `Sugerencia o acción propuesta` | Resultado producido por el agente. | Puede requerir confirmación del propietario antes de aplicarse, según su nivel de riesgo. |

## Ciclo de vida y reglas iniciales

1. El propietario autoriza un agente y su contrato: qué puede consultar y qué puede proponer o ejecutar.
2. Cuando el agente necesita responder o actuar, este módulo compone el contexto a partir de lo que los módulos autorizados exponen, sin exponer más de lo que el contrato permite.
3. Si el agente propone una acción que modifica datos, el sistema la presenta como propuesta y exige confirmación explícita del propietario, salvo que el contrato la haya marcado explícitamente como de bajo riesgo y autoexecutable.
4. Cada interacción relevante se registra: qué contexto se compuso, qué se propuso, qué se confirmó o rechazó.
5. Revocar el contrato de un agente detiene su capacidad de consultar o actuar de inmediato, sin afectar a las acciones ya confirmadas previamente.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta las operaciones expuestas y eventos internos sobre los que se apoya el contrato de un agente. |
| Identidad y Seguridad (1) | Autoriza y limita a los agentes de la misma forma que a cualquier otro actor, dentro del alcance de permisos del propietario. |
| Búsqueda (11) | Fuente natural de contexto para un agente que necesita localizar información antes de responder. |
| Automatizaciones (12) | Módulo hermano conceptual: comparte la idea de actuar sobre eventos y operaciones expuestas, pero con reglas declaradas frente a comportamiento más flexible de un agente. |
| Notificaciones (3) | Canal para avisar al propietario de una acción propuesta pendiente de confirmación. |
| Integraciones (13) | Si un agente depende de un modelo o servicio externo, esa conexión se gestionaría a través de Integraciones, no directamente por este módulo. |
| Todos los módulos funcionales | Fuentes previsibles de contexto y de operaciones que un agente podría invocar, siempre dentro de su contrato. |

## Seguridad, privacidad y límites de acceso

Este módulo concentra un riesgo particular porque un agente de IA puede combinar información de varios módulos de forma que ningún módulo individual expondría por sí solo. Se proponen como principios de diseño: contratos de agente explícitos y mínimos, confirmación obligatoria para acciones que modifiquen datos salvo excepción aprobada, y registro auditable completo de contexto entregado y acciones propuestas o ejecutadas. Si el procesamiento ocurre en un servicio externo, su gobierno de datos corresponde a Integraciones y a Identidad y Seguridad, no se decide en este módulo.

## Automatizaciones

Este módulo no ejecuta automatizaciones por sí mismo; las acciones que un agente propone requieren, en el MVP, confirmación del propietario. La relación con Automatizaciones (reglas declaradas frente a comportamiento generado por IA) queda como un límite conceptual a mantener claro cuando ambos módulos se implementen.

## MVP propuesto

Dado que ningún módulo funcional exige aún una capacidad de IA concreta, el MVP de este módulo podría limitarse a definir el contrato (agente, contexto, confirmación) sin conectar todavía un modelo de IA real, o bien esperar a que se apruebe un primer caso de uso concreto. Esta decisión de alcance queda pendiente, de forma similar a Integraciones.

## Futuro, no MVP

- Primer agente concreto conectado a un modelo o servicio de IA, con un caso de uso aprobado.
- Acciones de bajo riesgo marcadas como autoejecutables sin confirmación.
- Búsqueda semántica apoyada en este módulo y en Búsqueda.
- Sugerencias proactivas del agente sin que el propietario las solicite explícitamente.

## Decisiones pendientes

- Si este módulo se implementa antes de tener un caso de uso concreto de IA aprobado, o se pospone hasta entonces.
- Primer caso de uso y primer agente a soportar, si se decide avanzar.
- Qué operaciones se consideran de bajo riesgo y autoejecutables, si alguna, en el futuro.
- Dónde ocurre el procesamiento (local o externo) y cómo se gobierna esa decisión con Integraciones y Seguridad.
- Formato y detalle del registro de interacciones de un agente.

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
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.