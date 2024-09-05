import pygame

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
DARK_GREY = (30, 30, 30)
LIGHT_GREY = (125, 125, 125)
DIM_GREY = (55, 55, 55)
GREEN = (0, 255, 0)


# define text drawing
def draw_text(text, font, color, x, y, surface):
    img = font.render(text, True, color)
    surface.blit(img, (x, y))


# define fonts
def title_font(size):
    return pygame.font.Font("Assets/ArcadeClassic.ttf", size)


def context_font(size):
    return pygame.font.Font("Assets/computer_pixel-7.ttf", size)
