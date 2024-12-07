import pygame

FONT_NAME = "assets/PublicPixel-rv0pA.ttf"
BOX_COLOR = (7, 7, 36)

class Textbox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.font_size = 20
        self.x = x
        self.y = y
    
        self.text = text
        self.font = pygame.font.Font(FONT_NAME, self.font_size)

    def set_font_size(self, font_size):
        self.font = pygame.font.Font(FONT_NAME, font_size)
    
    def draw_textbox(self, screen, text, center, text_color = "white", box_color = BOX_COLOR):
            """
            Draws a text string with inputted font size in a rect defined by its center coordinate
            args: (str) text, (int) size, 
            return: None
            """
            textbox = self.font.render(text, True, text_color)
            textbox_rect = textbox.get_rect(center = (center))
            self.image.fill(box_color)
            screen.blit(self.image, self.rect)
            screen.blit(textbox, textbox_rect)