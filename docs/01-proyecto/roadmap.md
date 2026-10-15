# Roadmap documental

## Actual

- Línea base funcional y de alcance inicial disponible.
- ADR-001 y ADR-002 aprobadas.
- Modelo conceptual de Core aprobado por ADR-005; tecnología y autorización concreta pendientes.
- Estudio global de módulos completo; los módulos 0 a 15 cuentan con documentación de análisis Fase 1.
- Contratos de agentes de desarrollo y prioridades del equipo definidos (ADR-004); R2 de DEV-00 y EVAL-01 satisfactorios; EVAL-02 validado técnicamente por EVAL-03. EVAL-04 registrado: Reviewer satisfactorio y Tester satisfactorio en detección tras una repetición, con incidencia de protocolo inicial y observaciones conservadas. Piloto global y configuración ejecutable pendientes.
- El 2026-10-07 queda preparado el [diseño EVAL-05 de evaluación de permisos](../10-ia/diseno-evaluacion-permisos-agentes.md), asociado al [issue #36](https://github.com/LeoAstray/HPA-Herramienta_Personal_de_Administracion/issues/36). Incluye matriz por rol, casos positivos/negativos, entorno sintético, evidencia, encargo y plantilla de resultados. Sin laboratorio creado ni evaluación ejecutada. [CHG-021](../14-cambios/CHG-021-diseno-evaluacion-permisos-y-roadmap.md) registra el avance y la regla de actualizar este roadmap en cada cambio.
- Comprobaciones locales del cambio documental completadas: diff sin incidencias y 63 enlaces relativos resueltos. No sustituyen la revisión independiente del diseño ni la futura evaluación de controles.
- Comprobaciones de preparación CHG-022 completadas: formato sin incidencias y 89 enlaces relativos resueltos en el conjunto de cambios locales.
- La propuesta del bloque 1 está documentada en [CHG-025](../14-cambios/CHG-025-propuesta-identidad-permisos.md). Su revisión y continuación se mantienen en el [seguimiento de identidad, permisos y sesiones](#seguimiento-de-identidad-permisos-y-sesiones).

Corrección documental del 2026-10-07: la propuesta de Core se ha recolocado directamente en `docs/03-arquitectura/` y se ha eliminado la carpeta anidada vacía. Las referencias de ADR-005 y CHG-020 resuelven ahora a la ruta prevista; véase [CHG-023](../14-cambios/CHG-023-correccion-carpeta-arquitectura.md).

El 2026-10-09 se centraliza el seguimiento de EVAL-05 en este roadmap y se sustituyen sus copias operativas por enlaces. Las instrucciones de mantenimiento recogen esta regla; los registros históricos conservan su contenido. Véase [CHG-024](../14-cambios/CHG-024-centralizacion-seguimiento-roadmap.md).

## Seguimiento de identidad, permisos y sesiones

**Avance:** el 2026-10-11 se redacta la [propuesta del bloque 1](../03-arquitectura/propuesta-identidad-permisos.md), registrada en CHG-025. El 2026-10-13 el colaborador confirma que ambos han revisado la propuesta y comunica que cerrará manualmente el issue #42. Se registra esa revisión humana en [CHG-026](../14-cambios/CHG-026-revision-humana-identidad-permisos.md). La redacción y la revisión previstas por el issue están realizadas; el cierre en GitHub no se ha comprobado.

**Pendientes:** no se ha comunicado el acuerdo sobre las cinco decisiones de la propuesta ni se ha formalizado ADR-006. El bloque 1 sigue abierto como decisión y los permisos de los módulos afectados conservan su carácter provisional.

**Siguiente paso:** el colaborador cierra #42 como entrega documental revisada. En un issue posterior, concretar el acuerdo de ambos sobre las decisiones; si se acuerdan, formalizar ADR-006 y actualizar Identidad y Seguridad, los módulos afectados y el inventario de decisiones transversales.

## Seguimiento de EVAL-05

**Avance:** el 2026-10-07 el colaborador comunica conformidad con el diseño inicial entregado con CHG-021 y confirma que él realiza la revisión; no se requiere un Reviewer agente para esa revisión documental. Se prepara la [ficha del entorno](../10-ia/entorno-eval-05.md) y la [guía de revisión humana](../10-ia/revision-eval-05-colaborador.md), registradas en [CHG-022](../14-cambios/CHG-022-preparacion-revision-y-entorno-eval-05.md). La ficha recoge el inventario de aquella sesión, explica por qué no acredita el aislamiento y propone rutas, perfiles y puertas de entrada.

**Avance del 2026-10-14:** se prepara la ficha `EVAL-05-ENTORNO-R1`, con inventario histórico identificado y requisitos de datos para G2–G6. La guía R1 delimita la revisión humana y su registro. El [encargo documental EVAL-05-DEV02-R1](../10-ia/encargo-eval-05-developer.md) identifica el primer Developer, los casos candidatos, los campos por completar y la plantilla futura, sin autorizar ejecución. [CHG-028](../14-cambios/CHG-028-preparacion-documental-encargo-eval-05.md) identifica la entrega, los hashes de revisión y las comprobaciones documentales locales sin incidencias.

**Avance del 2026-10-15:** el colaborador de este chat comunica conformidad con toda la ficha R1 de `5501a2a`, con la observación de cambiar la raíz. Confirma una carpeta `Tests` hermana de HPA y solicita usar únicamente `/Tests/HPA-EVAL-05` en los documentos. Se aplica la corrección como ficha `EVAL-05-ENTORNO-R2` y encargo `EVAL-05-DEV02-R2`, con guía humana R2. [CHG-029](../14-cambios/CHG-029-revision-ficha-y-ruta-eval-05.md) conserva fuente, alcance, observación, hashes y comprobaciones documentales sin incidencias. Se prepara la [guía de raíz y perfiles](../10-ia/preparacion-raiz-perfiles-eval-05.md) y una plantilla de permisos sin ruta personal completa, con sintaxis TOML y PowerShell comprobada sin aplicarlas. La revisión humana y su corrección autorizada quedan registradas; no se exige repetir la conformidad por ese cambio.

**Preparación manual del 2026-10-15:** el colaborador comunica la creación de la estructura y del contenido sintético y la copia de configuración. Se observa la presencia de `agente/AGENTS.md`, los tres archivos de muestra y `agente/.codex/config.toml`; el SHA-256 de este último coincide con la plantilla de perfiles. Esto acredita presencia y copia, no carga efectiva ni aislamiento. Se prepara un script manual para generar trece copias rectoras seleccionadas y el manifiesto privado, con extractos que excluyen resultados y enlaces a documentos no incluidos. Véase [CHG-030](../14-cambios/CHG-030-preparacion-fuentes-eval-05.md).

**Confirmación posterior del 2026-10-15:** el colaborador ejecuta el generador y se contrastan las trece copias con sus hashes del manifiesto, sin diferencias. Después aporta la salida de creación manual del repositorio sintético: commit inicial `eae3022`, dos archivos y consultas finales de remotos/estado sin salida. Los avisos LF/CRLF no impiden el commit. Esta evidencia Git procede de la terminal del colaborador; el intento de contraste desde la sesión de HPA recibe acceso denegado y no se cuenta como sonda del laboratorio. Se concreta en la guía la inspección manual de configuración con una CLI separada, sin entregar todavía el encargo Developer.

**Disponibilidad de CLI del 2026-10-15:** la terminal humana devuelve `CommandNotFoundException` tanto para la versión como para el arranque de `codex`. La CLI observada en la sesión del agente procede de una ruta interna versionada de la aplicación; su disponibilidad no se transfiere al PowerShell del colaborador. Se añade a la guía la comprobación previa y una vía oficial de instalación manual de la CLI independiente. No se instala desde este chat ni se inicia el laboratorio.

**Incidencia del instalador del 2026-10-15:** el colaborador ejecuta el instalador oficial y aporta `PropertyNotFoundStrict` para `OSArchitecture`. La causa concreta no está identificada y no se dispone de una instalación terminada ni de versión de CLI humana. Una consulta aislada a `RuntimeInformation.OSArchitecture` sí responde en PowerShell 7.6.5 y Windows PowerShell 5.1.26100.9711 desde la sesión del agente; esto no reproduce el instalador ni diagnostica la terminal humana. Se prepara la recogida de traza, versión y disponibilidad de PowerShell/Node.js/npm antes de elegir la vía compatible.

**Datos de la terminal humana del 2026-10-15:** el colaborador confirma Windows PowerShell Desktop `5.1.26100.9711` y resolución de `node.exe` y `npm.cmd`; la consulta de `pwsh.exe` no devuelve entrada y la propiedad `ScriptStackTrace` tampoco está disponible en el objeto consultado. Se corrige esa consulta en la guía. Las comprobaciones de versión sobre las rutas de Node.js/npm indicadas devuelven `v24.21.0` y `12.2.0` desde la sesión del agente. Se prepara la alternativa oficial de instalación mediante npm y comprobación del lanzador `.cmd` por la ruta que devuelve npm. No se ha ejecutado esa instalación ni se conoce todavía la versión de CLI humana.

**Instalación de CLI del 2026-10-15:** el colaborador ejecuta la instalación mediante npm y aporta `added 2 packages` y `codex-cli 0.162.1`. Se contrasta esa versión mediante el lanzador npm y se consulta su ayuda: reconoce `--strict-config`, `--no-daemon` y `--cd`. La CLI independiente está disponible por su ruta de instalación. No se ha abierto todavía la sesión del laboratorio ni inspeccionado su perfil efectivo.

**Incompatibilidad de backend del 2026-10-15:** el arranque humano falla al cargar `AGENTS.md` porque `elevated` exige lectura efectiva de `:root`, denegada por el perfil. `/status` queda como borrador no enviado; no hay inspección completada ni caso ejecutado. Se corrige el procedimiento de arranque con selección explícita y temporal `windows.sandbox=mxc`, conservando las reglas de permisos. [CHG-031](../14-cambios/CHG-031-compatibilidad-backend-windows-eval-05.md) registra el fallo, la fuente oficial y el alcance de la corrección. La compatibilidad y el arranque efectivos con MXC siguen por comprobar.

**Inspección inicial del 2026-10-15:** las salidas humanas de `/status` y `/debug-config` confirman el arranque de CLI 0.162.1 con workspace `agente`, lectura de `AGENTS.md`, perfil declarado `eval05-developer` y aprobación `never`. La capa de proyecto está habilitada; la capa de sesión declara `windows.sandbox = "mxc"` y no se declaran requisitos gestionados. El cliente muestra GPT-6.1 Sol con esfuerzo `xhigh` y `agents.enabled = true`: faltan el esfuerzo Medium previsto por ADR-004 y la exclusión de herramientas de subagentes. Se prepara un nuevo arranque con esas opciones explícitas, conservando MXC y el perfil. El inventario de MCP y demás canales y las comprobaciones técnicas permanecen pendientes; el arranque no demuestra por sí solo aislamiento.

**Confirmación de configuración del 2026-10-15:** el colaborador aporta nuevas salidas de `/status`, `/debug-config` y `/mcp`. El cliente declara CLI `0.163.0`, GPT-6.1 Sol / Medium, workspace `agente`, `AGENTS.md`, perfil `eval05-developer` con aprobación `never`, capa de proyecto habilitada y opciones de sesión `windows.sandbox = "mxc"`, `model_reasoning_effort = "medium"` y `agents.enabled = false`; no declara requisitos gestionados. El inventario MCP muestra `code-review` y `codex_app` deshabilitados, pero `codex_apps` (177 herramientas), `codex_worktrees` (3), `cua_repl` (3) y `node_repl` (4) conectados. Quedan confirmados los valores declarados de modelo/esfuerzo y subagentes; la exclusión de canales no está completa. [CHG-031](../14-cambios/CHG-031-compatibilidad-backend-windows-eval-05.md) conserva esta evidencia sin datos de cuenta, rutas personales, identificadores de sesión ni cuotas. No se han ejecutado casos ni comprobado controles efectivos.

**Alcance de cierre documental:** los tres criterios del issue de continuación vinculado a #36 quedan cubiertos por la revisión humana identificada en CHG-029, la corrección de ruta autorizada, los requisitos de G2–G6 y el encargo futuro documentados, y este seguimiento centralizado. La preparación práctica posterior se registra como avance adicional; completar el laboratorio y ejecutar EVAL-05 no son condiciones añadidas al cierre de ese issue. Las comprobaciones locales de la entrega se registran en CHG-031.

**Verificación documental del 2026-10-16:** doce archivos locales, incluidos los nuevos; ochenta enlaces locales y veinte anclas resueltos, seis bloques PowerShell y el generador analizados sin errores de sintaxis, TOML válido y formato sin incidencias. Los hashes de ficha R2, encargo R2, guía de revisión R2 y plantilla coinciden con CHG-029. Estas comprobaciones verifican la entrega documental, no los controles del laboratorio.

**Pendientes del issue documental:** revisión final de los cambios locales por el colaborador, commit, push e integración según el flujo del proyecto y cierre manual del issue. No se ha comprobado su estado remoto ni se ha realizado ninguna de esas operaciones desde este chat.

**Pendientes del laboratorio para el trabajo posterior:** responsabilidad registrada, comprobación de propietario y enlaces de la raíz, revisión humana de la selección de fuentes/manifiesto, retirada y comprobación de los cuatro MCP conectados y del resto de canales, comprobación técnica de permisos y exclusión del evaluador, fuente/cobertura/custodia de trazas y encargo ejecutable con casos seleccionados. La carga declarada del perfil está observada; sus controles efectivos no se han verificado. No se han ejecutado casos P01–P13. El intento previo de ayuda con `codex sandbox windows --help` falló durante el arranque y no aporta evidencia de controles del laboratorio.

**Siguiente paso inmediato:** revisar y publicar manualmente la entrega documental mediante commit y push; integrar y cerrar el issue según el flujo del proyecto. Después, continuar la configuración del laboratorio en una tarea posterior, empezando por resolver la disponibilidad de los MCP y demás canales en la sesión separada. Antes de los casos deben completarse y verificarse G2–G6. El cierre documental no cierra EVAL-05 ni autoriza sondas; no usar esta sesión de HPA como laboratorio.

## Seguimiento del workflow de asignación de issues

**Avance:** el 2026-10-13 se documenta el workflow existente [Auto-assign issue creator](../../.github/workflows/auto-assign.yml), cuya configuración local solicita añadir al autor como responsable al abrirse un issue. Su procedimiento y límites se incorporan al [proceso de cambio](../00-gobierno/proceso-de-cambio.md#automatización-de-asignación-de-issues), con registro en [CHG-027](../14-cambios/CHG-027-documentacion-workflow-asignacion-issues.md). Se inspecciona la configuración local; no se ejecuta ni modifica el workflow.

**Pendientes:** no se dispone en este trabajo de evidencia de una ejecución real ni de la asignación resultante. La presencia de la versión vigente en la rama por defecto y los permisos efectivos del remoto no se han comprobado.

**Siguiente paso:** el colaborador aporta una referencia a una ejecución real en Actions y al issue con su autor asignado, comprobando que la versión vigente está en la rama por defecto. Registrar el resultado y las incidencias, si las hay, en este seguimiento.

## Próximo

1. Ejecutar el descubrimiento y diseño de IA/Agentes: casos de uso, inventario de agentes, criterios de evaluación de modelos y límites de seguridad y privacidad (ADR-003).
   Para desarrollo, consultar el [seguimiento de EVAL-05](#seguimiento-de-eval-05). EVAL-04 no garantiza evaluación ciega ni cierra el piloto. Consumo atribuible, utilidad de DEV-00 frente a una plantilla y el estado histórico de su prompt siguen pendientes. Developer conserva Sol 6.1 / Medium por defecto y Luna / Medium para tareas sencillas; los candidatos de los demás roles no cambian.
2. Resolver las decisiones de dominio que condicionan los agentes internos del producto: el contrato de Core ya está aprobado (ADR-005); para identidad, permisos y sesiones, consultar el [seguimiento del bloque 1](#seguimiento-de-identidad-permisos-y-sesiones). La preparación de agentes de desarrollo tiene sus propios contratos y puede avanzar antes.
3. Diseñar la arquitectura global y el modelo de dominio, incorporando los límites aprobados para IA/Agentes.
4. Convertir el alcance aprobado en requisitos con identificadores.
5. Elegir el diseño técnico e iterar hacia implementación, incluidos únicamente los agentes cuya necesidad, modelo y controles hayan sido aprobados.

## Futuro, no MVP

Móvil, Siri/voz, agentes IA funcionales, integraciones complejas, automatizaciones avanzadas y multiusuario. El descubrimiento de IA/Agentes está priorizado, pero no autoriza todavía una funcionalidad de IA en el MVP.

## Mantenimiento obligatorio

Cada cambio actualiza este documento con avance, pendientes y siguiente paso, aunque no cambie el orden de los hitos. Véase el [proceso de cambio](../00-gobierno/proceso-de-cambio.md). El issue organiza la tarea; Markdown conserva el estado operativo. La asignación inicial de responsables dispone de la [automatización acotada documentada](../00-gobierno/proceso-de-cambio.md#automatización-de-asignación-de-issues); las demás operaciones de GitHub y Asana se gestionan manualmente por el colaborador, sin acceso remoto por parte del agente salvo nueva petición expresa.

El detalle del avance operativo, los pendientes y el siguiente paso se mantiene aquí. Los demás documentos enlazan a la sección correspondiente, sin copiar esos párrafos. Los documentos especializados conservan requisitos, propuestas, procedimientos y evidencias; los registros históricos conservan el estado del momento que documentan.
