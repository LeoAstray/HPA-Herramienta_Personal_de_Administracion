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

## Pendiente de decisión

- Tecnología, base de datos, infraestructura, acceso remoto y autenticación.
- Modelo de dominio y relaciones transversales.
- Alcance exacto de MVP de cada módulo.
- Sincronización entre archivos físicos y su representación lógica.
- Política de búsqueda, backup, automatización y auditoría.

## Prioridad inmediata

Se prioriza el descubrimiento y diseño de IA/Agentes (ADR-003) para identificar casos de uso, agentes necesarios, criterios de evaluación de modelos y límites de datos, permisos y confirmación. Esta prioridad no aprueba un proveedor, modelo, orquestador ni código de producto. La implementación de agentes permanece condicionada por las decisiones transversales de Core e Identidad y Seguridad.

ADR-004 concreta los agentes de desarrollo para dos colaboradores: ejecución manual local en Windows, permisos por rol, operaciones Git humanas y uso exclusivo de las suscripciones. Su evaluación puede avanzar independientemente de Core e Identidad y Seguridad, que son prerrequisitos de los agentes internos del producto. Tras cuatro respuestas manuales de DEV-00, la revisión R2 superó los dos casos de comportamiento en subagentes independientes con GPT-6 Luna / Low solicitado explícitamente. Se mantiene esa selección provisional. EVAL-01 del Reviewer DEV-01 supera los criterios documentales de su caso con GPT-6.1 Sol / Medium confirmado por el colaborador, sin telemetría ni consumo atribuible. EVAL-02 se ha ejecutado con GPT-6 Luna / Medium: dos enlaces corregidos y registro CHG-016, pendientes de validación independiente EVAL-03. El colaborador aprueba provisionalmente para Developer DEV-02 GPT-6.1 Sol / Medium por defecto y GPT-6 Luna / Medium para tareas sencillas y acotadas. El próximo entregable es EVAL-03; controles efectivos, consumo y utilidad frente a una plantilla siguen pendientes. No se equipara este resultado a fiabilidad general ni a una prueba idéntica al chat manual. La configuración ejecutable compartida sigue pendiente; Reviewer, Tester, Documentación y Coordinación conservan sus candidatos.

## Convención de estado

- **Estado actual:** realidad comprobada hoy.
- **Objetivo:** resultado deseado.
- **Propuesta:** opción aún no aprobada.
- **Decisión:** opción aceptada y registrada mediante ADR cuando sea relevante.
- **Pendiente:** información o elección necesaria para avanzar.
- **Descartado:** opción excluida, con motivo si es relevante.
