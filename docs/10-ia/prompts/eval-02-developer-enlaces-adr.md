# EVAL-02 — Developer DEV-02 — Enlaces del índice ADR

## Estado y configuración

**Preparado y ejecutado el 2026-09-30 con GPT-6 Luna / Medium según el colaborador; validado técnicamente por EVAL-03 en el estado examinado, sin aprobación de integración.** Se conserva el bloque enviado y su configuración como evidencia del caso sencillo, compatible con la política posterior Sol 6.1 / Medium por defecto y Luna / Medium para tareas sencillas. Encargo acotado a partir del primer hallazgo confirmado de EVAL-01. El colaborador seleccionará GPT-6 Luna (`gpt-6-luna`) / Medium (`medium`) antes de ejecutar. Este Markdown no cambia el modelo ni configura un agente. No sustituir ni escalar sin autorización humana; si la configuración efectiva no es visible, declararla no verificada.

## Petición para copiar

```text
Actúa como Developer (DEV-02) para EVAL-02 en:
C:\Users\leoli\Documents\Proyectos\HPA-Herramienta_Personal_de_Administracion

Objetivo: corregir los dos enlaces rotos a ADR-001 y ADR-002 en
docs/13-adrs/indice.md, confirmados en EVAL-01, y registrar la corrección.

Cumple AGENTS.md y su orden de lectura obligatorio. Consulta los contratos
de docs/10-ia/agentes-desarrollo.md y la evidencia de EVAL-01 en
docs/10-ia/evaluacion-agentes-desarrollo.md. Puedes leer otras fuentes
rectoras o históricas necesarias, sin editar sus contenidos.

Únicos archivos editables:
- docs/13-adrs/indice.md: solo los destinos de los enlaces ADR-001/002.
- docs/14-cambios/CHG-016-correccion-enlaces-indice-adr.md: crear el registro
  de la corrección, sus comprobaciones y pendientes para el Tester.
  Si ya existe, no sobrescribirlo: informa del conflicto.

Los archivos de destino existen en:
- docs/general-docs/fuentes/adrs/ADR-001/ADR-001_ASANA_DESARROLLO_VS_PRODUCTO.md
- docs/general-docs/fuentes/adrs/ADR-002/ADR-002_ARQUITECTURA_MULTICLIENTE_MOVIL_VOZ.md

Calcula los enlaces relativos desde docs/13-adrs/indice.md. Conserva
etiquetas, estados, decisiones, ADR-003 y ADR-004 y el resto del índice.
No muevas ni modifiques las fuentes históricas. No corrijas los otros
hallazgos de EVAL-01 ni amplíes el alcance.

Puedes ejecutar comprobaciones locales breves: Get-Content, rg,
Test-Path -LiteralPath y Git de lectura con --no-optional-locks
(rev-parse HEAD, status --porcelain=v1, diff, diff --cached, diff --check).
No ejecutes instalaciones, comandos destructivos, otros agentes ni
operaciones de escritura Git. No modifiques GitHub o Asana, publiques
ni apruebes tu propio trabajo.

Antes de editar, identifica HEAD y cambios locales, incluidos no rastreados.
Si existen cambios ajenos, consérvalos y distingue tu diff de ellos.
Si se solapan con los archivos asignados, informa y no sobrescribas.

Criterios de aceptación:
1. Ambos enlaces resuelven a los Markdown históricos correctos existentes.
2. En el índice solo cambian los dos destinos; decisiones y etiquetas se conservan.
3. El registro nuevo documenta el motivo, la evidencia de EVAL-01,
   archivos cambiados, comandos/resultados y validación independiente pendiente.
4. No se modifican otros archivos ni se realizan escrituras Git o externas.

Entrega HEAD y estado inicial/final, archivos y diff de tu cambio,
comandos y resultados reales, criterios cubiertos y pendientes de EVAL-03.
No declares ejecutadas comprobaciones que no hayas realizado ni equipares
un árbol de trabajo controlado con una prueba completa de aislamiento.
```

## Validación posterior

EVAL-03 verificará un diff estable de esta ejecución, los destinos de enlaces, la conservación del contenido y el ámbito de archivos. El Tester no corregirá archivos mantenidos. Las aprobaciones y operaciones Git siguen correspondiendo al colaborador. No se requiere tarea externa de Asana para esta preparación ni se autoriza crearla.
