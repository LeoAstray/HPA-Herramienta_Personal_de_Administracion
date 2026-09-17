# Módulo Core — estudio inicial

## Estado

**Fase 1 iniciada.** Este documento formula una propuesta conceptual; no define una arquitectura técnica ni un modelo de datos definitivo.

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

## Entidades y relaciones — propuesta inicial

Se estudiarán como conceptos, no como tablas aún: `Entidad del dominio`, `Relación`, `Área/Categoría`, `Actor/Identidad`, `Evento interno` y `Registro de auditoría`. Un elemento de un módulo podrá relacionarse con otro mediante una relación explícita y con significado definido; por ejemplo, una tarea asociada a un documento o a un evento.

## Dependencias

El Core debe depender de abstracciones del dominio, no de la web, Asana, Siri, un agente de IA ni un proveedor de almacenamiento. Los módulos funcionales usarán sus contratos transversales sin introducir dependencias circulares.

## Seguridad y automatizaciones

Core debe ofrecer puntos para autorización, auditoría y emisión de eventos internos, pero no decidir todavía la tecnología ni ejecutar automatizaciones por sí mismo. Las automatizaciones consumirán eventos autorizados y deberán conservar trazabilidad.

## MVP y futuro

**MVP propuesto:** relaciones básicas entre información, tareas y fechas; operaciones reutilizables; principios de autorización/auditoría y eventos internos mínimos.  
**Futuro:** reglas de relación más ricas, políticas de permisos multiusuario, contratos para agentes y canales externos.

## Decisiones pendientes

- Qué convierte exactamente a un concepto en entidad común.
- Tipos y semántica de relaciones.
- Modelo de eventos internos, entrega, reintentos e idempotencia.
- Separación concreta entre Core, servicios de aplicación y módulos.
- Alcance mínimo de auditoría y autorización en el MVP.
