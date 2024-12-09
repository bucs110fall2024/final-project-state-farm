import time

class Time:
    def __init__(self):
        """
        Creates a Time object which manages all time-based information for the game.
        args: None
        return: None
        """
        self.start_time = None
        self.elapsed_time = 0
        self.paused = True

    def start(self):
        """
        Starts the timer.
        args: None
        return: None
        """
        if self.paused:
            self.start_time = time.time()
            self.paused = False
    
    def stop(self):
        """
        Stops the timer.
        args: None
        return: None
        """
        if not self.paused:
            self.elapsed_time += time.time() - self.start_time
            self.paused = True

    def reset(self):
        """
        Resets the timer.
        args: None
        return: None
        """
        self.start_time = None
        self.elapsed_time = 0
        self.paused = True
    
    def get_time(self):
        """
        Returns the current time.
        args: None
        return: (float) curr_time
        """
        curr_time = self.elapsed_time
        if not self.paused:
            curr_time += time.time() - self.start_time
        return curr_time
    
    def convert_time_to_str(self):
        """
        Converts the current time returned by the get_time() method into a string formatted into minutes and seconds.
        args: None
        return: (str) time_str
        """
        seconds = int(self.get_time() % 60)
        minutes = int(self.get_time() / 60)
        time_str = "TIME: " + f"{minutes:02}:{seconds:02}"
        return time_str