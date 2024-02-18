"""
This script contains all the pdf's/documents' flowables.
"""
from reportlab.lib.units import inch
from docs_text import *
from styles import *
from reportlab.platypus import Image, Paragraph, Spacer, Table
from PIL import Image as Img
import io

footer_text_style = get_small_text_styling('footer', rightIndent=20, alignment=TA_JUSTIFY)
subtitle_text_style = get_small_text_styling(backColor="#EDEDED", rightIndent=100, alignment=TA_CENTER)

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


# PAGE ONE ==> FRAME 1
page1_frame1_flowables = [
    Paragraph(PAGE_ONE_SUBTITLE, subtitle_text_style),
    Paragraph(PAGE_ONE_TITLE, get_header_styling()),
    Spacer(1, 8 * inch),
    Paragraph(PAGE_ONE_COLUMN_ONE_FOOTER_TEXT, footer_text_style),
]


# PAGE ONE ==> FRAME 2
frame2_image = "assets/images/left_image.jpg"
cropped_image = crop_image(input_image_path=frame2_image)

body_paragraphs = PAGE_ONE_BODY.split('\n')
total_paragraphs_per_frame = len(body_paragraphs) // 2
frame2_body_paragraph = body_paragraphs[:total_paragraphs_per_frame]

page1_frame2_flowables = [
    Paragraph(PAGE_ONE_SUBHEADING, get_normal_text_styling()),
    *[
        Paragraph(frame2_paragraph, get_normal_text_styling()) 
        for frame2_paragraph in frame2_body_paragraph
    ],
    Spacer(1, 2.9 * inch),
    Image(cropped_image, width=2*inch, height=2*inch, hAlign='RIGHT')
]

# PAGE ONE ==> FRAME 3
frame3_image = "assets/images/left_image.jpg"
cropped_image = crop_image(input_image_path=frame3_image)

frame3_body_paragraph = body_paragraphs[total_paragraphs_per_frame:]

page1_frame3_flowables = [
    Paragraph('', get_normal_text_styling(spaceAfter=21.2)),
    *[
        Paragraph(frame3_paragraph, get_normal_text_styling(borderPadding=10)) 
        for frame3_paragraph in frame3_body_paragraph
    ],
    Spacer(1, 2.79 * inch),
    Image(cropped_image, width=2*inch, height=2*inch, hAlign='LEFT')
]

# PAGE TWO ==> FRAME 1
wrap = []
for i, (cell1,cell2,cell3) in enumerate(PAGE_TWO_TABLE):
    if i < 1:
        wrap.append([
            Paragraph(cell1,get_small_text_styling(textColor='white')),
            Paragraph(cell2,get_small_text_styling(textColor='white')),
            Paragraph(cell3, get_small_text_styling(textColor='white'))
        ])
    else:
        wrap.append([
            Paragraph(cell1,get_small_text_styling(textColor='white', fontName='NeueMontreal', textTransform='capitalize')),
            Paragraph(cell2,get_small_text_styling(textColor='white', fontName='NeueMontreal', textTransform='capitalize')),
            Paragraph(cell3, get_small_text_styling(textColor='white',fontName='NeueMontreal', textTransform='capitalize'))
        ])

page2_frame1_flowables = [
    Paragraph(PAGE_ONE_SUBTITLE, get_small_text_styling(backColor="#ADC3CA", rightIndent=490, alignment=TA_CENTER)),
    Paragraph(PAGE_TWO_TITLE, get_header_styling(textColor='white',leading=40, rightIndent=350)),
    Spacer(1, 1.2 * inch),
    Paragraph(PAGE_TWO_BODY, get_normal_text_styling(rightIndent=200, textColor='white',firstLineIndent=60, leading=20, alignment=TA_LEFT, fontSize=20, fontName='NeueMontreal')),
    Paragraph('Summary of Tests', get_small_text_styling(textColor='white',fontName='NeueMontreal',textTransform='capitalize', spaceBefore=300, alignment=TA_LEFT)),
    Table(wrap, spaceBefore=10, style=TABLE_STYLE)
]
