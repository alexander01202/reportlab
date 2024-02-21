"""
This scripts generates the pdf document
"""
from reportlab.platypus import BaseDocTemplate, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from docs_texts import *
from flowables import *
from reportlab.lib import colors
from headerhandler import HeaderHandler
from framehandler import FrameHandler

styles = getSampleStyleSheet()

def add_header_grid(canvas, doc):
    canvas.setStrokeColor('#fcdce4')
    bottom_line_y_pos = doc.height - 16
    lines = [
        (doc.leftMargin, doc.height + 16, doc.width, doc.height + 16), 
        (doc.leftMargin, bottom_line_y_pos, doc.width, bottom_line_y_pos)
    ]
    canvas.lines(lines)

    return bottom_line_y_pos

def add_horizontal_body_grid(canvas, doc, prev_line_y_pos_end,num_of_grids = 13):
    canvas.setStrokeColor('#fcdce4')

    for _ in range(num_of_grids):
        starting_line = prev_line_y_pos_end - 60 if _ > 0 else prev_line_y_pos_end - 35
        ending_line = starting_line - 10
        
        lines = [
            (doc.leftMargin, starting_line, doc.width, starting_line), 
            (doc.leftMargin, ending_line, doc.width, ending_line)
        ]
        canvas.lines(lines)
        prev_line_y_pos_end = ending_line

def add_vertical_body_grid(canvas, doc, header_grid_y_pos_end, num_of_grids = 13):
    x_grid_spacing = (doc.width - (doc.leftMargin * 2)) / num_of_grids + 10
    y_grid_spacing = (doc.height - (doc.bottomMargin * 2)) / num_of_grids + 10

    beginning_of_line_y_axis = header_grid_y_pos_end - 35
    prev_line_x_pos_end = doc.leftMargin

    canvas.setStrokeColor('#fcdce4')
    for _ in range(13):
        
        x_pos_start = prev_line_x_pos_end + x_grid_spacing if _ > 0 else prev_line_x_pos_end
        x_pos_end = x_pos_start + 10

        lines = [
            (x_pos_start, doc.bottomMargin, x_pos_start, beginning_of_line_y_axis), 
            (x_pos_end, doc.bottomMargin, x_pos_end, beginning_of_line_y_axis)
        ]
        canvas.lines(lines)

        prev_line_x_pos_end = x_pos_end

def generate_pdf(
        doc,
        canvas, 
        page_flowables:list[list],
        frame_count:int,
        filename:str, 
        page_name:str, 
        page_index:str, 
        draw_line=False,
        background='#FFFFFF', 
        primary_color=colors.black,
        secondary_color=colors.lightgrey,
        primary_font='NeueMontreal'
    ):

    # Applies background colors to the canvas
    canvas.setFillColor(background)
    canvas.rect(0, 0, letter[0], letter[1], fill=1)

    page_name = page_name.capitalize()

    # Create PDF header
    header_handler = HeaderHandler(doc, canvas, page_index, primary_color, secondary_color, font_name=primary_font)
    navigation_path = PAGE_NAVIGATIONS[FIRST_PATH] + PAGE_NAVIGATIONS[SECOND_PATH] + PAGE_NAVIGATIONS[page_name]
    navigation_path_width = header_handler.add_navigation_path_to_page_header(navigation_path, current_path=page_name)

    header_handler.add_page_index_to_page_header()
    header_handler.add_line_separator_to_page_header(navigation_path_width)
    
    # Define Frame height and width
    frameHeight = doc.height - 50
    frameWidth = (doc.width/frame_count)

    if draw_line:
        header_grid_y_pos_end = add_header_grid(canvas, doc)
        frameHeight = header_grid_y_pos_end - 40
        add_horizontal_body_grid(canvas, doc, header_grid_y_pos_end)
        add_vertical_body_grid(canvas, doc, header_grid_y_pos_end)

    frame_handler = FrameHandler(
        canvas, 
        frameHeight=frameHeight, 
        frameWidth=frameWidth, 
        document=doc, 
        frame_count=frame_count
    )
    frames = frame_handler.create_frames()

    for i, frame_flowables in enumerate(page_flowables):
        frames[i].addFromList(frame_flowables, canvas)
