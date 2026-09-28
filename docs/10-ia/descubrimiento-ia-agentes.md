# Descubrimiento de IA y Agentes

## Estado

**Análisis inicial.** Este documento convierte la prioridad de ADR-003 en una cartera de casos de uso para investigar. No selecciona modelos, proveedores, tecnologías ni agentes aprobados para implementación.

## Ámbitos de descubrimiento

1. **Agentes internos del producto:** capacidades futuras del HPA para consultar o actuar sobre la información personal del propietario.
2. **Agentes de desarrollo:** asistentes para que los dos colaboradores analicen, implementen, revisen, prueben y documenten el código y la documentación del proyecto.

Los ámbitos son independientes. Un agente de desarrollo no es una funcionalidad del HPA, y un futuro agente del HPA no recibe acceso al repositorio por defecto.

## Objetivo

Identificar qué agentes aportarían valor real al propietario y al equipo de desarrollo, qué información necesitarían, qué acciones podrían realizar y qué controles exigirían antes de comparar modelos.

## Criterios de priorización

- **Valor:** ahorro de tiempo, reducción de dispersión o mejora de decisiones cotidianas.
- **Riesgo:** sensibilidad de los datos, impacto de una respuesta incorrecta y posibilidad de acciones irreversibles.
- **Viabilidad:** disponibilidad de datos y operaciones expuestas por el sistema.
- **Trazabilidad:** capacidad de explicar el contexto usado, la propuesta generada y el resultado.
- **Reversibilidad:** posibilidad de mantener el primer caso en solo lectura o exigir confirmación antes de modificar datos.
- **Coste operativo:** complejidad, latencia, consumo y dependencia externa que introduciría.

## Cartera inicial de agentes internos del producto

| ID | Agente candidato | Caso de uso | Datos potenciales | Acciones iniciales | Riesgo inicial | Prioridad de investigación |
| --- | --- | --- | --- | --- | --- | --- |
| AG-01 | Consulta personal | Responder preguntas sobre información, tareas, eventos, guías y documentos autorizados. | Búsqueda y resúmenes de módulos autorizados. | Solo lectura; enlaces a fuentes. | Medio por agregación de contexto. | Alta |
| AG-02 | Planificador personal | Ayudar a ordenar tareas y fechas, detectar conflictos y proponer un plan. | Tareas, calendario, prioridades y preferencias. | Propuestas; no modifica sin confirmación. | Medio. | Alta |
| AG-03 | Asistente de tareas y calendario | Convertir una petición del propietario en una tarea, evento o recordatorio. | Contexto mínimo de la petición y preferencias relevantes. | Crear o modificar tras confirmación explícita. | Medio-alto. | Alta |
| AG-04 | Organizador documental | Proponer categorías, relaciones y metadatos para archivos registrados. | Metadatos y, si se autoriza después, contenido seleccionado. | Propuestas de clasificación; no mueve ni elimina archivos. | Alto por privacidad y archivos físicos. | Media |
| AG-05 | Asistente financiero | Explicar movimientos y vencimientos y detectar preguntas para revisión. | Datos financieros expresamente autorizados. | Solo lectura y avisos; sin pagos ni cambios automáticos. | Alto por sensibilidad financiera. | Baja inicial |
| AG-06 | Asistente de operaciones y recuperación | Informar sobre estado de copias, verificaciones y procedimientos. | Estado operativo y registros de backup. | Diagnóstico y propuestas; restauración siempre manual. | Alto por impacto de recuperación. | Baja inicial |

## Candidato recomendado para el primer caso de uso del producto

La recomendación de análisis es **AG-01, Consulta personal**, limitado inicialmente a lectura, respuestas con referencias a los elementos originales y un contexto explícitamente seleccionado. Es el caso que permite validar búsqueda, composición de contexto, permisos, registro y revocación sin empezar por acciones irreversibles.

Esta recomendación es una **propuesta de análisis**, no una decisión de implementación. Debe confirmarse después de comprobar la disponibilidad del contrato de Core, la autorización de Identidad y Seguridad y la capacidad de Búsqueda para filtrar resultados.

## Cartera inicial de agentes de desarrollo

| ID | Agente candidato | Responsabilidad | Alcance inicial | Independencia requerida | Prioridad |
| --- | --- | --- | --- | --- | --- |
| DEV-01 | Developer | Implementar cambios aprobados y sus pruebas unitarias. | Rama y archivos asignados; sin despliegues ni servicios externos. | No aprueba su propio cambio. | Alta |
| DEV-02 | Reviewer | Revisar requisitos, diseño, seguridad, calidad, regresiones y documentación del cambio. | Solo lectura del diff y del contexto necesario; hallazgos accionables. | Debe ser distinto de quien produjo el cambio. | Alta |
| DEV-03 | Tester | Diseñar casos, ejecutar pruebas, reproducir fallos y comunicar evidencia. | Entorno de pruebas y resultados; no modifica producción. | Puede validar el trabajo de DEV-01. | Alta |
| DEV-04 | Documentación y trazabilidad | Mantener requisitos, ADR, cambios y evidencias coherentes con lo implementado. | Documentación afectada y referencias de prueba. | Revisión humana de decisiones. | Media |
| DEV-05 | Coordinador técnico | Descomponer trabajo, detectar dependencias y proponer orden de ejecución. | Solo planificación; no actualiza Asana ni publica sin autorización. | No sustituye decisiones del equipo. | Media |

## Configuración operativa propuesta para dos colaboradores

ADR-004 confirma el contrato de desarrollo: un colaborador define el objetivo; DEV-01 edita archivos locales delimitados y ejecuta comprobaciones breves; DEV-02 revisa un diff estable sin haberlo producido; DEV-03 realiza la validación independiente. Cualquiera de los dos colaboradores puede aprobar revisión y pruebas. Las correcciones de revisión se piden al Developer y todas las operaciones de escritura Git se realizan manualmente. GitHub es de solo lectura para los agentes. Ambos colaboradores tienen Plus y priorizan consumo, calidad, autonomía y velocidad, en ese orden.

No se asignarán dos agentes escritores al mismo archivo a la vez. La paralelización se reservará para análisis, revisión, pruebas y documentación independientes. Esta organización aprovecha agentes especializados sin perder la revisión cruzada entre las dos personas.

## Recomendación inicial para desarrollo

La propuesta es adoptar el flujo **DEV-01 → DEV-02 → DEV-03**, con DEV-04 cuando el cambio sea relevante. Mientras el proyecto siga sin código de producto, estos agentes se aplicarán a documentación, diseño, pruebas de documentación y preparación de la futura implementación; no se simulará una implementación de producción inexistente.

## Límites para los agentes internos del producto

- Acceso únicamente mediante contratos y operaciones expuestas; nunca acceso directo a almacenamiento.
- Mínimo privilegio por agente, caso de uso, módulo y tipo de dato.
- Separación entre consulta, propuesta y ejecución.
- Confirmación humana para crear, modificar o eliminar datos, salvo excepciones aprobadas explícitamente.
- Registro de contexto, solicitud, propuesta, autorización, resultado y error, minimizando datos sensibles.
- Revocación inmediata del contrato del agente.
- Prohibición de pagos, exposición a Internet, borrado o modificación física de archivos y restauraciones automáticas en esta fase.

## Preguntas que deben resolverse antes de comparar modelos

1. ¿Qué fuentes entran en el primer caso de uso del producto y cuáles quedan excluidas por sensibilidad?
2. ¿Qué nivel de frescura y precisión necesitan las respuestas del producto?
3. ¿Qué operaciones del producto serán siempre solo lectura y cuáles podrán proponerse con confirmación?
4. ¿Se exige procesamiento local para algún tipo de dato?
5. ¿Qué latencia, coste y disponibilidad son aceptables para el uso personal y para el desarrollo?
6. ¿Qué evidencia debe mostrar cada agente para que una respuesta, revisión o prueba sea verificable?
7. ¿Cómo se aplicarán en la herramienta elegida los permisos de desarrollo ya definidos por ADR-004?

## Siguiente trabajo de investigación

Para desarrollo, los permisos ya están definidos en [agentes-desarrollo.md](agentes-desarrollo.md). Se investigarán configuraciones incluidas en las suscripciones usando [escenarios documentales](evaluacion-agentes-desarrollo.md). La selección por rol aún está pendiente. Las preguntas de datos y contratos del producto siguen abiertas.

1. Confirmar los casos de uso iniciales y las fuentes autorizadas de cada ámbito.
2. Definir el contrato operativo de DEV-01, DEV-02 y DEV-03 para los dos colaboradores.
3. Convertir AG-01 en un contrato mínimo de contexto, operaciones y auditoría.
4. Definir escenarios de evaluación y ejemplos representativos sin datos reales.
5. Comparar modelos y opciones de ejecución usando esos escenarios y criterios.
6. Registrar la recomendación como decisión separada antes de implementar.

