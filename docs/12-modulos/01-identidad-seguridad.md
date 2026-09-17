# Módulo 1 — Identidad y Seguridad — estudio inicial

## Estado

**Fase 1 iniciada.** Este documento formula una propuesta conceptual; no define un mecanismo de autenticación, cifrado ni tecnología concreta.

## Propósito

Determinar quién puede acceder al sistema, desde qué dispositivos y con qué nivel de privilegio, y ofrecer al resto de módulos un concepto común de identidad y autorización sin imponer una implementación técnica.

## Problema que resuelve

Sin un módulo propio, cada módulo (Tareas, Documentos, Finanzas, etc.) tendría que decidir por su cuenta quién puede leer o modificar sus datos, y el acceso desde la red local del usuario quedaría sin una política única de autenticación, cifrado y control. Esto generaría reglas inconsistentes y puntos de entrada sin auditar.

## Debe permitir

- Identificar de forma única a quien usa el sistema (el propio usuario, en el alcance actual de un solo usuario).
- Autorizar el acceso desde dispositivos de la red local, con un mecanismo de descubrimiento y verificación aún por diseñar.
- Emitir la información de identidad y permisos que Core necesita para su concepto de `Actor/Identidad` y para el registro de auditoría.
- Distinguir niveles de confianza o alcance de acceso si en el futuro hay más de un actor (multiusuario) o canales adicionales (móvil, voz, agentes de IA).
- Revocar o expirar el acceso de un dispositivo o sesión.

## No debe hacer

- No elegir todavía la tecnología de autenticación, cifrado ni almacenamiento de credenciales.
- No sustituir la lógica de permisos específica de cada módulo funcional; solo ofrece la identidad y el marco de autorización sobre el que esos módulos deciden sus propias reglas.
- No implementar acceso remoto fuera de la red local: ese mecanismo sigue pendiente de diseño según `estado-proyecto.md`.
- No asumir todavía un escenario multiusuario: el MVP es de un solo usuario.

## Entidades y relaciones — propuesta inicial

Como conceptos, no como tablas: `Identidad` (quién es el actor), `Credencial` (cómo se verifica esa identidad, sin definir su forma técnica), `Sesión/Dispositivo autorizado` (desde dónde se accede) y `Permiso/Alcance` (qué puede hacer esa identidad). Una `Identidad` se relaciona con Core a través del concepto `Actor/Identidad`, y cada acción sujeta a autorización debe poder trazarse hasta una identidad y, cuando aplique, hasta un dispositivo o sesión concretos.

## Dependencias

Identidad y Seguridad depende de los conceptos transversales de Core (`Actor/Identidad`, `Evento interno`, `Registro de auditoría`) pero no de una tecnología, framework de autenticación ni proveedor externo concreto. Los módulos funcionales dependerán de este módulo para saber quién actúa y con qué permiso, sin necesidad de reimplementar su propia verificación de identidad.

## Seguridad y automatizaciones

Este módulo es, por definición, el núcleo de seguridad del producto: toda operación sensible debería poder apoyarse en él para autorizar y auditar. Debe definir, a nivel conceptual, qué constituye un intento de acceso no autorizado y cómo se registra, sin implementar todavía la detección ni la respuesta automática. Las automatizaciones de otros módulos deberán ejecutarse siempre dentro del alcance de permisos de la identidad que las originó.

## MVP y futuro

**MVP propuesto:** una identidad de usuario único, un mecanismo mínimo de verificación de acceso desde la red local, sesiones o dispositivos autorizados con posibilidad de revocación, y trazabilidad básica de accesos.
**Futuro:** soporte multiusuario, permisos granulares por módulo o por dato, acceso remoto fuera de la red local, autenticación para canales adicionales (móvil, voz, agentes de IA) e integración con proveedores externos de identidad si se decide en su momento.

## Decisiones pendientes

- Mecanismo concreto de autenticación (credenciales propias, proveedor externo, biometría del dispositivo, etc.).
- Forma de cifrado de credenciales y de los datos en tránsito dentro de la red local.
- Mecanismo de descubrimiento y verificación de dispositivos en la red local.
- Modelo de sesiones: duración, expiración, revocación y renovación.
- Si el registro de auditoría de accesos vive en este módulo o se apoya enteramente en el concepto de Core.
- Alcance mínimo de permisos en el MVP, dado que hay un único usuario.
