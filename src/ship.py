import pygame
from src.sound import Sound, SHIP_CHANNEL

SOUNDS = Sound()
KEYS = pygame.key.get_pressed()

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        """
        Initializes the ship.
        args: (tuple) pos = spawn position
        return: None
        """
        super().__init__()
        self.image = pygame.image.load('assets/ship.png').convert_alpha()
        self.hitbox = pygame.mask.from_surface(self.image)
        self.rect = self.hitbox.get_rect(center = pos)
        self.velo = 8
        self.move_sound = pygame.mixer.Sound("assets/move_sound.mp3")
        self.is_moving = False
        # self.boosting = False

    def move(self):
        """
        Moves the ship's position based on keys pressed.
        args: None
        return: None
        """
        keys = pygame.key.get_pressed()
        
        is_moving = (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] \
                     or keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s])
        
        if is_moving and not self.is_moving:
            SHIP_CHANNEL.play(SOUNDS.move_sound, -1)
            self.is_moving = True
            
        if not is_moving and self.is_moving:
            SHIP_CHANNEL.stop()
            self.is_moving = False
        
        screen_constraints = {
            "left" : 0,
            "right" : 1000,
            "top" : 400,
            "bottom" : 800
        }
        
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left >= screen_constraints["left"]:
            self.rect.x -= self.velo
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right <= screen_constraints["right"]:
            self.rect.x += self.velo
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.top >= screen_constraints["top"]:
            self.rect.y -= self.velo
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom <= screen_constraints["bottom"]:
            self.rect.y += self.velo
    
    def update(self):
        self.move()