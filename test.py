from config import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BCOLOR, SCREEN_FCOLOR
from Components.Surface import Surface
from Components.Bar import Bar

surface = Surface(
    (0, 0),
    (SCREEN_WIDTH-1, SCREEN_HEIGHT-1),
    False,
    SCREEN_BCOLOR,
    SCREEN_FCOLOR
)

bar = Bar()

def print_screen(screen):
    surface.draw(screen)
    bar.draw(screen)
    
    for row in screen:
        for char in row:
            print(char, end="")
        print()

print_screen(SCREEN)
