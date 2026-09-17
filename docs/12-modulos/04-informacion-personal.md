# Módulo 4 — Información Personal — estudio inicial

## Estado

**Fase 1 iniciada.** Este documento formula una propuesta conceptual; no define un esquema de datos concreto ni un formato de almacenamiento.

## Propósito

Definir dónde y cómo se guarda la información personal de base del usuario (datos de contacto, identificativos, datos relevantes de su vida que otros módulos pueden necesitar), como referencia común, sin que cada módulo funcional duplique esos datos por su cuenta.

## Problema que resuelve

Sin este módulo, datos como el nombre completo, contacto, direcciones o identificadores personales quedarían dispersos: Documentos podría guardar una copia, Finanzas otra, Estudios otra, sin una fuente única. Esto genera inconsistencia cuando un dato cambia y dificulta responder "¿qué sabe el sistema sobre mí?" de forma unificada.

## Debe permitir

- Mantener los datos personales de base del usuario en un único lugar de referencia (identificativos, contacto, datos relevantes que no pertenecen a otro módulo más específico).
- Permitir que otros módulos consulten esos datos por referencia en vez de duplicarlos (p. ej. Documentos podría referenciar el titular sin copiar su información personal completa).
- Permitir que el usuario revise y corrija su propia información personal.
- Distinguir datos de identidad básica (nombre, fecha de nacimiento) de datos de contacto o de otro tipo que puedan cambiar con más frecuencia.

## No debe hacer

- No sustituir a Identidad y Seguridad: este módulo guarda información descriptiva sobre la persona, no gestiona credenciales ni autenticación.
- No absorber datos que pertenecen claramente a otro módulo más específico (historial académico → Estudios; movimientos económicos → Finanzas), aunque pueda haber referencias cruzadas.
- No decidir todavía el nivel de detalle ni el esquema exacto de campos a almacenar.
- No implementar todavía exportación o portabilidad de datos, aunque es un requisito razonable a futuro.

## Entidades y relaciones — propuesta inicial

Como concepto central: `Perfil personal` (el conjunto de datos descriptivos del usuario), compuesto por subconjuntos como `Datos de identidad` y `Datos de contacto`. El `Perfil personal` se relaciona uno a uno con el `Actor/Identidad` de Core, y otros módulos pueden referenciarlo (no duplicarlo) cuando necesiten mostrar o usar ese dato.

## Dependencias

Información Personal depende de Core (`Actor/Identidad`) para saber a quién pertenece el perfil. Depende de Identidad y Seguridad para decidir quién puede leer o modificar cada campo, especialmente si en el futuro hay más de un actor. El resto de módulos dependen de este para no duplicar datos personales básicos, referenciándolo cuando lo necesiten.

## Seguridad y automatizaciones

Los datos personales de base suelen ser sensibles por naturaleza (identificativos, contacto), por lo que su acceso y modificación deberían quedar sujetos a los permisos de Identidad y Seguridad y, razonablemente, quedar registrados como evento auditable cuando cambian. Este módulo no define aún automatizaciones propias, aunque un cambio en el perfil personal podría disparar avisos a través de Notificaciones (p. ej. confirmar un cambio de datos de contacto).

## MVP y futuro

**MVP propuesto:** un conjunto mínimo de campos de identidad y contacto para el usuario único, editables por el propio usuario, sin historial de cambios.
**Futuro:** historial de cambios sobre el perfil, más de un perfil si el sistema pasa a ser multiusuario, exportación/portabilidad de los datos personales, y validaciones más estrictas de formato para ciertos campos (p. ej. email, teléfono).

## Decisiones pendientes

- Qué campos concretos forman parte del MVP del perfil personal.
- Si se guarda algún historial de cambios sobre estos datos desde el principio o se deja para el futuro.
- Cómo referencian otros módulos al perfil personal sin duplicar información (por identificador, por vínculo directo, etc.).
- Si algún campo del perfil requiere un nivel de protección distinto al resto (p. ej. datos más sensibles que el nombre de contacto).
