from config import (
    BRICK_1_BCOLOR, 
    BRICK_1_FCOLOR,
    BRICK_2_BCOLOR,
    BRICK_2_FCOLOR,
    BRICK_3_BCOLOR,
    BRICK_3_FCOLOR,
    BRICK_4_BCOLOR,
    BRICK_4_FCOLOR,
    BRICK_5_BCOLOR,
    BRICK_5_FCOLOR,
)
from Components.Surface import Surface

def color_identifier(strength):
    if strength == 1:
        return BRICK_1_BCOLOR, BRICK_1_FCOLOR
    if strength == 2:
        return BRICK_2_BCOLOR, BRICK_2_FCOLOR
    if strength == 3:
        return BRICK_3_BCOLOR, BRICK_3_FCOLOR
    if strength == 4:
        return BRICK_4_BCOLOR, BRICK_4_FCOLOR
    if strength == 5:
        return BRICK_5_BCOLOR, BRICK_5_FCOLOR

class Brick(Surface):
    def __init__(self, start, end, strength):
        bcolor, fcolor = color_identifier(strength)
        super().__init__(
            start=start,
            end=end, 
            out=True, 
            bcolor=bcolor, 
            fcolor=fcolor
        )
        self.strength = strength
        self.yeet = False

    def destroy(self, through=False):
        # if through ball, remove everything in path
        if through or self.strength == 1:
            self.yeet = True
        elif 1 < self.strength < 4:
            self.strength -= 1
            self.bcolor, self.fcolor = color_identifier(self.strength)
            self.draw(True)
            self.draw()
        elif self.strength == 5:
            # print('boom')
            self.yeet = True
            return True

    def handle_collided(self, point):
        direction = super().handle_collided(point, (not point.through))

        if not direction:
            return None

        # handles all kinds of destructions
        return self.destroy(point.through)
