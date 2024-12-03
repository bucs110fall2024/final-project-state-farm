import pygame
import random

pygame.init()

scr_width = 1000
scr_length = 600
scr = pygame.display.set_mode((scr_width, scr_length))
pygame.display.set_caption("Jake Edelstein CS110 Final Project - Asteroid Dodging Game")

class Ship:

    def __init__(self):
        self.x = scr_width // 2
        self.y = scr_length - 100
        self.sprite = pygame.image.load("player.png")
        self.velo = 1
        
        self.boost = 100

    def move(self):        
        keys = pygame.key.get_pressed()
        boosting = keys[pygame.KMOD_CTRL]
        if boosting:
            self.velo = 2
            self.boost -= 5

        else:
            if self.boost < 100:
                self.boost += 2
        if keys[pygame.K_LEFT] and self.x > 200:
            self.x -= self.velo
        if keys[pygame.K_RIGHT] and self.x < 800:
            self.x += self.velo
        if keys[pygame.K_UP] and self.y > 300:
            self.y -= self.velo
        if keys[pygame.K_DOWN] and self.y < 540:
            self.y += self.velo
    
    def get_pos(self):
        return [self.x, self.y]

class Asteroid:

    def __init__(self):
        asteroid_spawning_boundaries = 0, 940
        self.x = random(asteroid_spawning_boundaries(0), asteroid_spawning_boundaries(1))
        self.y = 0
        self.img = pygame.image.load("asteroid.png")
        self.boost = 100
        self.fall_speed = 1
    
    def fall(self):
        self.y += self.fall_speed

class Sound:
    
    def __init__(self):
        """
        
        
        
        """
        self.move_sound = pygame.mixer.Sound("")
        self.collision_sound = pygame.mixer.Sound("")
        self.game_over_sound = pygame.mixer.Sound("")
        self.music = pygame.mixer.Sound("")
    
    def toggle_sfx(self):
        sfx_off = self.move_sound.get_volume() == 0
        
        if sfx_off:
            self.move_sound.set_volume(1)
            self.collision_sound.set_volume(1)
            self.game_over_sound.set_volume(1)
        
        else:
            self.move_sound.set_volume(0)
            self.collision_sound.set_volume(0)
            self.game_over_sound.set_volume(0)

    def toggle_music(self):
        music_off = self.music.get_volume() == 0
        if music_off:
            self.music.set_volume(1)
        else:
            self.music.set_volume(0)
