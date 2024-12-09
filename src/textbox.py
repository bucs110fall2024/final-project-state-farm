import pygame

FONT_NAME = "assets/PublicPixel-rv0pA.ttf"

class Textbox(pygame.sprite.Sprite):
    def __init__(self, x, y, text, text_color = "white", box_color = "black", width = None, height = None):
        """
        Creates a textbox which can be displayed.
        args: (int) x, (int) y, (str) text, (color) text_color, (color) box_color, (int) width, (int) height
        return: None
        """
        super().__init__()
        self.font_size = 20
        self.font = pygame.font.Font(FONT_NAME, self.font_size)
        self.x = x
        self.y = y
        self.text = text
        self.text_color = text_color
        self.box_color = box_color

        if width != None and height != None:
            self.image = pygame.Surface((width, height))
            self.rect = self.image.get_rect(center = (x, y)) 
        else:
            self.image = self.font.render(self.text, True, text_color)
            self.rect = self.image.get_rect(center=(x, y))

    def set_font_size(self, font_size):
        """
        Changes the font size of the Textbox to the inputted parameter.
        args: (int) font_size
        return: None
        """
        self.font = pygame.font.Font(FONT_NAME, font_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def set_text_color(self, text_color):
        """
        Changes the text color of the Textbox to the inputted parameter.
        args: (color) text_color
        return: None
        """
        self.image = self.font.render(self.text, True, text_color)
        self.text_color = text_color
    
    def set_text(self, text):
        """
        Changes the text of the Textbox to the inputted parameter.
        args: (str) text
        return: None
        """
        self.image = self.font.render(text, True, self.text_color)
        self.text = text
    
    def draw_textbox(self, screen, text_color = "white", boxed = False, box_color = "black"):
            """
            Draws a textbox.
            args: (Surface) screen, (str) text, (color) text_color, (bool) boxed, (color) box_color)
            return: None
            """
            self.set_text_color(text_color)
            if boxed:
                bg = pygame.Surface((self.rect.width, self.rect.height))
                bg.fill(box_color)
                screen.blit(bg, self.rect)
            screen.blit(self.image, self.rect)

    def update(self, screen, text_color = "white", boxed = False, box_color = "black"):
         """
         Runs the draw_textbox method.
         args: (Surface) screen, (str) text, (xolor) text_color, (color) box_color
         return: None
         """
         self.draw_textbox(screen, text_color, boxed, box_color)