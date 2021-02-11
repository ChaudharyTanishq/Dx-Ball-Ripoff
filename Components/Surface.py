from colorama import Fore, Back, Style

class Surface():
    def __init__(self, start, end, out, bcolor=None, fcolor=None):
        """
        initialising a basic surface class

        input prams:
            start:
                start point of the box
            end:
                end point of the box
            out:
                False if the box is inward facing
                True if its outward facing
        """
        self.start = start
        self.end = end
        self.out = out
        if not bcolor: 
            self.bcolor = Back.RESET
        else:
            self.bcolor = bcolor

        if not fcolor: 
            self.fcolor = Fore.RESET
        else:
            self.fcolor = fcolor

    def draw(self, screen, fill=None):
        """
        draws the box on screen

        input prams:
            screen:
                the screen to add the surface on
            fill:
                input text to the box
        """
        x1, y1 = self.start
        x2, y2 = self.end

        def color_string():
            return self.bcolor + self.fcolor + ' ' + Style.RESET_ALL
        
        screen[y1][x1] = color_string()
        screen[y1][x2] = color_string()
        screen[y2][x1] = color_string()
        screen[y2][x2] = color_string()
        
        for i in range(x1+1, x2):
            screen[y1][i] = color_string()
            screen[y2][i] = color_string()
        for j in range(y1+1, y2):
            screen[j][x1] = color_string()
            screen[j][x2] = color_string()

    def check_collision(self, x3, y3):
        """
        checks if a collision has occured with the box or not

        input prams:
            (x3, y3): 
                the location of the point object which has to be
                checked for collision. 
                This restricts to be of size 1x1.
        
        return:
            bool, False if no collision, True if collision

        """
        pass


    def handle_collision(self, x3, y3, bar, through):
        """
        handles any collisions

        input prams:
            (x3, y3): 
                the location of the point object which has to be
                collided with.
            bar:
                if the object is the bar
            through:
                if the object has to go through the surface
        """
        pass
