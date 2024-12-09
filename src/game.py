import pygame
import sys
import random
import math
from src.ship import Ship
from src.asteroid import Asteroid, INIT_FALL_SPEED
from src.textbox import Textbox
from src.counter import Counter
from src.button import Button
from src.sound import Sound, MUSIC_CHANNEL, SHIP_CHANNEL, GAME_SFX_CHANNEL, GAME_OVER_SFX_CHANNEL

SCREEN_W = 1000
SCREEN_H = 800
START_Y = 400
PLAY_AGAIN_Y = 500
HIGHSCORE_X = 115
HIGHSCORE_Y = 20
HIGHSCORE_MAX_NUM = 5
CENTER_X = 500
MENU_BUTTON_Y_INCREMENT = 40
TITLE_Y = OPTIONS_Y = HIGHSCORE_TITLE_Y = GAME_OVER_Y = 250
TITLE_SIZE = OPTIONS_SIZE = GAME_OVER_SIZE = HIGHSCORE_TITLE_SIZE = 50
TIMER_X = 110
TIMER_Y = 10
TIMER_INIT_TEXT = "Time: 00:00"
SCORE_X = 850
SCORE_Y = 10
SCORE_INIT_TEXT = "SCORE: 00000000"
FRAME_RATE = 60
ASTEROID_INIT_FALL_SPEED = 6
ASTEROID_INIT_STAGGER = 0.8
INIT_SPEED_INCREASE_COOLDOWN = 20
INIT_STAGGER_DECREASE_COOLDOWN = 5
MENU_BACKGROUND = pygame.image.load("assets/menu_background.png")
GAME_BACKGROUND = pygame.image.load("assets/game_background.png")
DISPLAY_ICON = pygame.image.load("assets/display_icon.png")

SOUNDS = Sound()
CLOCK = pygame.time.Clock()

class Game:
    def __init__(self):
        """
        Initializes key parts of the game (screen, sprites/sprite groups, timer, score, gamestate)
        args: None
        return: None
        """
        #screen
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("SPACE ROCKS")
        pygame.display.set_icon(DISPLAY_ICON)

        #background
        self.background = pygame.transform.scale(MENU_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))

        #sprites
        self.ship = Ship((SCREEN_W / 2, SCREEN_H - 50))
        self.myship = pygame.sprite.GroupSingle(self.ship)

        self.asteroids = pygame.sprite.Group()
        self.asteroid_fall_speed = ASTEROID_INIT_FALL_SPEED
        self.asteroid_speed_increase_cooldown = INIT_SPEED_INCREASE_COOLDOWN
        self.asteroid_stagger = ASTEROID_INIT_STAGGER
        self.asteroid_stagger_decrease_cooldown = INIT_STAGGER_DECREASE_COOLDOWN
        self.asteroid_last_spawn = 0

        self.counters = pygame.sprite.Group()
        self.timer = Counter(TIMER_X, TIMER_Y, TIMER_INIT_TEXT, "timer")
        self.counters.add(self.timer)
        self.score = Counter(SCORE_X, SCORE_Y, SCORE_INIT_TEXT, "score")
        self.counters.add(self.score)

        #variables to update highscores
        self.last_score = 0
        self.hs_added = False
        self.hs_list = [0] * HIGHSCORE_MAX_NUM

        #gamestate
        self.state = "menu"

    def reset_game(self):
        """
        Helper function which resets the necessary variables to initialize the game state.
        args: None
        return: None 
        """
        #reset counters
        self.timer.time.reset()
        self.timer.time.start()
        self.score.reset()
        
        #reset ship
        self.ship = Ship((SCREEN_W / 2, SCREEN_H - 50))
        self.myship = pygame.sprite.GroupSingle(self.ship)

        #reset asteroids
        self.asteroids.empty()
        self.asteroid_last_spawn = 0
        self.asteroid_fall_speed = INIT_FALL_SPEED
        self.asteroid_stagger = ASTEROID_INIT_STAGGER
        self.asteroid_speed_increase_cooldown = INIT_SPEED_INCREASE_COOLDOWN
        self.asteroid_stagger_decrease_cooldown = INIT_STAGGER_DECREASE_COOLDOWN

    def mainloop(self):
        """
        Allows program to switch between gamestates.
        args: None
        return: None
        """
        while True:
            if self.state == "menu":
                self.menuloop()
            if self.state == "highscores":
                self.highscoreloop()
            if self.state == "game":
                self.gameloop()
            if self.state == "options":
                self.optionsloop()
            if self.state == "game over":
                self.gameoverloop()

    def menuloop(self):
        """
        Displays and manages the menu screen.
        args: None
        return: None
        """
        
        #background
        self.background = pygame.transform.scale(MENU_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))

        #music
        MUSIC_CHANNEL.play(SOUNDS.menu_music, -1)
        
        while self.state == "menu":
            #title
            title = Textbox(CENTER_X, TITLE_Y, "SPACE ROCKS")
            title.set_font_size(TITLE_SIZE)

            #buttons
            menu_buttons = pygame.sprite.Group()
            num_buttons = 0

            start_button = Button(CENTER_X, START_Y, "START")
            menu_buttons.add(start_button)
            num_buttons += 1

            options_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, "OPTIONS")
            menu_buttons.add(options_button)
            num_buttons += 1

            quit_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons,"QUIT")
            menu_buttons.add(quit_button)
            num_buttons += 1

            highscore_button = Button(HIGHSCORE_X, HIGHSCORE_Y, "HIGHSCORES")
            menu_buttons.add(highscore_button)
            num_buttons += 1

            #manage events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if start_button.is_clicked(event):
                    self.reset_game()
                    self.state = "game"
                elif options_button.is_clicked(event):
                    self.state = "options"
                elif highscore_button.is_clicked(event):
                    self.state = "highscores"
                elif quit_button.is_clicked(event):
                    pygame.quit()
                    sys.exit()
        
            #update screen
            self.screen.blit(self.background, (0, 0))
            title.update(self.screen)
            menu_buttons.update(self.screen)
            pygame.display.update()
        
    def highscoreloop(self):
        """
        Updates and displays the 5 highest recorded scores within the current launch.
        args: None
        return: None        
        """

        while self.state == "highscores":
            #title
            highscore_title = Textbox(CENTER_X, HIGHSCORE_TITLE_Y, "HIGHSCORES")
            highscore_title.set_font_size(HIGHSCORE_TITLE_SIZE)
            
            #buttons
            back_button = Button(CENTER_X, 640, "BACK")
            highscore_buttons = pygame.sprite.GroupSingle(back_button)
            
            #manage events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if back_button.is_clicked(event):
                    self.state = "menu"
                
            #highscore sprites
            highscore_group = pygame.sprite.Group()
            hs_start_y = HIGHSCORE_TITLE_Y + 150
            hs_rank_list = ["1ST", "2ND", "3RD", "4TH", "5TH"]
            hs_rank_length = 3
            hs_max_length = 8
           
            #initializing sprites with updated highscores and formatting textbox to align scores properly
            for hs in self.hs_list:
                curr_rank = hs_rank_list[0]
                hs_text = f"{curr_rank:<{hs_rank_length}}         {hs:>{hs_max_length}}"

                #only creates highscore texboxes for non-zero scores
                if hs != 0:
                    hs_textbox = Textbox(CENTER_X, hs_start_y, hs_text)
                    highscore_group.add(hs_textbox)
                    hs_start_y += MENU_BUTTON_Y_INCREMENT
                hs_rank_list.pop(0)
            
            #update display
            self.screen.blit(self.background, (0, 0))
            highscore_title.update(self.screen)
            highscore_buttons.update(self.screen)
            
            for hs in highscore_group:
                hs.update(self.screen)

            pygame.display.update()
                
    def gameloop(self):
        """
        Displays and manages the game screen.
        args: None
        return: None
        """
        has_collided = False
        
        
        #music
        MUSIC_CHANNEL.play(SOUNDS.game_music, -1)

        while self.state == "game":            
            #reset hs_added
            self.hs_added = False
            
            #set background
            self.background = pygame.transform.scale(GAME_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))
            
            #manage events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    GAME_SFX_CHANNEL.play(SOUNDS.button_click_sound, 0)
                    if not self.timer.time.paused:
                        self.timer.time.stop()
                    else:
                        self.timer.time.start()

            #initializing sprites (for restart)
            if self.timer.restarting:
                self.ship = Ship((SCREEN_W / 2, SCREEN_H - 50))
                self.myship = pygame.sprite.GroupSingle(self.ship)
            #restart
            if not self.timer.time.paused:
                #collision
                if pygame.sprite.spritecollide(self.ship, self.asteroids, False, pygame.sprite.collide_mask):
                    #reset all necessary variables
                    has_collided = True
                    self.last_score = self.score.myscore
                    #updating highscores
                    if self.score.myscore > min(self.hs_list) and not self.hs_added:
                        self.hs_list.append(self.score.myscore)
                        # print(f"High score list after append: {self.hs_list}") #debug
                        self.hs_list.sort(reverse = True)
                        # print(f"High score list after sort: {self.hs_list}") #debug
                        self.hs_list = self.hs_list[:HIGHSCORE_MAX_NUM]
                        # print(f"New high score list: {self.hs_list}") #debug
                        self.hs_added = True
                    
                    #end game
                    self.timer.time.stop()
                    self.myship.empty()
                    MUSIC_CHANNEL.stop()
                    SHIP_CHANNEL.stop()
                    GAME_SFX_CHANNEL.play(SOUNDS.collision_sound, 0)
                    pygame.time.wait(2000)
                    self.state = "game over"
                    
                #manage game
                if not has_collided:
                    self.counters.update(self.screen)

                    #difficulty increase
                    speed_increase = math.floor(self.timer.time.get_time() / self.asteroid_speed_increase_cooldown) == 1
                    stagger_decrease = math.floor(self.timer.time.get_time() / self.asteroid_stagger_decrease_cooldown) == 1

                    if speed_increase:
                        self.asteroid_fall_speed += 2
                        self.asteroid_speed_increase_cooldown += self.asteroid_speed_increase_cooldown
                    
                    if stagger_decrease:
                        if self.asteroid_stagger > 0.1:
                            self.asteroid_stagger -= 0.1
                        else:
                            self.asteroid_stagger *= 0.8

                        self.asteroid_stagger_decrease_cooldown += self.asteroid_stagger_decrease_cooldown

                    #respawning asteroids / asteroid spawning cooldown
                    if self.timer.time.get_time() - self.asteroid_last_spawn >= self.asteroid_stagger:
                        newasteroid = Asteroid((random.randint(0, SCREEN_W), 0))
                        self.asteroid_last_spawn = self.timer.time.get_time()
                        self.asteroids.add(newasteroid)
                        
                    #set asteroid speed 
                    for asteroid in self.asteroids:
                        asteroid.set_fall_speed(self.asteroid_fall_speed)

                #update screen
                self.screen.blit(self.background, (0, 0))
                self.myship.update()
                self.myship.draw(self.screen)
                self.asteroids.update()
                self.asteroids.draw(self.screen)
                self.counters.update(self.screen)

            #pause menu
            else:
                #background
                self.background = pygame.transform.scale(MENU_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))
                
                pause = Textbox(CENTER_X, 200 , "PAUSED")
                resume_message = Textbox(CENTER_X, 300, "PRESS ESC TO RESUME")

                #create buttons for pause menu
                pause_buttons = pygame.sprite.Group()

                #changes button text to match the state of SFX and music    
                sfx_text = "SFX: ON"
                if not SOUNDS.sfx_on:
                    sfx_text = "SFX: OFF"

                music_text = "MUSIC: ON"
                if not SOUNDS.music_on:
                    music_text = "MUSIC: OFF"
                    
                #buttons
                sfx_button = Button(CENTER_X, 500, sfx_text)
                pause_buttons.add(sfx_button)

                music_button = Button(CENTER_X, 550, music_text)
                pause_buttons.add(music_button)

                menu_button = Button(CENTER_X, 600, "BACK TO MENU")
                pause_buttons.add(menu_button)

                quit_button = Button(CENTER_X, 650, "QUIT")
                pause_buttons.add(quit_button)

                #manage events in pause menu
                for event in events:
                    if sfx_button.is_clicked(event):
                        SOUNDS.toggle_sfx()
                    elif music_button.is_clicked(event):
                        SOUNDS.toggle_music()
                        if SOUNDS.music_on:
                            MUSIC_CHANNEL.play(SOUNDS.game_music, -1)
                    elif menu_button.is_clicked(event):
                        
                        self.state = "menu"
                    elif quit_button.is_clicked(event):
                        pygame.quit()
                        sys.exit()

                #update pause menu
                self.screen.blit(self.background, (0, 0))
                pause.update(self.screen)
                pause_buttons.update(self.screen)
                resume_message.update(self.screen)

            #update game
            pygame.display.update()
            CLOCK.tick(FRAME_RATE)

    def optionsloop(self):
        """
        Manages and displays the options menu.
        args: None
        return:
        """

        #background
        self.background = pygame.transform.scale(MENU_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))

        #music
        MUSIC_CHANNEL.play(SOUNDS.options_music, -1)

        while self.state == "options":
            #title
            title = Textbox(CENTER_X, OPTIONS_Y, "OPTIONS")
            title.set_font_size(OPTIONS_SIZE)
            
            #buttons
            options_buttons = pygame.sprite.Group()
            num_buttons = 0

            #changes button text to match the state of SFX and music
            sfx_text = "SFX: ON"
            if not SOUNDS.sfx_on:
                sfx_text = "SFX: OFF"

            music_text = "MUSIC: ON"
            if not SOUNDS.music_on:
                music_text = "MUSIC: OFF"

            sfx_button = Button(CENTER_X, START_Y, sfx_text)
            options_buttons.add(sfx_button)
            num_buttons += 1

            music_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, music_text)
            options_buttons.add(music_button)
            num_buttons += 1

            back_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, "BACK TO MENU")
            options_buttons.add(back_button)
            num_buttons += 1

            #manage events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if sfx_button.is_clicked(event):
                    SOUNDS.toggle_sfx()
                elif music_button.is_clicked(event):
                    SOUNDS.toggle_music()
                    if SOUNDS.music_on:
                        MUSIC_CHANNEL.play(SOUNDS.options_music, -1)
                elif back_button.is_clicked(event):
                    self.state = "menu"
            
            #update screen
            self.screen.blit(self.background, (0, 0))
            title.update(self.screen)
            options_buttons.update(self.screen)
            pygame.display.update()

    def gameoverloop(self):
        """
        Displays and manages the game over screen.
        """

        #background
        self.background = pygame.transform.scale(MENU_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))

        self.timer.restarting = True
        #music/sfx
        MUSIC_CHANNEL.stop()
        GAME_OVER_SFX_CHANNEL.play(SOUNDS.game_over_sound, 0)
        MUSIC_CHANNEL.play
        while self.state == "game over":
            
            #buttons
            game_over_buttons = pygame.sprite.Group()
            num_buttons = 0

            play_again_button = Button(CENTER_X, PLAY_AGAIN_Y, "PLAY AGAIN")
            game_over_buttons.add(play_again_button)
            num_buttons += 1

            options_button = Button(CENTER_X, PLAY_AGAIN_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, "OPTIONS")
            game_over_buttons.add(options_button)
            num_buttons += 1

            menu_button = Button(CENTER_X, PLAY_AGAIN_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, "BACK TO MENU")
            game_over_buttons.add(menu_button)
            num_buttons += 1

            quit_button = Button(CENTER_X, PLAY_AGAIN_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, "QUIT")
            game_over_buttons.add(quit_button)
            num_buttons += 1

            #manage events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if play_again_button.is_clicked(event):
                    GAME_OVER_SFX_CHANNEL.stop()
                    self.reset_game()
                    self.state = "game"
                elif options_button.is_clicked(event):
                    GAME_OVER_SFX_CHANNEL.stop()
                    self.state = "options"
                elif menu_button.is_clicked(event):
                    GAME_OVER_SFX_CHANNEL.stop()
                    self.state = "menu"
                elif quit_button.is_clicked(event):
                    pygame.quit()
                    sys.exit()

            #textboxes            
            end_textboxes = pygame.sprite.Group()

            game_over_textbox = Textbox(CENTER_X, GAME_OVER_Y, "OH NO! YOU EXPLODED!")
            game_over_textbox.set_font_size(50)
            end_textboxes.add(game_over_textbox)

            final_score_textbox = Textbox(CENTER_X, GAME_OVER_Y + 100, f"SCORE: {self.last_score}")
            end_textboxes.add(final_score_textbox)

            #checks if the score for the last game was a highscore (top 5)
            if self.hs_added:
                new_highscore_textbox = Textbox(CENTER_X, GAME_OVER_Y + 75, "NEW HIGHSCORE!")
                end_textboxes.add(new_highscore_textbox)                

            #update screen
            self.screen.blit(self.background, (0, 0))
            end_textboxes.update(self.screen)
            game_over_buttons.update(self.screen)
            pygame.display.update()