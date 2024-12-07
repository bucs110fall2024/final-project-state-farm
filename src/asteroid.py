import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid.png").convert_alpha()
        self.hitbox = pygame.mask.from_surface(self.image)
        self.rect = self.hitbox.get_rect(midtop = pos)
        # self.rect = self.image.get_rect(midtop = pos)
        self.fall_speed = 3
        self.death_height = 800
        # self.hitbox = self.rect
        # self.hitbox.center = self.rect.center

    def set_fall_speed(self, new_fall_speed):
        self.fall_speed = new_fall_speed
    
    def fall(self):
        # if self.rect.y >= self.death_height:
        #     self.rect.x = random.randint(0, 1000)
        #     self.rect.y = 0

        self.rect.y += self.fall_speed
        # self.hitbox.center = self.rect.center

    def update(self):
        self.fall()
        if self.rect.y > 800:
            self.kill()