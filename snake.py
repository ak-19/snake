import pygame

from collections import deque
from random import randint
from colors import Colors
from screen import Screen

class Snake:

    def __init__(self, display) -> None:
        self.display = display
        x = Screen.BOX * randint(0, Screen.WIDTH // Screen.BOX - Screen.BOX)
        y = Screen.BOX * randint(0, Screen.HEIGHT //  Screen.BOX - Screen.BOX)
        self.body = deque([(x, y)])
        self.dx = 0
        self.dy = 1
    
    def move(self):
        x, y = self.body[-1]
        x += self.dx * Screen.BOX
        y += self.dy * Screen.BOX
        self.body.append((x, y))
        self.body.popleft()

    def draw(self):
        for i in range(len(self.body)):
            x, y = self.body[i]
            color = Colors.BODY_COLOR
            if i == len(self.body) - 1:
                color = Colors.RED
            pygame.draw.rect(self.display, color, (x, y, Screen.BOX, Screen.BOX))

    def direct(self, key):
        if key == pygame.K_UP:
            self.dx = 0
            self.dy = -1            
        elif key == pygame.K_DOWN:
            self.dx = 0
            self.dy = 1                        
        elif key == pygame.K_LEFT:
            self.dx = -1
            self.dy = 0                                   
        elif key == pygame.K_RIGHT:
            self.dx = 1
            self.dy = 0            


    def eaten_food(self, food):
        x, y = self.body[-1]

        if x == food.x and y == food.y:
            self.move_without_cut()
            return True

        return False

    def move_without_cut(self):
        x, y = self.body[-1]
        x += self.dx * Screen.BOX
        y += self.dy * Screen.BOX
        self.body.append((x, y))

    def failed(self):
        x, y = self.body[-1]

        if x < 0 or y < 0: 
            return True
        if x + Screen.BOX > Screen.WIDTH or y + Screen.BOX > Screen.HEIGHT: 
            return True

        for i in range(len(self.body) - 1):
            xx, yy = self.body[i]
            if x == xx and y == yy:
                return True

        return False