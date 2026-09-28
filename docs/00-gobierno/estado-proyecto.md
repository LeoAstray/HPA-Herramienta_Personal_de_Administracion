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

## Convención de estado

- **Estado actual:** realidad comprobada hoy.
- **Objetivo:** resultado deseado.
- **Propuesta:** opción aún no aprobada.
- **Decisión:** opción aceptada y registrada mediante ADR cuando sea relevante.
- **Pendiente:** información o elección necesaria para avanzar.
- **Descartado:** opción excluida, con motivo si es relevante.
