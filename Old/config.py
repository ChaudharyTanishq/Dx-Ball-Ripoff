# a file that stores the hyperparameters

import random
from colorama import Fore, Back, Style

# SCREEN PARAMETERS
SCREEN_WIDTH = 32
SCREEN_HEIGHT = 20
SCREEN = []
for i in range(SCREEN_HEIGHT):
    SCREEN.append([' ' for _ in range(SCREEN_WIDTH)])
FRAME_BCOLOR = Back.BLACK
FRAME_FCOLOR = Fore.BLACK

# BAR PARAMETERS
bar_start_x = random.randint(10, SCREEN_WIDTH-10)
INIT_BAR_START = (bar_start_x, SCREEN_HEIGHT-3)
INIT_BAR_END = (bar_start_x+4, SCREEN_HEIGHT-3)
BAR_SPEED = 2
BAR_BCOLOR = Back.GREEN
BAR_FCOLOR = Fore.RESET

# BALL PARAMETERS
BALL_BCOLOR = Back.RESET
BALL_FCOLOR = Fore.MAGENTA
BALL_X = SCREEN_WIDTH//2
BALL_Y = SCREEN_HEIGHT-10

# BRICK PARAMETERS
BRICK_1_BCOLOR = Back.CYAN
BRICK_1_FCOLOR = Fore.RESET
BRICK_2_BCOLOR = Back.BLUE
BRICK_2_FCOLOR = Fore.RESET
BRICK_3_BCOLOR = Back.YELLOW
BRICK_3_FCOLOR = Fore.RESET
BRICK_4_BCOLOR = Back.WHITE
BRICK_4_FCOLOR = Fore.RESET
BRICK_5_BCOLOR = Back.RED
BRICK_5_FCOLOR = Fore.RESET

BRICK_SIZE = 5
BRICK_REDUCE_SCORE = 5
BRICK_REMOVE_SCORE = 10

# POWERUPS
POWERUPS = ['G', 'S']
POWERUPS_BCOLOR = Back.RESET
POWERUPS_FCOLOR = Fore.LIGHTBLACK_EX