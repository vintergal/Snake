
from Snake import *
import threading
import time



def is_wrong_press(current_direction, pressed_direction):
    if pressed_direction == ARROW_RIGHT_CODE and current_direction==ARROW_LEFT_CODE:
        return True
    elif pressed_direction == ARROW_LEFT_CODE and current_direction==ARROW_RIGHT_CODE:
        return True
    elif pressed_direction == ARROW_UP_CODE and current_direction==ARROW_DOWN_CODE:
        return True
    elif pressed_direction == ARROW_DOWN_CODE and current_direction==ARROW_UP_CODE:
        return True

    return False

def is_player_lost(snake_head: SnakeNode):
    if snake_head.pos_x == Board_START_X:
        return True
    if snake_head.pos_x == Board_END_X:
        return True
    if snake_head.pos_y == Board_START_Y:
        return True
    if snake_head.pos_y == Board_END_Y:
        return True

    return False


def handle_keypress(event, snake_head, event_player_lost):
    if is_wrong_press(SnakeNode.direction, event.keycode):
        return
    if event_player_lost.isSet():
        return
    SnakeNode.direction=event.keycode
    snake_step(snake_head, event_player_lost)


def snake_step(snake_head: SnakeNode, event_player_lost: threading.Event):
    if SnakeNode.direction == ARROW_RIGHT_CODE:
        snake_head.move(STEP, 0)
    elif SnakeNode.direction == ARROW_LEFT_CODE:
        snake_head.move(-STEP, 0)
    elif SnakeNode.direction == ARROW_UP_CODE:
        snake_head.move(0, -STEP)
    elif SnakeNode.direction == ARROW_DOWN_CODE:
        snake_head.move(0, STEP)
    elif SnakeNode.direction == SPACE_CODE:
        snake_head.move(0, STEP)

    if is_player_lost(snake_head):
        event_player_lost.set()


def refresh_game(snake_head: SnakeNode, event_player_lost: threading.Event):
    while not event_player_lost.isSet():
        snake_step(snake_head, event_player_lost)
        is_player_lost(snake_head)

        time.sleep(0.1)



window=tk.Tk()
window.title(string="snake")

press_lock=threading.Lock()
event_player_lost_main=threading.Event()

c_game_board=tk.Canvas(master=window, bg="black", height=Board_END_X,width=Board_END_Y)
c_game_board.pack()
snake_head_main = SnakeNode(SNAKE_HEAD_INITIAL_POS_X,SNAKE_HEAD_INITIAL_POS_Y,c_game_board,is_head=True)
SnakeNode.initSnake(snake_head_main, 2)


window.bind("<Key>", lambda event, snake_head_param=snake_head_main, event_player_lost_param=event_player_lost_main: handle_keypress(event, snake_head_param, event_player_lost_param))
SnakeNode.lock=threading.Lock()
refresh_thread=threading.Thread(target=refresh_game, args=(snake_head_main, event_player_lost_main,))
refresh_thread.start()
tk.mainloop()



