from Components.Point import Point

class Powerup(Point):
    def __init__(self, symbol, position):
        super().__init__(
            symbol=symbol, 
            position=position,
            through=True, 
        )
