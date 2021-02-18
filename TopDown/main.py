from config import SCREEN_HEIGHT, SCREEN_WIDTH
from Input import Get, input_to
from Game import Game
import time
import os

getch = Get()
game = Game()
start_time = time.time()

def set():
    print(f'\033[{SCREEN_HEIGHT+1};{1}H', end='')

os.system('clear')
while True:
    c = input_to(getch, timeout=0.1)
    game.handle_input(c)
    game.render()
    if game.quit:
        break
    set()
    print("lives:", game.lives, "score:", game.score)

print("GAME OVER!")
print("total time:", int(time.time()-start_time))
print("total brick score:", game.score)
print("total lives left:", game.lives)
