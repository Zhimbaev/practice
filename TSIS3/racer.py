import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (220, 50,  50)
BLUE = (50,  100, 220)
YELLOW = (255, 220, 0)
ORANGE = (255, 150, 0)
HOT_PINK = (255, 50,  180)
GREEN = (50,  200, 50)
GRAY = (80,  80,  80)
DARK_GRAY = (40,  40,  40)
LIGHT_GRAY = (160, 160, 160)
CYAN = (0,   200, 220)
PURPLE = (180, 50,  220)
OIL_COLOR = (30,  20,  50)
NITRO_COLOR = (0,   220, 200)


COIN_TYPES = [
    {"value": 1, "color": YELLOW, "weight": 60, "label": "$"},
    {"value": 3, "color": ORANGE, "weight": 30, "label": "$$"},
    {"value": 5, "color": HOT_PINK, "weight": 10, "label": "$$$"},
]

POWERUP_TYPES = ["nitro", "shield", "repair"]
POWERUP_COLORS = {"nitro": CYAN, "shield": GREEN, "repair": ORANGE}
POWERUP_LABELS = {"nitro": "N", "shield": "S", "repair": "R"}

DIFF_SETTINGS = {
    "easy":   {"start_speed": 4, "interval": 95},
    "normal": {"start_speed": 5, "interval": 80},
    "hard":   {"start_speed": 7, "interval": 60},
}


class PlayerCar:
    def __init__(self, color, sw, sh):
        self.w = 50
        self.h = 80
        self.x = sw // 2 - self.w // 2
        self.y = sh - self.h - 20
        self.base_speed = 6
        self.color = tuple(color)
        self.shield = False

    def move(self, sw, extra_speed=0):
        keys = pygame.key.get_pressed()
        sp = self.base_speed + extra_speed
        if keys[pygame.K_LEFT]:
            self.x -= sp
        if keys[pygame.K_RIGHT]:
            self.x += sp
        self.x = max(0, min(self.x, sw - self.w))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 8,  self.w - 14, 18))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 52, self.w - 14, 14))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 54, 8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.w, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.w, self.y + 54, 8, 18))
        if self.shield:
            pygame.draw.rect(surface, GREEN, (self.x - 4, self.y - 4, self.w + 8, self.h + 8), 3)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


class EnemyCar:
    def __init__(self, speed, sw):
        self.w = 50
        self.h = 80
        self.x = random.randint(20, sw - self.w - 20)
        self.y = -self.h
        self.speed = speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 8,  self.w - 14, 18))
        pygame.draw.rect(surface, DARK_GRAY, (self.x + 7, self.y + 52, self.w - 14, 14))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x - 8, self.y + 54, 8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.w, self.y + 8,  8, 18))
        pygame.draw.rect(surface, BLACK, (self.x + self.w, self.y + 54, 8, 18))

    def move(self):
        self.y += self.speed

    def off_screen(self, sh):
        return self.y > sh

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


class WeightedCoin:
    def __init__(self, sw):
        self.r = 14
        weights = [ct["weight"] for ct in COIN_TYPES]
        chosen = random.choices(COIN_TYPES, weights=weights, k=1)[0]
        self.value = chosen["value"]
        self.color = chosen["color"]
        self.label = chosen["label"]
        self.x = random.randint(30, sw - 30)
        self.y = -self.r
        self.speed = 3

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(surface, BLACK,       (self.x, self.y), self.r, 2)
        f = pygame.font.SysFont("arial", 11)
        s = f.render(self.label, True, BLACK)
        surface.blit(s, (self.x - s.get_width() // 2, self.y - s.get_height() // 2))

    def move(self):
        self.y += self.speed

    def off_screen(self, sh):
        return self.y > sh

    def get_rect(self):
        return pygame.Rect(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)


class PowerUp:
    def __init__(self, sw, sh):
        kind = random.choice(POWERUP_TYPES)
        self.kind  = kind
        self.color = POWERUP_COLORS[kind]
        self.label = POWERUP_LABELS[kind]
        self.r = 16
        self.x= random.randint(30, sw - 30)
        self.y = -self.r
        self.speed = 3
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 8000

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(surface, WHITE,      (self.x, self.y), self.r, 2)
        f = pygame.font.SysFont("arial", 14, bold=True)
        s = f.render(self.label, True, BLACK)
        surface.blit(s, (self.x - s.get_width() // 2, self.y - s.get_height() // 2))

    def move(self):
        self.y += self.speed

    def off_screen(self, sh):
        return self.y > sh

    def expired(self):
        return (pygame.time.get_ticks() - self.spawn_time) >= self.lifetime

    def get_rect(self):
        return pygame.Rect(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)


class OilSpill:
    def __init__(self, sw):
        self.w = random.randint(60, 130)
        self.h = 30
        self.x = random.randint(20, sw - self.w - 20)
        self.y = -self.h
        self.speed = 4

    def draw(self, surface):
        oil_surf = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        oil_surf.fill((30, 20, 50, 200))
        surface.blit(oil_surf, (self.x, self.y))
        pygame.draw.rect(surface, (60, 40, 90), (self.x, self.y, self.w, self.h), 2)
        f = pygame.font.SysFont("arial", 10)
        s = f.render("OIL", True, (180, 150, 220))
        surface.blit(s, (self.x + self.w // 2 - s.get_width() // 2, self.y + 8))

    def move(self):
        self.y += self.speed

    def off_screen(self, sh):
        return self.y > sh

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


class NitroStrip:
    def __init__(self, sw):
        self.w = sw - 40
        self.h = 18
        self.x = 20
        self.y = -self.h
        self.speed = 4

    def draw(self, surface):
        pygame.draw.rect(surface, NITRO_COLOR, (self.x, self.y, self.w, self.h))
        f = pygame.font.SysFont("arial", 11)
        s = f.render("NITRO STRIP", True, BLACK)
        surface.blit(s, (self.x + self.w // 2 - s.get_width() // 2, self.y + 2))

    def move(self):
        self.y += self.speed

    def off_screen(self, sh):
        return self.y > sh

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


class Obstacle:
    def __init__(self, sw, player_x):
        self.w = 28
        self.h = 36
        attempts = 0
        while True:
            self.x = random.randint(20, sw - self.w - 20)
            if abs(self.x - player_x) > 80 or attempts > 30:
                break
            attempts += 1
        self.y = -self.h
        self.speed = 4

    def draw(self, surface):
        cx = self.x + self.w // 2
        pygame.draw.polygon(surface, ORANGE, [
            (cx, self.y), (self.x, self.y + self.h), (self.x + self.w, self.y + self.h)
        ])
        pygame.draw.polygon(surface, WHITE, [
            (cx, self.y), (self.x, self.y + self.h), (self.x + self.w, self.y + self.h)
        ], 2)
        pygame.draw.rect(surface, WHITE, (cx - 3, self.y + 10, 6, 14))

    def move(self):
        self.y += self.speed

    def off_screen(self, sh):
        return self.y > sh

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


def draw_road(surface, offset, sw, sh):
    surface.fill(GRAY)
    for lx in [sw // 3, (sw * 2) // 3]:
        for ly in range(-60, sh + 60, 60):
            yp = (ly + offset) % (sh + 60) - 60
            pygame.draw.rect(surface, LIGHT_GRAY, (lx - 3, yp, 6, 35))
    pygame.draw.rect(surface, DARK_GRAY, (0, 0, 12, sh))
    pygame.draw.rect(surface, DARK_GRAY, (sw - 12, 0, 12, sh))


def run_game(screen, clock, settings, username):
    sw, sh = screen.get_size()
    diff   = DIFF_SETTINGS.get(settings.get("difficulty", "normal"), DIFF_SETTINGS["normal"])

    player = PlayerCar(settings.get("car_color", [50, 100, 220]), sw, sh)
    enemies = []
    coins = []
    power_ups = []
    oil_spills = []
    nitro_strips = []
    obstacles = []

    score = 0
    coin_count = 0
    distance = 0
    enemy_speed = diff["start_speed"]
    game_over = False
    road_offset = 0

    enemy_timer = 0
    coin_timer = 0
    oil_timer = 0
    nitro_timer = 0
    obs_timer = 0
    pu_timer = 0

    ENEMY_IV = diff["interval"]
    COIN_IV = 110
    OIL_IV = 300
    NITRO_IV = 500
    OBS_IV = 200
    PU_IV = 350

    nitro_end = 0
    oil_slow_end = 0
    active_pu = None

    font = pygame.font.SysFont("arial", 22)
    fsmall = pygame.font.SysFont("arial", 14)

    enemies.append(EnemyCar(enemy_speed, sw))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return {"score": score, "distance": distance, "coins": coin_count, "cancelled": True}

        if not game_over:
            now = pygame.time.get_ticks()

            nitro_active = now < nitro_end
            oil_active = now < oil_slow_end

            extra_sp = 3 if nitro_active else 0
            player.move(sw, extra_sp)

            road_offset = (road_offset + enemy_speed) % 60
            distance   += enemy_speed

            enemy_timer += 1
            if enemy_timer >= ENEMY_IV:
                enemies.append(EnemyCar(enemy_speed, sw))
                enemy_timer = 0

            coin_timer += 1
            if coin_timer >= COIN_IV:
                coins.append(WeightedCoin(sw))
                coin_timer = 0

            oil_timer += 1
            if oil_timer >= OIL_IV:
                oil_spills.append(OilSpill(sw))
                oil_timer = 0

            nitro_timer += 1
            if nitro_timer >= NITRO_IV:
                nitro_strips.append(NitroStrip(sw))
                nitro_timer = 0

            obs_timer += 1
            if obs_timer >= OBS_IV:
                obstacles.append(Obstacle(sw, player.x))
                obs_timer = 0

            pu_timer += 1
            if pu_timer >= PU_IV and len(power_ups) == 0:
                power_ups.append(PowerUp(sw, sh))
                pu_timer = 0

            for e in enemies:
                e.speed = enemy_speed
                e.move()
            for c in coins:
                c.move()
            for pu in power_ups:
                pu.move()
            for o in oil_spills:
                o.move()
            for ns in nitro_strips:
                ns.move()
            for ob in obstacles:
                ob.move()

            alive_e = []
            for e in enemies:
                if e.off_screen(sh):
                    score += 1
                else:
                    alive_e.append(e)
            enemies = alive_e

            coins = [c for c in coins       if not c.off_screen(sh)]
            power_ups = [p for p in power_ups   if not p.off_screen(sh) and not p.expired()]
            oil_spills = [o for o in oil_spills  if not o.off_screen(sh)]
            nitro_strips = [n for n in nitro_strips if not n.off_screen(sh)]
            obstacles = [o for o in obstacles   if not o.off_screen(sh)]

            pr = player.get_rect()

            collected = [c for c in coins if pr.colliderect(c.get_rect())]
            for c in collected:
                score += c.value
                coin_count += 1
                coins.remove(c)

            needed_speed = diff["start_speed"] + (coin_count // 5)
            if needed_speed > enemy_speed:
                enemy_speed = needed_speed

            for pu in list(power_ups):
                if pr.colliderect(pu.get_rect()):
                    active_pu = pu.kind
                    if pu.kind == "nitro":
                        nitro_end = now + 4000
                    elif pu.kind == "shield":
                        player.shield = True
                    elif pu.kind == "repair":
                        oil_slow_end = 0
                    power_ups.remove(pu)

            for o in list(oil_spills):
                if pr.colliderect(o.get_rect()):
                    oil_slow_end = now + 2500

            for ns in list(nitro_strips):
                if pr.colliderect(ns.get_rect()):
                    nitro_end = now + 3000

            for ob in list(obstacles):
                if pr.colliderect(ob.get_rect()):
                    game_over = True

            for e in enemies:
                if pr.colliderect(e.get_rect()):
                    if player.shield:
                        player.shield = False
                        enemies.remove(e)
                        break
                    else:
                        game_over = True
                        break

        draw_road(screen, road_offset, sw, sh)
        player.draw(screen)
        for e in enemies:
            e.draw(screen)
        for c in coins:
            c.draw(screen)
        for pu in power_ups:
            pu.draw(screen)
        for o in oil_spills:
            o.draw(screen)
        for ns in nitro_strips:
            ns.draw(screen)
        for ob in obstacles:
            ob.draw(screen)

        screen.blit(font.render(f"Score: {score}", True, WHITE), (20, 10))
        screen.blit(font.render(f"Coins: {coin_count}", True, YELLOW), (sw - 160, 10))
        dist_km = distance // 100
        screen.blit(fsmall.render(f"Dist: {dist_km}m", True, LIGHT_GRAY), (20, 38))
        screen.blit(fsmall.render(f"Spd: {enemy_speed}", True, LIGHT_GRAY), (20, 56))

        if pygame.time.get_ticks() < nitro_end:
            rem = (nitro_end - pygame.time.get_ticks()) // 1000 + 1
            screen.blit(font.render(f"NITRO {rem}s", True, CYAN), (sw // 2 - 50, 10))
        if player.shield:
            screen.blit(font.render("SHIELD", True, GREEN), (sw // 2 - 45, 10))
        if pygame.time.get_ticks() < oil_slow_end:
            screen.blit(fsmall.render("OIL SLOW", True, (180, 150, 220)), (sw // 2 - 40, 36))

        if game_over:
            ov = pygame.Surface((sw, sh))
            ov.set_alpha(160)
            ov.fill(BLACK)
            screen.blit(ov, (0, 0))
            f2 = pygame.font.SysFont("arial", 30)
            f3 = pygame.font.SysFont("arial", 18)
            cx = sw // 2
            cy = sh // 2
            screen.blit(f2.render("GAME OVER", True, RED),   (cx - 90, cy - 70))
            screen.blit(f3.render(f"Score: {score}   Dist: {dist_km}m   Coins: {coin_count}", True, YELLOW), (cx - 160, cy - 20))
            screen.blit(f3.render("Press ENTER to continue", True, WHITE), (cx - 110, cy + 20))
            pygame.display.update()
            waiting = True
            while waiting:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        waiting = False
            return {"score": score, "distance": dist_km, "coins": coin_count, "cancelled": False}

        pygame.display.update()
        clock.tick(60)
