# CHG-003 — Normalización de numeración y definición de Documentos y Archivos

## Estado

Documentado y aplicado a la documentación operativa. No afecta a código de producto: el repositorio no contiene implementación de producto, arquitectura técnica aprobada ni esquema de datos.

## Objetivo y alcance

Se normaliza la numeración de los módulos para que corresponda a los prefijos de archivo: Core se trata como módulo 0 y base transversal; `01` a `04` corresponden a los módulos funcionales 1 a 4; `05` corresponde a Documentos y Archivos.

También se inicia la definición funcional del módulo 5, Documentos y Archivos. Se delimita su relación con una ruta física configurable, registros lógicos, metadatos, referencias cruzadas, privacidad, operaciones físicas y pendientes de diseño.

## Impacto

- **Catálogo y contexto:** se actualizan `docs/12-modulos/README.md` y `docs/general-docs/contexto/Explicacion Inicial Modules Leo.txt`.
- **Documentos de módulo:** los títulos de `00-core.md` a `04-informacion-personal.md` reflejan su número; se añade `05-documentos-y-archivos.md`.
- **Seguridad:** `docs/07-seguridad/README.md` incorpora límites de acceso a rutas y manejo de contenido no confiable.
- **Roadmap:** se indica que los módulos 0 a 5 están documentados en análisis.
- **Arquitectura, datos, API, interfaz, requisitos, pruebas y operaciones:** no se toma ninguna decisión ni se crea un artefacto técnico; siguen pendientes tras la Fase 1.
- **ADR y Asana:** no procede ADR ni actualización de Asana. No se ha tomado una decisión técnica o de amplio impacto y no se proporcionó una referencia de Asana.

## Seguridad y privacidad

La definición del módulo propone mínimo privilegio sobre rutas autorizadas, separación entre registro lógico y archivo físico, ausencia de operaciones físicas implícitas y no ejecución de contenido no confiable. No se incluyen secretos ni datos personales reales.

## Verificación y rollback

Se debe comprobar que la secuencia `00`–`05`, el catálogo y los enlaces internos coincidan. Las fuentes históricas bajo `docs/general-docs/fuentes/` conservan su redacción original y no se alteran. El rollback consiste en revertir los archivos de documentación cambiados; no altera datos, servicios ni infraestructura.

## Documentación relacionada

- `docs/12-modulos/README.md`
- `docs/12-modulos/00-core.md` a `docs/12-modulos/05-documentos-y-archivos.md`
- `docs/07-seguridad/README.md`
- `docs/01-proyecto/roadmap.md`
