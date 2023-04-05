import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self,y_pos):
        # pasamos la primera imagen de BIRD=0 al padre (Obst) para iniciar el intercalado
        super().__init__(BIRD[0])
        self.rect.y = 250
        self.index = 0
        self.rect.y = y_pos

    
    def update(self,game_speed, obstacles):
        #se utilizar para actualizar la posicion y dectectar la colision
        super().update(game_speed, obstacles)
        # si el residuo del mutiplo de 5 al indice de la imagen es 0 entonces se inicia la condicion
        #    1%5 = 1 = True
        #    0%5 = 0 = False
        #cada 5 frames se imprime una u otra
        if self.index % 5==0:
            if self.image == BIRD[0]:
                self.image = BIRD[1]
            else:
                self.image = BIRD[0]
        self.index += 1
        
    
