from Components.Ball import Ball
from Components.Point import Point
from config import POWERUPS, POWERUP_FRAMES
import random

class Powerups():
    def __init__(self, bar, balls):
        self.bar = bar
        self.balls = balls
        self.powerups = []
        self.active_powerups = []

    # generates a random powerup at a given position
    def generate(self, position):
        symbol = random.choice(POWERUPS)
        self.powerups.append(Point(symbol, position, through=True))

    def move(self):
        for powerup in self.powerups:
            powerup.move()
        
        self.powerups = [powerup for powerup in self.powerups if not powerup.over]

    # activates a particular powerup
    # removes it from the old list
    def activate(self, powerup, velocity=None):
        s = powerup.symbol

        self.powerups = [powerup for powerup in self.powerups if powerup.symbol != s]
        self.active_powerups = [powerup for powerup in self.active_powerups if powerup.symbol != s]

        # adding it afresh
        if s == 'G' or s == 'S' or s == 'T' or s == 'F':
            self.active_powerups.append(powerup)
            
            # doing the required logic
            if s == 'G':
                self.bar.grow()
            elif s == 'S':
                self.bar.shrink()
            elif s == 'T':
                for ball in self.balls:
                    ball.through = True
            elif s == 'F':
                for ball in self.balls:
                    xv, yv = ball.velocity
                    ball.velocity = xv, yv*2
        elif s == 'K':
            for ball in self.balls:
                ball.stick = True
            self.active_powerups.append(powerup)
        elif s == 'B':
            new_balls = []
            for ball in self.balls:
                x, y = ball.position
                xv, yv = ball.velocity
                new_balls.append(
                    Ball(x-xv, y-yv)
                )
            self.balls.extend(new_balls)

    # the collision velocity of the ball
    def stick(self, velocity):
        sticky = [powerup for powerup in self.active_powerups if powerup.symbol == 'K']
        if len(sticky):
            return velocity
            
