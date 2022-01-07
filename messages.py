import pygame
from screen import Screen
from colors import Colors

class Messages:
    def __init__(self, display) -> None:
        self.display = display


    def show_end_game(self):
        font = pygame.font.SysFont('gabriola', 42)

        maint_text = font.render('Game over', True, Colors.WHITE)
        maint_text_rect = maint_text.get_rect()
        maint_text_rect.center = (Screen.WIDTH//2, Screen.HEIGHT//2)

        instruction_text = font.render('Press p to play again', True, Colors.WHITE)
        instruction_text_rect = instruction_text.get_rect()
        instruction_text_rect.center = (Screen.WIDTH//2, Screen.HEIGHT//2 + 50)        

        self.display.blit(maint_text, maint_text_rect)
        self.display.blit(instruction_text, instruction_text_rect)