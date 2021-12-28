
from ConstantAndImports import *


class SnakeNode:

    next = None
    node_graphic = None
    canvas = None
    index=-1

    def __init__(self, pos_x, pos_y, canvas, is_head:bool = False):
        self.next=None
        self.canvas=canvas
        self.node_graphic=canvas.create_oval(pos_x, pos_y, pos_x+SNAKE_BODY_PART_R, pos_y+SNAKE_BODY_PART_R, fill="red"if is_head else "white")

    def add_node(self, pos_x=-1, pos_y=-1):
        if self.next is None:
            coords=self.canvas.coords(self.node_graphic)
            if pos_x == -1:
                pos_x=int(coords[0])
            if pos_y == -1:
                pos_y = int(coords[1]) + STEP
            self.next=SnakeNode(pos_x=pos_x, pos_y=pos_y, canvas=self.canvas)
        else:
            self.next.add_node(pos_x=pos_x, pos_y=pos_y)



    @staticmethod
    def initSnake(head, nodes_after_head: int = 5):
        i=0
        for i in range(nodes_after_head):
            head.add_node()

