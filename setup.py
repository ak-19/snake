import pygame

from screen import Screen

class Setup:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake game')

    def get_display(self):
        return pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

    def quit(self):
        pygame.quit()
