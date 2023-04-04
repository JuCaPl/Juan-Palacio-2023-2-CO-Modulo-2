import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self,y_pos):
        # pasamos la primera imagen de BIRD=0
        super().__init__(BIRD[0])
        self.rect.y = 250
        self.index = 0
        self.rect.y = y_pos

    
    def update(self,game_speed, obstacles):
        super().update(game_speed, obstacles)
        if self.index % 5==0:
            if self.image == BIRD[0]:
                self.image = BIRD[1]
            else:
                self.image = BIRD[0]
        
        self.index += 1
        
    
