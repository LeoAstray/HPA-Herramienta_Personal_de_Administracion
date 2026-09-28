# CHG-009 — Prioridades y comprobaciones locales de agentes

## Estado y alcance

Aplicado a Markdown a partir de la confirmación del propietario: ambos colaboradores tienen Plus; las prioridades son consumo, calidad, autonomía y velocidad. Se habilitan comprobaciones locales breves para el Developer y se explicita GitHub como fuente de solo lectura para todos los agentes.

## Impacto

Se actualizan ADR-004, contratos de desarrollo, contrato general y evaluación. El Developer puede corregir errores de sus comprobaciones dentro de la tarea; Reviewer y Tester siguen informando y sus correcciones se solicitan por una persona. El Tester mantiene la validación independiente. Git y publicación siguen a cargo de los colaboradores.

## Verificación y recuperación

Comprobar formato y coherencia de permisos y prioridades en los documentos activos. Los controles efectivos de las herramientas siguen pendientes de configurar y verificar en el piloto. No se modifica GitHub ni se configura un proveedor. La recuperación consiste en revertir los cambios documentales mediante una operación elegida por un colaborador.

## Referencias

- [Contratos](../10-ia/agentes-desarrollo.md)
- [Evaluación](../10-ia/evaluacion-agentes-desarrollo.md)
- [ADR-004](../13-adrs/ADR-004-contratos-agentes-desarrollo.md)
