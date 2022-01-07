import pygame
from screen import Screen

class Text:

    def __init__(self, display):
        self.display = display
    
    def show_end(self):
        end_font = pygame.font.SysFont('sahadeva', 32)
        end_text = end_font.render('Game over, press p to play again', True, (255, 255, 0), (0,0,0))
        end_text_rect = end_text.get_rect()
        end_text_rect.center = (Screen.WIDTH//2, Screen.HEIGHT // 2)
        self.display.blit(end_text, end_text_rect)