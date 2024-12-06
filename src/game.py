import pygame
import sys
import random
from src.ship import Ship
from src.asteroid import Asteroid
from src.textbox import Textbox
from src.timer import Timer
from src.button import Button

SCREEN_W = 1000
SCREEN_H = 800
START_Y = 500
CENTER_X = 500
BUTTON_W = 200
BUTTON_H = MENU_BUTTON_Y_INCREMENT = 80
BUTTON_FS = 20
TITLE_Y = 100
TITLE_W = 300
TITLE_H = 100
TITLE_SIZE = 50
TIMER_X = 120
TIMER_Y = 30
TIMER_W = 180
TIMER_H = 60
TIMER_FS = 20
TIMER_INIT_TEXT = "Time: 00:00"

clock = pygame.time.Clock()

class Game:
    def __init__(self):
        #screen & display
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

        #background
        self.background = pygame.transform.scale(pygame.image.load("assets/background.png"), \
            (SCREEN_W, SCREEN_H))
        #sprites
        self.ship = Ship((SCREEN_W / 2, SCREEN_H))
        self.myship = pygame.sprite.GroupSingle(self.ship)

        self.asteroids = pygame.sprite.Group()
        self.asteroid_template = Asteroid((random.randint(0, SCREEN_W), 0))
        # for i in range(self.asteroid.max_num):
        #     self.asteroid = Asteroid((random.randint(0, SCREEN_W), 0))
        #     self.asteroids.add(self.asteroid)

        self.timer = Timer(TIMER_X, TIMER_Y, TIMER_W, TIMER_H, TIMER_INIT_TEXT)
        self.mytimer = pygame.sprite.GroupSingle(self.timer)

        #gamestate
        self.state = "menu"

    def mainloop(self):
        
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
        while self.state == "menu":
            #title
            title = Textbox(CENTER_X, TITLE_Y, TITLE_W, TITLE_H, "SPACE ROCKS")
            title.set_font_size(TITLE_SIZE)
            title.draw_textbox(self.screen, title.text, title.rect.center, "white")

            #buttons

            buttons = pygame.sprite.Group()
            num_buttons = 0

            start_button = Button(CENTER_X, START_Y, BUTTON_W, BUTTON_H, "START")
            buttons.add(start_button)
            num_buttons += 1

            options_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "OPTIONS")
            buttons.add(options_button)
            num_buttons += 1

            quit_button = Button(CENTER_X, START_Y + MENU_BUTTON_Y_INCREMENT * num_buttons, BUTTON_W, BUTTON_H, "QUIT")
            buttons.add(quit_button)
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
        
            buttons.update(self.screen)


            pygame.display.update()
        
    def gameloop(self):
        while self.state == "game":
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_ESCAPE]:
                        self.timer.pause()

            if not self.timer.paused:
                #background
                self.screen.blit(self.background, (0, 0))
                #timer
                self.timer.update(self.screen)
                clock.tick(120)

                #player movement
                self.ship.update()

                #difficulty increase
                # if self.timer.curr_time > 

                #asteroids
                for i in range(self.asteroid_template.max_num):
                    self.asteroid = self.asteroid_template
                    self.asteroids.add(self.asteroid)
                
                #collision
                for asteroid in self.asteroids:
                    asteroid.update()
                    if self.ship.hitbox.colliderect(asteroid.hitbox):
                        asteroid.die()
                        self.timer.pause()
                        pygame.time.delay(1500)
                        self.timer.resume()
                        self.asteroids.add(self.asteroid)
                


                
            

                
            
            pygame.display.update()    


    def optionsloop(self):
        pass

    def gameoverloop(self):
        pass

