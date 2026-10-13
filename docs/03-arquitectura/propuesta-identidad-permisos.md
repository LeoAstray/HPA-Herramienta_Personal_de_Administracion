# Propuesta — Modelo de identidad, permisos y sesiones

## Estado

**Propuesta pendiente de revisión.** No es una decisión. Responde al bloque 1 de [decisiones transversales pendientes](../01-proyecto/decisiones-transversales-pendientes.md). Si ambos colaboradores la acuerdan, con o sin cambios, se formaliza como ADR-006 siguiendo el [proceso de cambio](../00-gobierno/proceso-de-cambio.md).

## Por qué ahora

[ADR-005](../13-adrs/ADR-005-modelo-core.md) dejó en Core el lugar donde aplicar la autorización, pero no decide quién puede hacer qué. Identidad y Seguridad (1), Configuración (2), Documentos y Archivos (5), Finanzas (9), IA / Agentes (14) y Backup y Recuperación (15) mantienen decisiones provisionales hasta resolverlo. [Seguridad](../07-seguridad/README.md) exige definir autenticación, autorización, sesiones, cifrado en tránsito, secretos, auditoría y revocación antes de implementar la conectividad.

## 1. Actores

**Propuesta:** un actor es quien origina una acción. Se distinguen cuatro tipos:

- **Propietario:** la persona usuaria del sistema (caso inicial de un único usuario).
- **Cliente o dispositivo autorizado:** actúa en nombre del propietario y solo mientras tenga una autorización vigente.
- **Automatización:** actúa siempre dentro del alcance del actor que originó el evento, como ya establece Automatizaciones (12).
- **Agente interno del producto (futuro):** solo opera mediante un contrato explícito; nunca hereda los privilegios del propietario.

`Actor/Identidad` pertenece por dueño natural a Identidad y Seguridad, según ADR-005. Los agentes de desarrollo de ADR-004 no son actores del producto y quedan fuera de esta propuesta.

## 2. Autenticación del propietario

**Propuesta:** credencial propia del propietario, creada en el primer arranque. El sistema conserva solo un derivado no reversible, nunca la credencial. En el MVP no hay proveedor externo de identidad: exigiría Integraciones y contradice el objetivo de ejecución local.

**Alternativa descartada:** confiar en la red local sin autenticar. Una red doméstica compartida no es una frontera de confianza, y ADR-002 prevé varios clientes. La técnica concreta de derivación es una decisión técnica posterior.

## 3. Dispositivos y clientes

**Propuesta:** cada cliente se autoriza de forma explícita. El propietario aprueba el emparejamiento desde una sesión ya autorizada o, en el primer uso, desde el propio equipo anfitrión. Tras la aprobación, el cliente recibe una credencial de dispositivo propia y revocable. El MVP no incluye descubrimiento automático en la red: el propietario indica la dirección del servicio. Reduce la superficie expuesta y encaja con que [infraestructura](../08-infraestructura/README.md) sigue pendiente. Revocar un dispositivo cierra sus sesiones.

## 4. Sesiones

**Propuesta:** toda sesión se asocia a un actor y a un dispositivo, con caducidad por inactividad y caducidad absoluta. Mientras no caduque la absoluta, se renueva sin reautenticar. Los valores por defecto se fijan en el diseño técnico y se alojan en Configuración como ajuste sensible. Se puede revocar una sesión concreta o cerrar todas. Cambiar la credencial invalida todas las sesiones.

## 5. Acciones sensibles

**Propuesta:** las acciones sensibles exigen una reautenticación reciente aunque la sesión sea válida. Lista inicial a confirmar: cambiar la credencial, autorizar o revocar dispositivos, crear o revocar una conexión de Integraciones, restaurar una copia de seguridad, cambiar rutas autorizadas de Documentos, borrar o exportar datos financieros en bloque y aprobar el contrato de un agente. Cada módulo declara cuáles de sus operaciones son sensibles; este módulo aplica la regla.

## 6. Autorización

**Propuesta:** denegar por defecto. Una única política responde a "¿puede este actor realizar esta acción sobre este recurso?". Vive en Identidad y Seguridad y se invoca a través de lo que Core expone (ADR-005, punto 5), de modo que ningún módulo implementa su propia verificación de identidad.

En el MVP el propietario tiene todos los permisos, pero toda comprobación pasa por la misma política. Así, multiusuario, canales como móvil o voz (ADR-002) y agentes internos se añaden sin reescribir módulos. Cada módulo conserva sus reglas de negocio; este módulo decide quién puede invocarlas.

## 7. Auditoría y avisos

**Propuesta:** sobre el registro mínimo de ADR-005 se auditan inicios de sesión correctos y fallidos, emparejamiento y revocación de dispositivos, cierre o revocación de sesiones, reautenticaciones y acciones denegadas. Ninguna credencial ni token aparece en eventos, auditoría o notificaciones. Los avisos de seguridad (dispositivo nuevo, intentos fallidos repetidos) se envían por Notificaciones y no se pueden desactivar. Su contenido es mínimo y no incluye detalle financiero ni de documentos.

## 8. Transporte y alcance de red

**Propuesta:** el cifrado en tránsito es obligatorio también dentro de la red local. El mecanismo (TLS, certificados locales, puertos) se decide en [infraestructura](../08-infraestructura/README.md). No se expone el servicio a Internet. El acceso remoto sigue fuera de alcance y requeriría su propia ADR.

## 9. Pérdida de la credencial

**Propuesta:** en el primer arranque se genera una clave de recuperación que el propietario guarda fuera del sistema. Usarla restablece la credencial y revoca todas las sesiones y dispositivos. El procedimiento se detalla junto con Backup y Recuperación (15).

**Alternativa descartada:** restablecer por correo o proveedor externo. Introduce dependencia de terceros y de Integraciones antes de que existan.

## Impacto si se aprueba

- ADR-006 y su registro de cambio; `docs/12-modulos/01-identidad-seguridad.md` pasa de decisiones abiertas a un modelo concreto.
- El bloque 1 de decisiones transversales queda resuelto y los permisos provisionales de los módulos 2, 5, 9, 14 y 15 pasan a apoyarse en esta política.
- Configuración (2) declara sus ajustes sensibles y Notificaciones (3) fija los avisos de seguridad como no desactivables.
- El roadmap cierra el ítem de identidad, permisos y sesiones; el siguiente paso es la arquitectura global.

## Qué no resuelve esta propuesta

- Técnica de derivación de la credencial, formato de token y almacenamiento de secretos.
- TLS, certificados, puertos y descubrimiento automático de servicio.
- Multiusuario, roles y permisos granulares por dato.
- Acceso remoto fuera de la red local y autenticación biométrica.

## Decisiones que ambos colaboradores deben confirmar

1. Si la reautenticación para acciones sensibles entra en el MVP o se pospone.
2. Si la clave de recuperación generada en el primer arranque es el mecanismo elegido.
3. Si el emparejamiento solo se aprueba desde una sesión autorizada o el equipo anfitrión, o se admite un código de un solo uso.
4. Si los avisos de seguridad no se pueden desactivar.
5. Si se confirma la lista inicial de acciones sensibles.

## Siguiente paso

Revisar esta propuesta entre ambos colaboradores. Si se acuerda, formalizarla como ADR-006 y actualizar los módulos y el bloque 1 de decisiones transversales.