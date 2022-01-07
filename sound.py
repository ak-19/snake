import pygame

class Sound:

    def __init__(self):
        self.pickup = pygame.mixer.Sound('assets/pickup.wav')

    def pick(self):
        self.pickup.play()