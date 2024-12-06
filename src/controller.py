import pygame
from game import Game


class Controller:
    def __init__(self):
        pygame.init()
        self.run = True
        screen_w = 1000
        screen_h = 800
        screen = pygame.display.set_mode((screen_w, screen_h))
        display = pygame.Surface((screen_w, screen_h))
        self.game = Game()
    
    
    
    def mainloop(self):
        while self.run == True:
            if self.state =


