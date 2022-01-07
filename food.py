import pygame
from random import randint
from screen import Screen

class Food:
    def __init__(self, display):
        self.display = display
        self.x = 10 * randint(0, Screen.WIDTH//10 - Screen.BOX)
        self.y = 10 * randint(0, Screen.HEIGHT//10 - Screen.BOX)

    def draw(self):
        pygame.draw.rect(self.display, (0, 255, 0), (self.x,self.y,Screen.BOX, Screen.BOX))