from Helpers.main import Game
from Components.Bar import Bar
from Components.Frame import Frame

from config import SCREEN
from Input import Get, input_to

getch = Get()
frame = Frame()
frame.draw(SCREEN)
bar = Bar()
game = Game(SCREEN, bar)

while True:
    c = input_to(getch)
    game.handle_input(c)
    if game.c == 'q': break
    game.render()
