import pygame


from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_STYLE,GMOV,REST,PLAY
from dino_runner.utils.constants import DEFAULT_TYPE,HEART,HEARTR,SHIELD_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


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
        self.menu = Menu(self.screen)  # Acomodar esto
        self.running = False
        self.death_count = 0
        self.max_death = 0
        self.score = 0
        self.max_score = 0
        self.power_up_manager = PowerUpManager()
        self.color = (94, 94, 94)
        self.color_time = 0
        self.lives = 8
        
       
    

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()      
        pygame.display.quit()
        pygame.quit()
            

    def run(self):
        self.reset_game()
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
        self.player.update(user_input)      # dino
        self.cloud.update()                 # nubes
        self.Obs_Manager.update(self)       # Cactus
        self.power_up_manager.update(self)  # powers
        self.update_score()                 # puntaje


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.Obs_Manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_lives()
        
        pygame.display.update()
        pygame.display.flip() #Actualiza la superficie de visualización completa a la pantalla 
        

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

        self.power_up_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.player.draw(self.screen)
        self.Obs_Manager.draw(self.screen)
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.death_count == 0:
          self.menu.draw(self.screen,"Press any key to start...",60,700,100)
          self.screen.blit(PLAY, (650, 200))
        else:
            self.menu.update_message(self.count())
            self.screen.blit(GMOV, (610, 50))
            self.screen.blit(REST, (280, 50))
        self.menu.update(self)
        
        
    def update_score(self):
        self.score += 1
        # empieza a aumentar la velocidad desde los 100 puntos y asi sucesivamente si su residuo es 0
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 5
        
        if self.score > self.max_score:
            self.max_score = self.score
            if self.max_score % 100 == 0:
                self.color_time = 10

    def draw_score(self): 
        self.font = pygame.font.Font(FONT_STYLE, 32)   
        texto = 'Score:            '+ str(self.score).zfill(6)
        self.text = self.font.render(texto, True,(94, 94, 94))
        #self.text = self.font.render('Points: '+ str(self.points), True,(96,96,96))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (955,80)
        self.screen.blit(self.text, self.text_rect)
        
        
        textoM = 'High score: '+ str(self.max_score).zfill(6)
        if self.max_score % 100 == 0:
            self.color_time = 10
        elif self.color_time > 0:
            self.color = (0,255,0) # color por el que cambia
            self.color_time -=1
        else:
            self.color = (94, 94, 94)
        self.textM = self.font.render(textoM, True,self.color)
        self.textM_rect = self.textM.get_rect()
        self.textM_rect.center = (955,50)
        self.screen.blit(self.textM, self.textM_rect)

        
        

    
    def count(self):
        
        self.font = pygame.font.Font(FONT_STYLE, 35)
        textoDeth ='Total Death:   '+ str(self.death_count).zfill(6)
        textoAct = 'Your Score:   '+ str(self.score).zfill(6)
        textoMax = 'High score:   '+ str(self.max_score).zfill(6)

        self.text = self.font.render('Press any key to continue playing', True,(94, 94, 94 ))
        self.textAct = self.font.render(textoAct, True,(94, 94, 94))
        self.textMax = self.font.render(textoMax, True,(94, 94, 94 ))
        self.textDeth = self.font.render(textoDeth, True,(94, 94, 94 ))
        
        self.text_rect_message = self.text.get_rect()
        self.text_rect_actual = self.textAct.get_rect()
        self.text_rect_maximo = self.textMax.get_rect()
        self.text_rect_death = self.textDeth.get_rect()

        self.text_rect_message.center = (320,200)
        self.text_rect_actual.center = (800,150)
        self.text_rect_maximo.center = (800,220)
        self.text_rect_death.center = (800,290)

        self.screen.blit(self.text,self.text_rect_message)
        self.screen.blit(self.textDeth, self.text_rect_death)
        self.screen.blit(self.textAct, self.text_rect_actual)
        self.screen.blit(self.textMax, self.text_rect_maximo)
    
    def reset_game(self):
        self.game_speed = self.GAME_SPEED
        self.score = 0
        self.player.reset()
        self.Obs_Manager.reset()
        self.power_up_manager.reset()
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000,2)

            if time_to_show >=0:
                    if self.player.type == SHIELD_TYPE:
                         self.menu.draw(self.screen, f'Shield enabled for', 34, 550, 50)
                         self.menu.draw(self.screen, f'({time_to_show})  seconds',34, 550,100)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    


    def draw_lives(self):
        if self.death_count > self.max_death:
            self.max_death = self.death_count


        for i in range(self.lives):
            self.screen.blit(HEARTR, (i*35 + 820,10))

        for i in range(self.max_death):
            self.screen.blit(HEART, (i*35+820,10))

        pygame.display.update()  
        
        if self.death_count > 7:
            self.playing=False
            pygame.display.quit()
            pygame.quit()
        
    
  
            



 