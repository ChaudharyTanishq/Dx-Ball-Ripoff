class Surface():
    def __init__(self, start, end, out):
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

    def draw(self, fill, color):
        """
        draws the box on screen

        input prams:
            fill:
                input text to the box
            color:
                color to make the box
        """
        pass

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
