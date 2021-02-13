from config import SCREEN_HEIGHT
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
        color = ' ' if reset else self.bcolor + self.fcolor + ' '
        return color + Style.RESET_ALL
    
    def draw(self, screen, reset=False):
        """
        draws the box on screen

        input prams:
            screen:
                the screen to add the surface on
            reset:
                instead of colouring, just removes the object
        """
        x1, y1 = self.start
        x2, y2 = self.end

        screen[y1][x1] = self.color_string(reset)
        screen[y1][x2] = self.color_string(reset)
        screen[y2][x1] = self.color_string(reset)
        screen[y2][x2] = self.color_string(reset)
        
        for i in range(x1+1, x2):
            screen[y1][i] = self.color_string(reset)
            screen[y2][i] = self.color_string(reset)
        for j in range(y1+1, y2):
            screen[j][x1] = self.color_string(reset)
            screen[j][x2] = self.color_string(reset)

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
        if not self.out:
            if x1+1 == x3 or x2-1 == x3:
                return 'x'
            if y1+1 == y3 or y2-1 == y3:
                return 'y'
        else:
            if x1 <= x3 <= x2 and (y3+1 == y1 or y2 == y3):
                return 'y'
            if y1 == y3 and (x1 == x3+1 or x2 == x3):
                return 'x'

        return None
        

    def handle_collision(self, ball):
        """
        handles any collisions

        input prams:
            ball:
                the ball object
        """
        # extracting ball's velocity
        # collisions happen with positions only.
        x_v, y_v = ball.velocity 
        
        direction = self.check_collision(ball)
        if direction and direction == 'x':
            x_v *= -1
        elif direction and direction == 'y':
            y_v *= -1

        # saving ball's new velocity
        ball.velocity = x_v, y_v
