# Módulo 2 — Configuración — estudio inicial

## Estado

**Fase 1 iniciada.** Este documento formula una propuesta conceptual; no define un formato de almacenamiento, esquema técnico ni interfaz concreta.

## Propósito

Definir dónde y cómo se gestionan las preferencias y parámetros que afectan al comportamiento del sistema y de sus módulos, de forma centralizada, sin que cada módulo tenga que inventar su propio mecanismo de configuración.

## Problema que resuelve

Sin un módulo de Configuración, cada módulo (Notificaciones, Calendario, IA/Agentes, etc.) definiría sus propios ajustes de forma aislada, generando duplicación, inconsistencia en cómo se guardan y exponen las preferencias, y dificultad para que el usuario tenga una visión única de qué puede ajustar en el sistema.

## Debe permitir

- Centralizar las preferencias globales del usuario (idioma, formato de fecha/hora, zona horaria, tema u otras opciones de carácter general).
- Ofrecer a cada módulo funcional un lugar donde declarar y almacenar sus propios ajustes, sin obligarlo a construir su propio sistema de configuración.
- Distinguir entre valores por defecto del sistema y valores personalizados por el usuario.
- Consultar y modificar configuración de forma consistente desde cualquier módulo o interfaz.
- Reflejar cambios de configuración de forma que otros módulos puedan reaccionar a ellos (p. ej. un cambio de idioma afecta a Notificaciones).

## No debe hacer

- No almacenar datos de negocio de otros módulos (tareas, documentos, finanzas): solo sus parámetros de comportamiento.
- No decidir todavía el mecanismo técnico de persistencia ni el formato de los valores de configuración.
- No gestionar identidad ni permisos: eso corresponde a Identidad y Seguridad, aunque Configuración pueda tener ajustes visibles solo para ciertos niveles de acceso.
- No implementar todavía sincronización entre dispositivos si en el futuro hay más de un cliente (móvil, voz).

## Entidades y relaciones — propuesta inicial

Como conceptos: `Ajuste` (una preferencia concreta, con una clave y un valor), `Ámbito` (si el ajuste es global del sistema o específico de un módulo) y `Valor por defecto` frente a `Valor personalizado`. Cada `Ajuste` se relaciona con el `Actor/Identidad` de Core cuando es una preferencia personal del usuario, y con el módulo correspondiente cuando es un parámetro de comportamiento de ese módulo.

## Dependencias

Configuración depende de los conceptos transversales de Core (`Actor/Identidad`, `Evento interno`) para saber de quién es una preferencia y para notificar cambios. Depende de Identidad y Seguridad para decidir quién puede leer o modificar determinados ajustes. El resto de módulos funcionales dependerán de Configuración para almacenar y consultar sus propios parámetros, en vez de definir un mecanismo propio.

## Seguridad y automatizaciones

Algunos ajustes pueden ser sensibles (por ejemplo, los relacionados con notificaciones de seguridad o con integraciones externas), por lo que su modificación debería quedar sujeta a los permisos definidos por Identidad y Seguridad y, si procede, registrada como evento auditable. Los cambios de configuración pueden disparar automatizaciones en otros módulos (p. ej. cambiar el idioma reconfigura las plantillas de Notificaciones), pero este módulo no define aún ese mecanismo de propagación.

## MVP y futuro

**MVP propuesto:** un conjunto reducido de ajustes globales (idioma, zona horaria, formato de fecha) y un mecanismo simple para que un módulo declare y lea sus propios ajustes con un valor por defecto.
**Futuro:** perfiles de configuración, ajustes por dispositivo o canal, sincronización entre clientes, historial de cambios de configuración y ajustes con distintos niveles de visibilidad según permisos.

## Decisiones pendientes

- Formato y lugar de almacenamiento de los ajustes (archivo, base de datos, u otro).
- Si existirá un esquema o validación formal para los ajustes que declara cada módulo.
- Cómo se notifica a un módulo que uno de sus ajustes ha cambiado.
- Qué ajustes se consideran sensibles y qué nivel de permiso exige modificarlos.
- Si en el MVP de un solo usuario tiene sentido distinguir "valor por defecto del sistema" de "valor personalizado", o si se simplifica hasta que haya más de un actor.
