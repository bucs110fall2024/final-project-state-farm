import pygame, time
from src.textbox import Textbox

class NewTimer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.paused = True

    def pause(self):
        self.paused = not self.paused

    def start(self):
        if self.paused:
            self.start_time = time.time()
            self.paused = False
    
    def stop(self):
        if not self.paused:
            self.elapsed_time += time.time() - self.start_time
            self.paused = True
    
    def get_time(self):
        curr_time = self.elapsed_time
        if not self.paused:
            curr_time += time.time() - self.start_time
        return curr_time
    
    def convert_to_time_str(self):
        time_str = "TIME: " + self.get_time()
        return time_str