from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

styles = getSampleStyleSheet()


def generate_pdf(dataset):

    os.makedirs("reports/exports", exist_ok=True)

    filename = f"reports/exports/{dataset['dataset_name']}.pdf"

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>InsightOS Executive Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Dataset:</b> {dataset['dataset_name']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Rows:</b> {dataset['rows']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Columns:</b> {dataset['columns']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Quality Score:</b> {dataset['quality_score']}%", styles["Normal"]))

    story.append(Paragraph(f"<b>Missing Values:</b> {dataset['missing_values']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Duplicate Rows:</b> {dataset['duplicate_rows']}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Decision Intelligence</b>", styles["Heading2"]))

    story.append(Paragraph(dataset["decision"]["health"], styles["Normal"]))

    for rec in dataset["decision"]["recommendations"]:
        story.append(Paragraph("• " + rec, styles["Normal"]))

    doc.build(story)

    return filename