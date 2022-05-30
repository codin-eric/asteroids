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
        self.speed = 5

    def move(self, dir):
        # Final position
        self.pos = (
            self.pos[0] + dir[0] * self.speed,
            self.pos[1] + dir[1] * self.speed,
        )

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

    player_dir = (0, 0)
    if key[pygame.K_DOWN]:
        player_dir = (player_dir[0], player_dir[1] + 1)

    if key[pygame.K_UP]:
        player_dir = (player_dir[0], player_dir[1] - 1)

    if key[pygame.K_RIGHT]:
        player_dir = (player_dir[0] + 1, player_dir[1])

    if key[pygame.K_LEFT]:
        player_dir = (player_dir[0] - 1, player_dir[1])

    # Move
    player.move(player_dir)

    # Draw
    player.draw()
    pygame.display.update()
