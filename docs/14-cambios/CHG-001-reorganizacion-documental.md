# CHG-001 — Reorganización documental y base para agentes

## Estado

Documentado y aplicado en la documentación. No afecta a código de producto.

## Objetivo y motivación

Convertir la documentación inicial dispersa en una estructura navegable, preservar la trazabilidad de decisiones y ofrecer contexto suficiente a futuros agentes de IA.

## Alcance

Se crea un índice documental, secciones por disciplina, contexto y contrato de agentes, y la base de Fase 1 con el estudio inicial de Core. Los documentos fuente originales se conservan.

## Impacto

No hay cambios de arquitectura técnica, datos, API, interfaz, infraestructura ni implementación. No se toma ninguna decisión nueva de producto.

## Seguridad

Las instrucciones para agentes exigen mínimo privilegio, ausencia de secretos y validación de acciones sensibles.

## Pruebas y rollback

La verificación consiste en revisar enlaces y consistencia de estados. El cambio es documental y reversible eliminando los nuevos archivos; no altera datos de producto.

## Documentación relacionada

`docs/README.md`, `AGENTS.md`, `docs/10-ia/`, `docs/12-modulos/`, ADR-001 y ADR-002.
