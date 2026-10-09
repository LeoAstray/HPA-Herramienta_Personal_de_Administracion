# CHG-023 — Corrección de la carpeta anidada de arquitectura

## Estado y alcance

Aplicado el 2026-10-07 por petición del colaborador. Se mueve `docs/03-arquitectura/03-arquitectura/propuesta-modelo-core.md` a `docs/03-arquitectura/propuesta-modelo-core.md` y se elimina únicamente la carpeta interior ya vacía, incluidos los controles de ausencia de archivos ocultos. Se preservan los cambios locales de CHG-021/022.

## Análisis y documentación

La carpeta interior solo contenía la propuesta de Core. ADR-005 y CHG-020 ya referenciaban la ruta correcta de destino, por lo que no requieren modificaciones. Se añade el enlace en el [README de arquitectura](../03-arquitectura/README.md) y se actualiza el [roadmap](../01-proyecto/roadmap.md), conservando pendientes y siguiente paso.

No se modifica el contenido de la [propuesta](../03-arquitectura/propuesta-modelo-core.md), las decisiones de Core ni la arquitectura técnica. No requiere ADR nueva, publicación consolidada DOCX/PDF, código de producto, acceso al remoto ni operaciones Git de escritura.

## Verificación

Movimiento local con `Move-Item` y eliminación no recursiva con `Remove-Item`, tras resolver y verificar las rutas absolutas dentro de arquitectura. SHA-256 antes/después idéntico: `35295CAC09A3C59939C509628B2DE53F5E89A2BF20D259FDF9A1E30491D17E23`; carpeta interior ausente. `git --no-optional-locks diff --check` sin incidencias en rastreados. Resolución local de los doce enlaces relativos del README de arquitectura, roadmap y este registro: todos los destinos existen. `rg --files docs/03-arquitectura` confirma únicamente README y propuesta al nivel correcto. No se consultan enlaces web.

## Siguiente paso y recuperación

El colaborador revisa la ficha EVAL-05; después se preparan los recursos y perfiles del laboratorio conforme al roadmap. Recuperación documental, si se solicita: devolver el archivo a su ubicación anterior y retirar únicamente los ajustes de este cambio, preservando cambios ajenos. No se ejecuta recuperación.
