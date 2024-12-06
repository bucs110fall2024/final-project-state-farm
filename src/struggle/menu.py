import pygame

class Menu():
    def __init__(self):
        self.game = Game()
        self.center_x = self.game.screen_w / 2
        self.center_y = self.game.screen_h / 2
        self.show_menu = True
        self.cursor_rect = pygame.Rect(self.center_x - 120, self.center_y, 20, 20)
        self.cursor_image = pygame.image.load('assets/cursor.png').convert_alpha()
        self.options = []
        self.curr_option = ""

    def draw_cursor(self, midtop):
        self.game.screen.blit(self.cursor_image, self.cursor_rect)
        # pygame.display.flip()

    def screen_blit(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_events()


class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.options = ["Play", "Settings", "Quit"]
        
        self.state = "Play"
        self.y_increment = 20

        self.title_x = self.center_x
        self.title_y = self.center_y - 40
        
        self.play_x = self.center_x
        self.play_y = self.title_y + self.y_increment

        self.settings_x = self.center_x
        self.settings_y = self.play_y + self.y_increment

        self.quit_x = self.center_x
        self.quit_y = self.settings_y + self.y_increment

        self.cursor_rect = pygame.Rect(self.play_x - 120, self.play_y, 20, 20)

    def move_cursor(self):
        self.game.check_events()
        if self.game.UP:
            self.curr_option = (self.curr_option - 1) % len(self.options)
        if self.game.DOWN:
            self.curr_option = (self.curr_option + 1) % len(self.options)
        self.cursor_rect.midright = (self.cursor_rect.right, self.play_y + (self.y_increment * self.curr_option))
    
    def check_inputs(self):
        self.move_cursor()
        if self.game.RETURN:
            if self.state == "Play":
                self.game.playing = True
                self.game.menu_open = False
            elif self.state == "Settings":
                # self.game.curr_menu = Settings()
                pass
            elif self.state == "Quit":
                self.game.running = False

    def draw_menu(self):
        self.show_menu = True
        while self.show_menu:
            self.game.check_events()
            self.check_inputs()
            
            self.game.display.fill("black")

            self.game.draw_text("Main Menu", 20, (self.title_x, self.title_y))
            self.game.draw_text("Play", 20, (self.play_x, self.play_y))
            self.game.draw_text("Settings", 20, (self.settings_x, self.settings_y))
            self.game.draw_text("Quit", 20, (self.quit_x, self.quit_y))
            self.draw_cursor(self.cursor_rect.midtop)


            self.screen_blit()
