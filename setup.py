import pygame

from screen import Screen


class Setup:

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Snake game')
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

    def quit(self):
        pygame.quit()

    def get_display(self):
        return self.display
