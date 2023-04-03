import pygame


from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.Cactus = Cactus()
        self.bird = Bird()
        self.Cactus_l = Obstacle()
        self.points = 0
        self.font = pygame.font.Font('fonts/PIX-L.ttf', 30)
        

        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
          # dino
        self.player.update(user_input)
          # nubes
        self.cloud.update()
          # Cactus
        self.Cactus.update()
        self.Cactus_l.update()
        self.bird.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.cols(self.screen)
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.Cactus.draw(self.screen)
        self.Cactus_l.draw(self.screen)
        self.bird.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()
        
        
      
       
     


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    
    def score(self):

        self.points += 1
        # empieza a aumentar la velocidad desde los 100 puntos y asi sucesivamente si su residuo es 0
        if self.points % 100 == 0:
            self.game_speed += 1
        
        texto = 'Points: '+ str(self.points).zfill(6)
        self.text = self.font.render(texto, True,(96,96,96))
        #self.text = self.font.render('Points: '+ str(self.points), True,(96,96,96))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (980,30)
        self.screen.blit(self.text, self.text_rect)