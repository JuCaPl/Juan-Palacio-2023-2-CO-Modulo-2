import pygame


from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.Obs_Manager = ObstacleManager()
        self.menu = Menu("Press any key to start...",self.screen)
        self.running = False
        self.death_count = 0
        self.score = 0
        self.font = pygame.font.Font(FONT_STYLE, 30)
    
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
            

    def run(self):
        self.game_speed = self.GAME_SPEED
        self.score = 0
        self.player.reset_dino()
        self.Obs_Manager.reset_obs()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

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
        self.Obs_Manager.update(self)
           #self.Cols.update()
        self.update_score()
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
          #self.player.cols(self.screen)
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.Obs_Manager.draw(self.screen)
          #self.Cols.draw(self.screen)
        self.draw_score()
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
    
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)

        if self.death_count == 0:
          self.menu.draw(self.screen)
        else:
            self.menu.update_message('new message')
            self.menu.draw(self.screen)
        self.menu.update(self)
        
    def update_score(self):
        self.score += 1
        # empieza a aumentar la velocidad desde los 100 puntos y asi sucesivamente si su residuo es 0
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5

    def draw_score(self):    
        texto = 'Points: '+ str(self.score).zfill(6)
        self.text = self.font.render(texto, True,(96,96,96))
        #self.text = self.font.render('Points: '+ str(self.points), True,(96,96,96))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (980,30)
        self.screen.blit(self.text, self.text_rect)
    


 