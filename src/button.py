import pygame
from src.textbox import Textbox

class Button(Textbox):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height, text)
        self.color = self.text_color = "white"
        self.hov_color = (255, 234, 0)

    def set_color(self):
        color = self.text_color
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = self.hov_color

        self.color = color
    
    def draw_button(self, screen):
        self.draw_textbox(screen, self.text, self.rect.center, self.color)
    
    def update(self, screen):
        self.set_color()
        self.draw_button(screen)