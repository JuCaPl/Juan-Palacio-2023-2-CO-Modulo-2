import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS,BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        obs_imges = SMALL_CACTUS + LARGE_CACTUS 
        obs_img = random.choice(obs_imges)
        if obs_img in LARGE_CACTUS:
            obstacle = Cactus(obs_img, y_pos=300)
        else:
            if random.randint(0,1):
                obstacle = Cactus(obs_img)
            else:
                # imprime aleatoriamnete alto, medio y bajo
                birdpos=[250,270,300]
                y_pos = random.choice(birdpos)
                obstacle = Bird(y_pos)
                print('bird')
        return obstacle
        

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print('Cols')  # para ver si funciona la colision
                #pygame.time.delay(1000)
                game.playin = False
                break

    def draw(self,screen):
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)

