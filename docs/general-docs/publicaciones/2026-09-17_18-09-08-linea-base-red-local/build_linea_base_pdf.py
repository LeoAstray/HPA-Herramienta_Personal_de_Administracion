from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

out = "docs/documentacion/publicaciones/2026-09-17_18-09-08-linea-base-red-local/HPA_Linea_Base_Red_Local.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CenteredTitle", parent=styles["Title"], alignment=TA_CENTER, fontName="Helvetica-Bold", fontSize=22, leading=27, spaceAfter=10))
styles.add(ParagraphStyle(name="CenteredSub", parent=styles["Normal"], alignment=TA_CENTER, fontSize=10, leading=14, spaceAfter=22))
styles["BodyText"].fontSize = 10
styles["BodyText"].leading = 14
styles["Heading1"].keepWithNext = True

story = []
def h(text):
    story.append(Paragraph(text, styles["Heading1"]))
def p(text):
    story.append(Paragraph(text, styles["BodyText"]))
    story.append(Spacer(1, 7))
def bullets(items):
    story.append(ListFlowable([ListItem(Paragraph(x, styles["BodyText"])) for x in items], bulletType="bullet", leftIndent=17))
    story.append(Spacer(1, 7))

story.append(Paragraph("Herramienta Personal de Administración", styles["CenteredTitle"]))
story.append(Paragraph("Línea base documental y estructura de proyecto<br/>17 de septiembre de 2026", styles["CenteredSub"]))

h("Propósito")
p("Esta edición de lectura consolida el contexto aprobado y la estructura documental inicial del proyecto. El contenido Markdown de docs es la fuente de verdad operativa; este documento no sustituye a sus archivos modulares.")
h("Estado actual")
p("El proyecto está en definición y estudio global de módulos. No hay código de producto ni arquitectura técnica concreta aprobada. El siguiente objetivo es completar la Fase 1 antes de definir arquitectura, modelo de dominio, requisitos y diseño técnico.")
h("Visión y alcance")
p("La aplicación será un centro privado de información y organización para uso personal: información cotidiana, documentos, estudios, planificación económica, guías, tareas, calendario, recordatorios y automatizaciones. Los datos residirán inicialmente en el ordenador del usuario.")
bullets([
    "MVP propuesto: web responsive, autenticación y sesión segura, información estructurada, archivos en ruta configurable, tareas, calendario y recordatorios básicos, búsqueda global, configuración y backup/restauración documentados.",
    "Fuera del alcance actual: SaaS multiusuario, app móvil nativa, Siri/voz, IA funcional, pagos o acceso bancario, y exposición directa a Internet sin diseño seguro.",
])
h("Decisiones vigentes")
bullets([
    "ADR-001: Asana gestiona el desarrollo y no forma parte del producto final.",
    "ADR-002: la web, futuros clientes móviles, voz y agentes usarán fronteras comunes de API y lógica de negocio; móvil y voz no son funciones del MVP.",
    "Alcance confirmado: el MVP será accesible desde dispositivos de la red local del usuario; sus controles técnicos de seguridad aún deben diseñarse.",
])
h("Estructura documental")
p("La documentación se organiza por gobierno, proyecto, requisitos, arquitectura, datos, API, frontend, seguridad, infraestructura, pruebas, IA, operaciones, módulos, ADR y cambios. Los documentos Markdown permiten trazabilidad y alimentación de agentes; los originales se preservan como fuentes históricas.")
h("Agentes de IA")
p("Los agentes son una evolución futura y deben permanecer desacoplados del núcleo. Deben usar permisos mínimos, fronteras de API, validación para acciones sensibles, revocación y registro de su actividad. No pueden convertir una propuesta en decisión ni implementar cambios relevantes sin análisis y documentación previos.")
h("Fase 1: estudio de módulos")
p("Cada módulo se analizará antes de diseñar la arquitectura: propósito, problema, capacidades, límites, entidades, relaciones, dependencias, seguridad, automatizaciones, interacciones, MVP, futuro y decisiones pendientes.")
bullets([
    "El estudio de Core está iniciado como propuesta conceptual.",
    "Identidad y Seguridad, Configuración, Notificaciones, Información Personal, Documentos, Tareas, Calendario, Estudios, Finanzas, Guías, Búsqueda, Automatizaciones, Integraciones, IA y Backup permanecen pendientes de estudio.",
])
h("Proceso obligatorio de cambio")
p("Análisis -> Diseño -> Documentación -> Asana -> Implementación -> Pruebas -> Documentación actualizada.")
p("Cada cambio relevante debe explicar qué, por qué, cómo, alternativas, impacto, seguridad, pruebas, despliegue, rollback y documentación relacionada. Nunca se documentan secretos reales.")
h("Fuentes de verdad")
p("Para la versión mantenible y detallada, consultar docs/README.md, docs/00-gobierno/estado-proyecto.md, docs/01-proyecto/vision-y-alcance.md, docs/13-adrs/indice.md, docs/12-modulos/README.md y docs/10-ia/.")

SimpleDocTemplate(out, pagesize=A4, rightMargin=2.5*cm, leftMargin=2.5*cm, topMargin=2.2*cm, bottomMargin=2.2*cm, title="Herramienta Personal de Administración").build(story)
