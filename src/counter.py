# import pygame, time

# from src.textbox import Textbox, BOX_COLOR

# class Timer(Textbox):
#     def __init__(self, x, y, width, height, text):
#         super().__init__(x, y, width, height, text)
#         self.start_time = pygame.time.get_ticks()
#         self.elapsed_time = 0
#         self.paused = False
#         self.color = "white"
#         self.text = text
#         self.final_time = 0
#         self.end_menu_time = 0

#     def pause(self):
#         self.paused = not self.paused

#     def convert_to_min_and_sec(self, time):
#         seconds = int((time / 1000) % 60)
#         minutes = int((time / 60000))

#         min_and_sec_str = f"{minutes:02}:{seconds:02}"
#         return min_and_sec_str

        
#     def update_time(self):
#         if not self.paused:
#             self.elapsed_time = pygame.time.get_ticks() - self.start_time
#         else:
#             self.elapsed_time = 0
        
#         # self.seconds = int((self.elapsed_time / 1000) % 60)
#         # self.minutes = int((self.elapsed_time / 60000))

#         time_str = "TIME: " + self.convert_to_min_and_sec(self.elapsed_time - self.end_menu_time)
#         self.text = time_str

#     def stop(self):
#         # self.paused = True
#         self.final_time = self.elapsed_time
#         # self.elapsed_time = 0
#         self.end_menu_time = pygame.time.get_ticks() - self.final_time

#     def start(self):
#         self.paused = False
#         self.elapsed_time = 0
#         self.start_time -= self.start_time

#     def draw_timer(self, screen, final = None):
#         if final:
#             final_time_str = self.convert_to_min_and_sec(self.final_time)
#             self.text = "TIME: " + final_time_str
#         self.draw_textbox(screen, self.text, self.rect.center, self.color, BOX_COLOR)


#     def update(self, screen):
#         self.update_time()
#         self.draw_timer(screen)
        
    
#     class Score(Textbox):
#         def __init__(self, x, y, width, height, text):
#             super().__init__(x, y, width, height, text)



import math
from src.textbox import Textbox
from src.mytime import MyTime

# class Timer(Textbox):
#     def __init__(self, x, y, width, height, text):
#         super().__init__(x, y, width, height, text)
#         self.mytime = MyTime()
#         self.text_color = "white"
#         self.restarting = False

#     def draw_timer(self, screen):
#         self.draw_textbox(screen, self.text, self.rect.center, self.text_color, BOX_COLOR)
    
#     def update(self, screen):

#         if self.restarting:
#             self.mytime.reset()
#             self.mytime.start()
#             self.restarting = False

#         # self.mytime.set_str()
#         # self.text = self.mytime.time_str
#         self.text = self.mytime.convert_time_to_str()
#         self.draw_timer(screen)


class Counter(Textbox):
    def __init__(self, x, y, text, type):
        super().__init__(x, y, text)
        self.mytime = MyTime()
        # self.set_text_color(text_color)
        self.restarting = False
        self.myscore = self.real_score = 0
        self.last_score = 0
        self.type = type

    def draw_counter(self, screen, text_color = "white", box_color = "Black"):
        self.draw_textbox(screen, text_color, box_color)
    
    def update(self, screen):
        if self.restarting:
            self.mytime.reset()
            self.mytime.start()

            self.last_score = self.real_score
            self.real_score = 0
            self.restarting = False

        if self.type == "timer":
            self.text = self.mytime.convert_time_to_str()
        elif self.type == "score":
            self.calculate_score()
            self.text = self.convert_score_to_str()
        self.draw_counter(screen)
    
    def calculate_score(self):
        curr_time = self.mytime.get_time()
        pts_per_update = (1 / math.pow(1000, ((curr_time + 0.000001)))) #avoid div. by 0 error
        self.real_score += pts_per_update
        self.myscore = int(self.real_score)
    
    def convert_score_to_str(self):
        score_str = "SCORE: " + f"{self.myscore:08}"
        return score_str
        


