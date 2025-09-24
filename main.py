from manim import *
from mobjects.TextRectangle import TextRectangle
from mobjects.MobStack import MobStack
from mobjects.TextCircle import TextCircle
from mobjects.CircleTree import CircleTree
from mobjects.TitleArea import TitleArea
class Main(Scene):
  def construct(self):
    title = Text("测试", font="Microsoft YaHei").scale(2)
    ta = TitleArea(config.frame_width, config.frame_height)
    anm = ta.move_up(title, scale=0.5,buff_y=0.3)

    self.play(Create(title))
    self.wait(0.5)
    self.play(anm)
    self.play(Create(ta.line))
    self.wait()
