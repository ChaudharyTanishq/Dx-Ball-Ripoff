from colorama.ansi import Style
from config import POWERUPS, POWERUPS_BCOLOR, POWERUPS_FCOLOR, SCREEN_HEIGHT
import random


class Powerups():
    def __init__(self, x, y):
        self.position = (x, y)
        self.bcolor = POWERUPS_BCOLOR
        self.fcolor = POWERUPS_FCOLOR
        self.symbol = random.choice(POWERUPS)
    
    def reset(self):
        """
        resets the mouse pointer to 1, 1
        """
        print(f'\033[{SCREEN_HEIGHT+1};{1}H', end='')
        print()
    
    def color_string(self, reset):
        color = ' ' if reset else self.bcolor + self.fcolor + self.symbol
        return color + Style.RESET_ALL

    def draw(self, reset=False):
        x, y = self.position
        print(f'\033[{y+1};{x+1}H', end='')
        print(self.color_string(reset))
        self.reset()

    def move(self):
        x, y = self.position
        self.position = x, y+1
        if self.position[1] >= SCREEN_HEIGHT-2:
            self.reset()