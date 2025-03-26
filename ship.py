import pygame
#Players ship 
class Ship:
    def __init__(self,ai_game):
        #Initilise the ship and get to its possition
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #Load the ship image and get its position
        self.image=pygame.image.load('images/main_ship.bmp')
        self.rect=self.image.get_rect()
        
        #Start each new ship on the bottom middle of the screen
        self.rect.midbottom=self.screen_rect.midbottom
    
        # Movement flag; start with a ship that is not moving
        self.moving_right=False
        self.moving_left= False

    def update(self):# Update the ships position based on the movment flag 
        if self.moving_right:
            self.rect.x+= 1 
        if self.moving_left:
            self.rect.x-= 1
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
