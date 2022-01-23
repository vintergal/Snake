import threading
from turtle import width

from Snake import SnakeNode
from checks import *
from ConstantAndImports import *
from queue import Queue
from InterFunctionsObject import InterFunctionsObject


def handle_keypress(event, refresh_thread: threading.Thread, inter_functions_object: InterFunctionsObject):
    # snake_head=inter_functions_object_param.snake_head
    to_change_direction = True
    if event.keycode == SPACE_CODE:
        # if inter_functions_object.event_player_lost.is_set():
        # inter_functions_object.event_player_lost.clear()
        # refresh_thread.start()
        # else:
        inter_functions_object.event_player_lost.set()
        to_change_direction=False


    if is_wrong_press(snake_head.direction, event.keycode):
        to_change_direction = False
        print("cant change direction wrong direction")
    if inter_functions_object.event_player_lost.isSet():
        to_change_direction = False
        print("cant change direction because lost")
    if to_change_direction:
        inter_functions_object.turns_queue.put(event.keycode)
        # snake_head.direction=event.keycode
        # print("changed direction")


def snake_step(inter_functions_object: InterFunctionsObject):
    snake_head = inter_functions_object.snake_head
    # print(snake_head.direction)
    if inter_functions_object.snake_head.direction == ARROW_RIGHT_CODE:
        snake_head.move(STEP, 0)
    elif snake_head.direction == ARROW_LEFT_CODE:
        snake_head.move(-STEP, 0)
    elif snake_head.direction == ARROW_UP_CODE:
        snake_head.move(0, -STEP)
    elif snake_head.direction == ARROW_DOWN_CODE:
        snake_head.move(0, STEP)
    elif snake_head.direction == SPACE_CODE:
        snake_head.move(0, STEP)
    # print(snake_head.pos_y)
    if is_player_lost(inter_functions_object.snake_head):
        inter_functions_object.event_player_lost.set()
        print("lost")
        return


def refresh_game(inter_functions_object: InterFunctionsObject):
    while not inter_functions_object.event_player_lost.isSet():

        with inter_functions_object.lock:
            if not inter_functions_object.turns_queue.empty():
                inter_functions_object.snake_head.direction = inter_functions_object.turns_queue.get()
            snake_step(inter_functions_object)
            time.sleep(0.05)

    print("dfg")


if __name__ == "__main__":
    window = tk.Tk()
    window.title(string="snake")
    window.minsize(width=Board_WIDTH, height=BOARD_HEIGHT + Board_START_Y)

    c_game_board = tk.Canvas(master=window, bg="black", height=BOARD_HEIGHT, width=Board_WIDTH)
    c_game_board.place(x=Board_START_X, y=Board_START_Y)
    snake_head = SnakeNode(SNAKE_HEAD_INITIAL_POS_X, SNAKE_HEAD_INITIAL_POS_Y, c_game_board, is_head=True)
    SnakeNode.initSnake(snake_head, 20)
    inter_functions_object_main = InterFunctionsObject(snake_head=snake_head, event_player_lost=threading.Event(),
                                                       turns_queue=Queue(), lock=threading.Lock())
    refresh_thread = threading.Thread(target=refresh_game, args=(inter_functions_object_main,))
    refresh_thread.daemon=True
    window.bind("<Key>", lambda event, refresh_thread_param=refresh_thread,
                                inter_functions_object_param=inter_functions_object_main:
    handle_keypress(event, refresh_thread=refresh_thread_param, inter_functions_object=inter_functions_object_main))

    refresh_thread.start()
    tk.mainloop()
