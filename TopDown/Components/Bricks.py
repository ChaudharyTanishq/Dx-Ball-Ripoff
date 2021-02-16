from config import BRICK_SIZE
from Components.Brick import Brick

class Bricks():
    def __init__(self):
        self.bricks = []
        for i in range(1):
            for j in range(1):
                self.bricks.append(
                    Brick(
                        start=(4+BRICK_SIZE*j, i+3),
                        end=(4+BRICK_SIZE-1+BRICK_SIZE*j, i+3),
                        strength=3-i
                    )
                )
        self.score = 0
    
    def draw(self):
        new_bricks = []
        for brick in self.bricks:
            if brick.yeet:
                brick.draw(True)
                del brick
                self.score += 5
            else:
                brick.draw()
                new_bricks.append(brick)
        self.bricks = new_bricks

    def handle_collided(self, point):
        for brick in self.bricks:
            brick.handle_collided(point)
