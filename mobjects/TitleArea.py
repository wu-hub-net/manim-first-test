from manim import *
import numpy as np
class TitleArea():
  def __init__(self,width,height):
    # 基于初始坐标从左上角开始
    self.__width = width
    self.__height = height
    self.__position = np.array([0 - width / 2,height / 2,0])
  def get_position(self):
    return self.__position
  def move_ur(self,mobject,buff_x = 0,buff_y = 0,line_buff = 0.1,scale = 1):
    end = self.__position + np.array([buff_x, -buff_y, 0])
    line_start = end + np.array([0, - mobject.height * scale - line_buff, 0])
    line_end = end + np.array([mobject.width * scale, - mobject.height * scale - line_buff, 0])
    line = Line(line_start,line_end,color=WHITE)
    self.line = line
    return mobject.animate.scale(scale).move_to(end, aligned_edge=UL),
  def move_up(self,mobject,buff_y = 0,line_buff = 0.1,scale=1):
    end = self.__position + np.array([self.__width / 2,0 - buff_y,0]) 
    line_start = end + np.array([- mobject.width * scale / 2, - mobject.height * scale - line_buff, 0])
    line_end = end + np.array([mobject.width * scale / 2, - mobject.height * scale - line_buff, 0])
    line = Line(line_start,line_end,color=WHITE)
    self.line = line
    return mobject.animate.scale(scale).move_to(end, aligned_edge=UP)