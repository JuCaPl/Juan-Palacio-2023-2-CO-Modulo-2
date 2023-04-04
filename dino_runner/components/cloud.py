import pygame
import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD,SCREEN_WIDTH


class Cloud:
    game_speed = 20

    def __init__(self):
        #      ancho de cuadro + un valor entre 10 y 100                  
        self.X = SCREEN_WIDTH + random.randint(1,500)
        self.Y = random.randint(5,100)
        self.image = CLOUD
        #            ancho de la imagen Cloud
        self.width = self.image.get_width()
        

    def update(self):
        # va ir al lado contrario(velocidad negativa)
        self.X -= self.game_speed
        # se imprime solo una vez la nube si y al estar en 0 se ejecuta esto y asi sucesivamente
        if self.X < -self.width:
            self.X = SCREEN_WIDTH + random.randint(1,100)
            self.Y = random.randint(5,200)

    def draw(self, SCREEN):
        SCREEN.blit(self.image,(self.X,self.Y))
