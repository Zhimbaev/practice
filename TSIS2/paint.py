import pygame
from datetime import datetime
import tools

pygame.init()

SCREEN_W = 960
SCREEN_H = 680
TOOLBAR_H = 100
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 180, 50)
BLUE = (50, 100, 220)
YELLOW = (240, 210, 0)
PURPLE = (150, 0, 200)
ORANGE = (255, 140, 0)
CYAN = (0, 200, 200)
PINK = (255, 100, 180)
GRAY = (160, 160, 160)
DARK_GRAY = (70, 70, 70)
PANEL_BG = (45, 45, 55)

screen  = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Paint - TSIS2")
clock = pygame.time.Clock()
fnt12 = pygame.font.SysFont("arial", 12)
fnt16 = pygame.font.SysFont("arial", 16)
fnt_txt = pygame.font.SysFont("arial", 22)

canvas = pygame.Surface((SCREEN_W, SCREEN_H - TOOLBAR_H))
canvas.fill(WHITE)

tool_names = ["pencil", "line", "rectangle", "square", "circle", "rtriangle", "etriangle", "rhombus", "fill", "text", "eraser"]
palette = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN, PINK, GRAY, DARK_GRAY]
sizes = [2, 5, 10]
size_lbls = ["S (1)", "M (2)", "L (3)"]

current_tool = "pencil"
current_color = BLACK
size_idx = 0

is_drawing = False
start_pos = None
prev_pos = None

text_mode = False
text_pos = None
text_buffer = ""

palette_rects = [pygame.Rect(10 + i * 36, 6, 30, 30) for i in range(len(palette))]

tool_rects = []
for i in range(len(tool_names)):
    col = i % 6
    row = i // 6
    tool_rects.append(pygame.Rect(10 + col * 110, 44 + row * 26, 105, 22))

size_rects = [pygame.Rect(SCREEN_W - 205 + i * 67, 6, 62, 30) for i in range(3)]
clear_rect = pygame.Rect(SCREEN_W - 120, 44, 110, 22)


def get_cp(p):
    return p[0], p[1] - TOOLBAR_H


def on_canvas(p):
    return p[1] >= TOOLBAR_H


def draw_toolbar():
    pygame.draw.rect(screen, PANEL_BG, (0, 0, SCREEN_W, TOOLBAR_H))
    pygame.draw.line(screen, GRAY, (0, TOOLBAR_H), (SCREEN_W, TOOLBAR_H), 2)

    for i, r in enumerate(palette_rects):
        pygame.draw.rect(screen, palette[i], r)
        pygame.draw.rect(screen, WHITE, r, 1)
        if palette[i] == current_color:
            pygame.draw.rect(screen, YELLOW, r, 3)

    for i, r in enumerate(tool_rects):
        c = (80, 120, 200) if tool_names[i] == current_tool else DARK_GRAY
        pygame.draw.rect(screen, c, r)
        pygame.draw.rect(screen, GRAY, r, 1)
        lbl = fnt12.render(tool_names[i], True, WHITE)
        screen.blit(lbl, (r.x + r.w // 2 - lbl.get_width() // 2, r.y + 4))

    for i, r in enumerate(size_rects):
        c = (60, 160, 60) if i == size_idx else DARK_GRAY
        pygame.draw.rect(screen, c, r)
        pygame.draw.rect(screen, GRAY, r, 1)
        lbl = fnt12.render(size_lbls[i], True, WHITE)
        screen.blit(lbl, (r.x + r.w // 2 - lbl.get_width() // 2, r.y + 8))

    pygame.draw.rect(screen, (170, 50, 50), clear_rect)
    pygame.draw.rect(screen, GRAY, clear_rect, 1)
    lbl = fnt12.render("Clear  (C)", True, WHITE)
    screen.blit(lbl, (clear_rect.x + 6, clear_rect.y + 4))

    pv = pygame.Rect(SCREEN_W - 44, 52, 32, 32)
    pygame.draw.rect(screen, current_color, pv)
    pygame.draw.rect(screen, WHITE, pv, 2)


while True:
    mp = pygame.mouse.get_pos()
    cp = get_cp(mp)
    oc = on_canvas(mp)
    bw = sizes[size_idx]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if text_mode:
                if event.key == pygame.K_RETURN:
                    s = fnt_txt.render(text_buffer, True, current_color)
                    canvas.blit(s, text_pos)
                    text_mode = False
                    text_pos = None
                    text_buffer = ""
                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_pos = None
                    text_buffer = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_buffer = text_buffer[:-1]
                else:
                    if event.unicode and event.unicode.isprintable():
                        text_buffer += event.unicode
            else:
                if event.key == pygame.K_c:
                    canvas.fill(WHITE)
                if event.key == pygame.K_1:
                    size_idx = 0
                if event.key == pygame.K_2:
                    size_idx = 1
                if event.key == pygame.K_3:
                    size_idx = 2
                mods = pygame.key.get_mods()
                if event.key == pygame.K_s and (mods & pygame.KMOD_CTRL):
                    fname = datetime.now().strftime("canvas_%Y%m%d_%H%M%S.png")
                    pygame.image.save(canvas, fname)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not text_mode:
                for i, r in enumerate(palette_rects):
                    if r.collidepoint(mp):
                        current_color = palette[i]
                for i, r in enumerate(tool_rects):
                    if r.collidepoint(mp):
                        current_tool = tool_names[i]
                for i, r in enumerate(size_rects):
                    if r.collidepoint(mp):
                        size_idx = i
                if clear_rect.collidepoint(mp):
                    canvas.fill(WHITE)
                if oc:
                    if current_tool == "fill":
                        tools.flood_fill(canvas, cp[0], cp[1], current_color)
                    elif current_tool == "text":
                        text_mode = True
                        text_pos = cp
                        text_buffer = ""
                    else:
                        is_drawing = True
                        start_pos = cp
                        prev_pos = cp

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if is_drawing and start_pos is not None and oc:
                ex, ey = cp
                ep = (ex, ey)
                if current_tool == "line":
                    tools.draw_line(canvas, current_color, start_pos, ep, bw)
                elif current_tool == "rectangle":
                    tools.draw_rectangle(canvas, current_color, start_pos, ep, bw)
                elif current_tool == "square":
                    tools.draw_square(canvas, current_color, start_pos, ep, bw)
                elif current_tool == "circle":
                    tools.draw_circle(canvas, current_color, start_pos, ep, bw)
                elif current_tool == "rtriangle":
                    tools.draw_right_triangle(canvas, current_color, start_pos, ep, bw)
                elif current_tool == "etriangle":
                    tools.draw_equilateral_triangle(canvas, current_color, start_pos, ep, bw)
                elif current_tool == "rhombus":
                    tools.draw_rhombus(canvas, current_color, start_pos, ep, bw)
            is_drawing = False
            start_pos  = None
            prev_pos   = None

    pressed = pygame.mouse.get_pressed()
    if pressed[0] and oc and not text_mode:
        if current_tool == "pencil":
            if prev_pos is not None:
                pygame.draw.line(canvas, current_color, prev_pos, cp, bw)
            prev_pos = cp
        elif current_tool == "eraser":
            pygame.draw.circle(canvas, WHITE, cp, bw * 4)
    if not pressed[0]:
        prev_pos = None

    screen.blit(canvas, (0, TOOLBAR_H))

    if is_drawing and start_pos is not None and oc:
        ex, ey = cp
        sp_s = (start_pos[0], start_pos[1] + TOOLBAR_H)
        ep_s = (ex, ey + TOOLBAR_H)
        if current_tool == "line":
            tools.draw_line(screen, current_color, sp_s, ep_s, bw)
        elif current_tool == "rectangle":
            tools.draw_rectangle(screen, current_color, sp_s, ep_s, 1)
        elif current_tool == "square":
            tools.draw_square(screen, current_color, sp_s, ep_s, 1)
        elif current_tool == "circle":
            tools.draw_circle(screen, current_color, sp_s, ep_s, 1)
        elif current_tool == "rtriangle":
            tools.draw_right_triangle(screen, current_color, sp_s, ep_s, 1)
        elif current_tool == "etriangle":
            tools.draw_equilateral_triangle(screen, current_color, sp_s, ep_s, 1)
        elif current_tool == "rhombus":
            tools.draw_rhombus(screen, current_color, sp_s, ep_s, 1)

    if text_mode and text_pos is not None:
        preview = fnt_txt.render(text_buffer + "|", True, current_color)
        screen.blit(preview, (text_pos[0], text_pos[1] + TOOLBAR_H))

    draw_toolbar()
    pygame.display.update()
    clock.tick(FPS)
