import pygame
import json
import os
import db
import game
import config

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_W, config.SCREEN_H))
pygame.display.set_caption("Snake - TSIS4")
clock  = pygame.time.Clock()

SW = config.SCREEN_W
SH = config.SCREEN_H

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GRAY = (110, 110, 120)
DARK = (18,  18,  28)
RED = (220, 50,  50)
YELLOW = (240, 210, 0)
GREEN = (50,  200, 50)

SETTINGS_FILE = "/Users/zamirzimbaev/Desktop/practice/TSIS4/settings.json"


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return config.DEFAULT_SETTINGS.copy()


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)


class Button:
    def __init__(self, x, y, w, h, text, color=(55, 55, 80), hover=(90, 110, 175)):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover = hover
        self.font = pygame.font.SysFont("arial", 20)

    def draw(self, surface):
        c = self.hover if self.rect.collidepoint(pygame.mouse.get_pos()) else self.color
        pygame.draw.rect(surface, c, self.rect, border_radius=7)
        pygame.draw.rect(surface, (180, 180, 210), self.rect, 2, border_radius=7)
        t = self.font.render(self.text, True, WHITE)
        surface.blit(t, (self.rect.x + self.rect.w // 2 - t.get_width()  // 2,
                         self.rect.y + self.rect.h // 2 - t.get_height() // 2))

    def clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.rect.collidepoint(event.pos))


def draw_c(surface, text, cx, y, size=24, color=WHITE):
    f = pygame.font.SysFont("arial", size)
    s = f.render(text, True, color)
    surface.blit(s, (cx - s.get_width() // 2, y))


def screen_username_entry():
    font_big = pygame.font.SysFont("arial", 30)
    name = ""
    while True:
        screen.fill(DARK)
        draw_c(screen, "SNAKE", SW // 2, 80,  size=52, color=GREEN)
        draw_c(screen, "Enter your name:", SW // 2, 190, size=22)
        box = pygame.Rect(SW // 2 - 130, 228, 260, 44)
        pygame.draw.rect(screen, (40, 50, 65), box)
        pygame.draw.rect(screen, WHITE, box, 2)
        ns = font_big.render(name + "|", True, WHITE)
        screen.blit(ns, (box.x + 8, box.y + 6))
        draw_c(screen, "Press ENTER to start", SW // 2, 290, size=15, color=GRAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    return name.strip()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if event.unicode.isprintable() and len(name) < 16:
                        name += event.unicode
        pygame.display.update()
        clock.tick(60)


def screen_menu(username, personal_best):
    btn_play = Button(SW // 2 - 100, 220, 200, 48, "Play")
    btn_lb = Button(SW // 2 - 100, 285, 200, 48, "Leaderboard")
    btn_set = Button(SW // 2 - 100, 350, 200, 48, "Settings")
    btn_quit = Button(SW // 2 - 100, 415, 200, 48, "Quit", color=(130, 40, 40), hover=(180, 60, 60))
    while True:
        screen.fill(DARK)
        draw_c(screen, "SNAKE", SW // 2, 70,  size=52, color=GREEN)
        draw_c(screen, f"Player: {username}", SW // 2, 150, size=18, color=GRAY)
        draw_c(screen, f"Best: {personal_best}", SW // 2, 175, size=18, color=YELLOW)
        for btn in [btn_play, btn_lb, btn_set, btn_quit]:
            btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if btn_play.clicked(event):
                return "play"
            if btn_lb.clicked(event):
                return "leaderboard"
            if btn_set.clicked(event):
                return "settings"
            if btn_quit.clicked(event):
                return "quit"
        pygame.display.update()
        clock.tick(60)


def screen_gameover(result, username, player_id, personal_best):
    if not result.get("cancelled"):
        db.save_session(player_id, result["score"], result["level"])
        new_pb = db.get_personal_best(username)
    else:
        new_pb = personal_best

    btn_retry = Button(SW // 2 - 110, 360, 210, 48, "Play Again")
    btn_menu = Button(SW // 2 - 110, 425, 210, 48, "Main Menu")
    font_med = pygame.font.SysFont("arial", 22)
    while True:
        screen.fill(DARK)
        draw_c(screen, "GAME OVER", SW // 2, 90,  size=44, color=RED)
        draw_c(screen, f"Score: {result['score']}", SW // 2, 190, size=28, color=YELLOW)
        draw_c(screen, f"Level: {result['level']}", SW // 2, 232, size=22)
        draw_c(screen, f"Personal Best: {new_pb}", SW // 2, 272, size=18, color=(150, 180, 230))
        draw_c(screen, f"Saved to DB  ✓", SW // 2, 306, size=16, color=GRAY)
        for btn in [btn_retry, btn_menu]:
            btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if btn_retry.clicked(event):
                return "retry", new_pb
            if btn_menu.clicked(event):
                return "menu", new_pb
        pygame.display.update()
        clock.tick(60)


def screen_leaderboard():
    rows = db.get_leaderboard()
    btn_back = Button(SW // 2 - 90, SH - 72, 180, 42, "Back")
    fnt_hd = pygame.font.SysFont("arial", 15, bold=True)
    fnt_row = pygame.font.SysFont("arial", 14)
    cols = [24, 55, 190, 280, 360, 440]
    headers = ["#", "Name", "Score", "Level", "Date"]
    while True:
        screen.fill(DARK)
        draw_c(screen, "LEADERBOARD", SW // 2, 24, size=30, color=YELLOW)
        for i, h in enumerate(headers):
            screen.blit(fnt_hd.render(h, True, (180, 180, 230)), (cols[i], 70))
        pygame.draw.line(screen, GRAY, (16, 92), (SW - 16, 92), 1)
        for ri, row in enumerate(rows):
            y  = 100 + ri * 24
            dt = str(row[3])[:10] if row[3] else "-"
            vals = [str(ri + 1), str(row[0])[:14], str(row[1]), str(row[2]), dt]
            c = YELLOW if ri == 0 else WHITE
            for ci, v in enumerate(vals):
                screen.blit(fnt_row.render(v, True, c), (cols[ci], y))
        btn_back.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if btn_back.clicked(event):
                return
        pygame.display.update()
        clock.tick(60)


def screen_settings(settings):
    color_opts = {
        "Green": [60,  200, 60],
        "Blue": [50,  100, 220],
        "Yellow": [240, 200, 0],
        "Red": [220, 70,  70],
        "Cyan": [0,   200, 210],
    }
    color_names = list(color_opts.keys())

    cur_color = settings.get("snake_color", [60, 200, 60])
    color_idx = 0
    for i, cn in enumerate(color_names):
        if color_opts[cn] == cur_color:
            color_idx = i

    grid_on  = settings.get("grid_overlay", True)
    sound_on = settings.get("sound", False)

    btn_cl = Button(SW // 2 - 180, 160, 40, 36, "<")
    btn_cr = Button(SW // 2 + 140, 160, 40, 36, ">")
    btn_grid = Button(SW // 2 - 90, 240, 180, 36, "")
    btn_sound = Button(SW // 2 - 90, 295, 180, 36, "")
    btn_save = Button(SW // 2 - 100, 390, 200, 46, "Save & Back")

    while True:
        screen.fill(DARK)
        draw_c(screen, "SETTINGS", SW // 2, 60, size=34, color=YELLOW)

        draw_c(screen, "Snake Color:", SW // 2, 128, size=18, color=GRAY)
        cc = tuple(color_opts[color_names[color_idx]])
        pygame.draw.rect(screen, cc, (SW // 2 - 28, 158, 56, 36))
        pygame.draw.rect(screen, WHITE, (SW // 2 - 28, 158, 56, 36), 2)
        draw_c(screen, color_names[color_idx], SW // 2, 200, size=16, color=GRAY)

        btn_grid.text  = f"Grid: {'ON' if grid_on else 'OFF'}"
        btn_sound.text = f"Sound: {'ON' if sound_on else 'OFF'}"

        for btn in [btn_cl, btn_cr, btn_grid, btn_sound, btn_save]:
            btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if btn_cl.clicked(event):
                color_idx = (color_idx - 1) % len(color_names)
            if btn_cr.clicked(event):
                color_idx = (color_idx + 1) % len(color_names)
            if btn_grid.clicked(event):
                grid_on = not grid_on
            if btn_sound.clicked(event):
                sound_on = not sound_on
            if btn_save.clicked(event):
                settings["snake_color"]  = color_opts[color_names[color_idx]]
                settings["grid_overlay"] = grid_on
                settings["sound"]        = sound_on
                save_settings(settings)
                return

        pygame.display.update()
        clock.tick(60)


def main():
    try:
        db.ensure_database()
        db.create_tables()
        db_ok = True
    except Exception as e:
        print(f"DB connection failed: {e}")
        db_ok = False
    try:
        db.create_tables()
        db_ok = True
    except Exception as e:
        print(f"DB connection failed: {e}")
        db_ok = False

    settings = load_settings()
    username = screen_username_entry()

    if db_ok:
        player_id = db.get_or_create_player(username)
        personal_best = db.get_personal_best(username)
    else:
        player_id = None
        personal_best = 0

    while True:
        action = screen_menu(username, personal_best)
        if action == "quit":
            break
        elif action == "leaderboard":
            if db_ok:
                screen_leaderboard()
        elif action == "settings":
            screen_settings(settings)
        elif action == "play":
            while True:
                result = game.run_game(screen, clock, settings, username, personal_best)
                if result.get("cancelled"):
                    break
                if db_ok and player_id:
                    go_action, personal_best = screen_gameover(result, username, player_id, personal_best)
                else:
                    go_action, personal_best = screen_gameover(result, username, None, personal_best)
                if go_action == "menu":
                    break

    pygame.quit()


if __name__ == "__main__":
    main()
