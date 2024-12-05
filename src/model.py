import pygame
import random
import sys

SCR_WIDTH = 1000
SCR_HEIGHT = 800


# class GameState:
#     def __init__(self):
#         self.score = 0
#         self.time = Timer()
#         self.highscore = 0
#         self.state = "menu"

#     def set_time(self):
#         if self.time.resume_time == 0:
#             self.time.start()
#         if self.state == "game":
#             self.time.resume()
#         elif self.state == "pause":
#             self.time.pause()
        
#     # def render_time(self):
#     #     text_rend = self.font.render(self.time.get_str(), True, "white")
#     #     rect = text_rend.get_rect(bottomleft = (0, SCR_HEIGHT))
#     #     self.screen.fill("black", rect)
#     #     self.screen.blit(text_rend, rect)
    
#     def update(self):
#         self.set_time()
#         # self.render_time()





# class GameState:
#     def __init__(self):
#         self.running = True
#         self.playing = False
#         self.score = 0
#         self.time = Timer()
#         self.highscore = 0
#         self.state = "menu"
#         self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
#         pygame.display.set_caption("Jake Edelstein CS110 Final Project - Asteroid Dodging Game")

#     def set_time(self):
#         if self.time.resume_time == 0:
#             self.time.start()
#         if self.state == "game":
#             self.time.resume()
#         elif self.state == "pause":
#             self.time.pause()
        
#     def render_time(self):
#         font = pygame.font.Font("assets/PublicPixel-rv0pA.ttf", 15)
#         text = font.render(self.time.get_str(), True, "white")
#         rect = text.get_rect(bottomleft = (0, SCR_HEIGHT))
#         self.screen.fill("black", rect)
#         self.screen.blit(text, rect)
    
#     def update(self):
#         self.set_time()
#         self.render_time()





        # self.switch_menu_state()
        












# class Menu:
    
#     def __init__(self, game):
#         self.MENU_STATES = {
#         "Back" : "menu",
#         "Main Menu" : "menu",
#         "Play" : "game",
#         "Resume" : "game",
#         "Play Again" : "game",
#         "Settings" : "settings",
#         "Quit" : "quit",
#         "End Game" : "game over"
#     } 
#         self.game = game
#         self.center_x = SCR_WIDTH / 2
#         self.center_y = SCR_HEIGHT / 2
#         self.show_menu = True
#         self.start_y = self.center_y - 30
#         self.state = "menu"
#         self.options = []
#         self.curr_option = 0
#         self.cursor_offset = -120
#         self.cursor = Cursor((self.center_x + self.cursor_offset, self.center_y))

#     # def set_options(self, options):
#     #     self.options.extend(options)

    # def draw_cursor(self, right_x, mid_y):
    #     self.cursor = Cursor((right_x, mid_y))

#     def move_cursor(self):
#         self.game.check_events()
#         if self.game.UP:
#             self.curr_option = (self.curr_option - 1) % len(self.options)
            
#         if self.game.DOWN:
#             self.curr_option = (self.curr_option + 1) % len(self.options)
#         increment = 20
#         self.cursor.rect.midright = (self.center_x + self.cursor_offset, self.start_y + (increment * self.curr_option))
#         self.switch_menu_state()

#     def switch_menu_state(self):
#         """
#         Responds to user's menu selection by changing the menu state
#         args: none
#         return: None
#         """
#         if self.game.RETURN:
#             self.state = self.MENU_STATES.get(self.options[self.curr_option])
   
#     def set_menu_state(self, state):
#         """
#         Sets the menu state to the inputted 'state' parameter
#         args: str
#         return: None
#         """
#         self.state = state

#     def pause(self):
#         if self.MENU_STATES.get(self.options[self.curr_option]) == "game":
#             self.game.check_events()
#             if self.game.ESCAPE:
#                 self.set_menu_state("pause")

#     def select_option(self):
#         if self.game.RETURN:
#             self.switch_menu_state()

#     def show_menu(self):
#         self.show_menu = True
#         while self.show_menu:
#             self.game.check_events()
#             self.game.screen.fill("black")
#             option_increment = 20
#             title_y = self.center_y - (len(self.options) * option_increment / 2) - 20
#             start_y = title_y + 30
#             self.game.draw_text(self, 25, (self.center_x, title_y))
#             self.move_cursor(start_y)
#             self.draw_cursor()

#             for x in self.options:
#                 self.game.draw_text(x, 20, (self.center_x, start_y))
#                 start_y += 20
            
#         self.game.screen.blit()

#     def update(self):
#         self.move_cursor()
#         self.select_option()

# #     def mainloop(self):







    
