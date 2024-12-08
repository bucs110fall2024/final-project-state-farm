import pygame

FONT_NAME = "assets/PublicPixel-rv0pA.ttf"
BOX_COLOR = (7, 7, 36)

# class Textbox(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height, text):
#         super().__init__()
#         self.image = pygame.Surface((width, height))
#         self.rect = self.image.get_rect(center=(x, y))
#         self.font_size = 20
#         self.x = x
#         self.y = y
    
#         self.text = text
#         self.font = pygame.font.Font(FONT_NAME, self.font_size)

#     def set_font_size(self, font_size):
#         self.font = pygame.font.Font(FONT_NAME, font_size)
    
#     def draw_textbox(self, screen, text, center, text_color = "white", box_color = BOX_COLOR):
#             """
#             Draws a text string with inputted font size in a rect defined by its center coordinate
#             args: (str) text, (int) size, 
#             return: None
#             """
#             textbox = self.font.render(text, True, text_color)
#             textbox_rect = textbox.get_rect(center = (center))
#             self.image.fill(box_color)
#             screen.blit(self.image, self.rect)
#             screen.blit(textbox, textbox_rect)

class Textbox(pygame.sprite.Sprite):
    def __init__(self, x, y, text, text_color = "white", width = None, height = None):
        super().__init__()
        self.font_size = 20
        self.font = pygame.font.Font(FONT_NAME, self.font_size)
        self.x = x
        self.y = y
        self.text = text
        self.text_color = text_color
        if width != None and height != None:
            self.image = pygame.Surface((width, height))
            self.rect = self.image.get_rect(center = (x, y))
        
        else:
            self.image = self.font.render(self.text, True, "white")
            self.rect = self.image.get_rect(center=(x, y))

    def set_font_size(self, font_size):
        self.font = pygame.font.Font(FONT_NAME, font_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def set_text_color(self, text_color):
        self.image = self.font.render(self.text, True, text_color)
        # self.text_color = text_color
    
    def set_text(self, text):
        self.image = self.font.render(text, True, self.text_color)
        self.text = text
    
    def draw_textbox(self, screen, text_color = "white", box_color = BOX_COLOR):
            """
            Draws a textbox.
            args: (Surface) screen, (str) text, (color) text_color, (color) box_color) 
            return: None
            """
            self.set_text_color(text_color)
            # textbox = self.image
            # textbox_rect = textbox.get_rect(center = (self.rect.center))
            bg = pygame.Surface((self.rect.width, self.rect.height))
            # bg_rect = self.rect
            bg.fill(box_color)
            screen.blit(bg, self.rect)
            screen.blit(self.image, self.rect)