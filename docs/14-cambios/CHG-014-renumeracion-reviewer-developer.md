# CHG-014 — Renumeración de Reviewer y Developer

## Decisión y motivo

El 2026-09-30 el colaborador solicita alinear los identificadores de los roles aún no probados con el orden del piloto documental. Solo DEV-00 tiene ejecuciones registradas.

- Reviewer: antes DEV-02, ahora **DEV-01**.
- Developer: antes DEV-01, ahora **DEV-02**.
- Preparador DEV-00, Tester DEV-03, Documentación DEV-04 y Coordinación DEV-05 conservan sus identificadores.

Los identificadores EVAL no cambian: EVAL-01 prueba al Reviewer y EVAL-02 al Developer. El flujo habitual de un cambio sigue siendo Developer → Reviewer → Tester; los números de rol siguen el orden del piloto, no una secuencia obligatoria de trabajo.

## Alcance y trazabilidad

Se actualizan el contrato de desarrollo, inventario de agentes, matriz de modelos, escenarios de evaluación, estado del proyecto y ADR-004. Los permisos y candidatos de modelo y esfuerzo se conservan por rol: Reviewer mantiene GPT-6.1 Sol / Medium y Developer GPT-6 Luna / Medium para cambios acotados. DEV-00 mantiene su selección provisional Luna / Low y sus evidencias.

El encargo de EVAL-01 preparado en la conversación deberá usar Reviewer (DEV-01). La prueba no se ejecuta ni se guarda un nuevo prompt. Las publicaciones y registros históricos previos no se reescriben; cualquier identificador antiguo se interpreta según la equivalencia anterior.

No se modifica producto ni configuración ejecutable, no se crean tareas de Asana y no se realizan operaciones de escritura Git ni modificaciones en GitHub.

## Verificación

Revisión del diff, comprobación de espacios con `git diff --check` y búsqueda global de DEV-01/DEV-02 para comprobar que las referencias operativas y flujos conservan el rol correcto. No se ejecutan pruebas de agentes.

## Documentos relacionados

- [Contrato de desarrollo](../10-ia/agentes-desarrollo.md)
- [Inventario](../10-ia/descubrimiento-ia-agentes.md)
- [Matriz](../10-ia/matriz-modelos-agentes-desarrollo.md)
- [Evaluación](../10-ia/evaluacion-agentes-desarrollo.md)
- [Estado](../00-gobierno/estado-proyecto.md)
- [ADR-004](../13-adrs/ADR-004-contratos-agentes-desarrollo.md)
