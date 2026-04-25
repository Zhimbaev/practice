import pygame
import random

pygame.init()

SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (220, 50,  50)
BLUE = (50,  100, 220)
YELLOW = (255, 220, 0)
ORANGE = (255, 150, 0)
HOT_PINK = (255, 50,  180)
GRAY = (80,  80,  80)
DARK_GRAY = (40,  40,  40)
LIGHT_GRAY = (160, 160, 160)

COIN_TYPES = [
    {"value": 1, "color": YELLOW,   "weight": 60, "label": "$"},
    {"value": 3, "color": ORANGE,   "weight": 30, "label": "$$"},
    {"value": 5, "color": HOT_PINK, "weight": 10, "label": "$$$"},
]

SPEED_UP_EVERY = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer - Practice 11")
clock      = pygame.time.Clock()
font       = pygame.font.SysFont("arial", 22)
small_font = pygame.font.SysFont("arial", 14)


class PlayerCar:
    def __init__(self):
        self.width  = 50
        self.height = 80
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 20
        self.speed = 6
        self.color = BLUE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 8,  self.width - 14, 18))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 52, self.width - 14, 14))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 54, 8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.width, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.width, self.y + 54, 8, 18))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class EnemyCar:
    def __init__(self, speed):
        self.width  = 50
        self.height = 80
        self.x = random.randint(20, SCREEN_WIDTH - self.width - 20)
        self.y = -self.height
        self.speed = speed
        self.color = RED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 8,  self.width - 14, 18))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 52, self.width - 14, 14))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 54, 8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.width, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.width, self.y + 54, 8, 18))

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class WeightedCoin:
    def __init__(self):
        self.radius = 14

        weights = [ct["weight"] for ct in COIN_TYPES]
        chosen  = random.choices(COIN_TYPES, weights=weights, k=1)[0]

        self.value = chosen["value"]
        self.color = chosen["color"]
        self.label = chosen["label"]

        self.x     = random.randint(30, SCREEN_WIDTH - 30)
        self.y     = -self.radius
        self.speed = 3

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(surface, BLACK, (self.x, self.y), self.radius, 2)

        sign = small_font.render(self.label, True, BLACK)
        surface.blit(sign, (self.x - sign.get_width() // 2,
                             self.y - sign.get_height() // 2))

        if self.value == 5:
            pygame.draw.circle(surface, WHITE, (self.x, self.y), self.radius + 3, 2)

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)


def draw_road(surface, offset):
    surface.fill(GRAY)
    for lane_x in [SCREEN_WIDTH // 3, (SCREEN_WIDTH * 2) // 3]:
        for line_y in range(-60, SCREEN_HEIGHT + 60, 60):
            y_pos = (line_y + offset) % (SCREEN_HEIGHT + 60) - 60
            pygame.draw.rect(surface, LIGHT_GRAY, (lane_x - 3, y_pos, 6, 35))
    pygame.draw.rect(surface, DARK_GRAY, (0, 0, 12, SCREEN_HEIGHT))
    pygame.draw.rect(surface, DARK_GRAY, (SCREEN_WIDTH - 12, 0, 12, SCREEN_HEIGHT))


player = PlayerCar()
enemies = []
coins = []
score = 0
coin_count = 0
enemy_speed = 5
game_over = False
road_offset = 0

enemy_timer = 0
coin_timer = 0
ENEMY_INTERVAL = 80
COIN_INTERVAL = 100

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player = PlayerCar()
                enemies = []
                coins = []
                score = 0
                coin_count = 0
                enemy_speed = 5
                game_over = False
                enemy_timer = 0
                coin_timer = 0
                road_offset = 0

    if not game_over:
        player.move()
        road_offset = (road_offset + enemy_speed) % 60

        enemy_timer += 1
        if enemy_timer >= ENEMY_INTERVAL:
            enemies.append(EnemyCar(enemy_speed))
            enemy_timer = 0

        coin_timer += 1
        if coin_timer >= COIN_INTERVAL:
            coins.append(WeightedCoin())
            coin_timer = 0

        for enemy in enemies:
            enemy.move()
        for coin in coins:
            coin.move()

        alive_enemies = []
        for enemy in enemies:
            if enemy.is_off_screen():
                score += 1
            else:
                alive_enemies.append(enemy)
        enemies = alive_enemies

        alive_coins = []
        for coin in coins:
            if not coin.is_off_screen():
                alive_coins.append(coin)
        coins = alive_coins

        player_rect = player.get_rect()
        collected = []
        for coin in coins:
            if player_rect.colliderect(coin.get_rect()):
                collected.append(coin)
                score += coin.value
                coin_count += 1

        for coin in collected:
            coins.remove(coin)

        needed_speed = 5 + (coin_count // SPEED_UP_EVERY)
        if needed_speed > enemy_speed:
            enemy_speed = needed_speed

        for enemy in enemies:
            if player_rect.colliderect(enemy.get_rect()):
                game_over = True

    draw_road(screen, road_offset)
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for coin in coins:
        coin.draw(screen)

    score_surf = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (20, 10))

    coins_surf = font.render(f"Coins: {coin_count}", True, YELLOW)
    screen.blit(coins_surf, (SCREEN_WIDTH - coins_surf.get_width() - 20, 10))

    spd_surf = small_font.render(f"Enemy speed: {enemy_speed}", True, LIGHT_GRAY)
    screen.blit(spd_surf, (20, 38))

    legend_y = 38
    for ct in COIN_TYPES:
        txt = small_font.render(f"{ct['label']} = {ct['value']}pts", True, ct["color"])
        screen.blit(txt, (SCREEN_WIDTH - txt.get_width() - 20, legend_y))
        legend_y += 18

    if game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(160)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        t1 = font.render("GAME OVER!", True, RED)
        t2 = font.render(f"Score: {score}   Coins: {coin_count}", True, YELLOW)
        t3 = font.render("Press R to restart", True, WHITE)
        cx = SCREEN_WIDTH // 2
        cy = SCREEN_HEIGHT // 2
        screen.blit(t1, (cx - t1.get_width() // 2, cy - 60))
        screen.blit(t2, (cx - t2.get_width() // 2, cy - 15))
        screen.blit(t3, (cx - t3.get_width() // 2, cy + 30))

    pygame.display.update()
    clock.tick(FPS)