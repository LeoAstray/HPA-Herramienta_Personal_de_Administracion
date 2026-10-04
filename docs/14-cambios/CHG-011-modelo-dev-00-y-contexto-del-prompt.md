# CHG-011 — Modelo provisional de DEV-00 y contexto del prompt

## Estado y alcance

Aplicado a documentación operativa el 2026-09-30 por petición del colaborador. No se implementan agentes ejecutables, skills ni producto, y no se alteran permisos del equipo.

## Análisis y decisión

El prompt anterior definía salidas y límites, pero no indicaba lectura rectora, contrato por rol ni el estado de una propuesta con preguntas pendientes. Dos respuestas de EVAL-00 aportadas por el colaborador fueron satisfactorias para el caso claro y satisfactorias con observación menor para el ambiguo.

Se aprueba mantener provisionalmente GPT-6 Luna (`gpt-6-luna`) / Low (`low`) para DEV-00. Se registra en ADR-004, contrato de desarrollo, matriz y prompt. El consumo y las operaciones realizadas no son verificables con las respuestas; no se declara ahorro demostrado ni piloto completo.

## Cambios y límites

El prompt incorpora contexto del proyecto, lectura obligatoria y selectiva, rol destinatario, tratamiento de supuestos, estados listo para aprobación/pendiente de aclaración y límites de solo lectura. El modelo se selecciona antes de invocar el rol: el Markdown no cambia el chat. No se permite escalado automático.

No se configura Asana ni se modifica ninguna tarea externa; su referencia queda pendiente si el equipo la incorpora manualmente. No hay cambios de arquitectura, datos, API, despliegue o permisos del producto.

## Verificación y recuperación

Comprobaciones documentales: formato del diff, destinos de enlaces locales y coherencia de configuración entre los documentos afectados. La regresión del prompt revisado está pendiente; los dos casos aportados corresponden a la versión anterior. No se usan secretos, servicios de pago ni operaciones de escritura Git/GitHub. Un colaborador puede recuperar la versión anterior mediante Git.

## Documentación relacionada

- [Prompt DEV-00](../10-ia/prompts/dev-00-preparar-peticion.md)
- [Contrato de desarrollo](../10-ia/agentes-desarrollo.md)
- [Matriz de modelos](../10-ia/matriz-modelos-agentes-desarrollo.md)
- [Evaluación y evidencias](../10-ia/evaluacion-agentes-desarrollo.md)
- [ADR-004](../13-adrs/ADR-004-contratos-agentes-desarrollo.md)
- [Estado del proyecto](../00-gobierno/estado-proyecto.md)
