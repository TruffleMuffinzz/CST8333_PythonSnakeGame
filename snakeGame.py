import pygame

from utils import BLACK, draw_text, context_font, WHITE, title_font, LIGHT_GREY
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 650
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

        self.snake = Snake(self.screen)
        self.food = Food(self.screen, self.snake.snake_size)

        self.game_over = False
        self.score = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if self.game_over:
                self.show_game_over()
                continue

            # telling the game to accept keyboard input
            self.snake.handle_input()

            # if update_pos returns false, game over screen shows
            if not self.snake.update_pos():
                self.game_over = True

            # handle when snake's head touches food. Grows snake's body, respawns food, and adds to score.
            if self.snake.body[0].colliderect(self.food.rect):
                self.snake.grow()
                self.food.respawn()
                self.score += 1

            self.screen.fill(BLACK)
            self.snake.draw()
            self.food.draw()
            self.display_score()

            pygame.display.flip()
            self.clock.tick(60)

    def show_game_over(self):
        self.screen.fill(BLACK)
        # Show the text for the game over screen
        draw_text("Game Over", title_font(100),
                  WHITE,
                  170,
                  50,
                  self.screen)
        if self.score != 0:
            draw_text(f"Your score was: {self.score}",
                      context_font(50),
                      WHITE,
                      230,
                      140,
                      self.screen)
        else:
            draw_text("Why did you just do that?",
                      context_font(50),
                      LIGHT_GREY,
                      173,
                      140,
                      self.screen)
        draw_text("Press Q to Quit or R to restart",
                  context_font(35),
                  WHITE,
                  193,
                  250,
                  self.screen)

        pygame.display.flip()

        # Check for user input on game over screen
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return
                    if event.key == pygame.K_r:
                        self.snake = Snake(self.screen)
                        self.food = Food(self.screen, self.snake.snake_size)
                        self.score = 0
                        self.game_over = False
                        waiting = False

    def display_score(self):
        draw_text(f"Score: {self.score}", context_font(40), WHITE, 10, 10, self.screen)
