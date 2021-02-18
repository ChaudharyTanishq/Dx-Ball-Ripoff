import random
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
                        strength=random.randint(4, 5)
                    )
                )
        for i in range(3):
            for j in range(5):
                self.bricks.append(
                    Brick(
                        start=(4+BRICK_SIZE*j, i+8),
                        end=(4+BRICK_SIZE-1+BRICK_SIZE*j, i+8),
                        strength=3-i
                    )
                )
    
    # draws regardless of whether a brick is yeeted or not
    def draw(self):
        for brick in self.bricks:
            brick.draw()

    # returns true/false if points intersect or not
    def intersect(self, start1, end1, start2, end2):
        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        if x1<=x4<=x2 and (y1<=y4<=y2 or y1<=y3<=y4):
            return True
        if x1<=x3<=x2 and (y1<=y4<=y2 or y1<=y3<=y4):
            return True
        return False

    # returns bricks who are neighbours
    def find_neighbours(self, cur_brick):
        neighbours = []
        x1, y1 = cur_brick.start
        x2, y2 = cur_brick.end
        # radius = BRICK_SIZE
        radius = 1
        for brick in self.bricks:
            if self.intersect(
                (x1-radius, y1-radius), (x2+radius, y2+radius), brick.start, brick.end
            ):
                neighbours.append(brick)
        
        return neighbours

    def boom(self, brick):
        neighbours = self.find_neighbours(brick)
        for brick in neighbours:
            if not brick.yeet:
                if brick.destroy():
                    self.boom(brick)


    def handle_collided(self, point):
        for brick in self.bricks:
            if brick.handle_collided(point):
                self.boom(brick)
            # brick.handle_collided(point)
