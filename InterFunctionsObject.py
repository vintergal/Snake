
from Snake import SnakeNode
import threading
from ConstantAndImports import *


class InterFunctionsObject:
    def __init__(self,snake_head: SnakeNode, event_player_lost: threading.Event, lock: threading.Lock,turns_queue: Queue, is_moved_from_changed_direction: bool = False):
        self.snake_head=snake_head
        self.event_player_lost=event_player_lost
        self.lock=lock
        self.is_moved_from_changed_direction=is_moved_from_changed_direction
        self.turns_queue=turns_queue
