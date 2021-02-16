from Components.Bricks import Bricks
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
        self.balls = [Ball()] # a list of ball objects
        self.bricks = Bricks() # the class that handles all the bricks
        self.c = None # the character that was inputted
        self.cheats = CHEATS
        self.cheat = None
        self.powerups = [] # stores all powerups on the screen
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
        elif c == 'i':
            for ball in self.balls:
                ball.velocity = (0, -1)
        elif c == 'j':
            for ball in self.balls:
                ball.velocity = (-1, 0)
        elif c == 'k':
            for ball in self.balls:
                ball.velocity = (0, 1)
        elif c == 'l':
            for ball in self.balls:
                ball.velocity = (1, 0)
        elif c == ':':
            self.cheat = input("Enter cheat code: ")
            if self.cheat in self.cheats:
                self.cheats[self.cheat] = True
                print("works!")
            else:
                print("YEET")
                exit()
                
    def handle_points(self):
        """
        handles ball logic for all the balls
        handles powerups for all the objects
        """
        for ball in self.balls:
            if self.cheats["THROUGH"]:
                ball.through = True
            ball.draw(reset=True)
            ball.move()
            ball.draw()
        for powerup in self.powerups:
            powerup.draw(True)
            powerup.move()
            powerup.draw()

    def handle_collisions(self):
        """
        handles all the collision cases.
        """
        for ball in self.balls:
            self.frame.handle_collision(ball)
            self.bar.handle_collision(ball)
            self.bricks.handle_collision(ball)
        
        self.powerups = self.bricks.powerups

        for powerup in self.powerups:
            self.bar.handle_powerup(powerup)

    def check_win(self):
        """
        checks for winning condition
        """
        if not len(self.bricks.bricks):
            print("YOU WIN!")
            return True
        
        hmm = True
        # if all bricks are of unbreakable type
        for brick in self.bricks.bricks:
            if brick.strength != 4:
                hmm = False
        return hmm

    def execute_powerups(self):
        powerups = [n for n,f in self.bar.powerups]

        for powerup in powerups:
            if powerup == 'G':
                self.bar.expand()
            elif powerup == 'S':
                self.bar.shrink()

    def render(self):
        """
        renders the components on the given screen
        """        

        # adding the components
        # draws the bar/paddle
        self.bar.draw(reset=False)

        self.bricks.draw()

        # handling all the collision logic
        self.handle_collisions()

        # handles all the drawing logic for the ball+powerups
        self.handle_points()

        # handles reducing of powerup time
        self.bar.handle_powerups()

        # execute powerups
        self.execute_powerups()

        # pausing for a bit
        time.sleep(0.07)

        if self.check_win():
            return True

        if self.cheats["BIG BALLS"]:
            self.balls.append(Ball())
            self.cheats["BIG BALLS"] = False

        if self.cheats["NO DIE"]:
            return False
        else:
            self.balls = [ball for ball in self.balls if not ball.over]        
            return False if len(self.balls) else True
