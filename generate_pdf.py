"""
This scripts generates the pdf document
"""
from reportlab.platypus import BaseDocTemplate, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from docs_text import *
from flowables import *
from headerhandler import HeaderHandler
from framehandler import FrameHandler

styles = getSampleStyleSheet()

def generate_pdf(
        canvas, 
        page_flowables:list[list],
        frame_count:int,
        filename:str, 
        page_name:str, 
        page_index:str, 
        background='#FFFFFF', 
        primary_color=colors.black,
        secondary_color=colors.lightgrey,
        primary_font='NeueMontreal'
    ):

    canvas.setFillColor(background)
    canvas.rect(0, 0, letter[0], letter[1], fill=1)
    page_name = page_name.capitalize()

    # Create a PDF document
    doc = BaseDocTemplate(
        filename,
        pagesize=letter,
        rightMargin = 12,
        leftMargin = 12,
        topMargin = 12,
        bottomMargin = 12
    )

    header_handler = HeaderHandler(doc, canvas, page_index, primary_color, secondary_color, font_name=primary_font)
    navigation_path = PAGE_NAVIGATIONS[FIRST_PATH] + PAGE_NAVIGATIONS[SECOND_PATH] + PAGE_NAVIGATIONS[page_name]
    navigation_path_width = header_handler.add_navigation_path_to_page_header(navigation_path, current_path=page_name)

    header_handler.add_page_index_to_page_header()
    header_handler.add_line_separator_to_page_header(navigation_path_width)

    frameHeight = doc.height - 50
    frameWidth = (doc.width/frame_count)

    frame_handler = FrameHandler(
        canvas, 
        frameHeight=frameHeight, 
        frameWidth=frameWidth, 
        document=doc, 
        frame_count=frame_count
    )
    frames = frame_handler.create_frames()

    # Create a list to hold the contents of the PDF
    page1_frame1_flowables.append(Spacer(0, doc.leftMargin))

    for i, frame_flowables in enumerate(page_flowables):
        frame_handler.add_FlowablesList_to_frame(frame=frames[i], flowables= frame_flowables)
