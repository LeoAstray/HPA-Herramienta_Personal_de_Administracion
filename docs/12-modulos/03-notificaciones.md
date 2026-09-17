# Módulo Notificaciones — estudio inicial

## Estado

**Fase 1 iniciada.** Este documento formula una propuesta conceptual; no define un canal técnico de envío, proveedor externo ni formato de mensaje concreto.

## Propósito

Definir cómo el sistema comunica al usuario eventos relevantes generados por cualquier módulo, de forma centralizada y consistente, sin que cada módulo tenga que implementar su propio mecanismo de aviso.

## Problema que resuelve

Sin un módulo de Notificaciones, cada módulo (Tareas, Calendario, Finanzas, Automatizaciones, etc.) tendría que decidir por su cuenta cómo avisar al usuario de algo, generando canales inconsistentes, avisos duplicados o contradictorios entre módulos, y ninguna forma centralizada de que el usuario gestione qué quiere recibir y cómo.

## Debe permitir

- Recibir de cualquier módulo la intención de notificar un evento (p. ej. una tarea vencida, un recordatorio de calendario, una alerta de seguridad).
- Componer y entregar ese aviso a través de uno o varios canales, sin acoplar a los módulos emisores al canal final.
- Dejar que el usuario configure, a través de Configuración, qué tipos de aviso quiere recibir y por qué canal.
- Distinguir niveles de urgencia o importancia entre notificaciones.
- Mantener un historial de notificaciones enviadas, al menos de forma básica.

## No debe hacer

- No decidir todavía el canal técnico de entrega (push, correo, mensajería, notificación local en el propio cliente web, etc.).
- No generar por sí mismo los eventos de negocio: cada módulo decide cuándo algo merece una notificación; este módulo solo la compone y la entrega.
- No gestionar permisos de quién puede notificar a quién: en el alcance actual de un solo usuario esto no aplica, pero no se cierra la puerta a que Identidad y Seguridad lo regule en el futuro.
- No implementar todavía plantillas multilingües completas, aunque debe poder apoyarse en la preferencia de idioma que gestiona Configuración.

## Entidades y relaciones — propuesta inicial

Como conceptos: `Notificación` (un aviso concreto, con origen, contenido y urgencia), `Canal` (el medio por el que se entrega, aún sin definir técnicamente) y `Preferencia de notificación` (qué quiere recibir el usuario y por dónde). Cada `Notificación` se origina en un `Evento interno` de Core, se dirige a un `Actor/Identidad`, y su entrega puede consultar las `Preferencias de notificación` almacenadas a través de Configuración.

## Dependencias

Notificaciones depende de los conceptos transversales de Core (`Evento interno`, `Actor/Identidad`) para saber qué avisar y a quién. Depende de Configuración para las preferencias de canal e idioma del usuario. Depende, en un sentido más amplio, de que el resto de módulos funcionales emitan eventos que este módulo pueda traducir en avisos, sin necesitar saber los detalles internos de cada módulo emisor.

## Seguridad y automatizaciones

Algunas notificaciones son en sí mismas mecanismos de seguridad (alertas de acceso no autorizado, cambios sensibles de configuración), por lo que su entrega no debería depender de preferencias que el usuario pueda desactivar sin restricción. Notificaciones es también el punto natural donde otros módulos y Automatizaciones podrían enganchar acciones disparadas por avisos (p. ej. escalar un aviso no atendido), aunque ese mecanismo de propagación no se define aún aquí.

## MVP y futuro

**MVP propuesto:** un canal único y simple de entrega (por ejemplo, dentro de la propia interfaz web), un modelo mínimo de notificación con urgencia y origen, y una preferencia básica de activar/desactivar por tipo de evento.
**Futuro:** múltiples canales configurables, plantillas por idioma y tipo de evento, notificaciones push a dispositivos móviles, agrupación y resumen de notificaciones, y reglas de escalado para avisos no atendidos.

## Decisiones pendientes

- Canal o canales de entrega a implementar en el MVP.
- Formato y estructura del contenido de una notificación (plantillas, texto libre, etc.).
- Qué eventos del sistema generan notificación por defecto y cuáles requieren que el usuario los active explícitamente.
- Si las notificaciones de seguridad tienen un tratamiento diferenciado que no pueda desactivarse.
- Cuánto tiempo y en qué forma se conserva el historial de notificaciones.