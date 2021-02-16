from Input import Get, input_to
from Game import Game

import time
import os

getch = Get()
game = Game()
start_time = time.time()

os.system('clear')
while True:
    c = input_to(getch, timeout=0.1)
    game.handle_input(c)
    game.render()

    if game.quit:
        break

print("total time:", int(time.time()-start_time))
print("total brick score:", game.score)
print("total lives left:", game.lives)
