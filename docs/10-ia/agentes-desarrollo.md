# Agentes de Desarrollo

## Estado

**Contrato operativo definido por el equipo; configuración pendiente.** Las restricciones y preferencias siguientes proceden de las respuestas del propietario. Los modelos, la plataforma de ejecución y las conexiones aún deben investigarse.

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
| Developer (DEV-01) | Implementar una tarea acotada. | Editar archivos locales asignados, incluido código de pruebas; ejecutar comprobaciones locales breves del cambio y explicar el resultado. | Aprobar su trabajo, modificar el estado Git mediante operaciones de escritura, escribir en GitHub, desplegar o decidir arquitectura. |
| Reviewer (DEV-02) | Detectar defectos, riesgos y desajustes con la documentación. | Inspeccionar el diff, ejecutar verificaciones de lectura y emitir hallazgos priorizados. | Modificar silenciosamente el cambio revisado o aprobar su propio código. |
| Tester (DEV-03) | Aportar evidencia de comportamiento y regresiones. | Diseñar casos y ejecutar pruebas en el entorno de prueba, con salidas temporales delimitadas. | Corregir código o pruebas, modificar archivos mantenidos, declarar éxito sin evidencia o desplegar. |
| Documentación (DEV-04) | Mantener trazabilidad y documentación. | Proponer cambios; editar documentos si la tarea manual lo asigna expresamente. | Convertir una propuesta en decisión o modificar el estado Git. |
| Coordinación (DEV-05) | Preparar el trabajo paralelo. | Proponer descomposición, dependencias y orden. | Gestionar servicios externos, publicar o crear tareas externas sin autorización. |

## Flujo mínimo por cambio

1. Un colaborador define el objetivo, límites y archivos o módulos previsiblemente afectados.
2. DEV-01 implementa el cambio en un ámbito exclusivo, ejecuta comprobaciones locales breves y entrega resultados y comprobaciones pendientes al Tester.
3. DEV-02 revisa de forma independiente un diff estable, con los requisitos y documentos aplicables.
4. DEV-03 verifica el comportamiento y las regresiones proporcionales al riesgo.
5. Cualquiera de los dos colaboradores aprueba revisión y pruebas, o solicita expresamente correcciones al Developer. La revisión del otro colaborador es posible, pero no un requisito para cada tarea.
6. DEV-04 actualiza la trazabilidad cuando el cambio lo requiere.

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
