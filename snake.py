import pygame
from pygame.locals import *

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600

pygame.init()
window = pygame.display.set_mode([WINDOWS_WIDTH, WINDOWS_HEIGHT])

while True:
    window.fill((68,189,50))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()
