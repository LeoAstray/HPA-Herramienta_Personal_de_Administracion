# CHG-006 — Inicio del descubrimiento de IA y Agentes

## Estado

Documentado y aplicado a la documentación operativa. No se selecciona ni conecta ningún modelo, proveedor o agente.

## Objetivo y alcance

Iniciar el siguiente paso definido por ADR-003: transformar la prioridad de IA/Agentes en una cartera de casos de uso evaluable, con una propuesta inicial de agente de bajo riesgo y preguntas que deben resolverse antes de comparar modelos.

## Impacto

- **IA/Agentes:** se añade el documento de descubrimiento y una cartera inicial de seis agentes candidatos.
- **Priorización:** AG-01, Consulta personal, queda como propuesta inicial para investigación por su enfoque de solo lectura.
- **Seguridad:** se establecen límites comunes de mínimo privilegio, confirmación humana, trazabilidad y revocación.
- **Arquitectura y código:** no se crean componentes, contratos técnicos ni integraciones.
- **Asana:** no se actualiza porque no se ha proporcionado una referencia de tarea o autorización para operar allí.

## Verificación y rollback

Se comprueba que el README de IA y el módulo 14 enlazan al documento de descubrimiento y que sus propuestas se distinguen de decisiones. El rollback consiste en revertir estos documentos; no afecta a datos, servicios ni infraestructura.

## Documentación relacionada

- `docs/10-ia/descubrimiento-ia-agentes.md`
- `docs/10-ia/README.md`
- `docs/12-modulos/14-ia-agentes.md`
- `docs/13-adrs/ADR-003-priorizacion-descubrimiento-ia-agentes.md`
