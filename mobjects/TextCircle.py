from manim import *
from .TextShape import TextShape

class TextCircle(TextShape):
    def __init__(self, color=RED, front_color=WHITE, text='null', radius=1, text_scale=0.5, **kwargs):
        shape = Circle(radius=radius)
        super().__init__(shape, color=color, front_color=front_color, text=text, text_scale=text_scale, **kwargs)
    def set_radius(self, radius):
        self[0].scale(radius/self[0].radius)
    def change_radius(self, radius):     
        return self[0].animate.scale(radius/self[0].radius)