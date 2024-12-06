import pygame

from src.textbox import Textbox

class Timer(Textbox):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height, text)
        self.curr_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        self.minutes = 0
        self.seconds = 0
        self.paused = False
        self.color = "white"
        self.text = text

    def pause(self):
        self.paused = not self.paused
        
        if self.paused:
            self.curr_time = self.curr_time
            self.elapsed_time = self.elapsed_time + self.curr_time
        else:
            self.curr_time = pygame.time.get_ticks() + self.elapsed_time
        
    def start(self):
        self.paused = False
        self.curr_time = pygame.time.get_ticks()
        self.seconds = int((self.curr_time / 1000) % 60)
        self.minutes = int((self.curr_time / 60000))


    def stop(self):
        self.paused = True
        self.final_time = self.curr_time
        self.curr_time = self.resume_time = 0

    def draw_timer(self, screen):
        
        self.draw_textbox(screen, self.text, self.rect.center, True, self.color)


    def update(self, screen):
        self.start()
        self.draw_timer(screen)

