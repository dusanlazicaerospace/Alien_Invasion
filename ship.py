import pygame
#Players ship 
class Ship:
    def __init__(self,ai_game):
        #Initilise the ship and get to its possition
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #Load the ship image and get its position
        self.image=pygame.image.load('images/main_ship.bmp')
        self.rect=self.image.get_rect()
        
        #Start each new ship on the bottom middle of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        #Stroe a float for the ships exact horizontal position 
        self.x=float(self.rect.x)

        # Movement flag; start with a ship that is not moving
        self.moving_right=False
        self.moving_left= False

    def update(self):# Update the ships position based on the movment flag 
        if self.moving_right:
            self.x+= self.settings.ship_speed
        if self.moving_left:
            self.x-= self.settings.ship_speed
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
