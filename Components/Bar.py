from Components.Ball import Ball
from Components.Surface import Surface
from config import BAR_BCOLOR, BAR_FCOLOR, BAR_INIT_X, BAR_INIT_Y

class Bar(Surface):
    def __init__(self):
        super().__init__(
            start=BAR_INIT_X, 
            end=BAR_INIT_Y, 
            out=True, 
            bcolor=BAR_BCOLOR, 
            fcolor=BAR_FCOLOR
        )
    
    def handle_collided(self, point):
        direction = super().handle_collision(point)

        if not direction:
            return None
        
        # the logic for angled point movements
        if direction == 'y':
            x1, _ = self.start
            x2, _ = self.end
            x3, _ = point.position
            xv, yv = point.velocity
            centre = (x2+x1)//2
            xv = x3-centre
            if xv > 2: xv = 2
            if xv < -2: xv = -2

            # if non stick, save new velocity now
            if isinstance(point, Ball):
                if not point.stick:
                    point.velocity = (xv, yv)
                # return regardless
                return (xv, yv)
            else:
                return True
        
        return None
    