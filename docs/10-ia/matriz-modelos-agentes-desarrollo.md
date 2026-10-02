# Matriz inicial de modelos para agentes de desarrollo

## Estado y fecha de consulta

**Investigación documentada el 2026-09-30; resultados actualizados el 2026-10-03. DEV-00 y política de modelos de DEV-02 aprobados provisionalmente; EVAL-01 documental satisfactorio; EVAL-02 con Luna validado técnicamente por EVAL-03. EVAL-04: Reviewer satisfactorio; Tester con incidencia de protocolo inicial y repetición satisfactoria en detección, con entrada ajustada y observaciones de presentación.** La disponibilidad real debe comprobarse en el selector de cada cuenta y cliente. Ambos colaboradores tienen Plus y no usarán API de pago ni créditos adicionales.

## Evidencia oficial

- [Modelos de ChatGPT Work y Codex](https://learn.chatgpt.com/docs/models): GPT-6.1 Sol se está desplegando para Plus y se recomienda para flujos complejos de programación; Luna se orienta a tareas claras, repetibles y frecuentes. El esfuerzo de razonamiento mayor consume más tokens y tarda más.
- [Precios y planes](https://learn.chatgpt.com/docs/pricing): Plus incluye Codex y GPT-6 Sol/Luna. El consumo depende del modelo, del tamaño y complejidad de la tarea y de si se ejecuta localmente o en la nube; la documentación no proporciona una equivalencia fija por tarea.
- [Selección de modelos](https://developers.openai.com/api/docs/guides/model-selection): Luna es la opción eficiente para trabajo acotado; GPT-6.1 Sol equilibra capacidad y coste para trabajo técnico complejo. OpenAI recomienda comparar las mismas entradas y conservar la configuración más ligera que alcance el nivel de calidad requerido.
- [Prácticas de prompts y skills](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): las instrucciones excesivas y lecturas obligatorias innecesarias consumen contexto; conviene aplicar instrucciones específicas al trabajo y mantener descripciones de skills breves.
- [Evaluación de skills](https://developers.openai.com/blog/eval-skills): una evaluación útil mide resultado, proceso, estilo y eficiencia con un conjunto pequeño de casos y controles deterministas.

## Selecciones provisionales y candidatos por rol

| Rol | Configuración inicial | Alternativa o escalado condicionado | Motivo e hipótesis a comprobar |
| --- | --- | --- | --- |
| DEV-00 Preparador de petición | **Selección provisional aprobada:** GPT-6 Luna (`gpt-6-luna`), esfuerzo Low (`low`) | Solo con autorización humana: evaluar Luna Medium si omite ambigüedades materiales | Dos respuestas iniciales satisfactorias; ahorro de consumo no demostrado y prompt revisado pendiente de regresión. |
| DEV-01 Reviewer | GPT-6.1 Sol Medium | Sol High para seguridad, arquitectura, datos o diffs amplios; GPT-6 Sol equivalente si 6.1 no aparece | EVAL-01 y EVAL-04 satisfactorios para sus casos documentales con GPT-6.1 Sol / Medium confirmado por el colaborador; EVAL-04 muestra 45 s. Consumo y telemetría no disponibles; se mantiene como candidato, sin fiabilidad general demostrada. |
| DEV-02 Developer | **Configuración habitual aprobada provisionalmente:** GPT-6.1 Sol (`gpt-6.1-sol`) / Medium (`medium`) | **Alternativa autorizada por tarea:** GPT-6 Luna (`gpt-6-luna`) / Medium (`medium`) para tareas sencillas y acotadas | Sol para funcionalidades, lógica, refactorizaciones y cambios con dependencias; Luna para enlaces, cambios mecánicos y correcciones pequeñas con criterios claros y bajo riesgo. EVAL-02 documental con Luna validado técnicamente mediante EVAL-03; Sol como Developer aún no evaluado. |
| DEV-03 Tester | GPT-6 Luna Medium | Sol Medium cuando haya fallos ambiguos, integración entre módulos o diagnóstico complejo | EVAL-03 documental satisfactorio con Luna / Medium confirmado. EVAL-04 registra 29 s con incidencia de acceso a criterios y 22 s en repetición con exclusiones añadidas: detección correcta, impactos poco desarrollados y celda L6 incoherente. Luna / Medium para EVAL-04 consta por contexto del encargo. Consumo y telemetría no disponibles; candidato conservado y pruebas complejas de código sin evaluar. |
| DEV-04 Documentación | GPT-6 Luna Low o Medium | Sol Medium para ADR o cambios transversales | Las ediciones mecánicas son acotadas; las decisiones necesitan más razonamiento. |
| DEV-05 Coordinación | GPT-6 Luna High | Sol Medium para dependencias transversales o planificación incierta | La planificación clara puede resolverse eficientemente; el conflicto de requisitos requiere Sol. |

DEV-00 se mantiene por decisión del colaborador tras los dos casos aportados de EVAL-00. El colaborador aprueba provisionalmente Sol / Medium como opción habitual de DEV-02 y Luna / Medium para tareas sencillas. Reviewer, Tester, Documentación y Coordinación conservan sus candidatos. Ninguna selección demuestra el consumo exacto de Plus. GPT-6.1 Sol está sujeto al despliegue y al cliente; el piloto registrará el modelo que realmente aparezca y se use. Astra no entra en la primera comparación porque Plus documenta Sol y Luna como opciones incluidas y el equipo prioriza cuota.

Para DEV-00, seleccionar modelo y esfuerzo antes de invocarlo. Los Markdown no cambian la configuración del chat. Una futura configuración ejecutable deberá fijar ambos valores sin alterar los modelos de los demás roles; su creación y verificación siguen pendientes. Véanse el [prompt](prompts/dev-00-preparar-peticion.md) y las [evidencias iniciales](evaluacion-agentes-desarrollo.md).

EVAL-04 compara cumplimiento del escenario por rol, no consumo entre Reviewer y Tester. La repetición del Tester recibió una entrada ajustada tras intervención humana; no se presenta como ejecución con condiciones idénticas a Reviewer. Los tiempos son los mostrados por la interfaz, no mediciones independientes. La primera ejecución se conserva como incidencia de protocolo; las declaraciones de no consultar criterios en las otras respuestas no garantizan evaluación ciega ni controles efectivos. Véase el [registro completo](evaluacion-agentes-desarrollo.md).

## Política de selección por tarea

1. Omitir DEV-00 cuando la petición ya contenga objetivo, alcance, permisos y criterio de aceptación suficientes.
2. Para Developer, seleccionar antes de ejecutar Sol / Medium por defecto; puede seleccionarse Luna / Medium para tareas sencillas, acotadas y de bajo riesgo. Registrar la configuración usada; los documentos no cambian el modelo del cliente. Si no está disponible o se necesita cambiarlo durante una ejecución, solicitar autorización humana. Para los demás roles, mantener las configuraciones de su fila.
3. Usar Sol desde el inicio para revisiones de riesgo alto o cambios que conecten varias áreas.
4. Escalar una sola vez cuando el resultado no alcance un criterio concreto; registrar el motivo.
5. No repetir una tarea completa solo para comparar modelos salvo que forme parte del piloto acordado.
6. No usar Max ni Ultra en el piloto inicial. La documentación oficial indica que la mayoría de tareas no los necesita y Ultra usa subagentes.

## Medición dentro de Plus

La cuota de Plus no ofrece una conversión pública estable de tarea a tokens o mensajes. Para cada ejecución se registrará el indicador de uso disponible en el cliente, modelo, esfuerzo, tamaño aproximado del contexto, número de rondas, resultado y correcciones humanas. Si el consumo por tarea no puede aislarse, se marcará como no comparable.

La decisión final favorecerá primero el menor consumo observado entre configuraciones que cumplan todos los criterios, después calidad, autonomía dentro de permisos y velocidad.
