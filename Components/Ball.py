from config import BAR_END, BAR_SPEED, BAR_START, SCREEN_HEIGHT, SCREEN_WIDTH
from Components.Point import Point

class Ball(Point):
    def __init__(self, position=None, velocity=(0, 1), game_init=False):
        if game_init:
            super().__init__(
                symbol='⬤',
                position=(SCREEN_WIDTH//2, SCREEN_HEIGHT-5),
                through=False,
                velocity=(0, 0)
            )            
            self.sticky = True
            self.saved_velocity = (0, -1)
        else:
            super().__init__(
                symbol='⬤', 
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
