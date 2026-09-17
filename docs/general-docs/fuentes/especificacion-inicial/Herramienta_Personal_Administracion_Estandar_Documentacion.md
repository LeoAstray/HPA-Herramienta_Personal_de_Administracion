# Herramienta Personal de Administración — Estándar de documentación

## A. Instrucciones compactas para Configuración del proyecto

ESTÁNDAR DE DOCUMENTACIÓN — HERRAMIENTA PERSONAL DE ADMINISTRACIÓN

La documentación es parte del sistema: todo cambio relevante se documenta antes/durante y se sincroniza con código. Explicar QUÉ, POR QUÉ y CÓMO, sin asumir contexto. Distinguir estado actual/objetivo, propuesta/decisión/pendiente. Registrar decisiones y, si cambian, qué sustituyen y por qué.

1. PROYECTO: visión, problema, necesidades incluidas/excluidas, usuarios, objetivos, alcance, funciones actuales/futuras/descartadas, estado, próximos objetivos y glosario.
2. REQUISITOS: RF/RNF. Cada RF: ID, nombre, descripción, justificación, actor, precondiciones, flujos, resultado, reglas, dependencias y estado. RNF: seguridad, rendimiento, disponibilidad, recuperación/backups, mantenibilidad, modularidad y escalabilidad.
3. ARQUITECTURA: arquitectura, componentes/responsabilidades, comunicaciones, dependencias, datos, límites de confianza y externos. Priorizar seguridad, privacidad, mínimo privilegio, modularidad, bajo acoplamiento, alta cohesión, mantenibilidad, fiabilidad, recuperación y evolución.
4. DIAGRAMAS: usar cuando aporten claridad: UML (casos de uso, clases, secuencia, estados, actividad, componentes, despliegue), ERD, datos/red, autenticación/autorización y navegación UI. Preferir Mermaid/PlantUML/editables.
5. DATOS: por entidad, propósito, campos, tipos, obligatoriedad, defaults, restricciones, índices, relaciones e integridad; ERD, migraciones, versionado, seeds, backups y restauración.
6. API: método, URL, autenticación, parámetros, body, respuestas, códigos, errores, permisos y ejemplos; naming, versionado, errores, paginación, filtros, ordenación y validación. OpenAPI/Swagger cuando proceda.
7. FRONTEND: pantallas, navegación, componentes, estados, formularios, validaciones, errores, carga, vacíos, responsive, accesibilidad y convenciones visuales; wireframes/mockups cuando ayuden.
8. SEGURIDAD: modelo de amenazas/superficie de ataque; autenticación, autorización, sesiones, secretos, cifrado, auditoría/logs, mínimo privilegio, acceso remoto, dependencias, backups/restauración y recuperación. No sacrificar seguridad por comodidad sin documentar riesgo, alternativas y decisión.
9. DESPLIEGUE/INFRA: local/remoto, exposición, red privada, DNS, HTTPS/TLS, certificados, firewall, reverse proxy, VPN/túneles, SO, contenedores, servicios, puertos, volúmenes, variables, secretos, monitorización y logs. Documentar instalación, configuración, inicio, parada, actualización y reconstrucción desde cero.
10. CÓDIGO: estructura, responsabilidades, arquitectura, naming, formato/linting, dependencias, entornos, Git, ramas, commits, versionado y revisión. Explicar decisiones no evidentes.
11. TESTING: unit, integración, API, E2E, seguridad y regresión según proceda; ejecución, cobertura, pruebas obligatorias/manuales/automatizadas y riesgos no cubiertos. Trazabilidad: requisito→test→resultado.
12. AUTOMATIZACIONES: ID, propósito, disparador/frecuencia, condiciones, datos, acciones, permisos, dependencias, resultado, errores, reintentos, logs y notificaciones; identificar creación/modificación/eliminación de datos y controles.
13. IA/AGENTES: contemplar IA/Codex desde el diseño. Documentar agentes, responsabilidades, datos, acciones, permisos, autenticación, aislamiento, comunicación, validación, revocación, fallos y trazabilidad. Mínimo privilegio; separar núcleo/datos/API/automatizaciones/agentes/externos. Agentes sustituibles/desactivables sin reconstruir núcleo; registrar agente, fecha, datos, acción solicitada/ejecutada y resultado.
14. ADR: toda decisión técnica/arquitectónica importante: ID, título, fecha, estado, contexto, problema, opciones, decisión, motivos, consecuencias y alternativas descartadas.
15. CAMBIOS: ID, objetivo, motivación, descripción, requisitos/componentes, arquitectura, BD, API, frontend, seguridad, dependencias, tests, migraciones, despliegue, rollback, impacto y estado.
16. TRAZABILIDAD: mantener cuando sea razonable requisito→diseño→ADR→Asana→implementación→test→documentación.
17. OPERACIONES/INCIDENCIAS: runbooks para arranque, parada, reinicio, actualización, migraciones, backup/restauración, logs, monitorización, diagnóstico y recuperación. Incidencias relevantes: RCA (qué, cuándo, impacto, causa raíz, factores, solución y prevención).
18. DEPENDENCIAS/INVENTARIO: documentar proveedor, propósito, datos, autenticación, permisos, criticidad, disponibilidad, alternativas y contingencia de externos. Inventariar componentes, servicios, BD, APIs, dependencias, dominios, certificados, integraciones, automatizaciones, agentes y configuración. Nunca guardar secretos reales.
19. MÓDULOS/ROADMAP: módulos complejos: propósito, funciones, requisitos, datos, API, relaciones, reglas, seguridad, automatizaciones, tests, limitaciones y evolución. Separar actual/desarrollo/planificado/propuesto/ideas/deuda/descartado.
20. CAMBIO/EVOLUCIÓN: antes de cambios relevantes comprobar problema/objetivo, requisitos, componentes, decisión/alternativas, arquitectura, datos/API/UI, seguridad, dependencias, tests, despliegue, rollback, documentación y Asana. Si una decisión queda obsoleta, registrar la nueva y actualizar arquitectura, requisitos, diagramas, tareas y documentación, conservando historial cuando proceda.
21. RELACIÓN: ChatGPT=análisis/diseño/planificación/documentación; documentación=fuente de verdad; Asana=tareas/prioridades/dependencias/estado; código=implementación. Flujo: ChatGPT→diseño→docs→Asana→código→tests→docs actualizada.

REGLA FUNDAMENTAL: toda funcionalidad/cambio relevante debe explicar qué, por qué, cómo, impacto, dependencias, riesgos, pruebas, despliegue, mantenimiento y rollback, de forma comprensible para alguien sin contexto previo.


---

## B. Documentación de referencia completa para el proyecto y agentes

# Estándar de documentación — Herramienta Personal de Administración

## 0. Propósito

Este documento define el estándar interno de documentación del proyecto. Su objetivo es que cualquier persona pueda comprender, mantener, modificar y evolucionar el sistema sin depender del contexto de conversaciones anteriores.

La documentación forma parte del producto y debe evolucionar junto con el código.

---

## 1. Principios generales

- Todo cambio relevante debe documentarse antes o durante su implementación.
- Explicar siempre qué se hace, por qué se hace y cómo funciona.
- Documentar decisiones técnicas, no únicamente resultados.
- No asumir conocimientos previos.
- Mantener documentación y código sincronizados.
- Cuando cambie una decisión, documentar la nueva decisión y, cuando proceda, qué sustituye y por qué.
- Distinguir siempre:
  - Estado actual.
  - Estado objetivo.
  - Propuesta.
  - Decisión tomada.
  - Pendiente de decidir.
- Toda funcionalidad nueva debe indicar dependencias, impacto y riesgos.
- Las decisiones arquitectónicas importantes deben conservar su contexto histórico.

## 2. Documentación general del proyecto

Debe existir una documentación inicial que explique:

### Descripción general
- Qué es la Herramienta Personal de Administración.
- Qué problema resuelve.
- Qué necesidades cubre.
- Qué queda fuera.
- Usuarios previstos.
- Objetivos.

### Alcance
- Funcionalidades incluidas.
- Futuras.
- Explícitamente descartadas.

### Estado
- Fase actual.
- Implementado.
- En desarrollo.
- Próximos objetivos.

### Glosario
- Términos propios.
- Abreviaturas.
- Conceptos técnicos.

## 3. Requisitos funcionales

Los requisitos deben describir qué hace el sistema independientemente de la implementación.

Cada requisito debe contener:
- ID único.
- Nombre.
- Descripción.
- Justificación.
- Actor.
- Precondiciones.
- Flujo principal.
- Flujos alternativos.
- Resultado esperado.
- Reglas de negocio.
- Dependencias.
- Estado.

Ejemplo:

> RF-001 — Gestión de tareas  
> El sistema permite crear, modificar, completar y eliminar tareas.  
> Actor: usuario propietario.  
> Precondición: usuario autenticado.  
> Resultado: tarea almacenada.

## 4. Requisitos no funcionales

Documentar explícitamente:

### Seguridad
Autenticación, autorización, sesiones, cifrado, secretos, ataques comunes, acceso remoto, mínimo privilegio y auditoría.

### Rendimiento
Tiempos esperados, usuarios/dispositivos previstos, volumen de datos y operaciones críticas.

### Disponibilidad
Fallos, recuperación, backups y restauración.

### Mantenibilidad
Estructura, convenciones, modularidad y sustitución de componentes.

### Escalabilidad
Qué puede crecer y qué está diseñado específicamente para uso personal.

## 5. Arquitectura

Documentar:
- Arquitectura general.
- Componentes.
- Responsabilidades.
- Comunicación.
- Dependencias.
- Flujos de datos.
- Límites de confianza.
- Sistemas externos.

Debe existir un diagrama de arquitectura general y evolucionar con el sistema.

## 6. UML y diagramas

Usar diagramas cuando aporten claridad, no por obligación.

### Casos de uso
Qué puede hacer cada actor.

### Clases
Entidades y relaciones importantes.

### Secuencia
Interacciones relevantes, por ejemplo login, creación de tareas, eventos, automatizaciones y agentes IA.

### Estados
Objetos con ciclos de vida importantes.

### Actividad
Procesos complejos.

### Componentes
Módulos y dependencias.

### Despliegue
Infraestructura, red, aplicación, BD y servicios externos.

### Otros
- ERD.
- Flujos de datos.
- Autenticación/autorización.
- Red.
- Navegación de UI.

Preferir Mermaid/PlantUML u otros formatos reproducibles/editables frente a imágenes estáticas.

## 7. Modelo de datos

Para cada entidad:
- Nombre.
- Propósito.
- Campos.
- Tipos.
- Obligatorio/opcional.
- Default.
- Restricciones.
- Índices.
- Relaciones.
- Integridad.

Además:
- ERD.
- Migraciones.
- Versionado.
- Seeds.
- Backups.
- Restauración.

## 8. API y contratos

Para cada endpoint:
- Método.
- URL.
- Autenticación.
- Parámetros.
- Body.
- Respuesta.
- Códigos HTTP.
- Errores.
- Permisos.
- Ejemplos.

También:
- Naming.
- Versionado.
- Formato de errores.
- Paginación.
- Filtros.
- Ordenación.
- Validaciones.

Usar OpenAPI/Swagger cuando sea apropiado.

## 9. Frontend

Documentar:
- Pantallas.
- Navegación.
- Componentes.
- Responsabilidades.
- Estados.
- Formularios.
- Validaciones.
- Errores.
- Carga.
- Estados vacíos.
- Responsive.
- Accesibilidad.
- Convenciones visuales.

Utilizar wireframes, mockups o diagramas de navegación cuando aporten valor.

## 10. Seguridad

Mantener una sección independiente.

### Modelo de amenazas
Qué protegemos, frente a qué amenazas y con qué impacto.

### Superficie de ataque
Frontend, backend, API, BD, red, acceso remoto, dispositivos, externos, automatizaciones y IA.

### Autenticación y autorización
Método, credenciales, sesiones, roles, permisos y mínimo privilegio.

### Secretos
Ubicación, uso, rotación y prohibición de valores reales en código/repositorio.

### Cifrado
Datos en tránsito, almacenados, certificados y claves.

### Auditoría
Acciones, información registrada, retención y acceso.

### Recuperación
Backups, restauración e incidentes.

Nunca sacrificar seguridad por comodidad sin documentar riesgo, alternativas y decisión.

## 11. Acceso remoto y despliegue

Documentar:
- Ubicación de componentes.
- Acceso local/remoto.
- Exposición a Internet.
- Red privada.
- DNS.
- HTTPS/TLS.
- Certificados.
- Firewall.
- Reverse proxy.
- VPN/túnel.
- Autenticación.
- Actualizaciones.
- Recuperación.

Debe existir un diagrama de despliegue.

## 12. Infraestructura

Documentar:
- Máquina/servidor.
- SO.
- Contenedores.
- Servicios.
- Red y puertos.
- Volúmenes.
- BD.
- Backups.
- Monitorización.
- Logs.
- Variables.
- Configuración.
- Secretos.
- Dependencias.

Debe existir un procedimiento para instalar, configurar, iniciar, detener, actualizar y reconstruir el entorno desde cero.

## 13. Código y desarrollo

Documentar:
- Estructura de carpetas.
- Responsabilidades.
- Arquitectura.
- Separación de responsabilidades.
- Naming.
- Formato.
- Linting.
- Dependencias.
- Configuración por entorno.
- Git.
- Ramas.
- Commits.
- Versionado.
- Revisión de código.

Explicar decisiones estructurales no evidentes.

## 14. Testing

Definir estrategia de:
- Unit.
- Integración.
- API.
- E2E.
- Seguridad.
- Regresión.

Documentar ejecución, cobertura esperada, pruebas obligatorias, manuales, automatizadas y riesgos no cubiertos.

Mantener trazabilidad:

`Requisito → Caso de prueba → Resultado esperado → Resultado obtenido`

## 15. Automatizaciones

Para cada automatización:
- ID.
- Propósito.
- Disparador/frecuencia.
- Condiciones.
- Datos.
- Acciones.
- Permisos.
- Dependencias.
- Resultado.
- Errores.
- Reintentos.
- Logs.
- Notificaciones.

Indicar expresamente acciones que creen, modifiquen o eliminen información.

## 16. IA y agentes

La futura integración de IA/Codex debe contemplarse desde el diseño.

Documentar:
- Agentes.
- Responsabilidades.
- Datos accesibles.
- Acciones.
- Permisos.
- Autenticación.
- Aislamiento.
- Comunicación.
- Validación de acciones sensibles.
- Revocación.
- Fallos.
- Trazabilidad.

Aplicar mínimo privilegio.

Separar:
- Núcleo.
- Datos.
- API.
- Automatizaciones.
- Agentes.
- Servicios externos.

Un agente debe poder sustituirse, desactivarse o eliminarse sin reconstruir el núcleo.

Registrar:
- Agente.
- Fecha/hora.
- Datos utilizados.
- Acción solicitada.
- Acción ejecutada.
- Resultado.

## 17. ADR

Las decisiones arquitectónicas/técnicas importantes deben registrarse como Architecture Decision Records.

Formato recomendado:

```text
ADR-XXX — Título

Fecha:
Estado:

Contexto:
Problema:

Opciones:
- A
- B
- C

Decisión:

Motivos:

Consecuencias:

Alternativas descartadas:

Sustituye a:
```

Usar ADR para framework, BD, autenticación, acceso remoto, despliegue, IA, backups y otras decisiones relevantes.

## 18. Documentación de cambios

Todo cambio relevante debe documentar:
- ID.
- Objetivo.
- Motivación.
- Descripción.
- Requisitos afectados.
- Componentes.
- Arquitectura.
- BD.
- API.
- Frontend.
- Seguridad.
- Dependencias.
- Tests.
- Migraciones.
- Despliegue.
- Rollback.
- Impacto.
- Estado.

## 19. Trazabilidad

Mantener, cuando sea razonable:

`Requisito → Diseño → ADR → Asana → Implementación → Test → Documentación`

Debe poder determinarse qué partes del sistema están afectadas por un cambio de requisito.

## 20. Operaciones y mantenimiento

Documentar:
- Arranque.
- Parada.
- Reinicio.
- Actualización.
- Migraciones.
- Backups.
- Restauración.
- Logs.
- Monitorización.
- Diagnóstico.
- Limpieza.
- Recuperación.

Crear Runbooks paso a paso.

## 21. Incidencias y RCA

Documentar:
- Detección.
- Logs.
- Reproducción.
- Clasificación.
- Impacto.
- Solución.
- Verificación.

Para incidencias relevantes usar Root Cause Analysis:

- Qué ocurrió.
- Cuándo.
- Impacto.
- Causa raíz.
- Factores contribuyentes.
- Solución.
- Prevención.
- Documentación afectada.

## 22. Dependencias externas

Para cada servicio externo:
- Nombre/proveedor.
- Propósito.
- Datos enviados/recibidos.
- Autenticación.
- Permisos.
- Criticidad.
- Disponibilidad.
- Alternativas.
- Contingencia.

Evaluar seguridad, privacidad, disponibilidad, coste y mantenimiento antes de introducir dependencias importantes.

## 23. Inventario

Mantener inventario de:
- Componentes.
- Servicios.
- BD.
- APIs.
- Dependencias.
- Dominios.
- Certificados.
- Integraciones.
- Automatizaciones.
- Agentes.
- Configuración.

Nunca guardar valores reales de secretos en la documentación.

## 24. Roadmap

Separar:
- Actual.
- En desarrollo.
- Planificado.
- Propuesto.
- Ideas.
- Deuda técnica.
- Mejoras.
- Descartado.

No tratar una propuesta como decisión.

## 25. Documentación por módulo

Para cada módulo complejo:
1. Propósito.
2. Funciones.
3. Requisitos.
4. Datos.
5. API.
6. Relaciones.
7. Reglas de negocio.
8. Seguridad.
9. Automatizaciones.
10. Tests.
11. Limitaciones.
12. Evolución.

## 26. Estructura documental

Estructura recomendada:

```text
docs/
├── 00-proyecto/
├── 01-requisitos/
├── 02-arquitectura/
├── 03-datos/
├── 04-api/
├── 05-frontend/
├── 06-seguridad/
├── 07-infraestructura/
├── 08-testing/
├── 09-automatizaciones/
├── 10-ia/
├── 11-operaciones/
├── 12-modulos/
├── 13-adrs/
├── 14-cambios/
└── 15-roadmap/
```

No es obligatorio crear todo desde el primer día; la estructura sirve como estándar de crecimiento.

## 27. Proceso obligatorio de cambio

Antes de implementar un cambio relevante comprobar:

1. Problema.
2. Objetivo.
3. Requisitos afectados.
4. Componentes afectados.
5. Decisión y alternativas.
6. Arquitectura.
7. BD.
8. API.
9. Frontend.
10. Seguridad.
11. Dependencias.
12. Tests.
13. Despliegue.
14. Rollback.
15. Documentación.
16. Tarea Asana.

## 28. Cambios de decisiones

Si una decisión anterior deja de ser adecuada:
- Identificarla.
- Explicar el problema.
- Analizar alternativas.
- Registrar nueva decisión.
- Actualizar arquitectura.
- Actualizar requisitos.
- Actualizar diagramas.
- Actualizar Asana.
- Mantener historial cuando sea relevante.

Nunca ocultar ni mantener artificialmente una decisión obsoleta.

## 29. Principios de diseño

Priorizar:
- Seguridad.
- Privacidad.
- Mínimo privilegio.
- Mantenibilidad.
- Modularidad.
- Simplicidad.
- Trazabilidad.
- Fiabilidad.
- Recuperación.
- Evolución.
- Separación de responsabilidades.
- Bajo acoplamiento.
- Alta cohesión.

No añadir complejidad innecesaria, pero tampoco bloquear innecesariamente la evolución futura.

## 30. Relación ChatGPT, documentación, Asana y código

**ChatGPT:** análisis, investigación, diseño, planificación y documentación.

**Documentación:** fuente de verdad técnica sobre funcionamiento y decisiones.

**Asana:** tareas, prioridades, dependencias y estado del trabajo.

**Código:** implementación real.

Flujo:

`ChatGPT → Diseño/planificación → Documentación → Asana → Código → Tests → Documentación actualizada`

Después de cada cambio relevante, actualizar código, tests, documentación y Asana.

## 31. Regla fundamental

Toda funcionalidad, cambio arquitectónico o modificación relevante debe responder documentalmente:

- Qué hacemos.
- Por qué.
- Cómo funciona.
- Qué afecta.
- Qué dependencias tiene.
- Qué riesgos introduce.
- Cómo se prueba.
- Cómo se despliega.
- Cómo se mantiene.
- Cómo se revierte.

La documentación debe permitir que una persona sin contexto previo comprenda y continúe el proyecto.

