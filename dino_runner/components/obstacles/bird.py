import pygame
import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import BIRD,SCREEN_WIDTH


class Bird():
    game_speed = 20

    def __init__(self):
        self.image = BIRD[0]
        self.x = SCREEN_WIDTH + random.randint(1,10)
        self.y = random.randint(250,300)
        self.step_index = 0
        self.bird_rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def update(self):
        self.x -= self.game_speed
        if self.step_index >= 10:
            self.step_index = 0
        self.fly()

    def fly(self):
        if self.step_index % 5 == 0:
            self.image = BIRD[1] if self.image == BIRD[0] else BIRD[0]

        if self.x < 0:
            self.x = SCREEN_WIDTH + random.randint(1,10)
            self.y = random.randint(250,308)
        
        # Actualizar la posición del rectángulo de colisión
        self.bird_rect.topleft = (self.x, self.y)
        
        self.step_index += 1

    def draw(self,screen):
        screen.blit(self.image,(self.x ,self.y))
        



