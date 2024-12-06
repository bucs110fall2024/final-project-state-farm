import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid.png").convert_alpha()
        self.rect = self.image.get_rect(midtop = pos)
        self.fall_speed = 4
        self.max_num = 5
        self.hitbox = self.rect
        self.hitbox.center = self.rect.center

    def set_fall_speed(self, new_fall_speed):
        self.fall_speed = new_fall_speed
    
    def set_max_num(self, new_max_num):
        self.max_num = new_max_num
    
    def fall(self):
        self.rect.y += self.fall_speed
        self.hitbox.center = self.rect.center

    def die(self):
        if self.rect.y >= 800:
            self.kill()

    def update(self):
        self.fall()
        self.die()