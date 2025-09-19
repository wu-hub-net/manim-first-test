from manim import *
import numpy as np

class CircleTree(VGroup):
    def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.nodes = []
      self.edges = []
      self.relations = []
    # 添加节点及连线
    def add_tree_node(self, node, parent=None, offset=DOWN):
      self.add(node)
      self.nodes.append(node)
      child_idx = len(self.nodes) - 1
      if parent:
        node.next_to(parent, offset)
        # 连线方向
        direction = node.get_center() - parent.get_center()
        direction = direction / np.linalg.norm(direction)
        parent_radius = parent[0].radius
        node_radius = node[0].radius
        # 连线起止点为圆边缘
        start = parent.get_center() + direction * parent_radius
        end = node.get_center() - direction * node_radius
        edge = Line(start, end)
        self.add(edge)
        self.edges.append(edge)
        edge_idx = len(self.edges) - 1
        parent_idx = self.nodes.index(parent)
        self.relations.append({
          "parent_idx": parent_idx,
          "child_idx": child_idx,
          "edge_idx": edge_idx
        })
      else:
        node.move_to(ORIGIN)
    def add_tree_node_animate(self, node, parent=None, offset=DOWN):
        self.add(node)
        self.nodes.append(node)
        child_idx = len(self.nodes) - 1
        animations = []
        if parent:
            # 先计算目标位置
            target_pos = parent.get_center() + offset
            move_anim = node.animate.move_to(target_pos)
            # 计算连线方向
            direction = target_pos - parent.get_center()
            direction = direction / np.linalg.norm(direction)
            parent_radius = parent[0].radius
            node_radius = node[0].radius
            start = parent.get_center() + direction * parent_radius
            end = target_pos - direction * node_radius
            edge = Line(start, end)
            self.add(edge)
            self.edges.append(edge)
            edge_idx = len(self.edges) - 1
            parent_idx = self.nodes.index(parent)
            self.relations.append({
                "parent_idx": parent_idx,
                "child_idx": child_idx,
                "edge_idx": edge_idx
            })
            animations.append(move_anim)
            animations.append(Create(edge))
        else:
            move_anim = node.animate.move_to(ORIGIN)
            animations.append(move_anim)
        return AnimationGroup(*animations)
    # 查找父节点
    def find_parent(self, child_node):
        child_idx = self.nodes.index(child_node)
        for rel in self.relations:
            if rel["child_idx"] == child_idx:
                return self.nodes[rel["parent_idx"]]
        return None

    # 查找子节点
    def find_children(self, parent_node):
        parent_idx = self.nodes.index(parent_node)
        return [self.nodes[rel["child_idx"]] for rel in self.relations if rel["parent_idx"] == parent_idx]

    # 该节点入边
    def find_in_edge(self, child_node):
        child_idx = self.nodes.index(child_node)
        for rel in self.relations:
            if rel["child_idx"] == child_idx:
                return self.edges[rel["edge_idx"]]
        return None

    # 查找该结点的出边
    def find_out_edges(self, parent_node):
        parent_idx = self.nodes.index(parent_node)
        return [self.edges[rel["edge_idx"]] for rel in self.relations if rel["parent_idx"] == parent_idx]