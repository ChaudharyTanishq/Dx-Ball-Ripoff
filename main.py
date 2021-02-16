from Input import Get, input_to
from Game import Game

getch = Get()
game = Game()

while True:
    c = input_to(getch, timeout=0.1)
    game.draw()    