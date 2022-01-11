
from ConstantAndImports import *


class SnakeNode:
    # static variable
    direction = ARROW_UP_CODE

    def __init__(self, pos_x, pos_y, canvas, is_head:bool = False):
        self.next=None
        self.canvas=canvas
        self.node_graphic=canvas.create_oval(pos_x, pos_y, pos_x+SNAKE_BODY_PART_R, pos_y+SNAKE_BODY_PART_R, fill="red"if is_head else "white")

    def add_node(self, pos_x=-1, pos_y=-1):
        if self.next is None:
            if pos_x == -1:
                pos_x=self.pos_x
            if pos_y == -1:
                pos_y = self.pos_y + STEP
            self.next=SnakeNode(pos_x=pos_x, pos_y=pos_y, canvas=self.canvas)
        else:
            self.next.add_node(pos_x=pos_x, pos_y=pos_y)

    def move(self, rel_pos_x=0,rel_pos_y=0):
        current_pos_x=self.pos_x
        current_pos_y=self.pos_y
        self.canvas.move(self.node_graphic, rel_pos_x, rel_pos_y)
        if self.next is not None:
            self.next.move(current_pos_x-self.next.pos_x, current_pos_y-self.next.pos_y)

    @property
    def pos_x(self):
        return self.canvas.coords(self.node_graphic)[0]

    @property
    def pos_y(self):
        return self.canvas.coords(self.node_graphic)[1]

    @staticmethod
    def initSnake(head, nodes_after_head: int = 5):
        i=0
        for i in range(nodes_after_head):
            head.add_node()

