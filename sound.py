import pygame

class Sound:
    def __init__(self) -> None:
        self.pick = pygame.mixer.Sound('assets/pickup.wav')

    def pickup(self):
        self.pick.play()