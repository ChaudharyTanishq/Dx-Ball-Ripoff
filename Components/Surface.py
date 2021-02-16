from colorama import Style, Back, Fore
from config import SCREEN_HEIGHT

class Surface():
    def __init__(self, start, end, out, bcolor=Back.RESET, fcolor=Fore.RESET):
        self.start = start
        self.end = end
        self.out = out
        self.bcolor = bcolor
        self.fcolor = fcolor

    # prepares for printing
    def set(self):
        x, y = self.start
        print(f'\033[{y+1};{x+1}H', end='')

    # goes to the point just after the game screen
    def reset(self):
        print(f'\033[{SCREEN_HEIGHT+1};{1}H')

    # prints coloured string
    def color_string(self, reset=False):
        color = ' ' if reset else self.bcolor + self.fcolor + ' '
        return color + Style.RESET_ALL

    # draws the shit on the screen
    def draw(self, reset=False):
        x1, y1 = self.start
        x2, y2 = self.end

        self.set()
        for _ in range(y1, y2+1):
            for __ in range(x1, x2+1):
                print(self.color_string(reset), end='')
            print()
        self.reset()

    # returns the direction to be reflected
    # if nothing, returns ''
    def is_collided(self, point):
        x1, y1 = self.start
        x2, y2 = self.end
        x3, y3 = point.position
        xv, yv = point.velocity
        nx3 = x3 + xv
        ny3 = y3 + yv
        
        # for frame, inside collisions
        if not self.out:
            if (xv<0 and x1 >= nx3) or (x2 <= nx3 and xv>0):
                return 'x'
            if (yv<0 and y1 >= ny3) or (y2 <= ny3 and yv>0):
                return 'y'
        # for bar and bricks, outside collisions
        else:
            # up-side
            if yv and ny3 == y1 and x1<=nx3<=x2:
                return 'y'
            # down-side
            elif yv and ny3 == y2 and x1<=nx3<=x2:
                return 'y'
            # right side
            elif xv and nx3 == x2+1 and y1<=ny3<=y2:
                return 'x'
            # left side
            elif xv and nx3 == x1-1 and y1<=ny3<=y2:
                return 'x'
            
        return ''

    # reflects the point (mostly written with ball in mind)
    def handle_collided(self, point):
        direction = self.is_collided(point)

        if not direction:
            return

        # reflection logic        
        xv, yv = point.velocity 
        if direction == 'x':
            xv *= -1
        elif direction == 'y':
            yv *= -1
        point.velocity = xv, yv
        # end of reflection logic

        return
