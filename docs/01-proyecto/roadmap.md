# Roadmap documental

## Actual

- Línea base funcional y de alcance inicial disponible.
- ADR-001 y ADR-002 aprobadas.
- Estudio global de módulos completo; los módulos 0 a 15 cuentan con documentación de análisis Fase 1.
- Contratos de agentes de desarrollo y prioridades del equipo definidos (ADR-004); R2 de DEV-00 y EVAL-01 satisfactorios; EVAL-02 validado técnicamente por EVAL-03. EVAL-04 registrado: Reviewer satisfactorio y Tester satisfactorio en detección tras una repetición, con incidencia de protocolo inicial y observaciones conservadas. Piloto global y configuración ejecutable pendientes.

## Próximo

1. Ejecutar el descubrimiento y diseño de IA/Agentes: casos de uso, inventario de agentes, criterios de evaluación de modelos y límites de seguridad y privacidad (ADR-003).
   Para desarrollo, la matriz inicial de modelos está documentada. EVAL-04 aporta detección de defectos sintéticos, con una repetición del Tester cuya entrada se precisó; no garantiza evaluación ciega ni cierra el piloto. El siguiente trabajo propuesto es definir una comprobación acotada de controles de permisos en un entorno local desechable, sin acceso al remoto real; su diseño y ejecución requieren el encargo correspondiente. Consumo atribuible y utilidad de DEV-00 frente a una plantilla siguen pendientes. Developer conserva Sol 6.1 / Medium por defecto y Luna / Medium para tareas sencillas y acotadas, aprobados provisionalmente. Reviewer y Tester conservan candidatos. CHG-019 actualiza el README de IA; queda pendiente el estado del prompt DEV-00 señalado en EVAL-01.
2. Resolver las decisiones de dominio que condicionan los agentes internos del producto: primero el contrato de Core y después identidad, permisos y sesiones. La preparación de agentes de desarrollo tiene sus propios contratos y puede avanzar antes.
3. Diseñar la arquitectura global y el modelo de dominio, incorporando los límites aprobados para IA/Agentes.
4. Convertir el alcance aprobado en requisitos con identificadores.
5. Elegir el diseño técnico e iterar hacia implementación, incluidos únicamente los agentes cuya necesidad, modelo y controles hayan sido aprobados.

## Futuro, no MVP

Móvil, Siri/voz, agentes IA funcionales, integraciones complejas, automatizaciones avanzadas y multiusuario. El descubrimiento de IA/Agentes está priorizado, pero no autoriza todavía una funcionalidad de IA en el MVP.
