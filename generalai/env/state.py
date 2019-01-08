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
    
    def step(self, action):
        self.action(action)
        self.state = DataGrabber.get_screen_array(40, 0, 800, 640)
        self.next_state = self.state
        self.reward = self.get_reward()
        self.done = self.get_done()
        return self.next_state, self.reward, self.done

    def render(self):
        pass

    def configure(self):
        pass

    def actions(self, action):
        DataGrabber.actions(action)

    
    def get_reward(self):
    
        return self.reward
    
    def get_done(self):
        
        return self.done

    

