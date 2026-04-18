import pygame

class Ball:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.radius = 25
        self.speed = 20

    def move(self, key):
        if key == pygame.K_UP:
            self.y -= self.speed
        if key == pygame.K_DOWN:
            self.y += self.speed
        if key == pygame.K_LEFT:
            self.x -= self.speed
        if key == pygame.K_RIGHT:
            self.x += self.speed

        # границы
        if self.x < self.radius:
            self.x = self.radius
        if self.x > 400 - self.radius:
            self.x = 400 - self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > 400 - self.radius:
            self.y = 400 - self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)