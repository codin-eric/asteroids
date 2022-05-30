import pygame
from constants import (
    SCREEN_RESOLUTION,
    FPS,
    WHITE,
    BLACK,
    LIGHT_BLUE,
    LIGHT_BLACK,
    COOL_RED,
)


class Nave:
    def __init__(self, x, y, color):
        self.pos = (x, y)
        self.size = 20
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.size, 0)


def end_game():
    pygame.quit()
    quit()


# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()  ## Syncing the FPS
screen_running = True
player = Nave(100, 100, WHITE)

# Game loop
while True:
    clock.tick(FPS)
    screen.fill(LIGHT_BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_game()

    key = pygame.key.get_pressed()

    if key[pygame.K_DOWN]:
        player.pos = (player.pos[0], player.pos[1] + 5)

    if key[pygame.K_UP]:
        player.pos = (player.pos[0], player.pos[1] - 5)

    if key[pygame.K_RIGHT]:
        player.pos = (player.pos[0] + 5, player.pos[1])

    if key[pygame.K_LEFT]:
        player.pos = (player.pos[0] - 5, player.pos[1])

    # Draw
    player.draw()
    pygame.display.update()
