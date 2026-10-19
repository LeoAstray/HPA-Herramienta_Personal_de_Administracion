# CHG-032 — Retirada de canales y compatibilidad de la sesión EVAL-05

## Fuente y alcance

Preparado el 2026-10-16 por petición de continuación acotada. El colaborador comunica aprobación de la PR de preparación documental; no comunica aquí merge ni cierre del issue. La entrega anterior conserva el alcance registrado en CHG-029 a CHG-031. No se reabre para exigir preparar todo el laboratorio o completar la evaluación.

Lectura inicial: rama `41-eval-05-revisar-la-ficha-del-entorno-y-preparar-g2g6`, HEAD `2b2fdb03b7d19b7074d161f58175856af43d272c` y árbol limpio. El seguimiento local figura como desaparecido; ese dato no acredita merge ni estado remoto. El checkout sí contiene ficha/guía/encargo R2, CHG-029 a CHG-031, guía de preparación, plantilla y generador. No se hace fetch ni ninguna operación Git de escritura.

## Análisis y diseño del procedimiento

Se aplica OpenAI Docs y se consultan las fuentes oficiales enlazadas en la [sección de retirada de canales](../10-ia/preparacion-raiz-perfiles-eval-05.md#5-retirar-canales-en-la-sesión-exclusiva-del-laboratorio). Se distinguen MCP directos, MCP de plugins y otros mecanismos. Las opciones documentadas de `requirements.toml` no se presentan como claves ordinarias equivalentes de configuración local.

La consulta filtrada de configuración de usuario identifica `node_repl` como MCP directo, sin `enabled` declarado. Los manifiestos locales vinculan `codex_app` con `codex-app-tools@openai-bundled`, `code-review` con `code-review@openai-bundled` y `cua_repl` con `unified-computer-use@openai-bundled`. Estos plugins y `browser@openai-bundled` y `computer-use@openai-bundled` figuran habilitados en configuración de usuario. Los dos últimos no declaran MCP en los manifiestos consultados. No se establece la procedencia de `codex_apps` ni de `codex_worktrees` con esa consulta; su origen/carga requieren evidencia del cliente separado. Estas lecturas no sustituyen ni alteran el inventario humano histórico de CHG-031.

La extracción solo muestra nombres, procedencia y estados; no imprime configuración completa, argumentos, credenciales, cabeceras ni variables sensibles. Se consulta versión/ayuda del lanzador local: CLI 0.163.0 y opciones `--strict-config`, `--no-daemon`, `--cd` y `-c`; esto no identifica un nuevo arranque humano ni verifica controles del laboratorio.

## Cambios documentales

- Guía ampliada con bloque manual para agregar un [fragmento de canales](../10-ia/plantillas/eval-05-canales.toml) al archivo local del laboratorio, previa comprobación del hash de la plantilla y conservación de copia privada. El fragmento desactiva el MCP directo, los cinco plugins identificados, apps, hooks, catálogo remoto e instalación de dependencias MCP de skills.
- Arranque nuevo de inspección que conserva MXC explícito, Sol / Medium, `agents.enabled=false`, perfil y restricciones previas; sin prompt de trabajo.
- Evidencia mínima depurada por canal, criterios de resultado compatible/limitado y recuperación local. Un canal persistente, un error de conexión o falta de inventario no se convierten en aislamiento demostrado.
- Preparación de `docs/10-ia/issue-eval-05-canales-y-compatibilidad.md` como borrador temporal, con problema, alcance, entregables y aceptación limitada a canales y compatibilidad. El resultado limitado requiere aceptación humana expresa para cerrar ese issue sin retirada conseguida.
- Roadmap actualizado con aprobación comunicada, disponibilidad del contenido en checkout y tareas posteriores separadas. No cambia contratos ni arquitectura de producto; no requiere ADR nueva.

## Verificación y límites

Comprobaciones locales sobre los cinco archivos de esta entrega, incluidos los tres nuevos:

- Cuatro Markdown: 45 enlaces locales y 14 anclas resueltos, sin incidencias; rutas del cuerpo publicable del issue, formato, saltos finales, espacios finales y marcadores de conflicto comprobados.
- Ocho bloques PowerShell de la guía, incluidos los dos de la nueva sección: análisis sintáctico correcto en Windows PowerShell `5.1.26100.9711` y PowerShell `7.6.5`, sin ejecutarlos.
- Fragmento y combinación con la plantilla analizados con `tomllib`: TOML válido, cuatro features desactivadas, cinco plugins desactivados y solo `node_repl` añadido como MCP directo. Todas las reglas y valores de la plantilla base se conservan.
- Hashes de ficha R2, encargo R2, guía de revisión R2 y plantilla de permisos iguales a CHG-029; registros históricos sin modificaciones.
- Ausencia de rutas personales en la entrega y `git --no-optional-locks diff --check` sin errores. El aviso de conversión LF/CRLF de Git no es un error de sintaxis ni una evidencia del laboratorio.

No se modifica el laboratorio ni su configuración desde esta sesión. Tampoco se ejecutan sondas, se entrega el encargo Developer o se invocan canales del laboratorio. No se realizan escrituras Git, cambios de configuración global, accesos a GitHub/Asana ni publicación del issue. La preparación no demuestra exclusión del evaluador, controles efectivos ni cobertura/custodia completa de trazas. El avance, los pendientes y el siguiente paso se mantienen solo en el [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05).

## Retirada del borrador tras publicación manual — 2026-10-16

El colaborador comunica «Issue publicado» y que va a seguir los pasos. Conforme al tratamiento del archivo como borrador temporal acordado en este chat, se elimina el borrador local del issue y se corrigen las referencias en guía y roadmap. Se conserva arriba la constancia histórica de su preparación; el número y enlace del issue no se han facilitado. No se accede a GitHub ni se atribuye ejecución del procedimiento a esa comunicación. La guía, el fragmento y las evidencias previas se conservan.

Verificación de esta retirada: borrador ausente, 41 enlaces locales y 13 anclas resueltos en los tres documentos afectados, formato y `git --no-optional-locks diff --check` sin errores. Los bloques manuales no se modifican ni se ejecutan.

## Aplicación humana y fallo posterior — 2026-10-16

El colaborador aporta el hash final del bloque de aplicación y después el fallo del arranque por `invalid transport` en `[mcp_servers.node_repl]`. La [evidencia](../10-ia/evidencias/eval-05-2026-10-16-configuracion-canales.md) conserva entrada y salidas con ruta normalizada. El hash coincide con la combinación histórica reconstruida, pero el cliente rechaza la entrada MCP sin transporte; la validez TOML comprobada anteriormente no acreditaba esa compatibilidad. [CHG-033](CHG-033-correccion-transporte-y-guia-sesiones-codex.md) registra la corrección del fragmento y el procedimiento de reparación, sin alterar el alcance de la evidencia anterior.
