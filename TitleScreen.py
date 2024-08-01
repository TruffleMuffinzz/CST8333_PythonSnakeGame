import pygame
from text_utils import draw_text, title_font, context_font, DARK_GREY, DIM_GREY, WHITE, LIGHT_GREY, BLACK
from button import Button

pygame.init()

# set game window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# define fps
FPS = 60
TIMER = pygame.time.Clock()

MAIN_MENU = True
GAME_SCREEN = False
SCORE_SCREEN = False


def start_game():
    global MAIN_MENU, GAME_SCREEN
    MAIN_MENU = False
    GAME_SCREEN = True


def show_leaders():
    pass


# array of buttons
buttons = [
    Button("Start Game", 290, 290, 200, 40, context_font(40), DARK_GREY, DIM_GREY, WHITE, start_game),
    Button("Leaderboard", 290, 350, 200, 40, context_font(40), DARK_GREY, DIM_GREY, WHITE, show_leaders),
    Button("Quit", 290, 410, 200, 40, context_font(40), DARK_GREY, DIM_GREY, WHITE, quit)
]


def draw_game():
    pygame.draw.rect(SCREEN, LIGHT_GREY, (100, 100, 300, 300))
    draw_text("This is where the actual game will appear", context_font(45), WHITE, 100, 100, SCREEN)


def draw_menu():
    # set title and credit
    draw_text("SNAKE", title_font(100), WHITE, 250, 150, SCREEN)
    draw_text("by: Elaine DeJoseph", context_font(35), WHITE, 300, 220, SCREEN)

    for button in buttons:
        button.draw(SCREEN)


# loop telling to run
RUN = True

while RUN:
    SCREEN.fill(BLACK)
    TIMER.tick(FPS)

    # set functionality for the red X that shows with the system window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    if MAIN_MENU:
        draw_menu()
    elif GAME_SCREEN:
        draw_game()

    pygame.display.flip()
pygame.quit()
