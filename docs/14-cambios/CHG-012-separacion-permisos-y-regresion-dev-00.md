# CHG-012 — Separación de permisos y regresión de DEV-00

## Estado y alcance

Aplicado a Markdown operativo el 2026-09-30, por petición del colaborador de continuar tras aportar la regresión de DEV-00. Cambio documental; no configura agentes ejecutables ni modifica producto, arquitectura o permisos.

## Análisis y diseño

Las dos respuestas de R1 (CHG-011) mejoraron la identificación de pendientes, pero no superaron completamente los criterios: la ambigua trasladó límites del preparador al destinatario; la clara reescribió innecesariamente el encargo y añadió una prohibición de lectura. Se corrige el prompt antes de aumentar esfuerzo o evaluar otro modelo.

R2 distingue los permisos de ejecución de DEV-00 de las acciones del encargo original, diferencia archivos objeto de revisión y fuentes rectoras, y obliga a recomendar la original sin reescribirla cuando ya es suficiente. Se alinea el contrato documental y se registran los cuatro resultados sin afirmar consumo medido ni operaciones verificadas.

## Decisiones y pendientes

Se mantiene la selección provisional GPT-6 Luna / Low y los límites de ADR-004; no hay nueva decisión de permisos que requiera otro ADR. Falta repetir ambos casos con R2 antes de EVAL-01. No se crean tareas ni se escribe en Asana: la vinculación externa queda a cargo del equipo si procede.

## Verificación y recuperación

Comprobar formato del diff y enlaces locales. Estas comprobaciones no sustituyen la regresión del comportamiento de Luna / Low, que queda pendiente. No se ejecutan escrituras Git, cambios remotos, instalaciones ni llamadas API de pago. Un colaborador puede recuperar la versión anterior mediante Git.

## Documentación relacionada

- [Prompt R2](../10-ia/prompts/dev-00-preparar-peticion.md)
- [Contrato de desarrollo](../10-ia/agentes-desarrollo.md)
- [Evaluación y regresión R1](../10-ia/evaluacion-agentes-desarrollo.md)
- [Estado del proyecto](../00-gobierno/estado-proyecto.md)
- [ADR-004, sin cambio de permisos](../13-adrs/ADR-004-contratos-agentes-desarrollo.md)
