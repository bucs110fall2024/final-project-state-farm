import pygame
import random

class Ship:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("ship.png").convert()
        self.velo = 5
        
        self.boost = 100

    def move(self):        
        keys = pygame.key.get_pressed()
        boosting = keys[pygame.KMOD_CTRL]
        if boosting:
            self.velo = 10
            self.boost -= 5

        else:
            self.velo = 5
            if self.boost < 99:
                self.boost += 2
            if self.boost == 99:
                self.boost += 1
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
        asteroid_spawning_x_boundary = 940
        self.x = random(range(asteroid_spawning_x_boundary))
        self.y = 0
        self.img = pygame.image.load("asteroid.png").convert()
        self.fall_speed = 5
    
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

class GameState:
    def __init__(self):
        self.score = 0
        self.time = 0
        self.highscore = 0
        self.state = "menu"
