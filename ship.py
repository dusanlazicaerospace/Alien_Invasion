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
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
