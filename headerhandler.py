"""
This script creates and handles headers in a document.
"""

class HeaderHandler:

    def __init__(self, document, canvas, page_index:str, primary_color, secondary_color, font_name:str) -> None:
        self.c = canvas
        self.doc = document
        self.font_name = font_name
        self.secondary_color = secondary_color
        self.primary_color = primary_color
        self.page_index = page_index

    def add_navigation_path_to_page_header(self, paths:list[str], current_path:str, ellipsis=True):

        path_x_position = self.doc.leftMargin + 5
        path_y_position = self.doc.height + 2
        
        # Create a TextObject 
        textobject = self.c.beginText()

        for i, path in enumerate(paths):
            font_color = self.secondary_color
            if ellipsis and i > 0:
                self.add_ellipses_to_navigation_path(ellipsis_x=path_x_position, ellipsis_y=path_y_position)

            if path == current_path:
                font_color = self.primary_color

            # Set font, size, and color
            textobject.setFont(self.font_name, 10)
            textobject.setFillColor(font_color)
            textobject.setTextOrigin(path_x_position, path_y_position)

            textobject.textOut(path)
            self.c.drawText(textobject)
            textobject.moveCursor(15, 0) # add space in front of the text
            (x,y) = textobject.getCursor()
            string_width = self.c.stringWidth(path, self.font_name, 10)
            path_x_position, path_y_position = string_width + x, y # new text position 

        
        return path_x_position

    def add_ellipses_to_navigation_path(self, ellipsis_x, ellipsis_y) -> int:
        # Set the color and fill mode for the ellipse
        ellipse_x_size = 2
        self.c.setStrokeColor(self.secondary_color)
        self.c.setFillColor(self.secondary_color)

        # Define the initial position
        self.c.ellipse(
            (ellipsis_x - 7.5),
            ellipsis_y + 4,
            (ellipsis_x - 7.5) + ellipse_x_size,
            ellipsis_y + 2,
            fill=1
        )

    def add_page_index_to_page_header(self) -> None:

        self.c.setFont('NeueMontreal', 15)
        self.c.setFillColor(self.primary_color)
        self.c.drawString(self.doc.width, self.doc.height, self.page_index)

    def add_line_separator_to_page_header(self, page_topics_width:int):
        x1, y1 = page_topics_width, self.doc.height
        x2, y2 = self.doc.width, y1

        # Set line color and width
        self.c.setStrokeColor(self.secondary_color)  # Set line color to secondary color
        self.c.setLineWidth(0.5)  # Set line width to 0.5 points
        self.c.line(x1, y1+5, x2 - 10, y2+5)
