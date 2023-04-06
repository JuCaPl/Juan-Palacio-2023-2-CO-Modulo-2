
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD,SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self,x=0,y = 0):
        super().__init__(SHIELD,SHIELD_TYPE)
        self.rect.y = y
        self.rect.x = x