# IA y agentes

Esta carpeta distingue dos familias de agentes: los futuros agentes internos del producto HPA y los agentes que ayudan al equipo a desarrollar el código. Conforme a ADR-003, su descubrimiento y diseño es la prioridad inmediata. Ninguna de las dos familias queda implementada o aprobada solo por esta documentación.

El descubrimiento debe producir, antes de cualquier implementación, casos de uso priorizados, un inventario de agentes candidatos, criterios para evaluar modelos, límites de datos y permisos, y una decisión explícita de qué agente —si alguno— se implementará primero.

Leer primero [contexto-agentes.md](contexto-agentes.md) y [contrato-de-agentes.md](contrato-de-agentes.md).

El análisis de los agentes internos del producto está en [descubrimiento-ia-agentes.md](descubrimiento-ia-agentes.md); sus modelos y proveedores siguen sin aprobarse. La organización operativa de desarrollo está en [agentes-desarrollo.md](agentes-desarrollo.md): ADR-004 aprueba sus contratos y existen selecciones provisionales de DEV-00 y Developer DEV-02. La configuración ejecutable sigue pendiente.

Los [escenarios y resultados de evaluación](evaluacion-agentes-desarrollo.md) registran R2 de DEV-00 y EVAL-01 satisfactorios, EVAL-02 validado técnicamente por EVAL-03 y EVAL-04 con Reviewer satisfactorio y Tester satisfactorio en detección tras una repetición. Se conservan la incidencia de acceso a criterios en la primera ejecución del Tester, las observaciones de la repetición y el ajuste de entrada. Controles efectivos, consumo atribuible y piloto global siguen pendientes; no se garantiza evaluación ciega.

La [matriz inicial de modelos](matriz-modelos-agentes-desarrollo.md) recoge la investigación documentada el 2026-09-30, las selecciones provisionales de DEV-00 y DEV-02 y los candidatos de los demás roles. Los resultados son específicos de los casos evaluados y no demuestran ahorro ni fiabilidad general.

El [diseño EVAL-05](diseno-evaluacion-permisos-agentes.md), preparado el 2026-10-07 para el issue #36, define cómo evaluar comportamiento y controles efectivos en un entorno sintético. La [ficha de entorno](entorno-eval-05.md) y la [guía de revisión humana](revision-eval-05-colaborador.md) desarrollan su preparación.

La [preparación del encargo Developer](encargo-eval-05-developer.md) identifica el primer perfil, los campos que requiere el laboratorio y una plantilla futura. La [guía de raíz y perfiles](preparacion-raiz-perfiles-eval-05.md) explica cómo preparar manualmente `/Tests/HPA-EVAL-05` y contiene una plantilla portable de permisos. La revisión, las versiones y la evidencia de aplicación se consultan en el roadmap; estos documentos no acreditan controles efectivos ni autorizan ejecución por sí solos.

El avance, los pendientes y el siguiente paso se mantienen en el [seguimiento de EVAL-05 en el roadmap](../01-proyecto/roadmap.md#seguimiento-de-eval-05), que debe actualizarse en cada cambio.
