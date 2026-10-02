# CHG-019 — Resultados de EVAL-04: Reviewer y Tester

## Estado y autorización

Registrado el 2026-10-03 por la petición del colaborador «Sigue con el siguiente paso», tras aportar las respuestas de Reviewer y Tester y revisar la repetición de este último. El encargo es documentar la evidencia y actualizar el estado del piloto. La fecha del registro no determina la fecha exacta de ejecución: las transcripciones solo aportan horas de interfaz.

## Análisis y criterio de registro

Se contrastan los resultados con la muestra S1 y las fuentes locales. Reviewer detecta los tres defectos con evidencia e impacto, sin falsos positivos. Tester detecta los tres en ambas respuestas; la primera comunica lectura del documento de evaluación, cuyo contenido incluye criterios esperados. La repetición recibe una exclusión adicional de documentos y conserva detección correcta, con impactos poco desarrollados y una celda incoherente en el caso L6. El razonamiento y conclusión de L6 sí son correctos.

Se conservan separadamente las tres peticiones y respuestas, con sus horas y tiempos mostrados: 45 s, 29 s y 22 s. La aportación inicial con `[ROL]` sin sustituir fue reemplazada por la de Reviewer y no se cuenta como ejecución identificada de un rol. No se eliminan la incidencia ni la intervención humana del historial. No se afirma que la repetición tenga entrada idéntica a las otras ejecuciones, ni que estos tiempos permitan comparar consumo.

Sol 6.1 / Medium del Reviewer está confirmado por el colaborador. Luna / Medium del Tester se registra por el contexto comunicado del encargo y su continuidad, sin confirmación individual adicional en cada transcripción ni telemetría independiente.

## Documentación actualizada

- [Evaluación](../10-ia/evaluacion-agentes-desarrollo.md): resultados por ejecución, contenido, protocolo, intervención humana, comandos comunicados y límites; preparación anterior conservada como estado histórico.
- [Contrato operativo de desarrollo](../10-ia/agentes-desarrollo.md): estado del piloto actualizado; los permisos siguen definidos por ADR-004.
- [Matriz de modelos](../10-ia/matriz-modelos-agentes-desarrollo.md): evidencia adicional por rol y advertencia sobre entrada ajustada y consumo no comparable.
- [Estado del proyecto](../00-gobierno/estado-proyecto.md) y [roadmap](../01-proyecto/roadmap.md): EVAL-04 registrado y comprobación de controles como siguiente trabajo propuesto.
- [README de IA](../10-ia/README.md): distingue contratos y selecciones provisionales de desarrollo de propuestas del producto; corrige sus estados desactualizados señalados en EVAL-01. El estado del prompt DEV-00 sigue pendiente.
- [Encargo EVAL-04](../10-ia/prompts/eval-04-deteccion-sintetica.md): estado actualizado y precisión de la repetición registrada fuera del bloque original.
- Transcripciones íntegras de [Reviewer](../10-ia/evidencias/eval-04-2026-10-03-reviewer-peticion-y-respuesta.md), [Tester inicial](../10-ia/evidencias/eval-04-2026-10-03-tester-primera-peticion-y-respuesta.md) y [Tester repetición](../10-ia/evidencias/eval-04-2026-10-03-tester-repeticion-peticion-y-respuesta.md), con hash de cada adjunto de origen.

## Resultado y pendientes

Reviewer satisfactorio para este caso; Tester satisfactorio en detección tras repetición, con incidencia inicial y observaciones de entrega conservadas. No se requiere otra repetición automática por esas observaciones. Los candidatos de Reviewer y Tester se mantienen y las selecciones provisionales anteriores no cambian. Este cambio registra evidencia, no una nueva decisión de arquitectura o permisos; no requiere una ADR nueva ni modifica los contratos de los agentes del producto.

Siguen pendientes controles efectivos, trazas completas, consumo atribuible, utilidad de DEV-00 frente a una plantilla y configuración ejecutable. No se garantiza evaluación ciega, fiabilidad general ni cierre del piloto. La propuesta de comprobar permisos en un entorno local desechable queda sin diseñar ni ejecutar. No se crean tareas de Asana, ni se implementa producto, ni se lanzan agentes.

## Comprobaciones documentales

Estado local previo al registro: HEAD `06689607869f722d5c69284c9c99a6f88b71deb6`, árbol limpio. `Test-Path` confirma que el destino ficticio de L3 no existe. Las cláusulas citadas de permisos, consumo y arquitectura coinciden con las fuentes actuales. El hash del registro anterior coincide con el comunicado por el primer Tester; ese hash identifica la versión anterior a CHG-019.

Comprobaciones ejecutadas por el agente que registra:

- `git --no-optional-locks rev-parse HEAD` y `status --short`: HEAD indicado y árbol limpio antes de editar; al terminar, siete Markdown modificados, tres transcripciones nuevas y este registro nuevo, sin cambios adicionales observados.
- `Test-Path` sobre L3: `False`. `Get-FileHash` del registro anterior: coincide con el hash comunicado por TST1. Los hashes del índice ADR y CHG-016 conservan los valores registrados en EVAL-03.
- Lectura y contraste de cláusulas rectoras, de adjuntos y del diff. `git --no-optional-locks diff --check`: sin incidencias en archivos rastreados; no cubre los nuevos sin rastrear.
- Comprobación local en PowerShell de 33 enlaces documentales relativos en los siete documentos operativos y CHG-019, excluyendo bloques de código: todos los destinos existen. No se consultan ni revalidan fuentes web.
- Comparación textual del primer bloque de petición de EVAL-04 con `git --no-optional-locks show HEAD:docs/10-ia/prompts/eval-04-deteccion-sintetica.md`, normalizando terminadores de línea: contenido íntegro conservado.
- Comparación ordinal del texto completo de cada adjunto con el final de su archivo de evidencia: las tres transcripciones están íntegras. Se conservan su formato y posibles espacios originales.

Los enlaces sintéticos inexistentes dentro del bloque de prueba y las transcripciones son parte de la evidencia, no referencias operativas nuevas. Las comprobaciones propias del registro no sustituyen la validación independiente de las ejecuciones ni acreditan ausencia histórica de escrituras. No se ejecutan operaciones Git de escritura, acciones en GitHub o Asana, ni otras evaluaciones.
