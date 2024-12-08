import pygame
from src.textbox import Textbox

class Highscore(Textbox):
    def __init__(self, x, y, text, score):
        super().__init__(x, y, text)
        self.score = score

    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score = score

    