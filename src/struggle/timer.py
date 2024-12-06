import pygame

class Timer:
    def __init__(self):
        self.curr_time = 0
        self.resume_time = 0
        self.minutes = 0
        self.seconds = 0
        self.paused = True

    def pause(self):
        self.paused = True
        self.curr_time = self.curr_time
        self.resume_time = self.curr_time
    
    def resume(self):
        self.paused = False
        self.curr_time = pygame.time.get_ticks() + self.resume_time
        
    def start(self):
        self.paused = False
        self.curr_time = pygame.time.get_ticks()
        self.seconds = int((self.curr_time / 1000) % 60)
        self.minutes = int((self.curr_time / 60000))

    # def get_minutes(self):
    #     return self.minutes

    # def get_seconds(self):
    #     return self.seconds
    
    def get_str(self):
        time_str = "TIME: " + f"{self.minutes:02}:{self.seconds:02}"
        return time_str
