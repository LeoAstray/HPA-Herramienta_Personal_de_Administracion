# CHG-010 — Preparador de peticiones y matriz inicial de modelos

## Estado y alcance

Aplicado a documentación operativa el 2026-09-30. Se incorpora DEV-00 como preparador opcional de peticiones y se documentan candidatos de modelo por rol para las cuentas Plus.

## Decisiones y propuestas

DEV-00 conserva la petición original, propone una versión verificable y no ejecuta la tarea ni amplía permisos. Su uso es selectivo para evitar consumo adicional en peticiones claras. La asignación de modelos sigue siendo una propuesta que debe validarse con el piloto; no se convierte en decisión técnica.

Se añade un prompt manual experimental para EVAL-00. Se evaluará antes de convertirlo en una skill o configuración reutilizable.

La investigación usa documentación oficial de OpenAI vigente en la fecha indicada. Se propone empezar con Luna en trabajo acotado y Sol en revisión o trabajo complejo, con GPT-6.1 Sol sujeto a disponibilidad en cada cuenta y cliente.

## Seguridad, verificación y recuperación

No se conectan servicios, no se usa API de pago y no se modifica GitHub. Se comprobarán enlaces, formato y coherencia con ADR-004. Para recuperar el estado anterior, un colaborador revertirá los cambios documentales mediante Git.

## Documentación relacionada

- [Contratos de desarrollo](../10-ia/agentes-desarrollo.md)
- [Matriz de modelos](../10-ia/matriz-modelos-agentes-desarrollo.md)
- [Escenarios de evaluación](../10-ia/evaluacion-agentes-desarrollo.md)
- [Prompt experimental DEV-00](../10-ia/prompts/dev-00-preparar-peticion.md)
- [ADR-004](../13-adrs/ADR-004-contratos-agentes-desarrollo.md)
