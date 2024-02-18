"""
This script contains and handles all the stylings for the documents.
"""
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib import colors

styles = getSampleStyleSheet()

def register_custom_font(font_path, font_name):
    pdfmetrics.registerFont(TTFont(font_name, font_path))

register_custom_font('assets/fonts/NeueMontreal.ttf', 'NeueMontreal')
register_custom_font('assets/fonts/F37ZagmaMonoTrial-Light.ttf', 'F37 Zagma Mono Trial')
register_custom_font('assets/fonts/NeueMontreal-Light.ttf', 'NeueMontreal-Light')

def get_small_text_styling(
    name='small_text', 
    fontName="F37 Zagma Mono Trial",
    fontSize=8,
    parent_style='Normal',
    spaceBefore=4.4,
    spaceAfter=4.4,
    backColor=None,
    textTransform='uppercase',
    **kwargs
):
    SMALL_TEXT_STYLE = ParagraphStyle(
        **kwargs,
        name=name, 
        fontName=fontName,
        fontSize=fontSize,
        spaceBefore=spaceBefore,
        spaceAfter=spaceAfter,
        backColor=backColor,
        textTransform=textTransform,
        parent=styles[parent_style]
    )
    return SMALL_TEXT_STYLE

def get_header_styling(
    name='header',
    fontName="NeueMontreal",
    fontSize=40,
    parent=styles['Heading1'],
    alignment=TA_LEFT,
    spaceBefore=10,
    **kwargs
):
    HEADER_STYLE=ParagraphStyle(
        **kwargs,
        name=name,
        fontName=fontName,
        fontSize=fontSize,
        parent=parent,
        alignment=alignment,
        spaceBefore=spaceBefore
    )
    return HEADER_STYLE

def get_normal_text_styling(
    name='normal_text',
    fontName="NeueMontreal-Light",
    fontSize=10,
    parent_style='Normal',
    alignment=TA_JUSTIFY,
    spaceBefore=10,
    spaceAfter=10,
    borderPadding=0,
    **kwargs
):

    NORMAL_TEXT_STYLE = ParagraphStyle(
        **kwargs,
        name=name,
        fontName=fontName,
        fontSize=fontSize,
        parent=styles[parent_style],
        alignment=alignment,
        spaceBefore=spaceBefore,
        spaceAfter=spaceAfter,
        borderPadding=borderPadding
    )
    return NORMAL_TEXT_STYLE

TABLE_STYLE = TableStyle([
    ('LINEBELOW', (0,-1), (-1,-1), 2, colors.gray),
    ('LINEBELOW', (0, 1), (-1, 1), 1, colors.gray),
    ('LINEBELOW', (0, 0), (-1, 0), 1, colors.gray),
    ('LEFTPADDING', (0, 0), (0, 0), 1, colors.gray),
    ('LEFTPADDING', (0, 1), (0, 1), 1, colors.gray),
    ('LEFTPADDING', (0, 2), (0, 2), 1, colors.gray),
])