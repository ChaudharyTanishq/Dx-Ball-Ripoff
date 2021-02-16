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
        self.strength = strength
        # self.yeet = False

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
        for _ in range(x2-x1+1):
            print(self.color_string(reset), end='')
        self.reset()

    def handle_collision(self, ball):
        # gets the direction after collision checking
        direction = super().handle_collision(ball)

        if not direction:
            return None

        if ball.through:
            # inverting collisions, since ball has to 
            # 'cut-through'
            x_v, y_v = ball.velocity 
            
            if direction == 'x':
                x_v *= -1
            elif direction == 'y':
                y_v *= -1

            # saving ball's new velocity
            ball.velocity = x_v, y_v
            return 'through'
        
        return direction
