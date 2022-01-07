import pygame
from sound import Sound
from food import Food

from snake import Snake
from text import Text


class Game:

    def __init__(self, display):
        self.display = display
        self.run = True
        self.pause = False
        self.snake = Snake(self.display)
        self.food = Food(self.display)
        self.clock = pygame.time.Clock()        
        self.text = Text(self.display)
        self.sound = Sound()

    def show_end_text(self):
        self.text.show_end()

    def run_game(self):
        
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False                    
                    elif not self.pause and event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:                    
                        self.snake.direct(event.key)
                    elif self.pause and event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        self.pause = False
                        self.snake = Snake(self.display)
                        self.food = Food(self.display)    

            if self.pause: 
                self.show_end_text()
                continue

            self.snake.move()

            if self.snake.self_bite() or self.snake.touched_border():
                self.pause = True
                self.show_end_text()
            else:
                if self.snake.eat(self.food):
                    self.sound.pick()
                    self.food = Food(self.display)
                self.display.fill((0,0,0))            
                self.snake.draw() 
                self.food.draw() 
            pygame.display.update()
            self.clock.tick(10)


