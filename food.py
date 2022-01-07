import pygame
from random import randint
from screen import Screen
from colors import Colors

class Food:

    def __init__(self, display) -> None:
        self.display = display
        self.x = Screen.BOX * randint(0, Screen.WIDTH // Screen.BOX - Screen.BOX)
        self.y = Screen.BOX * randint(0, Screen.HEIGHT //  Screen.BOX - Screen.BOX)

    def draw(self):
        pygame.draw.rect(self.display, Colors.GREEN, (self.x,self.y, Screen.BOX, Screen.BOX), width=0)