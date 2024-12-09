import pygame
from src.textbox import Textbox
from src.sound import Sound, BUTTON_CHANNEL

SOUNDS = Sound()

class Button(Textbox):
    def __init__(self, x, y, text):
        """
        Creates a Button as a modified version of a Textbox which can be hovered and clicked.
        args: (int) x, (int) y, (str) text
        return: None
        """
        super().__init__(x, y, text)
        self.color = self.text_color = "white"
        self.hov_color = (255, 234, 0)
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())

    def set_hovered(self):
        """
        Updates the button depending on if it is currently hovered.
        args: None
        return: None
        """
        now_hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        self.color = self.text_color
        if now_hovered:
            if not self.hovered:
                BUTTON_CHANNEL.play(SOUNDS.button_hover_sound, 0)
            self.color = self.hov_color
    
    def is_clicked(self, event):
        """
        Checks if the button is clicked. If it is, plays the button click sound and returns True.
        args: (Event) event
        return: (bool) is_clicked
        """
        is_clicked = False
        if self.hovered and event.type == pygame.MOUSEBUTTONDOWN:
            is_clicked = True
            BUTTON_CHANNEL.play(SOUNDS.button_click_sound, 0)
        return is_clicked
        
    def draw_button(self, screen, boxed = False, box_color = "black"):
        """
        Draws the Button.
        args: (Surface) screen: Surface to be drawn on, (bool) boxed, (color) box_color
        """
        self.draw_textbox(screen, self.color, boxed, box_color)
    
    def update(self, screen, boxed = False, box_color = "black"):
        self.set_hovered()
        self.draw_button(screen, boxed, box_color)