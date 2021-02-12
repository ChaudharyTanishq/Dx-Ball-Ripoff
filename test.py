from config import (
    SCREEN, 
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    SCREEN_BCOLOR, 
    SCREEN_FCOLOR
)
from Components.Surface import Surface
from Components.Bar import Bar

from Input import Get, input_to
getch = Get()

import os
import time
import copy

surface = Surface(
    (0, 0),
    (SCREEN_WIDTH-1, SCREEN_HEIGHT-1),
    False,
    SCREEN_BCOLOR,
    SCREEN_FCOLOR
)

bar = Bar()

def print_screen(screen, c):
    surface.draw(screen)
    bar.draw(screen)
    if c == 'a':
        bar.move(True)
    elif c == 'd':
        bar.move(False)


    for row in screen:
        for char in row:
            print(char, end="")
        print()
    print(bar.start, bar.end)

def specialprint(x):
    while len(x) < 30:
        x += " "
    print(x, end='\r')

def main(verbose):
    """
    The main game loop!

    input params:
        verbose:
            shouts out loud what you are currently doing
    """
    while True:
        c = input_to(getch)

        os.system('clear')
        # time.sleep(1)
        print_screen(copy.deepcopy(SCREEN), c)
    
        if not c: continue
        
        if c == 'q': 
            if verbose:
                specialprint('quitting ...')
            break

        if c == 'a':
            if verbose:
                specialprint('left')
        if c == 'd':
            if verbose:
                specialprint('right')
        if c == ':':
            if verbose:
                specialprint('cheat mode on')
            
            while True:
                c = input_to(getch)
                if not c: continue

                specialprint(f'you have entered {c}')

                if c == 'q': 
                    specialprint('quitting cheat mode ...')
                    break
    print()
    return

main(True)