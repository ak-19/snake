import pygame
from collections import deque

from pygame.constants import K_RIGHT
from screen import Screen

class Snake:
    def __init__(self, display):
        self.display = display
        self.body = deque([(Screen.WIDTH//2, Screen.HEIGHT // 2)])
        self.dx = 0
        self.dy = 1

    def draw(self):
        for i, b in enumerate(self.body):
            x, y = b
            color = (255,255,0)
            if i == len(self.body) - 1:
                color = (255,0,0)
            pygame.draw.rect(self.display, color, (x, y, Screen.BOX,Screen.BOX), width=0)

    def self_bite(self):
        x, y = self.body[-1]
        for i in range(len(self.body) - 1):
            xx, yy = self.body[i]
            if xx == x and yy == y:
                return True
        
        return False

    def move(self):
        x = self.body[-1][0] + self.dx * Screen.BOX
        y = self.body[-1][1] + self.dy * Screen.BOX
        self.body.append((x, y))
        self.body.popleft()

    def move_without_cut(self):
        x = self.body[-1][0] + self.dx * Screen.BOX
        y = self.body[-1][1] + self.dy * Screen.BOX
        self.body.append((x, y))

    def touched_border(self):
        x, y = self.body[-1]
        
        if x < 0 or y < 0: return True

        if x + Screen.BOX > Screen.WIDTH or y + Screen.BOX > Screen.HEIGHT:
            return True

        return False
            
    def direct(self, key):
        if key == pygame.K_LEFT:
            self.dx = -1
            self.dy = 0
        elif key == pygame.K_RIGHT:
            self.dx = 1
            self.dy = 0            
        elif key == pygame.K_DOWN:
            self.dx = 0
            self.dy = 1            
        elif key == pygame.K_UP:
            self.dx = 0
            self.dy = -1

    def eat(self, food):
        x, y = self.body[-1]
        if x == food.x and y == food.y:
            self.move_without_cut()
            return True

        return False