from colorama import Fore, Back, Style

SCREEN_WIDTH = 32
SCREEN_HEIGHT = 28

SCREEN_BCOLOR = Back.BLACK
SCREEN_FCOLOR = Fore.BLACK

BAR_BCOLOR = Back.GREEN
BAR_FCOLOR = Fore.RESET
BAR_SIZE = 5
BAR_SPEED = 1
BAR_START = (SCREEN_WIDTH//2-2, SCREEN_HEIGHT-4)
BAR_END = (SCREEN_WIDTH//2+2, SCREEN_HEIGHT-4)

BRICK_SIZE = 4
BRICK_1_BCOLOR = Back.MAGENTA
BRICK_1_FCOLOR = Fore.RESET
BRICK_2_BCOLOR = Back.BLUE
BRICK_2_FCOLOR = Fore.RESET
BRICK_3_BCOLOR = Back.CYAN
BRICK_3_FCOLOR = Fore.RESET
BRICK_4_BCOLOR = Back.BLACK
BRICK_4_FCOLOR = Fore.RESET
BRICK_5_BCOLOR = Back.RED
BRICK_5_FCOLOR = Fore.RESET

POWERUPS = ['G', 'S', 'K', 'T', 'F', 'B']
POWERUP_PROBABILITY = 0.6
