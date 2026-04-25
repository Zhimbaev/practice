import pygame
import math

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650
TOOLBAR_H = 90

FPS = 60

WHITE      = (255, 255, 255)
BLACK      = (0,   0,   0)
RED        = (220, 50,  50)
GREEN      = (50,  180, 50)
BLUE       = (50,  100, 220)
YELLOW     = (240, 210, 0)
PURPLE     = (150, 0,   200)
ORANGE     = (255, 140, 0)
CYAN       = (0,   200, 200)
PINK       = (255, 100, 180)
GRAY       = (160, 160, 160)
DARK_GRAY  = (70,  70,  70)
PANEL_BG   = (50,  50,  60)
LIGHT_GRAY = (200, 200, 200)

tools = [
    "pencil"
    "rectangle",
    "square",
    "circle",
    "rtriangle",
    "etriangle",
    "rhombus",
    "eraser",
]

palette = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN, PINK, GRAY, DARK_GRAY]

screen   = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint - Practice 11")
clock    = pygame.time.Clock()
font12   = pygame.font.SysFont("arial", 12)
font14   = pygame.font.SysFont("arial", 14)

canvas_width  = SCREEN_WIDTH
canvas_height = SCREEN_HEIGHT - TOOLBAR_H
canvas = pygame.Surface((canvas_width, canvas_height))
canvas.fill(WHITE)

current_tool  = "pencil"
current_color = BLACK
brush_size    = 4
eraser_size   = 15

is_drawing = False
start_pos  = None

palette_rects = []
for i in range(len(palette)):
    rect = pygame.Rect(10 + i * 36, 6, 30, 30)
    palette_rects.append(rect)

tool_rects = []
for i in range(len(tools)):
    col = i % 4
    row = i // 4
    rect = pygame.Rect(10 + col * 110, 45 + row * 22, 105, 20)
    tool_rects.append(rect)

clear_rect = pygame.Rect(SCREEN_WIDTH - 110, 6, 100, 30)



def get_canvas_pos(screen_pos):
    return screen_pos[0], screen_pos[1] - TOOLBAR_H

def is_on_canvas(screen_pos):
    return screen_pos[1] >= TOOLBAR_H

def draw_toolbar():
    pygame.draw.rect(screen, PANEL_BG, (0, 0, SCREEN_WIDTH, TOOLBAR_H))
    pygame.draw.line(screen, GRAY, (0, TOOLBAR_H), (SCREEN_WIDTH, TOOLBAR_H), 2)

    for i, rect in enumerate(palette_rects):
        pygame.draw.rect(screen, palette[i], rect)
        pygame.draw.rect(screen, WHITE, rect, 1)
        if palette[i] == current_color:
            pygame.draw.rect(screen, YELLOW, rect, 2)

    for i, rect in enumerate(tool_rects):
        btn_color = (80, 120, 200) if tools[i] == current_tool else DARK_GRAY
        pygame.draw.rect(screen, btn_color, rect)
        pygame.draw.rect(screen, GRAY, rect, 1)
        label = font12.render(tools[i], True, WHITE)
        screen.blit(label, (rect.x + rect.w // 2 - label.get_width() // 2,
                             rect.y + rect.h // 2 - label.get_height() // 2))

    pygame.draw.rect(screen, (180, 50, 50), clear_rect)
    pygame.draw.rect(screen, GRAY, clear_rect, 1)
    lbl = font14.render("Clear (C)", True, WHITE)
    screen.blit(lbl, (clear_rect.x + 5, clear_rect.y + 7))

    preview = pygame.Rect(SCREEN_WIDTH - 50, 40, 38, 38)
    pygame.draw.rect(screen, current_color, preview)
    pygame.draw.rect(screen, WHITE, preview, 2)



def draw_rectangle(surface, color, start, end, width=2):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])
    if w > 1 and h > 1:
        pygame.draw.rect(surface, color, (x, y, w, h), width)


def draw_square(surface, color, start, end, width=2):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    side = min(abs(dx), abs(dy))
    sign_x = 1 if dx >= 0 else -1
    sign_y = 1 if dy >= 0 else -1
    ex = start[0] + sign_x * side
    ey = start[1] + sign_y * side
    x = min(start[0], ex)
    y = min(start[1], ey)
    if side > 1:
        pygame.draw.rect(surface, color, (x, y, side, side), width)


def draw_right_triangle(surface, color, start, end, width=2):
    x1, y1 = start
    x2, y2 = end[0], y1
    x3, y3 = x1, end[1]
    points = [(x1, y1), (x2, y2), (x3, y3)]
    pygame.draw.polygon(surface, color, points, width)


def draw_equilateral_triangle(surface, color, start, end, width=2):
    x1, y1 = start
    x2 = end[0]
    y_base = y1
    base_w = x2 - x1

    height = math.sqrt(3) / 2 * abs(base_w)
    apex_x = (x1 + x2) // 2
    apex_y = int(y_base - height)

    points = [(x1, y_base), (x2, y_base), (apex_x, apex_y)]
    if abs(base_w) > 2:
        pygame.draw.polygon(surface, color, points, width)


def draw_rhombus(surface, color, start, end, width=2):
    x_left = min(start[0], end[0])
    x_right = max(start[0], end[0])
    y_top = min(start[1], end[1])
    y_bottom = max(start[1], end[1])

    center_x = (x_left + x_right) // 2
    center_y = (y_top  + y_bottom) // 2

    points = [
        (center_x, y_top),
        (x_right,  center_y),
        (center_x, y_bottom),
        (x_left,   center_y),
    ]

    if (x_right - x_left) > 2 and (y_bottom - y_top) > 2:
        pygame.draw.polygon(surface, color, points, width)


while True:
    mouse_pos  = pygame.mouse.get_pos()
    canvas_pos = get_canvas_pos(mouse_pos)
    on_canvas  = is_on_canvas(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(palette_rects):
                if rect.collidepoint(mouse_pos):
                    current_color = palette[i]

            for i, rect in enumerate(tool_rects):
                if rect.collidepoint(mouse_pos):
                    current_tool = tools[i]

            if clear_rect.collidepoint(mouse_pos):
                canvas.fill(WHITE)

            if on_canvas:
                is_drawing = True
                start_pos  = canvas_pos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if is_drawing and on_canvas and start_pos is not None:
                ex, ey = canvas_pos

                if current_tool == "rectangle":
                    draw_rectangle(canvas, current_color, start_pos, (ex, ey))

                elif current_tool == "square":
                    draw_square(canvas, current_color, start_pos, (ex, ey))

                elif current_tool == "circle":
                    dx = ex - start_pos[0]
                    dy = ey - start_pos[1]
                    radius = int((dx**2 + dy**2) ** 0.5)
                    if radius > 2:
                        pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                elif current_tool == "rtriangle":
                    draw_right_triangle(canvas, current_color, start_pos, (ex, ey))

                elif current_tool == "etriangle":
                    draw_equilateral_triangle(canvas, current_color, start_pos, (ex, ey))

                elif current_tool == "rhombus":
                    draw_rhombus(canvas, current_color, start_pos, (ex, ey))

            is_drawing = False
            start_pos  = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                canvas.fill(WHITE)

    pressed = pygame.mouse.get_pressed()
    if pressed[0] and on_canvas:
        if current_tool == "pencil":
            pygame.draw.circle(canvas, current_color, canvas_pos, brush_size)
        elif current_tool == "eraser":
            pygame.draw.circle(canvas, WHITE, canvas_pos, eraser_size)

    screen.blit(canvas, (0, TOOLBAR_H))

    if is_drawing and start_pos is not None and on_canvas:
        ex, ey = canvas_pos
        sp_screen = (start_pos[0], start_pos[1] + TOOLBAR_H)
        ep_screen = (ex, ey + TOOLBAR_H)

        if current_tool == "rectangle":
            draw_rectangle(screen, current_color, sp_screen, ep_screen, 1)

        elif current_tool == "square":
            draw_square(screen, current_color, sp_screen, ep_screen, 1)

        elif current_tool == "circle":
            dx = ex - start_pos[0]
            dy = ey - start_pos[1]
            radius = int((dx**2 + dy**2) ** 0.5)
            if radius > 0:
                pygame.draw.circle(screen, current_color,
                                   (start_pos[0], start_pos[1] + TOOLBAR_H), radius, 1)

        elif current_tool == "rtriangle":
            draw_right_triangle(screen, current_color, sp_screen, ep_screen, 1)

        elif current_tool == "etriangle":
            draw_equilateral_triangle(screen, current_color, sp_screen, ep_screen, 1)

        elif current_tool == "rhombus":
            draw_rhombus(screen, current_color, sp_screen, ep_screen, 1)

    draw_toolbar()

    pygame.display.update()
    clock.tick(FPS)