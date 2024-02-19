"""
This scripts begins the pdf generation
"""
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate
from generate_pdf import generate_pdf
from flowables import Flowables

if __name__ == "__main__":
    filename = "output.pdf"
    canvas = Canvas(filename, pagesize=letter)
    doc = BaseDocTemplate(
        filename,
        pagesize=letter,
        rightMargin = 12,
        leftMargin = 12,
        topMargin = 12,
        bottomMargin = 12
    )

    PRIMARY_COLOR = colors.black
    SECONDARY_COLOR = colors.lightgrey
    flowables = Flowables(doc, PRIMARY_COLOR, SECONDARY_COLOR)
    page_flowables = [
        flowables.get_page1_frame1_flowables(),
        flowables.get_page1_frame2_flowables(),
        flowables.get_page1_frame3_flowables()
    ]
    generate_pdf(
        canvas=canvas,
        page_flowables=page_flowables,
        filename=filename, 
        frame_count=3,
        page_name='Theory', 
        page_index='1',
        primary_color=colors.black
    )
    canvas.showPage()

    PRIMARY_COLOR = colors.white
    SECONDARY_COLOR = colors.gray
    flowables = Flowables(doc, PRIMARY_COLOR, SECONDARY_COLOR)
    page_flowables = [
        flowables.get_page2_frame1_flowables()
    ]
    generate_pdf(
        canvas=canvas, 
        page_flowables=page_flowables, 
        filename=filename, 
        frame_count=1,
        page_name='Assessment',
        page_index='2',
        background='#233137',
        primary_color=PRIMARY_COLOR,
        secondary_color=SECONDARY_COLOR
    )
    canvas.showPage()
    canvas.save()
