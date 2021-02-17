from config import BRICK_SIZE
from Components.Brick import Brick

class Bricks():
    def __init__(self):
        self.bricks = []
        for i in range(5):
            for j in range(5):
                self.bricks.append(
                    Brick(
                        start=(4+BRICK_SIZE*j, i+3),
                        end=(4+BRICK_SIZE-1+BRICK_SIZE*j, i+3),
                        strength=5-i
                    )
                )
    
    # draws regardless of whether a brick is yeeted or not
    def draw(self):
        for brick in self.bricks:
            brick.draw()

    # returns bricks who are neighbours
    def find_neighbours(self, brick):
        neighbours = []
        return neighbours

    def boom(self, brick):
        neighbours = self.find_neighbours(brick)
        for brick in neighbours:
            brick.destroy()

    def handle_collided(self, point):
        for brick in self.bricks:
            if brick.handle_collided(point):
                self.boom(brick)
            # brick.handle_collided(point)
