
from Snake import *
import threading
import time





def handle_keypress(event, canvas, snake_head):
    if (event.keycode==ARROW_RIGHT_CODE):
        canvas.move(snake_head, STEP, 0)
    elif (event.keycode==ARROW_LEFT_CODE):
        canvas.move(snake_head, -STEP, 0)
    elif (event.keycode==ARROW_UP_CODE):
        canvas.move(snake_head, 0, -STEP)
    elif (event.keycode==ARROW_DOWN_CODE):
        canvas.move(snake_head, 0, STEP)



window=tk.Tk()
window.title(string="snake")

c_game_board=tk.Canvas(master=window, bg="black", height=500,width=500)
c_game_board.pack()
snake_head = SnakeNode(SNAKE_HEAD_INITIAL_POS_X,SNAKE_HEAD_INITIAL_POS_Y,c_game_board,is_head=True)
SnakeNode.initSnake(snake_head, 2)


window.bind("<Key>", lambda event, canvas_param=c_game_board, snake_head_param=snake_head.node_graphic: handle_keypress(event, canvas_param, snake_head_param))
tk.mainloop()
