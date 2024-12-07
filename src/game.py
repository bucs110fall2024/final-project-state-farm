import pygame
import sys
import random
import math
from src.ship import Ship
from src.asteroid import Asteroid
from src.textbox import Textbox, BOX_COLOR
from src.timer import Timer
from src.button import Button
from src.sound import Sound

SCREEN_W = 1000
SCREEN_H = 800
START_Y = PLAY_AGAIN_Y = 500
CENTER_X = 500
BUTTON_W = 200
BUTTON_H = MENU_BUTTON_Y_INCREMENT = 80
TITLE_Y = 100
TITLE_W = 300
TITLE_H = 100
TITLE_SIZE = 50
TIMER_X = 110
TIMER_Y = 10
TIMER_W = 2 * TIMER_X
TIMER_H = 2 * TIMER_Y
TIMER_INIT_TEXT = "Time: 00:00"
GAME_OVER_Y = 200
GAME_OVER_W = 1000
GAME_OVER_H = 50
ASTEROID_INIT_NUM = 4
GAME_BACKGROUND = pygame.image.load("assets/game_background.png")
END_BACKGROUND = pygame.image.load("assets/end_background.png")

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
        self.asteroid_fall_speed = 3
        self.asteroid_max_num = ASTEROID_INIT_NUM
        self.asteroid_speed_increase_cooldown = 20000
        self.asteroid_max_num_increase_cooldown = 40000
        self.asteroid_stagger = 800
        self.asteroid_stagger_decrease_cooldown = 15000
        self.asteroid_last_spawn = 0

        self.timer = Timer(TIMER_X, TIMER_Y, TIMER_W, TIMER_H, TIMER_INIT_TEXT)
        self.mytimer = pygame.sprite.GroupSingle(self.timer)

        self.sounds = Sound()

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

        while self.state == "menu":
            #title
            title = Textbox(CENTER_X, TITLE_Y, TITLE_W, TITLE_H, "SPACE ROCKS")
            title.set_font_size(TITLE_SIZE)
            # title.draw_textbox(self.screen, title.text, title.rect.center, "white", "black")

            #buttons

            menu_buttons = pygame.sprite.Group()
            num_buttons = 0

            start_button = Button(CENTER_X, START_Y, BUTTON_W, BUTTON_H, "START")
            menu_buttons.add(start_button)
            num_buttons += 1

            options_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "OPTIONS")
            menu_buttons.add(options_button)
            num_buttons += 1

            quit_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "QUIT")
            menu_buttons.add(quit_button)
            num_buttons += 1


            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.state = "game"
                    elif options_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.state = "options"
                    elif quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
        
            #update screen
            self.screen.fill("black")
            title.draw_textbox(self.screen, title.text, title.rect.center, "white", "black")
            menu_buttons.update(self.screen, "black")
            pygame.display.update()
        
    def gameloop(self):
        """
        displays and manages the game screen
        args: none
        return: None
        """
        while self.state == "game":
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # keys = pygame.key.get_pressed()
                # if event.type == pygame.KEYDOWN:
                #     if keys[pygame.K_ESCAPE]:
                #         self.timer.pause()
                #         if not self.timer.paused:
                #             self.timer.start_time = pygame.time.get_ticks()

            # if not self.timer.paused:

            #initializing sprites (for restart)
            self.timer.elapsed_time -= self.timer.final_time
            self.myship = pygame.sprite.GroupSingle(self.ship)



            #difficulty increase
            speed_increase = math.floor(self.timer.elapsed_time / self.asteroid_speed_increase_cooldown) == 1
            max_num_increase = math.floor(self.timer.elapsed_time / self.asteroid_max_num_increase_cooldown) == 1
            stagger_decrease = math.floor(self.timer.elapsed_time / self.asteroid_stagger_decrease_cooldown) == 1

            if speed_increase and self.asteroid_fall_speed <= 10:
                self.asteroid_fall_speed += 1
                self.asteroid_speed_increase_cooldown += 20000
            if max_num_increase and self.asteroid_max_num <= 8:
                self.asteroid_max_num += 1
                self.asteroid_max_num_increase_cooldown += 40000
            if stagger_decrease and self.asteroid_stagger_decrease_cooldown >= 400:
                self.asteroid_stagger -= 50

            for asteroid in self.asteroids:
                asteroid.set_fall_speed(self.asteroid_fall_speed)
                
            #collision
            if pygame.sprite.spritecollide(self.ship, self.asteroids, False, pygame.sprite.collide_mask):
                #without lives
                self.timer.stop()
                
                self.asteroids.empty()
                self.myship.empty()
                self.state = "game over"

                #with lives
                    
                # self.timer.pause()
                # pygame.time.delay(1500)
                # asteroid.kill()
                # self.timer.pause() ## This would be for implementing a short pause after being hit, and will only be
                #                     ## utilized if I were to implement multiple lives/hp for the ship
                # if self.ship.lives > 0:
                #     self.ship.lives -= 1
                #     self.asteroids.add(self.asteroid) ## unsure if this line is necessary

                # else:
                #     self.state = "game over"
            
            #updating ship
            # self.myship = pygame.sprite.GroupSingle(self.ship)
            
            #updating asteroids
            if len(self.asteroids) < self.asteroid_max_num:
                newasteroid = Asteroid((random.randint(0, SCREEN_W), 0))
                #asteroid spawning cooldown
                if pygame.time.get_ticks() - self.asteroid_last_spawn > self.asteroid_stagger:
                    self.asteroid_last_spawn = pygame.time.get_ticks()
                    self.asteroids.add(newasteroid)
                
                # if speed_increase and self.asteroid_fall_speed <= 10:
                #     self.asteroid_fall_speed += 1
                #     self.asteroid_speed_increase_cooldown += 20000
                # if max_num_increase and self.asteroid_max_num <= 8:
                #     self.asteroid_max_num += 1
                #     self.asteroid_max_num_increase_cooldown += 40000

            #set background
            self.background = pygame.transform.scale(GAME_BACKGROUND.convert_alpha(), (SCREEN_W, SCREEN_H))
            
            #update screen
            self.screen.blit(self.background, (0, 0))
            self.myship.update()
            self.myship.draw(self.screen)
            self.asteroids.update()
            self.asteroids.draw(self.screen)
            self.mytimer.update(self.screen)

            pygame.display.update()
            clock.tick(120)



    def optionsloop(self):
            
            options_buttons = pygame.sprite.Group()
            num_buttons = 0

            sfx_button = Button(CENTER_X, START_Y, BUTTON_W, BUTTON_H, "SFX")
            options_buttons.add(sfx_button)
            num_buttons += 1

            music_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "MUSIC")
            options_buttons.add(music_button)
            num_buttons += 1

            back_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "BACK TO MENU")
            options_buttons.add(back_button)
            num_buttons += 1

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sfx_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.sounds.toggle_sfx()
                        pass
                    elif music_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.sounds.toggle_music()
                        pass
                    elif back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.state = "menu"
            
            self.screen.fill("black")
            options_buttons.update(self.screen, "black")
            pygame.display.update()

    def gameoverloop(self):
        while self.state == "game over":
            #background
            self.background = pygame.transform.scale(END_BACKGROUND, (SCREEN_W, SCREEN_H))
            
            #buttons

            game_over_buttons = pygame.sprite.Group()
            num_buttons = 0

            play_again_button = Button(CENTER_X, PLAY_AGAIN_Y, BUTTON_W, BUTTON_H, "PLAY AGAIN")
            game_over_buttons.add(play_again_button)
            num_buttons += 1

            options_button = Button(CENTER_X, PLAY_AGAIN_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "OPTIONS")
            game_over_buttons.add(options_button)
            num_buttons += 1

            quit_button = Button(CENTER_X, PLAY_AGAIN_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "QUIT")
            game_over_buttons.add(quit_button)
            num_buttons += 1

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.state = "game"
                    elif options_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.state = "options"
                    elif quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
            
            game_over_textbox = Textbox(CENTER_X, GAME_OVER_Y, GAME_OVER_W, GAME_OVER_H, "OH NO! YOU EXPLODED!")
            game_over_textbox.set_font_size(50)

            #update screen
            
            self.screen.fill("black")
            self.screen.blit(self.background, (0, 0))
            self.timer.draw_timer(self.screen, True)
            game_over_textbox.draw_textbox(self.screen, game_over_textbox.text, game_over_textbox.rect.center, "white", "black")
            game_over_buttons.update(self.screen, BOX_COLOR)
            pygame.display.update()
