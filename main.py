import pygame
import random

pygame.init()
window_size = (250, 150)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Christmas Countdown")


class Snowflake:
    def __init__(self):
        self.x = random.randint(0, window_size[0])
        self.y = random.randint(-10, -5)
        self.speed = random.randint(1, 3)
        self.radius = random.randint(1, 3)
        self.drift = random.uniform(-0.5, 0.5)

    def update(self):
        self.y += self.speed
        self.x += self.drift

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)


running = True
clock = pygame.time.Clock()
snowflakes = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 135, 62))
    
    if len(snowflakes) < 100:
        snowflakes.append(Snowflake())
    
    for flake in snowflakes:
        flake.update()
        flake.draw(screen)
        if flake.y > window_size[1]:
            snowflakes.remove(flake)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
