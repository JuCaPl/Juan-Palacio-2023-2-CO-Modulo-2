import pygame

from dino_runner.utils.constants import FONT_STYLE,SCREEN_HEIGHT,SCREEN_WIDTH

class Menu:
    #HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2
    #HALF_SCREEN_WIDTH = SCREEN_WIDTH //2

    def __init__(self, screen):
       screen.fill((255,255,255))
       self.font = pygame.font.Font(FONT_STYLE,60)
       
       
    
    def update(self,game):
        pygame.display.update() # actualiza la ventana para mostrar los cambios
        self.handle_events_on_menu(game)

    def draw(self,screen,message,size,x=0,y=0):
       self.font = pygame.font.Font(FONT_STYLE,size)
       self.text = self.font.render(message,True,(94, 94, 94))
       self.text_rect = self.text.get_rect()
       self.text_rect.center = (x,y)
       screen.blit(self.text, self.text_rect)
    
    def reset_screen_color(self,screen):
       screen.fill((255,255,255))
    
    def handle_events_on_menu(self, game):
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             game.running = False
             game.playing = False
          elif event.type == pygame.KEYUP:
             game.run()
    
    def update_message(self,message):
       self.font = pygame.font.Font(FONT_STYLE,60)
       self.text = self.font.render(message,True,(0,0,0))
       self.text_rect = self.text.get_rect()
       self.text_rect.center = (0,0)
 

