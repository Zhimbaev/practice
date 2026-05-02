import pygame
import math
from collections import deque


def draw_line(surface, color, start, end, width):
    pygame.draw.line(surface, color, start, end, width)


def draw_rectangle(surface, color, start, end, width):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])
    if w > 1 and h > 1:
        pygame.draw.rect(surface, color, (x, y, w, h), width)


def draw_square(surface, color, start, end, width):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    side = min(abs(dx), abs(dy))
    sx = 1 if dx >= 0 else -1
    sy = 1 if dy >= 0 else -1
    ex = start[0] + sx * side
    ey = start[1] + sy * side
    x = min(start[0], ex)
    y = min(start[1], ey)
    if side > 1:
        pygame.draw.rect(surface, color, (x, y, side, side), width)


def draw_circle(surface, color, start, end, width):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    radius = int((dx ** 2 + dy ** 2) ** 0.5)
    if radius > 2:
        pygame.draw.circle(surface, color, start, radius, width)


def draw_right_triangle(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end[0], y1
    x3, y3 = x1, end[1]
    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3)], width)


def draw_equilateral_triangle(surface, color, start, end, width):
    x1, y1 = start
    x2 = end[0]
    base_w = x2 - x1
    height = math.sqrt(3) / 2 * abs(base_w)
    apex_x = (x1 + x2) // 2
    apex_y = int(y1 - height)
    if abs(base_w) > 2:
        pygame.draw.polygon(surface, color, [(x1, y1), (x2, y1), (apex_x, apex_y)], width)


def draw_rhombus(surface, color, start, end, width):
    xl = min(start[0], end[0])
    xr = max(start[0], end[0])
    yt = min(start[1], end[1])
    yb = max(start[1], end[1])
    cx = (xl + xr) // 2
    cy = (yt + yb) // 2
    points = [(cx, yt), (xr, cy), (cx, yb), (xl, cy)]
    if (xr - xl) > 2 and (yb - yt) > 2:
        pygame.draw.polygon(surface, color, points, width)


def flood_fill(surface, start_x, start_y, fill_color):
    w = surface.get_width()
    h = surface.get_height()
    if start_x < 0 or start_x >= w or start_y < 0 or start_y >= h:
        return

    target = surface.get_at((start_x, start_y))
    tr, tg, tb = target.r, target.g, target.b
    fr, fg, fb = fill_color[0], fill_color[1], fill_color[2]

    if (tr, tg, tb) == (fr, fg, fb):
        return

    surface.lock()

    queue = deque()
    queue.append((start_x, start_y))
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        cx, cy = queue.popleft()
        c = surface.get_at((cx, cy))
        if c.r != tr or c.g != tg or c.b != tb:
            continue
        surface.set_at((cx, cy), fill_color)
        for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    surface.unlock()
