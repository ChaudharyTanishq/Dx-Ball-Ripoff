from Components.Powerups import Powerups
from config import BRICK_SIZE
from Components.Brick import Brick
import random

class Bricks():
    def __init__(self):
        self.bricks = []
        for i in range(3):
            self.bricks.append(
                Brick(
                    (6+(BRICK_SIZE)*i, 5),
                    (6+BRICK_SIZE-1+(BRICK_SIZE)*i, 5),
                    i+1
                )
            )
        self.powerups = []

    def draw(self):
        for brick in self.bricks:
            brick.draw(False)

    def handle_collision(self, ball):
        new_bricks = []
        for brick in self.bricks:
            # if nothing happens, put the brick there
            
            direction = brick.handle_collision(ball)
            if not direction:
                new_bricks.append(brick)
            else:
                if brick.strength == 1 or direction == 'through':
                    brick.draw(True)
                    self.powerups.append(
                        Powerups(
                            (brick.start[0]+brick.end[0])//2,
                            brick.start[1]
                        )
                    )
                    del brick
                elif 4>brick.strength>1:
                    new_bricks.append(
                        Brick(
                            brick.start,
                            brick.end,
                            brick.strength-1
                        )
                    )
                    del brick
                elif brick.strength == '4':
                    new_bricks.append(brick)

        self.bricks = new_bricks
            
            