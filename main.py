import pygame
from random import randint
from copy import deepcopy

RES = WIDTH, HEIGHT = 400, 400
TILE = 20
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]


def check_cell(current_field, x, y):
    count = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if current_field[i][j]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(surface, pygame.Color('gray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('gray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    for x in range(1, W-1):
        for y in range(1, H-1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('green'), (x*TILE+2, y*TILE+2, TILE-2, TILE-2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)
    pygame.display.flip()
    clock.tick(FPS)
