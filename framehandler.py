"""
This script creates and adds contents to a document's frame
"""
from reportlab.platypus import Frame

class FrameHandler:
    def __init__(self, canvas, document, frameHeight:int, frameWidth:int, frame_count=1) -> None:
        self.c = canvas
        self.doc = document
        self.frames = [] # contains a doc's frames
        self.frame_count = frame_count # number of frames in a doc
        self.frameHeight = frameHeight
        self.frameWidth = frameWidth

    def create_frames(self, showBoundary=0) -> list:
        for frame in range(self.frame_count):
            leftMargin = self.doc.leftMargin + frame * self.frameWidth
            bottomMargin = self.doc.bottomMargin

            # Define the frame
            frame = Frame(leftMargin, bottomMargin, self.frameWidth, self.frameHeight, showBoundary=showBoundary)
            self.frames.append(frame)

        return self.frames
    
    def add_flowable_to_frame(self, frame, flowable):
        frame.add(flowable, self.c)