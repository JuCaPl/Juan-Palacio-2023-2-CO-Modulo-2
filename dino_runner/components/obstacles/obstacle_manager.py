import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS,SHIELD_TYPE,BOMB_TYPE,PLAY,SCREEN_HEIGHT, SCREEN_WIDTH,EXPLO

class ObstacleManager:
    sound = pygame.mixer.Sound('sounds\explosion-8-bit.wav')
    def __init__(self):
        self.obstacles = []
        

    def generate_obstacle(self):
        obs_imges = SMALL_CACTUS + LARGE_CACTUS 
        obs_img = random.choice(obs_imges)
        if obs_img in LARGE_CACTUS:                                  #SIMPLIFICAR CONDICIONES
            obstacle = Cactus(obs_img, y_pos=300)
            
        else:
            if random.randint(0,1):
                obstacle = Cactus(obs_img)
            else:
                # imprime aleatoriamnete alto, medio y bajo
                birdpos=[230,270,300]
                y_pos = random.choice(birdpos)
                obstacle = Bird(y_pos)
                print('bird')
        
        return obstacle
        

    def update(self, game):
        # Este método actualiza la posición y el estado de los obstáculos en la pantalla. 
        # Si la lista de obstáculos está vacía, genera un nuevo obstáculo llamando al método 
        if len(self.obstacles) == 0:
            #llama al metodo !abajo
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)
        
        if game.player.type == BOMB_TYPE:
                    self.sound.play()
                    pygame.time.delay(1000)
                    #game.playing=False
                    pygame.display.quit()
                    pygame.quit()
                    print("HAT")
       
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                    
                if game.player.type == SHIELD_TYPE:
                    print("sen")
                    self.obstacles.remove(obstacle)
                
                else:
                    print('Cols') # para ver si funciona la colision
                    #pygame.time.delay(1000)
                    game.death_count += 1
                    game.playing = False
                    break
                    

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        self.obstacles = []

