# a file that stores the hyperparameters

import random
from colorama import Fore, Back, Style

# SCREEN PARAMETERS
SCREEN_WIDTH = 42
SCREEN_HEIGHT = 24
SCREEN = []
for i in range(SCREEN_HEIGHT):
    SCREEN.append([' ' for _ in range(SCREEN_WIDTH)])
FRAME_BCOLOR = Back.BLACK
FRAME_FCOLOR = Fore.BLACK

# BAR PARAMETERS
bar_start_x = random.randint(10, SCREEN_WIDTH-10)
INIT_BAR_START = (bar_start_x, -3)
INIT_BAR_END = (bar_start_x+4, -3)
BAR_SPEED = 1
BAR_BCOLOR = Back.WHITE
BAR_FCOLOR = Fore.RESET
