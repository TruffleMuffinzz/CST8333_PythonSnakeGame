import pygame
from text_utils import draw_text, LIGHT_GREY


class Button:
    def __init__(self, text, x, y, width, height, font, default_colour, hover_colour, text_colour, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.default_colour = default_colour
        self.hover_colour = hover_colour
        self.text_colour = text_colour
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            colour = self.hover_colour
            if pygame.mouse.get_pressed()[0] and self.action:
                self.action()
        else:
            colour = self.default_colour

        pygame.draw.rect(surface, colour, self.rect)
        pygame.draw.rect(surface, LIGHT_GREY, self.rect, 3, 2)  # border

        # centre the text on the button
        text_surface = self.font.render(self.text, True, self.text_colour)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
