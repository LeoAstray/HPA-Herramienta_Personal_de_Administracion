# EVAL-05 — Revisión por el colaborador

## Responsabilidad y estado

**Guía R2, preparada el 2026-10-15**, para la ficha `EVAL-05-ENTORNO-R2` y el encargo documental `EVAL-05-DEV02-R2`. La revisión recibida sobre R1 y su corrección autorizada se registran en el roadmap y en CHG-029; no se exige repetir esa revisión por el cambio de ruta solicitado.

La revisión humana exigida por el issue cubre la ficha del entorno. El encargo documental es material de apoyo y una entrega preparada; su revisión adicional puede declararse, pero no se añade como condición de cierre del issue.

La revisión documental corresponde al colaborador. No se requiere un Reviewer agente para esta revisión. Los contratos de los agentes de ADR-004 no cambian.

El estado de revisión del diseño y la [ficha del entorno](entorno-eval-05.md), los pendientes y el siguiente paso se consultan en el [seguimiento de EVAL-05 en el roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05). La aceptación documental no demuestra controles efectivos ni autoriza por sí sola la ejecución.

## Material a revisar

- [Diseño inicial](diseno-evaluacion-permisos-agentes.md): matriz, casos P01–P13, procedimiento y evidencia.
- [Ficha del entorno](entorno-eval-05.md): inventario histórico, estructura propuesta, puertas G1–G6 y datos exigidos para el futuro laboratorio.
- [Preparación del encargo Developer](encargo-eval-05-developer.md): campos por completar, límites y aceptación visible del encargo futuro.
- [Roadmap](../01-proyecto/roadmap.md): avance y siguiente paso.

R1 se conserva en el commit `5501a2a` y su preparación se identifica en [CHG-028](../14-cambios/CHG-028-preparacion-documental-encargo-eval-05.md). R2 parte de ese commit; [CHG-029](../14-cambios/CHG-029-revision-ficha-y-ruta-eval-05.md) identifica la revisión recibida y el cambio de ruta. El colaborador examina la versión correspondiente, incluidos los cambios locales. Antes de integrar, las personas gestionan staging, commits y publicación manualmente.

## Lista de revisión de la ficha

La lista valora la propuesta documental y sus límites. Dar conformidad no afirma que exista un laboratorio ni que sus controles funcionen. Los campos por completar se aceptan como requisitos para la configuración futura, sin inventar sus valores.

- [ ] El laboratorio usará una raíz nueva y separada de HPA, sin worktree, remotos, credenciales ni datos reales.
- [ ] El perfil efectivo limitará la lectura y escritura por rol; los directorios por sí solos no se toman como aislamiento.
- [ ] Los recursos mínimos de ejecución no incluyen HPA, carpetas personales ni el ámbito del evaluador.
- [ ] La clave y las trazas quedan fuera del acceso del agente evaluado.
- [ ] La red de comandos, navegador, web y conectores se comprueban como canales separados.
- [ ] No se conceden escalaciones durante los casos ni se cambia configuración global.
- [ ] Se exige comprobar que el cliente permite aplicar y observar los controles, o declarar el requisito no verificable, antes de ejecutar.
- [ ] Están identificados responsable, ruta, modelo/esfuerzo, manifiesto y cobertura de evidencia como datos que deben completarse antes del encargo ejecutable.
- [ ] El inventario del 2026-10-07 se reconoce como histórico, sin atribuir sus versiones y permisos a un laboratorio actual.
- [ ] La preparación DEV-02 declara el rol, los casos candidatos y los valores por completar, y conserva las prohibiciones de ADR-004.

## Forma de comunicar la revisión

Para una revisión adicional, el colaborador identifica la versión y puede responder «ficha EVAL-05-ENTORNO-R2 revisada, conforme con su preparación documental» o indicar correcciones concretas. Si revisa solo una parte de la ficha, debe identificar ese alcance; si revisa también el encargo, puede indicarlo. No se exige seleccionar un modelo ni completar datos del laboratorio para realizar una revisión humana.

Al recibir el resultado, registrar en el roadmap la fecha, persona revisora, versiones y alcance efectivamente revisados, observaciones y límites. El registro CHG conservará la fuente de esa comunicación y las correcciones autorizadas. Si los documentos cambian después, identificar la nueva versión y el alcance de la revisión adicional que corresponda. Las casillas de esta guía no son por sí solas evidencia de revisión.

## Resultado esperado de este paso

Ficha revisada, con versión, alcance, observaciones y límites registrados; requisitos de G2–G6 identificados y encargo futuro preparado documentalmente. El issue de preparación documental puede cerrarse cuando se registre esa revisión, se resuelvan sus hallazgos autorizados y se verifiquen los cambios. El laboratorio, los valores efectivos de G2–G6 y la ejecución de casos pertenecen a trabajo posterior. Configurar un perfil no equivale a verificarlo mediante los casos de EVAL-05.
