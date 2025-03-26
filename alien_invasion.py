import sys
from settings import Settings
from ship import Ship
import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock() # Initilize game clock
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Using the numbers from class settings.py
        pygame.display.set_caption("Alien Invasion") # Top title on the top bar
        self.ship=Ship(self) #Initilize ship from ship.py

    def run_game(self):
        while True: # Running the game
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60) # Ajust the frame rate (60 frames per second)

    def _update_screen(self):#More cleared code which helper modules with "_"
        self.screen.fill(self.settings.screen_bg_colour) #Using the numbers from settings.py for the colour  
        self.ship.blitme()
        pygame.display.flip() 

    def _check_events(self): #More cleared code which helper modules with "_"
        for event in pygame.event.get(): # Get events
            if event.type == pygame.QUIT: # If we the event is quit
                sys.exit() #Exit the game using the sys package
            elif event.type == pygame.KEYDOWN: # If a key is pressed...
                if event.key == pygame.K_RIGHT: #... and that key is the right arrow on the keybord ...
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()