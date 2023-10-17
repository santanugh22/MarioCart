import pygame




class Player(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image=pygame.Surface((size,size))
        self.image.fill('red')
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=pygame.math.Vector2(0,0)



    def get_input(self):
      
        keys=pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x+=4
        elif keys[pygame.K_LEFT]:
            self.direction.x-=4

        else:
            self.direction.x=0


        self.rect.x=self.direction.x

        def gravity(self):
            pass



 

    def update(self):
        self.get_input()
        
        





       


        