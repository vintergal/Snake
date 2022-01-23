from Snake import SnakeNode
from ConstantAndImports import *

def is_wrong_press(current_direction, pressed_direction):
    if not pressed_direction in [ARROW_RIGHT_CODE,ARROW_LEFT_CODE,ARROW_UP_CODE,ARROW_DOWN_CODE]:
        return True
    if pressed_direction == ARROW_RIGHT_CODE and current_direction==ARROW_LEFT_CODE:
        return True
    elif pressed_direction == ARROW_LEFT_CODE and current_direction==ARROW_RIGHT_CODE:
        return True
    elif pressed_direction == ARROW_UP_CODE and current_direction==ARROW_DOWN_CODE:
        return True
    elif pressed_direction == ARROW_DOWN_CODE and current_direction==ARROW_UP_CODE:
        return True
    elif pressed_direction == current_direction:
        return True

    return False


def is_player_bite_itself(snake_head: SnakeNode):
    head_pos_x=snake_head.pos_x
    head_pos_y=snake_head.pos_y
    node_iterator=snake_head.next
    while node_iterator is not None:
        if head_pos_x==node_iterator.pos_x and head_pos_y==node_iterator.pos_y:
            print("bitten itself")
            return True
        node_iterator=node_iterator.next
    return False


def is_player_out_of_bound(snake_head: SnakeNode):
    if snake_head.pos_x == 0:
        print("out of bound")
        return True
    if snake_head.pos_y == 0:
        print("out of bound")
        return True
    if snake_head.pos_x == Board_WIDTH:
        print("out of bound")
        return True
    if snake_head.pos_y == BOARD_HEIGHT:
        print("out of bound")
        return True

    return False


def is_player_lost(snake_head: SnakeNode):
    return is_player_out_of_bound(snake_head) or is_player_bite_itself(snake_head)
