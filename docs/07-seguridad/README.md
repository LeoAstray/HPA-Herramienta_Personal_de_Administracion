# Seguridad

La seguridad es un requisito transversal desde el diseño. El MVP debe permitir acceso desde dispositivos de la red local del usuario, por lo que autenticación, autorización, sesiones, cifrado en tránsito, segmentación de red, secretos, auditoría y revocación deben definirse antes de implementar la conectividad.

No está autorizado exponer el servicio a Internet; el acceso remoto fuera de la red local sigue pendiente de una decisión técnica informada.

## Documentos y archivos

El módulo Documentos y Archivos solo podrá operar sobre rutas explícitamente autorizadas por el propietario. El acceso a un registro lógico no supone acceso ilimitado a su archivo físico ni a otras rutas. Crear, mover, renombrar, sobrescribir o eliminar archivos físicos requerirá una política explícita, confirmación aplicable, trazabilidad y una estrategia de recuperación antes de implementarse.

Los nombres, rutas, metadatos y contenidos de documentos pueden ser sensibles. Las notificaciones, registros de auditoría y futuras capacidades de búsqueda o previsualización deberán minimizar su exposición. No se ejecutará contenido de archivos no confiables desde este módulo.

## Evaluación de agentes de desarrollo

El [diseño EVAL-05](../10-ia/diseno-evaluacion-permisos-agentes.md) propone comprobar permisos sobre recursos sintéticos en un laboratorio desechable, sin checkout/metadatos de HPA, credenciales, datos personales ni acceso al remoto real. Distingue rechazo por instrucciones de denegación técnica y exige declarar canales no cubiertos. El evaluador debe quedar fuera del ámbito accesible al agente, o el aislamiento se registra como no verificable. Diseño preparado; controles no configurados ni probados. No modifica los contratos de ADR-004 ni define identidad, permisos o sesiones del producto.
