# Evaluación de agentes de desarrollo

## Estado y objetivo

**Diseño de piloto; ejecución pendiente.** Comparar configuraciones incluidas en las suscripciones de los dos colaboradores, siguiendo el contrato de [agentes-desarrollo.md](agentes-desarrollo.md). Modelos y cuotas disponibles todavía no están comprobados.

Ambos colaboradores tienen Plus individual. El orden de evaluación es consumo → calidad → autonomía → velocidad; la disponibilidad efectiva de cada configuración debe verificarse.

## Escenarios iniciales

| ID | Rol | Entrada | Criterio de aceptación |
| --- | --- | --- | --- |
| EVAL-00 | Preparador de petición | Una petición clara y otra ambigua sobre el mismo tipo de cambio documental. | Omitirse en la petición clara; en la ambigua, conservar intención y permisos, identificar carencias y producir criterios verificables sin ejecutar la tarea. |
| EVAL-01 | Reviewer | Documentación operativa de estado, roadmap, ADR y agentes de desarrollo. | Detectar contradicciones con referencias verificables y distinguir fuentes históricas de estado actual, sin editar. |
| EVAL-02 | Developer | Solicitud acotada de corregir un enlace o una incoherencia previamente confirmada en Markdown. | Editar solo los documentos asignados y el registro de cambios aplicable, conservar decisiones y dejar Git sin operaciones de escritura. |
| EVAL-03 | Tester | Diff estable de EVAL-02 y sus criterios de aceptación. | Verificar destinos de enlaces, coherencia y formato; comunicar comandos y resultados, sin corregir los archivos mantenidos. |
| EVAL-04 | Reviewer y Tester | Ejemplo sintético entregado en la petición con enlace roto, afirmación contradictoria y afirmación sin evidencia. | Identificar los defectos esperados, explicar su impacto y evitar inventar problemas. |

El primer piloto comenzará con EVAL-00 y continuará con EVAL-01, una corrección solicitada por un colaborador mediante EVAL-02 y su validación EVAL-03. EVAL-04 permite comprobar detección de fallos sin introducir errores deliberados en la documentación operativa. Estas tareas no autorizan código de producto.

## Registro por ejecución

- Identificador de escenario, fecha, colaborador y estado exacto examinado.
- Herramienta, modelo y configuración efectivamente usados; no inferir datos no expuestos.
- Entrada y criterios de aceptación comunes para las alternativas.
- Resultado, defectos encontrados, falsos positivos, omisiones y correcciones humanas necesarias.
- Consumo observado, fuente de medición y limitaciones; no disponible si no puede atribuirse a la ejecución.
- Tiempo hasta obtener un resultado aceptable y número de rondas.
- Intervenciones humanas necesarias para completar el trabajo autorizado; no contar como defecto las aprobaciones y operaciones Git que el contrato reserva a las personas.
- Respeto de permisos, con atención a pruebas del Developer y operaciones Git.
- Para DEV-00: intención preservada, requisitos inventados, preguntas útiles, mejora de aceptación del agente siguiente y consumo añadido por preparar la petición.

## Criterio de elección

Primero descartar configuraciones que incumplan permisos o criterios mínimos de calidad. Entre las que cumplen, priorizar menor consumo total por tarea aceptada, después calidad adicional, después capacidad de completar el trabajo autorizado con menos intervenciones y finalmente tiempo. Si el consumo no es comparable, registrar la incertidumbre y evitar declarar un ganador por consumo.

El piloto verificará que el Developer puede efectuar comprobaciones breves locales y que ningún agente realiza escrituras Git o modificaciones en GitHub. Las validaciones de esos límites se harán con evidencias locales y controles de permisos, sin intentar escribir en el repositorio remoto real.

Probar inicialmente una tarea pequeña por rol. Repetir o ampliar solo cuando existan diferencias relevantes o incertidumbre que afecte a la elección. Los dos colaboradores pueden repartirse escenarios y compartir resultados; no se presupone que cuentas o herramientas tengan los mismos límites.

DEV-00 se conserva solo si reduce repeticiones o errores más de lo que aumenta el consumo. También se comparará con una plantilla rellenada directamente por el colaborador, que no requiere una ejecución adicional.

El prompt experimental de EVAL-00 se mantiene en [prompts/dev-00-preparar-peticion.md](prompts/dev-00-preparar-peticion.md). Su redacción podrá cambiar a partir de los resultados; todavía no es una skill ni una configuración definitiva.
