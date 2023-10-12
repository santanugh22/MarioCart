import pygame
import sys
from Constants import *
from Tiles import *
from Level import *

pygame.init()

screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()

level=Level(surface=screen,level_data=level_maps)











while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption("My Game")
    level.run()


    pygame.display.update()
    clock.tick(FRAME_RATE)



    

