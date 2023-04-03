import pygame
import random
from pygame.sprite import Sprite


from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


def detect_collision(rect1, rect2):
        if rect1.x < rect2.x  and rect1.x  > rect2.x and rect1.y < rect2.y  and rect1.y  > rect2.y:
            return True
        else:
            return False


class Obstacle(): 

    def __init__(self):
        self.cactus = Cactus()
        self.bird = Bird()
        self.player = Dinosaur()

    def update(self): 
         pass#pygame.draw.rect(screen,(255,0,0),player.dino_rect,2)
    

    def draw(self,screen):
        if detect_collision(self.player.dino_rect,self.cactus.cactus_rect):
           pygame.draw.rect(screen,(255,0,0),self.player.dino_rect,2)