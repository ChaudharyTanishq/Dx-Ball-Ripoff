from config import SCREEN_BCOLOR, SCREEN_FCOLOR, SCREEN_HEIGHT, SCREEN_WIDTH
from Components.Surface import Surface

class Frame(Surface):
    def __init__(self):
        super().__init__(
            start=(0, 0), 
            end=(SCREEN_WIDTH-1, SCREEN_HEIGHT-1),
            out=False, 
            bcolor=SCREEN_BCOLOR, 
            fcolor=SCREEN_FCOLOR
        )
    