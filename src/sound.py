import pygame

pygame.init()

BUTTON_CHANNEL = pygame.mixer.Channel(0)
MUSIC_CHANNEL = pygame.mixer.Channel(1)
SHIP_CHANNEL = pygame.mixer.Channel(2)
GAME_SFX_CHANNEL = pygame.mixer.Channel(3)
GAME_OVER_SFX_CHANNEL = pygame.mixer.Channel(4)

class Sound:
    def __init__(self):
        """
        Creates a library of named sounds and channels to draw from.
        args: None
        return: None
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

        #group all sfx channels into a list
        self.sfx_channels = [BUTTON_CHANNEL, GAME_SFX_CHANNEL, GAME_OVER_SFX_CHANNEL, SHIP_CHANNEL]
        
    def toggle_sfx(self):
        """
        Toggles the state of the SFX channels.
        args: None
        return: None
        """
        self.sfx_on = not self.sfx_on
        
        for channel in self.sfx_channels:
            if not self.sfx_on:
                channel.set_volume(0)
                channel.stop()
            else:
                channel.set_volume(1)

    def toggle_music(self):
        """
        Toggles the state of the MUSIC channels.
        args: None
        return: None
        """
        self.music_on = not self.music_on
        if not self.music_on:
            MUSIC_CHANNEL.set_volume(0)
            MUSIC_CHANNEL.stop()
        else:
            MUSIC_CHANNEL.set_volume(1)