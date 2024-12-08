import pygame
import random

INIT_FALL_SPEED = 6
DEATH_HEIGHT = 800
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid.png").convert_alpha()
        self.hitbox = pygame.mask.from_surface(self.image)
        self.rect = self.hitbox.get_rect(midtop = pos)
        self.fall_speed = INIT_FALL_SPEED
        self.death_height = DEATH_HEIGHT

    def set_fall_speed(self, new_fall_speed):
        self.fall_speed = new_fall_speed
    
    def fall(self):
        self.rect.y += self.fall_speed

    def update(self):
        self.fall()
        if self.rect.y > DEATH_HEIGHT:
            self.kill()