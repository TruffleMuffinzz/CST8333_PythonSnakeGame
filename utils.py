import os
import sys
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

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

arcade_class_path = os.path.join(base_path, 'Assets', 'ArcadeClassic.ttf')
computer_pixel_path = os.path.join(base_path, 'Assets', 'computer_pixel-7.ttf')


# define text drawing
def draw_text(text, font, color, x, y, surface):
    img = font.render(text, True, color)
    surface.blit(img, (x, y))


# define fonts
def title_font(size):
    return pygame.font.Font(arcade_class_path, size)


def context_font(size):
    return pygame.font.Font(computer_pixel_path, size)
