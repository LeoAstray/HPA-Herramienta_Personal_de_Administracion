from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

out = "docs/documentacion/publicaciones/2026-09-17_18-09-08-linea-base-red-local/HPA_Linea_Base_Red_Local.docx"
doc = Document()
section = doc.sections[0]
section.top_margin = Cm(2.2)
section.bottom_margin = Cm(2.2)
section.left_margin = Cm(2.5)
section.right_margin = Cm(2.5)

styles = doc.styles
styles["Normal"].font.name = "Aptos"
styles["Normal"].font.size = Pt(10.5)
styles["Title"].font.name = "Aptos Display"
styles["Title"].font.size = Pt(24)

title = doc.add_paragraph(style="Title")
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title.add_run("Herramienta Personal de Administración")
subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitle.add_run("Línea base documental y estructura de proyecto\n17 de septiembre de 2026").italic = True

def heading(text, level=1):
    paragraph = doc.add_heading(text, level=level)
    paragraph.paragraph_format.keep_with_next = True

def bullet(text):
    doc.add_paragraph(text, style="List Bullet")

heading("Propósito")
doc.add_paragraph(
    "Esta edición de lectura consolida el contexto aprobado y la estructura documental inicial del proyecto. "
    "El contenido Markdown de docs es la fuente de verdad operativa; este documento no sustituye a sus archivos modulares."
)

heading("Estado actual")
doc.add_paragraph(
    "El proyecto está en definición y estudio global de módulos. No hay código de producto ni arquitectura técnica concreta aprobada. "
    "El siguiente objetivo es completar la Fase 1 antes de definir arquitectura, modelo de dominio, requisitos y diseño técnico."
)

heading("Visión y alcance")
doc.add_paragraph(
    "La aplicación será un centro privado de información y organización para uso personal: información cotidiana, documentos, estudios, "
    "planificación económica, guías, tareas, calendario, recordatorios y automatizaciones. Los datos residirán inicialmente en el ordenador del usuario."
)
bullet("MVP propuesto: web responsive, autenticación y sesión segura, información estructurada, archivos en ruta configurable, tareas, calendario y recordatorios básicos, búsqueda global, configuración y backup/restauración documentados.")
bullet("Fuera del alcance actual: SaaS multiusuario, app móvil nativa, Siri/voz, IA funcional, pagos o acceso bancario, y exposición directa a Internet sin diseño seguro.")

heading("Decisiones vigentes")
bullet("ADR-001: Asana gestiona el desarrollo y no forma parte del producto final.")
bullet("ADR-002: la web, futuros clientes móviles, voz y agentes usarán fronteras comunes de API y lógica de negocio; móvil y voz no son funciones del MVP.")
bullet("Alcance confirmado: el MVP será accesible desde dispositivos de la red local del usuario; sus controles técnicos de seguridad aún deben diseñarse.")

heading("Estructura documental")
doc.add_paragraph(
    "La documentación se organiza por gobierno, proyecto, requisitos, arquitectura, datos, API, frontend, seguridad, infraestructura, pruebas, "
    "IA, operaciones, módulos, ADR y cambios. Los documentos Markdown permiten trazabilidad y alimentación de agentes; los originales se preservan como fuentes históricas."
)

heading("Agentes de IA")
doc.add_paragraph(
    "Los agentes son una evolución futura y deben permanecer desacoplados del núcleo. Deben usar permisos mínimos, fronteras de API, validación para acciones sensibles, revocación y registro de su actividad. "
    "No pueden convertir una propuesta en decisión ni implementar cambios relevantes sin análisis y documentación previos."
)

heading("Fase 1: estudio de módulos")
doc.add_paragraph(
    "Cada módulo se analizará antes de diseñar la arquitectura: propósito, problema, capacidades, límites, entidades, relaciones, dependencias, seguridad, automatizaciones, interacciones, MVP, futuro y decisiones pendientes."
)
bullet("El estudio de Core está iniciado como propuesta conceptual.")
bullet("Identidad y Seguridad, Configuración, Notificaciones, Información Personal, Documentos, Tareas, Calendario, Estudios, Finanzas, Guías, Búsqueda, Automatizaciones, Integraciones, IA y Backup permanecen pendientes de estudio.")

heading("Proceso obligatorio de cambio")
doc.add_paragraph("Análisis -> Diseño -> Documentación -> Asana -> Implementación -> Pruebas -> Documentación actualizada.")
doc.add_paragraph(
    "Cada cambio relevante debe explicar qué, por qué, cómo, alternativas, impacto, seguridad, pruebas, despliegue, rollback y documentación relacionada. Nunca se documentan secretos reales."
)

heading("Fuentes de verdad")
doc.add_paragraph(
    "Para la versión mantenible y detallada, consultar docs/README.md, docs/00-gobierno/estado-proyecto.md, docs/01-proyecto/vision-y-alcance.md, "
    "docs/13-adrs/indice.md, docs/12-modulos/README.md y docs/10-ia/."
)

doc.save(out)
