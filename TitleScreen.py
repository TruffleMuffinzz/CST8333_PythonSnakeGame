import pygame

pygame.init()

# set game window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)


# define fonts
def title_font(size):
    return pygame.font.Font("Assets/ArcadeClassic.ttf", size)


def context_font(size):
    return pygame.font.Font("Assets/computer_pixel-7.ttf", size)


# define text drawing
def draw_text(text, font, white, x, y):
    img = font.render(text, True, white)
    SCREEN.blit(img, (x, y))


# loop telling to run
RUN = True

while RUN:
    SCREEN.fill(BLACK)

    MENU_TEXT = title_font(100).render("SNAKE", True, WHITE)
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

    draw_text("SNAKE", title_font(100), WHITE, 250, 150)
    draw_text("by: Elaine DeJoseph", context_font(35), WHITE, 300, 220)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    pygame.display.update()
pygame.quit()
