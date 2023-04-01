import random

from dino_runner.components.obstacles.obstacle import Obstacle



class Cactus (Obstacle):
    
    def _init_(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325