import os

class Game():
    def __init__(self, screen, bar):
        """
        input params:
            frame:
                the frame object
            bar:
                the bar object
        """
        self.screen = screen
        self.bar = bar
        self.c = None
        # renders the screen only when needed
        self.re_render = True
        return

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
            # need to re render after bar move.
            self.re_render = True

    def render(self):
        """
        renders the components on the given screen
        """
        # quit if not needed.
        if not self.re_render:
            # print('yeet')
            return
        
        # adding the components
        os.system('clear')
        self.bar.draw(self.screen)

        # printing the components on the screen
        for row in self.screen:
            for char in row:
                print(char, end="")
            print()
        
        # done rendering. stopping till required again.
        self.re_render = False
