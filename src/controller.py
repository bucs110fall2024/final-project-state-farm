import pygame

from src.game import Game
from src.ship import Ship
from src.asteroid import Asteroid
from src.sound import Sound
from src.timer import Timer
from src.menu import Menu, MainMenu

class Controller:
    def __init__(self):
        self.game = Game()
        self.menu = Menu(self.game)
        ship_sprite = Ship((self.game.screen_w / 2, self.game.screen_h - 50))
        self.ship = pygame.sprite.GroupSingle(ship_sprite)

    def main_menu_loop(self):
        while self.menu_open == True:
            self.check_events()
            if self.state != "menu":
                self.menu_open == False
            self.display.fill("black")
            
            self.screen.blit(self.display, (0, 0))

            pygame.display.update()
            self.reset_events()















    # def check_events(self):
    #     """
    #     Runs a check for all events relevant to the Controller class.
    #     args: None
    #     return: None
    #     """
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.gamestate = "quit"
    #         if event.type == pygame.KEYDOWN:
    #             if event.type == pygame.K_UP:
    #                 self.UP = True
    #             if event.type == pygame.K_DOWN:
    #                 self.DOWN = True
    #             if event.type == pygame.K_RETURN:
    #                 self.RETURN = True
    #             if event.type == pygame.K_ESCAPE:
    #                 self.ESCAPE = True
        
    # def menuloop(self):
    #     menu_options = ["Play", "Settings", "Quit"]
    #     curr_option = 0
        
    #     menu_running = True
    #     settings_running = False
    #     game_running = False

    #     while(menu_running):
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 menu_running = False

    #             elif event.type == pygame.KEYDOWN:
    #                 if event.type == pygame.K_UP:
    #                     curr_option = (curr_option - 1) % len(menu_options)
    #                 elif event.type == pygame.K_DOWN:
    #                     curr_option = (curr_option + 1) % len(menu_options)
    #                 elif event.type == pygame.K_RETURN:
    #                     if menu_options[curr_option] == "Play":
    #                         menu_running = False
    #                         game_running = True
    #                     elif menu_options[curr_option] == "Settings":
    #                         menu_running = False
    #                         settings_running = True
    #                     elif menu_options[curr_option] == "Quit":
    #                         menu_running = False

    def menuloop(self):
        self.menu = Menu(self.game)
        menu_options = ["Play", "Settings", "Quit"]
        self.menu.set_options(menu_options)
        
        while(self.game.state == "menu"):
            self.game.check_events()
            # if self.game.UP:
            #     curr_option = (curr_option - 1) % len(menu_options)
            # elif self.game.DOWN:
            #     curr_option = (curr_option + 1) % len(menu_options)
            self.menu.move_cursor()
            
            if self.game.RETURN:
                if menu_options[self.menu.curr_option] == "Play":
                    self.game.state = "game"
                elif menu_options[self.menu.curr_option] == "Settings":
                    self.game.state = "settings"
                elif menu_options[self.menu.curr_option] == "Quit":
                    self.game.state = "quit"
            

    # def settingsloop(self):
    #     settings_options = ["SFX", "Music", "Back"]
    #     curr_option = 0
        
    #     settings_running = True
    #     menu_running = False

    #     while(settings_running):
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 settings_running = False

    #             elif event.type == pygame.KEYDOWN:
    #                 if event.type == pygame.K_UP:
    #                     curr_option = (curr_option - 1) % len(settings_options)
    #                 elif event.type == pygame.K_DOWN:
    #                     curr_option = (curr_option + 1) % len(settings_options)
    #                 elif event.type == pygame.K_RETURN:
    #                     if settings_options[curr_option] == "SFX":
    #                         Sound.toggle_sfx()
    #                     elif settings_options[curr_option] == "Music":
    #                         Sound.toggle_music()
    #                     elif settings_options[curr_option] == "Back":
    #                         settings_running = False
    #                         menu_running = True

    def settingsloop(self):
        menu = Menu(self.game)
        settings_options = ["SFX", "Music", "Back"]
        menu.set_options(settings_options)

        while(self.game.state == "settings"):
            self.game.check_events()
            # if self.game.UP:
            #     curr_option = (curr_option - 1) % len(settings_options)
            # elif self.game.DOWN:
            #     curr_option = (curr_option + 1) % len(settings_options)
            # menu.move_cursor()

            if self.game.RETURN:
                if settings_options[menu.curr_option] == "SFX":
                    Sound.toggle_sfx()
                elif settings_options[menu.curr_option] == "Music":
                    Sound.toggle_music()
                elif settings_options[menu.curr_option] == "Back":
                    self.game.state = "menu"

    # def gameloop(self):
    #     game_running = True
    #     menu_running = False
        
    #     while game_running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 game_running = False
                
    #             elif event.type == pygame.K_ESCAPE:
    #                 game_running = False
    #                 menu_running = True
            
    #         """
    #         stuff
    #         the code
    #         do
    #         """
    #         pygame.display.flip()

    #         """
    #         updates
    #         for
    #         next loop
    #         """

    def pauseloop(self):
        pause_options = ["Resume", "Settings", "End Game", "Quit"]
        curr_option = 0
        
        self.game.check_events()
        if self.game.UP:
            curr_option = (curr_option - 1) % len(pause_options)
        elif self.game.DOWN:
            curr_option = (curr_option + 1) % len(pause_options)
        elif self.game.RETURN:
            if pause_options[curr_option] == "Resume":
                self.game.state = "game"
            elif pause_options[curr_option] == "Settings":
                self.game.state = "settings"
            elif pause_options[curr_option] == "End Game":
                self.game.state = "game over"
            elif pause_options[curr_option] == "Quit":
                self.game.state = "quit"

    def gameloop(self):
        self.game.check_events()
        while(self.game.state == "game"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.state = "quit"
                elif event.type == pygame.K_ESCAPE:
                    self.game.state = "pause"
            
            clock = pygame.time.Clock()
            self.game.screen.fill("black")
            self.ship.update()
            self.ship.draw(self.game.screen)
            timer_center_pos = (90, 20)
            self.game.draw_text(self.game.time.get_str(), 15, (timer_center_pos))
            
            self.game.update()
            
            pygame.display.flip()
            clock.tick(320)
            """
            stuff
            the code
            do
            """
            self.game.screen.fill("black")
            pygame.display.flip()
            self.game.reset_events()

            """
            updates
            for
            next loop
            """
    # def game_over_loop():
    #     game_over_running = True
    #     menu_running = False
    #     game_running = False

    #     game_over_options = ["Play Again", "Main Menu", "Quit"]
    #     while(game_over_running):
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 game_over_running = False

    #             elif event.type == pygame.KEYDOWN:
    #                 if event.type == pygame.K_UP:
    #                     curr_option = (curr_option - 1) % len(game_over_options)
    #                 elif event.type == pygame.K_DOWN:
    #                     curr_option = (curr_option + 1) % len(game_over_options)
    #                 elif event.type == pygame.K_RETURN:
    #                     if game_over_options[curr_option] == "Play Again":
    #                         game_over_running = False
    #                         game_running = True
    #                     elif game_over_options[curr_option] == "Main Menu":
    #                         menu_running = True
    #                         game_over_running = False
    #                     else:
    #                         game_over_running = False

    def game_over_loop(self):
        game_over_options = ["Play Again", "Main Menu", "Quit"]
        while(self.game == "game over"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = "quit"

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_UP:
                        curr_option = (curr_option - 1) % len(game_over_options)
                    elif event.type == pygame.K_DOWN:
                        curr_option = (curr_option + 1) % len(game_over_options)
                    elif event.type == pygame.K_RETURN:
                        
                        if game_over_options[curr_option] == "Play Again":
                            game_over_running = False
                            game_running = True
                        elif game_over_options[curr_option] == "Main Menu":
                            menu_running = True
                            game_over_running = False
                        else:
                            game_over_running = False

    def mainloop(self):
        pygame.init()
        self.game.state = "menu"
        while(self.game.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
            if self.game.state == "menu":
                self.menuloop()
                self.game.playing = False
            elif self.game.state == "settings":
                self.settingsloop()
            elif self.game.state == "game":
                self.gameloop()
                self.game.playing = True
            elif self.game.state == "pause":
                self.pauseloop()
            elif self.game.state == "game over":
                self.game_over_loop()
                self.game.playing = False
            else:
                self.game.running = False
                self.game.playing = False
            
        
        pygame.quit()
        quit()