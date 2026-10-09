# CHG-021 — Diseño de EVAL-05 y actualización obligatoria del roadmap

## Estado y autorización

Documentado el 2026-10-07 por la petición del colaborador de revisar la regla del roadmap y continuar con el siguiente paso del [issue #36](https://github.com/LeoAstray/HPA-Herramienta_Personal_de_Administracion/issues/36). Trabajo local en `codex/disenar-evaluacion-permisos-agentes`, base `2dfdd5325e9df58dae12fec315bb87d348a24e40`, árbol inicialmente limpio. La fecha corresponde al trabajo documental, no a una evaluación ejecutada.

## Análisis y diseño

Ni `AGENTS.md` ni el proceso de cambio nombraban explícitamente la actualización obligatoria del roadmap. La instrucción directa del colaborador se incorpora a ambos: cada cambio registra avance, pendientes y siguiente paso, aunque no altere el orden de hitos.

El pendiente de EVAL-04 era comprobar controles efectivos: la detección correcta del Tester y su declaración de lecturas no acreditan aislamiento. Se prepara [EVAL-05](../10-ia/diseno-evaluacion-permisos-agentes.md) con matriz de los seis roles, trece casos, entorno sintético, separación del evaluador, procedimiento, encargo adaptable y plantilla de resultados. Las pruebas de comportamiento y las sondas técnicas humanas se evalúan por separado. Una simulación o falta de trazas no se presenta como bloqueo demostrado.

## Documentación actualizada

- `AGENTS.md` y [proceso de cambio](../00-gobierno/proceso-de-cambio.md): regla obligatoria del roadmap y preferencia de issues manuales en las instrucciones de agentes.
- [Roadmap](../01-proyecto/roadmap.md), [estado](../00-gobierno/estado-proyecto.md) y [README general](../README.md): diseño preparado y siguiente paso explícito. README/estado reflejan también Core aprobado por ADR-005; tecnología y autorización permanecen pendientes.
- [Contrato de desarrollo](../10-ia/agentes-desarrollo.md), [evaluación](../10-ia/evaluacion-agentes-desarrollo.md) y [README de IA](../10-ia/README.md): trazabilidad de EVAL-05 y distinción entre diseño y resultados.
- [Módulo 14](../12-modulos/14-ia-agentes.md): referencia al piloto de desarrollo manteniéndolo separado de los agentes del producto.
- [Seguridad](../07-seguridad/README.md) y [pruebas](../09-testing/README.md): condiciones y límites del laboratorio propuesto.

## Decisiones, límites e impacto

La regla del roadmap y la publicación manual de issues proceden de instrucciones expresas del colaborador. EVAL-05 es una propuesta documental de evaluación; no cambia los permisos de ADR-004 ni la decisión de Core de ADR-005, y no requiere una ADR arquitectónica nueva. No elige herramientas o tecnologías ni implementa producto, configuración, sondas o scripts de laboratorio. No altera datos, API, interfaz, despliegue ni infraestructura. No se genera una publicación DOCX/PDF de una línea base consolidada: el diseño permanece pendiente de revisión independiente.

No se accede a GitHub ni se utiliza autenticación Git, no se edita el issue ni se opera Asana. El colaborador puede publicar el resumen manualmente y gestionar la tarea de Asana si procede. No se realizan operaciones Git de escritura ni se lanzan agentes. La selección de modelos no cambia; no se registra consumo atribuible.

## Verificación y recuperación

Comprobaciones locales ejecutadas:

- `git --no-optional-locks diff --check`: sin incidencias en archivos rastreados. Revisión adicional de espacios finales de los dos nuevos Markdown sin rastrear: sin incidencias.
- Resolución de enlaces relativos mediante PowerShell sobre los trece Markdown afectados: 63 referencias comprobadas, 39 destinos de enlace nuevos respecto a la versión base de cada documento; todos existen. No se consultan enlaces web ni se verifican anclas internas.
- Lectura del diff y contraste con ADR-004 y el registro del piloto: permisos conservados, historial de EVAL-04 intacto, EVAL-05 identificado como diseño sin ejecutar y siguiente paso consistente en roadmap, estado y documentos de IA.
- `git --no-optional-locks status --short`: once Markdown modificados y dos nuevos, sin otros cambios observados. No se realiza validación independiente ni se accede al remoto.

Estas comprobaciones documentales no constituyen ejecución de EVAL-05 ni validación independiente del diseño. La recuperación documental consistiría en restaurar solo los archivos afectados desde la base, conservando cambios ajenos; no se ejecuta ahora ninguna restauración. La recuperación del laboratorio futuro está definida en el diseño y corresponde al colaborador.

## Resultado y siguiente paso

**Estado actual:** diseño preparado, roadmap actualizado y regla persistida. **Pendientes:** revisión independiente, concreción del entorno/control, configuración, encargo de ejecución y resultados. No se declara aislamiento efectivo, evaluación ciega, cierre del piloto ni fiabilidad general.

**Siguiente paso:** revisar el diseño sobre un diff estable y definir el entorno y la evidencia que puede proporcionar antes de ejecutar los casos. Actualizar el roadmap y el registro de cambios al completar ese avance.
