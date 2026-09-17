# Módulo 5 — Documentos y Archivos — definición funcional inicial

## Estado

**Fase 1 en análisis.** Este documento define el alcance funcional propuesto del módulo. No aprueba un sistema de archivos, una base de datos, un motor de indexación, un formato de metadatos ni un mecanismo de sincronización.

## Propósito

Permitir al propietario localizar, consultar y organizar los documentos y archivos que residen en una ruta física configurable de su ordenador, conservando la relación entre el elemento lógico mostrado por la aplicación y su archivo físico sin convertir el producto en un proveedor de almacenamiento externo.

## Problema que resuelve

Los archivos cotidianos se dispersan entre carpetas, nombres y soportes. Sin una vista organizada, cuesta saber qué se tiene, encontrar un documento relevante, relacionarlo con una tarea o dato personal y detectar cuándo una referencia de la aplicación ya no coincide con el archivo físico.

## Alcance funcional propuesto

El módulo tratará el archivo físico y su representación lógica como conceptos distintos:

- `Archivo físico`: elemento existente en una ruta autorizada del ordenador del propietario.
- `Documento o archivo registrado`: referencia lógica que permite clasificar, describir y relacionar un archivo físico.
- `Metadato`: información descriptiva o de organización añadida por el usuario o derivada de forma segura; no sustituye el contenido original.
- `Ruta gestionada`: ubicación raíz configurada explícitamente desde la que el módulo puede descubrir o administrar archivos.

El registro lógico no debe dar a entender que un archivo existe cuando su referencia física ya no es válida. La reconciliación exacta entre ambos conceptos queda pendiente de diseño.

## Debe permitir

- Definir una o varias rutas gestionadas, dentro de los límites que se aprueben para el MVP.
- Explorar y localizar archivos existentes en las rutas autorizadas.
- Registrar información descriptiva útil: título o nombre de presentación, tipo, ubicación, fechas conocidas, áreas/categorías y notas breves.
- Asociar un documento o archivo con elementos de otros módulos mediante relaciones explícitas de Core: por ejemplo, una tarea, un evento, un perfil o un área.
- Abrir o entregar el archivo al mecanismo local autorizado, sin asumir un visor técnico concreto.
- Detectar y comunicar referencias rotas, archivos no disponibles o cambios que requieran revisión, según las capacidades que se definan.
- Permitir retirar un registro lógico de la organización sin que ello implique borrar el archivo físico.

## No debe hacer

- No almacena credenciales, secretos ni material de autenticación dentro de los metadatos.
- No sustituye al sistema de archivos ni administra ubicaciones no autorizadas por el propietario.
- No borra, mueve, renombra ni sobrescribe archivos físicos como comportamiento implícito de una operación lógica.
- No interpreta el contenido de documentos privados, ejecutables o formatos desconocidos para extraer información en el MVP.
- No sincroniza con nubes, proveedores externos, correo, móvil, voz o agentes de IA; esas integraciones son futuras y requieren autorización específica.
- No asume que todos los archivos personales deben registrarse ni que un archivo registrado se pueda compartir con otros módulos sin control de acceso.

## Conceptos y relaciones — propuesta

| Concepto | Papel | Relación propuesta |
| --- | --- | --- |
| `Ruta gestionada` | Límite de ubicación autorizado por el propietario. | Agrupa archivos físicos que el módulo puede examinar bajo una política pendiente. |
| `Archivo físico` | Referencia a un elemento del sistema de archivos. | Puede estar vinculado a cero o un registro lógico; su disponibilidad debe verificarse antes de una operación sensible. |
| `Documento/archivo registrado` | Elemento de dominio organizado por la aplicación. | Tiene metadatos y se vincula a un archivo físico cuando aplique. |
| `Metadato` | Descripción y clasificación aportada por el usuario o derivada de forma segura. | Pertenece al registro; no reemplaza ni modifica el contenido del archivo físico. |
| `Referencia cruzada` | Relación semántica con otro elemento del dominio. | Se expresa mediante las relaciones explícitas de Core, con significado y autorización definidos. |

Un archivo físico puede existir sin registro lógico. Un registro puede quedar temporalmente sin archivo físico disponible; ese estado no autoriza a crear una copia, borrar evidencia ni modificar la ruta de forma automática.

## Ciclo de vida y reglas iniciales

1. El propietario autoriza una ruta gestionada mediante la configuración y los controles que se definan.
2. El módulo descubre o recibe la selección de un archivo dentro de esa ruta y crea un registro lógico si el usuario así lo solicita.
3. El propietario puede completar o corregir los metadatos y crear relaciones explícitas.
4. Antes de abrir, modificar o ejecutar una acción sobre el archivo físico, el sistema deberá comprobar que sigue dentro de una ruta autorizada y que la referencia es válida.
5. Si el archivo se mueve, desaparece o cambia fuera de la aplicación, el módulo debe marcar la referencia para revisión. La estrategia de actualización, reconciliación y resolución de conflictos sigue pendiente.
6. Retirar el registro lógico solo elimina su organización y relaciones según las reglas que se aprueben; borrar, mover o renombrar el archivo físico exige una operación separada, explícita y reversible cuando sea posible.

## Dependencias e interacción

| Módulo | Relación |
| --- | --- |
| Core (0) | Aporta entidades, relaciones explícitas, eventos internos y auditoría conceptual. |
| Identidad y Seguridad (1) | Autoriza el acceso a rutas, registros y operaciones sensibles. |
| Configuración (2) | Aloja las preferencias y la declaración de rutas gestionadas; no lee archivos por sí misma. |
| Notificaciones (3) | Puede comunicar referencias rotas, errores de acceso o solicitudes de revisión sin incluir contenido sensible. |
| Información Personal (4) | Puede ser referenciada como titular o contexto cuando sea necesario, sin duplicar datos personales. |
| Tareas, Calendario, Estudios, Finanzas, Guías y Búsqueda | Podrán crear relaciones con registros autorizados; sus reglas propias no pertenecen a este módulo. |
| Backup y Recuperación | Deberá definir en el futuro qué se respalda: metadatos, archivos físicos, ambos o referencias a rutas. |

No existe dependencia de Asana ni de una integración externa.

## Seguridad, privacidad y límites de acceso

Los documentos pueden contener datos personales, financieros, académicos o secretos. Se proponen los siguientes controles de diseño:

- limitar toda exploración y operación a rutas explícitamente autorizadas;
- aplicar mínimo privilegio a lectura, creación de registros, apertura y futuras operaciones físicas;
- no exponer contenido, nombres completos, rutas absolutas ni metadatos sensibles en notificaciones o auditorías cuando no sea necesario;
- separar los permisos sobre el registro lógico de los permisos sobre el archivo físico;
- requerir confirmación explícita y trazabilidad para acciones futuras que alteren archivos físicos;
- tratar archivos desconocidos, ejecutables o potencialmente peligrosos como contenido no confiable y no ejecutarlos desde el módulo.

El cifrado en reposo, las reglas de acceso del sistema operativo, la detección de malware, la retención, el borrado seguro, la copia de seguridad y la recuperación no están decididos. Este módulo no habilita acceso externo a los archivos ni exposición a Internet.

## Automatizaciones

No se propone automatización propia para el MVP. En el futuro podría notificar referencias rotas, solicitar clasificación de nuevos archivos o ejecutar revisiones programadas de disponibilidad. Toda automatización deberá tener una identidad, alcance de ruta, autorización y registro de resultado; no podrá mover, eliminar, subir o compartir archivos sin una política explícita y aprobación aplicable.

## MVP propuesto

- Ruta física configurable y explícitamente autorizada para los archivos del propietario.
- Exploración y registro básico de documentos y archivos existentes.
- Metadatos manuales mínimos: nombre de presentación, tipo, ruta o referencia de ubicación, área/categoría y nota opcional.
- Consulta, apertura local autorizada y relaciones básicas con otros elementos del dominio.
- Aviso o estado visible de referencia no disponible cuando se pueda comprobar.
- Retirada de registros lógicos sin borrado implícito del archivo físico.

El número de rutas, los tipos de archivo soportados, los metadatos obligatorios y la capacidad de detectar cambios externos son decisiones pendientes; por ello no se presentan como requisitos aprobados.

## Futuro, no MVP

- Operaciones físicas controladas de crear, mover, renombrar, versionar, archivar o eliminar con confirmación y recuperación.
- Previsualización segura, extracción de texto y clasificación asistida.
- Sincronización o importación desde fuentes externas aprobadas.
- Reglas de conservación, deduplicación, detección de modificaciones y resolución de conflictos.
- Búsqueda de contenido, etiquetado avanzado, OCR y relaciones semánticas más ricas.
- Compartición controlada si se aprueba un escenario multiusuario.

## Decisiones pendientes

- Número y tipo de rutas gestionadas en el MVP, y cómo se autorizan o revocan.
- Regla de identidad estable del archivo cuando se mueve o renombra fuera de la aplicación.
- Conjunto mínimo de metadatos, categorías y validaciones.
- Alcance de las operaciones físicas y el mecanismo de confirmación, auditoría, rollback y recuperación.
- Política de referencias rotas, cambios externos, archivos duplicados y conflictos.
- Qué se incluye en backup y restauración, y cómo evitar restaurar una referencia que apunte a una ubicación insegura.
- Criterios de contenido no confiable, previsualización y acceso a archivos sensibles.

## Trazabilidad

- Visión y alcance: `docs/01-proyecto/vision-y-alcance.md`.
- Core y relaciones: `docs/12-modulos/00-core.md`.
- Identidad y Seguridad: `docs/12-modulos/01-identidad-seguridad.md`.
- Configuración y Notificaciones: `docs/12-modulos/02-configuracion.md` y `docs/12-modulos/03-notificaciones.md`.
- Información Personal: `docs/12-modulos/04-informacion-personal.md`.
- Seguridad, infraestructura, operaciones, requisitos, datos, API, interfaz y pruebas: pendientes de concretar tras la Fase 1.
