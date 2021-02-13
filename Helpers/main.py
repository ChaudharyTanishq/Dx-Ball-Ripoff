from Components.Frame import Frame
from Components.Bar import Bar
from Components.Ball import Ball
from cheat import CHEATS

import os
import time

class Game():
    def __init__(self, frame):
        """
        input params:
            screen:
                the screen to be used for drawing
        """
        self.frame = frame
        self.bar = Bar() # bar object
        self.ball = Ball() # ball object
        self.c = None # the character that was inputted
        self.cheats = CHEATS
        self.cheat = None
        return        

    def handle_input(self, c):
        """
        handles arbitary inputs
        """
        if c == 'q':
            self.c = c
        elif c == 'a' or c == 'd':
            self.c = c
            self.bar.draw(reset=True)
            self.bar.move(True if c == 'a' else False)
        elif c == ':':
            self.cheat = input("Enter cheat code: ")
            if self.cheat in self.cheats:
                self.cheats[self.cheat] = True
                print("works!")
            else:
                print("YEET")
                exit()
                
    def handle_ball(self):
        """
        handles ball logic
        """
        self.ball.draw(reset=True)
        self.ball.move()
        self.ball.draw()
    
    def handle_collisions(self):
        """
        handles all the collision cases.
        """
        self.frame.handle_collision(self.ball)
        self.bar.handle_collision(self.ball)

    def render(self):
        """
        renders the components on the given screen
        """        

        # adding the components
        # draws the bar/paddle
        self.bar.draw(reset=False)

        # handles all the drawing logic for the ball
        self.handle_ball()

        # handling all the collision logic
        self.handle_collisions()

        # pausing for a bit
        time.sleep(0.1)
        
        if self.cheats.get(self.cheat, False):
            return False
        return True if self.ball.over else False
