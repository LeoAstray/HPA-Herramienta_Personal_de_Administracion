# ADR-005 — Modelo de entidades, relaciones, eventos y auditoría de Core

## Estado

Aprobada.

## Fecha

2026-10-05.

## Contexto

El estudio funcional Fase 1 de los 16 módulos quedó completo, pero todos ellos asumían un contrato común de Core (entidades referenciables, relaciones explícitas, eventos internos, auditoría) sin que ese contrato estuviera definido. `docs/01-proyecto/decisiones-transversales-pendientes.md` identificó este vacío como el bloque de decisión que más módulos condicionaba. ADR-003 (priorización de IA/Agentes) confirma, de forma independiente, que el contrato de eventos de Core sigue siendo un prerrequisito no resuelto para cualquier agente interno del producto. `docs/03-arquitectura/propuesta-modelo-core.md` desarrolló la propuesta que aquí se formaliza.

## Problema

Sin un modelo definido de qué es una entidad común, cómo se relacionan datos de distintos módulos, cómo se propagan eventos entre ellos y qué se audita como mínimo, cada módulo habría resuelto estas piezas de forma distinta, o habría quedado bloqueado esperando a que otro las resolviera primero.

## Objetivo

Fijar el modelo mínimo de dominio compartido que el resto de módulos puede dar por hecho, sin entrar en decisiones de identidad/permisos (bloque 1, todavía pendiente) ni en tecnología concreta de persistencia o mensajería.

## Decisión

Se adopta la propuesta de `propuesta-modelo-core.md` en su totalidad:

1. **Entidad común:** vive en Core cuando al menos dos módulos funcionales necesitan referenciarla sin que ninguno sea su dueño natural. Core no duplica el dato del módulo dueño; solo ofrece un identificador estable y una forma mínima de describirla (tipo, título breve).
2. **Relaciones explícitas:** vínculo dirigido entre dos entidades referenciables, con un tipo declarado libremente por quien la crea, sin catálogo cerrado en el MVP. Core garantiza integridad referencial, limpieza al eliminar una entidad, y consulta inversa aunque la relación se haya declarado en un solo sentido.
3. **Eventos internos:** mensaje emitido por un módulo cuando algo relevante ocurre en una de sus entidades, con tipo, referencia a la entidad y marca de tiempo. Los módulos se suscriben a los tipos que les interesan sin que el emisor conozca a sus consumidores. Todo evento debe poder procesarse más de una vez sin duplicar su efecto. El orden de ejecución entre reglas que reaccionan al mismo evento no está garantizado en el MVP.
4. **Separación Core / módulos:** Core no contiene lógica de negocio de ningún módulo. Cada módulo accede a lo transversal solo a través de lo que Core expone, nunca directamente a los datos internos de otro módulo — el mismo principio de mínimo acceso que ADR-003/ADR-004 aplican a los agentes de desarrollo.
5. **Auditoría mínima:** todo evento interno queda registrado con tipo, entidad afectada, actor que lo originó y marca de tiempo, desde el MVP. La autorización concreta queda para el bloque 1 (identidad y permisos), todavía pendiente.

## Principios derivados

- Ningún módulo posee datos de otro: refleja, relaciona o referencia, nunca duplica silenciosamente.
- Un módulo nuevo se integra suscribiéndose a eventos existentes, no pidiendo acceso directo a otro módulo.
- La ausencia de garantía de orden entre reglas de Automatizaciones es una restricción de diseño, no un descuido.

## Seguridad futura

El modelo de auditoría mínima queda listo para que, cuando se resuelva el bloque 1 de decisiones transversales, la autorización se aplique sobre la misma base de eventos sin rediseñar el mecanismo de registro. Cuando se aprueben agentes internos del producto (ADR-003/ADR-004), su contrato de acceso se apoyará en este mismo modelo de eventos y relaciones, no en uno nuevo.

## Impacto en módulos

Todos los módulos 1 a 15 quedan respaldados por un contrato real en vez de un concepto sin especificar. `docs/12-modulos/00-core.md` se actualiza para reflejar este modelo en sus secciones de entidades, relaciones y dependencias.

## Alcance del MVP

Entidad referenciable con identificador y descripción mínima; relaciones explícitas tipadas libremente, con integridad referencial y consulta inversa; eventos internos con entrega al menos una vez e idempotencia por identificador; registro de auditoría mínimo por evento. Sin catálogo cerrado de tipos de relación o evento, sin garantía de orden entre reglas, sin tecnología de mensajería decidida.

## Pendientes

- Bloque 1 de decisiones transversales: identidad, permisos y sesiones — ahora el siguiente bloqueador real del roadmap.
- Tecnología concreta de entrega de eventos.
- Si en algún momento conviene cerrar un catálogo de tipos de relación o de evento.

## Consecuencia

`docs/12-modulos/00-core.md` pasa de "Fase 1 iniciada" con conceptos abiertos a tener un modelo de entidad/relación/evento aprobado.

## Regla de mantenimiento

Cualquier cambio a este modelo requiere una nueva ADR que referencie esta, no una edición directa de `00-core.md` sin registro.