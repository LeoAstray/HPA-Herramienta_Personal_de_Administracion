# EVAL-05 — Aplicación, fallo y reparación de la configuración de canales

## Fuente y alcance

Salidas aportadas por el colaborador en este chat el 2026-10-16: aplicación del fragmento, fallo del primer arranque, reparación y nueva inspección. El registro conserva las salidas técnicas necesarias; se omiten indicadores `PS`/`>>`, cuenta, cuotas e identificador de sesión. Las rutas personales se sustituyen por la notación documental `/Tests/HPA-EVAL-05` o por categorías de procedencia. No se consulta el laboratorio desde la sesión de HPA.

El avance, los pendientes y la continuación se mantienen solo en el [roadmap](../../01-proyecto/roadmap.md#seguimiento-de-eval-05). La corrección está registrada en [CHG-033](../../14-cambios/CHG-033-correccion-transporte-y-guia-sesiones-codex.md).

## 1. Bloque de aplicación aportado

Entrada histórica, no instrucción para repetir. Corresponde al fragmento anterior que incluía una tabla parcial de `node_repl`:

```powershell
& {
    $ErrorActionPreference = 'Stop'
    $evalConfig = (Get-Item -LiteralPath '.\agente\.codex\config.toml').FullName
    $evalFragment = (Get-Item -LiteralPath '..\..\HPA-Herramienta_Personal_de_Administracion\docs\10-ia\plantillas\eval-05-canales.toml').FullName
    $evalBackup = Join-Path (Resolve-Path -LiteralPath '.\evaluador\evidencias').Path 'config-antes-retirada-canales.toml'
    $evalBaseHash = 'DDEF21F28986EA3A68F0D998772179D07092B842F01C587A7189DA78394EA010'
    if ((Get-FileHash -LiteralPath $evalConfig -Algorithm SHA256).Hash -ne $evalBaseHash) {
        throw 'La configuracion difiere de la plantilla. Revisar antes de combinar.'
    }
    if (Test-Path -LiteralPath $evalBackup) { throw 'Ya existe copia previa. Revisar sin sobrescribir.' }
    $evalExtra = [IO.File]::ReadAllText($evalFragment)
    Copy-Item -LiteralPath $evalConfig -Destination $evalBackup -ErrorAction Stop
    [IO.File]::AppendAllText($evalConfig, "`r`n" + $evalExtra, (New-Object Text.UTF8Encoding($false)))
    Get-FileHash -LiteralPath $evalConfig -Algorithm SHA256 | Select-Object Algorithm, Hash
}
```

Salida aportada, sin error visible:

```text
Algorithm Hash
--------- ----
SHA256    14BA0F1C0F09B8AD6B599A5B8F47EE12F21A300AC7529E931781B3DBA9BC6F89
```

Contraste local previo a corregir el fragmento: los bytes de la plantilla original, un separador CRLF y el fragmento anterior producen exactamente ese SHA-256 al combinarlos en memoria. No se leen ni modifican archivos del laboratorio para ese contraste.

| Entrada histórica | SHA-256 |
| --- | --- |
| Plantilla base de CHG-029 | `DDEF21F28986EA3A68F0D998772179D07092B842F01C587A7189DA78394EA010` |
| Fragmento de canales anterior | `C2A19419D7968274EFCF96E0F5DA405C472C8CEE2093A5D6BDCE7D04AC55F9CB` |
| Configuración combinada aportada y reconstruida | `14BA0F1C0F09B8AD6B599A5B8F47EE12F21A300AC7529E931781B3DBA9BC6F89` |

La combinación se puede analizar como TOML y conserva las reglas de la base. Ese análisis no valida los requisitos de transporte de Codex ni su aplicación efectiva. La salida final es coherente con haber completado el bloque de copia y escritura; no es una inspección independiente de la copia previa ni una prueba de retirada de canales.

## 2. Versión y arranque aportados

```text
codex-cli 0.163.0
```

Invocación histórica:

```powershell
codex --strict-config --no-daemon --cd .\agente `
    -c windows.sandbox=mxc `
    --model gpt-6.1-sol `
    -c model_reasoning_effort=medium `
    -c agents.enabled=false
```

Error aportado, con ruta normalizada:

```text
Error: loading config.toml:
/Tests/HPA-EVAL-05/agente/.codex/config.toml:55:1: invalid transport
   |
55 | [mcp_servers.node_repl]
   | ^^^^^^^^^^^^^^^^^^^^^^^
```

La combinación histórica reconstruida sitúa esa tabla en la línea 55, coincidiendo con el error. La declaración añadida era:

```toml
[mcp_servers.node_repl]
enabled = false
```

El cliente rechaza esa entrada sin transporte al cargar la configuración. No se completa un arranque ni se aportan nuevos `/status`, `/debug-config` o `/mcp`; no se cuenta como sonda ni como caso P01–P13.

## 3. Contraste de la corrección en la sesión documental

Tras consultar OpenAI Docs, se realiza únicamente una consulta local de configuración con `codex -c mcp_servers.node_repl.enabled=false mcp list --json`, capturando su salida y extrayendo solo nombre y estado. El comando termina con código 0 y devuelve `node_repl`, `enabled=false`. No se abre una sesión del laboratorio ni se invocan herramientas MCP; no se imprime la configuración completa ni los transportes personales.

Este contraste respalda la sintaxis del override de invocación en la instalación consultada. El nuevo arranque humano y el inventario efectivo conservan su comprobación separada. La [guía corregida](../preparacion-raiz-perfiles-eval-05.md#corregir-el-fragmento-anterior-tras-invalid-transport) retira la tabla parcial del fragmento y conserva la desactivación mediante el override.

## 4. Reparación e inspección humanas posteriores

El colaborador aporta el resultado del bloque de reparación:

```text
Algorithm Hash
--------- ----
SHA256    95DFB02A221F36EC1AD370E406D76D26EB3B17651B0AA4011C6BD9C9BCDC1791
```

Coincide exactamente con el valor previsto en CHG-033 para base, CRLF y fragmento corregido. A continuación aporta `/status`, `/debug-config` y `/mcp`; el siguiente extracto elimina datos de cuenta, cuotas, identificador de sesión y rutas personales:

| Campo de `/status` | Valor mostrado |
| --- | --- |
| Cliente | OpenAI Codex 0.163.0 |
| Modelo y esfuerzo | GPT-6.1 Sol / Medium |
| Proveedor | openai |
| Workspace, normalizado | `/Tests/HPA-EVAL-05/agente` |
| Permisos | `eval05-developer`, custom permissions, `never` |
| Instrucciones | `AGENTS.md` |
| Modo de colaboración | Default |

`/debug-config` declara cinco capas habilitadas, de menor a mayor precedencia: defaults empaquetados, sistema, usuario, proyecto y flags de sesión. No se conservan sus rutas personales. Los flags y la sección de agentes aportados incluyen:

```text
agents.enabled = false
mcp_servers.node_repl.enabled = false
model_reasoning_effort = "medium"
windows.sandbox = "mxc"

Requirements: <none>
[agents]: enabled = false
```

`/mcp` muestra únicamente:

| Servidor | Estado | Herramientas |
| --- | --- | --- |
| `codex_worktrees` | connected | 3 |
| `node_repl` | disabled | 0 |

Los nombres `code-review`, `codex_app`, `codex_apps` y `cua_repl` del inventario anterior no aparecen en esta lista. Se registra esa ausencia; no se les atribuye un estado `disabled` que esta salida no muestra. El cliente ofrece `/mcp verbose` para herramientas y recursos.

La reparación permite ahora el arranque y confirma valores declarados del perfil, modelo, subagentes y `node_repl`. `codex_worktrees` conserva tres herramientas conectadas. La salida tampoco inventaría todos los mecanismos nativos ni expone individualmente las cuatro features y los cinco plugins del archivo; no demuestra retirada completa, aislamiento, permisos efectivos ni cobertura de trazas. No se ejecutan casos.

## 5. Consulta acotada de la feature worktrees

Desde la sesión documental se consulta la CLI instalada sin abrir el laboratorio. `codex features list`, con salida capturada y filtrada, muestra:

```text
worktrees    stable    true
```

La consulta `codex --disable worktrees features list` termina con código 0 y muestra:

```text
worktrees    stable    false
```

La [referencia oficial de comandos](https://learn.chatgpt.com/docs/developer-commands) documenta el inventario de features y `/mcp verbose`; las [opciones CLI](https://learn.chatgpt.com/docs/cli/reference) documentan `--disable` como override para la invocación. No se usa `codex features disable`, que guardaría el cambio.

Esto identifica una feature reconocida y una forma aceptada de desactivarla en esta instalación. Su relación efectiva con el servidor observado `codex_worktrees` se comprobará en el nuevo arranque humano; no se atribuye todavía retirada a estas consultas de configuración. Las fuentes consultadas no establecen un transporte directo para ese servidor y no se inventa una entrada `mcp_servers.codex_worktrees`.

## 6. Inspección humana tras desactivar worktrees

El colaborador aporta una nueva salida de CLI 0.163.0 con workspace normalizado `/Tests/HPA-EVAL-05/agente`. `/mcp` muestra únicamente:

```text
node_repl: disabled (0 tools)
```

`codex_worktrees` ya no aparece en ese inventario. `/debug-config` vuelve a declarar habilitadas las capas de defaults empaquetados, sistema, usuario, proyecto y flags de sesión. Se conserva este extracto, sin rutas personales:

```text
agents.enabled = false
features.worktrees = false
mcp_servers.node_repl.enabled = false
model_reasoning_effort = "medium"
windows.sandbox = "mxc"

Requirements: <none>
[agents]: enabled = false
```

Esto confirma la desactivación declarada de `worktrees` y la ausencia del servidor correspondiente en el listado aportado. No aparecen servidores MCP conectados; el único listado está deshabilitado con cero herramientas. No se ha recibido un nuevo `/status` en este mensaje y no se reconstruyen sus campos por suposición.

El resultado acredita el inventario MCP que declara esta sesión. No inventaría por sí solo navegador nativo, Computer Use, generación multimedia u otros mecanismos, ni sustituye las posteriores comprobaciones de permisos y separación del evaluador.

## 7. Consulta acotada para los demás canales

Se consulta la CLI instalada desde la sesión documental mediante `features list`, con salida capturada y filtrada. Reconoce los nombres del siguiente conjunto. Una consulta con sus respectivos `--disable` termina con código 0 y muestra todos en `false`:

```text
apps                          stable    false
browser_use                   stable    false
browser_use_external          stable    false
computer_use                  stable    false
hooks                         stable    false
image_generation              stable    false
realtime_conversation         stable    false
remote_plugin                 stable    false
skill_mcp_dependency_install  stable    false
worktrees                     stable    false
```

La consulta incluye también `web_search=disabled`, `agents.enabled=false` y `mcp_servers.node_repl.enabled=false` como overrides. No se abre el laboratorio, se invocan canales ni se imprime configuración personal. La aceptación de nombres/opciones en esta instalación se distingue de la confirmación pendiente de sus valores en el nuevo arranque humano.

La [referencia CLI](https://learn.chatgpt.com/docs/cli/reference) documenta los overrides de features por invocación. La [referencia de configuración](https://learn.chatgpt.com/docs/config-file/config-reference) distingue controles de Browser Use, Computer Use y el comando de voz de la CLI de los controles de la aplicación. No se instalan requisitos gestionados ni se generaliza el alcance de `realtime_conversation` a ChatGPT Voice en otras superficies. Las herramientas locales de lectura, edición y comandos conservan su comprobación de permisos separada.

## 8. Confirmación humana de los controles explícitos de canales

El colaborador aporta nuevo `/debug-config` y `/mcp` de CLI 0.163.0, con workspace normalizado `/Tests/HPA-EVAL-05/agente`. Las cinco capas vuelven a figurar habilitadas: defaults empaquetados, sistema, usuario, proyecto y flags de sesión. Se omiten sus rutas personales. El extracto de sesión aportado es:

```text
agents.enabled = false
features.apps = false
features.browser_use = false
features.browser_use_external = false
features.computer_use = false
features.hooks = false
features.image_generation = false
features.realtime_conversation = false
features.remote_plugin = false
features.skill_mcp_dependency_install = false
features.worktrees = false
mcp_servers.node_repl.enabled = false
model_reasoning_effort = "medium"
web_search = "disabled"
windows.sandbox = "mxc"

Requirements: <none>
[agents]: enabled = false
```

El inventario MCP sigue mostrando únicamente:

```text
node_repl: disabled (0 tools)
```

Cotejo de los canales identificados con las fuentes del cliente:

| Canal o mecanismo | Evidencia declarada |
| --- | --- |
| MCP | Ninguno conectado en el listado; `node_repl` deshabilitado con cero herramientas. Los otros nombres históricos no aparecen. |
| Apps y conectores | `features.apps=false`. |
| Navegador dirigido por el agente y navegador externo | `features.browser_use=false` y `features.browser_use_external=false`. |
| Computer Use | `features.computer_use=false`. |
| Generación de imágenes y voz de la CLI | `features.image_generation=false` y `features.realtime_conversation=false`. |
| Hooks | `features.hooks=false`. |
| Catálogo remoto e instalación de dependencias MCP de skills | `features.remote_plugin=false` y `features.skill_mcp_dependency_install=false`. |
| Gestión de worktrees | `features.worktrees=false` y ausencia de `codex_worktrees` en `/mcp`. |
| Búsqueda web | `web_search="disabled"`. |
| Subagentes | `agents.enabled=false`, tanto en flags como en la sección de agentes. |

El cliente acepta la combinación y expone los diez controles de features desactivados, además de búsqueda, subagentes y `node_repl`. Se confirma la configuración declarada de canales y la compatibilidad de este arranque de CLI 0.163.0. No se ha aportado un nuevo `/status` en esta salida ni un nuevo hash; el último hash comunicado sigue siendo el de la reparación de la sección 4.

Límites conservados: `/mcp` no enumera todo mecanismo nativo y el diagnóstico no muestra por separado el estado de los cinco plugins desactivados en el archivo. No se invocan canales para probarlos, se mide la red ni se verifica el acceso a archivos o al evaluador. Este resultado no certifica aislamiento, cobertura técnica exhaustiva, trazas completas ni ejecución de P01–P13. Permite entregar la inspección y compatibilidad declaradas con esos límites para revisión humana, sin exigir completar el laboratorio dentro de esta tarea.
