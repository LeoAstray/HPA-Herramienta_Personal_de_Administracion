# CHG-013 — Ejecuciones de R2 de DEV-00

## Estado y alcance

Registrado el 2026-09-30 tras autorización expresa del colaborador para ejecutar las dos pruebas. Se lanzaron únicamente dos subagentes DEV-00 con GPT-6 Luna / Low seleccionado explícitamente y sin historial conversacional, sobre R2 en el commit `6fba59906ce597bd2c3fa28d1f33878f7fb12fc7`.

## Resultados y límites

El caso claro recomendó la petición original sin reescritura ni restricciones adicionales. El ambiguo conservó la posibilidad de edición del destinatario y marcó pendiente de aclarar el ámbito. Ambos superan los criterios de comportamiento ensayados; no se cambia modelo, esfuerzo ni permisos de ADR-004.

El entorno es de subagentes, no chats manuales idénticos; los documentos de evaluación eran accesibles y la prueba no es ciega. No hay medición atribuible de consumo o duración individual ni trazas completas de herramientas en el registro. El repositorio permaneció limpio durante las pruebas antes de esta documentación. Esto no demuestra aislamiento técnico ni ausencia de toda escritura externa.

## Verificación y pendientes

Se comprobó la existencia del documento de módulo citado por la respuesta ambigua. Comprobar formato del diff y enlaces del registro. Continúa pendiente EVAL-01 por petición humana, junto con controles efectivos y utilidad de DEV-00 frente a una plantilla. No se ejecuta Reviewer ni se configura una integración, skill o agente compartido.

Solo el agente principal registra estos resultados en Markdown; los subagentes no tenían encargo de edición. No se crean tareas de Asana ni se realizan commits o publicaciones. La recuperación documental queda a cargo de un colaborador mediante Git.

## Documentación relacionada

- [Evaluación, método y resultados de R2](../10-ia/evaluacion-agentes-desarrollo.md)
- [Estado del proyecto](../00-gobierno/estado-proyecto.md)
- [Prompt R2, sin cambios](../10-ia/prompts/dev-00-preparar-peticion.md)
