import pygame, sys
from timer import Timer
from menu import MainMenu

class Game:
    def __init__(self):
        """
        Initializes the game class
        """
        pygame.init()
        self.screen_w = 1000
        self.screen_h = 800
        self.display = pygame.Surface((self.screen_w, self.screen_h))
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        self.running = True
        self.playing = False
        self.menu_open = True
        self.curr_menu = MainMenu(self)
        self.font = "assets/PublicPixel-rv0pA.ttf"
        pygame.display.set_caption("Jake Edelstein CS110 Final Project - Asteroid Dodging Game")

        self.UP = False
        self.DOWN = False
        self.RETURN = False
        self.ESCAPE = False

        self.score = 0
        self.time = Timer()
        self.highscore = 0
        self.state = "menu"

    def set_time(self):
        if self.time.resume_time == 0:
            self.time.start()
        if self.state == "game":
            self.time.resume()
        elif self.state == "pause":
            self.time.pause()
        
    def check_events(self):
        """
        Runs a check for all events relevant to the Game class.
        args: None
        return: None
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP:
                    self.UP = True
                if event.type == pygame.K_DOWN:
                    self.DOWN = True
                if event.type == pygame.K_RETURN:
                    self.RETURN = True
                if event.type == pygame.K_ESCAPE:
                    self.ESCAPE = True
    
    def reset_events(self):
        """
        Sets the values for all recorded events to false
        args: none
        return: None
        """
        self.UP = False
        self.DOWN = False
        self.RETURN = False
        self.ESCAPE = False
    
    def draw_text(self, text, size, center):
        """
        Draws a text string with inputted font size in a rect defined by its bottom left coordinate
        args: str, int, Point
        return: None
        """
        font = pygame.font.Font(self.font, size)
        text_rend = font.render(text, True, "white")
        text_rect = text_rend.get_rect(center = (center))
        self.display.blit(text_rend, text_rect)



