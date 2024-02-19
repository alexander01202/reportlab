"""
This script contains all the pdf's/documents' flowables.
"""
from reportlab.lib.units import inch
from docs_texts import *
from styles import Styles
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import Image, Paragraph, Spacer, Table
from PIL import Image as Img
import io

def crop_image(input_image_path, crop_box=(20, 20, 100, 100)):
    # Open the input image
    image = Img.open(input_image_path, mode='r')

    # Get the size of the image (width, height)
    image_width, image_height = image.size
    crop_height = 1000
    
    # Crop the image using the specified crop box
    cropped_image = image.crop((0,0,image_width, image_height - crop_height))

    # Convert the cropped image to bytes
    with io.BytesIO() as output:
        cropped_image.save(output, format=image.format)
        cropped_image_bytes = output.getvalue()
    
    return io.BytesIO(cropped_image_bytes)

class Flowables:

    def __init__(self, document, primary_color, secondary_color) -> None:
        self.doc = document
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.styles = Styles(primary_color, secondary_color)

    def get_page1_frame1_flowables(self):
        # PAGE ONE ==> FRAME 1
        footer_text_style = self.styles.get_small_text_styling('footer', rightIndent=20, alignment=TA_JUSTIFY)
        subtitle_text_style = self.styles.get_small_text_styling(backColor="#EDEDED", rightIndent=100, alignment=TA_CENTER)
        page1_frame1_flowables = [
            Paragraph(PAGE_ONE_SUBTITLE, subtitle_text_style),
            Paragraph(PAGE_ONE_TITLE, self.styles.get_header_styling()),
            Spacer(1, 8 * inch),
            Paragraph(PAGE_ONE_COLUMN_ONE_FOOTER_TEXT, footer_text_style),
            Spacer(0, self.doc.leftMargin)
        ]

        return page1_frame1_flowables

    def get_page1_frame2_flowables(self):
        # PAGE ONE ==> FRAME 2
        frame2_image = "assets/images/left_image.jpg"
        cropped_image = crop_image(input_image_path=frame2_image)

        body_paragraphs = PAGE_ONE_BODY.split('\n')
        total_paragraphs_per_frame = len(body_paragraphs) // 2
        frame2_body_paragraph = body_paragraphs[:total_paragraphs_per_frame]

        page1_frame2_flowables = [
            Paragraph(PAGE_ONE_SUBHEADING, self.styles.get_normal_text_styling()),
            *[
                Paragraph(frame2_paragraph, self.styles.get_normal_text_styling()) 
                for frame2_paragraph in frame2_body_paragraph
            ],
            Spacer(1, 2.9 * inch),
            Image(cropped_image, width=2*inch, height=2*inch, hAlign='RIGHT')
        ]
        return page1_frame2_flowables
    
    def get_page1_frame3_flowables(self):
        # PAGE ONE ==> FRAME 3
        frame3_image = "assets/images/left_image.jpg"
        cropped_image = crop_image(input_image_path=frame3_image)

        body_paragraphs = PAGE_ONE_BODY.split('\n')
        total_paragraphs_per_frame = len(body_paragraphs) // 2
        frame3_body_paragraph = body_paragraphs[total_paragraphs_per_frame:]

        page1_frame3_flowables = [
            Paragraph('', self.styles.get_normal_text_styling(spaceAfter=21.2)),
            *[
                Paragraph(frame3_paragraph, self.styles.get_normal_text_styling(borderPadding=10)) 
                for frame3_paragraph in frame3_body_paragraph
            ],
            Spacer(1, 2.79 * inch),
            Image(cropped_image, width=2*inch, height=2*inch, hAlign='LEFT')
        ]
        return page1_frame3_flowables
    
    def get_page2_frame1_flowables(self):
        # PAGE TWO ==> FRAME 1
        table_cell_style = self.styles.get_small_text_styling(fontName='NeueMontreal', textTransform='capitalize')
        table_header_style = self.styles.get_small_text_styling()
        wrap = []
        for i, (cell1,cell2,cell3) in enumerate(PAGE_TWO_TABLE):
            if i < 1:
                wrap.append([
                    Paragraph(cell1,table_header_style),
                    Paragraph(cell2,table_header_style),
                    Paragraph(cell3,table_header_style)
                ])
            else:
                wrap.append([
                    Paragraph(cell1,table_cell_style),
                    Paragraph(cell2,table_cell_style),
                    Paragraph(cell3,table_cell_style)
                ])

        page2_frame1_flowables = [
            Paragraph(PAGE_ONE_SUBTITLE, self.styles.get_small_text_styling(backColor="#ADC3CA", rightIndent=490, alignment=TA_CENTER)),
            Paragraph(PAGE_TWO_TITLE, self.styles.get_header_styling(leading=40, rightIndent=350)),
            Spacer(1, 1.2 * inch),
            Paragraph("<super>02/</super> Next Few Pages", self.styles.get_normal_text_styling(fontName='NeueMontreal',)),
            Paragraph(PAGE_TWO_BODY, self.styles.get_normal_text_styling(rightIndent=200, firstLineIndent=60, leading=20, alignment=TA_LEFT, fontSize=20, fontName='NeueMontreal')),
            Paragraph('Summary of Tests', self.styles.get_small_text_styling(fontName='NeueMontreal',textTransform='capitalize', spaceBefore=270, alignment=TA_LEFT)),
            Table(wrap, spaceBefore=10, style=self.styles.get_table_style())
        ]

        return page2_frame1_flowables
