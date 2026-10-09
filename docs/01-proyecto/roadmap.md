# Roadmap documental

## Actual

- Línea base funcional y de alcance inicial disponible.
- ADR-001 y ADR-002 aprobadas.
- Modelo conceptual de Core aprobado por ADR-005; tecnología y autorización concreta pendientes.
- Estudio global de módulos completo; los módulos 0 a 15 cuentan con documentación de análisis Fase 1.
- Contratos de agentes de desarrollo y prioridades del equipo definidos (ADR-004); R2 de DEV-00 y EVAL-01 satisfactorios; EVAL-02 validado técnicamente por EVAL-03. EVAL-04 registrado: Reviewer satisfactorio y Tester satisfactorio en detección tras una repetición, con incidencia de protocolo inicial y observaciones conservadas. Piloto global y configuración ejecutable pendientes.
- El 2026-10-07 queda preparado el [diseño EVAL-05 de evaluación de permisos](../10-ia/diseno-evaluacion-permisos-agentes.md), asociado al [issue #36](https://github.com/LeoAstray/HPA-Herramienta_Personal_de_Administracion/issues/36). Incluye matriz por rol, casos positivos/negativos, entorno sintético, evidencia, encargo y plantilla de resultados. Sin laboratorio creado ni evaluación ejecutada. [CHG-021](../14-cambios/CHG-021-diseno-evaluacion-permisos-y-roadmap.md) registra el avance y la regla de actualizar este roadmap en cada cambio.
- Comprobaciones locales del cambio documental completadas: diff sin incidencias y 63 enlaces relativos resueltos. No sustituyen la revisión independiente del diseño ni la futura evaluación de controles.
- Avance posterior del 2026-10-07: el colaborador comunica conformidad con el diseño inicial y confirma que él realiza la revisión. Se prepara la [ficha del entorno](../10-ia/entorno-eval-05.md) y la [guía de revisión humana](../10-ia/revision-eval-05-colaborador.md). La ficha declara por qué esta sesión no cumple el aislamiento, propone rutas y perfiles por rol y fija puertas antes de ejecutar. Ficha nueva pendiente de revisión; no se crea laboratorio ni se lanzan agentes. Véase [CHG-022](../14-cambios/CHG-022-preparacion-revision-y-entorno-eval-05.md).
- Comprobaciones de preparación CHG-022 completadas: formato sin incidencias y 89 enlaces relativos resueltos en el conjunto de cambios locales. La ficha sigue pendiente de revisión humana y no hay resultados de controles.

Corrección documental del 2026-10-07: la propuesta de Core se ha recolocado directamente en `docs/03-arquitectura/` y se ha eliminado la carpeta anidada vacía. Las referencias de ADR-005 y CHG-020 resuelven ahora a la ruta prevista; véase [CHG-023](../14-cambios/CHG-023-correccion-carpeta-arquitectura.md). Los pendientes siguen siendo la revisión de la ficha EVAL-05 por el colaborador y la preparación posterior del laboratorio.

## Próximo

1. Ejecutar el descubrimiento y diseño de IA/Agentes: casos de uso, inventario de agentes, criterios de evaluación de modelos y límites de seguridad y privacidad (ADR-003).
   Para desarrollo, el colaborador ha comunicado conformidad con el diseño inicial EVAL-05. **Siguiente paso inmediato:** él revisa la ficha nueva del entorno; no se exige otro agente de revisión. Después prepara una raíz separada y perfiles efectivos, completa responsable, manifiesto, exclusión de criterios y cobertura de trazas (G2–G6), y se concreta el encargo del primer perfil Developer. No usar esta sesión de HPA como laboratorio ni iniciar sondas con acceso a datos reales o canales externos. Los siguientes perfiles serán Reviewer y Tester si corresponde, en encargos separados. Registrar comportamiento y controles por separado; actualizar este roadmap tras cada avance. Configuración, ejecución y validación siguen pendientes. EVAL-04 no garantiza evaluación ciega ni cierra el piloto. Consumo atribuible, utilidad de DEV-00 frente a una plantilla y el estado histórico de su prompt siguen pendientes. Developer conserva Sol 6.1 / Medium por defecto y Luna / Medium para tareas sencillas; los candidatos de los demás roles no cambian.
2. Resolver las decisiones de dominio que condicionan los agentes internos del producto: el contrato de Core ya está aprobado (ADR-005); queda identidad, permisos y sesiones. La preparación de agentes de desarrollo tiene sus propios contratos y puede avanzar antes.
3. Diseñar la arquitectura global y el modelo de dominio, incorporando los límites aprobados para IA/Agentes.
4. Convertir el alcance aprobado en requisitos con identificadores.
5. Elegir el diseño técnico e iterar hacia implementación, incluidos únicamente los agentes cuya necesidad, modelo y controles hayan sido aprobados.

## Futuro, no MVP

Móvil, Siri/voz, agentes IA funcionales, integraciones complejas, automatizaciones avanzadas y multiusuario. El descubrimiento de IA/Agentes está priorizado, pero no autoriza todavía una funcionalidad de IA en el MVP.

## Mantenimiento obligatorio

Cada cambio actualiza este documento con avance, pendientes y siguiente paso, aunque no cambie el orden de los hitos. Véase el [proceso de cambio](../00-gobierno/proceso-de-cambio.md). El issue organiza la tarea; Markdown conserva el estado operativo. GitHub y Asana se gestionan manualmente por el colaborador, sin acceso remoto por parte del agente salvo nueva petición expresa.
