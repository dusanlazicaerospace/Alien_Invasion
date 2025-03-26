import sys

import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1600,800)) # Resolution of the main window 
        pygame.display.set_caption("Alien Invasion") # Top title on the top bar
    def run_game(self):
        while True: # Running the game
            for event in pygame.event.get(): # Get events
                if event.type == pygame.QUIT: # If we the event is quit
                    sys.exit() #Exit the game using the sys package 
        pygame.display.flip()

if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()