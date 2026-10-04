# CHG-017 — Modelos del Developer y estado de EVAL-02

## Decisión

El 2026-09-30 el colaborador aprueba provisionalmente GPT-6.1 Sol (`gpt-6.1-sol`) / Medium (`medium`) como configuración habitual de Developer DEV-02. Para tareas sencillas y acotadas se autoriza seleccionar GPT-6 Luna (`gpt-6-luna`) / Medium (`medium`) antes de ejecutar el encargo.

Sol es la opción habitual para funcionalidades, lógica de negocio, refactorizaciones y cambios con dependencias entre archivos. Luna puede usarse para enlaces, cambios mecánicos y correcciones pequeñas con criterios claros y bajo riesgo. La selección se hará por tarea y se registrará; no concede permiso para cambiar de modelo durante una ejecución, alterar esfuerzos o sustituir modelos no disponibles sin autorización humana.

Es una decisión operativa provisional, no una conclusión comparativa de consumo o calidad del código. EVAL-02 prueba solo una corrección documental con Luna, no desarrollo de funcionalidades ni Sol como Developer. La configuración ejecutable y los controles efectivos siguen pendientes.

## Estado de EVAL-02

El colaborador aporta la respuesta de Developer con GPT-6 Luna / Medium y tiempo mostrado de 1 min 8 s. La comprobación local del agente principal confirma los dos destinos corregidos, la existencia de los archivos históricos y el ámbito índice + CHG-016. Los cambios se conservan sin modificarlos; la validación independiente EVAL-03 continúa pendiente.

## Documentación y verificación

Se actualizan ADR-004, contrato de desarrollo, matriz de modelos, evaluación, estado del proyecto, roadmap y estado del encargo EVAL-02. Se conserva el bloque enviado al Developer con Luna / Medium para no atribuirle otra configuración.

Se revisan referencias y diff y se ejecuta `git diff --check`. No se modifican el índice ADR ni CHG-016, no se ejecuta al Tester y no se realizan operaciones de escritura Git, GitHub o Asana.

- [ADR-004](../13-adrs/ADR-004-contratos-agentes-desarrollo.md)
- [Contrato](../10-ia/agentes-desarrollo.md)
- [Matriz](../10-ia/matriz-modelos-agentes-desarrollo.md)
- [Evaluación](../10-ia/evaluacion-agentes-desarrollo.md)
- [Encargo EVAL-02](../10-ia/prompts/eval-02-developer-enlaces-adr.md)
