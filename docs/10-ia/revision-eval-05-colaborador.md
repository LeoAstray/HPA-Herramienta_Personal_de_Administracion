# EVAL-05 — Revisión por el colaborador

## Responsabilidad y estado

El 2026-10-07 el colaborador comunica «veo todos los cambios bien» sobre el diseño inicial y precisa que la revisión le corresponde a él. Esa conformidad humana se registra sobre el diseño entregado con CHG-021. No se exige ni lanza un Reviewer agente para esta revisión. Los contratos de los agentes de ADR-004 no cambian.

La [ficha del entorno](entorno-eval-05.md), preparada después de esa conformidad, sigue pendiente de su revisión. La aceptación documental no demuestra controles efectivos ni autoriza ejecutar EVAL-05 en la sesión actual.

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

El colaborador puede responder «ficha revisada, conforme» o indicar correcciones concretas. Se registrará la versión revisada y sus observaciones. Hasta recibir esa revisión, G1 está completada para el diseño inicial y pendiente para la ficha nueva; G2–G6 continúan pendientes. No se exige seleccionar un modelo para realizar una revisión humana.

## Resultado esperado de este paso

Ficha revisada y alcance de preparación confirmado. Después, el colaborador prepara los perfiles del laboratorio y aporta los valores efectivos para completar G2–G6. Configurar un perfil no equivale todavía a verificarlo mediante los casos de EVAL-05.
