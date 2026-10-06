# Estado del proyecto

## Estado actual

El proyecto es una herramienta personal de administración en fase de definición. Aún no hay código de producto, modelo de datos, API, tecnología, mecanismo de acceso remoto ni autenticación aprobados.

## Objetivo del producto

Crear una aplicación web personal que centralice información cotidiana, documentos, estudios, planificación económica, guías, tareas, eventos, recordatorios y automatizaciones, con seguridad, recuperación y evolución controlada.

## Decisiones confirmadas

- Asana se usa solo para gestionar el desarrollo y no es parte del producto (ADR-001).
- El primer cliente será una web responsive. Móvil, Siri/voz y agentes IA serán futuros clientes o canales, no funciones del MVP (ADR-002).
- El MVP debe privilegiar un núcleo seguro, recuperable y extensible frente al número de funciones.
- El MVP deberá poder utilizarse desde dispositivos de la red local del usuario. El mecanismo de autenticación, cifrado, descubrimiento y control de acceso sigue pendiente de diseño.
- El modelo conceptual de entidades referenciables, relaciones, eventos y auditoría mínima de Core está aprobado por [ADR-005](../13-adrs/ADR-005-modelo-core.md); no fija tecnología ni autorización concreta.

## Pendiente de decisión

- Tecnología, base de datos, infraestructura, acceso remoto y autenticación.
- Resto del modelo de dominio y decisiones transversales; Core ya cuenta con el modelo conceptual aprobado por ADR-005.
- Alcance exacto de MVP de cada módulo.
- Sincronización entre archivos físicos y su representación lógica.
- Política de búsqueda, backup, automatización y auditoría.

## Prioridad inmediata

Se prioriza el descubrimiento y diseño de IA/Agentes (ADR-003) para identificar casos de uso, agentes necesarios, criterios de evaluación de modelos y límites de datos, permisos y confirmación. Esta prioridad no aprueba un proveedor, modelo, orquestador ni código de producto. La implementación de agentes permanece condicionada por las decisiones transversales de Core e Identidad y Seguridad.

ADR-004 concreta los agentes de desarrollo para dos colaboradores: ejecución manual local en Windows, permisos por rol, operaciones Git humanas y uso exclusivo de las suscripciones. Su evaluación puede avanzar independientemente de Core e Identidad y Seguridad, que son prerrequisitos de los agentes internos del producto. Tras cuatro respuestas manuales de DEV-00, la revisión R2 superó los dos casos de comportamiento en subagentes independientes con GPT-6 Luna / Low solicitado explícitamente. Se mantiene esa selección provisional. EVAL-01 del Reviewer DEV-01 supera los criterios documentales de su caso con GPT-6.1 Sol / Medium confirmado por el colaborador, sin telemetría ni consumo atribuible. EVAL-02 se ha ejecutado con GPT-6 Luna / Medium: dos enlaces corregidos y registro CHG-016, validados técnicamente por EVAL-03 con Tester GPT-6 Luna / Medium en el estado examinado. El colaborador aprueba provisionalmente para Developer DEV-02 GPT-6.1 Sol / Medium por defecto y GPT-6 Luna / Medium para tareas sencillas y acotadas.

EVAL-04 se registra el 2026-10-03 con Reviewer satisfactorio (Sol 6.1 / Medium confirmado), primera ejecución del Tester con incidencia de lectura de criterios del evaluador y repetición satisfactoria en detección con observaciones de presentación. Luna / Medium para Tester consta por el contexto del encargo comunicado, sin telemetría independiente. La repetición recibió una exclusión explícita de documentos adicional: las entradas no son idénticas entre todas las ejecuciones y no se garantiza evaluación ciega. Véanse resultados y fuentes en el [registro de evaluación](../10-ia/evaluacion-agentes-desarrollo.md). Controles efectivos, consumo, utilidad frente a plantilla y configuración ejecutable compartida siguen pendientes. No se equiparan estos casos a fiabilidad general ni se cierra el piloto. Reviewer, Tester, Documentación y Coordinación conservan sus candidatos.

## Avance documental del 2026-10-07

En la primera entrega del 2026-10-07 se prepara el [diseño EVAL-05](../10-ia/diseno-evaluacion-permisos-agentes.md) para el [issue #36](https://github.com/LeoAstray/HPA-Herramienta_Personal_de_Administracion/issues/36): matriz de permisos, casos sintéticos, separación del evaluador, evidencias y procedimiento. En ese momento quedan pendientes revisión, entorno, configuración y ejecución. No se lanzan agentes ni se verifican controles efectivos. Se explicita la actualización obligatoria del roadmap en cada cambio; los issues se preparan localmente para publicación manual del colaborador.

**Avance posterior:** el colaborador comunica conformidad con el diseño inicial EVAL-05 y confirma que la revisión la realiza él. Se prepara una [ficha concreta del entorno](../10-ia/entorno-eval-05.md) y una [guía humana](../10-ia/revision-eval-05-colaborador.md), pendientes de su revisión. El contexto actual declara lectura amplia, escritura sobre HPA y herramientas externas disponibles: no acredita la frontera del laboratorio. No se cambia la configuración ni se ejecutan sondas. Siguiente paso: revisar la ficha y preparar los perfiles/recursos separados antes del encargo de ejecución. [CHG-022](../14-cambios/CHG-022-preparacion-revision-y-entorno-eval-05.md) registra la preparación.

## Convención de estado

- **Estado actual:** realidad comprobada hoy.
- **Objetivo:** resultado deseado.
- **Propuesta:** opción aún no aprobada.
- **Decisión:** opción aceptada y registrada mediante ADR cuando sea relevante.
- **Pendiente:** información o elección necesaria para avanzar.
- **Descartado:** opción excluida, con motivo si es relevante.
