import pygame
import random
from game import Game

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, pos, fall_speed = 3, max_num = 4):
        super().__init__()

        self.image = pygame.image.load("assets/asteroid.png").convert_alpha()
        self.rect = self.image.get_rect(midtop = pos)
        
        self.fall_speed = fall_speed
        self.max_num = max_num
    
    def set_fall_speed(self, new_fall_speed):
        self.fall_speed = new_fall_speed
    
    def set_max_num(self, new_max_num):
        self.max_num = new_max_num

    def fall(self):
        self.rect.y += self.fall_speed

    def kill(self):
        if self.rect.y >= 800:
            self.kill()

    def update(self):
        self.fall()
        self.kill()

