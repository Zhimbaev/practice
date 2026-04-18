import pygame
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball = Ball()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            ball.move(event.key)

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()