import pygame
import sys
import random
import math
from src.ship import Ship
from src.asteroid import Asteroid, INIT_FALL_SPEED
from src.textbox import Textbox, BOX_COLOR
from src.counter import Counter
from src.button import Button
from src.highscore import Highscore
from src.sound import Sound, MUSIC_CHANNEL, BUTTON_CLICK_CHANNEL, GAME_SFX_CHANNEL, GAME_OVER_SFX_CHANNEL

SCREEN_W = 1000
SCREEN_H = 800
START_Y = PLAY_AGAIN_Y = 500
HIGHSCORE_X = 115
HIGHSCORE_Y = 780
HIGHSCORE_MAX_NUM = 5
CENTER_X = 500
MENU_BUTTON_Y_INCREMENT = 80
TITLE_Y = OPTIONS_Y = HIGHSCORE_TITLE_Y = 100
TITLE_SIZE = OPTIONS_SIZE = GAME_OVER_SIZE = HIGHSCORE_TITLE_SIZE = 50
TIMER_X = 110
TIMER_Y = 10
TIMER_INIT_TEXT = "Time: 00:00"
SCORE_X = 850
SCORE_Y = 10
SCORE_INIT_TEXT = "SCORE: 00000000"
FRAME_RATE = 60
GAME_OVER_Y = 200
ASTEROID_INIT_FALL_SPEED = 6
ASTEROID_INIT_STAGGER = 0.8
INIT_SPEED_INCREASE_COOLDOWN = 20
INIT_STAGGER_DECREASE_COOLDOWN = 5
GAME_BACKGROUND = pygame.image.load("assets/game_background.png")
END_BACKGROUND = pygame.image.load("assets/end_background.png")

SOUNDS = Sound()
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        """
        initializes key parts of the game (screen, sprites/sprite groups, timer, gamestate)
        args: none
        return: None
        """

        #screen
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

        # #background
        # self.background = (GAME_BACKGROUND, \
        #     (SCREEN_W, SCREEN_H))
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

        # self.last_score = 0
        self.last_scores = []
        self.hs_added = False
        self.hs_list = [0] * HIGHSCORE_MAX_NUM



        #gamestate
        self.state = "menu"

    def mainloop(self):
        """
        Allows program to switch between gamestates
        args: none
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
        displays and manages the menu screen
        args: none
        return: None
        """

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


            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        self.timer.mytime.start()
                        self.score.reset()
                        self.state = "game"
                    elif options_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        self.state = "options"
                    elif highscore_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        self.state = "highscores"
                    elif quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        pygame.quit()
                        sys.exit()
        
            #update screen
            self.screen.fill("black")
            title.draw_textbox(self.screen, "white", "black")
            menu_buttons.update(self.screen, "black")
            pygame.display.update()
        
    def highscoreloop(self):
        """
        updates and displays the 5 highest recorded scores within the current launch
        args: none
        return: None        
        """

        while self.state == "highscores":
        
            #updating highscores
            for score in self.last_scores:
                if score > min(self.hs_list) and not self.hs_added:
                    self.hs_list.append(score)
                    print(f"High score list after append: {self.hs_list}") #debug
                    self.hs_list.sort(reverse = True)
                    print(f"High score list after sort: {self.hs_list}") #debug
                    self.hs_list = self.hs_list[:5]
                    print(f"New high score list: {self.hs_list}") #debug
                    self.hs_added = True
            
            #title
            highscore_title = Textbox(CENTER_X, HIGHSCORE_TITLE_Y, "HIGHSCORES")
            highscore_title.set_font_size(HIGHSCORE_TITLE_SIZE)
            
            #buttons
            back_button = Button(CENTER_X, 750, "BACK")
            highscore_buttons = pygame.sprite.GroupSingle(back_button)
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound)
                        self.state = "menu"
                
            #highscore sprites
            highscore_group = pygame.sprite.Group()
            hs_start_y = 300
            hs_rank_list = ["1ST", "2ND", "3RD", "4TH", "5TH"]
            hs_rank_length = 3
            hs_max_length = 8
           
            #initializing sprites with updated highscores and formatting textbox to align scores properly
            for hs in self.hs_list:
                curr_rank = hs_rank_list[0]
                hs_text = f"{curr_rank:<{hs_rank_length}}         {hs:>{hs_max_length}}"

                hs_textbox = Textbox(CENTER_X, hs_start_y, hs_text)
                highscore_group.add(hs_textbox)
                hs_start_y += 40
                hs_rank_list.pop(0)
            
            #update display
            self.screen.fill("black")
            highscore_title.draw_textbox(self.screen, "white", "black")
            highscore_buttons.update(self.screen, "black")
            

            for hs in highscore_group:
                hs.draw_textbox(self.screen, "white", "black")

            pygame.display.update()
                
    def gameloop(self):
        """
        displays and manages the game screen
        args: none
        return: None
        """
        has_collided = False
        
        #set background
        self.background = pygame.transform.scale(GAME_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))
        
        #music
        MUSIC_CHANNEL.play(SOUNDS.game_music, -1)

        while self.state == "game":            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    if not self.timer.mytime.paused:
                        self.timer.mytime.stop()
                    else:
                        self.timer.mytime.start()

            #initializing sprites (for restart)
            if self.timer.restarting:
                self.ship = Ship((SCREEN_W / 2, SCREEN_H - 50))
                self.myship = pygame.sprite.GroupSingle(self.ship)
            #restart
            if not self.timer.mytime.paused:
                #collision
                if pygame.sprite.spritecollide(self.ship, self.asteroids, False, pygame.sprite.collide_mask):
                    #reset all necessary variables
                    has_collided = True
                    self.last_scores.append(self.score.myscore)
                    print(f"Last scores: {self.last_scores}")  #debugging last scores
                    self.timer.mytime.stop()
                    self.asteroids.empty()
                    self.asteroid_last_spawn = 0
                    self.asteroid_fall_speed = INIT_FALL_SPEED
                    self.asteroid_stagger = ASTEROID_INIT_STAGGER
                    self.asteroid_speed_increase_cooldown = INIT_SPEED_INCREASE_COOLDOWN
                    self.asteroid_stagger_decrease_cooldown = INIT_STAGGER_DECREASE_COOLDOWN
                    self.myship.empty()
                    MUSIC_CHANNEL.stop()
                    GAME_SFX_CHANNEL.play(SOUNDS.collision_sound, 0)
                    pygame.time.wait(2000)
                    self.state = "game over"
            
                
                
                if not has_collided:
                    self.counters.update(self.screen)

                    #difficulty increase
                    speed_increase = math.floor(self.timer.mytime.get_time() / self.asteroid_speed_increase_cooldown) == 1
                    stagger_decrease = math.floor(self.timer.mytime.get_time() / self.asteroid_stagger_decrease_cooldown) == 1

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
                    if self.timer.mytime.get_time() - self.asteroid_last_spawn >= self.asteroid_stagger:
                        newasteroid = Asteroid((random.randint(0, SCREEN_W), 0))
                        self.asteroid_last_spawn = self.timer.mytime.get_time()
                        self.asteroids.add(newasteroid)
                        

                    for asteroid in self.asteroids:
                        asteroid.set_fall_speed(self.asteroid_fall_speed)

            #update screen
                self.screen.blit(self.background, (0, 0))
                self.myship.update()
                self.myship.draw(self.screen)
                self.asteroids.update()
                self.asteroids.draw(self.screen)
                self.counters.update(self.screen)

            else:
                pause = Textbox(CENTER_X, 200 , "PAUSED")
                resume_message = Textbox(CENTER_X, 400, "PRESS ESC TO RESUME")

                pause.draw_textbox(self.screen)
                resume_message.draw_textbox(self.screen)
            pygame.display.update()
            clock.tick(FRAME_RATE)

    def optionsloop(self):
        #music
        MUSIC_CHANNEL.play(SOUNDS.options_music, -1)

        while self.state == "options":
            #title
            title = Textbox(CENTER_X, OPTIONS_Y, "OPTIONS", "white")
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

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sfx_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        SOUNDS.toggle_sfx()
                    elif music_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        SOUNDS.toggle_music()
                        if SOUNDS.music_on:
                            MUSIC_CHANNEL.play(SOUNDS.options_music, -1)
                    elif back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        self.state = "menu"
            
            self.screen.fill("black")
            title.draw_textbox(self.screen, "white", "black")
            options_buttons.update(self.screen, "black")
            pygame.display.update()

    def gameoverloop(self):
        #music
        MUSIC_CHANNEL.stop()
        GAME_OVER_SFX_CHANNEL.play(SOUNDS.game_over_sound, 0)
        MUSIC_CHANNEL.play
        # background_image = END_BACKGROUND.convert_alpha()
        # self.background = pygame.transform.scale(background_image, (SCREEN_W, SCREEN_H))
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

            quit_button = Button(CENTER_X, PLAY_AGAIN_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, "QUIT")
            game_over_buttons.add(quit_button)
            num_buttons += 1

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.timer.restarting = True
                        self.timer.mytime.start()
                        self.score.reset()
                        self.state = "game"
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                    elif options_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.timer.restarting = True
                        self.state = "options"
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                    elif quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        BUTTON_CLICK_CHANNEL.play(SOUNDS.button_click_sound, 0)
                        pygame.quit()
                        sys.exit()
            
            game_over_textbox = Textbox(CENTER_X, GAME_OVER_Y, "OH NO! YOU EXPLODED!")
            game_over_textbox.set_font_size(50)

            # self.last_score = self.timer.myscore
            self.hs_added = False
            
            #update screen
            
            self.screen.fill("black")
            # self.screen.blit(self.background, (0, 0))
            for counter in self.counters:
                counter.draw_counter(self.screen)
            game_over_textbox.draw_textbox(self.screen, "white", "black")

            game_over_buttons.update(self.screen, BOX_COLOR)
            pygame.display.update()
