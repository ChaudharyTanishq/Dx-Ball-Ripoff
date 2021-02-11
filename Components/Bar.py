from Surface import Surface
from config import (
    INIT_BAR_START, 
    INIT_BAR_END,
    BAR_SPEED
)

class Bar(Surface):
    def __init__(self):
        """
        initialises the bar object according to the config's
        hyperparameters
        """
        # initialising the super class parmeters
        super().__init__(
            start=INIT_BAR_START,
            end=INIT_BAR_END,
            out=True
        )

        # stores a list of powerup tuples,
        # (NAME, frames_left) 
        # where NAME is the unique key deciding behaviour
        self.powerups = []
    
    def handle_powerup(name):
        """
        handles powerup addition to the bar.

        input parameters:
            name:
                the unique key from which a powerup can be identified

        NOTE: powerups have one letter size, to account for 
        check_collision(), and make it behave like its a ball :P

        NOTE 2: we actually don't care about handling this type 
        of collision, since the powerup is 'absorbed' by the bar.
        """
        pass

    def handle_powerups(self):
        """
        decreases the frames left for each of the current powerups     
        """
        new_powerups = []
        for powerup, frames_left in self.powerups:
            new_powerups.append((powerup, frames_left-1))
        
        self.powerups = new_powerups
        return

    def move(self, left):
        """
        input params:
            left:
                True if the direction to be moved is left
                False if the direction is right instead.
        """
        x1, y1 = self.start
        x2, y2 = self.end

        # mathematical convenience
        left = -1 if left else 1
        
        # updating x positions
        x1 = x1 + left*BAR_SPEED
        x2 = x2 + left*BAR_SPEED

        # saving the values
        self.start = (x1, y1)
        self.end = (x2, y2)
        return
