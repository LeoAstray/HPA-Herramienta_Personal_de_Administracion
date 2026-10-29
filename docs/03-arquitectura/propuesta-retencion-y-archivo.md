# Propuesta — Política común de retención y archivo

## Estado

**Propuesta pendiente de revisión.** No es una decisión ni aprueba plazos, permisos ni cambios en los módulos. Primera entrega del issue #61 (ARQ-4) y respuesta al bloque 5 de [decisiones transversales pendientes](../01-proyecto/decisiones-transversales-pendientes.md). La adopción y la actualización de los documentos afectados se coordinan solo tras el acuerdo de ambos colaboradores.

## Por qué ahora

Tareas (6), Notificaciones (3), Búsqueda (11) y Backup y Recuperación (15) dejan abierta, cada uno por su lado, qué se conserva, durante cuánto tiempo y en qué forma. Si cada módulo lo resuelve por separado, el resultado puede ser incompatible: por ejemplo, una tarea eliminada que sigue visible en el historial de copias, o una notificación conservada con un contenido que su módulo de origen ya no conserva.

## Alcance y exclusiones

Esta propuesta cubre únicamente cuatro categorías: tareas resueltas, historial de notificaciones, posible historial de búsquedas e historial de copias de seguridad.

No propone plazos concretos, purgas, borrado seguro ni limpieza de copias reales. No implementa nada ni modifica la auditoría mínima de [ADR-005](../13-adrs/ADR-005-modelo-core.md). La sincronización temporal entre módulos corresponde a ARQ-3 (#60). No analiza si algún dato está sujeto a obligaciones externas de conservación.

## Principios propuestos

1. **Conservar con finalidad.** Cada categoría declara para qué se conserva; sin finalidad vigente, sus elementos pasan a ser candidatos a archivo o eliminación.
2. **Tres estados.** Un elemento está activo, archivado (fuera de las vistas por defecto y recuperable) o eliminado (se retira su registro y sus relaciones). Si el estado "archivado" es común o propio de cada módulo es una decisión humana pendiente.
3. **Sin eliminación automática sin criterio aprobado.** Ningún elemento se archiva o elimina por tiempo o cantidad hasta que el propietario apruebe el criterio. Los valores concretos no se proponen aquí.
4. **Eliminar un registro no toca archivos físicos.** Se mantiene lo ya definido en [Documentos y Archivos](../12-modulos/05-documentos-y-archivos.md): retirar un registro lógico no borra el archivo físico.
5. **Separar lo existente de lo propuesto.** Cada fila de la matriz indica si la capacidad ya figura en el módulo, está solo propuesta o no existe.

## Alternativas de retención

- **A. Conservar sin límite** hasta que el propietario elimine.
- **B. Archivar según criterio** (estado, antigüedad u otro que fije el propietario), conservando el elemento recuperable.
- **C. Eliminar según criterio** tras un plazo fijado por el propietario.
- **D. Conservar solo los N más recientes** y eliminar los anteriores.
- **E. No conservar** (no registrar el dato).

## Matriz por categoría

| Categoría | Capacidad actual | Propósito de conservar | Sensibilidad | Alternativas | Consecuencias |
| --- | --- | --- | --- | --- | --- |
| Tareas completadas o canceladas | [Tareas](../12-modulos/06-tareas.md) define completar, cancelar y eliminar. El archivo no está definido. | Consultar lo hecho y mantener relaciones con documentos o eventos. | Media: el título puede revelar asuntos personales o laborales. | A, B, C | A acumula elementos y exige filtros en listados y búsqueda. B añade un estado nuevo al ciclo de vida de Tareas y exige un criterio. C reduce la acumulación, pero pierde el histórico y obliga a limpiar relaciones. |
| Historial de notificaciones | [Notificaciones](../12-modulos/03-notificaciones.md) propone un historial "al menos básico", sin plazo ni forma. | Comprobar qué se avisó y diagnosticar fallos de entrega. | Media-alta: puede contener contenido derivado de módulos sensibles. | A, C, D | A mantiene indefinidamente contenido potencialmente sensible. C o D limitan esa exposición, pero se pierde el rastro. Los avisos de seguridad pueden merecer un tratamiento aparte (ver decisiones). |
| Historial de búsquedas | **No existe ni está aprobado.** [Búsqueda](../12-modulos/11-busqueda.md) indica que la consulta no se almacena salvo que se apruebe. | Solo hipotético: sugerencias o búsquedas recientes. | Alta si existiera: revela intereses y consultas sobre datos sensibles. | E (situación actual); C o D solo si se aprobara | E no tiene coste ni utilidad. Si algún día se aprueba, quedaría sujeto a esta política antes de existir y requeriría decidir su protección y qué módulos excluye. |
| Historial de copias de seguridad | [Backup y Recuperación](../12-modulos/15-backup-y-recuperacion.md) propone un historial consultable. La retención está "por definir" y la expiración automática figura como futuro. | Poder restaurar a un estado previo ante pérdida o corrupción. | Muy alta: cada copia replica datos sensibles de todos los módulos. | A, C, D | A consume almacenamiento y conserva datos ya eliminados sin límite. D es simple, pero limita cuánto se puede retroceder. C fija un plazo por antigüedad. En todos los casos, un dato eliminado en la aplicación sigue recuperable en las copias anteriores hasta que estas expiren. |

## Casos documentados

**1. Archivar una tarea completada (propuesto).** Sale de las vistas por defecto, conserva sus relaciones y el propietario puede recuperarla. Queda por decidir si sigue apareciendo en Búsqueda y cómo se refleja su fecha en Calendario; esto último pertenece a ARQ-3 (#60).

**2. Eliminar una tarea.** Se retira su registro y sus relaciones, como ya define Tareas y garantiza ADR-005. Los documentos o eventos vinculados siguen existiendo sin ese vínculo. Se emite el evento y la auditoría mínima de ADR-005. La eliminación es irreversible salvo que exista una copia de seguridad que la contenga.

**3. Restaurar un elemento archivado.** Vuelve al estado activo y recupera su lugar en las vistas. Sus relaciones siguen válidas mientras los otros extremos existan. Si alguno se eliminó mientras tanto, esa relación ya no existe y no se recrea.

**4. Restaurar desde una copia de seguridad.** Requiere confirmación explícita, según Backup y Recuperación. Puede reintroducir elementos eliminados después de la copia y dejar relaciones hacia elementos que ya no existen o duplicados. Si tras restaurar se reaplican las eliminaciones posteriores a la copia es una decisión humana pendiente.

**5. Referencias a un elemento retirado.**
- *Archivado:* la relación se mantiene y el elemento se muestra como archivado.
- *Eliminado:* la relación se limpia (ADR-005) y el otro extremo sigue existiendo sin ella.
- *Auditoría:* el registro conserva el identificador de la entidad aunque ya no exista. ADR-005 no define si conserva también su descripción mínima; queda como pregunta abierta, sin modificar ADR-005.

**6. Retirar un registro de Documentos y Archivos.** Se retira el registro lógico y sus relaciones; el archivo físico no se toca. La política común no autoriza ningún borrado de archivos físicos.

## Permisos

No se definen permisos concretos. Quién puede archivar, eliminar, restaurar o fijar criterios depende del acuerdo del bloque 1. La [propuesta de identidad, permisos y sesiones](propuesta-identidad-permisos.md) sigue pendiente de acuerdo y ADR-006 no existe. Esa propuesta incluye entre las acciones sensibles a confirmar la restauración de copias y el borrado de datos financieros en bloque.

## Decisiones humanas pendientes

1. Si "archivado" es un estado común del sistema o cada módulo define el suyo.
2. Qué categorías admiten archivo y cuáles solo conservar o eliminar.
3. Quién fija los criterios y plazos. Propuesta: el propietario, sin valores por defecto hasta que se decidan.
4. Excepciones: si los avisos de seguridad se conservan con un criterio distinto, y cómo tratar los datos con posible obligación externa de conservación, que esta propuesta no analiza.
5. Si se acepta que un dato eliminado persista en copias anteriores hasta que expiren, o se estudia un mecanismo de purga, que queda fuera de este alcance.
6. Si restaurar una copia reaplica las eliminaciones posteriores.
7. Si el historial de búsquedas se aprueba como capacidad o se descarta.
8. Si un elemento archivado sigue apareciendo en Búsqueda.
9. Si la auditoría conserva la descripción mínima de una entidad eliminada.

## Adopción

Si se acuerda, la actualización coordinada, a cargo de un único integrador, afectaría a los módulos 3, 6, 11 y 15, al bloque 5 de decisiones transversales y al README de arquitectura. Se abriría una ADR solo si se decide formalizar el acuerdo. Hasta entonces, ningún documento distinto de esta propuesta se modifica.