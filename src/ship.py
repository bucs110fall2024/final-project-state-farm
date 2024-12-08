import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('assets/ship.png').convert_alpha()
        self.hitbox = pygame.mask.from_surface(self.image)
        self.rect = self.hitbox.get_rect(center = pos)
        self.velo = 8
        # self.boosting = False


    def move(self):
        """
        Moves the ship's position based on keys pressed.
        args: None
        return: None
        """
        keys = pygame.key.get_pressed()

    #     boosting = self.boost >= 50 and pygame.key.get_mods() & pygame.KMOD_CTRL
    #     if boosting:
    #         if self.velo == 1:
    #             self.velo = self.velo * 2
    #         self.boost -= 50

    #     else:
    #         self.velo = 1
    #         if self.boost < 992:
    #             self.boost += 8
    #         if self.boost >= 992:
    #             self.boost = 1000
        
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





    