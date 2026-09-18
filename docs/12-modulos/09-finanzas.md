# Módulo 9 — Finanzas / Planificación Salarial — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un modelo de datos definitivo, una moneda base, ni una integración con bancos o servicios financieros externos.

## Propósito

Permitir al propietario registrar y consultar su situación económica personal —ingresos, gastos, planificación salarial— con la información mínima necesaria para entender de dónde vienen y a dónde van sus recursos, sin convertir el producto en un gestor contable completo ni en un agregador bancario.

## Problema que resuelve

La información financiera personal suele quedar dispersa entre hojas de cálculo, aplicaciones bancarias y notas sueltas, sin relación con el resto de la vida del propietario (una tarea de pago pendiente, un documento de nómina, un evento de vencimiento). Sin un módulo propio, no habría un lugar único donde ver la situación económica de conjunto ni relacionarla con otros módulos del sistema.

## Alcance funcional propuesto

El módulo distingue el registro de movimientos del de planificación:

- `Movimiento`: entrada o salida de dinero registrada manualmente, con importe, fecha, categoría y una nota opcional.
- `Categoría`: clasificación de un movimiento (ingreso, gasto fijo, gasto variable, ahorro), sin un catálogo cerrado definido aún.
- `Planificación salarial`: previsión o desglose de ingresos esperados (salario, otras fuentes) en un periodo, distinta del registro real de movimientos.
- `Vencimiento financiero`: fecha relevante asociada a un pago o cobro esperado, que Calendario puede reflejar igual que hace con Tareas y Estudios.

El módulo no pretende reconciliar automáticamente con ninguna cuenta bancaria real en el MVP: los movimientos se registran manualmente o se importan de forma explícita, sin conexión directa a un banco.

## Debe permitir

- Registrar un movimiento con importe, fecha, categoría y nota opcional.
- Consultar el balance en un periodo (por ejemplo, un mes) y un desglose por categoría.
- Definir una planificación salarial simple (ingresos esperados en un periodo) y compararla, si se aprueba, con los movimientos reales.
- Registrar un vencimiento financiero con su fecha, para que Calendario lo refleje mediante relación explícita.
- Relacionar un movimiento con un documento (una factura, un justificante) a través de Documentos y Archivos.
- Disparar, a través de Notificaciones, un aviso previo a un vencimiento próximo.

## No debe hacer

- No se conecta a bancos, tarjetas ni servicios de agregación financiera en el MVP; cualquier importación queda como acción explícita del propietario, no como sincronización automática.
- No calcula impuestos, nóminas ni retenciones: solo registra los importes que el propietario introduce.
- No sustituye a Documentos y Archivos para guardar facturas o justificantes: los referencia mediante relación.
- No decide todavía si soporta múltiples monedas ni cómo se convertirían entre sí.
- No comparte ni expone información financiera a otros módulos salvo mediante relaciones explícitas y autorizadas.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Movimiento` | Entrada o salida de dinero registrada. | Puede relacionarse con un documento justificante mediante Core. |
| `Categoría` | Clasificación de un movimiento. | Atributo del movimiento; catálogo inicial abierto a definición. |
| `Planificación salarial` | Previsión de ingresos en un periodo. | Se compara, si se aprueba, con los movimientos reales de ingreso del mismo periodo. |
| `Vencimiento financiero` | Fecha relevante de un pago o cobro esperado. | Fecha relevante externa que Calendario puede reflejar, igual que Tareas y Estudios. |

## Ciclo de vida y reglas iniciales

1. El propietario registra un movimiento con al menos importe y fecha; categoría y nota son opcionales en el MVP.
2. El propietario puede, por separado, definir una planificación salarial para un periodo (p. ej. un mes), sin que esto genere movimientos automáticamente.
3. Un vencimiento financiero puede registrarse de forma independiente de un movimiento real, y se marca como resuelto cuando el propietario registra el movimiento correspondiente; la regla exacta de vinculación queda pendiente de diseño.
4. Antes de un vencimiento, el módulo puede solicitar a Notificaciones un aviso previo, según la preferencia del propietario.
5. Eliminar un movimiento o vencimiento retira su registro y sus relaciones; los documentos relacionados no se eliminan, solo se desvincula la relación.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta entidades, relaciones explícitas, eventos internos y auditoría conceptual. |
| Identidad y Seguridad (1) | Autoriza quién puede ver o modificar información financiera; especialmente sensible en este módulo. |
| Configuración (2) | Puede alojar preferencias como la moneda por defecto o el periodo de balance habitual. |
| Notificaciones (3) | Recibe los eventos de vencimiento próximo y decide cómo avisar. |
| Documentos y Archivos (5) | Destino habitual de relaciones desde un movimiento (factura, justificante, nómina). |
| Calendario y Eventos (7) | Refleja los vencimientos financieros como fechas relevantes externas. |
| Búsqueda, Automatizaciones, IA/Agentes | Consumirán la información financiera como datos de dominio cuando se estudien esos módulos, con especial atención a permisos. |

## Seguridad, privacidad y límites de acceso

Este es uno de los módulos con información más sensible del sistema. Se proponen los siguientes principios de diseño: acceso restringido por defecto al propietario, sin exposición de detalle financiero en notificaciones más allá de lo necesario (p. ej. un aviso de vencimiento no necesita mostrar el importe exacto en un canal poco seguro), y trazabilidad de quién accede o modifica un movimiento cuando en el futuro haya más de un actor. El cifrado en reposo y el nivel de auditoría exacto quedan pendientes de decisión técnica.

## Automatizaciones

No se propone automatización propia para el MVP más allá de disparar el evento interno que Notificaciones puede consumir para el aviso previo a un vencimiento. En el futuro podría estudiarse la conciliación asistida entre movimientos y vencimientos, o alertas de gasto inusual, pero esa lógica corresponde a Automatizaciones y no se decide aquí.

## MVP propuesto

- Registro manual de movimientos con importe, fecha, categoría y nota opcional.
- Consulta de balance y desglose por categoría en un periodo.
- Registro de vencimientos financieros con aviso previo simple a través de Notificaciones.
- Relación explícita con documentos justificantes.

El soporte de planificación salarial comparada con movimientos reales, el soporte multimoneda y el catálogo cerrado de categorías son decisiones pendientes; por ello no se presentan como requisitos aprobados.

## Futuro, no MVP

- Importación desde extractos bancarios o ficheros externos, siempre como acción explícita del propietario.
- Soporte multimoneda con conversión.
- Presupuestos por categoría y alertas de desviación.
- Conciliación asistida entre planificación salarial y movimientos reales.
- Informes o gráficas de evolución financiera a lo largo del tiempo.

## Decisiones pendientes

- Catálogo inicial de categorías de movimiento.
- Si la planificación salarial forma parte del MVP o se pospone.
- Regla de vinculación entre un vencimiento financiero y el movimiento real que lo resuelve.
- Soporte de una sola moneda frente a varias desde el inicio.
- Nivel de detalle financiero permitido en una notificación de vencimiento.

## Trazabilidad

- Visión y alcance: `docs/01-proyecto/vision-y-alcance.md`.
- Core y relaciones: `docs/12-modulos/00-core.md`.
- Identidad y Seguridad: `docs/12-modulos/01-identidad-seguridad.md`.
- Configuración y Notificaciones: `docs/12-modulos/02-configuracion.md` y `docs/12-modulos/03-notificaciones.md`.
- Información Personal: `docs/12-modulos/04-informacion-personal.md`.
- Documentos y Archivos: `docs/12-modulos/05-documentos-y-archivos.md`.
- Tareas: `docs/12-modulos/06-tareas.md`.
- Calendario y Eventos: `docs/12-modulos/07-calendario-y-eventos.md`.
- Estudios: `docs/12-modulos/08-estudios.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.