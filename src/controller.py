import pygame

import model
import view

pygame.init()

class Controller:
    def __init__(self, model):
        self.model = model
        self.gamestate = "menu"

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
        menu_options = ["Play", "Settings", "Quit"]
        curr_option = 0
        # self.gamestate = "menu"

        while(self.gamestate == "menu"):
            for event in pygame.event.get():
                # if event.type == pygame.QUIT:
                #     self.gamestate = "quit"

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_UP:
                        curr_option = (curr_option - 1) % len(menu_options)
                    elif event.type == pygame.K_DOWN:
                        curr_option = (curr_option + 1) % len(menu_options)
                    elif event.type == pygame.K_RETURN:
                        if menu_options[curr_option] == "Play":
                            self.gamestate = "game"
                        elif menu_options[curr_option] == "Settings":
                            self.gamestate = "settings"
                        elif menu_options[curr_option] == "Quit":
                            self.gamestate = "quit"

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
        settings_options = ["SFX", "Music", "Back"]
        curr_option = 0

        while(self.gamestate == "settings"):
            for event in pygame.event.get():
                # if event.type == pygame.QUIT:
                #     self.gamestate = "quit"

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_UP:
                        curr_option = (curr_option - 1) % len(settings_options)
                    elif event.type == pygame.K_DOWN:
                        curr_option = (curr_option + 1) % len(settings_options)
                    elif event.type == pygame.K_RETURN:
                        if settings_options[curr_option] == "SFX":
                            Sound.toggle_sfx()
                        elif settings_options[curr_option] == "Music":
                            Sound.toggle_music()
                        elif settings_options[curr_option] == "Back":
                            self.gamestate = "menu"

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

    def gameloop(self):
        while(self.gamestate == "game"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestate = "quit"
                elif event.type == pygame.K_ESCAPE:
                    self.gamestate = "menu"
            
            """
            stuff
            the code
            do
            """
            pygame.display.flip()

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
        while(self.gamestate == "game over"):
            for event in pygame.event.get():
                # if event.type == pygame.QUIT:
                #     self.gamestate = "quit"

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
        self.gamestate = "menu"
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if self.gamestate == "menu":
                self.menuloop()
            elif self.gamestate == "settings":
                self.settingsloop()
            elif self.gamestate == "game":
                self.gameloop()
            elif self.gamestate == "game over":
                self.game_over_loop()
            else:
                running = False

            pygame.display.flip()
        
        pygame.quit()
