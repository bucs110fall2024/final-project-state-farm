import pygame
from src.textbox import Textbox

# class Button(Textbox):
#     def __init__(self, x, y, width, height, text):
#         super().__init__(x, y, width, height, text)
#         self.color = self.text_color = "white"
#         self.hov_color = (255, 234, 0)
#         self.hover_sound = pygame.mixer.Sound("assets/button_hover.mp3")
#         self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
#         self.was_unhovered = True

#     def set_hovered(self):
#         color = self.text_color
#         if self.hovered:
#             color = self.hov_color
#             if self.was_unhovered:
#                 pygame.mixer.Channel(0).play(self.hover_sound, 0)
#             self.was_unhovered = False
#         else:
#             self.was_unhovered = True
#         self.color = color
    
#     def draw_button(self, screen, box_color):
#         self.draw_textbox(screen, self.text, self.rect.center, self.color, box_color)
    
#     def update(self, screen, box_color):
#         self.set_hovered()
#         self.draw_button(screen, box_color)
#         if self.hovered:
#             self.was_unhovered = False


class Button(Textbox):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)
        self.color = self.text_color = "white"
        self.hov_color = (255, 234, 0)
        self.hover_sound = pygame.mixer.Sound("assets/button_hover.mp3")
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        self.was_unhovered = True

    def set_hovered(self):
        color = self.text_color
        if self.hovered:
            color = self.hov_color
        #     if self.was_unhovered:
        #         pygame.mixer.Channel(0).play(self.hover_sound, 0)
        #         self.was_unhovered = False
        # else:
        #     self.was_unhovered = True
        self.color = color
    
    def draw_button(self, screen, box_color):
        self.draw_textbox(screen, self.color, box_color)
    
    def update(self, screen, box_color):
        self.set_hovered()
        self.draw_button(screen, box_color)
        if self.hovered:
            self.was_unhovered = False