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
        x1 = x1 + left*BAR_SPEED
        x2 = x2 + left*BAR_SPEED

        # checking validity of x positions
        while x1 < 0:
            x1 += 1
            x2 += 1
        while x2 > SCREEN_WIDTH-1:
            x1 -= 1
            x2 -= 1

        # saving the values
        self.start = (x1, y1)
        self.end = (x2, y2)

    # reflects the point (mostly written with ball in mind)
    def handle_collided(self, point):
        direction = self.is_collided(point)

        if not direction:
            return None
        
        # reflect the point always
        self.reflect(point, direction)

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
            point.velocity = (xv, yv)
