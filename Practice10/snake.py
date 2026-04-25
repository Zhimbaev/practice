import pygame
import random

pygame.init()

CELL_SIZE = 22
GRID_WIDTH = 24
GRID_HEIGHT = 24

SCREEN_WIDTH  = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

FPS_MAX = 30

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (60,  200, 60)
DARK_GREEN = (30,  140, 30)
RED = (220, 50,  50)
GRAY = (60,  60,  60)
YELLOW = (255, 220, 0)

UP    = (0,  -1)
DOWN  = (0,   1)
LEFT  = (-1,  0)
RIGHT = (1,   0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake - Practice 8")
clock = pygame.time.Clock()

font       = pygame.font.SysFont("arial", 20)
big_font   = pygame.font.SysFont("arial", 30)


def generate_food(snake_body):
    while True:
        fx = random.randint(1, GRID_WIDTH - 2)
        fy = random.randint(1, GRID_HEIGHT - 2)
        pos = (fx, fy)
        if pos not in snake_body:
            return pos


def reset_game():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    next_direction = RIGHT
    food = generate_food(snake)
    score = 0
    level = 1
    foods_eaten = 0
    speed = 6
    return snake, direction, next_direction, food, score, level, foods_eaten, speed


snake, direction, next_direction, food, score, level, foods_eaten, speed = reset_game()
game_over = False


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                next_direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                next_direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                next_direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                next_direction = RIGHT

            if event.key == pygame.K_r and game_over:
                snake, direction, next_direction, food, score, level, foods_eaten, speed = reset_game()
                game_over = False

    if not game_over:
        direction = next_direction

        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        new_head = (head_x, head_y)

        if head_x <= 0 or head_x >= GRID_WIDTH - 1 or \
           head_y <= 0 or head_y >= GRID_HEIGHT - 1:
            game_over = True

        elif new_head in snake:
            game_over = True

        else:
            snake.insert(0, new_head)

            if new_head == food:
                score += 10
                foods_eaten += 1
                food = generate_food(snake)

                if foods_eaten % 3 == 0:
                    level += 1
                    speed += 2

            else:
                snake.pop()

    screen.fill(BLACK)

    for gx in range(GRID_WIDTH):
        pygame.draw.rect(screen, GRAY,
                         (gx * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GRAY,
                         (gx * CELL_SIZE, (GRID_HEIGHT - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for gy in range(GRID_HEIGHT):
        pygame.draw.rect(screen, GRAY,
                         (0, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GRAY,
                         ((GRID_WIDTH - 1) * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    food_rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE,
                            CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, food_rect)
    cx = food[0] * CELL_SIZE + CELL_SIZE // 2
    cy = food[1] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, WHITE, (cx, cy), CELL_SIZE // 4)

    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        seg_rect = pygame.Rect(
            segment[0] * CELL_SIZE + 1,
            segment[1] * CELL_SIZE + 1,
            CELL_SIZE - 2,
            CELL_SIZE - 2
        )
        pygame.draw.rect(screen, color, seg_rect)

    score_surf = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (5, 3))

    level_surf = font.render(f"Level: {level}", True, YELLOW)
    screen.blit(level_surf, (SCREEN_WIDTH - level_surf.get_width() - 5, 3))

    if game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(170)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        t1 = big_font.render("GAME OVER!", True, RED)
        t2 = font.render(f"Score: {score}   Level: {level}", True, WHITE)
        t3 = font.render("Press R to restart", True, YELLOW)
        cx = SCREEN_WIDTH // 2
        cy = SCREEN_HEIGHT // 2
        screen.blit(t1, (cx - t1.get_width() // 2, cy - 60))
        screen.blit(t2, (cx - t2.get_width() // 2, cy - 10))
        screen.blit(t3, (cx - t3.get_width() // 2, cy + 30))

    pygame.display.update()
    clock.tick(speed)