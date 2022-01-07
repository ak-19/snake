import pygame

from food import Food
from messages import Messages
from snake import Snake
from colors import Colors
from sound import Sound

class Game:

    def __init__(self, display) -> None:
        self.display =  display
        self.run = True
        self.paused = False
        self.snake = Snake(display)
        self.food = Food(display)
        self.clock = pygame.time.Clock()
        self.sound = Sound()
        self.text = Messages(display)

    def  run_game_loop(self):

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type  == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False
                elif event.type  == pygame.KEYDOWN and self.paused and event.key == pygame.K_p:                
                    self.snake = Snake(self.display)
                    self.food = Food(self.display)
                    self.paused = False
                elif event.type  == pygame.KEYDOWN:
                    self.snake.direct(event.key)

            if self.paused:                 
                self.display.fill(Colors.BLACK)                
                self.text.show_end_game()
                pygame.display.update()
                self.clock.tick(10)                
                continue

            self.snake.move()

            if self.snake.failed():
                self.paused = True
                continue

            if self.snake.eaten_food(self.food):
                self.sound.pickup()
                self.food = Food(self.display)

            self.display.fill(Colors.BLACK)

            self.food.draw()
            self.snake.draw()

            pygame.display.update()
            self.clock.tick(10)


