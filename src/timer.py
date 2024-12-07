import pygame, time

from src.textbox import Textbox, BOX_COLOR

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
            
