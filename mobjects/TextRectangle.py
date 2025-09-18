from manim import *

class TextRectangle(VGroup):
  text_scale=0.5
  def __init__(self, rect_color=RED, front_color=WHITE, text='null', width=2, height=2,text_scale=0.5,**kwargs):
    super().__init__(**kwargs)
    rectangle = Rectangle(width=width, height=height, color=rect_color,fill_opacity=0.5)
    text = Text(text, opacity=0.5, color=front_color).scale(text_scale)
    text.move_to(rectangle.get_center())
    self.add(rectangle, text)
    self.__front_color=front_color
    self.__rect_color=rect_color
    self.__text_scale=text_scale
    self.__text = text
    self.__width = width
    self.__height = height
  #set
  def set_rect_color(self, color):
    self.__rect_color = color
    self[0].set_color(color)
  #
  def set_front_color(self, color):
    self.__front_color = color
    self[1].set_color(color)
  #
  def set_width(self, width):
    self.__width = width
    self[0].stretch(width/self[0].width,0)
  #
  def set_height(self, height):
    self.__height = height
    self[0].stretch(height/self[0].height,1)
  #set-animate
  def change_rect_color(self, color):
    self.__rect_color = color
    return self[0].animate.set_color(color)
  #
  def change_front_color(self, color):
    self.__front_color = color
    return self[1].animate.set_color(color)
  #
  def change_width(self,width):
    self.__width = width
    return self[0].animate.stretch(width/self[0].width,0)
  #
  def change_height(self,height):
    self.__height = height
    return self[0].animate.stretch(height/self[0].height,1)
  #
  def change_text(self, text):
    self.__text = text
    new_text = Text(text,color=self.__front_color).scale(self.text_scale).move_to(self[0].get_center())
    return ReplacementTransform(self[1], new_text)
  #get
  def get_rect_color(self):
    return self.__rect_color
  
  def get_front_color(self):
    return self.__front_color
  
  def get_width(self):
    return self.__width
  
  def get_height(self):
    return self.__height
  
  def get_text_scale(self):
    return self.__text_scale
  
  def get_text(self):
    return self.__text