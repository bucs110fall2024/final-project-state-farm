import pygame

class Sound:
    
    def __init__(self):
        """
        
        
        
        """
        self.move_sound = pygame.mixer.Sound("assets/move_sound.mp3")
        self.collision_sound = pygame.mixer.Sound("assets/collision_sfx.mp3")
        self.game_over_sound = pygame.mixer.Sound("assets/game_over_sfx.mp3")
        self.music = pygame.mixer.Sound("assets/music.mp3")
    
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
