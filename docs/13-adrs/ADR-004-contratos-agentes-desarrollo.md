# ADR-004 — Contratos de agentes de desarrollo

## Estado y fecha

**Decisión de organización y permisos**, basada en las respuestas del propietario del 2026-09-28. Actualizada el 2026-09-30 con la selección provisional de DEV-00 y la política provisional de modelos de DEV-02. Configuración ejecutable y selección de los demás roles pendientes.

## Contexto

Dos colaboradores con responsabilidades equivalentes desarrollan el repositorio en Windows, usando actualmente Codex y VS Code con cuentas individuales Plus. Se busca optimizar las suscripciones existentes, con prioridad de consumo, calidad, autonomía y velocidad, en ese orden, y posibilidad de cambiar de herramienta.

## Opciones y decisión

Se comparan un flujo con publicación y corrección automáticas, y un flujo iniciado manualmente con permisos por rol. Se adopta el segundo: Developer edita archivos locales y ejecuta comprobaciones breves del cambio; Reviewer y Tester informan; Tester realiza la validación independiente. Las correcciones derivadas de revisión y validación se solicitan al Developer por una persona. Cualquiera de los dos colaboradores puede aprobar resultados.

Se incorpora un Preparador de petición opcional (DEV-00) para encargos ambiguos, complejos o con varios roles. Conserva la petición original, propone una versión mejorada y requiere que un colaborador decida cuál usar. Se omite en tareas claras para reducir consumo.

Los colaboradores gestionan ramas, staging, commits, push, pull requests, merges y publicación manualmente. Los agentes operan localmente y con capacidades incluidas en las suscripciones; queda excluido gasto adicional de API. Issues de GitHub y tareas del proyecto Asana son fuentes deseadas de contexto, con conexiones pendientes.

## Consecuencias

Los contratos y escenarios se documentan en Markdown portable. La configuración deberá demostrar que aplica los permisos. No se requieren sesiones adicionales para cada responsabilidad ni concurrencia por defecto. La selección de modelos se hará con tareas aceptadas y evidencia de consumo disponible.

La preparación de agentes de desarrollo puede avanzar antes de la arquitectura del producto: sus permisos corresponden al repositorio. Core e Identidad y Seguridad siguen condicionando los agentes internos del producto.

Se aprueban comprobaciones locales breves del Developer dentro del alcance asignado. GitHub queda como fuente de solo lectura para todos los agentes; las escrituras mediante push, API, CLI, conectores o interfaz web están excluidas. La autonomía se optimizará dentro de esos límites y no eliminará las aprobaciones ni las operaciones manuales de Git.

El 2026-09-30 el colaborador aprueba mantener provisionalmente GPT-6 Luna (`gpt-6-luna`) con esfuerzo Low (`low`) para DEV-00, tras aportar dos respuestas satisfactorias de EVAL-00. Esta evidencia no demuestra ahorro de cuota ni verificación de operaciones realizadas. La revisión posterior del prompt requiere una comprobación de regresión. No se permite escalado automático; una alternativa requiere autorización humana.

La selección se aplica manualmente antes de ejecutar DEV-00; los documentos no cambian el modelo del chat. La configuración ejecutable sigue pendiente. La política de Developer se actualiza mediante la decisión posterior de esta ADR; los demás roles conservan candidatos sujetos al piloto. La matriz se conserva en `docs/10-ia/matriz-modelos-agentes-desarrollo.md`.

El 2026-09-30 el colaborador aprueba renumerar los roles aún no probados para alinearlos con el piloto documental: Reviewer pasa de DEV-02 a DEV-01 y Developer de DEV-01 a DEV-02. DEV-00, DEV-03, DEV-04 y DEV-05 conservan sus identificadores. La numeración no impone el flujo de ejecución: en un cambio habitual, Developer precede a Reviewer. Los permisos y candidatos de modelo y esfuerzo permanecen asociados a sus roles.

El 2026-09-30 el colaborador aprueba provisionalmente GPT-6.1 Sol (gpt-6.1-sol) / Medium (medium) como configuración habitual de Developer DEV-02, con GPT-6 Luna (gpt-6-luna) / Medium (medium) autorizado para tareas sencillas y acotadas. Se seleccionará y registrará antes de cada encargo. Sol se usará por defecto para funcionalidades, lógica de negocio, refactorizaciones y cambios con dependencias entre archivos; Luna puede usarse para enlaces, cambios mecánicos y correcciones pequeñas con criterios claros y bajo riesgo. Cambiar de modelo durante una ejecución, usar otra configuración o sustituir un modelo no disponible requiere autorización humana. Esta decisión no configura el cliente ni autoriza implementar producto; tampoco demuestra ahorro o calidad comparativa. EVAL-02 solo aporta evidencia documental con Luna, pendiente de EVAL-03; Sol como Developer aún no se ha evaluado.

## Referencias

- [Contratos operativos](../10-ia/agentes-desarrollo.md)
- [Evaluación](../10-ia/evaluacion-agentes-desarrollo.md)
- [Matriz de modelos](../10-ia/matriz-modelos-agentes-desarrollo.md)
- [ADR-003](ADR-003-priorizacion-descubrimiento-ia-agentes.md)
