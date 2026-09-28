# Contexto para agentes de IA

## Misión

Ayudar a analizar, diseñar, documentar, implementar y mantener la Herramienta Personal de Administración respetando esta documentación como fuente de verdad.

Los agentes de desarrollo asisten al equipo de dos colaboradores; no son funcionalidades del producto HPA. Los futuros agentes internos del producto son un ámbito distinto y solo podrán acceder al producto mediante sus fronteras de seguridad aprobadas.

## Estado y límites

El estudio global de módulos está completo. El descubrimiento y diseño de IA/Agentes es la prioridad inmediata (ADR-003), pero no hay arquitectura técnica ni código de producción aprobados. Un agente debe identificar si trabaja sobre un estado actual, objetivo, propuesta, decisión, pendiente o elemento descartado; si falta una decisión que cambie materialmente el diseño, debe solicitarla.

## Reglas invariantes

- No implementar cambios relevantes sin análisis y documentación previos.
- No usar ni registrar secretos reales.
- No convertir Asana en dependencia de producto.
- No implementar móvil, Siri/voz, IA funcional ni integraciones complejas por preparación futura.
- Durante el descubrimiento de IA/Agentes, no seleccionar proveedor, modelo u orquestador ni conectar datos reales sin una decisión documentada y autorización explícita.
- Mantener el Core independiente de una interfaz concreta.
- Aplicar mínimo privilegio y registrar las acciones de cambio relevantes.
- Distinguir siempre si una tarea corresponde a un agente de desarrollo o a un futuro agente del producto; sus datos, permisos y contratos no se comparten por defecto.
- Los agentes de desarrollo no sustituyen la responsabilidad de los dos colaboradores sobre decisiones, revisión, aprobación de cambios ni publicación.

## Lectura mínima por tarea

`docs/README.md` -> estado -> visión y alcance -> ADRs -> módulo afectado -> documentación de seguridad/arquitectura aplicable.
