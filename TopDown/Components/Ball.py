from config import BAR_END, BAR_SPEED, BAR_START, SCREEN_HEIGHT
from Components.Point import Point

class Ball(Point):
    def __init__(self, position, velocity=(0, 1)):
        super().__init__(
            symbol='O', 
            position=position, 
            through=False,
            velocity=velocity
        )
        self.sticky = False
        self.saved_velocity = None

    def fast(self):
        xv, yv = self.velocity
        if yv > 4:
            return
        self.velocity = xv, yv*2

    def move(self, bar=None, direction=None):
        if not bar:
            super().move()
        else:
            direction = -1 if direction else 1
            x, y = self.position
            self.position = x + direction*BAR_SPEED, y
