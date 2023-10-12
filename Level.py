import pygame
from Tiles import *
from Constants import TILE_SIZE
from Player import Player

class Level:
    def __init__(self,surface,level_data):
        self.surface=surface
        self.level_setup(level_data)
        self.world_shift=4
       

    def level_setup(self,level_data):
        self.tiles=pygame.sprite.Group()
        self.player=pygame.sprite.GroupSingle()

        for col_index,col_data in enumerate(level_data):
            for row_index,row_data in enumerate(col_data):
                x=row_index*TILE_SIZE
                y= col_index*TILE_SIZE
                if row_data=='X':
                  
                    tile=Tile((x,y),TILE_SIZE)
                    self.tiles.add(tile)
                if row_data=='P':
                    player=Player((x,y),TILE_SIZE)
                    self.player.add(player)



    def run(self):
        
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
     
        self.player.update()


        self.player.draw(self.surface)
      

