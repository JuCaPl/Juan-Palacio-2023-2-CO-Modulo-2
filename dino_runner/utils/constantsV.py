import os
import pygame

pygame.init()
# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

JUMPING_V = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump_V.png"))