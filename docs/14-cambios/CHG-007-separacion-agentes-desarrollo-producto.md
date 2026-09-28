# CHG-007 — Separación de agentes de desarrollo y producto

## Estado

Documentado y aplicado a la documentación operativa. No se conecta ningún modelo, proveedor o servicio externo, ni se añade código de producto.

## Objetivo y alcance

Adaptar el descubrimiento de IA/Agentes al desarrollo colaborativo entre dos personas. Se separan los agentes que ayudarán a desarrollar el repositorio de los futuros agentes internos del producto HPA, para que sus permisos, datos y responsabilidades no se confundan.

## Impacto

- **Desarrollo:** se proponen los roles Developer, Reviewer, Tester, Documentación y Coordinación, con flujo de revisión cruzada para dos colaboradores.
- **Producto:** la cartera de agentes internos se conserva como un ámbito independiente y no recibe acceso al repositorio por defecto.
- **Seguridad:** se refuerzan mínimo privilegio, separación de ámbitos, prohibición de autoaprobación y autorización humana para acciones sensibles o externas.
- **Modelos:** la futura comparación se realizará por rol y con escenarios representativos, no mediante una selección genérica.
- **Arquitectura y código:** no se toma una decisión técnica ni se implementa ningún agente.

## Verificación y rollback

Se comprueba que la documentación de IA enlaza los dos ámbitos y que la propuesta de roles no se presenta como una funcionalidad del producto. El rollback consiste en revertir los documentos de este cambio; no afecta a datos, servicios ni infraestructura.

## Documentación relacionada

- `docs/10-ia/agentes-desarrollo.md`
- `docs/10-ia/descubrimiento-ia-agentes.md`
- `docs/10-ia/contrato-de-agentes.md`
- `docs/13-adrs/ADR-003-priorizacion-descubrimiento-ia-agentes.md`
