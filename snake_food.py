from random import randint
from screen import Screen

class SnakeFood:
    def __init__(self) -> None:
        self.x = 10 * randint(0, Screen.WIDTH//10 - 10)
        self.y = 10 * randint(0, Screen.HEIGHT//10 - 10)