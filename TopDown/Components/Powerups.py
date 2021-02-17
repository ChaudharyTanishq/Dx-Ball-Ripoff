class Powerups():
    def __init__(self):
        self.powerups = []

    def draw(self):
        for powerup in self.powerups:
            powerup.draw()
