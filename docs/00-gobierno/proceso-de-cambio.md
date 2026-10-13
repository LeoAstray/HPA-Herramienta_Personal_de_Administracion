# Proceso de cambio y publicación documental

## Cambios relevantes

Antes de implementar un cambio relevante se debe documentar problema, objetivo, alcance, alternativas, impacto en arquitectura/datos/API/interfaz, seguridad, dependencias, pruebas, despliegue y rollback. El flujo es:

`Análisis -> Diseño -> Documentación -> Asana -> Implementación -> Pruebas -> Documentación actualizada`

## Automatización de asignación de issues

El workflow [Auto-assign issue creator](../../.github/workflows/auto-assign.yml) organiza el desarrollo: al abrirse un issue (`issues`, tipo `opened`), solicita añadir a su autor como responsable. No actúa al editar o reabrir un issue ni procesa retrospectivamente los existentes. La operación añade responsables sin retirar los que ya existan, según el [contrato de la API de GitHub](https://docs.github.com/en/rest/issues/assignees#add-assignees-to-an-issue).

La configuración usa un runner `ubuntu-latest` y GitHub CLI para llamar a la API de asignación. Declara únicamente `issues: write`; el token automático de GitHub Actions se entrega mediante `GH_TOKEN`, sin credenciales personales guardadas en el archivo. No realiza checkout ni operaciones Git sobre archivos del proyecto.

Para que el evento dispare el workflow, el archivo debe existir en la rama por defecto del repositorio y GitHub Actions debe estar habilitado. Véase la [documentación del evento `issues`](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#issues). La asignación depende de los permisos efectivos y de que GitHub permita asignar al autor. Su comprobación requiere revisar la ejecución en Actions y el responsable resultante del issue.

La automatización se limita a esa asignación. Los colaboradores crean, revisan y cierran issues, gestionan Asana y realizan ramas, staging, commits, push, pull requests y merges manualmente. Los agentes conservan los límites de ADR-004; esta automatización no les concede escritura externa. Es una herramienta de organización del repositorio y no una dependencia del producto.

La configuración observada, las evidencias disponibles y la continuación se mantienen en el [seguimiento del workflow del roadmap](../01-proyecto/roadmap.md#seguimiento-del-workflow-de-asignación-de-issues).

## Fuente de verdad y formatos

1. Markdown, organizado por área y módulo, es la versión editable y consultable por agentes.
2. DOCX y PDF son ediciones consolidadas de lectura. Se publican al aprobar una línea base, una decisión de amplio impacto o un cambio documental relevante.
3. Cada publicación se guarda en `docs/documentacion/publicaciones/<YYYY-MM-DD_HH-mm-ss>-<nombre>/`. La carpeta contiene el DOCX y el PDF con el mismo nombre, más los generadores o metadatos necesarios para reproducirlos.
4. No se requiere generar una copia DOCX/PDF por cada archivo Markdown aislado; el paquete publicado debe indicar qué versión de Markdown consolida.

## Registro mínimo

Cada cambio debe actualizar el [roadmap](../01-proyecto/roadmap.md), indicando el avance realizado, los pendientes y el siguiente paso. Si no cambia el orden de los hitos, registrar igualmente el avance. El trabajo no se considera documentalmente cerrado sin esta actualización. Regla explicitada por el colaborador el 2026-10-07.

Todo cambio relevante se registra en `14-cambios/` y enlaza a requisitos, ADR, pruebas y tareas de Asana cuando existan. Nunca se guardan secretos reales.

El detalle del avance operativo, los pendientes y el siguiente paso se mantiene solo en el roadmap. Los demás documentos enlazan a su sección correspondiente, sin copiar los párrafos de seguimiento. Los documentos especializados conservan requisitos, propuestas, procedimientos y evidencias; los registros históricos conservan el estado del momento documentado.
