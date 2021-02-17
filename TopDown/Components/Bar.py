from Components.Powerup import Powerup
from config import BAR_BCOLOR, BAR_END, BAR_FCOLOR, BAR_SPEED, BAR_START, SCREEN_WIDTH
from Components.Surface import Surface


class Bar(Surface):
    def __init__(self):
        super().__init__(
            start=BAR_START, 
            end=BAR_END, 
            out=True, 
            bcolor=BAR_BCOLOR, 
            fcolor=BAR_FCOLOR
        )

    def grow(self):
        x1, y1 = self.start
        x2, y2 = self.end

        if x2-x1+1 > 7:
            return

        self.start = x1-1, y1
        self.end = x2+1, y2
    
    def shrink(self):
        x1, y1 = self.start
        x2, y2 = self.end
        
        if x2-x1+1 < 3:
            return
        
        self.draw(True)
        self.start = x1+1, y1
        self.end = x2-1, y2
        self.draw()
    
    def move(self, left):
        x1, y1 = self.start
        x2, y2 = self.end

        # mathematical convenience
        left = -1 if left else 1
        
        # updating x positions
        t1 = x1 + left*BAR_SPEED
        t2 = x2 + left*BAR_SPEED

        # checking validity of x positions
        if t1 <0 or t2 > SCREEN_WIDTH:
            return False
        # while x1 < 0:
        #     x1 += 1
        #     x2 += 1
        # while x2 > SCREEN_WIDTH-1:
        #     x1 -= 1
        #     x2 -= 1

        # saving the values
        self.start = (t1, y1)
        self.end = (t2, y2)
        return True

    # reflects the point (mostly written with ball in mind)
    def handle_collided(self, point):
        direction = self.is_collided(point)

        # if no collision at all
        if not direction:
            return None
        
        # if powerup
        if isinstance(point, Powerup):
            return True

        # only ball object reaches here
        unsaved_velocity = None

        # the logic for angled point returns
        if direction == 'y':
            x1, _ = self.start
            x2, _ = self.end
            x3, _ = point.position
            xv, yv = point.velocity
            centre = (x2+x1)//2
            xv = x3-centre
            if xv > 2: xv = 2
            if xv < -2: xv = -2
            if not point.sticky:
                point.velocity = (xv, yv)
            else:
                unsaved_velocity = (xv, yv)
        
        # reflect the point if not sticky
        if not point.sticky: 
            self.reflect(point, direction)
        else:
            try:
                xv, yv = unsaved_velocity 
                if direction == 'x':
                    xv *= -1
                elif direction == 'y':
                    yv *= -1
                unsaved_velocity = (xv, yv)
            except:
                return None
        # if already saved from before, dont save again
        if point.saved_velocity:
            return None
        else:
            return unsaved_velocity
