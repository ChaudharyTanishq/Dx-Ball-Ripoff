from config import SCREEN_HEIGHT
from colorama import Style, Back, Fore

class Point():
    def __init__(self, symbol, position, through, bcolor=Back.RESET, fcolor=Fore.RESET):
        self.symbol = symbol
        self.position = position
        self.velocity = (0, 1)
        self.through = through
        self.bcolor = bcolor
        self.fcolor = fcolor

    # prepares for printing
    def set(self):
        x, y = self.position
        print(f'\033[{y+1};{x+1}H', end='')

    # goes to the point just after the game screen
    def reset(self):
        print(f'\033[{SCREEN_HEIGHT+1};{1}H')

    # prints coloured string
    def color_string(self, reset=False):
        color = ' ' if reset else self.bcolor + self.fcolor + self.symbol
        return color + Style.RESET_ALL

    # draws the shit on the screen
    def draw(self, reset=False):
        self.set()
        print(self.color_string(reset))
        self.reset()

    # moves the point object
    def move(self):
        x, y = self.position
        xv, yv = self.velocity

        # limiting velocities
        if xv > 2:
            xv = 2
        if xv < -2:
            xv = -2
        if yv > 2:
            yv = 2
        if yv < -2:
            yv = -2
        
        self.velocity = (xv, yv)
        self.position = (x+xv, y+yv)
