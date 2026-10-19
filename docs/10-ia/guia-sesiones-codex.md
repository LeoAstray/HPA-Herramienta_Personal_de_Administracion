# Guía manual para crear y usar sesiones de Codex en HPA

## Finalidad y límites

Guía de uso para los dos colaboradores en Windows, preparada el 2026-10-16 con OpenAI Docs y los [contratos de desarrollo](agentes-desarrollo.md). Explica cómo abrir, inspeccionar, usar y continuar chats. El [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05) mantiene el avance y los pendientes de configuración.

HPA sigue en definición y diseño. Abrir una sesión no autoriza implementar producto, elegir arquitectura, operar Git en escritura o publicar. La configuración ejecutable por rol sigue sujeta a la evaluación; estas instrucciones no acreditan permisos efectivos.

## Qué significa cada elemento

| Elemento | Uso |
| --- | --- |
| Terminal PowerShell | Donde se ejecutan comandos como `codex --version` y los bloques de preparación humana. |
| CLI de Codex | Interfaz que aparece después del arranque; recibe la petición y comandos como `/status`. |
| Chat o sesión | Conversación con su historial. Conviene dedicar cada chat a un resultado concreto. |
| Carpeta de trabajo | Archivos que contextualizan la tarea. Elegir una carpeta no impone por sí solo una frontera de seguridad. |
| Rol | Contrato de responsabilidad, como Developer o Reviewer. Es distinto del modelo y de los permisos técnicos. |
| Modelo y esfuerzo | Selección manual antes del encargo conforme a ADR-004. |
| Perfil de permisos | Reglas técnicas que el cliente debe aplicar. `--profile` selecciona una capa de configuración; no equivale al nombre de un perfil de permisos. |

Las [fuentes de proyecto y chats](https://learn.chatgpt.com/docs/projects) explican la relación entre carpeta, historial y archivos actuales. El historial de una conversación no congela los archivos del repositorio.

## 1. Elegir la carpeta y la tarea

Para mantener documentación de HPA, usar su proyecto/carpeta. Para evaluar permisos, usar exclusivamente `/Tests/HPA-EVAL-05/agente` y la [guía específica del laboratorio](preparacion-raiz-perfiles-eval-05.md#5-retirar-canales-en-la-sesión-exclusiva-del-laboratorio). No usar el arranque genérico de esta guía como sustituto del procedimiento del laboratorio.

Desde la raíz de HPA, estas consultas humanas permiten comprobar el checkout sin cambiar Git:

```powershell
git --no-optional-locks branch --show-current
git --no-optional-locks status --short --branch
git --no-optional-locks rev-parse HEAD
```

La persona prepara y actualiza su rama según el flujo del equipo. Comparar referencias locales no demuestra que se haya consultado el remoto. Antes de asignar edición, identificar qué cambios previos pertenecen a otra tarea y conservarlos.

Definir resultado, rol, fuentes, archivos editables, comprobaciones permitidas y aceptación. Los roles y la selección provisional de modelos están en [agentes de desarrollo](agentes-desarrollo.md) y [ADR-004](../13-adrs/ADR-004-contratos-agentes-desarrollo.md); no se elige automáticamente otro modelo si falta el previsto.

## 2. Abrir una sesión nueva

En la aplicación, seleccionar el proyecto HPA y abrir un chat nuevo en la carpeta local que haya preparado la persona. Verificar el proyecto, entorno y carpeta visibles antes de enviar el encargo. La aplicación y una CLI independiente pueden mostrar versiones, herramientas o capas diferentes: registrar el cliente realmente usado.

En PowerShell, comprobar primero la CLI instalada:

```powershell
Get-Command codex -ErrorAction Stop
codex --version
codex --help
```

Si no está disponible, seguir la [comprobación de instalación](preparacion-raiz-perfiles-eval-05.md#4-comprobar-el-entorno-antes-de-entregar-un-caso). El ejecutable interno de la aplicación no garantiza disponibilidad en la terminal humana.

Ejemplo de **arranque de inspección desde la raíz de HPA**, con el modelo habitual de Developer aprobado. No contiene un encargo ni instala un perfil de permisos de HPA:

```powershell
codex --strict-config --no-daemon --cd . `
    --model gpt-6.1-sol `
    -c model_reasoning_effort=medium `
    -c agents.enabled=false
```

Las [opciones oficiales de CLI](https://learn.chatgpt.com/docs/cli/reference) documentan carpeta, overrides, comprobación de campos desconocidos y uso sin servidor compartido. Los permisos y canales heredados deben inspeccionarse antes de entregar trabajo; el comando no impone el aislamiento del laboratorio.

## 3. Inspeccionar antes de enviar el encargo

Dentro de la CLI, introducir cada comando por separado:

```text
/status
/debug-config
/mcp
```

Comprobar cliente/versión, carpeta, modelo/esfuerzo, instrucciones de proyecto, perfil/aprobaciones y canales. `/debug-config` ayuda a identificar capas y requisitos; `/mcp` identifica servidores MCP, sin cubrir por sí solo todos los mecanismos del cliente. Véanse [Developer commands](https://learn.chatgpt.com/docs/developer-commands) y [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic).

Si falta un permiso o el entorno no coincide, resolverlo antes de trabajar. Conservar los diagnósticos completos privadamente y compartir solo el extracto técnico necesario, sin cuentas, cuotas, identificadores de sesión, rutas personales, credenciales ni argumentos privados. No pedir al agente que certifique por su respuesta que está aislado.

## 4. Entregar y seguir una tarea

Una petición breve puede usar estos campos, completados por la persona:

```text
Objetivo: [resultado concreto].
Rol: [contrato de desarrollo aplicable].
Fuentes: AGENTS.md, orden obligatorio de docs y documentos afectados.
Archivos editables: [lista].
Comprobaciones permitidas: [lista o solo lectura].
Aceptación: [resultado verificable].
Límites: conservar cambios ajenos; Git y publicaciones manuales;
sin implementación de producto ni decisiones técnicas no autorizadas.
Salida: cambios, comprobaciones, evidencia y limitaciones.
```

Esta plantilla es para tareas ordinarias de HPA; no es el encargo ejecutable de EVAL-05. Durante el laboratorio no se entrega trabajo hasta completar sus condiciones específicas.

Revisar los avances y las operaciones propuestas. Si cambia materialmente el objetivo, aclarar el alcance. Un Developer puede hacer las comprobaciones breves asignadas; Reviewer y Tester informan bajo sus propios contratos. Una revisión independiente debe identificar un estado estable y no proceder del autor del cambio. Trabajar secuencialmente por defecto; no lanzar roles adicionales solo por tenerlos documentados.

Al recibir la entrega, revisar el diff y las comprobaciones. La persona gestiona staging, commits, push, PR, merge, Asana y publicación de issues. Los borradores locales de issues se retiran tras la confirmación de publicación, actualizando referencias, CHG y roadmap; las guías y evidencias se conservan.

## 5. Salir, continuar o empezar otro chat

| Acción | En la CLI |
| --- | --- |
| Salir | `/quit` |
| Abrir otro chat dentro de la misma CLI | `/new`; mantener la carpeta actual y evitar crear un worktree sin petición específica. |
| Elegir una conversación guardada desde PowerShell | `codex resume` |

Estos comandos están en [Developer commands](https://learn.chatgpt.com/docs/developer-commands). Después de cambiar configuración, backend, rol o canales, cerrar con `/quit` y usar el arranque revisado en un proceso nuevo; `/new` no sustituye esa recarga. Para EVAL-05 se usa el arranque nuevo de su guía, sin reanudar una sesión anterior.

Al continuar una conversación ordinaria, comprobar otra vez carpeta, rama, cambios y configuración: sus archivos pueden haber cambiado desde el último turno. El encargo no debe depender solo de información guardada en un chat; mantener las instrucciones y decisiones en Markdown.

## Problemas frecuentes

| Síntoma | Acción |
| --- | --- |
| PowerShell muestra `>>` | Está esperando que termine el bloque o una expresión. Copiar únicamente el código, sin los indicadores `PS` o `>>`. |
| Se muestra un SHA-256 | Es la huella del archivo indicado; conservarla como evidencia de contenido, separada de la carga efectiva. |
| `invalid transport` en `[mcp_servers.node_repl]` | Aplicar la [corrección de la guía](preparacion-raiz-perfiles-eval-05.md#corregir-el-fragmento-anterior-tras-invalid-transport); no inventar un transporte ni copiar argumentos privados. |
| El arranque devuelve un error de configuración | Conservar versión y error depurado, corregir antes del siguiente paso y no ampliar permisos para conseguir un arranque. |
| `/mcp` conserva un servidor conectado | Registrar nombre/estado y resolver su procedencia; no afirmar retirada por haber modificado el archivo. |
