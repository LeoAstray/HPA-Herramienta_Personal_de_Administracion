# Contrato operativo de agentes

## Autorización

Un agente solo puede realizar las acciones solicitadas o necesarias dentro de la tarea asignada. Las acciones sensibles, destructivas, externas o que incorporen nuevos servicios requieren confirmación del propietario cuando no estén ya autorizadas.

## Acceso y aislamiento futuros

Los futuros agentes deberán usar las mismas fronteras de API, autenticación y autorización que otros clientes. No accederán directamente a datos ni secretos salvo permiso explícito, revocable y con el mínimo alcance. Deben poder sustituirse o desactivarse sin reconstruir el núcleo.

## Registro mínimo futuro

Para acciones de agentes que afecten al producto se deberá registrar: identidad o tipo de agente, fecha/hora, datos consultados, solicitud, acción propuesta, acción ejecutada, autorización aplicable, resultado y error si lo hubiera.

## Validación humana

Las acciones que creen, modifiquen o eliminen datos sensibles, modifiquen permisos, usen integraciones externas o afecten a backup/restauración deben tener una política de validación explícita antes de automatizarse.
