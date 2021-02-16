from Components.Point import Point

class Ball(Point):
    def __init__(self, position):
        super().__init__(
            symbol='O', 
            position=position, 
            through=False
        )
        self.stick = False

    def move(self, velocity=None):
        # follows the bar
        if self.stick and velocity:
            x, y = self.position
            xv, yv= velocity
            self.position = (x+xv, y+yv)
        else:
            super().move()
