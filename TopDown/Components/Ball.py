from config import BAR_END, SCREEN_HEIGHT
from Components.Point import Point

class Ball(Point):
    def __init__(self, position):
        super().__init__(
            symbol='O', 
            position=position, 
            through=False
        )
        self.over = False

    def move(self):
        super().move()

        _, y = self.position
        if y >= SCREEN_HEIGHT-2:
            self.over = True
