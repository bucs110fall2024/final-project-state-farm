import pygame, sys, time

class MyTime:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.paused = True

    def start(self):
        if self.paused:
            self.start_time = time.time()
            self.paused = False
    
    def stop(self):
        if not self.paused:
            self.elapsed_time += time.time() - self.start_time
            self.paused = True

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.paused = True
    
    def get_time(self):
        curr_time = self.elapsed_time
        if not self.paused:
            curr_time += time.time() - self.start_time
        return curr_time
    
    def convert_time_to_str(self):
        seconds = int(self.get_time() % 60)
        minutes = int(self.get_time() / 60)
        time_str = "TIME: " + f"{minutes:02}:{seconds:02}"
        return time_str