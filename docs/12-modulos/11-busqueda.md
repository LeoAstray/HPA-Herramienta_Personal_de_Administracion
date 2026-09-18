# Módulo 11 — Búsqueda — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un motor de indexación, un algoritmo de relevancia ni un formato de índice concreto.

## Propósito

Permitir al propietario encontrar cualquier elemento del sistema —una tarea, un documento, un evento, una guía— desde un único punto de búsqueda, sin tener que recordar en qué módulo vive cada cosa.

## Problema que resuelve

A medida que crecen los módulos (Tareas, Documentos, Calendario, Estudios, Finanzas, Guías), la información del propietario se reparte entre entidades de dominio distintas. Sin un módulo de Búsqueda, encontrar algo exigiría saber de antemano en qué módulo buscar, lo que rompe la promesa de un punto único de administración personal.

## Alcance funcional propuesto

El módulo trata la búsqueda como una capa transversal de consulta, no como el dueño de ningún dato:

- `Consulta`: texto o criterio introducido por el propietario para encontrar elementos.
- `Resultado`: referencia a un elemento de dominio (tarea, documento, evento, guía, etc.) que coincide con la consulta, junto con el módulo al que pertenece.
- `Índice`: representación interna que permite localizar elementos rápidamente, como concepto de implementación, sin definir aún su tecnología.
- `Filtro`: restricción de la búsqueda a un módulo, categoría o rango de fechas concreto.

Búsqueda nunca es la fuente de verdad de un dato: siempre remite al elemento original en su módulo de origen y respeta los permisos que ese módulo definiría sobre quién puede verlo.

## Debe permitir

- Buscar por texto libre sobre los elementos que cada módulo decida hacer buscables (título, contenido descriptivo básico, metadatos).
- Mostrar resultados agrupados o etiquetados por módulo de origen.
- Filtrar resultados por módulo, categoría o rango de fechas, según lo que cada módulo exponga.
- Abrir o navegar desde un resultado hasta el elemento original en su módulo correspondiente.
- Excluir de los resultados elementos que el propietario (u otro actor futuro) no tenga permiso para ver.

## No debe hacer

- No decide todavía la tecnología de indexación ni si la búsqueda es en tiempo real o sobre un índice reconstruido periódicamente.
- No sustituye el modelo de permisos de cada módulo: si un módulo restringe el acceso a un elemento, Búsqueda debe respetarlo, no exponerlo igualmente.
- No interpreta el contenido de documentos (OCR, extracción de texto de binarios) en el MVP; eso, si se aprueba, es responsabilidad de Documentos y Archivos exponer un texto buscable.
- No ofrece búsqueda semántica ni asistida por IA en el MVP; cualquier capacidad de ese tipo corresponde a IA/Agentes y se apoyaría en este módulo, no lo sustituye.
- No indexa contenido de módulos que no lo autoricen explícitamente.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Consulta` | Texto o criterio de búsqueda del propietario. | Entrada del usuario; no se almacena como dato de dominio salvo que se apruebe un historial de búsquedas. |
| `Resultado` | Referencia a un elemento de otro módulo. | Apunta al elemento original mediante las relaciones/identificadores de Core; no lo duplica. |
| `Índice` | Representación interna para localizar elementos. | Concepto de implementación; se alimenta de lo que cada módulo expone como buscable. |
| `Filtro` | Restricción de módulo, categoría o fecha. | Se aplica sobre la consulta antes de devolver resultados. |

## Ciclo de vida y reglas iniciales

1. Cada módulo decide qué campos de sus elementos son buscables (título, descripción breve, categoría) y los expone a Búsqueda mediante un contrato definido por Core.
2. El propietario introduce una consulta, opcionalmente con filtros de módulo, categoría o fecha.
3. Búsqueda devuelve resultados que remiten al elemento original, respetando los permisos vigentes en el momento de la consulta.
4. Si un elemento se modifica o elimina en su módulo de origen, el índice debe reflejarlo con una demora aceptable aún por definir; Búsqueda no es responsable de mantener una copia autorizada del dato.
5. Un resultado nunca se edita desde Búsqueda: cualquier acción sobre el elemento se realiza en su módulo de origen.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta el contrato común para que un módulo declare qué expone como buscable, y las relaciones para referenciar el elemento original. |
| Identidad y Seguridad (1) | Filtra los resultados según los permisos del actor que realiza la búsqueda. |
| Todos los módulos funcionales (Tareas, Documentos, Calendario, Estudios, Finanzas, Guías y los que se estudien después) | Fuentes de contenido buscable, cada uno decidiendo qué expone. |
| IA/Agentes | Consumidor futuro previsible de Búsqueda para respuestas asistidas; no se decide en este módulo. |

## Seguridad, privacidad y límites de acceso

Búsqueda puede convertirse, sin querer, en una vía indirecta de exponer información sensible si no respeta con cuidado los permisos de cada módulo de origen: un resultado no debería revelar en su vista previa más de lo que el propietario podría ver directamente en el módulo original. Este módulo no debe indexar contenido marcado como sensible por otro módulo salvo que ese módulo lo autorice explícitamente y de forma consciente.

## Automatizaciones

No se propone automatización propia para el MVP: Búsqueda responde a una acción explícita del propietario. En el futuro podría estudiarse un historial de búsquedas recientes o sugerencias de búsqueda, y una capa de búsqueda semántica apoyada en IA/Agentes, pero esas capacidades no se decide aquí.

## MVP propuesto

- Búsqueda de texto libre sobre los campos que Tareas, Documentos, Calendario, Estudios, Finanzas y Guías decidan exponer.
- Resultados agrupados por módulo de origen, con navegación al elemento original.
- Filtro básico por módulo.
- Respeto de los permisos vigentes del actor en el momento de la consulta.

El soporte de filtros por fecha o categoría, el mecanismo de actualización del índice y un posible historial de búsquedas son decisiones pendientes; por ello no se presentan como requisitos aprobados.

## Futuro, no MVP

- Búsqueda semántica o asistida por IA/Agentes.
- Historial y sugerencias de búsqueda.
- Indexación de contenido extraído de documentos (texto de PDFs, OCR).
- Búsqueda por voz o desde canales externos, cuando se aprueben esas integraciones.

## Decisiones pendientes

- Qué campos concretos expone cada módulo como buscables en el MVP.
- Mecanismo y frecuencia de actualización del índice frente al dato original.
- Si existe historial de búsquedas y, si existe, cómo se protege.
- Alcance exacto de los filtros disponibles en el MVP (solo módulo, o también fecha/categoría).

## Trazabilidad

- Visión y alcance: `docs/01-proyecto/vision-y-alcance.md`.
- Core y relaciones: `docs/12-modulos/00-core.md`.
- Identidad y Seguridad: `docs/12-modulos/01-identidad-seguridad.md`.
- Configuración y Notificaciones: `docs/12-modulos/02-configuracion.md` y `docs/12-modulos/03-notificaciones.md`.
- Información Personal: `docs/12-modulos/04-informacion-personal.md`.
- Documentos y Archivos: `docs/12-modulos/05-documentos-y-archivos.md`.
- Tareas: `docs/12-modulos/06-tareas.md`.
- Calendario y Eventos: `docs/12-modulos/07-calendario-y-eventos.md`.
- Estudios: `docs/12-modulos/08-estudios.md`.
- Finanzas / Planificación Salarial: `docs/12-modulos/09-finanzas.md`.
- Guías y Procedimientos: `docs/12-modulos/10-guias-y-procedimientos.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.