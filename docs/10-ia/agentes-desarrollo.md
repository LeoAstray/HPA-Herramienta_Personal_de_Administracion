# Agentes de Desarrollo

## Estado

**Propuesta operativa.** Este documento organiza agentes que ayudan a desarrollar el repositorio. No forma parte del producto HPA, no define modelos ni autoriza despliegues, publicaciones ni servicios externos.

## Equipo y responsabilidad

El desarrollo se realiza entre dos colaboradores. Los agentes aumentan capacidad de análisis y ejecución, pero no sustituyen la responsabilidad humana sobre alcance, seguridad, integración o publicación.

Cada cambio relevante sigue el flujo del proyecto: `Análisis -> Diseño -> Documentación -> Asana -> Implementación -> Pruebas -> Documentación actualizada`. La fase de Asana solo ocurre cuando el equipo haya creado o autorizado la tarea correspondiente; Asana no es una dependencia del producto.

## Roles propuestos

| Rol | Objetivo | Puede hacer | No puede hacer por sí solo |
| --- | --- | --- | --- |
| Developer (DEV-01) | Implementar una tarea acotada. | Editar los archivos asignados, añadir pruebas y explicar el cambio. | Aprobar su propio trabajo, desplegar, publicar o decidir arquitectura. |
| Reviewer (DEV-02) | Detectar defectos, riesgos y desajustes con la documentación. | Inspeccionar el diff, ejecutar verificaciones de lectura y emitir hallazgos priorizados. | Modificar silenciosamente el cambio revisado o aprobar su propio código. |
| Tester (DEV-03) | Aportar evidencia de comportamiento y regresiones. | Diseñar casos, ejecutar pruebas autorizadas y reportar resultados reproducibles. | Declarar listo un cambio sin evidencia o desplegarlo. |
| Documentación (DEV-04) | Mantener trazabilidad y documentación. | Proponer o realizar actualizaciones documentales autorizadas. | Convertir una propuesta en decisión. |
| Coordinación (DEV-05) | Preparar el trabajo paralelo. | Proponer descomposición, dependencias y orden. | Gestionar servicios externos, publicar o crear tareas externas sin autorización. |

## Flujo mínimo por cambio

1. Un colaborador define el objetivo, límites y archivos o módulos previsiblemente afectados.
2. DEV-01 implementa el cambio en un ámbito exclusivo y adjunta las pruebas realizadas.
3. DEV-02 revisa de forma independiente un diff estable, con los requisitos y documentos aplicables.
4. DEV-03 verifica el comportamiento y las regresiones proporcionales al riesgo.
5. Un colaborador integra o solicita correcciones; el otro colaborador participa en decisiones de alcance, seguridad o publicación relevantes.
6. DEV-04 actualiza la trazabilidad cuando el cambio lo requiere.

## Reglas de concurrencia

- Un archivo tiene un único agente escritor a la vez.
- Developer, Reviewer y Tester pueden trabajar en paralelo cuando sus salidas no se solapan.
- Toda revisión identifica la revisión, el diff o commit examinado y las verificaciones ejecutadas.
- Un agente nunca usa secretos reales ni los copia a comentarios, pruebas o documentación.
- Cualquier comando destructivo, instalación, comunicación externa, publicación o cambio de permisos requiere la autorización aplicable.

## Evidencia mínima

Cada tarea debe dejar, en proporción a su riesgo: objetivo, cambios realizados, pruebas ejecutadas, resultado, hallazgos de revisión pendientes y documentos afectados. Las afirmaciones de un agente no sustituyen resultados reproducibles.

## Preparación para evaluar modelos

Los modelos se compararán por rol y no como una elección única: capacidad de razonamiento y revisión, calidad de edición de código, fiabilidad de pruebas, coste, latencia, contexto disponible, privacidad, capacidad de usar herramientas y facilidad de sustituirlos. La comparación partirá de tareas representativas y datos sintéticos o autorizados.
