from manim import *
from mobjects.TextRectangle import TextRectangle
from mobjects.MobStack import MobStack
from mobjects.TextCircle import TextCircle
from mobjects.CircleTree import CircleTree
class Main(Scene):
  def construct(self):
    # 创建所有节点
    root_rect = TextRectangle(text="根节点", width=1, height=0.5)
    left_rect = TextRectangle(text="左孩子", width=1, height=0.5)
    right_rect = TextRectangle(text="右孩子", width=1, height=0.5)
    left_left_rect = TextRectangle(text="左左", width=1, height=0.5)
    left_right_rect = TextRectangle(text="左右", width=1, height=0.5)
    right_left_rect = TextRectangle(text="右左", width=1, height=0.5)
    right_right_rect = TextRectangle(text="右右", width=1, height=0.5)

    rectangles = [right_right_rect, right_left_rect, left_right_rect, left_left_rect, right_rect, left_rect, root_rect]

    # 创建栈
    stack = MobStack()
    self.add(stack)
    self.play(stack.stack_init())
    for rect in rectangles:
        self.play(stack.push(rect))

    # 创建树
    tree = CircleTree()
    def transform(rect, circle, parent=None, offset=DOWN):
        circle.move_to(rect.get_center())
        circle.shift(UP*0.5)
        self.play(ReplacementTransform(rect, circle))
        self.play(tree.add_tree_node_animate(circle, parent=parent, offset=offset))
        stack.pop_not_change()

    # 第一层
    root_circle = TextCircle(text="根节点", radius=0.5)
    transform(root_rect, root_circle)
    # 第二层
    left_circle = TextCircle(text="左孩子", radius=0.5)
    transform(left_rect, left_circle, parent=root_circle, offset=2*LEFT + DOWN)
    right_circle = TextCircle(text="右孩子", radius=0.5)
    transform(right_rect, right_circle, parent=root_circle, offset=2*RIGHT + DOWN)
    # 第三层
    left_left_circle = TextCircle(text="左左", radius=0.5)
    transform(left_left_rect, left_left_circle, parent=left_circle, offset=LEFT + DOWN)
    left_right_circle = TextCircle(text="左右", radius=0.5)
    transform(left_right_rect, left_right_circle, parent=left_circle, offset=RIGHT + DOWN)
    right_left_circle = TextCircle(text="右左", radius=0.5)
    transform(right_left_rect, right_left_circle, parent=right_circle, offset=LEFT + DOWN)
    right_right_circle = TextCircle(text="右右", radius=0.5)
    transform(right_right_rect, right_right_circle, parent=right_circle, offset=RIGHT + DOWN)