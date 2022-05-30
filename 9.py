import pygame
import numpy as np
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
        self.pos = np.array([x, y])
        self.size = 20
        self.color = color
        self.speed = np.array([0, 0])
        self.acc = 0.5
        self.top_speed = 5

    def move(self, dir):
        abs_speed = np.sum(np.absolute(self.speed))
        abs_dir = np.sum(np.absolute(dir))

        speed_final = self.speed + dir * self.acc

        self.pos = self.pos + (self.speed + speed_final) / 2
        self.speed = speed_final

        # Limites de pantalla.
        # En X
        if self.pos[0] < self.size:
            self.pos[0] = self.size
            self.speed[0] = 0
        elif self.pos[0] > SCREEN_RESOLUTION[0] - self.size:
            self.pos[0] = SCREEN_RESOLUTION[0] - self.size
            self.speed[0] = 0
        # En Y
        if self.pos[1] < self.size:
            self.pos[1] = self.size
            self.speed[1] = 0
        elif self.pos[1] > SCREEN_RESOLUTION[1] - self.size:
            self.pos[1] = SCREEN_RESOLUTION[1] - self.size
            self.speed[1] = 0

        # Desaceleracion
        if abs_speed != 0 and abs_dir == 0:
            self.speed = self.speed - self.speed / 10
            if abs_speed < 0.4:
                self.speed = [0, 0]

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos.astype(int), self.size, 0)


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

    player_dir = np.array([0, 0])
    if key[pygame.K_DOWN]:
        player_dir = player_dir + np.array([0, 1])

    if key[pygame.K_UP]:
        player_dir = player_dir + np.array([0, -1])

    if key[pygame.K_RIGHT]:
        player_dir = player_dir + np.array([1, 0])

    if key[pygame.K_LEFT]:
        player_dir = player_dir + np.array([-1, 0])

    # Move
    player.move(player_dir)

    # Draw
    player.draw()
    pygame.display.update()
