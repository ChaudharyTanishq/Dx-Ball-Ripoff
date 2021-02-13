from Components.Ball import Ball
from Helpers.main import Game
from Components.Bar import Bar
from Components.Frame import Frame

from config import SCREEN
from Input import Get, input_to

import time

getch = Get()
game = Game(SCREEN)

while True:
    c = input_to(getch)
    game.handle_input(c)
    if game.c == 'q': break
    if game.render():
        break
    time.sleep(0.1)
