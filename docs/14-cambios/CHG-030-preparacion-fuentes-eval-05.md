# CHG-030 — Preparación manual de fuentes de EVAL-05

## Fuente y alcance

Registrado el 2026-10-15. El colaborador comunica que ha creado la estructura, los archivos sintéticos y la configuración del laboratorio. La lectura local confirma la presencia de `agente/AGENTS.md`, tres archivos de muestra y `agente/.codex/config.toml`. El hash de configuración coincide con la plantilla. No se inspecciona el contenido privado del evaluador ni se ejecutan agentes o sondas.

Se prepara el siguiente paso manual del laboratorio `/Tests/HPA-EVAL-05`. El [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05) conserva el avance, los pendientes y la continuación. La copia de configuración no acredita su carga por el cliente.

## Cambio

- [Script de preparación](../10-ia/plantillas/preparar-fuentes-eval-05.ps1) ejecutado por la persona: selección cerrada de trece fuentes, extractos identificados, conservación de rutas y manifiesto bajo `evaluador`.
- Exclusión del seguimiento y resultados de evaluación mediante selección de secciones; rechazo adicional de referencias explícitas a casos en el texto seleccionado. Los enlaces locales a fuentes no incluidas se sustituyen por texto y se registran.
- Manifiesto con fecha UTC, origen local, revisión base, hash del generador, hashes de originales y copias y adaptaciones. Los hashes identifican la copia de trabajo aunque esté modificada; la revisión base no se presenta como identidad exacta del contenido.
- Comprobación previa de destinos vacíos, rechazo de puntos de reanálisis en las rutas de destino y creación sin sobrescritura. No hay borrado ni recuperación automática ante errores parciales.
- [Guía manual](../10-ia/preparacion-raiz-perfiles-eval-05.md) y roadmap actualizados. Los hashes de CHG-029 conservan su valor histórico para la guía anterior; no se modifica la ficha R2, el encargo R2 ni la plantilla TOML.

La selección es un procedimiento para el caso documental, no una nueva decisión del producto ni una revisión humana adicional atribuida al colaborador. Su lectura y revisión forman parte de la preparación manual antes de entregar el encargo. El script no sustituye la verificación del aislamiento ni el registro de G2–G6. No prepara Git, configura permisos, consulta el remoto ni inicia evaluaciones.

## Verificación al preparar el script

Comprobaciones en PowerShell 7.6.5, sobre una raíz temporal separada del laboratorio humano:

- Parser del script: sin errores. El archivo del script contiene solo ASCII; las fuentes se procesan como UTF-8.
- Ejecución del generador: trece fuentes y un manifiesto. Los veintiséis hashes de originales y copias coinciden con sus archivos; los diez enlaces locales conservados tienen destino. Las copias no contienen las referencias explícitas a casos/resultados excluidas por el generador.
- Segunda ejecución: rechazada antes de escribir; inventario y hashes sin cambios. Una raíz de nombre incorrecto también se rechaza.
- Formato de los cuatro archivos de este paso: salto final, espacios finales, marcadores de conflicto y rutas personales compartidas sin incidencias. Treinta y cuatro enlaces locales y nueve anclas resueltos. `git --no-optional-locks diff --check` sin incidencias.

Límites de verificación: la creación de una junction temporal para probar ese rechazo fue denegada por el entorno de esta sesión, antes de ejecutar el generador sobre ella; esa rama de protección no queda comprobada mediante ejecución. El intento adicional con `powershell.exe -File` fue bloqueado por AuthorizationManager; la ejecución con Windows PowerShell queda sin verificar. No se cambian políticas ni se equiparan esos fallos a controles del laboratorio. Una comprobación adicional no pudo reutilizar el temporal de otra invocación por restricciones de acceso; no altera el resultado de la prueba completa realizada en una sola invocación.

Durante la preparación del script no se generan las fuentes ni el manifiesto del laboratorio humano: se proporciona el procedimiento para su ejecución manual posterior. En ese momento no se han verificado controles efectivos ni se han ejecutado casos de EVAL-05.

## Confirmaciones posteriores de preparación manual — 2026-10-15

Tras preparar el script, el colaborador comunica su ejecución satisfactoria. Se leen los metadatos del manifiesto y se cotejan las trece copias bajo `agente/docs` con sus SHA-256 registrados: sin diferencias. La configuración sigue coincidiendo con la plantilla. Este cotejo no equivale a una revisión humana del contenido ni acredita exclusión técnica del evaluador.

El colaborador aporta después la salida de creación del Git sintético: commit raíz `eae3022`, mensaje `Base sintetica de EVAL-05`, dos archivos y ocho inserciones. Las consultas finales de remotos y estado no producen salida. Los avisos LF/CRLF se registran como avisos de conversión de saltos de línea; el commit finaliza. La consulta Git de contraste desde esta sesión recibe `Permission denied`: se conserva la salida humana como fuente, sin atribuir una comprobación independiente ni una sonda de EVAL-05.

Se incorpora a la guía un arranque manual de CLI para inspección, sin prompt, con `--strict-config`, `--no-daemon` y workspace `agente`, seguido de `/status` y `/debug-config`. La ayuda local confirma las opciones y la versión `0.162.0-alpha.17.2`; siguen apareciendo avisos de acceso a temporales del cliente. OpenAI Docs y las páginas oficiales de [configuración](https://learn.chatgpt.com/docs/developer-settings), [permisos](https://learn.chatgpt.com/docs/permissions) y [CLI](https://learn.chatgpt.com/docs/cli/reference) sustentan el procedimiento y el límite de que la configuración heredada puede prevalecer sobre los perfiles. No se cambia la configuración personal ni se inicia la sesión del laboratorio desde este chat.

El roadmap se actualiza con estas evidencias y la continuación. La inspección del cliente y la verificación efectiva de G2–G6 conservan su condición de pendientes.

Comprobación documental de esta actualización: tres archivos, treinta y cuatro enlaces locales y nueve anclas sin incidencias; tres bloques PowerShell analizados sin errores y sin ejecutarlos. Formato, ausencia de rutas personales compartidas y `git --no-optional-locks diff --check` correctos. La ayuda de la CLI se consulta sin iniciar una sesión de evaluación.

## Incidencia de disponibilidad de CLI — 2026-10-15

El colaborador aporta `CommandNotFoundException` para `codex --version` y para el arranque de inspección: PowerShell no localiza el comando. Se confirma que la sesión del agente resuelve una CLI en una ruta interna versionada de la aplicación. La versión y ayuda observadas allí no acreditaban su disponibilidad en la terminal humana; la indicación anterior había omitido esa comprobación previa.

Se añade a la guía la verificación mediante `Get-Command`, el instalador independiente para Windows documentado en [variables de entorno de OpenAI](https://learn.chatgpt.com/docs/config-file/environment-variables), la comprobación en una terminal nueva y la identificación de la versión realmente utilizada. El roadmap recoge la incidencia y la continuación. No se instala software, modifica el `PATH`, cambia la política de PowerShell ni ejecuta el instalador desde esta sesión. La instalación queda a cargo del colaborador mediante el procedimiento manual.

La consulta del instalador se limita a la documentación oficial; el comando de instalación de la guía se valida como texto, sin descargarlo ni ejecutarlo. No se altera el contenido del laboratorio ni se consideran esos errores una prueba de sus permisos.

Verificación de esta corrección: tres documentos, treinta y cuatro enlaces locales, nueve anclas y cuatro bloques PowerShell sin incidencias de resolución o sintaxis. Formato y `git --no-optional-locks diff --check` correctos; los bloques no se ejecutan.

## Error del instalador — 2026-10-15

El colaborador comunica `PropertyNotFoundStrict`: el instalador no encuentra la propiedad `OSArchitecture`. No se dispone de traza con línea ni versión de esa terminal y no se afirma una causa concreta o una instalación completada.

Se consulta únicamente `RuntimeInformation.OSArchitecture`, sin ejecutar el instalador, desde PowerShell 7.6.5 y Windows PowerShell 5.1.26100.9711 en el entorno del agente: ambos devuelven X64. Esto limita la hipótesis de incompatibilidad general de Windows PowerShell; no reproduce el fallo ni acredita la arquitectura detectada por el instalador en la sesión humana.

La guía añade consultas de traza, versión y disponibilidad de PowerShell/Node.js/npm. La vía npm se contrasta con la documentación oficial de OpenAI enlazada allí; no se presupone Node.js disponible ni se instala. Roadmap actualizado. No se altera el instalador ni se ejecutan casos o cambios sobre el laboratorio.

Verificación documental: tres documentos, treinta y cuatro enlaces locales resueltos y cinco bloques PowerShell analizados sin errores, sin ejecutar los bloques. Formato y `git --no-optional-locks diff --check` sin incidencias.

## Alternativa mediante npm — 2026-10-15

El colaborador aporta Windows PowerShell Desktop `5.1.26100.9711`, rutas resolubles de `node.exe` y `npm.cmd`, y ausencia de entrada para `pwsh.exe` en esa consulta. La lectura directa de `ScriptStackTrace` produce otro `PropertyNotFoundStrict`; no se obtiene la traza ni se atribuye una causa nueva al instalador. La guía sustituye esa lectura por presentación selectiva de propiedades, que admite propiedades ausentes.

Se consultan solo las versiones de Node.js y npm en las rutas aportadas: `v24.21.0` y `12.2.0`. Se contrasta de nuevo la instalación oficial mediante npm. Se prepara un bloque manual que instala `@openai/codex@latest`, detiene la secuencia si falla y comprueba `codex.cmd` por la ruta devuelta por `npm.cmd prefix --global`. No requiere suponer que el lanzador ya está en el `PATH` de la terminal.

Guía y roadmap actualizados. No se ejecuta la instalación ni se cambia la política de PowerShell, la configuración global de npm o el laboratorio desde esta sesión. La versión de CLI y los controles efectivos siguen sin verificarse.

Verificación documental: tres documentos, treinta y cuatro enlaces locales y seis bloques PowerShell sin incidencias de formato, resolución o sintaxis; bloques sin ejecutar. La presentación selectiva de propiedades se comprueba con un objeto sin traza bajo modo estricto, sin error. `git --no-optional-locks diff --check` correcto.

## Confirmación de instalación de CLI — 2026-10-15

El colaborador ejecuta el bloque npm y aporta `added 2 packages in 47s` y `codex-cli 0.162.1`. Se contrasta mediante el lanzador npm: la versión coincide y su ayuda reconoce `--strict-config`, `--no-daemon` y `--cd`. La consulta de ayuda sigue mostrando avisos de acceso a temporales del cliente desde el entorno del agente; no se ejecuta una sesión del laboratorio ni se equiparan esos avisos a resultados de sus controles.

El roadmap registra la instalación y la continuación con inspección de configuración. La guía aclara que la ruta directa de npm permite usar el lanzador desde la misma terminal; una ventana nueva se necesita para recoger cambios de `PATH` cuando se utilice el nombre del comando. Los archivos del laboratorio, la configuración personal y los permisos no se modifican desde esta sesión. La instalación no acredita la carga del perfil ni completa G2–G6.

Comprobación de esta actualización: formato y treinta y cuatro enlaces locales de tres documentos sin incidencias; `git --no-optional-locks diff --check` correcto. Sintaxis del arranque por ruta npm analizada sin ejecutarlo; opciones contrastadas con la ayuda de la CLI 0.162.1 instalada.
