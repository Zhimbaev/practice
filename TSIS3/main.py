import pygame
import persistence
import racer
from ui import Button, draw_text, draw_centered

pygame.init()

SW, SH = 520, 620
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Racer - TSIS3")
clock = pygame.time.Clock()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 110)
DARK = (25,  25,  35)
RED = (220, 50,  50)
YELLOW = (240, 210, 0)
GREEN = (50,  180, 50)
BLUE = (50,  100, 220)
CYAN = (0,   200, 220)

CAR_COLORS = {
    "Blue": [50,  100, 220],
    "Red": [200, 50,  50],
    "Green": [50,  180, 50],
    "Purple": [160, 50,  200],
}


def screen_username_entry():
    font_big  = pygame.font.SysFont("arial", 32)
    font_med  = pygame.font.SysFont("arial", 20)
    font_hint = pygame.font.SysFont("arial", 15)
    name = ""
    while True:
        screen.fill(DARK)
        draw_centered(screen, "RACER", SW // 2, 100, size=52, color=YELLOW)
        draw_centered(screen, "Enter your name:", SW // 2, 200, size=24)
        box = pygame.Rect(SW // 2 - 140, 240, 280, 44)
        pygame.draw.rect(screen, (50, 50, 70), box)
        pygame.draw.rect(screen, WHITE, box, 2)
        name_surf = font_big.render(name + "|", True, WHITE)
        screen.blit(name_surf, (box.x + 10, box.y + 6))
        draw_centered(screen, "Press ENTER to continue", SW // 2, 310, size=16, color=GRAY)
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


def screen_menu(username):
    btn_play = Button(SW // 2 - 110, 230, 220, 50, "Play")
    btn_lb = Button(SW // 2 - 110, 300, 220, 50, "Leaderboard")
    btn_set = Button(SW // 2 - 110, 370, 220, 50, "Settings")
    btn_quit  = Button(SW // 2 - 110, 440, 220, 50, "Quit", color=(140, 40, 40), hover=(190, 60, 60))
    while True:
        screen.fill(DARK)
        draw_centered(screen, "RACER", SW // 2, 100, size=52, color=YELLOW)
        draw_centered(screen, f"Player: {username}", SW // 2, 170, size=20, color=GRAY)
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


def screen_gameover(result, username):
    settings = persistence.load_settings()
    persistence.add_score(username, result["score"], result["distance"], result["coins"])
    btn_retry = Button(SW // 2 - 120, 380, 220, 50, "Play Again")
    btn_menu = Button(SW // 2 - 120, 450, 220, 50, "Main Menu")
    while True:
        screen.fill(DARK)
        draw_centered(screen, "GAME OVER", SW // 2, 100, size=44, color=RED)
        draw_centered(screen, f"Score:    {result['score']}",    SW // 2, 200, size=26, color=YELLOW)
        draw_centered(screen, f"Distance: {result['distance']}m", SW // 2, 240, size=22)
        draw_centered(screen, f"Coins:    {result['coins']}",    SW // 2, 276, size=22)
        draw_centered(screen, f"Saved as: {username}", SW // 2, 320, size=18, color=GRAY)
        for btn in [btn_retry, btn_menu]:
            btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if btn_retry.clicked(event):
                return "retry"
            if btn_menu.clicked(event):
                return "menu"
        pygame.display.update()
        clock.tick(60)


def screen_leaderboard():
    scores = persistence.load_leaderboard()
    btn_back = Button(SW // 2 - 100, SH - 80, 200, 45, "Back")
    font_hd = pygame.font.SysFont("arial", 16, bold=True)
    font_row = pygame.font.SysFont("arial", 15)
    while True:
        screen.fill(DARK)
        draw_centered(screen, "TOP 10 SCORES", SW // 2, 30, size=30, color=YELLOW)
        headers = ["#", "Name", "Score", "Dist", "Coins"]
        cols    = [30, 70, 220, 310, 400]
        for i, h in enumerate(headers):
            s = font_hd.render(h, True, (180, 180, 220))
            screen.blit(s, (cols[i], 80))
        pygame.draw.line(screen, GRAY, (20, 102), (SW - 20, 102), 1)
        for ri, entry in enumerate(scores[:10]):
            y   = 112 + ri * 26
            row = [str(ri + 1), entry["name"][:12], str(entry["score"]),
                   f"{entry['distance']}m", str(entry["coins"])]
            for ci, val in enumerate(row):
                color = YELLOW if ri == 0 else WHITE
                screen.blit(font_row.render(val, True, color), (cols[ci], y))
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
    diff_options = ["easy", "normal", "hard"]
    color_names  = list(CAR_COLORS.keys())

    diff_idx = diff_options.index(settings.get("difficulty", "normal"))
    color_name = "Blue"
    for cn, cv in CAR_COLORS.items():
        if cv == settings.get("car_color", [50, 100, 220]):
            color_name = cn
    color_idx = color_names.index(color_name)
    sound_on = settings.get("sound", False)

    btn_diff_l = Button(SW // 2 - 180, 160, 40, 36, "<")
    btn_diff_r = Button(SW // 2 + 140, 160, 40, 36, ">")
    btn_color_l = Button(SW // 2 - 180, 230, 40, 36, "<")
    btn_color_r = Button(SW // 2 + 140, 230, 40, 36, ">")
    btn_sound = Button(SW // 2 - 80,  300, 160, 36, "Sound: ON" if sound_on else "Sound: OFF")
    btn_save = Button(SW // 2 - 100, 400, 200, 46, "Save & Back")

    font = pygame.font.SysFont("arial", 20)

    while True:
        screen.fill(DARK)
        draw_centered(screen, "SETTINGS", SW // 2, 60, size=34, color=YELLOW)

        draw_centered(screen, "Difficulty:", SW // 2, 130, size=18, color=GRAY)
        draw_centered(screen, diff_options[diff_idx].upper(), SW // 2, 165, size=22)

        draw_centered(screen, "Car Color:", SW // 2, 200, size=18, color=GRAY)
        cc = tuple(CAR_COLORS[color_names[color_idx]])
        pygame.draw.rect(screen, cc, (SW // 2 - 30, 228, 60, 36))
        pygame.draw.rect(screen, WHITE, (SW // 2 - 30, 228, 60, 36), 2)
        draw_centered(screen, color_names[color_idx], SW // 2, 270, size=16, color=GRAY)

        sound_lbl = "Sound: ON" if sound_on else "Sound: OFF"
        btn_sound.text = sound_lbl

        for btn in [btn_diff_l, btn_diff_r, btn_color_l, btn_color_r, btn_sound, btn_save]:
            btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if btn_diff_l.clicked(event):
                diff_idx = (diff_idx - 1) % len(diff_options)
            if btn_diff_r.clicked(event):
                diff_idx = (diff_idx + 1) % len(diff_options)
            if btn_color_l.clicked(event):
                color_idx = (color_idx - 1) % len(color_names)
            if btn_color_r.clicked(event):
                color_idx = (color_idx + 1) % len(color_names)
            if btn_sound.clicked(event):
                sound_on = not sound_on
            if btn_save.clicked(event):
                settings["difficulty"] = diff_options[diff_idx]
                settings["car_color"]  = CAR_COLORS[color_names[color_idx]]
                settings["sound"]      = sound_on
                persistence.save_settings(settings)
                return

        pygame.display.update()
        clock.tick(60)


def main():
    settings = persistence.load_settings()
    username = screen_username_entry()

    while True:
        action = screen_menu(username)
        if action == "quit":
            break
        elif action == "leaderboard":
            screen_leaderboard()
        elif action == "settings":
            screen_settings(settings)
        elif action == "play":
            while True:
                result = racer.run_game(screen, clock, settings, username)
                if result.get("cancelled"):
                    break
                action2 = screen_gameover(result, username)
                if action2 == "menu":
                    break

    pygame.quit()


if __name__ == "__main__":
    main()
