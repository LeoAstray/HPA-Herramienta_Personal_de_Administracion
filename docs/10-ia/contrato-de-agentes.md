# Contrato operativo de agentes

## Autorización

Un agente solo puede realizar las acciones solicitadas o necesarias dentro de la tarea asignada. Las acciones sensibles, destructivas, externas o que incorporen nuevos servicios requieren confirmación del propietario cuando no estén ya autorizadas.

## Separación de ámbitos

Los agentes de desarrollo trabajan sobre el repositorio, la documentación y las pruebas del proyecto. No son parte del producto HPA, no definen sus permisos de usuario y no obtienen acceso a datos personales del futuro producto por el hecho de ayudar a desarrollarlo.

Los agentes internos del producto serán clientes futuros del HPA y deberán usar sus propias fronteras de API, identidad, autorización y auditoría. Su diseño no autoriza a reutilizar automáticamente herramientas o permisos de los agentes de desarrollo.

## Colaboración de desarrollo

El equipo está formado por dos colaboradores. Un agente puede proponer, editar dentro de una tarea autorizada, revisar o ejecutar pruebas, pero una persona conserva la responsabilidad de aprobar decisiones, integrar cambios y publicar resultados. Un agente revisor no debe aprobar como independiente cambios que haya producido él mismo.

ADR-004 y [agentes-desarrollo.md](agentes-desarrollo.md) concretan esos permisos: Developer edita archivos locales y ejecuta comprobaciones breves; Reviewer y Tester informan; Tester realiza la validación independiente. Cualquier colaborador puede aprobar. Las operaciones de escritura Git son manuales, GitHub es de solo lectura para los agentes y las correcciones de revisión y validación vuelven al Developer por petición humana.

## Acceso y aislamiento futuros

Los futuros agentes deberán usar las mismas fronteras de API, autenticación y autorización que otros clientes. No accederán directamente a datos ni secretos salvo permiso explícito, revocable y con el mínimo alcance. Deben poder sustituirse o desactivarse sin reconstruir el núcleo.

## Registro mínimo futuro

Para acciones de agentes que afecten al producto se deberá registrar: identidad o tipo de agente, fecha/hora, datos consultados, solicitud, acción propuesta, acción ejecutada, autorización aplicable, resultado y error si lo hubiera.

## Validación humana

Las acciones que creen, modifiquen o eliminen datos sensibles, modifiquen permisos, usen integraciones externas o afecten a backup/restauración deben tener una política de validación explícita antes de automatizarse.
