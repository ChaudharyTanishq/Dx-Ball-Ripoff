import time
from Components.Ball import Ball
from Components.Frame import Frame
from Components.Bar import Bar
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Game():
    def __init__(self):
        self.frame = Frame()
        self.bar = Bar()
        self.balls = [Ball((SCREEN_WIDTH//2, SCREEN_HEIGHT//2))]
        # variables needed for external use
        self.lives = 3
        self.score = 0
        self.quit = False

    # checks for winning condition
    def check_ok(self):
        if self.ball.over:
            self.ball = None

    # handles all kinds of inputs
    def handle_input(self, c):
        if not c:
            return
        c = c.lower()
        if c == 'q':
            self.quit = True
        elif c == 'a':
            self.bar.draw(True)
            self.bar.move(True)
        elif c == 'd':
            self.bar.draw(True)
            self.bar.move(False)

    # resets the game after all balls are lost
    def reset(self):
        # reducing lives
        self.lives -= 1
        if self.lives <= 0:
            self.quit = True
            return
        # a new hope
        else:
            x1, y1 = self.bar.start
            x2, _ = self.bar.end
            self.balls.append(Ball(((x1+x2)//2, y1-2)))
    
    # yeets balls which die
    def yeet_balls(self):
        newballs = []
        for ball in self.balls:
            if ball.over:
                # ball.draw(True)
                del ball
            else:
                newballs.append(ball)
        self.balls = newballs

    # handles all the moving objects
    def handle_movements(self):
        # moves the balls
        for ball in self.balls:
            ball.draw(True)
            ball.move()

    # handles all the collisions
    def handle_collisions(self):
        # ball related collisions
        for ball in self.balls:
            self.bar.handle_collided(ball)
            self.frame.handle_collided(ball)

    def render(self):
        # yeets balls which die
        self.yeet_balls()

        # CHECKING NEW BALL/GAME OVER CONDITION
        if not len(self.balls):
            self.reset()
        
        # MOVING OBJECTS
        self.handle_movements()
        
        # COLLIDING THE OBJECTS
        self.handle_collisions()

        # DRAW THE SHAPES
        # self.frame.draw()
        self.bar.draw()
        for ball in self.balls:
            ball.draw()
