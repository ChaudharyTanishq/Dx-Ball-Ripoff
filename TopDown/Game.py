from Components.Frame import Frame
from Components.Ball import Ball
from Components.Bar import Bar
from Components.Bricks import Bricks
from Components.Powerups import Powerups
from Components.Powerup import Powerup

from config import POWERUPS, POWERUP_PROBABILITY, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Game():
    def __init__(self):
        self.frame = Frame()
        self.bar = Bar()
        self.balls = [Ball((SCREEN_WIDTH//2, SCREEN_HEIGHT//2))]
        self.bricks = Bricks()
        self.powerups = Powerups()
        
        self.sticky_balls = []

        # variables needed for external use
        self.lives = 3
        self.score = 0
        self.quit = False

    # checks for winning condition
    def check_win(self):
        through = False
        for ball in self.balls:
            if ball.through:
                through = True
                break
        if through:
            self.quit = not len(self.bricks.bricks)

        flag = True
        for brick in self.bricks.bricks:
            if brick.strength != 4:
                flag = False
                break
        
        if flag:
            self.quit = True

    # handles all kinds of inputs
    def handle_input(self, c):
        if not c:
            return
        c = c.lower()
        if c == 'q':
            self.quit = True
        elif c == 'a':
            self.bar.draw(True)
            if self.bar.move(True):
                for ball in self.sticky_balls:
                    ball.draw(True)
                    ball.move(self.bar, True)
                    ball.draw()
        elif c == 'd':
            self.bar.draw(True)
            if self.bar.move(False):
                for ball in self.sticky_balls:
                    ball.draw(True)
                    ball.move(self.bar, False)
                    ball.draw()
        elif c == 'w':
            for ball in self.sticky_balls:
                # resetting for all the balls
                ball.sticky = False
                if ball.saved_velocity:
                    ball.velocity = ball.saved_velocity
                ball.saved_velocity = None
            self.sticky_balls = []

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
    def yeet_points(self):
        newballs = []
        for ball in self.balls:
            if ball.over:
                # shows graves of the balls
                # ball.draw(True)
                del ball
            else:
                newballs.append(ball)
        self.balls = newballs

        new_powerups = []
        for powerup in self.powerups.powerups:
            if powerup.over:
                powerup.draw(True)
                del powerup
            else:
                new_powerups.append(powerup)
        self.powerups.powerups = new_powerups

    def yeet_bricks(self):
        new_bricks = []
        for brick in self.bricks.bricks:
            if brick.yeet:
                brick.draw(True)
                self.score += 5
                
                symbol = random.choice(POWERUPS)
                x1, y1 = brick.start
                x2, y2 = brick.end

                if random.random() < POWERUP_PROBABILITY:
                    self.powerups.powerups.append(
                        Powerup(
                            symbol=symbol,
                            position=((x1+x2)//2, y1)
                        )
                    )
                
                del brick
            else:
                brick.draw()
                new_bricks.append(brick)
        self.bricks.bricks = new_bricks

    # handles all the moving objects
    def handle_movements(self):
        # moves the balls
        for ball in self.balls:
            if not ball.saved_velocity:
                ball.draw(True)
                ball.move()
        
        # moves the powerups
        for powerup in self.powerups.powerups:
            powerup.draw(True)
            powerup.move()

    def handle_cheats(self, c):
        if c == 'G':
            self.bar.grow()
        elif c == 'S':
            self.bar.shrink()
        elif c == 'T':
            for ball in self.balls:
                ball.through = True
        elif c == 'F':
            for ball in self.balls:
                ball.fast()
        elif c == 'B':
            new_balls = []
            for ball in self.balls:
                xv, yv = ball.velocity
                new_balls.append(
                    Ball(
                        ball.position, 
                        velocity=(-xv, -yv)
                    )
                )
            self.balls.extend(new_balls)
        elif c == 'K':
            for ball in self.balls:
                ball.sticky = True

    # handles all the collisions
    def handle_collisions(self):
        # ball related collisions
        for ball in self.balls:
            saved_velocity = self.bar.handle_collided(ball)
            # only saved when sticky, since otherwise its None
            if saved_velocity: 
                ball.saved_velocity = saved_velocity
                # print(ball.saved_velocity)
                self.sticky_balls.append(ball)

            self.frame.handle_collided(ball)
            self.bricks.handle_collided(ball)
        
        # moves the powerups
        for powerup in self.powerups.powerups:
            # yeets if out of bar bound
            self.frame.handle_collided(powerup, reflect=False)
            # checks if the powerup is absorbed
            is_absorbed = self.bar.handle_collided(powerup)
            if is_absorbed:
                powerup.over = True
                self.handle_cheats(powerup.symbol)

    def render(self):
        # checks if the game has been won or not
        self.check_win()

        # yeets balls & powerups which die
        self.yeet_points()
        # yeets bricks which die
        self.yeet_bricks()

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
        self.bricks.draw()
        self.powerups.draw()
