import tkinter as tk
from tkinter import messagebox
SNAKE_HEAD_INITIAL_POS_X=250
SNAKE_HEAD_INITIAL_POS_Y=250
SNAKE_BODY_PART_R=10
STEP=10

ARROW_RIGHT_CODE=39
ARROW_LEFT_CODE=37
ARROW_UP_CODE=38
ARROW_DOWN_CODE=40



def handle_keypress(event, canvas, snake_head):
    if (event.keycode==ARROW_RIGHT_CODE):
        canvas.move(snake_head, STEP, 0)

    if (event.keycode==ARROW_LEFT_CODE):
        canvas.move(snake_head, -STEP, 0)

    if (event.keycode==ARROW_UP_CODE):
        canvas.move(snake_head, 0, -STEP)

    if (event.keycode==ARROW_DOWN_CODE):
        canvas.move(snake_head, 0, STEP)

    #canvas.move(snake_head,SNAKE_BODY_PART_R,SNAKE_BODY_PART_R)


window=tk.Tk()
window.title(string="snake")

c_game_board=tk.Canvas(master=window, bg="black", height=500,width=500)
snake_head = c_game_board.create_oval(SNAKE_HEAD_INITIAL_POS_X, SNAKE_HEAD_INITIAL_POS_Y, SNAKE_HEAD_INITIAL_POS_X+SNAKE_BODY_PART_R, SNAKE_HEAD_INITIAL_POS_Y+SNAKE_BODY_PART_R, fill="red")
c_game_board.pack()

window.bind("<Key>", lambda event, canvas_param=c_game_board, snake_head_param=snake_head: handle_keypress(event, canvas_param, snake_head_param))
tk.mainloop()
