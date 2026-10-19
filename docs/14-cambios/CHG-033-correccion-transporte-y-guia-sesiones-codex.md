# CHG-033 — Corrección del transporte MCP y guía de sesiones Codex

## Fuente y alcance

Preparado el 2026-10-16. El colaborador solicita guardar la salida del bloque de aplicación y comprobar rama, relación con `main` y alcance de cambios. Durante ese trabajo comunica el fallo del siguiente arranque, `invalid transport` en la tabla local de `node_repl`, y solicita un Markdown sobre creación y uso de sesiones Codex.

Se conservan ambas salidas en la [evidencia de configuración y arranque](../10-ia/evidencias/eval-05-2026-10-16-configuracion-canales.md), con ruta normalizada y sin datos personales. No se ejecuta el laboratorio desde HPA ni se entrega el encargo Developer.

## Comprobación Git de lectura

Rama observada: `50-eval-05-retirar-mcp-y-otros-canales-de-la-sesión-del-laboratorio-y-resolver-compatibilidad`. HEAD, `main`, `origin/main` y la rama de seguimiento local coinciden en `8094ac5487403ff80648e19b92e49426d609a1ad`; las tres comparaciones de commits devuelven `0 0`. No hay cambios en staging ni commits propios adicionales respecto de `main`.

Antes de esta actualización había cuatro archivos pendientes: roadmap, guía de preparación, fragmento de canales y CHG-032. Su contenido corresponde a la tarea nueva de canales; la preparación documental anterior ya está incluida en el historial local de `main`, mediante `2b2fdb0`, `485ffeb` y `8094ac5`. Esto permite distinguir integración local del estado del issue anterior, cuyo cierre no se ha confirmado aquí.

La referencia almacenada `origin/main` tiene entrada de reflog del 2026-10-16 a las 01:16:48 +02:00. No se realiza fetch, se accede al remoto ni se escribe Git; la comparación acredita coincidencia con las referencias locales disponibles, sin garantizar que el remoto no haya cambiado después.

## Hallazgo y corrección

El hash comunicado coincide exactamente con la combinación histórica de plantilla, separador CRLF y fragmento de CHG-032 reconstruida en memoria. El TOML conserva las reglas base, pero la declaración parcial del MCP carece de transporte y el arranque humano la rechaza. La comprobación sintáctica anterior no había detectado esa incompatibilidad de Codex; no se presenta como validación suficiente de configuración.

Se consulta OpenAI Docs, en particular [Configuration Reference](https://learn.chatgpt.com/docs/config-file/config-reference), [opciones CLI](https://learn.chatgpt.com/docs/cli/reference) y [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic). La definición existente puede deshabilitarse mediante un override de invocación. Una consulta local de configuración, con salida capturada y filtrada, acepta `-c mcp_servers.node_repl.enabled=false` y devuelve `node_repl`, `enabled=false`, código 0. No abre una conversación ni conecta MCP; ese resultado no se atribuye al laboratorio humano.

Cambios:

- Se retira la tabla parcial de `node_repl` del [fragmento](../10-ia/plantillas/eval-05-canales.toml). Las features y los cinco plugins conservan sus valores.
- La [guía](../10-ia/preparacion-raiz-perfiles-eval-05.md#corregir-el-fragmento-anterior-tras-invalid-transport) incorpora reparación manual con comprobación de los hashes de archivo fallido y copia base, conservación del fallido y reconstrucción a partir de la base y del fragmento corregido. No recopia sobre contenido distinto ni borra evidencia.
- El arranque corregido agrega `-c mcp_servers.node_repl.enabled=false`; mantiene MXC explícito, Sol / Medium, subagentes desactivados y todas las restricciones del perfil. No copia transportes, argumentos o credenciales de la configuración personal.
- Se crea la [guía de sesiones Codex](../10-ia/guia-sesiones-codex.md), solicitada por el colaborador, y se enlaza desde el README de IA. Es una referencia operativa de aplicación/CLI y contratos existentes; no amplía el alcance de aceptación del issue de canales, aprueba producto ni redefine perfiles.
- Se actualiza el roadmap con evidencia de aplicación, fallo de arranque, comparación local con `main` y continuación. CHG-032 conserva su estado histórico con referencia a esta corrección.

## Verificación y límites

Comprobaciones locales de los ocho archivos pendientes de esta entrega, incluidos cinco nuevos:

- Siete Markdown: 76 enlaces locales y 23 anclas resueltos; formato y minimización de rutas personales sin incidencias.
- Catorce bloques PowerShell de la guía de laboratorio, la guía de sesiones y la evidencia histórica: análisis correcto en Windows PowerShell `5.1.26100.9711`, sin ejecutar los bloques.
- Fragmento y combinación corregidos válidos como TOML; cuatro features y cinco plugins desactivados, sin tabla MCP parcial y con todas las reglas de la base intactas. El arranque de la sección corregida incluye el override de `node_repl`.
- Hashes de ficha R2, encargo R2, guía humana R2 y plantilla de permisos iguales a CHG-029. Borrador del issue ausente.
- Diff y estado Git dentro del alcance: tres archivos modificados y cinco nuevos; staging vacío, `main...HEAD` y `origin/main...HEAD` sin commits de diferencia, `git --no-optional-locks diff --check` sin errores.

SHA-256 del fragmento corregido: `E14FF01DB64F02CBCFBD70980F4CF8068F8470196F24B114ADC2D5511EC7D138`. La combinación de los bytes actuales de la base, CRLF y ese fragmento produce en memoria `95DFB02A221F36EC1AD370E406D76D26EB3B17651B0AA4011C6BD9C9BCDC1791`. Este último es un valor previsto para el archivo reconstruido, no una salida aportada por la persona; los hashes identifican bytes, incluidos sus saltos de línea.

La consulta filtrada de configuración descrita arriba es distinta de una prueba de permisos o de una conexión MCP. La sintaxis corregida requiere un nuevo arranque humano para comprobar su efecto en el laboratorio.

No se modifica la configuración del laboratorio ni la global desde HPA. Tampoco se escribe Git ni se accede a GitHub/Asana. El fallo impide completar el nuevo inventario; no demuestra retirada efectiva, aislamiento ni ejecución de casos. El avance, los pendientes y el siguiente paso se mantienen solo en el [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05).

## Confirmación humana de reparación y canal restante — 2026-10-16

El colaborador aporta el hash previsto de reparación y un nuevo `/status`, `/debug-config` y `/mcp`. La [evidencia](../10-ia/evidencias/eval-05-2026-10-16-configuracion-canales.md#4-reparación-e-inspección-humanas-posteriores) conserva únicamente el extracto técnico: arranque con CLI 0.163.0, Sol / Medium, perfil `eval05-developer`, aprobación `never`, selección MXC, subagentes desactivados y `node_repl` deshabilitado. No se copian cuenta, cuotas, identificador de sesión ni rutas personales. El hash que antes era un cálculo previsto queda ahora también aportado por la persona.

Persiste `codex_worktrees`, conectado con tres herramientas; los otros cuatro nombres del inventario anterior no aparecen en el nuevo listado, sin que se les asigne un estado no mostrado. No se da por completa la retirada ni la cobertura de otros mecanismos.

La consulta filtrada de configuración de sistema/usuario no identifica una entrada directa de ese servidor. Las fuentes oficiales de [comandos](https://learn.chatgpt.com/docs/developer-commands) y [opciones CLI](https://learn.chatgpt.com/docs/cli/reference) documentan `features list`, el override `--disable` y `/mcp verbose`. El inventario de la CLI instalada identifica `worktrees`, estable y `true`; una consulta con `--disable worktrees` devuelve `false` y código 0, sin modificar configuración persistente ni conectar MCP. Esto verifica el reconocimiento de la feature en esa instalación, no todavía su efecto en el laboratorio humano.

Se añade `--disable worktrees` al arranque manual de la guía, conservando las demás opciones y el archivo ya reparado. Si el servidor persiste, la guía limita el siguiente diagnóstico a nombres, estados y procedencia expuesta mediante `/mcp verbose`, sin ejecutar herramientas ni copiar argumentos o URLs privadas. El roadmap registra la continuación, sin ampliar el trabajo a sondas ni casos.

Verificación de esta actualización: catorce bloques analizados sin errores en Windows PowerShell 5.1, sin ejecutarlos; 78 enlaces locales y 25 anclas resueltos en los siete Markdown de la entrega; datos privados excluidos, hash reconstruido igual al comunicado y formato/diff sin errores.

## Confirmación de worktrees y preparación de los demás canales — 2026-10-16

El nuevo inventario humano muestra solo `node_repl` deshabilitado con cero herramientas, y declara `features.worktrees=false` junto con los otros flags del arranque. `codex_worktrees` ya no aparece; se conserva esa [evidencia depurada](../10-ia/evidencias/eval-05-2026-10-16-configuracion-canales.md#6-inspección-humana-tras-desactivar-worktrees). Queda observado un inventario MCP sin conexiones, sin equipararlo a retirada completa de mecanismos nativos ni aislamiento.

Para evitar inferir el estado de otros canales de la sola lista MCP, se consulta `features list` en la instalación documental con nombres y estados filtrados. Se reconocen `browser_use`, `browser_use_external`, `computer_use`, `image_generation` y `realtime_conversation`. Una consulta con sus `--disable`, junto con apps, hooks, catálogo, instalación de dependencias y worktrees, devuelve las diez features en `false` y código 0. No se abre una conversación ni se conecta un canal para probarlo.

La guía añade estos overrides y `web_search=disabled` al mismo arranque manual. Son opciones por invocación, sin modificar el archivo reparado, política gestionada ni configuración global; la referencia oficial distingue los controles de voz de la CLI de otras superficies. Se mantienen comandos y edición del perfil, sin intentar resolver aquí sus futuras pruebas de permisos. El roadmap conserva como pendiente el extracto de los nuevos flags y los límites del inventario nativo, sin reabrir la entrega anterior ni ejecutar casos.

Verificación de esta actualización: catorce bloques PowerShell analizados sin errores en Windows PowerShell 5.1, sin ejecutarlos; 79 enlaces locales y 26 anclas resueltos en los siete Markdown de la entrega; hash combinado conservado, diez overrides en el arranque y comprobaciones de formato, privacidad y diff sin errores.

## Confirmación humana de los controles explícitos y entrega para revisión — 2026-10-16

El colaborador aporta `/debug-config` con los diez controles de features desactivados, búsqueda web deshabilitada, `node_repl` y subagentes desactivados, Medium y selección MXC. El cliente sigue mostrando solo `node_repl` deshabilitado con cero herramientas en `/mcp`. La [evidencia normalizada](../10-ia/evidencias/eval-05-2026-10-16-configuracion-canales.md#8-confirmación-humana-de-los-controles-explícitos-de-canales) conserva el extracto y un cotejo por canal; no copia rutas personales ni atribuye un nuevo `/status` o hash no aportados.

Se documenta la compatibilidad y configuración declarada observadas. Se preservan como límites la ausencia de un inventario exhaustivo de mecanismos nativos y del estado individual de los plugins en los diagnósticos. No se declara retirada técnica total, aislamiento, controles efectivos ni casos ejecutados. La guía delimita el cierre de la inspección y el roadmap deja la revisión/integración/cierre manual como continuación de esta entrega, sin exigir más reinicios ni completar G2–G6 dentro de este issue.

Verificación de esta actualización documental: 82 enlaces locales y 29 anclas correctos en los siete Markdown de la entrega; extracto final cotejado con las diez features en `false` y demás campos aportados, sin rutas personales ni datos de cuenta; formato y diff sin errores. No cambian bloques ejecutables ni plantillas y no se repiten pruebas de sintaxis ya superadas.
