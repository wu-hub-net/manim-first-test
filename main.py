from manim import *
from mobjects.TextRectangle import TextRectangle
class Main(Scene):
  def construct(self):
    trect = TextRectangle(text='文本矩形')
    self.play(Create(trect))
    self.wait(1)
    self.play(trect.change_rect_color(BLUE))
    self.wait(1)
    self.play(trect.change_width(4))
    self.wait(1)
    self.play(trect.change_height(1))
    self.wait(1)
    self.play(trect.change_text('新文本'))
    self.wait(1)
    self.wait(1)