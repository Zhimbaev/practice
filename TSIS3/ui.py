import pygame


class Button:
    def __init__(self, x, y, w, h, text, color=(65, 65, 90), hover=(95, 120, 190)):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover = hover
        self.font = pygame.font.SysFont("arial", 20)

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        c = self.hover if self.rect.collidepoint(mouse) else self.color
        pygame.draw.rect(surface, c, self.rect, border_radius=7)
        pygame.draw.rect(surface, (190, 190, 210), self.rect, 2, border_radius=7)
        txt = self.font.render(self.text, True, (255, 255, 255))
        surface.blit(txt, (
            self.rect.x + self.rect.w // 2 - txt.get_width()  // 2,
            self.rect.y + self.rect.h // 2 - txt.get_height() // 2
        ))

    def clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.rect.collidepoint(event.pos))


def draw_text(surface, text, x, y, size=22, color=(255, 255, 255)):
    font = pygame.font.SysFont("arial", size)
    surface.blit(font.render(text, True, color), (x, y))


def draw_centered(surface, text, cx, y, size=24, color=(255, 255, 255)):
    font = pygame.font.SysFont("arial", size)
    s = font.render(text, True, color)
    surface.blit(s, (cx - s.get_width() // 2, y))
