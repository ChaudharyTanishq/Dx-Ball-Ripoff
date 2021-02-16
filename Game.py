from Components.Bar import Bar
from Components.Frame import Frame
from config import BAR_INIT_X, BAR_INIT_Y
from Components.Ball import Ball


class Game():
    def __init__(self):
        self.balls = [Ball((BAR_INIT_X, BAR_INIT_Y))]
        self.frame = Frame()
        self.bar = Bar()
    
    def draw(self):
        self.bar.draw(False)
        