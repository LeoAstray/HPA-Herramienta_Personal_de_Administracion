# Proceso de cambio y publicación documental

## Cambios relevantes

Antes de implementar un cambio relevante se debe documentar problema, objetivo, alcance, alternativas, impacto en arquitectura/datos/API/interfaz, seguridad, dependencias, pruebas, despliegue y rollback. El flujo es:

`Análisis -> Diseño -> Documentación -> Asana -> Implementación -> Pruebas -> Documentación actualizada`

## Fuente de verdad y formatos

1. Markdown, organizado por área y módulo, es la versión editable y consultable por agentes.
2. DOCX y PDF son ediciones consolidadas de lectura. Se publican al aprobar una línea base, una decisión de amplio impacto o un cambio documental relevante.
3. Cada publicación se guarda en `docs/documentacion/publicaciones/<YYYY-MM-DD_HH-mm-ss>-<nombre>/`. La carpeta contiene el DOCX y el PDF con el mismo nombre, más los generadores o metadatos necesarios para reproducirlos.
4. No se requiere generar una copia DOCX/PDF por cada archivo Markdown aislado; el paquete publicado debe indicar qué versión de Markdown consolida.

## Registro mínimo

Cada cambio debe actualizar el [roadmap](../01-proyecto/roadmap.md), indicando el avance realizado, los pendientes y el siguiente paso. Si no cambia el orden de los hitos, registrar igualmente el avance. El trabajo no se considera documentalmente cerrado sin esta actualización. Regla explicitada por el colaborador el 2026-10-07.

Todo cambio relevante se registra en `14-cambios/` y enlaza a requisitos, ADR, pruebas y tareas de Asana cuando existan. Nunca se guardan secretos reales.
