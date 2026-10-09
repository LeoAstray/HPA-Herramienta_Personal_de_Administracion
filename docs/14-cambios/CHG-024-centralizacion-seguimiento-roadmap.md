# CHG-024 — Centralización del seguimiento en el roadmap

## Estado y alcance

Aplicado el 2026-10-09 a propuesta del colaborador. El detalle del avance de EVAL-05 estaba repetido en varios documentos y podía desincronizarse al actualizar el roadmap.

## Cambio documental

Se reúne el avance, los pendientes, el estado de las puertas G1–G6 y el siguiente paso en el [seguimiento de EVAL-05 del roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05). Los documentos de entrada, estado, contrato, diseño, evaluación, ficha del entorno y guía de revisión enlazan a esa sección en lugar de copiar el seguimiento.

La ficha conserva la evidencia exigida por cada puerta y su inventario histórico de la sesión del 2026-10-07. Los requisitos, propuestas, procedimientos y evidencias de evaluación se conservan en sus documentos especializados. Los registros CHG anteriores mantienen el estado histórico que documentan.

Se añade la regla de centralización a [AGENTS.md](../../AGENTS.md), al [proceso de cambio](../00-gobierno/proceso-de-cambio.md) y al mantenimiento del roadmap. No cambia la aceptación, los contratos de agentes ni el alcance del producto; no requiere una nueva ADR ni una publicación DOCX/PDF.

## Verificación

Comprobaciones locales sobre los doce archivos del cambio: `git --no-optional-locks diff --check` sin incidencias; CHG-024 sin espacios finales; 79 enlaces relativos y 15 anclas resueltos. La búsqueda de las fórmulas de avance duplicadas solo conserva la conformidad en el roadmap y en el registro histórico CHG-022. Los registros CHG anteriores no tienen modificaciones. No se consultan enlaces web ni se ejecuta EVAL-05.

## Pendientes, siguiente paso y recuperación

Los pendientes operativos y el siguiente paso se consultan en el [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05). El colaborador revisa este cambio documental antes de integrarlo. GitHub y Asana se gestionan manualmente.

La recuperación, si se solicita, consiste en revertir únicamente las modificaciones de CHG-024 y retirar este registro, preservando cambios ajenos.
