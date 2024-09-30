import pygame
import random
from utils import RED


class Food:
    def __init__(self, screen, snake_size):
        self.screen = screen
        self.snake_size = snake_size
        self.food_color = RED
        self.food_pos = self.generate_food_pos()
        self.rect = pygame.Rect(self.food_pos[0], self.food_pos[1], self.snake_size, self.snake_size)

    # This will generate the food at a random location on the screen, includes padding to make sure it is on the screen
    def generate_food_pos(self):
        max_x = (self.screen.get_width() // self.snake_size) - 1
        max_y = (self.screen.get_height() // self.snake_size) - 1
        return [random.randint(0, max_x) * self.snake_size,
                random.randint(0, max_y) * self.snake_size]

    def draw(self):
        pygame.draw.rect(self.screen, self.food_color, self.rect)

    def respawn(self):
        self.food_pos = self.generate_food_pos()
        self.rect.topleft = self.food_pos
