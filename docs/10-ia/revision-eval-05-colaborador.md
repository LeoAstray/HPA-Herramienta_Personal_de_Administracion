# EVAL-05 — Revisión por el colaborador

## Responsabilidad y estado

La revisión documental corresponde al colaborador. No se requiere un Reviewer agente para esta revisión. Los contratos de los agentes de ADR-004 no cambian.

El estado de revisión del diseño y la [ficha del entorno](entorno-eval-05.md), los pendientes y el siguiente paso se consultan en el [seguimiento de EVAL-05 en el roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05). La aceptación documental no demuestra controles efectivos ni autoriza por sí sola la ejecución.

## Material a revisar

- [Diseño inicial](diseno-evaluacion-permisos-agentes.md): matriz, casos P01–P13, procedimiento y evidencia.
- [Ficha del entorno](entorno-eval-05.md): límites actuales, estructura propuesta y puertas G1–G6.
- [Roadmap](../01-proyecto/roadmap.md): avance y siguiente paso.

El colaborador revisa el estado de trabajo local, incluidos los nuevos sin rastrear. Base HEAD `2dfdd5325e9df58dae12fec315bb87d348a24e40`; rama `codex/disenar-evaluacion-permisos-agentes`. Antes de integrar, las personas gestionan staging, commits y publicación manualmente.

## Lista de revisión de la ficha

- [ ] El laboratorio usará una raíz nueva y separada de HPA, sin worktree, remotos, credenciales ni datos reales.
- [ ] El perfil efectivo limitará la lectura y escritura por rol; los directorios por sí solos no se toman como aislamiento.
- [ ] Los recursos mínimos de ejecución no incluyen HPA, carpetas personales ni el ámbito del evaluador.
- [ ] La clave y las trazas quedan fuera del acceso del agente evaluado.
- [ ] La red de comandos, navegador, web y conectores se comprueban como canales separados.
- [ ] No se conceden escalaciones durante los casos ni se cambia configuración global.
- [ ] El cliente permite aplicar y observar estos controles, o se registra el requisito no verificable antes de ejecutar.
- [ ] Se designa responsable y se completan ruta, modelo/esfuerzo del agente evaluado, manifiesto y cobertura de evidencia antes del encargo.

## Forma de comunicar la revisión

El colaborador puede responder «ficha revisada, conforme» o indicar correcciones concretas. Se registrará la versión revisada y sus observaciones en el roadmap. No se exige seleccionar un modelo para realizar una revisión humana.

## Resultado esperado de este paso

Ficha revisada y alcance de preparación confirmado. Después, el colaborador prepara los perfiles del laboratorio y aporta los valores efectivos para completar G2–G6. Configurar un perfil no equivale todavía a verificarlo mediante los casos de EVAL-05.
