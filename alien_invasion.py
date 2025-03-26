import sys
from settings import Settings
import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock() # Initilize game clock
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Using the numbers from class settings.py
        pygame.display.set_caption("Alien Invasion") # Top title on the top bar
        

    def run_game(self):
        while True: # Running the game
            for event in pygame.event.get(): # Get events
                if event.type == pygame.QUIT: # If we the event is quit
                    sys.exit() #Exit the game using the sys package
            self.screen.fill(self.settings.screen_bg_colour) #Using the numbers from settings.py for the colour  
            pygame.display.flip() 
            self.clock.tick(60) # Ajust the frame rate (60 frames per second)

if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()