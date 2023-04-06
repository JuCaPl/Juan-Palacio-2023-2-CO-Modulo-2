import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.lifes import Life


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(150,250)
        self.duration= random.randint(3,5)
    
    def generate_power_up(self):
        power_up_classes = [Shield, Life]
        power_up_class = random.choice(power_up_classes)
        if power_up_class == Shield: # Si es un escudo, se generan coordenadas en la parte inferior de la pantalla
            power_up_x = random.randint(10, 3000)
            power_up_y = random.randint(200, 200)
        else: # Si es una vida, se generan coordenadas en la parte superior de la pantalla
            power_up_x = random.randint(10,4000)
            power_up_y = random.randint(310, 310)
        power_up = power_up_class(x=power_up_x, y=power_up_y)
        #self.when_appears += random.randint(150,250)
        self.power_ups.append(power_up)

    def update(self,game):
        if len(self.power_ups)==0 :
            power_up = self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration*1000)
                self.power_ups.remove(power_up)


    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
   
    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(150,250)


