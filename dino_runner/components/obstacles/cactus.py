
import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
  def __init__(self, image, y_pos = 325):
    #self.type = random.randint(0, 2)
    # puede funcionar sin el self.type y que solo pida la imagen
    super().__init__(image)
    self.rect.y = y_pos
   