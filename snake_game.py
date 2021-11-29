import pygame
from screen import Screen
from random import randint
from colors import Colors
from game_over_image import getImage
from setup_pygame import setup
from snake_food import SnakeFood
from snake import Snake

class SnakeGame:
    def __init__(self):
        self.snake_food = SnakeFood()
        self.display, self.clock = setup()
        self.game_over_image = getImage()
        self.setupGameStart()

    def setupGameStart(self): 
        self.snake_food = SnakeFood()
        self.game_run = True
        self.game_exit = False
        self.snake  = Snake(300, 200)
        self.dx, self.dy = 10, 0

    def draw(self):
        if self.game_run:
            self.display.fill(Colors.BLACK)                
            x, y = self.snake.head()       
            self.snake.draw(self.display)
            pygame.draw.rect(self.display, Colors.FOOD, (self.snake_food.x, self.snake_food.y, 10, 10))
        else:
            self.display.fill(Colors.OVER)  
            self.display.blit(self.game_over_image, [180,140])            
        pygame.display.update()

    def check_and_set_game_state(self):
        if self.snake.selfBite():
            self.game_run = False
        else:
            x, y = self.snake.head()       
            self.game_run = not (x < 0 or x > Screen.WIDTH - 10 or y < 0 or y > Screen.HEIGHT - 10)

    def updateCoordinates(self, key):
        if key == pygame.K_UP:
            self.dx = 0
            self.dy = -10            
        elif key == pygame.K_DOWN:
            self.dx = 0
            self.dy = 10
        elif key == pygame.K_RIGHT:                
            self.dx = 10
            self.dy = 0
        elif key == pygame.K_LEFT:                
            self.dx = -10
            self.dy = 0

    def howToContinue(self, key):
        if key == pygame.K_q:
            self.game_exit = True
        elif key == pygame.K_p:
            self.setupGameStart()

    def move(self):
        x,y = self.snake.head()
        x += self.dx
        y += self.dy

        if x == self.snake_food.x and y == self.snake_food.y:
            self.snake.moveWithExtension(self.dx, self.dy)
            self.snake_food = SnakeFood()
        else:
            self.snake.move(self.dx, self.dy)


    def game_update(self):
        self.check_and_set_game_state()

        if self.game_run: self.move()

        self.draw()     
        
    def game_loop(self):
        while self.game_run or self.game_exit == False:    
            
            for e in pygame.event.get():

                if e.type == pygame.QUIT:
                    self.game_run = False
                    self.game_exit = True

                elif e.type == pygame.KEYDOWN:
                    if self.game_run: 
                        self.updateCoordinates(e.key)
                    else: 
                        self.howToContinue(e.key)
                        
                if self.game_exit: 
                    pygame.quit()

            self.game_update()

            self.clock.tick(10)

        pygame.quit()