from manim import *

class MobStack(VGroup):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.length = 0
    self.__init_status = False
    
  def stack_init(self,text='Stack',text_scale=0.5,text_color=WHITE):
    text = Text(text, opacity=0.5, color=text_color).scale(text_scale)
    self.add(text)
    self.length += 1
    text.animate.move_to(self.get_center())
    self.__init_status = True
    return Create(text)
  def push_prepare(self, mobject):
    return mobject.animate.next_to(self[self.length-1], UL, buff=0.5)
  def push(self, mobject):
    if(not self.__init_status):
      return None
    top_mob = self[self.length-1]
    self.add(mobject)
    self.length += 1
    if(self.length == 2):
      return mobject.animate.next_to(top_mob, UP, buff=0.1)
    return mobject.animate.next_to(top_mob, UP, buff=0)