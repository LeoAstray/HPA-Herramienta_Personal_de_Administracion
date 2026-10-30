# Acuerdo — Identidad, permisos y sesiones

## Estado

**Registro abierto: ningún acuerdo registrado.** Este documento recoge la respuesta explícita de cada colaborador sobre las cinco decisiones de la [propuesta de identidad, permisos y sesiones](propuesta-identidad-permisos.md). Continúa el issue #42, cerrado con el alcance de redactar y revisar la propuesta. Primera entrega del issue #58 (ARQ-1).

Ninguna respuesta se infiere ni se atribuye por silencio. Una casilla sin respuesta significa que la decisión sigue pendiente.

## Versión de la propuesta

Se somete a acuerdo `docs/03-arquitectura/propuesta-identidad-permisos.md` con el blob Git `cef2671ef4def7b6033921c441b590d7e2e00eda`, en el estado en que CHG-033 es el último registro de cambio. Quien registre su respuesta debe comprobar antes con `git hash-object` que lee la misma versión y anotar cualquier diferencia. Como en [CHG-026](../14-cambios/CHG-026-revision-humana-identidad-permisos.md), es una versión local de referencia, no una identificación independiente de lo que cada persona haya leído.

## Revisión y acuerdo se registran por separado

**Revisión.** El 2026-10-13 el colaborador comunicó que ambos habían revisado la propuesta, y [CHG-026](../14-cambios/CHG-026-revision-humana-identidad-permisos.md) lo registró. Acredita la revisión, no el acuerdo sobre las cinco decisiones.

**Acuerdo.** No registrado. Se anotará una entrada fechada cuando ambos hayan respondido de forma explícita sobre la misma versión. Si falta una respuesta o hay discrepancia, esa decisión permanece pendiente.

## Cómo responder

Cada colaborador escribe su propia respuesta, con fecha, con una de estas fórmulas:

- **De acuerdo.**
- **De acuerdo con cambios:** indicar el cambio exacto.
- **En desacuerdo:** indicar el motivo y, si la hay, la alternativa.

Nadie rellena la respuesta de otra persona.

## Las cinco decisiones

### 1. Reautenticación para acciones sensibles

**La propuesta plantea:** si la reautenticación reciente para acciones sensibles entra en el MVP o se pospone. Propone exigirla aunque la sesión sea válida (sección 5).

| Colaborador | Respuesta y fecha |
| --- | --- |
| @iagolucasaran | **De acuerdo.** , 30/10/2026 |
| @LeoAstray | Sin respuesta registrada |

**Estado:** Pendiente.

### 2. Clave de recuperación

**La propuesta plantea:** si el mecanismo elegido es una clave de recuperación generada en el primer arranque y guardada por el propietario fuera del sistema. Usarla restablece la credencial y revoca todas las sesiones y dispositivos (sección 9).

| Colaborador | Respuesta y fecha |
| --- | --- |
| @iagolucasaran | **De acuerdo.** , 30/10/2026 |
| @LeoAstray | Sin respuesta registrada |

**Estado:** Pendiente.

### 3. Emparejamiento de dispositivos

**La propuesta plantea:** si el emparejamiento solo se aprueba desde una sesión ya autorizada o desde el equipo anfitrión, o se admite además un código de un solo uso (sección 3). Propone la primera opción y sin descubrimiento automático en el MVP.

| Colaborador | Respuesta y fecha |
| --- | --- |
| @iagolucasaran | **De acuerdo.** , 30/10/2026 |
| @LeoAstray | Sin respuesta registrada |

**Estado:** Pendiente.

### 4. Avisos de seguridad

**La propuesta plantea:** si los avisos de seguridad (dispositivo nuevo, intentos fallidos repetidos) se envían por Notificaciones sin posibilidad de desactivarlos (sección 7).

| Colaborador | Respuesta y fecha |
| --- | --- |
| @iagolucasaran | **De acuerdo.** , 30/10/2026 |
| @LeoAstray | Sin respuesta registrada |

**Estado:** Pendiente.

### 5. Lista inicial de acciones sensibles

**La propuesta plantea:** confirmar la lista inicial (sección 5): cambiar la credencial, autorizar o revocar dispositivos, crear o revocar una conexión de Integraciones, restaurar una copia de seguridad, cambiar rutas autorizadas de Documentos, borrar o exportar datos financieros en bloque y aprobar el contrato de un agente. Cada módulo declara después cuáles de sus operaciones son sensibles.

| Colaborador | Respuesta y fecha |
| --- | --- |
| @iagolucasaran | **De acuerdo.** , 30/10/2026 |
| @LeoAstray | Sin respuesta registrada |

**Estado:** Pendiente.

## Confirmación de la propuesta completa

Además de las cinco decisiones, cada colaborador indica si confirma el resto de la propuesta (actores, autenticación, sesiones, autorización, auditoría, transporte) tal como está o con cambios.

| Colaborador | Respuesta y fecha |
| --- | --- |
| @iagolucasaran | **De acuerdo.** , 30/10/2026 |
| @LeoAstray | Sin respuesta registrada |

## Cambios solicitados a la propuesta

| Sección | Cambio | Solicitado por | Estado |
| --- | --- | --- | --- |
| Ninguno registrado | | | |

## Discrepancias

Ninguna registrada. Cuando exista, se anotará aquí con la decisión afectada y quedará pendiente hasta que ambos la resuelvan por escrito.

## Después del acuerdo

Solo si ambos acuerdan, la integración coordinada, a cargo de un único integrador y en turno exclusivo, actualizaría:

- una ADR de identidad, numerada al integrar (ADR-006 es la referencia provisional de las fuentes, no una reserva);
- la propuesta de identidad y el [README de arquitectura](README.md), para reflejar que está formalizada;
- los módulos 1, 2, 3, 5, 9, 13, 14 y 15, y el documento de seguridad;
- el bloque 1 de decisiones transversales y el índice de ADR;
- el roadmap y un CHG nuevo, con el número asignado al integrar.

## Qué no hace este documento

No reabre #42, no atribuye aprobación por inferencia y no cambia ADR-005. No decide algoritmos, tokens, certificados ni puertos, ni implementa autenticación. Los detalles técnicos y el alcance futuro siguen pendientes. Ninguna excepción de permisos del producto se supone aprobada.