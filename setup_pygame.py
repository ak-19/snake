import pygame
from screen import Screen

def setup():
    pygame.init()
    display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
    pygame.display.set_caption('Ante Snake game')
    return display, pygame.time.Clock()