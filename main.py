import pygame
import sys
from Constants import *
from Tiles import *

pygame.init()

screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()

tiles_group=pygame.sprite.Group(Tile((100,100),200))




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('white')
    pygame.display.set_caption("My Gam")

    tiles_group.draw(screen)
    pygame.display.update()
    clock.tick(FRAME_RATE)



    

