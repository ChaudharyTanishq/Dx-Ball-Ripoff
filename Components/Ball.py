from config import BALL_BCOLOR, BALL_FCOLOR, SCREEN_HEIGHT, SCREEN_WIDTH
from colorama import Style

class Ball():
    def __init__(self):
        self.position = (SCREEN_WIDTH//2, SCREEN_HEIGHT-15)
        # down is positive
        self.velocity = (0, 1)
        self.bcolor = BALL_BCOLOR
        self.fcolor = BALL_FCOLOR
        self.over = False
    
    def reset(self):
        """
        resets the mouse pointer to 1, 1
        """
        print(f'\033[{SCREEN_HEIGHT};{0}H', end='')
        print()
    
    def color_string(self, reset):
        color = ' ' if reset else self.bcolor + self.fcolor + 'O'
        return color + Style.RESET_ALL

    def draw(self, reset=False):
        x, y = self.position
        print(f'\033[{y+1};{x+1}H', end='')
        print(self.color_string(reset))
        self.reset()

    def move(self):
        x, y = self.position
        x_v, y_v = self.velocity
        self.position = (x+x_v, y+y_v)

        if self.position[1] >= SCREEN_HEIGHT-2:
            self.over = True
