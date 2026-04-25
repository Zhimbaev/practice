import pygame
import random

pygame.init()

CELL_SIZE = 22
GRID_WIDTH = 24
GRID_HEIGHT = 24
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (60,  200, 60)
DARK_GREEN = (30,  140, 30)
RED = (220, 50,  50)
ORANGE = (255, 150, 0)
HOT_PINK = (255, 50,  180)
GRAY = (60,  60,  60)
YELLOW = (255, 220, 0)

UP    = (0,  -1)
DOWN  = (0,   1)
LEFT  = (-1,  0)
RIGHT = (1,   0)

screen   = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake - Practice 11")
clock    = pygame.time.Clock()
font     = pygame.font.SysFont("arial", 18)
big_font = pygame.font.SysFont("arial", 28)

FOOD_TYPES = [
    {"value": 10, "color": RED,      "weight": 60, "lifetime": 7000},  # Обычная — 7 сек
    {"value": 25, "color": ORANGE,   "weight": 30, "lifetime": 5000},  # Редкая — 5 сек
    {"value": 50, "color": HOT_PINK, "weight": 10, "lifetime": 3000},  # Супер — 3 сек
]

MAX_FOODS = 3


class Food:
    def __init__(self, pos, food_type):
        self.pos = pos
        self.value = food_type["value"]
        self.color = food_type["color"]
        self.lifetime = food_type["lifetime"]
        self.spawn_time = pygame.time.get_ticks()

    def is_expired(self):
        now = pygame.time.get_ticks()
        return (now - self.spawn_time) >= self.lifetime

    def time_left_ratio(self):
        now = pygame.time.get_ticks()
        elapsed = now - self.spawn_time
        ratio = 1.0 - (elapsed / self.lifetime)
        if ratio < 0:
            ratio = 0
        return ratio

    def draw(self, surface):
        fx = self.pos[0] * CELL_SIZE
        fy = self.pos[1] * CELL_SIZE
        pygame.draw.rect(surface, self.color, (fx, fy, CELL_SIZE, CELL_SIZE))

        ratio = self.time_left_ratio()
        bar_w = int(CELL_SIZE * ratio)
        pygame.draw.rect(surface, WHITE, (fx, fy + CELL_SIZE - 4, CELL_SIZE, 4))
        pygame.draw.rect(surface, YELLOW, (fx, fy + CELL_SIZE - 4, bar_w, 4))
        label = font.render(str(self.value), True, WHITE)
        surface.blit(label, (fx + CELL_SIZE // 2 - label.get_width() // 2,
                              fy + CELL_SIZE // 2 - label.get_height() // 2))

        if self.value == 50:
            pygame.draw.rect(surface, WHITE, (fx, fy, CELL_SIZE, CELL_SIZE), 2)


def generate_food(snake_body, existing_foods):
    food_positions = [f.pos for f in existing_foods]

    attempts = 0
    while attempts < 200:
        fx = random.randint(1, GRID_WIDTH  - 2)
        fy = random.randint(1, GRID_HEIGHT - 2)
        pos = (fx, fy)

        if pos not in snake_body and pos not in food_positions:
            weights = [ft["weight"] for ft in FOOD_TYPES]
            chosen  = random.choices(FOOD_TYPES, weights=weights, k=1)[0]
            return Food(pos, chosen)

        attempts += 1

    return None


def reset_game():
    snake          = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction      = RIGHT
    next_direction = RIGHT
    score          = 0
    level          = 1
    foods_eaten    = 0
    speed          = 6

    foods = []
    first_food = generate_food(snake, foods)
    if first_food:
        foods.append(first_food)

    return snake, direction, next_direction, foods, score, level, foods_eaten, speed


snake, direction, next_direction, foods, score, level, foods_eaten, speed = reset_game()
game_over = False


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP    and direction != DOWN:
                next_direction = UP
            elif event.key == pygame.K_DOWN  and direction != UP:
                next_direction = DOWN
            elif event.key == pygame.K_LEFT  and direction != RIGHT:
                next_direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                next_direction = RIGHT

            if event.key == pygame.K_r and game_over:
                snake, direction, next_direction, foods, score, level, foods_eaten, speed = reset_game()
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

            eaten_food = None
            for food in foods:
                if new_head == food.pos:
                    eaten_food = food
                    break

            if eaten_food is not None:
                score       += eaten_food.value
                foods_eaten += 1
                foods.remove(eaten_food)

                if foods_eaten % 3 == 0:
                    level += 1
                    speed += 2

            else:
                snake.pop()

        alive_foods = []
        for food in foods:
            if not food.is_expired():
                alive_foods.append(food)
        foods = alive_foods

        while len(foods) < MAX_FOODS:
            new_food = generate_food(snake, foods)
            if new_food is not None:
                foods.append(new_food)
            else:
                break

    screen.fill(BLACK)

    for gx in range(GRID_WIDTH):
        pygame.draw.rect(screen, GRAY, (gx * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GRAY, (gx * CELL_SIZE, (GRID_HEIGHT - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for gy in range(GRID_HEIGHT):
        pygame.draw.rect(screen, GRAY, (0, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GRAY, ((GRID_WIDTH - 1) * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for food in foods:
        food.draw(screen)

    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        seg_rect = pygame.Rect(segment[0] * CELL_SIZE + 1, segment[1] * CELL_SIZE + 1,
                               CELL_SIZE - 2, CELL_SIZE - 2)
        pygame.draw.rect(screen, color, seg_rect)

    score_surf = font.render(f"Score: {score}", True, WHITE)
    level_surf = font.render(f"Level: {level}", True, YELLOW)
    screen.blit(score_surf, (5, 3))
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