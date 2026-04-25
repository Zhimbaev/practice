import pygame

pygame.init()

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 620
TOOLBAR_H     = 90

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (220, 50,  50)
GREEN = (50,  180, 50)
BLUE = (50,  100, 220)
YELLOW = (240, 210, 0)
PURPLE = (150, 0,   200)
ORANGE = (255, 140, 0)
CYAN = (0,   200, 200)
PINK = (255, 100, 180)
GRAY = (160, 160, 160)
DARK_GRAY = (70,  70,  70)
PANEL_BG = (50,  50,  60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint - Practice 8")
clock  = pygame.time.Clock()
font   = pygame.font.SysFont("arial", 14)
font16 = pygame.font.SysFont("arial", 16)

canvas_width  = SCREEN_WIDTH
canvas_height = SCREEN_HEIGHT - TOOLBAR_H
canvas = pygame.Surface((canvas_width, canvas_height))
canvas.fill(WHITE)

tools = ["pencil", "rectangle", "circle", "eraser"]

palette = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN, PINK, GRAY, DARK_GRAY]

current_tool  = "pencil"
current_color = BLACK
brush_size    = 4
eraser_size   = 15

is_drawing  = False
start_pos   = None


palette_rects = []
for i in range(len(palette)):
    rect = pygame.Rect(10 + i * 38, 8, 32, 32)
    palette_rects.append(rect)

tool_rects = []
for i in range(len(tools)):
    rect = pygame.Rect(10 + i * 110, 50, 100, 30)
    tool_rects.append(rect)

clear_rect = pygame.Rect(SCREEN_WIDTH - 110, 50, 100, 30)



def draw_toolbar():
    pygame.draw.rect(screen, PANEL_BG, (0, 0, SCREEN_WIDTH, TOOLBAR_H))
    pygame.draw.line(screen, GRAY, (0, TOOLBAR_H), (SCREEN_WIDTH, TOOLBAR_H), 2)

    for i, rect in enumerate(palette_rects):
        pygame.draw.rect(screen, palette[i], rect)
        pygame.draw.rect(screen, WHITE, rect, 1)

        if palette[i] == current_color:
            pygame.draw.rect(screen, YELLOW, rect, 3)

    for i, rect in enumerate(tool_rects):
        btn_color = (100, 140, 200) if tools[i] == current_tool else DARK_GRAY
        pygame.draw.rect(screen, btn_color, rect)
        pygame.draw.rect(screen, GRAY, rect, 1)
        label = font16.render(tools[i], True, WHITE)
        screen.blit(label, (rect.x + rect.w // 2 - label.get_width() // 2,
                             rect.y + rect.h // 2 - label.get_height() // 2))

    pygame.draw.rect(screen, (180, 50, 50), clear_rect)
    pygame.draw.rect(screen, GRAY, clear_rect, 1)
    clr_label = font16.render("Clear (C)", True, WHITE)
    screen.blit(clr_label, (clear_rect.x + 5,
                             clear_rect.y + clear_rect.h // 2 - clr_label.get_height() // 2))

    preview_rect = pygame.Rect(SCREEN_WIDTH - 50, 5, 38, 38)
    pygame.draw.rect(screen, current_color, preview_rect)
    pygame.draw.rect(screen, WHITE, preview_rect, 2)
    label = font.render("color", True, GRAY)
    screen.blit(label, (SCREEN_WIDTH - 48, 46))


def get_canvas_pos(screen_pos):
    cx = screen_pos[0]
    cy = screen_pos[1] - TOOLBAR_H
    return cx, cy

def is_on_canvas(screen_pos):
    return screen_pos[1] >= TOOLBAR_H


while True:
    mouse_pos = pygame.mouse.get_pos()
    canvas_pos = get_canvas_pos(mouse_pos)
    on_canvas = is_on_canvas(mouse_pos)

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
                if current_tool == "rectangle":
                    end_x, end_y = canvas_pos
                    x = min(start_pos[0], end_x)
                    y = min(start_pos[1], end_y)
                    w = abs(end_x - start_pos[0])
                    h = abs(end_y - start_pos[1])
                    if w > 2 and h > 2:
                        pygame.draw.rect(canvas, current_color, (x, y, w, h), 2)

                if current_tool == "circle":
                    end_x, end_y = canvas_pos
                    dx = end_x - start_pos[0]
                    dy = end_y - start_pos[1]
                    radius = int((dx**2 + dy**2) ** 0.5)
                    if radius > 2:
                        pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

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

        if current_tool == "rectangle":
            x = min(start_pos[0], ex)
            y = min(start_pos[1], ey) + TOOLBAR_H 
            w = abs(ex - start_pos[0])
            h = abs(ey - start_pos[1])
            if w > 0 and h > 0:
                pygame.draw.rect(screen, current_color, (x, y, w, h), 1)

        if current_tool == "circle":
            dx = ex - start_pos[0]
            dy = ey - start_pos[1]
            radius = int((dx**2 + dy**2) ** 0.5)
            cx_draw = start_pos[0]
            cy_draw = start_pos[1] + TOOLBAR_H
            if radius > 0:
                pygame.draw.circle(screen, current_color, (cx_draw, cy_draw), radius, 1)

    draw_toolbar()

    pygame.display.update()
    clock.tick(FPS)