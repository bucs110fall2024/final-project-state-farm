import pygame

from src.textbox import Textbox, BOX_COLOR

class Timer(Textbox):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height, text)
        self.start_time = pygame.time.get_ticks()
        # self.elapsed_time = 0
        # self.minutes = 0
        # self.seconds = 0
        self.paused = False
        self.color = "white"
        self.text = text

    def pause(self):
        self.paused = not self.paused
        
        # if self.paused:
        #     self.curr_time = self.curr_time
        #     self.elapsed_time = self.elapsed_time + self.curr_time
        # else:
        #     self.elapsed_time = pygame.time.get_ticks() - self.start_time()
        
    def update_time(self):
        if not self.paused:
            self.elapsed_time = pygame.time.get_ticks() - self.start_time
        else:
            self.elapsed_time = 0
        
        self.seconds = int((self.elapsed_time / 1000) % 60)
        self.minutes = int((self.elapsed_time / 60000))

        time_str = "TIME: " + f"{self.minutes:02}:{self.seconds:02}"
        self.text = time_str

    
    # def start(self):
    #     self.paused = False
    #     # self.curr_time = pygame.time.get_ticks()
    #     self.seconds = int((self.elapsed_time / 1000) % 60)
    #     self.minutes = int((self.elapsed_time / 60000))

    # def update_text(self):
    #     time_str = "TIME: " + f"{self.minutes:02}:{self.seconds:02}"
    #     self.text = time_str

    def stop(self):
        self.paused = True
        self.final_time = self.curr_time
        self.curr_time = self.elapsed_time = 0

    def draw_timer(self, screen):
        self.draw_textbox(screen, self.text, self.rect.center, self.color, BOX_COLOR)

    def update(self, screen):
        self.update_time()
        self.draw_timer(screen)