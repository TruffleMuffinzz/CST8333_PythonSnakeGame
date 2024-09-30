import pygame
import json
import os
import sys

from utils import BLACK, draw_text, context_font, WHITE, title_font, LIGHT_GREY
from snake import Snake
from food import Food

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

leaderboard_path = os.path.join(base_path, 'Assets', 'leaderboard.json')


def load_leaderboard():
    try:
        with open(leaderboard_path, 'r') as file:
            data = json.load(file)
            print("Loaded leaderboard:", data)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return [
            {"player": "AAA", "score": 100},
            {"player": "BBB", "score": 50},
            {"player": "CCC", "score": 25}
        ]


def save_leaderboard(leaderboard):
    with open(leaderboard_path, 'w') as file:
        json.dump(leaderboard, file, indent=4)


def is_high_score(score, leaderboard):
    return any(score > entry["score"] for entry in leaderboard)


def update_leaderboard(player, score, leaderboard):
    leaderboard.append({"player": player, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)  # sorts by score, highest to lowest
    leaderboard.pop()  # removes the lowest score from the leaderboard
    save_leaderboard(leaderboard)


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
                self.game_over_with_lb()
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

    def game_over_with_lb(self):
        leaderboard = load_leaderboard()

        if is_high_score(self.score, leaderboard):
            self.prompt_initials()
        else:
            self.show_game_over()

    # Game over screen display and logic
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
        draw_text("Press Q to Quit, R to restart, or L for leaderboard",
                  context_font(30),
                  WHITE,
                  125,
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
                    if event.key == pygame.K_l:
                        self.show_leaderboard()
                        self.show_game_over()

    def show_leaderboard(self):
        leaderboard = load_leaderboard()

        while True:
            self.screen.fill(BLACK)
            draw_text("Leaderboard", title_font(70), WHITE, 180, 50, self.screen)

            for i, entry in enumerate(leaderboard):
                draw_text(f"{i + 1}. {entry['player']} - {entry['score']}",
                          context_font(40), WHITE, 300, 150 + i * 50, self.screen)

            draw_text("Press B to go back", context_font(40), WHITE, 250, 150 + len(leaderboard) * 50 + 20, self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        return

    def prompt_initials(self):
        player_initials = ""
        while True:
            self.screen.fill(BLACK)
            draw_text("New High Score!", title_font(70), WHITE, 160, 50, self.screen)
            draw_text(f"Score: {self.score}", context_font(40), WHITE, 340, 150, self.screen)
            draw_text(f"Enter your initials: {player_initials}", context_font(40), WHITE, 230, 200, self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if len(player_initials) < 3 and event.unicode.isalpha():
                        player_initials += event.unicode.upper()
                    elif event.key == pygame.K_BACKSPACE and len(player_initials) > 0:
                        player_initials = player_initials[:-1]
                    elif event.key == pygame.K_RETURN and len(player_initials) == 3:
                        leaderboard = load_leaderboard()
                        update_leaderboard(player_initials, self.score, leaderboard)
                        self.show_game_over()
                        return

    def display_score(self):
        draw_text(f"Score: {self.score}", context_font(40), WHITE, 10, 10, self.screen)
