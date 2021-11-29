import pygame
from typing import Deque
from collections import deque as dq

from colors import Colors

class Snake:
    def __init__(self, x, y) -> None:
        self.body = dq()
        self.body.append((x,y))

    def move(self, dx, dy) -> None:
        self.moveWithExtension(dx, dy)
        self.body.popleft()

    def moveWithExtension(self, dx, dy) -> None:
        x,y = self.body[-1]
        x += dx
        y += dy
        self.body.append((x,y))

    def head(self):
        return self.body[-1]

    def selfBite(self):
        x, y = self.head()
        N = len(self.body)
        for i in range(N-1):
            if self.body[i] == self.head():
                return True
        return False 

    def draw(self, display):
        for x,y in self.body:
            pygame.draw.rect(display, Colors.ORANGE, (x, y, 10, 10))
