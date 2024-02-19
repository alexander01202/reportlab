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

class Styles:
    def __init__(self, primary_color=colors.black, secondary_color=colors.gray) -> None:
        self.primary_color = primary_color
        self.secondary_color = secondary_color

    def get_small_text_styling(
        self,
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
            textColor=self.primary_color,
            spaceBefore=spaceBefore,
            spaceAfter=spaceAfter,
            backColor=backColor,
            textTransform=textTransform,
            parent=styles[parent_style]
        )
        return SMALL_TEXT_STYLE

    def get_header_styling(
        self,
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
            textColor=self.primary_color,
            parent=parent,
            alignment=alignment,
            spaceBefore=spaceBefore
        )
        return HEADER_STYLE

    def get_normal_text_styling(
        self,
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
            textColor=self.primary_color,
            parent=styles[parent_style],
            alignment=alignment,
            spaceBefore=spaceBefore,
            spaceAfter=spaceAfter,
            borderPadding=borderPadding
        )
        return NORMAL_TEXT_STYLE

    def get_table_style(self):
        TABLE_STYLE = TableStyle([
            ('LINEBELOW', (0,-1), (-1,-1), 2, self.secondary_color),
            ('LINEBELOW', (0, 1), (-1, 1), 1, self.secondary_color),
            ('LINEBELOW', (0, 0), (-1, 0), 1, self.secondary_color),
            ('LEFTPADDING', (0, 0), (0, 0), 1, self.secondary_color),
            ('LEFTPADDING', (0, 1), (0, 1), 1, self.secondary_color),
            ('LEFTPADDING', (0, 2), (0, 2), 1, self.secondary_color)
        ])

        return TABLE_STYLE
    