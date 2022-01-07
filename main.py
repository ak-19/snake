from game import Game
from setup import Setup


setup = Setup()

display = setup.get_display()

game = Game(display)

game.run_game_loop()

setup.quit()