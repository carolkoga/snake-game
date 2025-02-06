import pygame
from pygame.locals import *
import random
import time

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
BLOCK = 10
POS_INICIAL_X = (WINDOWS_WIDTH // BLOCK // 2) * BLOCK
POS_INICIAL_Y = (WINDOWS_HEIGHT // BLOCK // 2) * BLOCK
direcao = K_RIGHT
pontos = 0
velocidade = 10

pygame.font.init()
fonte = pygame.font.SysFont('arial', 35, False, True)

def colisao(pos1, pos2):
    return pos1 == pos2

def verifica_margens(pos):
    return not (0 <= pos[0] < WINDOWS_WIDTH and 0 <= pos[1] < WINDOWS_HEIGHT)

def game_over():
    fonte = pygame.font.SysFont('arial', 60, True, True)
    gameOver = "GAME OVER"
    text_over = fonte.render(gameOver, True, (255,255,255))
    window.blit(text_over, (110,300))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()

def gera_pos_aleatoria():
    x = random.randint(0, WINDOWS_WIDTH // BLOCK - 1) * BLOCK
    y = random.randint(0, WINDOWS_HEIGHT // BLOCK - 1) * BLOCK
    if (x,y) in obstaculo_pos:
        return gera_pos_aleatoria()
    return x, y

pygame.init()
window = pygame.display.set_mode([WINDOWS_WIDTH, WINDOWS_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption('Snake game')

cobra_pos = [
    (POS_INICIAL_X, POS_INICIAL_Y),
    (POS_INICIAL_X - BLOCK, POS_INICIAL_Y),
    (POS_INICIAL_X - 2 * BLOCK, POS_INICIAL_Y)
]
cobra_surface = pygame.Surface((BLOCK, BLOCK))
cobra_surface.fill((59, 59, 72))

obstaculo_pos = []
obstaculo_surface = pygame.Surface((BLOCK, BLOCK))
obstaculo_surface.fill((0, 0, 0))

maca_surface = pygame.Surface((BLOCK, BLOCK))
maca_surface.fill((255, 0, 0))
maca_pos = gera_pos_aleatoria()

running = True
while running:
    window.fill((68, 189, 50))

    # Renderiza a pontuação e a exibe no canto superior esquerdo
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (255, 255, 255))
    window.blit(texto, (10, 10))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            running = False
        elif evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                if evento.key == K_UP and direcao == K_DOWN:
                    continue
                elif evento.key == K_DOWN and direcao == K_UP:
                    continue
                elif evento.key == K_LEFT and direcao == K_RIGHT:
                    continue
                elif evento.key == K_RIGHT and direcao == K_LEFT:
                    continue
                direcao = evento.key

    head_x, head_y = cobra_pos[0]
    if direcao == K_RIGHT:
        head_x += BLOCK
    elif direcao == K_LEFT:
        head_x -= BLOCK
    elif direcao == K_UP:
        head_y -= BLOCK
    elif direcao == K_DOWN:
        head_y += BLOCK
    cobra_pos = [(head_x, head_y)] + cobra_pos[:-1]

    if colisao(cobra_pos[0], maca_pos):
        cobra_pos.append(cobra_pos[-1])
        maca_pos = gera_pos_aleatoria()
        obstaculo_pos.append(gera_pos_aleatoria())
        pontos += 1
        if pontos % 5 == 0:
            velocidade += 2

    for pos in obstaculo_pos:
        if colisao(cobra_pos[0], pos):
            game_over()
        window.blit(obstaculo_surface, pos)

    if any(colisao(cobra_pos[0], cobra_pos[item]) for item in range(1, len(cobra_pos))):
        game_over()
    if verifica_margens(cobra_pos[0]):
        game_over()

    window.blit(maca_surface, maca_pos)

    for pos in cobra_pos:
        window.blit(cobra_surface, pos)

    pygame.display.update()
    clock.tick(velocidade)

pygame.quit()