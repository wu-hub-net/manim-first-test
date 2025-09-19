from manim import *

class TextShape(VGroup):
    def __init__(self, shape, color=RED, front_color=WHITE, text='null', text_scale=0.5, **kwargs):
        super().__init__(**kwargs)
        shape.set_color(color)
        shape.set_fill(color, opacity=0.5)
        text_obj = Text(text, opacity=0.5, color=front_color).scale(text_scale)
        text_obj.move_to(shape.get_center())
        self.add(shape, text_obj)
        self.__shape = shape
        self.__front_color = front_color
        self.__color = color
        self.__text_scale = text_scale
        self.__text = text
# set
    def set_shape_color(self, color):
        self.__color = color
        self[0].set_color(color)

    def set_front_color(self, color):
        self.__front_color = color
        self[1].set_color(color)
# set-animate
    def change_shape_color(self, color):
        self.__color = color
        return self[0].animate.set_color(color)

    def change_front_color(self, color):
        self.__front_color = color
        return self[1].animate.set_color(color)

    def change_text(self, text):
        self.__text = text
        new_text = Text(text, color=self.__front_color).scale(self.__text_scale).move_to(self[0].get_center())
        return ReplacementTransform(self[1], new_text)
# get
    def get_shape_color(self):
        return self.__color

    def get_front_color(self):
        return self.__front_color

    def get_text_scale(self):
        return self.__text_scale

    def get_text(self):
        return self.__text