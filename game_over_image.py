import pygame
from colors import Colors

def getImage():
    font_style = pygame.font.SysFont('freesans', 24)
    return font_style.render('You lost, press "P" to play again or "Q" for exit', True, Colors.RED)
