from Helpers.main import Game

from config import SCREEN
from Input import Get, input_to

import time
import os

getch = Get()
game = Game(SCREEN)
for row in SCREEN:
    for char in row:
        print(char, end="")
    print()

while True:
    c = input_to(getch)
    game.handle_input(c)
    if game.c == 'q': break
    if game.render():
        break
