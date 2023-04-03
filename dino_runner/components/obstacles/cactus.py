import pygame
import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import SMALL_CACTUS,SCREEN_WIDTH,LARGE_CACTUS




class Cactus():
    game_speed = 20

    def __init__(self):
        CACTUS = random.choice([SMALL_CACTUS,LARGE_CACTUS])
        self.image = CACTUS[0]
        self.cactus_rect = self.image.get_rect()
        self.cactus_rect.x = SCREEN_WIDTH + random.randint(1,2)
        if CACTUS == SMALL_CACTUS:
            self.cactus_rect.y = 320
        elif CACTUS == LARGE_CACTUS:
            self.cactus_rect.y = 300
        self.type = random.randint(0, 2)
        self.image = CACTUS[self.type]
        self.width = self.image.get_width()
  
    def update(self):
        self.cactus_rect.x -= self.game_speed
        if self.cactus_rect.x < -self.width:
            CACTUS = random.choice([SMALL_CACTUS,LARGE_CACTUS])
            self.cactus_rect.x = SCREEN_WIDTH + random.randint(1,2)
            if CACTUS == SMALL_CACTUS:
                self.cactus_rect.y = 320
            elif CACTUS == LARGE_CACTUS:
                self.cactus_rect.y = 300
            self.type = random.randint(0, 2)
            self.image = CACTUS[self.type]
        

    def draw(self,screen):
        screen.blit(self.image,(self.cactus_rect.x ,self.cactus_rect.y))
       





class Cactus_L():
    game_speed = 20

    def __init__(self):
        self.image = LARGE_CACTUS[0]
        self.cactus_rect = self.image.get_rect()
        self.cactus_rect.x = SCREEN_WIDTH + random.randint(5,50)
        self.cactus_rect.y = 300
        self.type = random.randint(0, 2)
        self.image = LARGE_CACTUS[self.type]
        self.width = self.image.get_width()
  
    def update(self):
        self.cactus_rect.x -= self.game_speed
        if self.cactus_rect.x < -self.width:
            self.cactus_rect.x = SCREEN_WIDTH + random.randint(5,50)
            self.cactus_rect.y = 300
            self.type = random.randint(0, 2)
            self.image = LARGE_CACTUS[self.type]
       

    def draw(self,screen):
        screen.blit(self.image,(self.cactus_rect.x ,self.cactus_rect.y))
        
