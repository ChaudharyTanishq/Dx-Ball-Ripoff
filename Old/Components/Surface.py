from config import SCREEN_HEIGHT, SCREEN_WIDTH
from colorama import Fore, Back, Style

class Surface():
    def __init__(self, start, end, out, bcolor=None, fcolor=None):
        """
        initialising a basic surface class

        input prams:
            start:
                start point of the box
            end:
                end point of the box
            out:
                False if the box is inward facing
                True if its outward facing
        """
        self.start = start
        self.end = end
        self.out = out
        if not bcolor: 
            self.bcolor = Back.RESET
        else:
            self.bcolor = bcolor

        if not fcolor: 
            self.fcolor = Fore.RESET
        else:
            self.fcolor = fcolor


    def color_string(self, reset):
        color = None 
        if reset:
            color = ' '
        else:
            color = self.bcolor + self.fcolor + ' '
        return color + Style.RESET_ALL
    
    def draw(self, screen):
        """
        drawing the frame on the screen.

        this is the default case of burning on the screen.
        """
        x1, y1 = self.start
        x2, y2 = self.end
        
        for i in range(x1, x2+1):
            screen[y1][i] = self.color_string(False)
            screen[y2][i] = self.color_string(False)
        for j in range(y1, y2+1):
            screen[j][x1] = self.color_string(False)
            screen[j][x1+1] = self.color_string(False)
            screen[j][x2] = self.color_string(False)
            screen[j][x2-1] = self.color_string(False)

    def reset(self):
        """
        resets the mouse pointer to 1, 1
        """
        print(f'\033[{SCREEN_HEIGHT};{0}H', end='')
        print()

    def check_collision(self, ball):
        """
        checks if a collision has occured with the box or not

        input prams:
            ball:
                the ball object
        
        return:
            'x', if along 'x' axis,
            'y', if along 'y' axis,
            None if no collision. 
        """
        x1, y1 = self.start
        x2, y2 = self.end
        x3, y3 = ball.position
        x_v, y_v = ball.velocity
        nx3 = x3 + x_v
        ny3 = y3 + y_v
        
        if not self.out:
            if (x_v<0 and x1+1 >= nx3) or (x2-1 <= nx3 and x_v>0):
                return 'x'
            if (y_v<0 and y1 >= ny3) or (y2 <= ny3 and y_v>0):
                return 'y'
        else:
            # print(x3, nx3, x1, x2)
            assert y1 == y2
            # up-side
            if y_v and ny3 == y1 and x1<=nx3<=x2:
                return 'y'
            # down-side
            elif y_v and ny3 == y2 and x1<=nx3<=x2:
                return 'y'
            # the only cases for out-ward facing surfaces is y1 == y2
            elif x_v and nx3 == x2+1 and ny3 == y1:
                return 'x'
            elif x_v and nx3 == x1-1 and ny3 == y1:
                return 'x'
            
        return None
        

    def handle_collision(self, ball):
        """
        handles any collisions

        input prams:
            ball:
                the ball object
        """
        direction = self.check_collision(ball)
        # early return if no collision
        if not direction:
            return None
        # extracting ball's velocity
        # collisions happen with positions only.
        x_v, y_v = ball.velocity 
        
        if direction == 'x':
            x_v *= -1
        elif direction == 'y':
            y_v *= -1

        # saving ball's new velocity
        ball.velocity = x_v, y_v
        return direction