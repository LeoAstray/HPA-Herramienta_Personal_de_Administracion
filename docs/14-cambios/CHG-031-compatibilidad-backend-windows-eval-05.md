# CHG-031 — Compatibilidad del backend Windows para EVAL-05

## Fuente y alcance

Registrado el 2026-10-15. Tras instalar la CLI 0.162.1 mediante npm, el colaborador aporta un fallo del arranque de inspección con workspace `agente`. El cliente informa de un borrador `/status` no enviado y de un error al cargar `AGENTS.md`: `elevated Windows sandbox requires effective :root read access`. No se inicia correctamente el hilo ni se completa la inspección del perfil.

La [plantilla de permisos](../10-ia/plantillas/eval-05-perfiles.toml) establece `:root = "deny"`. El procedimiento anterior no seleccionaba un backend compatible con esa restricción; faltaba concretar esa selección. El error identifica una incompatibilidad de arranque, no una prueba de denegación de acceso a un recurso sintético ni un caso P01–P13 ejecutado.

## Corrección del procedimiento

La [documentación oficial de Windows](https://learn.chatgpt.com/docs/windows/windows-sandbox) y la [referencia de configuración](https://learn.chatgpt.com/docs/config-file/config-reference) permiten seleccionar explícitamente `windows.sandbox=mxc` en CLI 0.162.0 y posteriores. La selección explícita falla si faltan capacidades nativas o las políticas impiden usar MXC; la preferencia `features.prefer_mxc` permite fallback y tiene un alcance distinto.

Se añade `-c windows.sandbox=mxc` al arranque manual de la [guía](../10-ia/preparacion-raiz-perfiles-eval-05.md#4-comprobar-el-entorno-antes-de-entregar-un-caso), conservando `--strict-config`, `--no-daemon` y workspace `agente`. El cambio afecta a esa invocación y no guarda una nueva selección global. La plantilla TOML, sus reglas y las copias existentes no se modifican; se conserva la denegación de `:root`.

El [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05) registra el fallo y la continuación. La disponibilidad de MXC y sus controles efectivos quedan pendientes de comprobación en la terminal humana. El arranque, si tiene éxito, solo habilita la inspección de configuración; no acredita aislamiento ni autoriza todavía el encargo Developer.

## Límites de comprobación

Se consulta documentación oficial y se prepara la invocación como texto. No se ejecuta el sandbox desde esta sesión de HPA para atribuir su resultado a la terminal humana. No se amplía lectura del host, cambia configuración personal, modifica el laboratorio, instala capacidades de Windows ni ejecutan agentes o casos de evaluación desde este chat.

Comprobaciones locales: formato, treinta y cinco enlaces relativos y diez anclas de tres documentos sin incidencias; seis bloques PowerShell y la invocación npm con MXC analizados sin errores de sintaxis, sin ejecutarlos. `git --no-optional-locks diff --check` correcto. La plantilla conserva SHA-256 `DDEF21F28986EA3A68F0D998772179D07092B842F01C587A7189DA78394EA010`, igual al registrado en CHG-029.

## Confirmación del arranque e inspección inicial — 2026-10-15

El colaborador aporta `/status` y `/debug-config`: CLI 0.162.1, workspace `agente`, `AGENTS.md`, perfil declarado `eval05-developer` con aprobación `never`, proyecto habilitado y selección de sesión `windows.sandbox = "mxc"`. No se declaran requisitos gestionados. El modelo mostrado es GPT-6.1 Sol con esfuerzo `xhigh` y la sección de agentes declara `enabled = true`.

Esto acredita un arranque satisfactorio con selección MXC y la configuración que declara el cliente. No verifica lecturas, escrituras, canales ni exclusión del evaluador; tampoco demuestra ejecución de un caso. El registro compartido conserva únicamente los datos técnicos necesarios de las salidas aportadas.

Se concreta un nuevo arranque de inspección con `--model gpt-6.1-sol`, `-c model_reasoning_effort=medium` y `-c agents.enabled=false`, conservando MXC y las reglas de permisos. Sol / Medium ya es la política provisional de Developer aprobada en ADR-004; no se introduce una nueva selección ni se cambia una evaluación en curso. Las opciones solo afectan a la sesión que abra la persona.

La [referencia oficial de configuración](https://learn.chatgpt.com/docs/config-file/config-reference) documenta esas claves; la [referencia de comandos](https://learn.chatgpt.com/docs/developer-commands) documenta `/quit` y `/mcp`. Se añade la confirmación de los valores y el inventario inicial de MCP a la guía; otros canales conservan sus requisitos de exclusión. El roadmap registra la evidencia y la continuación. No se modifica configuración global ni se inicia una sesión del laboratorio desde este chat.

Verificación de la actualización: tres documentos, treinta y cinco enlaces locales y diez anclas sin incidencias; seis bloques PowerShell y el nuevo arranque por ruta npm analizados sin errores y sin ejecutarlos. Formato, minimización de datos compartidos y `git --no-optional-locks diff --check` correctos. La plantilla TOML conserva su hash anterior. La confirmación efectiva de Medium, subagentes desactivados y canales corresponde al siguiente arranque humano.

## Confirmación posterior y alcance de cierre documental — 2026-10-15

El colaborador aporta nuevas salidas de `/status`, `/debug-config` y `/mcp`. El cliente declara CLI `0.163.0`, GPT-6.1 Sol / Medium, workspace `agente`, `AGENTS.md`, perfil `eval05-developer` con aprobación `never` y capa de proyecto habilitada. La capa de sesión declara `windows.sandbox = "mxc"`, `model_reasoning_effort = "medium"` y `agents.enabled = false`; la sección de agentes también muestra `enabled = false`. No se declaran requisitos gestionados. Se registra la versión que muestra esta salida, sin atribuir una causa al cambio respecto de la inspección anterior.

| Servidor MCP | Estado mostrado | Herramientas |
| --- | --- | --- |
| `code-review` | Deshabilitado | 0 |
| `codex_app` | Deshabilitado | 0 |
| `codex_apps` | Conectado | 177 |
| `codex_worktrees` | Conectado | 3 |
| `cua_repl` | Conectado | 3 |
| `node_repl` | Conectado | 4 |

La salida confirma la configuración declarada de esfuerzo y subagentes. Los cuatro MCP conectados impiden considerar completa la exclusión de canales prevista por la ficha; el inventario tampoco demuestra la cobertura de los demás canales. No se invocan esas herramientas en el laboratorio desde este chat ni se ejecutan casos. Se omiten datos de cuenta, rutas personales, sesión y cuotas del registro compartido.

Se contrasta el alcance facilitado por el colaborador para el issue de continuación documental vinculado a #36: revisión humana con observación y límites registrada en CHG-029, corrección autorizada aplicada, requisitos G2–G6 y futuro encargo preparados, seguimiento en roadmap y verificaciones locales. La configuración completa del laboratorio y la evaluación posterior no son condiciones de aceptación de ese issue. El roadmap recoge por separado el cierre documental manual y la continuación práctica; no se consulta ni modifica el issue remoto.

Se corrigen dos indicaciones de aplicación pendiente en el README de IA y al final de la guía: remiten a la evidencia centralizada en el roadmap, sin convertir las salidas del cliente en controles verificados. La ficha R2, el encargo R2, la guía de revisión R2 y la plantilla TOML conservan su contenido identificado en CHG-029.

## Verificación de la entrega documental — 2026-10-16

Se comprueba el conjunto de doce archivos locales de la entrega: seis modificados y seis nuevos, incluidos los dos archivos de plantillas.

- Diez documentos Markdown: ochenta enlaces locales y veinte anclas resueltos, sin fallos.
- Seis bloques PowerShell de la guía y el script generador: análisis sintáctico sin errores, sin ejecutarlos en esta comprobación. Las pruebas funcionales anteriores del generador y sus límites se conservan en CHG-030.
- Plantilla TOML válida; aprobación `never`, búsqueda web deshabilitada, denegación de `:root`, red de comandos deshabilitada y herencia de los tres perfiles contrastadas documentalmente.
- Hashes de ficha R2, encargo R2, guía de revisión R2 y plantilla iguales a los registrados en CHG-029.
- Saltos finales, espacios finales, marcadores de conflicto, ausencia de rutas personales y cuentas en los archivos compartidos y `git --no-optional-locks diff --check`: sin incidencias.

La comprobación parte de HEAD `5501a2a` y de los cambios locales de la rama `41-eval-05-revisar-la-ficha-del-entorno-y-preparar-g2g6`. No escribe Git, publica cambios, accede al remoto ni ejecuta casos. Los pendientes y el siguiente paso se mantienen en el roadmap.
