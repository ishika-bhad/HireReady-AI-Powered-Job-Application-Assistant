from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_updated_resume(resume_text, match_analysis):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    header = Paragraph("Updated Resume", styles['Heading1'])
    content = [header, Spacer(1, 12)]

    for line in resume_text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles['Normal']))

    if match_analysis.get("ats_optimization_suggestions"):
        content.append(Spacer(1, 12))
        content.append(Paragraph("ATS Optimization", styles['Heading2']))

        for s in match_analysis["ats_optimization_suggestions"]:
            content.append(
                Paragraph(f"- {s['section']}: {s['suggested_change']}",
                          styles['Normal'])
            )

    doc.build(content)
    buffer.seek(0)
    return buffer
