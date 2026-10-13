# Arquitectura

La arquitectura concreta está pendiente. La separación conceptual ya acordada es: clientes -> API/servicios -> Core/lógica de negocio -> persistencia, con integraciones externas desacopladas.

La [propuesta del modelo de Core](propuesta-modelo-core.md) se conserva como documento de origen de [ADR-005](../13-adrs/ADR-005-modelo-core.md), que formaliza el modelo conceptual aprobado. Los documentos de esta área se mantienen directamente en `docs/03-arquitectura/`, sin repetir esa carpeta dentro de sí misma.

La [propuesta de identidad, permisos y sesiones](propuesta-identidad-permisos.md) conserva su carácter de propuesta; si se acuerda, se formalizará como ADR-006. La revisión y continuación se consultan en el [seguimiento del roadmap](../01-proyecto/roadmap.md#seguimiento-de-identidad-permisos-y-sesiones).
