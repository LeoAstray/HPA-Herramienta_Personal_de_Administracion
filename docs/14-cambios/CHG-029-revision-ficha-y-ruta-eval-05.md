# CHG-029 — Revisión humana de la ficha y ruta de EVAL-05

## Fuente y alcance de la revisión

Registrado el 2026-10-15. El colaborador de este chat comunica: «me parece bien todo lo de la ficha pero quiero cambiar la ruta a /tests/HPA-EVAL-05». Después identifica la ubicación local como una carpeta `Tests` hermana de HPA y precisa: «en los docs no pongas esa ruta completa, pon /Tests/HPA-EVAL-05».

La comunicación se refiere a la ficha `EVAL-05-ENTORNO-R1` del commit `5501a2a`, propuesto como referencia en el mensaje anterior. Se registra conformidad sobre su preparación documental con una observación concreta de ruta. No se atribuye una revisión adicional del encargo, de la nueva guía de preparación o de la plantilla de perfiles.

La observación se aplica como ficha `EVAL-05-ENTORNO-R2` y encargo `EVAL-05-DEV02-R2`. No se exige una nueva aprobación por esta corrección expresamente solicitada. Los estados operativos y la continuación se consultan en el [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05).

## Cambio documental

- Ubicación compartida `/Tests/HPA-EVAL-05`, sin ruta personal completa. La ruta absoluta efectiva se resuelve y registra localmente por el evaluador.
- Ficha y encargo actualizados; guía de revisión R2 enlazada a la evidencia y a las versiones correspondientes. CHG-028 conserva los hashes y el estado histórico de R1.
- [Guía de preparación manual](../10-ia/preparacion-raiz-perfiles-eval-05.md) y [plantilla de perfiles](../10-ia/plantillas/eval-05-perfiles.toml), con instrucciones para la raíz y perfiles Developer/Reviewer/Tester. No se instalan ni aplican.
- README de IA y roadmap actualizados. La tabla de permisos de la ficha y ADR-004 conservan su alcance; no se aprueba producto ni una nueva arquitectura.
- `docs/09-testing/README.md` sustituye su indicación operativa de revisión pendiente por un enlace al seguimiento centralizado.

## Consultas y límites

Se utiliza OpenAI Docs y se consultan páginas oficiales de permisos, configuración, Windows sandbox y CLI enlazadas desde la guía. Las consultas de versión y ayuda de la CLI identifican `0.162.0-alpha.17.2`, con avisos de acceso a temporales. La variante `codex sandbox windows --help` provocó un intento de arranque que falló; se conserva esa incidencia y no se presenta como una sonda de EVAL-05 ni como bloqueo de un recurso. No se ejecutó una evaluación del perfil del laboratorio.

No se crea la raíz ni se instala configuración; no se cambian permisos globales ni se lanzan agentes. No se accede a GitHub, Asana, credenciales ni datos reales. La conformidad humana cubre la ficha con la corrección de ruta, no acredita G2–G6 ni controles efectivos. Git, integración y cierre externo del issue siguen siendo manuales.

## Verificación

Comprobaciones locales de los nueve archivos de esta entrega, incluidos tres nuevos:

- `git --no-optional-locks diff --check`, salto final, espacios finales y marcadores de conflicto: sin incidencias.
- Resolución local PowerShell de enlaces y anclas, incluidos los nuevos documentos y la plantilla enlazada; resultados sin fallos.
- Parser de PowerShell sobre el bloque de creación: sintaxis correcta, sin ejecutar el bloque ni crear la raíz.
- Python empaquetado y `tomllib`: sintaxis TOML correcta y reglas coincidentes con la matriz documental de Developer, Reviewer y Tester; configuración sin instalar.
- Ámbito contrastado con `git --no-optional-locks diff --name-only` y `git --no-optional-locks ls-files --others --exclude-standard`: seis archivos modificados y tres nuevos, sin cambios en ADR ni registros históricos.
- Búsqueda en los archivos modificados: sin ruta personal completa al laboratorio; la ubicación elegida aparece como `/Tests/HPA-EVAL-05`. La propuesta anterior solo se conserva donde corresponde al historial.

Hashes SHA-256 de las versiones preparadas, obtenidos con `Get-FileHash`:

| Documento | SHA-256 |
| --- | --- |
| `entorno-eval-05.md` — R2 | `7E345C3BDB32E8B278A4ED77FE9047DF539303589968E0AAC415DBB306999030` |
| `encargo-eval-05-developer.md` — R2 | `BEEAB2E9D746E0B50AEBDA09EEA0907F2A435A37EC6621F943344684F2888D4E` |
| `revision-eval-05-colaborador.md` — R2 | `FFFFA2556E7512EF9B8A76E28CA69485A93AD219C17462B07EC8774403A95CB5` |
| `preparacion-raiz-perfiles-eval-05.md` | `991DADB841F50B1E901F58D66FC1E9B9285650CD52B60D21B0BCD8EE17BB9672` |
| `plantillas/eval-05-perfiles.toml` | `DDEF21F28986EA3A68F0D998772179D07092B842F01C587A7189DA78394EA010` |

Estos hashes identifican contenido; no amplían el alcance de la revisión humana recibida ni acreditan la aplicación efectiva de los perfiles.

## Seguimiento y recuperación

El avance, los pendientes y el siguiente paso se mantienen en el [roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05).

La recuperación documental, si se solicita, consiste en retirar la guía, la plantilla y este registro y revertir únicamente las modificaciones de ficha, encargo, guía humana, README de IA y roadmap de este paso, preservando cambios ajenos. La comunicación humana se conserva en la conversación; no se ejecuta limpieza del laboratorio.
