# CHG-016 — Corrección de enlaces del índice ADR

## Estado y motivo

Corrección documental ejecutada el 2026-09-30 para EVAL-02. EVAL-01 confirmó que los destinos ADR-001 y ADR-002 del índice apuntaban a carpetas inexistentes, aunque los Markdown históricos estaban centralizados en `docs/general-docs/fuentes/adrs/`. Se actualizan únicamente esos destinos relativos. Las fuentes históricas no se modifican ni se mueven.

## Evidencia y archivos cambiados

- EVAL-01, registrado en `docs/10-ia/evaluacion-agentes-desarrollo.md` (hallazgo P2): confirmó los dos enlaces rotos en `docs/13-adrs/indice.md` y la existencia de los destinos históricos correctos. El registro advierte que esa comprobación no equivale a trazas completas ni demuestra aislamiento técnico.
- `docs/13-adrs/indice.md`: se cambiaron solo los destinos de ADR-001 y ADR-002. Etiquetas, estados, decisiones, ADR-003, ADR-004 y el resto del índice se conservaron.
- `docs/14-cambios/CHG-016-correccion-enlaces-indice-adr.md`: nuevo registro de motivo, alcance, comprobaciones y validación pendiente.

## Comprobaciones locales de DEV-02

Base examinada: `4739e2141c79e849f5144e7da7a389487baa4bbb`. El estado inicial (`git status --porcelain=v1`) estaba vacío.

| Comando | Resultado observado |
| --- | --- |
| `Test-Path -LiteralPath docs/general-docs/fuentes/adrs/ADR-001/ADR-001_ASANA_DESARROLLO_VS_PRODUCTO.md` | `True` |
| `Test-Path -LiteralPath docs/general-docs/fuentes/adrs/ADR-002/ADR-002_ARQUITECTURA_MULTICLIENTE_MOVIL_VOZ.md` | `True` |
| `git --no-optional-locks diff --check` | Sin salida; código de salida 0. |
| `git --no-optional-locks diff -- docs/13-adrs/indice.md` | Muestra exclusivamente las dos sustituciones de destino indicadas. |
| `git --no-optional-locks status --porcelain=v1` | Muestra el índice modificado y este registro nuevo sin rastrear. |

Las rutas relativas se calcularon desde `docs/13-adrs/indice.md` y apuntan a los dos Markdown históricos existentes. Estas comprobaciones locales no son una validación independiente ni una prueba completa de aislamiento.

## Pendiente para DEV-03 (EVAL-03)

Con un diff estable, verificar independientemente que ambos enlaces resuelven a los archivos históricos correctos, que en el índice solo cambiaron los dos destinos y que las etiquetas, estados, decisiones y demás filas se conservan. Revisar formato y ámbito de archivos; informar comandos, resultados y cualquier comprobación no ejecutada. El Tester no debe editar archivos mantenidos.
