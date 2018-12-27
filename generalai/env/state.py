import numpy as np
from ..common import DataGrabber
from ..common import Controller

class State():
    def __init__(self):
        self.love = "Ramona"
        self.done = False
        self.state = 0

    def reset(self):
        self.state = DataGrabber.get_screen_array(40, 0, 800, 640)
        return self.state
    
    def step(self):
        self.state = DataGrabber.get_screen_array(40, 0, 800, 640)
        self.next_state = self.state
        return self.next_state, self.reward, self.done

    def render(self):
        pass

    def configure(self):
        pass

    

