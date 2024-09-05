import pygame

from utils import GREEN


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.snake_color = GREEN
        self.snake_size = 30
        self.snake_pos = [self.screen.get_width() // 2, self.screen.get_height() // 2]
        self.body = [pygame.Rect(self.snake_pos[0], self.snake_pos[1], self.snake_size, self.snake_size)]
        self.direction = None
        self.snake_speed = 5
        self.moving = False
        self.growing = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if self.direction is None:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction = 'UP'
                self.moving = True
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction = 'DOWN'
                self.moving = True
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction = 'LEFT'
                self.moving = True
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction = 'RIGHT'
                self.moving = True
        else:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if self.direction != 'DOWN':
                    self.direction = 'UP'
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if self.direction != 'UP':
                    self.direction = 'DOWN'
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                if self.direction != 'RIGHT':
                    self.direction = 'LEFT'
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.direction != 'LEFT':
                    self.direction = 'RIGHT'

    def update_pos(self):
        if self.moving:
            if self.direction == 'UP':
                self.snake_pos[1] -= self.snake_speed
            elif self.direction == 'DOWN':
                self.snake_pos[1] += self.snake_speed
            elif self.direction == 'LEFT':
                self.snake_pos[0] -= self.snake_speed
            elif self.direction == 'RIGHT':
                self.snake_pos[0] += self.snake_speed

            new_head = pygame.Rect(self.snake_pos[0], self.snake_pos[1], self.snake_size, self.snake_size)
            self.body.insert(0, new_head)
            if not self.growing:
                self.body.pop()
            else:
                self.growing = False

            if (self.snake_pos[0] < 0 or self.snake_pos[0] >= self.screen.get_width() or
                    self.snake_pos[1] < 0 or self.snake_pos[1] >= self.screen.get_height()):
                return False

            if self.body[0] in self.body[1:]:
                print("Collision")
                return False

        return True

    def grow(self):
        tail = self.body[-1]
        new_segment = None
        if self.direction == 'UP':
            new_segment = pygame.Rect(tail.left, tail.top + (self.snake_size + 10), self.snake_size, self.snake_size)
        elif self.direction == 'DOWN':
            new_segment = pygame.Rect(tail.left, tail.top - (self.snake_size + 10), self.snake_size, self.snake_size)
        elif self.direction == 'LEFT':
            new_segment = pygame.Rect(tail.left + (self.snake_size + 10), tail.top, self.snake_size, self.snake_size)
        elif self.direction == 'RIGHT':
            new_segment = pygame.Rect(tail.left - (self.snake_size + 10), tail.top, self.snake_size, self.snake_size)

        if new_segment:
            self.body.append(new_segment)
            print(f"added new segment at {new_segment}")

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(self.screen, self.snake_color, segment)
