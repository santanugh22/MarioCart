import pygame
import sys
from Constants import *

pygame.init()

screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((20,80,200,0.3))
    pygame.display.set_caption("My Game")
    pygame.display.update()
    clock.tick(FRAME_RATE)
    

