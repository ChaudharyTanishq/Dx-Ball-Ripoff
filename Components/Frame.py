from Components.Surface import Surface
from config import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT,
    FRAME_BCOLOR,
    FRAME_FCOLOR
)

class Frame(Surface):
    def __init__(self):
        super().__init__(
            (0, 0),
            (SCREEN_WIDTH-1, SCREEN_HEIGHT-1),
            False,
            FRAME_BCOLOR,
            FRAME_FCOLOR
        )
        return
