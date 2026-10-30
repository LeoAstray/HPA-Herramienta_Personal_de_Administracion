# Propuesta — Sincronización de fechas y avisos entre módulos

## Estado

**Propuesta pendiente de revisión.** No es una decisión ni aprueba valores, permisos ni cambios en los módulos. Primera entrega del issue #60 (ARQ-3) y respuesta al bloque 3 de [decisiones transversales pendientes](../01-proyecto/decisiones-transversales-pendientes.md). La adopción y la actualización de los documentos afectados se coordinan solo tras el acuerdo de ambos colaboradores.

## Por qué ahora

Tareas (6), Estudios (8) y Finanzas (9) son dueños de fechas que [Calendario y Eventos](../12-modulos/07-calendario-y-eventos.md) debe reflejar. Calendario indica que el mecanismo para actualizar o retirar ese reflejo "queda pendiente de diseño". Además, Tareas, Estudios y Finanzas repiten la misma pregunta sobre cuándo y con qué contenido avisar. Sin un reparto común, el mismo vencimiento podría avisarse dos veces o no avisarse.

## Alcance y exclusiones

Esta propuesta cubre la relación entre el módulo de origen y Calendario, qué ocurre al dar de alta, cambiar o retirar una fecha, y el reparto de responsabilidades de los avisos entre origen, Calendario, Configuración y Notificaciones.

No propone un motor de calendario ni un planificador técnico, recurrencia completa, calendarios externos, permisos nuevos ni una garantía global de orden de eventos. No define la retención de elementos resueltos, que corresponde a ARQ-4 (#61). No introduce valores concretos de márgenes de aviso.

## Principios propuestos

1. **El origen conserva la propiedad.** La fecha pertenece al módulo que la crea. Calendario la refleja mediante una relación explícita de Core y nunca la edita ni la copia como dato propio.
2. **Un único emisor de aviso por fecha.** Para cada fecha, exactamente un módulo es responsable de decidir que "toca avisar": su dueño. Calendario no emite avisos de fechas que solo refleja.
3. **El estado vigente lo tiene el origen.** Ante cualquier duda sobre una fecha, se consulta al origen. Un evento recibido nunca prevalece sobre el estado actual del origen.
4. **Tolerancia a repetición y desorden.** El mecanismo funciona con la entrega al menos una vez e idempotente que define [ADR-005](../13-adrs/ADR-005-modelo-core.md), sin pedir orden entre eventos ni añadir campos al evento.

## Alternativas de mecanismo de reflejo

- **M1. Reflejo por consulta.** Calendario no guarda la fecha. Al construir la vista temporal pregunta a cada origen por sus fechas relevantes en el rango, siguiendo las relaciones de Core. Un cambio o retirada se refleja solo, porque no hay copia. Exige que cada origen exponga esa consulta y no sirve por sí solo para disparar avisos.
- **M2. Reflejo por eventos.** Calendario mantiene una proyección derivada, actualizada con los eventos de alta, cambio y retirada. La consulta es rápida, pero debe tolerar repeticiones y desorden y puede divergir del origen.
- **M3. Híbrido.** Proyección por eventos más una comprobación contra el origen al abrir la vista o de forma periódica. Combina rapidez y corrección, a cambio de más piezas.

Calendario ya describe la vista temporal como "concepto de consulta ... sin almacenamiento propio", lo que encaja con M1. La elección es una decisión humana.

## Alcance de orígenes en el MVP

- **S1. Solo Tareas.** Es lo que describe hoy el MVP de Calendario.
- **S2. Tareas y Estudios.** Añade convocatorias.
- **S3. Tareas, Estudios y Finanzas.** Añade vencimientos financieros.

Con S3 una vista de calendario revela la existencia de compromisos financieros, por lo que su acceso queda condicionado al acuerdo de identidad (ver "Acceso").

## Reparto de responsabilidades

| Pieza | Responsabilidad propuesta |
| --- | --- |
| Módulo de origen | Es dueño de la fecha y de su estado. Decide cuándo una fecha propia está próxima y emite el aviso debido, una sola vez por fecha vigente. Deja de avisar si el elemento se resuelve, cancela o retira. |
| Calendario | Refleja las fechas por relación y las muestra en la vista temporal. Emite avisos solo de sus eventos propios, nunca de fechas reflejadas. |
| Configuración | Aloja los márgenes de aviso y las preferencias de canal. No se proponen valores. |
| Notificaciones | Entrega el aviso (canal, idioma, preferencias) y evita entregar dos veces el mismo aviso. |
| Core | Aporta las relaciones, los eventos, la idempotencia y la auditoría mínima de ADR-005, sin cambios. |

**Definición única de "próximo a vencer".** Una fecha está próxima cuando la fecha vigente menos su margen es anterior o igual al momento actual, y la fecha aún no ha pasado. El margen se define por tipo de fecha (tarea, convocatoria, vencimiento financiero) y se guarda en Configuración. Sustituye las tres preguntas separadas de Tareas, Estudios y Finanzas.

**Prevención de duplicados.** Cada aviso se identifica por el origen, la entidad, la fecha vigente y el margen. Notificaciones no entrega dos avisos con la misma identidad. Si la fecha cambia, la identidad cambia y el aviso pendiente anterior queda sustituido.

## Contenido mínimo del aviso

Todo aviso incluye el tipo de fecha, un título breve del origen, la fecha y hora, y una referencia al elemento. Para los vencimientos financieros se proponen estas alternativas:

- **a.** Un aviso genérico, sin título ni importe ("Tienes un vencimiento próximo").
- **b.** El título breve que eligió el propietario, sin importe.
- **c.** Título e importe. Contradice el principio de minimizar la exposición en notificaciones; solo se consideraría por decisión expresa.

## Casos documentados

**1. Alta.** El origen crea la fecha y su relación con Calendario. Con M1 aparece en la vista al consultar; con M2 o M3 se proyecta al recibir el evento. El origen empieza a vigilar su vencimiento.

**2. Cambio de fecha.** El origen conserva la nueva fecha. Calendario la muestra actualizada (M1) o tras aplicar el evento (M2, M3). La identidad del aviso cambia: el aviso pendiente con la fecha anterior queda sustituido y se evalúa la nueva. Un aviso ya entregado con la fecha anterior no se retira; si debe corregirse es una decisión pendiente.

**3. Retirada.** Si la fecha se elimina, o el elemento se resuelve o cancela, deja de reflejarse y sus avisos pendientes se cancelan. Al eliminar una entidad, ADR-005 limpia sus relaciones. Si una fecha resuelta queda visible como histórico o desaparece, y qué ocurre al archivar, es una decisión pendiente; lo segundo se trata en #61.

**4. Evento repetido.** El mismo evento llega dos veces. Se procesa de forma idempotente, sin efecto adicional. Un aviso con la misma identidad no se entrega por segunda vez.

**5. Eventos fuera de orden.**
- *Cambio antiguo después de otro más reciente:* se descarta por tener una marca de tiempo anterior a la ya aplicada para esa entidad. Si no es concluyente, se consulta al origen.
- *Retirada antes del alta:* al comprobar contra el origen, la entidad no existe y no se crea el reflejo.
- *Aviso debido de una fecha ya cambiada:* se verifica la identidad contra el estado actual del origen; si ya no coincide, se descarta.

## Acceso

No se definen permisos nuevos. Un evento reflejado no debe mostrar más detalle del que el módulo de origen autoriza, como ya indica Calendario. El acceso a fechas de Tareas, Estudios y Finanzas queda condicionado al acuerdo de la [propuesta de identidad, permisos y sesiones](propuesta-identidad-permisos.md), que sigue pendiente de acuerdo. El principio de [seguridad](../07-seguridad/README.md) de minimizar la exposición en las notificaciones se aplica al contenido del aviso.

## Decisiones humanas pendientes

1. Mecanismo de reflejo: M1, M2 o M3.
2. Orígenes del MVP: S1, S2 o S3.
3. Aceptar la definición única de "próximo a vencer" y quién fija los márgenes por tipo. Los valores no se proponen aquí.
4. Contenido financiero mínimo del aviso: a, b o c.
5. Si una fecha de un elemento resuelto sigue visible como histórico.
6. Si un aviso ya entregado se corrige o retira cuando la fecha cambia.
7. Si Calendario usa el mismo margen configurable para los avisos de sus eventos propios.
8. Si en el futuro conviene una versión explícita en el evento, lo que exigiría ampliar el evento definido por ADR-005 y no se plantea ahora.

## Adopción

Si se acuerda, la actualización coordinada, a cargo de un único integrador, afectaría a los módulos 2, 3, 6, 7, 8 y 9, al bloque 3 de decisiones transversales y al README de arquitectura. Se abriría una ADR solo si se decide formalizar el acuerdo. Hasta entonces, ningún documento distinto de esta propuesta se modifica.