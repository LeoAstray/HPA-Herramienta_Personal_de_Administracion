# Herramienta Personal de Administración

## Propósito de esta documentación

Esta carpeta describe el producto, sus decisiones y su evolución para que una persona o agente sin conversaciones previas pueda comprenderlo y continuarlo. El contenido Markdown es la fuente de verdad operativa. Los archivos DOCX y PDF son versiones de lectura de una línea base aprobada o de una revisión documental.

## Estado actual

**Fase:** definición y estudio global de módulos.  
**Implementación de producto:** no iniciada.  
**Arquitectura técnica concreta:** pendiente.  
**Próximo objetivo:** el colaborador revisa la [ficha de entorno EVAL-05](10-ia/entorno-eval-05.md), posterior a su conformidad con el diseño inicial; después se completan perfiles y evidencias antes de encargar la ejecución. La sesión actual no constituye un laboratorio aislado. Para el producto, Core ya tiene modelo conceptual aprobado (ADR-005); quedan identidad, permisos y sesiones. El [roadmap](01-proyecto/roadmap.md) se actualiza en cada cambio.

## Cómo leerla

1. [Estado y gobierno](00-gobierno/estado-proyecto.md)
2. [Visión y alcance](01-proyecto/vision-y-alcance.md)
3. [Índice de decisiones](13-adrs/indice.md)
4. [Catálogo y estudio de módulos](12-modulos/README.md)
5. La sección especializada que corresponda al cambio.

## Estructura

| Ruta | Contenido |
| --- | --- |
| `00-gobierno/` | Estado, proceso de cambio y líneas base publicadas. |
| `01-proyecto/` | Visión, alcance, glosario y roadmap. |
| `02-requisitos/` | Requisitos funcionales y no funcionales, cuando se aprueben. |
| `03-arquitectura/` | Arquitectura conceptual, dominio y diagramas. |
| `04-datos/` | Modelo de datos, integridad y migraciones futuras. |
| `05-api/` | Convenciones y contratos de API futuros. |
| `06-frontend/` | Navegación, pantallas y accesibilidad. |
| `07-seguridad/` | Amenazas, controles, auditoría y recuperación. |
| `08-infraestructura/` | Despliegue, red, acceso remoto y operación. |
| `09-testing/` | Estrategia y trazabilidad de pruebas. |
| `10-ia/` | Contexto, límites y contratos para agentes de IA. |
| `11-operaciones/` | Runbooks, incidentes, backup y restauración. |
| `12-modulos/` | Estudio funcional de los módulos. |
| `13-adrs/` | Registro e índice de decisiones arquitectónicas. |
| `14-cambios/` | Registro de cambios relevantes. |

| `documentacion/` | Publicaciones DOCX/PDF y sus notas de contexto, separadas de la documentación Markdown operativa. |

Los Markdown históricos de `SPEC-INICIAL`, `ADR-001` y `ADR-002` se conservan como material fuente. Tanto esos archivos como sus DOCX/PDF están centralizados en `general-docs/fuentes/`. Ninguno de esos directorios es el lugar para crear documentación nueva.
