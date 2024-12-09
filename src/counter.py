import math
from src.textbox import Textbox
from src.mytime import Time

class Counter(Textbox):
    def __init__(self, x, y, text, type):
        """
        Creates a modified version of a Textbox which contains a  
        """
        super().__init__(x, y, text)
        self.time = Time()

        self.restarting = False
        self.myscore = self.real_score = 0
        self.type = type

    def draw_counter(self, screen, text_color="white", boxed = False, box_color="Black"):
        """
        Draws the counter on the inputted screen with optional parameters for text and background colors.
        args: (Surface) screen, (color) text_color, (color) box_color
        return: None
        """
        self.draw_textbox(screen, text_color, boxed, box_color)
    
    def update(self, screen):
        """
        Updates the counter object and draws it on the screen parameter.
        args: (Surface) screen
        return: None
        """
        
        # resets both timer and score when restarting
        if self.restarting:
            self.reset()  #resets the timer and score
            self.time.start()  #restarts the timer
            self.restarting = False  #ensures the timer and score only reset once at restart

        #update the text based on type of counter
        if self.type == "timer":
            self.text = self.time.convert_time_to_str()  #sets text to time
        elif self.type == "score":
            self.calculate_score()  #calculates score based on the current time
            self.text = self.convert_score_to_str()  #sets text to score

        #draws the counter (timer/score)
        self.draw_counter(screen)
    
    def calculate_score(self):
        """
        Calculates the current score.
        args: None
        return: None
        """
        curr_time = self.time.get_time()  #gets the current time in seconds
        pts_per_update = (1 / math.pow(1000, ((curr_time + 0.000001))))  #sets point increment per update; avoids div by 0 error
        self.real_score += pts_per_update  #adds points per update
        self.myscore = math.floor(self.real_score)  #converts score to integer
    
    def convert_score_to_str(self):
        """
        Converts the current score to a string.
        args: None
        return: (str) score_str
        """
        score_str = "SCORE: " + f"{self.myscore:08}"
        return score_str
    
    def reset(self):
        self.time.reset()
        if self.type == "score":
            self.real_score = 0
            self.myscore = 0
            self.text = "SCORE: 00000000"