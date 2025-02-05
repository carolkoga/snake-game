import pygame
from pygame.locals import *
import random

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
BLOCK = 10
POS_INICIAL_X = (WINDOWS_WIDTH // BLOCK // 2) * BLOCK
POS_INICIAL_Y = (WINDOWS_HEIGHT // BLOCK // 2) * BLOCK
direcao = K_RIGHT

def colisao(pos1,pos2):
    return pos1 == pos2

def verifica_margens(pos):
    if 0 <= pos[0] < WINDOWS_WIDTH and 0 <= pos[1] < WINDOWS_HEIGHT:
        return False
    else:
        return True

def game_over():
    pygame.quit()
    quit()

def gera_pos_aleatoria():
    x = random.randint(0, WINDOWS_WIDTH // BLOCK - 1) * BLOCK
    y = random.randint(0, WINDOWS_HEIGHT // BLOCK - 1) * BLOCK
    return x, y

pygame.init()
window = pygame.display.set_mode([WINDOWS_WIDTH, WINDOWS_HEIGHT])
clock = pygame.time.Clock()

# Inicializa a cobra centralizada e alinhada ao grid
cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y), (POS_INICIAL_X + BLOCK, POS_INICIAL_Y), (POS_INICIAL_X + 2 * BLOCK, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK, BLOCK))
cobra_surface.fill((59, 59, 72))

maca_surface = pygame.Surface((BLOCK, BLOCK))
maca_surface.fill((255, 0, 0))
maca_pos = gera_pos_aleatoria()

running = True
while running:
    window.fill((68, 189, 50))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            running = False
        elif evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao = evento.key

    window.blit(maca_surface, maca_pos)

    if (colisao(cobra_pos[0], maca_pos)):
        cobra_pos.append((-10,-10))
        maca_pos = gera_pos_aleatoria()

    for pos in cobra_pos:
        window.blit(cobra_surface, pos)

    for item in range(len(cobra_pos)-1,0,-1):
        cobra_pos[item] = cobra_pos[item-1]

    if verifica_margens(cobra_pos[0]):
        game_over()

    if direcao == K_RIGHT:
        nova_x = cobra_pos[0][0] + BLOCK
        nova_y = cobra_pos[0][1]
        cobra_pos[0] = (nova_x, nova_y)

    if direcao == K_LEFT:
        nova_x = cobra_pos[0][0] - BLOCK
        nova_y = cobra_pos[0][1]
        cobra_pos[0] = (nova_x, nova_y)

    if direcao == K_UP:
        nova_x = cobra_pos[0][0]
        nova_y = cobra_pos[0][1] - BLOCK
        cobra_pos[0] = (nova_x, nova_y)

    if direcao == K_DOWN:
        nova_x = cobra_pos[0][0]
        nova_y = cobra_pos[0][1] + BLOCK
        cobra_pos[0] = (nova_x, nova_y)

    pygame.display.update()
    clock.tick(10)

pygame.quit()