from Components.Frame import Frame
from Components.Bar import Bar
from Components.Ball import Ball
import os

class Game():
    def __init__(self, screen):
        """
        input params:
            screen:
                the screen to be used for drawing
        """
        self.frame = Frame() # frame object
        self.frame.draw(screen) # leaving the frame mark on the screen 
        self.screen = screen # screen
        
        self.bar = Bar() # bar object
        self.ball = Ball() # ball object
        self.c = None # the character that was inputted
        return
    
    def handle_ball(self):
        """
        handles ball logic
        """
        self.ball.draw(self.screen, reset=True)
        self.ball.move()
        self.ball.draw(self.screen)

    def handle_input(self, c):
        """
        handles arbitary inputs
        """
        if c == 'q':
            self.c = c
        elif c == 'a' or c == 'd':
            self.c = c
            self.bar.draw(self.screen, reset=True)
            self.bar.move(True if c == 'a' else False)
    
    def handle_collisions(self):
        """
        handles all the collision cases.
        """
        self.frame.handle_collision(self.ball)
        self.bar.handle_collision(self.ball)

    def render(self):
        """
        renders the components on the given screen
        """        

        # adding the components
        # draws the bar/paddle
        self.bar.draw(self.screen)
        # handles all the drawing logic for the ball
        self.handle_ball()

        # handling all the collision logic
        self.handle_collisions()

        # printing the components on the screen
        os.system('clear')
        for row in self.screen:
            for char in row:
                print(char, end="")
            print()
        
        # checking if the game is over or not
        if self.ball.over:
            return True
        else:
            return False
