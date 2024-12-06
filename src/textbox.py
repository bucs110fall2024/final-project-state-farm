import pygame

FONT_NAME = "assets/PublicPixel-rv0pA.ttf"

class Textbox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.font_size = 20
        self.x = x
        self.y = y
    
        self.text = text
        self.font = pygame.font.Font(FONT_NAME, self.font_size)

    def set_font_size(self, font_size):
        self.font = pygame.font.Font(FONT_NAME, font_size)
    
    def draw_textbox(self, screen, text, center, color = "white"):
            """
            Draws a text string with inputted font size in a rect defined by its center coordinate
            args: (str) text, (int) size, 
            return: None
            """
            textbox = self.font.render(text, True, color)
            textbox_rect = textbox.get_rect(center = (center))
            self.image.fill("black")
            screen.blit(textbox, textbox_rect)