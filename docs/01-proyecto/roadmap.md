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

**Pendientes de cierre documental:** revisión humana de la ficha R1, identificando persona, fecha, versión, alcance, observaciones y límites; corrección de los hallazgos autorizados si los hay y registro del resultado en este seguimiento y en CHG. La revisión adicional del encargo preparado es opcional, sin añadir una condición de cierre. G1 conserva conformidad únicamente sobre el diseño inicial. Los requisitos de G2–G6 están identificados, pero sus valores efectivos siguen sin aportar: responsable y raíz existente, perfiles configurados, manifiesto y exclusión del evaluador, cobertura/custodia de trazas y encargo ejecutable con modelo/esfuerzo y casos seleccionados. No se han ejecutado sondas P01–P13 ni validado controles efectivos.

**Siguiente paso inmediato:** el colaborador revisa la ficha `EVAL-05-ENTORNO-R1` con la guía R1 y comunica conformidad u observaciones sobre un alcance concreto. El encargo `EVAL-05-DEV02-R1` queda disponible como material de apoyo. Registrar la revisión y resolver las correcciones autorizadas; comprobar formato y enlaces de los cambios. Con esos criterios cubiertos puede cerrarse manualmente el issue de continuación documental, cuyo número no se ha aportado, vinculado a #36. Su cierre no cierra EVAL-05 ni autoriza sondas. La tarea posterior preparará raíz, perfiles y datos efectivos de G2–G6 antes de un encargo específico. No usar la sesión de documentación de HPA como laboratorio.

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
