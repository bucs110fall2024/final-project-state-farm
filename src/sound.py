import pygame

pygame.init()

MUSIC_CHANNEL = pygame.mixer.Channel(1)
BUTTON_CLICK_CHANNEL = pygame.mixer.Channel(2)
GAME_SFX_CHANNEL = pygame.mixer.Channel(3)
GAME_OVER_SFX_CHANNEL = pygame.mixer.Channel(4)

class Sound:
    
    def __init__(self):
        """
        
        
        
        """
        self.sfx_on = True
        self.music_on = True

        self.move_sound = pygame.mixer.Sound("assets/move_sound.mp3")
        self.collision_sound = pygame.mixer.Sound("assets/collision_sfx.mp3")
        self.game_over_sound = pygame.mixer.Sound("assets/game_over_sfx.mp3")
        self.button_hover_sound = pygame.mixer.Sound("assets/button_hover.mp3")
        self.button_click_sound = pygame.mixer.Sound("assets/button_click.mp3")
        
        self.menu_music = pygame.mixer.Sound("assets/menu_music.mp3")
        self.game_music = pygame.mixer.Sound("assets/game_music.mp3")
        self.options_music = pygame.mixer.Sound("assets/options_music.mp3")

        self.sfx_channels = [BUTTON_CLICK_CHANNEL, GAME_SFX_CHANNEL, GAME_OVER_SFX_CHANNEL]
        

    def toggle_sfx(self):
        self.sfx_on = not self.sfx_on
        
        for channel in self.sfx_channels:
            if not self.sfx_on:
                channel.set_volume(0)
                channel.stop()
            # self.move_sound.set_volume(1)
            # self.collision_sound.set_volume(1)
            # self.game_over_sound.set_volume(1)
            # self.button_hover_sound.set_volume(1)
            # self.button_click_sound.set_volume(1)
        
            else:
                channel.set_volume(1)
            # self.move_sound.set_volume(0)
            # self.collision_sound.set_volume(0)
            # self.game_over_sound.set_volume(0)
            # self.button_hover_sound.set_volume(1)
            # self.button_click_sound.set_volume(1)

    def toggle_music(self):
        self.music_on = not self.music_on
        if not self.music_on:
            MUSIC_CHANNEL.set_volume(0)
            MUSIC_CHANNEL.stop()
        else:
            MUSIC_CHANNEL.set_volume(1)
