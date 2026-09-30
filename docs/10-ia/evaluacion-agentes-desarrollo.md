# Evaluación de agentes de desarrollo

## Estado y objetivo

**Piloto iniciado: cuatro respuestas manuales de DEV-00, dos ejecuciones de R2 mediante subagentes y respuestas de EVAL-01 y EVAL-02 aportadas. R2 supera los dos casos probados; EVAL-01 supera los criterios documentales de su caso. EVAL-02 satisfactorio en comprobación local del cambio, pendiente de EVAL-03; controles efectivos pendientes.** Comparar configuraciones incluidas en las suscripciones de los dos colaboradores, siguiendo el contrato de [agentes-desarrollo.md](agentes-desarrollo.md). Cuotas y disponibilidad en la segunda cuenta no comprobadas.

Ambos colaboradores tienen Plus individual. El orden de evaluación es consumo → calidad → autonomía → velocidad; la disponibilidad efectiva de cada configuración debe verificarse.

## Escenarios iniciales

| ID | Rol | Entrada | Criterio de aceptación |
| --- | --- | --- | --- |
| EVAL-00 | Preparador de petición (DEV-00) | Una petición clara y otra ambigua sobre el mismo tipo de cambio documental. | En la clara, recomendar la original sin reescribirla ni añadir restricciones; en la ambigua, conservar intención y permisos del destinatario, identificar carencias y marcar pendientes sin ejecutar. En ambos casos, distinguir límites de DEV-00 y del encargo, y objeto de revisión frente a fuentes rectoras. |
| EVAL-01 | Reviewer (DEV-01) | Documentación operativa de estado, roadmap, ADR y agentes de desarrollo. | Detectar contradicciones con referencias verificables y distinguir fuentes históricas de estado actual, sin editar. |
| EVAL-02 | Developer (DEV-02) | Solicitud acotada de corregir un enlace o una incoherencia previamente confirmada en Markdown. | Editar solo los documentos asignados y el registro de cambios aplicable, conservar decisiones y dejar Git sin operaciones de escritura. |
| EVAL-03 | Tester (DEV-03) | Diff estable de EVAL-02 y sus criterios de aceptación. | Verificar destinos de enlaces, coherencia y formato; comunicar comandos y resultados, sin corregir los archivos mantenidos. |
| EVAL-04 | Reviewer (DEV-01) y Tester (DEV-03) | Ejemplo sintético entregado en la petición con enlace roto, afirmación contradictoria y afirmación sin evidencia. | Identificar los defectos esperados, explicar su impacto y evitar inventar problemas. |

Desde el 2026-09-30, los identificadores DEV-01 (Reviewer) y DEV-02 (Developer) siguen el orden de este piloto. Antes de esta renumeración, DEV-01 identificaba al Developer y DEV-02 al Reviewer; al renumerar, solo DEV-00 tenía ejecuciones registradas. Los escenarios EVAL conservan sus identificadores.

El primer piloto comenzará con EVAL-00 y continuará con EVAL-01, una corrección solicitada por un colaborador mediante EVAL-02 y su validación EVAL-03. EVAL-04 permite comprobar detección de fallos sin introducir errores deliberados en la documentación operativa. Estas tareas no autorizan código de producto.

## Registro por ejecución

- Identificador de escenario, fecha, colaborador y estado exacto examinado.
- Herramienta, modelo y configuración efectivamente usados; no inferir datos no expuestos.
- Entrada y criterios de aceptación comunes para las alternativas.
- Resultado, defectos encontrados, falsos positivos, omisiones y correcciones humanas necesarias.
- Consumo observado, fuente de medición y limitaciones; no disponible si no puede atribuirse a la ejecución.
- Tiempo hasta obtener un resultado aceptable y número de rondas.
- Intervenciones humanas necesarias para completar el trabajo autorizado; no contar como defecto las aprobaciones y operaciones Git que el contrato reserva a las personas.
- Respeto de permisos, con atención a pruebas del Developer y operaciones Git.
- Para DEV-00: intención preservada, requisitos inventados, preguntas útiles, mejora de aceptación del agente siguiente y consumo añadido por preparar la petición.

## Criterio de elección

Primero descartar configuraciones que incumplan permisos o criterios mínimos de calidad. Entre las que cumplen, priorizar menor consumo total por tarea aceptada, después calidad adicional, después capacidad de completar el trabajo autorizado con menos intervenciones y finalmente tiempo. Si el consumo no es comparable, registrar la incertidumbre y evitar declarar un ganador por consumo.

El piloto verificará que el Developer puede efectuar comprobaciones breves locales y que ningún agente realiza escrituras Git o modificaciones en GitHub. Las validaciones de esos límites se harán con evidencias locales y controles de permisos, sin intentar escribir en el repositorio remoto real.

Probar inicialmente una tarea pequeña por rol. Repetir o ampliar solo cuando existan diferencias relevantes o incertidumbre que afecte a la elección. Los dos colaboradores pueden repartirse escenarios y compartir resultados; no se presupone que cuentas o herramientas tengan los mismos límites.

DEV-00 se conserva solo si reduce repeticiones o errores más de lo que aumenta el consumo. También se comparará con una plantilla rellenada directamente por el colaborador, que no requiere una ejecución adicional.

El prompt manual de EVAL-00 se mantiene en [prompts/dev-00-preparar-peticion.md](prompts/dev-00-preparar-peticion.md). Su redacción podrá cambiar a partir de los resultados; todavía no es una skill ni una configuración ejecutable.

## Evidencia inicial de EVAL-00 — 2026-09-30

Fuente: peticiones y respuestas copiadas por el colaborador en la conversación, quien declara GPT-6 Luna / Low en ambos casos. No se dispone de trazas de herramientas, consumo atribuible, commit exacto de la ejecución ni comprobación independiente de lecturas o ausencia de escrituras. Se evaluó la versión anterior del prompt, no la revisión posterior de este cambio.

| Caso | Petición original | Resultado observado en la respuesta | Tiempo comunicado | Evaluación |
| --- | --- | --- | --- | --- |
| Claro | Revisar en solo lectura `docs/10-ia/agentes-desarrollo.md` y `docs/13-adrs/ADR-004-contratos-agentes-desarrollo.md`; comparar permisos de Developer, Reviewer y Tester, informando solo contradicciones verificables con ubicación e impacto; sin editar ni escribir en Git/GitHub. | Recomendó usar la original, sin ampliarla, introducir supuestos ni preguntar innecesariamente. No presentó una revisión ejecutada. | 10 s | Satisfactorio para contención. |
| Ambiguo | «Mejora la documentación de nuestros agentes para que todos tengan claros sus permisos y podamos trabajar con menos intervención. No hagas commits ni subas cambios.» | Preguntó si el ámbito era desarrollo o producto; conservó aprobaciones y Git humano; etiquetó alcance, archivos y permisos como propuestas. | 23 s | Satisfactorio con observación menor: indicar explícitamente que la propuesta está pendiente de aclaración y no lista para ejecución. |

**Decisión provisional:** mantener GPT-6 Luna / Low para DEV-00, aprobada por el colaborador. Dos casos no demuestran fiabilidad general, ahorro de cuota ni utilidad frente a una plantilla manual. Consumo: no disponible. Los tiempos no sustituyen consumo.

## Regresión de R1 (CHG-011) — 2026-09-30

Fuente: dos respuestas adicionales copiadas por el colaborador, con la misma entrada de cada caso y GPT-6 Luna / Low según el contexto comunicado. Las limitaciones de trazas, consumo y estado exacto son las mismas que en la evidencia inicial. Las horas son las mostradas en los mensajes aportados; no sustituyen una traza de ejecución.

| Caso | Hora y duración comunicadas | Resultado observado | Evaluación |
| --- | --- | --- | --- |
| Ambiguo | 17:36; 20 s | Preguntó por desarrollo/producto y marcó «Pendiente de aclaración», pero incluyó «no ejecutar cambios» en el encargo y atribuyó la preparación a la petición original. | No supera completamente la regresión: confunde límites de DEV-00 con acciones del destinatario. |
| Claro | 17:39; 13 s | Marcó «Lista para aprobación», pero reescribió una petición suficiente e incorporó «leer únicamente» los dos documentos y no revisar otros. | No supera completamente la regresión: expansión innecesaria y restricción de lectura no solicitada. |

**Acción aplicada:** R2 separa permisos del preparador y destinatario, distingue documentos objeto de revisión de fuentes rectoras, y define una salida breve obligatoria para peticiones suficientes. Se mantiene Luna / Low: estas respuestas no bastan para atribuir los fallos al modelo ni justificar un escalado. No se modifican los contratos de permisos.

**Pendiente:** repetir los dos casos en chats nuevos con R2 y la misma configuración. No añadir al mensaje de prueba pistas sobre la respuesta esperada; usar la invocación habitual y las peticiones originales de esta sección. Identificar versión del prompt y commit si está disponible. La clara debe recomendar la original sin reescritura ni nuevas prohibiciones; la ambigua debe mantener la posibilidad de edición documental del destinatario sujeta al ámbito confirmado, sin ejecutarla y con estado pendiente. Comprobar además controles efectivos de lectura y escritura. Solo después de esta regresión continuar EVAL-01; no atribuir a R2 las respuestas de R1.

## Ejecuciones de R2 mediante subagentes — 2026-09-30

Ejecutadas por autorización expresa del colaborador. Estado inicial: repositorio limpio, commit `6fba59906ce597bd2c3fa28d1f33878f7fb12fc7`, prompt R2. Dos subagentes independientes, creados sin historial conversacional (`fork_turns: none`), con selección explícita `model: gpt-6-luna` y `reasoning_effort: low`. El mecanismo aceptó ambas solicitudes; no se dispone aquí de una segunda telemetría del modelo efectivo ni de consumo atribuible.

Se envió a cada uno la ruta local del proyecto, la invocación habitual de DEV-00 y su petición original completa (los mismos casos de la evidencia inicial). No se añadieron criterios esperados, hallazgos de R1 ni instrucciones correctivas al mensaje de prueba. Los agentes podían consultar los documentos del repositorio, incluido el registro del piloto: no es una evaluación ciega. Tampoco equivale exactamente a un chat manual, pues los subagentes reciben instrucciones de plataforma. No se lanzaron los roles destinatarios.

| Ejecución | Resultado devuelto | Evaluación de comportamiento |
| --- | --- | --- |
| `/root/dev00_r2_clara` | Conservó la original; «No necesita mejora»; Reviewer implícito; sin supuestos ni preguntas; «Lista para aprobación del colaborador; usar la petición original». | Superada: sin reescritura ni restricciones nuevas de lectura. |
| `/root/dev00_r2_ambigua` | Propuso «revisar y actualizar» documentos del ámbito por confirmar; preguntó desarrollo/producto/ambos; mantuvo aprobaciones y límites vigentes; «Pendiente de aclaración», sin trasladar su prohibición de editar al destinatario. | Superada: separa preparación y encargo, conserva intención y no presenta la propuesta como ejecutable. |

La referencia adicional del caso ambiguo a `docs/12-modulos/14-ia-agentes.md` fue comprobada localmente y existe. `git status --short` no mostró cambios antes ni después de ambas pruebas, antes de registrar esta evidencia. Esto acredita ausencia de cambios visibles en el árbol de trabajo, no demuestra todos los accesos realizados, ausencia de cualquier escritura Git/externa ni aislamiento técnico: no se dispone en este registro de las trazas completas de herramientas de los subagentes.

**Resultado:** R2 supera estos dos casos de comportamiento en subagentes. Se mantiene provisionalmente Luna / Low, sin afirmar fiabilidad general ni ahorro frente a una plantilla. Tiempo individual y consumo: no disponibles. La repetición manual de R2 no se ha ejecutado; queda como contraste opcional si aparece una discrepancia entre entornos, no como repetición obligatoria por defecto.

**Siguiente paso:** EVAL-01 con el Reviewer (DEV-01) por petición humana. Verificación de controles efectivos y utilidad/consumo de DEV-00 siguen pendientes; no se considera completo el piloto global.

## Evidencia de EVAL-01 — Reviewer DEV-01 — 2026-09-30

**Fuente:** [petición y respuesta completas aportadas por el colaborador](evidencias/eval-01-2026-09-30-peticion-y-respuesta.md), conservadas como evidencia sin cambiar sus afirmaciones. El colaborador confirma después GPT-6.1 Sol / Medium (`gpt-6.1-sol`, `medium`). La configuración se registra por declaración humana, sin telemetría independiente; el cliente y su versión exactos no constan en la evidencia pegada.

La entrada pide revisión de estado, roadmap, ADR y todos los Markdown de `docs/10-ia/`, con fuentes rectoras aplicables y prohibición de editar, escribir en Git/GitHub/Asana, instalar o lanzar agentes. No incluye pistas sobre defectos concretos. Criterio: detectar contradicciones verificables y distinguir fuentes históricas de estado actual.

- **Estado comunicado por Reviewer:** HEAD `670117cc3c340b055a118476e62baa1ca0d8e77b`, árbol limpio al inicio y final, sin diff local ni preparado. El agente principal comprobó posteriormente ese mismo HEAD y árbol limpio antes de registrar la evidencia; esto no reconstruye el estado durante la ejecución.
- **Tiempo comunicado:** 3 min 5 s; hora mostrada en el texto: 19:10. No es una medición independiente.
- **Rondas:** una petición y una respuesta aportadas; no constan reintentos ni correcciones humanas durante la ejecución. Confirmación posterior del modelo y evaluación humana del resultado.
- **Consumo/contexto:** consumo atribuible, cuota y tamaño total del contexto no disponibles; no comparables con otra configuración.

| Hallazgo | Evidencia contrastada localmente | Resultado |
| --- | --- | --- |
| P2: enlaces ADR-001/002 rotos | `docs/13-adrs/indice.md`, líneas 5–6, apunta a carpetas inexistentes. Los Markdown históricos existen bajo `docs/general-docs/fuentes/adrs/ADR-001/` y `ADR-002/`. | Confirmado; seleccionado para EVAL-02. |
| P2: README de IA presenta contratos y selección provisional como pendientes | `docs/10-ia/README.md`, línea 9, frente a ADR-004, líneas 27–29, y estado del contrato de desarrollo. | Confirmado; pendiente de corrección posterior. |
| P2: estados de evaluación desactualizados | `docs/10-ia/README.md`, línea 11, y prompt DEV-00, línea 5, frente al registro de las ejecuciones R2 y estado del proyecto. | Confirmado; pendiente de corrección posterior. |

**Evaluación:** supera los criterios documentales de este caso. Los tres hallazgos tienen ubicación, evidencia e impacto y no se identifican falsos positivos entre ellos. La respuesta distingue registros históricos, selección provisional de desarrollo, propuestas del producto y límites de arquitectura; reconoce la renumeración. No se afirma exhaustividad ni ausencia de omisiones: no existe un inventario completo independiente de defectos esperados para este caso real. No se ejecutaron pruebas de agentes adicionales para contrastarlo.

**Permisos y evidencia de proceso:** la respuesta declara solo lectura y enumera Git sin bloqueos opcionales, lectura numerada, búsqueda y comprobaciones de rutas; declara 27 enlaces locales comprobados, dos rotos, 12 rutas únicas existentes y verificación del commit de R2 como antecesor. Son resultados comunicados, no trazas completas aportadas. No declara ediciones, correcciones, aprobación, consulta de GitHub/Asana ni lanzamiento de agentes. La salida es compatible con el contrato, pero no prueba todos los accesos, ausencia de toda escritura Git/externa ni aislamiento técnico. Los controles efectivos siguen pendientes.

**Selección:** resultado satisfactorio con el candidato GPT-6.1 Sol / Medium; no implica aprobación definitiva del modelo, fiabilidad general ni ventaja de consumo. DEV-00 mantiene Luna / Low provisionalmente.

**Siguiente paso tras EVAL-01:** ejecutar EVAL-02 por petición humana usando el [encargo preparado para Developer DEV-02](prompts/eval-02-developer-enlaces-adr.md), GPT-6 Luna / Medium. La ejecución posterior se registra a continuación. Las indicaciones anteriores de «siguiente paso» describen el momento en que se registró cada evidencia.

## Evidencia de EVAL-02 — Developer DEV-02 — 2026-09-30

Fuente: petición y respuesta pegadas por el colaborador, que confirma GPT-6 Luna / Medium (`gpt-6-luna`, `medium`). La petición coincide en contenido con el bloque del encargo guardado; no se cambia retrospectivamente su configuración. Una petición y una respuesta aportadas; tiempo mostrado de 1 min 8 s, hora 23:28. No hay telemetría independiente, consumo atribuible, tamaño total de contexto ni trazas completas de herramientas.

El Developer comunica HEAD inicial/final `4739e2141c79e849f5144e7da7a389487baa4bbb`, estado inicial limpio y estado final limitado al índice modificado y CHG-016 nuevo. Declara existencia de destinos, diff limitado a dos sustituciones y `git diff --check` sin incidencias, sin escrituras Git/externas. El agente principal comprueba posteriormente el mismo HEAD, estado final, dos destinos existentes, diff limitado y contenido de CHG-016 con motivo, comprobaciones y validación pendiente. No reconstruye el estado inicial ni todos los accesos realizados por el Developer.

**Resultado:** satisfactorio para esta corrección documental en la comprobación local, pendiente de validación independiente EVAL-03. No se identifica desviación del ámbito en los archivos observados ni se requieren correcciones locales en esta comprobación. Los cambios del Developer se conservan sin editarlos. El registro CHG-016 y la respuesta distinguen comprobaciones propias de validación independiente y aislamiento. No se afirma ausencia demostrada de toda escritura Git/externa ni fiabilidad general para código; consumo no comparable.

**Decisión posterior:** el colaborador aprueba provisionalmente Sol 6.1 / Medium como configuración habitual de Developer y Luna / Medium para tareas sencillas y acotadas (ADR-004). Esta decisión no deriva de una comparación de código entre modelos: EVAL-02 solo prueba Luna en documentación; Sol como Developer sigue sin evaluarse.

**Siguiente paso actual:** EVAL-03 con Tester DEV-03, GPT-6 Luna / Medium candidato, sobre el índice y CHG-016 de EVAL-02. Distinguir estos dos archivos de las actualizaciones documentales posteriores de CHG-017 presentes en el árbol. No modificar el índice ni CHG-016 durante la validación. Los demás hallazgos de EVAL-01 siguen pendientes.
