# CHG-022 — Preparación del entorno EVAL-05 y revisión humana

## Estado y autorización

Preparado el 2026-10-07, tras la valoración del colaborador «veo todos los cambios bien» y su petición de continuar. Durante este trabajo precisa: «La revision la debe hacer el colaborador, en este caso yo». Se registra su conformidad con el diseño inicial de CHG-021; la ficha nueva posterior sigue pendiente de su revisión. No se lanza Reviewer, subagente ni chat adicional.

Estado de entrada: rama `codex/disenar-evaluacion-permisos-agentes`, HEAD `2dfdd5325e9df58dae12fec315bb87d348a24e40`, con los once Markdown modificados y dos nuevos de CHG-021 todavía locales. Se preservan esos cambios. No se accede al remoto ni se publica.

## Análisis y propuesta

El contexto de esta sesión declara lectura desde la raíz, escritura sobre HPA/artefactos y capacidades externas disponibles. Esto no satisface la frontera sintética del diseño. Se inventarían garantías si se presentara una carpeta separada dentro de esta sesión como laboratorio aislado.

Se prepara la [ficha del entorno](../10-ia/entorno-eval-05.md): inventario acotado, raíz propuesta `C:\HPA-EVAL-05\`, recursos, perfiles iniciales por rol y puertas G1–G6. No se crea esa raíz, Git sintético, archivos de muestra ni configuración. La [guía humana](../10-ia/revision-eval-05-colaborador.md) sustituye la preparación inicial de un encargo a Reviewer, que no llegó a ejecutarse, conforme a la precisión del colaborador.

Se consulta documentación oficial de OpenAI sobre [permisos](https://learn.chatgpt.com/docs/permissions), [sandbox](https://learn.chatgpt.com/docs/sandboxing), [configuración](https://learn.chatgpt.com/docs/config-file/config-basic) y [sandbox Windows](https://learn.chatgpt.com/docs/windows/windows-sandbox), para fundamentar la propuesta. Las fuentes documentales no prueban disponibilidad o aplicación en este cliente. No se inspecciona configuración personal, tokens, credenciales ni trazas privadas.

## Cambios y límites

Ficha y guía nuevas; diseño inicial actualizado con revisión humana y siguiente paso; roadmap, estado, README general, README de IA, contrato de desarrollo y registro de evaluación sincronizados. CHG-021 se conserva como registro del paso anterior. No cambia la matriz de permisos de ADR-004 ni la arquitectura del producto; no requiere ADR nueva. No se publican DOCX/PDF de una línea base consolidada aún pendiente de revisión de la ficha.

Preparación documental únicamente: sin modificación de permisos reales, instalación, laboratorio, sondas, operaciones Git de escritura o acceso a GitHub/Asana. No hay resultados de EVAL-05 ni afirmación de bloqueo técnico. El contexto declarado se distingue de mediciones; PowerShell y Git se consultan con comandos locales de lectura.

## Verificación

Comprobación local de plataforma y herramientas: Win32NT, PowerShell 7.6.5 y Git 2.56.0.windows.2. Estos valores no identifican la versión exacta del cliente ni la configuración efectiva de un laboratorio futuro.

Verificación final local: `git --no-optional-locks diff --check` sin incidencias en rastreados; comprobación de espacios finales en los cinco Markdown nuevos sin rastrear, sin incidencias. Resolución PowerShell de 89 enlaces relativos sobre los dieciséis Markdown afectados por CHG-021/022: todos los destinos existen; no se verifican anclas ni se consulta GitHub. Estado final: once Markdown modificados y cinco nuevos, sin otros cambios observados. Se contrasta la coherencia de revisión humana y pendientes; no es revisión independiente ni ejecución de casos. Las consultas oficiales no identifican la configuración efectiva del cliente.

## Resultado y siguiente paso

Conformidad humana registrada para el diseño inicial; ficha de entorno y guía preparadas, pendientes de revisión del colaborador. Próximo paso: revisar esa ficha, preparar la raíz/perfiles separados y completar puertas G2–G6 antes del encargo del primer perfil. La actualización del roadmap permanece obligatoria en cada avance.

Recuperación documental: restaurar únicamente los cambios de este paso si procede, preservando CHG-021 y cambios ajenos. No se ejecuta recuperación ni limpieza.
