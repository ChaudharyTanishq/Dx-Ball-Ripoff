from config import FRAME_BCOLOR, FRAME_FCOLOR, SCREEN_HEIGHT, SCREEN_WIDTH
from Components.Surface import Surface

class Frame(Surface):
    def __init__(self):
        super().__init__(
            (0, 0), 
            (SCREEN_HEIGHT-1, SCREEN_WIDTH-1), 
            out=False,
            bcolor=FRAME_BCOLOR, 
            fcolor=FRAME_FCOLOR
        )

    # we do not want to draw the fame.
    # im too lazy to figure the logic
    def draw(self, reset):
        pass
