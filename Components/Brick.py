from config import (
    BRICK_1_BCOLOR,
    BRICK_1_FCOLOR,
    BRICK_2_BCOLOR,
    BRICK_2_FCOLOR,
    BRICK_3_BCOLOR,
    BRICK_3_FCOLOR,
    BRICK_4_BCOLOR,
    BRICK_4_FCOLOR
)
from Components.Surface import Surface

class Brick(Surface):
    def __init__(self, start, end, strength):
        bcolor = None
        fcolor = None
        
        if strength == 1:
            bcolor = BRICK_1_BCOLOR
            fcolor = BRICK_1_FCOLOR
        elif strength == 2:
            bcolor = BRICK_2_BCOLOR
            fcolor = BRICK_2_FCOLOR
        elif strength == 3:
            bcolor = BRICK_3_BCOLOR
            fcolor = BRICK_3_FCOLOR
        elif strength == 4:
            bcolor = BRICK_4_BCOLOR
            fcolor = BRICK_4_FCOLOR
        
        super().__init__(
            start,
            end,
            True,
            bcolor,
            fcolor
        )

# class Bricks():
#     def __init__(self):
        