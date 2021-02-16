from Components.Surface import Surface

from config import (
    INIT_BAR_START, 
    INIT_BAR_END,
    BAR_SPEED,
    BAR_BCOLOR,
    BAR_FCOLOR,
    SCREEN_WIDTH
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
            out=True,
            bcolor=BAR_BCOLOR,
            fcolor=BAR_FCOLOR,
        )

        # stores a list of powerup tuples,
        # (NAME, frames_left) 
        # where NAME is the unique key deciding behaviour
        self.powerups = []

    def draw(self, reset):
        """
        draws the box on screen

        input prams:
            reset:
                instead of colouring, it decolours
        """
        x1, y1 = self.start
        x2, y2 = self.end
        assert y1 == y2
        print(f'\033[{y1+1};{x1+1}H', end='')
        for _ in range(x1, x2+1):
            print(self.color_string(reset), end='')
        self.reset()

    def expand(self):
        x1, y1 = self.start
        x2, y2 = self.end
        x1 -= 1
        x2 += 1
        self.start = x1, y1
        self.end = x2, y2
    
    def shrink(self):
        x1, y1 = self.start
        x2, y2 = self.end
        if x2-x1+1 > 1:
            x1 += 1
            x2 -= 1
        self.start = x1, y1
        self.end = x2, y2
    
    def handle_powerup(self, name):
        # removing name if already present
        self.powerups = [(n, f) for n, f in self.powerups if n!=name]
        # adding new powerup
        self.powerups.append((name, 60))

    def handle_powerups(self):
        new_powerups = []
        for powerup, frames_left in self.powerups:
            if frames_left > 1:
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

        # checking validity of x positions
        while x1 < 2:
            x1 += 1
            x2 += 1
        while x2 > SCREEN_WIDTH-2:
            x1 -= 1
            x2 -= 1

        # saving the values
        self.start = (x1, y1)
        self.end = (x2, y2)
        return      

    def handle_collision(self, ball):
        """
        handles the collisions

        input prams:
            ball:
                the ball object
        """
        direction = super().handle_collision(ball)

        if not direction:
            return None
        
        # the logic for angled ball movements
        if direction == 'y':
            x1, _ = self.start
            x2, _ = self.end
            x3, _ = ball.position
            x_v, y_v = ball.velocity
            centre = (x2+x1)//2
            x_v = x3-centre
            if x_v > 2: x_v = 2
            if x_v < -2: x_v = -2
            ball.velocity = (x_v, y_v)
        
        return direction
    

        
        