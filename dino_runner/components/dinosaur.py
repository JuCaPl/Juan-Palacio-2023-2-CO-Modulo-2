import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING,JUMPING,DUCKING,DEFAULT_TYPE,SHIELD_TYPE,RUNNING_SHIELD,JUMPING_SHIELD,DUCKING_SHIELD


RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, 'bomb': RUNNING}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD , 'bomb': JUMPING}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, 'bomb': DUCKING}



class Dinosaur():
    x_pos= 80
    y_pos= 310
    JUMP_SPEED = 8.5
    y_duck = 340
    jump_sound = pygame.mixer.Sound('sounds\jump01.wav')
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED
        self.has_power_up = False
        self.power_time_up = 0
        
    

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
            self.jump_sound.play()
        elif user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
       
    def run(self):
        self.image = RUN_IMG[self.type][0] if self.step_index < 5 else RUN_IMG[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type] 
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.y_pos
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self):
        self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos 
        self.dino_rect.y = self.y_duck  
        self.step_index += 1

    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x ,self.dino_rect.y))
       
    def reset(self):
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED
  
    
   
                
