from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from io import BytesIO
from models import InspectionResult

def build_pdf(result: InspectionResult):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    c.setFont("Helvetica-Bold", 22)
    c.drawString(40, 800, "TaurgoVision Inspection Report")

    # Executive Summary
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 760, "Executive Summary")

    c.setFont("Helvetica", 12)
    c.drawString(40, 740, result.summary)

    # Defects Table
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, 700, "Defects Identified")

    y = 680
    c.setFont("Helvetica", 11)
    for d in result.defects:
        c.drawString(40, y, f"- {d.type} | Severity: {d.severity} | Confidence: {d.confidence*100:.1f}%")
        y -= 20

    # Recommendations
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y - 20, "Recommendations")
    y -= 40

    c.setFont("Helvetica", 11)
    for rec in result.recommendations:
        c.drawString(40, y, f"- {rec}")
        y -= 20

    c.save()
    return buffer.getvalue()