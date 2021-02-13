# a file that stores the hyperparameters

import random
from colorama import Fore, Back, Style

# SCREEN PARAMETERS
SCREEN_WIDTH = 32
SCREEN_HEIGHT = 16
SCREEN = []
for i in range(SCREEN_HEIGHT):
    SCREEN.append([' ' for _ in range(SCREEN_WIDTH)])
FRAME_BCOLOR = Back.BLACK
FRAME_FCOLOR = Fore.BLACK

# BAR PARAMETERS
bar_start_x = random.randint(10, SCREEN_WIDTH-10)
INIT_BAR_START = (bar_start_x, SCREEN_HEIGHT-3)
INIT_BAR_END = (bar_start_x+4, SCREEN_HEIGHT-3)
BAR_SPEED = 1
BAR_BCOLOR = Back.GREEN
BAR_FCOLOR = Fore.RESET

# BALL PARAMETERS
BALL_BCOLOR = Back.RESET
BALL_FCOLOR = Fore.MAGENTA
