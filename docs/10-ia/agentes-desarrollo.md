# Agentes de Desarrollo

## Estado

**Contrato operativo definido por el equipo; configuración ejecutable pendiente.** DEV-00 tiene una selección provisional aprobada: GPT-6 Luna / Low. Reviewer DEV-01 supera el caso documental EVAL-01 con GPT-6.1 Sol / Medium confirmado por el colaborador, sin selección definitiva ni controles efectivos verificados. EVAL-02 del Developer está preparado, no ejecutado. Los demás modelos siguen siendo candidatos del piloto; las conexiones siguen pendientes.

## Entorno y prioridades confirmados

- Dos colaboradores con responsabilidades equivalentes y asignación de tareas entre ellos; cualquiera puede aprobar revisión y pruebas.
- Ejecución local en Windows. Actualmente se utilizan Codex y VS Code, con cuentas individuales; herramientas y cuentas podrán cambiar.
- Ambos colaboradores tienen suscripción Plus individual, según confirmación del propietario. Solo se usarán capacidades incluidas en sus suscripciones; no se contratará consumo adicional de API. La disponibilidad efectiva de modelos y límites se comprobará durante la investigación.
- Inicio manual de cada tarea. Lectura de issues de GitHub y tareas del proyecto de Asana deseada; conexiones pendientes de configuración.
- Prioridades: consumo del plan → calidad → autonomía → velocidad. La autonomía mide cuánto trabajo autorizado puede completarse sin intervención humana; se evaluará dentro de los permisos establecidos.
- Ramas, staging, commits, push, pull requests, merges y publicación se realizan manualmente por los colaboradores.

## Equipo y responsabilidad

El desarrollo se realiza entre dos colaboradores. Los agentes aumentan capacidad de análisis y ejecución, pero no sustituyen la responsabilidad humana sobre alcance, seguridad, integración o publicación.

Cada cambio relevante sigue el flujo del proyecto: `Análisis -> Diseño -> Documentación -> Asana -> Implementación -> Pruebas -> Documentación actualizada`. La fase de Asana solo ocurre cuando el equipo haya creado o autorizado la tarea correspondiente; Asana no es una dependencia del producto.

## Contratos por rol

| Rol | Objetivo | Puede hacer | No puede hacer por sí solo |
| --- | --- | --- | --- |
| Preparador de petición (DEV-00) | Convertir una petición manual en un encargo claro y verificable para otro agente. | Reordenar el contexto aportado, señalar ambigüedades y proponer objetivo, alcance, restricciones y criterios de aceptación. | Cambiar la intención, ampliar permisos, inventar requisitos, ejecutar la tarea o sustituir la petición original sin mostrar los cambios. |
| Reviewer (DEV-01) | Detectar defectos, riesgos y desajustes con la documentación. | Inspeccionar el diff, ejecutar verificaciones de lectura y emitir hallazgos priorizados. | Modificar silenciosamente el cambio revisado o aprobar su propio código. |
| Developer (DEV-02) | Implementar una tarea acotada. | Editar archivos locales asignados, incluido código de pruebas; ejecutar comprobaciones locales breves del cambio y explicar el resultado. | Aprobar su trabajo, modificar el estado Git mediante operaciones de escritura, escribir en GitHub, desplegar o decidir arquitectura. |
| Tester (DEV-03) | Aportar evidencia de comportamiento y regresiones. | Diseñar casos y ejecutar pruebas en el entorno de prueba, con salidas temporales delimitadas. | Corregir código o pruebas, modificar archivos mantenidos, declarar éxito sin evidencia o desplegar. |
| Documentación (DEV-04) | Mantener trazabilidad y documentación. | Proponer cambios; editar documentos si la tarea manual lo asigna expresamente. | Convertir una propuesta en decisión o modificar el estado Git. |
| Coordinación (DEV-05) | Preparar el trabajo paralelo. | Proponer descomposición, dependencias y orden. | Gestionar servicios externos, publicar o crear tareas externas sin autorización. |

La numeración sigue el orden del piloto documental: DEV-00 Preparador → DEV-01 Reviewer → DEV-02 Developer → DEV-03 Tester. Los identificadores designan roles; el flujo habitual de un cambio sigue siendo Developer → Reviewer → Tester. DEV-04 y DEV-05 conservan sus identificadores.

## Flujo mínimo por cambio

1. Un colaborador define la petición manual. Si es ambigua, compleja o activa varios roles, DEV-00 propone una versión mejorada para que el colaborador la acepte o corrija.
2. El encargo aprobado fija objetivo, límites y archivos o módulos previsiblemente afectados.
3. DEV-02 implementa el cambio en un ámbito exclusivo, ejecuta comprobaciones locales breves y entrega resultados y comprobaciones pendientes al Tester.
4. DEV-01 revisa de forma independiente un diff estable, con los requisitos y documentos aplicables.
5. DEV-03 verifica el comportamiento y las regresiones proporcionales al riesgo.
6. Cualquiera de los dos colaboradores aprueba revisión y pruebas, o solicita expresamente correcciones al Developer. La revisión del otro colaborador es posible, pero no un requisito para cada tarea.
7. DEV-04 actualiza la trazabilidad cuando el cambio lo requiere.

## Preparación de peticiones

DEV-00 es opcional porque cada ejecución consume parte de la suscripción. Se activa cuando falten criterios de aceptación, existan varias interpretaciones razonables, haya riesgos o permisos que delimitar, o intervengan varios agentes. Una petición breve, clara y de bajo riesgo pasa directamente al rol correspondiente.

Si se invoca DEV-00 con una petición suficiente, devuelve la original intacta y recomienda usarla sin redactar una alternativa. Si hace falta mejorarla, añade una propuesta que usa, cuando aporten información, estos campos:

- resultado esperado;
- contexto y fuentes necesarias;
- alcance y exclusiones;
- archivos o módulos editables;
- permisos y acciones prohibidas;
- criterios de aceptación;
- comprobaciones esperadas;
- preguntas que cambiarían materialmente el resultado.

No añadirá requisitos por iniciativa propia. Distinguirá datos confirmados, supuestos propuestos y preguntas. El colaborador elige qué versión se envía al siguiente agente.

Los límites de la ejecución de DEV-00 (preparar mediante lectura sin editar ni ejecutar) no se transfieren automáticamente al encargo destinatario. Este conserva las acciones solicitadas y autorizadas en la petición original, sujetas al contrato del rol y a las aclaraciones pendientes. Los documentos objeto de revisión no excluyen la consulta de fuentes rectoras; no se inventarán prohibiciones adicionales de lectura.

**Configuración provisional de DEV-00:** GPT-6 Luna (`gpt-6-luna`) con esfuerzo Low (`low`), aprobada el 2026-09-30 tras dos respuestas iniciales satisfactorias de EVAL-00. La selección se hace antes de la ejecución en el cliente; el [prompt manual](prompts/dev-00-preparar-peticion.md) no cambia el modelo ni configura un agente ejecutable. No escalar ni sustituirlo sin autorización del colaborador. Si la configuración efectiva no es visible, declararla no verificada.

La salida distingue **lista para aprobación del colaborador** de **pendiente de aclaración**. Las preguntas materiales y las propuestas de alcance o permisos sin confirmar impiden presentar el encargo como listo para ejecución. DEV-00 no envía el encargo ni activa el siguiente rol.

## Reglas de concurrencia

- Un archivo tiene un único agente escritor a la vez.
- Developer, Reviewer y Tester pueden trabajar en paralelo cuando sus salidas no se solapan.
- Toda revisión identifica la revisión, el diff o commit examinado y las verificaciones ejecutadas.
- Un agente nunca usa secretos reales ni los copia a comentarios, pruebas o documentación.
- Cualquier comando destructivo, instalación, comunicación externa, publicación o cambio de permisos requiere la autorización aplicable.

## Reparto de pruebas

**Decisión actual:** el Developer edita archivos locales y puede ejecutar comprobaciones breves directamente relacionadas con su cambio, como sintaxis, formato sin corrección automática o pruebas unitarias afectadas. Solo se usarán comandos que operen en el entorno local de prueba, con salidas temporales delimitadas y sin publicación ni escritura en GitHub. El Tester conserva la validación independiente de aceptación y regresiones.

Reviewer y Tester informan de problemas; las correcciones vuelven al Developer únicamente cuando un colaborador las solicita. El código de prueba también es un archivo mantenido: el Tester puede proponerlo y el Developer escribirlo cuando se incluya en la tarea. El Developer puede subsanar errores detectados por sus propias comprobaciones dentro del alcance de la petición original.

## Entrada y salida de cada tarea

La petición manual indicará objetivo, colaborador responsable, rol, archivos editables, criterios de aceptación y comandos de prueba permitidos cuando proceda. Podrá incluir una referencia de issue o tarea de Asana. Si falta un dato, se resolverá con el contexto disponible salvo que cambie materialmente el alcance o los permisos.

| Rol | Salida mínima |
| --- | --- |
| Preparador de petición | Petición original, recomendación y estado listo/pendiente; propuesta mejorada solo si hace falta, supuestos introducidos y preguntas materiales pendientes. |
| Developer | Archivos locales cambiados, explicación breve, criterios cubiertos, comandos y resultados de comprobaciones breves y pruebas pendientes para el Tester. |
| Reviewer | Diff o estado revisado; hallazgos con archivo, ubicación, impacto y evidencia; declaración explícita si no hay hallazgos. |
| Tester | Estado examinado, comandos y casos ejecutados, resultado esperado y observado, fallos reproducibles y comprobaciones no ejecutadas. |
| Documentación | Documentos afectados, cambios y pendientes de decisión. |
| Coordinación | Subtareas, dependencias, responsables y criterio de cierre. |

Reviewer y Tester identificarán el commit base y el diff del estado de trabajo recibido. Si ese estado cambia durante la validación, marcarán su resultado como pendiente de revisión sobre la nueva versión.

## Acceso a fuentes

Se autoriza consultar el repositorio y sus documentos, y el proyecto de Asana cuando exista conexión configurada. Se prevé lectura de issues, pull requests y resultados de comprobaciones del repositorio de GitHub para aportar contexto a las tareas manuales. Esta previsión no configura conectores ni autoriza publicar comentarios o cambiar tareas externas.

Como apoyo, podrán consultarse documentos oficiales de las tecnologías que se evalúen y registros locales de pruebas generados para la tarea. No se necesita acceso general a carpetas personales, otros proyectos, credenciales, datos reales del producto ni backups. Los secretos encontrados accidentalmente se excluyen de las salidas y del contexto compartido.

GitHub es una fuente de solo lectura para todos los agentes de desarrollo. Se prohíbe modificar el repositorio remoto mediante push, API, CLI, conectores o interfaz web, así como crear o modificar issues, comentarios, pull requests, ramas remotas, ajustes o ejecuciones remotas. La edición local de archivos no concede permiso para publicarlos. Los colaboradores realizan las operaciones Git y las modificaciones externas manualmente.

## Uso eficiente de la suscripción

- Activar solo los roles necesarios para la tarea; Documentación y Coordinación son responsabilidades que pueden asumir el colaborador o el agente activo, sin lanzar sesiones adicionales por defecto.
- Proporcionar la lectura rectora obligatoria, el diff y el contexto afectado; evitar releer todas las publicaciones históricas en cada tarea.
- Trabajar secuencialmente por defecto. La concurrencia se usará cuando haya trabajo independiente y un beneficio medible.
- No ejecutar ciclos automáticos ilimitados: tras revisión y pruebas, entregar resultados y esperar una petición de corrección.
- Evaluar consumo por tarea aceptada, incluyendo reintentos y correcciones. Menor consumo no justifica omitir criterios de aceptación.
- Registrar consumo o variación de cuota solo cuando la herramienta lo exponga. Una medición desconocida se marca como no disponible; tiempo o longitud de salida no sustituyen consumo real.

## Portabilidad

Los contratos y las evidencias se mantienen en Markdown compartido. La futura configuración específica de Codex u otra herramienta debe ser reemplazable y documentar cómo aplica estos permisos. Escribir estas instrucciones no garantiza que una herramienta los imponga: los controles efectivos deberán verificarse durante el piloto.

## Evidencia mínima

Cada tarea debe dejar, en proporción a su riesgo: objetivo, cambios realizados, pruebas ejecutadas, resultado, hallazgos de revisión pendientes y documentos afectados. Las afirmaciones de un agente no sustituyen resultados reproducibles.

## Preparación para evaluar modelos

Los modelos se compararán por rol y no como una elección única: capacidad de razonamiento y revisión, calidad de edición de código, fiabilidad de pruebas, coste, latencia, contexto disponible, privacidad, capacidad de usar herramientas y facilidad de sustituirlos. La comparación partirá de tareas representativas y datos sintéticos o autorizados.

La [matriz inicial de modelos](matriz-modelos-agentes-desarrollo.md) contiene la selección provisional de DEV-00 y los candidatos de los demás roles, sujetos a disponibilidad en cada cuenta Plus y a los resultados del piloto.
