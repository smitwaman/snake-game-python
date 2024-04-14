import pygame
import random
import os

# Initialize SDL_AUDIODRIVER to dummy to avoid ALSA errors
os.environ['SDL_AUDIODRIVER'] = 'dummy'

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
APPLE_SIZE = 50
SNAKE_SIZE = 50
SNAKE_SPEED = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Load images
try:
    apple_img = pygame.image.load('assets/apple.png')
    snake_body_img = pygame.image.load('assets/snake_body.png')
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    exit()

# Snake and Apple positions
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
apple = (random.randint(0, (SCREEN_WIDTH - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE,
         random.randint(0, (SCREEN_HEIGHT - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE)

# Direction
direction = 'RIGHT'

# Score
score = 0

# Clock
clock = pygame.time.Clock()

def draw_snake(snake):
    for pos in snake:
        screen.blit(snake_body_img, pos)

def draw_apple(apple):
    screen.blit(apple_img, apple)

def move_snake(snake, direction):
    head = list(snake[0])
    if direction == 'UP':
        head[1] -= SNAKE_SPEED
    elif direction == 'DOWN':
        head[1] += SNAKE_SPEED
    elif direction == 'LEFT':
        head[0] -= SNAKE_SPEED
    elif direction == 'RIGHT':
        head[0] += SNAKE_SPEED
    snake.insert(0, tuple(head))
    snake.pop()

def collision_with_apple(snake, apple):
    return snake[0] == apple

def main():
    global direction
    global score
    global apple

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        screen.fill(BLACK)

        # Draw snake
        draw_snake(snake)

        # Move snake
        move_snake(snake, direction)

        # Draw apple
        draw_apple(apple)

        # Check collision with apple
        if collision_with_apple(snake, apple):
            score += 1
            apple = (random.randint(0, (SCREEN_WIDTH - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE,
                     random.randint(0, (SCREEN_HEIGHT - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE)
            snake.append(snake[-1])

        pygame.display.update()
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()
