# Instrucciones para agentes

## Fuente de verdad y fase actual

La documentación Markdown bajo `docs/` es la fuente de verdad operativa. Los documentos DOCX/PDF son ediciones de lectura de las líneas base documentales; no sustituyen a Markdown.

El proyecto está en **definición y diseño**. No existe código de producto ni una arquitectura técnica aprobada. No implementar producción, elegir tecnologías ni presentar una propuesta como decisión sin autorización expresa.

## Orden de lectura obligatorio

1. `docs/README.md`
2. `docs/00-gobierno/estado-proyecto.md`
3. `docs/01-proyecto/vision-y-alcance.md`
4. `docs/13-adrs/indice.md`
5. El documento del módulo y área de arquitectura o seguridad que afecte al trabajo.

## Forma de trabajar

Para todo cambio relevante: análisis -> diseño -> documentación -> Asana -> implementación -> pruebas -> actualización de documentación. Distinguir siempre **estado actual**, **objetivo**, **propuesta**, **decisión**, **pendiente** y **descartado**.

Priorizar seguridad, privacidad, mínimo privilegio, modularidad, simplicidad, trazabilidad, recuperación y bajo acoplamiento. Nunca incluir secretos reales. Asana solo organiza el desarrollo: no es una dependencia del producto.

## Límites del alcance actual

La primera interfaz será web responsive para uso personal. Móvil, Siri/voz, agentes de IA e integraciones complejas son evoluciones futuras. La preparación arquitectónica no autoriza su implementación.

## Documentación que debe actualizarse

Cada cambio debe actualizar `docs/01-proyecto/roadmap.md`: registrar el avance, los pendientes y el siguiente paso, aunque no cambie el orden de los hitos. Esta actualización forma parte del cierre del trabajo.

Cada cambio relevante debe actualizar el documento del módulo afectado, requisitos/arquitectura/seguridad cuando proceda, ADR si decide algo relevante y el registro de cambios. Mantener Markdown como versión mantenible para personas y agentes. Guardar las ediciones DOCX/PDF y su contexto de publicación en `docs/documentacion/publicaciones/<YYYY-MM-DD_HH-mm-ss>-<nombre>/`, fuera de las áreas Markdown numeradas.

Los issues de GitHub se preparan como texto local para que el colaborador los publique manualmente. No acceder al remoto ni utilizar una sesión de GitHub sin una nueva petición expresa del colaborador.
