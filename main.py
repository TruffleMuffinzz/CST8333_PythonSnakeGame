import pygame
import json

from utils import draw_text, title_font, context_font, DARK_GREY, DIM_GREY, WHITE, LIGHT_GREY, BLACK
from button import Button
from snakeGame import Game

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
LEADERBOARD_SCREEN = False

LEADERBOARD_FILE = 'Assets/leaderboard.json'


def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as file:
            print("opening leaderboard file")
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [
            {"player": "AAA", "score": 100},
            {"player": "BBB", "score": 50},
            {"player": "CCC", "score": 25}
        ]


def start_game():
    global MAIN_MENU, GAME_SCREEN
    MAIN_MENU = False
    GAME_SCREEN = True

    game = Game()
    game.run()


def show_leaders():
    global MAIN_MENU, LEADERBOARD_SCREEN
    MAIN_MENU = False
    LEADERBOARD_SCREEN = True


def back_to_menu():
    global MAIN_MENU, LEADERBOARD_SCREEN
    LEADERBOARD_SCREEN = False
    MAIN_MENU = True


# array of buttons
buttons = [
    Button("Start Game", 290, 290, 200, 40, context_font(40), DARK_GREY, DIM_GREY, WHITE, start_game),
    Button("Leaderboard", 290, 350, 200, 40, context_font(40), DARK_GREY, DIM_GREY, WHITE, show_leaders),
    Button("Quit", 290, 410, 200, 40, context_font(40), DARK_GREY, DIM_GREY, WHITE, quit)
]

leaderboard_buttons = [
    Button("Back", 350, 550, 100, 40, context_font(40), DARK_GREY, DIM_GREY, WHITE, back_to_menu)
]


def draw_menu():
    # set title and credit
    draw_text("SNAKE", title_font(100), WHITE, 250, 150, SCREEN)
    draw_text("by: Elaine DeJoseph", context_font(35), WHITE, 300, 220, SCREEN)

    for button in buttons:
        button.draw(SCREEN)


def draw_leaderboard():
    SCREEN.fill(BLACK)
    draw_text("LEADERBOARD", title_font(70), WHITE, 180, 50, SCREEN)

    leaderboard = load_leaderboard()

    for i, entry in enumerate(leaderboard):
        player_text = f"{entry['player']}: {entry['score']}"
        draw_text(player_text, context_font(40), WHITE, 345, 150 + i * 50, SCREEN)

    for button in leaderboard_buttons:
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
    elif LEADERBOARD_SCREEN:
        draw_leaderboard()

    pygame.display.flip()
pygame.quit()
