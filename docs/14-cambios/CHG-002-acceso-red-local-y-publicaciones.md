# CHG-002 — Acceso de MVP por red local y organización de publicaciones

## Estado

Documentado y aplicado a la estructura documental. No afecta a código de producto.

## Decisión de alcance

El MVP deberá ser accesible desde dispositivos de la red local del usuario. Esta decisión no aprueba todavía una tecnología, protocolo, puerto, esquema de autenticación ni mecanismo de descubrimiento.

## Impacto y pendientes

Identidad y Seguridad e Infraestructura deberán definir controles adecuados antes de implementar conectividad. La exposición a Internet sigue fuera del alcance actual.

## Organización documental

Las ediciones consolidadas DOCX/PDF se guardarán en `docs/documentacion/publicaciones/<YYYY-MM-DD_HH-mm-ss>-<nombre>/`, acompañadas de los archivos necesarios para reproducirlas.

## Seguridad y rollback

No se modifican sistemas ni datos. El cambio de alcance es reversible mediante una decisión posterior documentada; cualquier cambio de tecnología requerirá análisis, diseño y, si procede, un ADR.
