from manim import *

class MobStack(VGroup):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.length = 0
  def push(self, mobject):
    if self.length > 0:
      top_mob = self[self.length-1]
    else:
      top_mob = None
    self.add(mobject)
    self.length += 1
    if top_mob is not None:
      return mobject.animate.next_to(top_mob, UP, buff=0)
    else:
      return mobject.animate.move_to(self.get_center())