import pygame

INIT_FALL_SPEED = 6
DEATH_HEIGHT = 800
class Asteroid(pygame.sprite.Sprite):
    """
    Initializes the asteroid.
    args: (tuple) pos = spawn position
    return: None
    """
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid.png").convert_alpha()
        self.hitbox = pygame.mask.from_surface(self.image)
        self.rect = self.hitbox.get_rect(midtop = pos)
        self.fall_speed = INIT_FALL_SPEED
        self.death_height = DEATH_HEIGHT

    def set_fall_speed(self, new_fall_speed):
        """
        Sets the asteroid's fall speed to the inputted parameter.
        args: (int) new_fall_speed
        return: None
        """
        self.fall_speed = new_fall_speed

    def update(self):
        """
        Updates the asteroids position; if the asteroid falls beneath DEATH_HEIGHT, it is removed from all sprite groups.
        args: None
        return: None
        """
        self.rect.y += self.fall_speed
        if self.rect.y > DEATH_HEIGHT:
            self.kill()