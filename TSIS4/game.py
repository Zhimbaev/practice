import pygame
import random
import config

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
DARK_GREEN = (30,  140, 30)
GRAY = (60,  60,  60)
YELLOW = (255, 220, 0)
DARK_GRAY  = (90,  90,  90)
UP = (0,  -1)
DOWN = (0,   1)
LEFT = (-1,  0)
RIGHT = (1,   0)


class Food:
    def __init__(self, pos, ftype):
        self.pos = pos
        self.value = ftype["value"]
        self.color = ftype["color"]
        self.lifetime  = ftype["lifetime"]
        self.spawn_time = pygame.time.get_ticks()
        self.is_poison = False

    def expired(self):
        return (pygame.time.get_ticks() - self.spawn_time) >= self.lifetime

    def time_ratio(self):
        elapsed = pygame.time.get_ticks() - self.spawn_time
        r = 1.0 - elapsed / self.lifetime
        return max(0.0, r)

    def draw(self, surface):
        fx = self.pos[0] * config.CELL_SIZE
        fy = self.pos[1] * config.CELL_SIZE
        cs = config.CELL_SIZE
        pygame.draw.rect(surface, self.color, (fx, fy, cs, cs))
        bar_w = int(cs * self.time_ratio())
        pygame.draw.rect(surface, (60, 60, 60), (fx, fy + cs - 4, cs, 4))
        pygame.draw.rect(surface, YELLOW,       (fx, fy + cs - 4, bar_w, 4))
        f = pygame.font.SysFont("arial", 13)
        s = f.render(str(self.value), True, WHITE)
        surface.blit(s, (fx + cs // 2 - s.get_width() // 2, fy + cs // 2 - s.get_height() // 2))


class PoisonFood:
    def __init__(self, pos):
        self.pos = pos
        self.color = config.POISON_COLOR
        self.is_poison = True
        self.lifetime = 6000
        self.spawn_time = pygame.time.get_ticks()

    def expired(self):
        return (pygame.time.get_ticks() - self.spawn_time) >= self.lifetime

    def time_ratio(self):
        elapsed = pygame.time.get_ticks() - self.spawn_time
        return max(0.0, 1.0 - elapsed / self.lifetime)

    def draw(self, surface):
        fx = self.pos[0] * config.CELL_SIZE
        fy = self.pos[1] * config.CELL_SIZE
        cs = config.CELL_SIZE
        pygame.draw.rect(surface, self.color, (fx, fy, cs, cs))
        pygame.draw.rect(surface, (200, 50, 80), (fx, fy, cs, cs), 2)
        bar_w = int(cs * self.time_ratio())
        pygame.draw.rect(surface, (60, 60, 60), (fx, fy + cs - 4, cs, 4))
        pygame.draw.rect(surface, (220, 80, 80), (fx, fy + cs - 4, bar_w, 4))
        f = pygame.font.SysFont("arial", 13)
        s = f.render("!", True, (255, 100, 120))
        surface.blit(s, (fx + cs // 2 - s.get_width() // 2, fy + cs // 2 - s.get_height() // 2))


class PowerUp:
    def __init__(self, pos, kind):
        self.pos = pos
        self.kind = kind
        self.color = config.PU_COLORS[kind]
        self.spawn_time = pygame.time.get_ticks()

    def expired(self):
        return (pygame.time.get_ticks() - self.spawn_time) >= config.PU_LIFETIME

    def draw(self, surface):
        fx = self.pos[0] * config.CELL_SIZE
        fy = self.pos[1] * config.CELL_SIZE
        cs = config.CELL_SIZE
        pygame.draw.rect(surface, self.color, (fx + 2, fy + 2, cs - 4, cs - 4))
        pygame.draw.rect(surface, WHITE, (fx + 2, fy + 2, cs - 4, cs - 4), 2)
        labels = {"speed": ">>", "slow": "<<", "shield": "*"}
        f = pygame.font.SysFont("arial", 11)
        s = f.render(labels[self.kind], True, BLACK)
        surface.blit(s, (fx + cs // 2 - s.get_width() // 2, fy + cs // 2 - s.get_height() // 2))


def free_pos(snake, foods, obstacles, poison=None, power_up=None):
    occupied = set(snake)
    for fd in foods:
        occupied.add(fd.pos)
    occupied.update(obstacles)
    if poison:
        occupied.add(poison.pos)
    if power_up:
        occupied.add(power_up.pos)
    attempts = 0
    while attempts < 300:
        x = random.randint(1, config.GRID_WIDTH  - 2)
        y = random.randint(1, config.GRID_HEIGHT - 2)
        p = (x, y)
        if p not in occupied:
            return p
        attempts += 1
    return None


def make_food(snake, foods, obstacles, poison, power_up):
    pos = free_pos(snake, foods, obstacles, poison, power_up)
    if pos is None:
        return None
    weights = [ft["weight"] for ft in config.FOOD_TYPES]
    chosen  = random.choices(config.FOOD_TYPES, weights=weights, k=1)[0]
    return Food(pos, chosen)


def make_obstacles(snake, level):
    count = (level - 3) * 3 + 3
    existing = set(snake)
    result = set()
    head = snake[0]
    for _ in range(count * 5):
        if len(result) >= count:
            break
        x = random.randint(1, config.GRID_WIDTH  - 2)
        y = random.randint(1, config.GRID_HEIGHT - 2)
        p = (x, y)
        if p in existing or p in result:
            continue
        if abs(x - head[0]) <= 3 and abs(y - head[1]) <= 3:
            continue
        result.add(p)
        existing.add(p)
    return result


def run_game(screen, clock, settings, username, personal_best):
    gw = config.GRID_WIDTH
    gh = config.GRID_HEIGHT
    cs = config.CELL_SIZE
    sw = config.SCREEN_W
    sh = config.SCREEN_H

    snake_color  = tuple(settings.get("snake_color", [60, 200, 60]))
    grid_overlay = settings.get("grid_overlay", True)

    snake = [(gw // 2, gh // 2)]
    direction = RIGHT
    next_dir = RIGHT
    foods = []
    poison_food = None
    power_up = None
    obstacles = set()

    score = 0
    level = 1
    foods_eaten = 0
    speed = config.BASE_SPEED
    game_over = False

    pu_effect = None
    pu_end_time = 0
    shield_active = False

    poison_timer = 0
    POISON_IV = 220
    pu_spawn_timer = 0
    PU_IV = 300

    font = pygame.font.SysFont("arial", 16)
    font_big = pygame.font.SysFont("arial", 28)

    first_food = make_food(snake, foods, obstacles, poison_food, power_up)
    if first_food:
        foods.append(first_food)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    next_dir = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    next_dir = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    next_dir = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    next_dir = RIGHT
                if event.key == pygame.K_ESCAPE:
                    return {"score": score, "level": level, "cancelled": True}

        if not game_over:
            now = pygame.time.get_ticks()

            direction = next_dir
            hx = snake[0][0] + direction[0]
            hy = snake[0][1] + direction[1]
            new_head = (hx, hy)

            hit_wall = hx <= 0 or hx >= gw - 1 or hy <= 0 or hy >= gh - 1
            hit_self = new_head in snake
            hit_obs  = new_head in obstacles

            if (hit_wall or hit_self or hit_obs) and not shield_active:
                game_over = True
            else:
                if (hit_wall or hit_self or hit_obs) and shield_active:
                    shield_active = False
                else:
                    snake.insert(0, new_head)

                    ate_food = None
                    ate_poison = False
                    for fd in foods:
                        if new_head == fd.pos:
                            ate_food = fd
                            break
                    if poison_food and new_head == poison_food.pos:
                        ate_poison  = True
                        poison_food = None

                    ate_pu = False
                    if power_up and new_head == power_up.pos:
                        ate_pu = True
                        pu_type = power_up.kind
                        power_up = None

                    if ate_food:
                        score += ate_food.value
                        foods_eaten += 1
                        foods.remove(ate_food)
                        if foods_eaten % 3 == 0:
                            level += 1
                            speed += 2
                            if level >= 3:
                                obstacles = make_obstacles(snake, level)
                    elif ate_poison:
                        for _ in range(2):
                            if len(snake) > 1:
                                snake.pop()
                        if len(snake) <= 1:
                            game_over = True
                    else:
                        snake.pop()

                    if ate_pu:
                        pu_effect = pu_type
                        if pu_type == "speed":
                            pu_end_time = now + 5000
                        elif pu_type == "slow":
                            pu_end_time = now + 5000
                        elif pu_type == "shield":
                            shield_active = True
                            pu_end_time = 0

            if pu_effect in ("speed", "slow") and now > pu_end_time:
                pu_effect = None

            alive_foods = [fd for fd in foods if not fd.expired()]
            foods = alive_foods

            while len(foods) < config.MAX_FOODS:
                nf = make_food(snake, foods, obstacles, poison_food, power_up)
                if nf:
                    foods.append(nf)
                else:
                    break

            poison_timer += 1
            if poison_timer >= POISON_IV and poison_food is None:
                pp = free_pos(snake, foods, obstacles, None, power_up)
                if pp:
                    poison_food = PoisonFood(pp)
                poison_timer = 0
            if poison_food and poison_food.expired():
                poison_food = None

            pu_spawn_timer += 1
            if pu_spawn_timer >= PU_IV and power_up is None:
                pp2 = free_pos(snake, foods, obstacles, poison_food, None)
                if pp2:
                    kind = random.choice(["speed", "slow", "shield"])
                    power_up = PowerUp(pp2, kind)
                pu_spawn_timer = 0
            if power_up and power_up.expired():
                power_up = None

        screen.fill(BLACK)

        if grid_overlay:
            for gx in range(gw):
                for gy in range(gh):
                    pygame.draw.rect(screen, (15, 15, 15),
                                     (gx * cs + 1, gy * cs + 1, cs - 2, cs - 2))

        for gx in range(gw):
            pygame.draw.rect(screen, GRAY, (gx * cs, 0, cs, cs))
            pygame.draw.rect(screen, GRAY, (gx * cs, (gh - 1) * cs, cs, cs))
        for gy in range(gh):
            pygame.draw.rect(screen, GRAY, (0, gy * cs, cs, cs))
            pygame.draw.rect(screen, GRAY, ((gw - 1) * cs, gy * cs, cs, cs))

        for ob in obstacles:
            pygame.draw.rect(screen, DARK_GRAY, (ob[0] * cs, ob[1] * cs, cs, cs))
            pygame.draw.rect(screen, (120, 120, 120), (ob[0] * cs, ob[1] * cs, cs, cs), 1)

        for fd in foods:
            fd.draw(screen)
        if poison_food:
            poison_food.draw(screen)
        if power_up:
            power_up.draw(screen)

        for i, seg in enumerate(snake):
            color = snake_color if i == 0 else tuple(max(0, c - 40) for c in snake_color)
            if shield_active and i == 0:
                color = (100, 220, 100)
            pygame.draw.rect(screen, color,
                             (seg[0] * cs + 1, seg[1] * cs + 1, cs - 2, cs - 2))

        s_score = font.render(f"Score: {score}", True, WHITE)
        s_level = font.render(f"Level: {level}", True, YELLOW)
        s_pb = font.render(f"Best: {personal_best}", True, (150, 150, 200))
        screen.blit(s_score, (4, 3))
        screen.blit(s_level, (sw - s_level.get_width() - 4, 3))
        screen.blit(s_pb, (4, 22))

        if pu_effect == "speed":
            rem = max(0, (pu_end_time - pygame.time.get_ticks()) // 1000 + 1)
            screen.blit(font.render(f"SPEED BOOST {rem}s", True, config.PU_COLORS["speed"]),
                        (sw // 2 - 60, 3))
        elif pu_effect == "slow":
            rem = max(0, (pu_end_time - pygame.time.get_ticks()) // 1000 + 1)
            screen.blit(font.render(f"SLOW {rem}s", True, config.PU_COLORS["slow"]),
                        (sw // 2 - 30, 3))
        if shield_active:
            screen.blit(font.render("SHIELD", True, config.PU_COLORS["shield"]),
                        (sw // 2 - 28, 3))

        if game_over:
            ov = pygame.Surface((sw, sh))
            ov.set_alpha(165)
            ov.fill(BLACK)
            screen.blit(ov, (0, 0))
            cx, cy = sw // 2, sh // 2
            f2 = pygame.font.SysFont("arial", 22)
            screen.blit(font_big.render("GAME OVER", True, (220, 50, 50)), (cx - 90, cy - 70))
            screen.blit(f2.render(f"Score: {score}   Level: {level}", True, YELLOW), (cx - 110, cy - 20))
            screen.blit(f2.render("Press ENTER to continue", True, WHITE), (cx - 120, cy + 20))
            pygame.display.update()
            waiting = True
            while waiting:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                        waiting = False
            return {"score": score, "level": level, "cancelled": False}

        actual_speed = speed
        if pu_effect == "speed":
            actual_speed = speed + 4
        elif pu_effect == "slow":
            actual_speed = max(2, speed - 3)

        pygame.display.update()
        clock.tick(actual_speed)
