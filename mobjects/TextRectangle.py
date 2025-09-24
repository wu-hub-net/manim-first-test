from manim import *
from .TextShape import TextShape

class TextRectangle(TextShape):
    def __init__(self, color=RED, front_color=WHITE, text='null', width=2, height=1, text_scale=0.5, **kwargs):
      shape = Rectangle(width=width, height=height)
      super().__init__(shape, color=color, front_color=front_color, text=text, text_scale=text_scale, **kwargs)
      self.__width = width
      self.__height = height
# set
    def set_width(self, width):
      self.__width = width
      self[0].stretch(width/self[0].width,0)
    def set_height(self, height):
      self.__height = height
      self[0].stretch(height/self[0].height,1)
# set-animate
    def change_width(self,width):
      self.__width = width
      return self[0].animate.stretch(width/self[0].width,0)
    def change_height(self,height):
      self.__height = height
      return self[0].animate.stretch(height/self[0].height,1)
# get
    def get_width(self):
      return self.__width
    
    def get_height(self):
      return self.__height