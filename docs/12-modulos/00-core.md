# Módulo 0 — Core — estudio inicial

## Estado

**Fase 1 — modelo de entidades, relaciones, eventos y auditoría aprobado por ADR-005.** La tecnología concreta de persistencia y de entrega de eventos sigue sin definirse; ver `docs/13-adrs/ADR-005-modelo-core.md`.

## Propósito

Ofrecer capacidades y reglas transversales para que los módulos del producto se relacionen de forma coherente sin depender de una interfaz, de Asana ni de una integración externa concreta.

## Problema que resuelve

Evita que cada módulo invente su propia manera de identificar objetos, enlazarlos, aplicar reglas comunes o comunicar cambios. Sin un núcleo conceptual, Tareas, Calendario, Documentos e Información Personal tenderían a acoplarse entre sí o a la interfaz web.

## Debe permitir

- Operaciones de negocio reutilizables desde clientes autorizados.
- Identificación, relaciones y ciclo de vida común cuando el estudio de dominio lo justifique.
- Aplicación consistente de reglas, permisos, auditoría y eventos internos.
- Límites claros para que otros módulos aporten sus reglas específicas.

## No debe hacer

- No sustituir las reglas propias de Tareas, Eventos, Documentos o Finanzas.
- No decidir la persistencia, la tecnología, la UI ni la integración de voz.
- No actuar como un cajón genérico para lógica no clasificada.
- No acceder a sistemas externos como responsabilidad principal.

## Entidades, relaciones y eventos — modelo aprobado (ADR-005)

- **Entidad común:** vive en Core cuando al menos dos módulos funcionales necesitan referenciarla sin que ninguno sea su dueño natural. Core no duplica el dato del módulo dueño; ofrece un identificador estable y una descripción mínima (tipo, título breve).
- **Relación explícita:** vínculo dirigido entre dos entidades referenciables, con un tipo declarado libremente por quien la crea (`relacionado-con`, `depende-de`, `documenta-a`...), sin catálogo cerrado en el MVP. Core garantiza integridad referencial, limpieza al eliminar una entidad, y consulta inversa aunque la relación se declare en un solo sentido.
- **Evento interno:** mensaje que un módulo emite cuando algo relevante ocurre en una de sus entidades, con tipo, referencia a la entidad y marca de tiempo. Los módulos se suscriben a los tipos que les interesan sin que el emisor conozca a sus consumidores. Todo evento debe poder procesarse más de una vez sin duplicar su efecto; el orden entre reglas que reaccionan al mismo evento no está garantizado en el MVP.
- **Registro de auditoría:** todo evento interno queda registrado con tipo, entidad afectada, actor que lo originó y marca de tiempo, desde el MVP.
- `Área/Categoría` y `Actor/Identidad` siguen como conceptos transversales; `Actor/Identidad` pertenece por dueño natural a Identidad y Seguridad, no a Core, aunque todos los módulos lo referencien.

## Dependencias

El Core debe depender de abstracciones del dominio, no de la web, Asana, Siri, un agente de IA ni un proveedor de almacenamiento. Los módulos funcionales usarán sus contratos transversales sin introducir dependencias circulares.

## Seguridad y automatizaciones

Core debe ofrecer puntos para autorización, auditoría y emisión de eventos internos, pero no decidir todavía la tecnología ni ejecutar automatizaciones por sí mismo. Las automatizaciones consumirán eventos autorizados y deberán conservar trazabilidad.

## MVP y futuro

**MVP propuesto:** relaciones básicas entre información, tareas y fechas; operaciones reutilizables; principios de autorización/auditoría y eventos internos mínimos.  
**Futuro:** reglas de relación más ricas, políticas de permisos multiusuario, contratos para agentes y canales externos.

## Decisiones pendientes

Resuelto por ADR-005: qué convierte a un concepto en entidad común, tipos y semántica de relaciones, modelo de eventos internos, separación Core/módulos, y alcance mínimo de auditoría. Quedan abiertas:

- Autorización concreta (quién puede hacer qué) — bloque 1 de `docs/01-proyecto/decisiones-transversales-pendientes.md`, todavía pendiente.
- Tecnología concreta de entrega de eventos (cola, tabla con estado, u otra).
- Si en algún momento conviene cerrar un catálogo de tipos de relación o de evento, y cuándo.