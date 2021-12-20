import tkinter as tk
SNAKE_HEAD_INITIAL_POS_X=250
SNAKE_HEAD_INITIAL_POS_Y=250
SNAKE_BODY_PART_R=10


window=tk.Tk()
window.title(string="snake")


c_game_board=tk.Canvas(master=window, bg="black", height=500,width=500, )
oval = c_game_board.create_oval(SNAKE_HEAD_INITIAL_POS_X, SNAKE_HEAD_INITIAL_POS_Y, SNAKE_HEAD_INITIAL_POS_X+SNAKE_BODY_PART_R, SNAKE_HEAD_INITIAL_POS_Y+SNAKE_BODY_PART_R, fill="red")
c_game_board.pack()
tk.mainloop()
