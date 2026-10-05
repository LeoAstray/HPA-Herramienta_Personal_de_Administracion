# Propuesta — Modelo de entidades, relaciones, eventos y auditoría de Core

## Estado

**Propuesta, ya revisada y acordada por ambos colaboradores.** Responde al bloque 2 de `docs/01-proyecto/decisiones-transversales-pendientes.md`. Se formaliza como `docs/13-adrs/ADR-005-modelo-core.md`, siguiendo `docs/00-gobierno/proceso-de-cambio.md`.

## Por qué esto primero

Todos los módulos 1 a 15 asumen que Core ya define: qué es una "entidad común", cómo se relacionan dos elementos de distintos módulos, cómo se emite y consume un "evento interno", y qué nivel mínimo de auditoría existe. El propio ADR-003 (priorización de IA/Agentes) señala explícitamente que el contrato de eventos de Core sigue sin aprobar y lo deja como prerrequisito antes de que cualquier agente interno del producto pueda operar. Esta propuesta cierra esa pieza.

## 1. Qué convierte a un concepto en entidad común

**Propuesta:** una entidad es común (vive en Core) si al menos dos módulos funcionales necesitan referenciarla sin que ninguno de los dos sea su dueño natural. El `Actor/Identidad` es el ejemplo claro: todos los módulos lo referencian, pero pertenece a Identidad y Seguridad, no a Core, por dueño natural. Lo que sí vive en Core no es el dato en sí, sino el mecanismo para que un módulo declare una entidad "referenciable" por otros: un identificador estable y una forma mínima de describirla (tipo, título breve) sin exponer su contenido completo.

**Alternativa descartada por ahora:** que Core mantenga copias de los datos de cada módulo. Se descarta porque duplicaría la fuente de verdad y contradice el principio ya usado en varios módulos ("Búsqueda no duplica, referencia"; "Calendario refleja, no posee").

## 2. Tipos y semántica de relaciones explícitas

**Propuesta:** una relación explícita es un vínculo dirigido entre dos entidades referenciables, con un tipo declarado por quien la crea (p. ej. `relacionado-con`, `depende-de`, `documenta-a`), sin que Core imponga un catálogo cerrado de tipos en el MVP. Core garantiza tres cosas sobre cualquier relación: que ambos extremos existan, que eliminar una entidad limpie las relaciones que la referencian (sin eliminar el otro extremo), y que un módulo pueda consultar "qué está relacionado con esto" sin conocer de antemano qué módulos participan.

**Pendiente dentro de esta propuesta:** si las relaciones son siempre bidireccionalmente consultables aunque se declaren en un solo sentido. Se propone que sí, por simplicidad, dado que ya lo asumen Tareas (6), Calendario (7), Estudios (8) y Finanzas (9) en sus propios documentos.

## 3. Modelo de eventos internos

**Propuesta:** un evento interno es un mensaje que un módulo emite cuando algo relevante ocurre en una de sus entidades (creación, cambio de estado, eliminación), con un tipo, una referencia a la entidad afectada y una marca de tiempo. Otros módulos (Notificaciones, Automatizaciones, Búsqueda) se suscriben a los tipos de evento que les interesan, sin que el módulo emisor necesite saber quién escucha.

Sobre entrega, reintentos e idempotencia, se proponen dos reglas de diseño, no de implementación: (a) un evento debe poder procesarse más de una vez sin duplicar su efecto (idempotencia por identificador de evento); (b) el orden de ejecución entre varias reglas de Automatizaciones que reaccionan al mismo evento no está garantizado en el MVP. La tecnología concreta es una decisión técnica posterior, no de dominio.

## 4. Separación entre Core, servicios de aplicación y módulos

**Propuesta:** Core no contiene lógica de negocio de ningún módulo. Core solo ofrece el mecanismo común (entidades referenciables, relaciones, eventos, auditoría mínima). Cada módulo funcional implementa su propia lógica y, cuando necesita algo transversal, lo hace a través de lo que Core expone, nunca accediendo directamente a los datos internos de otro módulo. Este principio coincide con el que ADR-003/ADR-004 ya aplican a los agentes de desarrollo y a los futuros agentes del producto: ningún agente obtiene acceso directo a datos o permisos que no le correspondan por contrato explícito.

## 5. Alcance mínimo de auditoría y autorización en el MVP

**Propuesta:** todo evento interno queda registrado con su tipo, entidad afectada, actor que lo originó y marca de tiempo, sin excepción, desde el MVP. La autorización concreta (quién puede hacer qué) depende del bloque 1 de decisiones transversales (identidad y permisos), todavía pendiente; esta propuesta solo fija que Core deja un lugar donde esa autorización, cuando se decida, pueda aplicarse de forma uniforme.

## Impacto si se aprueba

- `docs/12-modulos/00-core.md` pasa de "Fase 1 iniciada" con conceptos abiertos a un modelo de entidad/relación/evento concreto.
- Todos los módulos que referencian "relaciones explícitas de Core" o "eventos internos de Core" quedan respaldados por una definición real.
- El bloque 1 (identidad y permisos) queda como el siguiente bloqueador real, tal y como ya señala el roadmap actual.
- Los futuros agentes internos del producto (ADR-003/ADR-004) tendrán, cuando se aprueben, un contrato de eventos sobre el que apoyarse en vez de uno sin definir.

## Qué no resuelve esta propuesta

- El bloque 1 (identidad, permisos y sesiones) sigue abierto; aquí solo se deja el lugar donde aplicarlo.
- La tecnología concreta de mensajería/cola para eventos internos.
- El catálogo cerrado (si lo hay) de tipos de relación y de evento.

## Siguiente paso

Formalizar como ADR-005 y actualizar `docs/12-modulos/00-core.md` para que dependencias, entidades y relaciones dejen de estar en blanco.