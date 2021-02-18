class Powerups():
    def __init__(self):
        self.powerups = []

    def draw(self, reset=False):
        for powerup in self.powerups:
            powerup.draw(reset)
