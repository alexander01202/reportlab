"""
This scripts begins the pdf generation
"""
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from generate_pdf import generate_pdf
from flowables import *

if __name__ == "__main__":
    filename = "output.pdf"
    canvas = Canvas(filename, pagesize=letter)
    page_flowables = [
        page1_frame1_flowables,
        page1_frame2_flowables,
        page1_frame3_flowables
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

    page_flowables = [
        page2_frame1_flowables
    ]
    generate_pdf(
        canvas=canvas, 
        page_flowables=page_flowables, 
        filename=filename, 
        frame_count=1,
        page_name='Assessment',
        page_index='2',
        background='#233137',
        primary_color=colors.white
    )
    canvas.showPage()
    canvas.save()
