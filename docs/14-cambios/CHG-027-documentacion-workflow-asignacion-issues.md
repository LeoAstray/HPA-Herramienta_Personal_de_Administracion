# CHG-027 — Documentación del workflow de asignación de issues

## Estado y autorización

Registrado el 2026-10-13 por petición expresa del colaborador de documentar el workflow que había añadido. El cambio describe una automatización existente de organización del desarrollo; no configura ni ejecuta nuevas operaciones externas.

Estado de entrada: rama `dev`, HEAD `627896830b707704a8991fabc7cb626f924d0804`, con los cambios documentales de CHG-026 todavía locales. Se preservan esos cambios. El historial local recoge la incorporación del workflow en `980c7aa` y el ajuste de su método de asignación en `6278968`.

## Configuración observada y cambio documental

Se inspecciona [auto-assign.yml](../../.github/workflows/auto-assign.yml). Declara el evento `issues` de tipo `opened`, un runner `ubuntu-latest`, permiso `issues: write` y una llamada con GitHub CLI para añadir al autor del issue a sus responsables. Usa el token automático del workflow mediante `GH_TOKEN`; el archivo no contiene una credencial personal ni hace checkout.

Se añade al [proceso de cambio](../00-gobierno/proceso-de-cambio.md#automatización-de-asignación-de-issues) el propósito, disparador, permisos, dependencias, comprobación y límites de la automatización. Se actualiza el [roadmap](../01-proyecto/roadmap.md#seguimiento-del-workflow-de-asignación-de-issues), que concentra el avance, los pendientes y el siguiente paso. Su regla de mantenimiento distingue la asignación automática del resto de operaciones manuales.

La documentación se apoya en las fuentes oficiales del [evento `issues`](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#issues), la [API de asignación](https://docs.github.com/en/rest/issues/assignees#add-assignees-to-an-issue) y [GitHub CLI](https://cli.github.com/manual/gh_api), consultadas el 2026-10-13. Describir la configuración no acredita una ejecución satisfactoria.

## Impacto y límites

No cambian el workflow, AGENTS.md, ADR-004, el modelo de permisos del producto ni su arquitectura. La automatización opera sobre la asignación de responsables del repositorio; no es una dependencia de HPA ni concede a los agentes permisos de publicación. No se requiere una ADR del producto.

No se accede al remoto, a una sesión autenticada, a registros de Actions ni a Asana. No se crean issues de prueba, se instalan herramientas ni se realizan operaciones Git de escritura. CHG-026 y los registros anteriores conservan su contenido.

## Verificación

Comprobaciones locales sobre los tres documentos afectados: `git --no-optional-locks diff --check` sin incidencias en rastreados; sin espacios finales y con salto final en los tres archivos, incluido CHG-027 sin rastrear. Tras corregir las referencias a encabezados con tildes, se resuelven 25 enlaces locales, nueve de ellos con ancla, sin fallos. No son una ejecución ni una validación funcional del workflow.

## Seguimiento y recuperación

El estado y la continuación se consultan en el [roadmap](../01-proyecto/roadmap.md#seguimiento-del-workflow-de-asignación-de-issues).

La recuperación, si se solicita, consiste en retirar esta sección del proceso de cambio, los cambios de seguimiento/mantenimiento de este paso y CHG-027, preservando CHG-026 y los cambios ajenos. El workflow existente se conserva.
