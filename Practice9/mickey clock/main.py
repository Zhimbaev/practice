import pygame
from clock import get_time, calculate_angles

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

hand = pygame.image.load("/Users/zamirzimbaev/Desktop/practice/Practice9/mickey clock/images/mickey_hand.png")
hand = pygame.transform.scale(hand, (200, 200))

center = (300, 300)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    minutes, seconds = get_time()
    min_angle, sec_angle = calculate_angles(minutes, seconds)

    min_hand = pygame.transform.rotate(hand, -min_angle)
    sec_hand = pygame.transform.rotate(hand, -sec_angle)

    screen.blit(min_hand, (200, 200))
    screen.blit(sec_hand, (200, 200))

    pygame.display.flip()
    clock.tick(1)

pygame.quit()