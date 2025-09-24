import sys
import os
from manim import *
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from mobjects.TextRectangle import TextRectangle
from mobjects.MobStack import MobStack
from mobjects.TextCircle import TextCircle
from mobjects.CircleTree import CircleTree
from mobjects.TitleArea import TitleArea
class InsertionSort(Scene):
  def construct(self):
    title = Text("插入排序", font="Microsoft YaHei").scale(2)
    ta = TitleArea(config.frame_width, config.frame_height)
    anm = ta.move_up(title, scale=0.45,buff_y=0.3)
    self.play(Create(title))
    self.wait()
    self.play(anm)
    self.play(Create(ta.line))
    self.wait()
    # 建立x轴
    x_axis = NumberLine(
            x_range=[0, 10, 1],
            length=7,
            color=BLUE,
            include_numbers=False,
            label_direction=DOWN
        ).to_corner(DL)
    custom_lables = {
      i + 0.5: str(i)
      for i in range(0, 10)
    }
    x_axis.add_labels(custom_lables,direction=DOWN, buff=0.2)
    self.play(Create(x_axis))
    self.wait(1)
    # 建立数组
    arr = [5, 2, 8, 3, 1, 6, 4, 7, 9, 8]
    # 建立数组矩形
    rectangles = []
    for i,value in enumerate(arr):
        height = value * 0.3
        rect = TextRectangle(text=str(value), width=x_axis.get_unit_size(), height=height, color=BLUE, front_color=WHITE)
        rect.set_top_text()
        rectangles.append(rect)
    x_start = x_axis.get_start()
    x_end = x_axis.get_end()
    num_rectangles = len(rectangles)
    spacing = x_axis.get_unit_size()
    for i, rect in enumerate(rectangles):
            x = x_start[0] + spacing * (0.5 + i)
            y = x_start[1] + rect.height/2
            rect.move_to([x, y, 0]) 
            
    self.play(*[Create(rect) for rect in rectangles])
    self.wait(1)
    self.insertion_sort(x_axis,rectangles,arr,3.25)
  def insertion_sort(self,x_axis,rectangles,arr,prepare_height):
    for i in range(1, len(arr)):
        # 选择当前索引作为关键字
        key = arr[i]
        rectangle_key = rectangles[i]
        insert_x = rectangles[i].get_center()[0]
        self.play(rectangles[i].animate.shift(UP * prepare_height))
        # 插入到[1,i-1]的有序子数组中
        j = i - 1
        while j >= 0 and key < arr[j]:
            insert_x = rectangles[j].get_center()[0]
            arr[j + 1] = arr[j]
            anim1 = rectangles[j].animate.shift(RIGHT * rectangles[j].get_width())
            anim2 = rectangle_key.animate.shift(LEFT * rectangles[j].get_width())
            color1 = rectangles[j][0].animate(run_time=0.3).set_color(YELLOW)
            color2 = rectangle_key[0].animate(run_time=0.3).set_color(YELLOW)
            self.play(color1,color2)
            self.play(anim1,anim2)
            self.play(rectangles[j][0].animate(run_time=0.3).set_color(BLUE))
            rectangles[j + 1] = rectangles[j]
            j -= 1
        arr[j + 1] = key
        self.play(rectangle_key.animate.move_to([insert_x,x_axis.get_start()[1] + rectangle_key.height/2,0]))
        rectangles[j + 1] = rectangle_key