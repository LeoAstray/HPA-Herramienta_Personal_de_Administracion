# ADR-003 — Priorización del descubrimiento de IA y Agentes

## Estado

**Decisión.**

## Fecha

2026-09-28

## Contexto

El estudio funcional de los módulos está completo. El producto se desarrolla entre dos colaboradores. El propietario quiere evaluar de forma temprana qué agentes de IA pueden aumentar el rendimiento del equipo de desarrollo y del futuro producto, y qué modelos podrían servir a cada necesidad.

El producto no tiene todavía arquitectura técnica, modelo de dominio definitivo, autenticación, permisos, sesiones ni contrato de eventos de Core aprobados. Además, IA/Agentes, Integraciones y Automatizaciones no son funciones aprobadas del MVP.

## Problema

Posponer todo el análisis de agentes impediría valorar pronto su utilidad y sus restricciones. Implementarlos antes de definir casos de uso, datos, permisos y fronteras comunes introduciría acceso excesivo, dependencia de proveedor y retrabajo arquitectónico.

## Opciones consideradas

1. Mantener IA/Agentes completamente pospuesto hasta después de la arquitectura global.
2. Implementar agentes y elegir modelos ahora, antes de cerrar sus dependencias transversales.
3. Priorizar una fase de descubrimiento y diseño de IA/Agentes, sin implementar agentes ni elegir modelos todavía.

## Decisión

Se elige la opción 3. El siguiente objetivo del proyecto será el descubrimiento y diseño de IA/Agentes. Esta fase separará los agentes de desarrollo de los futuros agentes internos del producto e identificará casos de uso, agentes candidatos, criterios de evaluación de modelos, límites de datos y permisos, y las dependencias que deben resolverse.

No se aprueba con esta ADR ningún proveedor, modelo, orquestador, integración externa, credencial ni código de producto. Ningún agente accederá a datos del producto ni ejecutará operaciones del producto hasta que se cierren el contrato de Core y las decisiones de Identidad y Seguridad aplicables, y se apruebe explícitamente el primer caso de uso.

## Consecuencias

- IA/Agentes deja de ser solo una evolución futura de análisis y pasa a ser la prioridad documental inmediata.
- La investigación comparará alternativas con criterios de utilidad, calidad, coste, latencia, privacidad, operación local o externa, seguridad, mantenimiento y reversibilidad.
- Cada agente candidato deberá declarar responsabilidad, datos accesibles, acciones permitidas, confirmaciones y registro de actividad.
- Los agentes de desarrollo asistirán a los dos colaboradores y operarán con roles independientes de developer, reviewer, tester, documentación y coordinación; no obtendrán por ello acceso a datos del producto.
- La arquitectura y los requisitos posteriores incorporarán únicamente los agentes aprobados, no una plataforma genérica de IA sin necesidad demostrada.
- Las decisiones de Core e Identidad y Seguridad siguen siendo prerrequisitos de implementación, no obstáculos que esta ADR elimine.

## Alternativas descartadas

- **Posponer todo el análisis:** rechazada porque no responde a la prioridad actual del propietario de evaluar el valor de los agentes.
- **Implementar primero:** rechazada porque el proyecto carece de las fronteras de seguridad y dominio necesarias para hacerlo de forma controlada.

## Documentación afectada

- `docs/01-proyecto/roadmap.md`
- `docs/00-gobierno/estado-proyecto.md`
- `docs/10-ia/`
- `docs/12-modulos/14-ia-agentes.md`
- `docs/13-adrs/indice.md`

