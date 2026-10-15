# CHG-028 — Preparación documental del encargo EVAL-05 Developer

## Estado, autorización y alcance

Preparado el 2026-10-14 por la petición del colaborador de atender primero el issue de continuación documental de EVAL-05, cuyo alcance y criterios aporta en esta conversación. Trabajo local sobre `dev`, base `4824dd107c9a0fa751491a9bc0435872dac636ec`, con árbol limpio al iniciar esta entrega.

Se prepara una versión concreta para revisión humana, los requisitos de G2–G6 y el futuro encargo del primer perfil Developer. La petición no comunica una revisión humana ya realizada; esa aceptación no se registra por inferencia.

## Análisis y cambios

- [Ficha EVAL-05-ENTORNO-R1](../10-ia/entorno-eval-05.md): identifica la versión de revisión, reconoce como histórico el inventario del 2026-10-07 y concreta los datos exigidos por G2–G6 sin inventar valores efectivos.
- [Guía R1](../10-ia/revision-eval-05-colaborador.md): delimita la revisión documental, sustituye la referencia antigua de trabajo por la base de esta entrega y define cómo registrar versiones, alcance, observaciones y límites.
- [Encargo EVAL-05-DEV02-R1](../10-ia/encargo-eval-05-developer.md): adapta la plantilla al primer Developer, identifica los campos por completar, los casos candidatos y los límites; no es un encargo ejecutable.
- README de IA y [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05): enlaces, avance, pendientes y siguiente paso. El detalle operativo permanece solo en el roadmap.

CHG-021/022/024 y el diseño inicial conservan su contenido. No cambia la matriz de permisos de ADR-004 ni la arquitectura del producto; no requiere una ADR nueva.

## Límites de la entrega

No se configura laboratorio, perfil, permisos o herramientas. No se selecciona modelo ni se ejecutan sondas o agentes. No hay controles efectivos verificados. No se accede a GitHub, Asana, credenciales, datos personales ni servicios externos. Git y publicación permanecen a cargo del colaborador. La revisión humana es una condición de cierre del issue documental; configurar y ejecutar el laboratorio es una tarea posterior.

## Verificación e identificación de versión

Comprobaciones locales sobre los seis Markdown del cambio, incluidos los dos nuevos sin rastrear:

- `git --no-optional-locks diff --check`: sin incidencias en los archivos rastreados.
- Lectura y validación PowerShell de salto final, espacios finales y marcadores de conflicto: sin incidencias.
- Resolución PowerShell de 56 enlaces locales y 13 anclas: todos resueltos; no se consultan enlaces web.
- Comparación de archivos con `git --no-optional-locks diff --name-only` y `git --no-optional-locks ls-files --others --exclude-standard`: cuatro archivos modificados y dos nuevos, únicamente de esta entrega EVAL-05.
- Revisión de contenido: ficha identificada como R1, inventario histórico, datos G2–G6 sin valores inventados, encargo no ejecutable y conformidad humana todavía sin registrar. La revisión del encargo no se añade como condición al criterio de revisión humana de la ficha.

`Get-FileHash -Algorithm SHA256` identifica los textos preparados para la revisión:

| Documento | SHA-256 |
| --- | --- |
| `docs/10-ia/entorno-eval-05.md` — EVAL-05-ENTORNO-R1 | `D5A1485EEFD32A684335C154C17C3F8534A07DF939A852BA0BD0D854C162978D` |
| `docs/10-ia/revision-eval-05-colaborador.md` — Guía R1 | `A8C12CDA396BFC30EB8E839A5F401D35946313E33368A123991F5A335E86F1F4` |
| `docs/10-ia/encargo-eval-05-developer.md` — EVAL-05-DEV02-R1 | `D5DF78683F10FB87429E22E0E1E19FE249B31F88B6A4245EEE45FE536CF8963C` |

Los hashes identifican el contenido; no demuestran que una persona lo haya revisado ni acreditan controles del laboratorio. Las comprobaciones son documentales y no ejecutan P01–P13.

## Seguimiento y recuperación

La revisión recibida, el avance, los pendientes y el siguiente paso se mantienen en el [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05). Cuando el colaborador comunique su revisión se registrará su fuente, versión, alcance, observaciones y límites, conservando este estado de preparación como histórico.

La recuperación, si se solicita, consiste en retirar el encargo nuevo y este registro y revertir únicamente los cambios de ficha, guía, README de IA y roadmap de esta entrega, preservando cambios ajenos. No se ejecuta recuperación del laboratorio.
